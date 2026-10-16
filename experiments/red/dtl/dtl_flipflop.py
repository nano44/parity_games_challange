#!/usr/bin/env python3
"""L-RED (2026-10-16, DTL flip-flop box): instrumented DTL run built on L-COMP's independent implementation
experiments/dtl-bench/dtl_py.py (imported, not copied; its best_vertices / search_rec bodies are repeated here verbatim with
log lines added). Per search it records the pruning rounds of every best_vertices call (candidates, the threshold at which a
candidate was forgiven, the distractions), the pieces removed from R (stable Dom(V,R), the -1 cut at threshold t with the
recursed remainder, Dom(prevV) when X is empty), and every new tangle (top, vertex set, piece). Then it prints the
distraction status of every vertex per search (the flip-flop the proof lane reported) and the chain restarts per top.
Usage: dtl_flipflop.py GAME.pg [--order stable|oink] [--player 0|1] [--quiet] [--oink OINK]
Vertex labels are the input ids. --oink cross-checks the tangle and iteration counts against the pinned binary."""
import sys, os, importlib.util, re, subprocess, collections
HERE = os.path.dirname(os.path.abspath(__file__))
BENCH = os.path.join(HERE, "..", "..", "dtl-bench")
sys.path.insert(0, os.path.join(HERE, "..", "..", "harness")); sys.path.insert(0, BENCH)
import pg
spec = importlib.util.spec_from_file_location("dtl_py", os.path.join(BENCH, "dtl_py.py")); dtl_py = importlib.util.module_from_spec(spec); spec.loader.exec_module(dtl_py)


class TraceDTL(dtl_py.DTL):
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.searches = []          # one record per search
        self.cur = None             # current search record
        self.piece_stack = []       # current piece records (one per recursion depth)

    # ---- hooks
    def new_piece(self, kind, depth, **kw):
        p = dict(kind=kind, depth=depth, rounds=[], tangles=[], **kw); self.cur["pieces"].append(p); return p

    def extractTangles(self, top, R):
        before = len(self.tv); d0 = self.dominions
        made = super().extractTangles(top, R)
        for t in range(before, len(self.tv)):
            vs = frozenset(v for v, _ in self.tv[t]); rec = (top, vs, len(self.cur["pieces"]) - 1)
            self.cur["tangles"].append(rec); self.cur["pieces"][-1]["tangles"].append(rec)
        if self.dominions > d0: self.cur["dominions"] += self.dominions - d0
        return made

    def attractTangle(self, t, p, R, Z, Gx, maxpr):
        ok = super().attractTangle(t, p, R, Z, Gx, maxpr)
        if ok:
            self.cur.setdefault("fired", []).append((t, len(self.cur["pieces"]), self.phase))
        return ok

    def best_vertices(self, V, R, p):          # dtl_py.best_vertices verbatim + logging into self.cur["bv"]
        log = dict(R=frozenset(R), rounds=[]); self.cur["bv"].append(log); self.phase = "prune"
        V.clear(); V.update(v for v in R if self.pr[v] % 2 == p)
        if not V:
            log["result"] = 0; return 0
        while True:
            prevV = set(V)
            Z = set(); CurR = set(R); regions = {}
            for top in range(self.n - 1, -1, -1):
                if top not in V or top in Z:
                    continue
                CurZ = {top}; self.Q = [top]
                self.tattr(p, CurZ, CurR, CurR, self.pr[top], CurR)
                regions[top] = frozenset(CurZ)
                Z |= CurZ
            cand = [v for v in sorted(V, reverse=True) if not self.attracts(p, v, Z, R)]
            rnd = dict(V=frozenset(V), regions=regions, cands=list(cand), forgiven={}, distractions=[]); log["rounds"].append(rnd)
            if not cand:
                log["result"] = 1; log["V"] = frozenset(V); return 1
            for t in [0] + [q for q in self.prios if q > 0 and q <= self.maxpr]:
                self.Q = sorted(Z)
                self.tattr(p, Z, R, R, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if self.pr[u] <= t:
                        keep += cand[i:]; break
                    if not self.attracts(p, u, Z, R):
                        keep.append(u)
                    else:
                        rnd["forgiven"][u] = t
                cand = keep
            rnd["distractions"] = list(cand)
            V -= set(cand)
            if not cand:
                log["result"] = 1; log["V"] = frozenset(V); return 1
            if not V:
                V.clear(); V.update(prevV)
                log["result"] = -1; log["V"] = frozenset(V); return -1

    def search_rec(self, R, p, depth):         # dtl_py.search_rec verbatim + piece logging
        X = set()
        while True:
            V = set()
            res = self.best_vertices(V, R, p)
            bv = self.cur["bv"][-1]; bv["depth"] = depth
            if res == 0:
                return
            if res == 1:
                piece = self.new_piece("stable", depth, V=frozenset(V), bv=bv)
                self.phase = "sptl"
                while self.sptl(V, set(R), p):
                    pass
                self.phase = "dom"
                R0 = set(R); self.dom(V, R, X, p); piece["removed"] = frozenset(R0 - R)
                continue
            t = 0; Z = set(); self.Q = []
            for v in range(self.n):
                if v not in R:
                    continue
                if self.pr[v] > t:
                    if self.Q:
                        break
                    t = self.pr[v]
                if self.attracts(p, v, X, R):
                    Z.add(v); self.str[v] = -1; self.Q.append(v)
            if self.Q:
                piece = self.new_piece("cut", depth, V=frozenset(V), bv=bv, t=t, seeds=frozenset(Z))
                self.phase = "cut"
                self.tattr(p, Z, R, R, t, R)
                piece["attracted"] = frozenset(Z)
                for u in range(self.n - 1, -1, -1):
                    if self.pr[u] < t:
                        break
                    if u in Z and self.pr[u] == t:
                        X.add(u); self.Q.append(u)
                while self.Q:
                    u = self.Q.pop(); Z.discard(u)
                    self.attractVertices(1 - p, u, Z, X, Z, t)
                X |= Z
                piece["removed"] = frozenset(piece["attracted"] - Z); piece["recursed"] = frozenset(Z)
                self.search_rec(Z, p, depth + 1)
            else:
                piece = self.new_piece("domfirst", depth, V=frozenset(V), bv=bv)
                self.phase = "dom"
                R0 = set(R); self.dom(V, R, X, p); piece["removed"] = frozenset(R0 - R)

    def search(self, p):
        self.cur = dict(player=p, index=len(self.searches), G=frozenset(self.G), pieces=[], bv=[], tangles=[], dominions=0, fired=[])
        self.searches.append(self.cur); self.phase = "ext"
        return super().search(p)


def load(path, order="oink"):
    g = pg.read(path)
    if order == "oink":
        from stdsort import oink_order
        idx = oink_order(g.prio)
    else:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v))
    new = {v: i for i, v in enumerate(idx)}
    d = TraceDTL([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], False, ins_desc=(order == "oink"))
    if order == "oink":
        dtl_py.TV_SORTED = True; dtl_py.PEARCE = True
    sys.setrecursionlimit(100000)
    d.run()
    d.idx = idx; d.g = g
    return d


def report(d, player=None, quiet=False):
    L = lambda v: str(d.idx[v])                       # input id
    S = lambda s: "{" + ",".join(sorted((L(v) for v in s), key=int)) + "}"
    pr = lambda v: d.pr[v]
    print(f"n={d.n} tangles={d.tangles} dominions={d.dominions} iterations={d.iterations}")
    for s in d.searches:
        if player is not None and s["player"] != player: continue
        print(f"\n== search {s['index']} player {s['player']} |G|={len(s['G'])} tangles {len(s['tangles'])} dominions {s['dominions']}")
        for i, pc in enumerate(s["pieces"]):
            bv = pc["bv"]
            if not quiet:
                for r_i, rnd in enumerate(bv["rounds"]):
                    print(f"  piece {i} d{pc['depth']} round {r_i}: V={S(rnd['V'])} cands={S(rnd['cands'])} forgiven={{{', '.join(f'{L(u)}@{t}' for u, t in rnd['forgiven'].items())}}} distractions={S(rnd['distractions'])}")
            head = f"  piece {i} d{pc['depth']} {pc['kind']}"
            if pc["kind"] == "cut": head += f" t={pc['t']} seeds={S(pc['seeds'])} toX={S(pc['removed'])} recursed={S(pc['recursed'])}"
            else: head += f" V={S(pc['V'])} removed={S(pc['removed'])}"
            print(head)
            for top, vs, _ in pc["tangles"]:
                print(f"    new tangle top {L(top)}(pr {pr(top)}) {S(vs)}")
    # distraction status per vertex in the FIRST best_vertices call (depth 0, piece 0) of each search, per player
    for p in (0, 1):
        ss = [s for s in d.searches if s["player"] == p and s["bv"]]
        if len(ss) < 2: continue
        print(f"\n== player {p}: status of each own-parity vertex in the first best_vertices call per search (V = kept, Dk = distraction at round k, '.' = not in G)")
        verts = sorted({v for s in ss for v in s["bv"][0]["R"] if pr(v) % 2 == p}, key=lambda v: (-pr(v), v))
        rows = []
        for v in verts:
            row = []
            for s in ss:
                bv = s["bv"][0]
                if v not in bv["R"]: row.append("."); continue
                st = "V"
                for k, rnd in enumerate(bv["rounds"]):
                    if v in rnd["distractions"]: st = f"D{k+1}"; break
                row.append(st)
            rows.append((v, row))
        for v, row in rows:
            flips = sum(1 for a, b in zip(row, row[1:]) if a != b and "." not in (a, b))
            print(f"  v{L(v):>4} pr{pr(v):>3} {'E' if d.ow[v]==0 else 'O'}: {' '.join(f'{x:>2}' for x in row)}   flips {flips}")
        print("  first-call result per search: " + " ".join(f"{s['bv'][0]['result']:>2}" for s in ss))
        print("  pieces per search:            " + " ".join(f"{len(s['pieces']):>2}" for s in ss))
    if "--diff" in sys.argv:
        # epoch structure: for consecutive same-player searches, the first depth-0 piece index at which the piece sequence
        # differs (kind, removed set, recursed set); "=" if the whole depth-0 sequence is equal (progress only inside a recursion)
        print("\n== piece-sequence diff between consecutive same-player searches (level = first differing depth-0 piece)")
        for p in (0, 1):
            ss = [s for s in d.searches if s["player"] == p]
            out = []
            for a, b in zip(ss, ss[1:]):
                pa = [(x["kind"], x.get("removed", frozenset()), x.get("recursed", frozenset())) for x in a["pieces"] if x["depth"] == 0]
                pb = [(x["kind"], x.get("removed", frozenset()), x.get("recursed", frozenset())) for x in b["pieces"] if x["depth"] == 0]
                lvl = next((i for i, (x, y) in enumerate(zip(pa, pb)) if x != y), None)
                if lvl is None: lvl = "=" if len(pa) == len(pb) else min(len(pa), len(pb))
                out.append(f"{a['index']}->{b['index']}:{lvl}")
            if out: print(f"  player {p}: " + " ".join(out))
    if "--revisits" in sys.argv:
        # replay in the loose sense: at depth-0 piece index i, a state (kind, removed, recursed) that occurred in an EARLIER
        # non-adjacent same-player search (the piece came back to an old value after being different)
        print("\n== revisits of depth-0 piece states (index: count of returns to an earlier non-adjacent state / distinct states)")
        for p in (0, 1):
            ss = [s for s in d.searches if s["player"] == p]
            cols = {}
            for s in ss:
                for i, x in enumerate([x for x in s["pieces"] if x["depth"] == 0]):
                    cols.setdefault(i, []).append((x["kind"], x.get("removed", frozenset()), x.get("recursed", frozenset())))
            out = []
            for i, seq in sorted(cols.items()):
                rev = sum(1 for k in range(1, len(seq)) if seq[k] != seq[k-1] and seq[k] in seq[:k-1])
                out.append(f"{i}:{rev}/{len(set(seq))}")
            if out: print(f"  player {p}: " + " ".join(out))
    if "--tangles" in sys.argv:
        print("\n== tangles: id learned(search/piece) top set escapes | fired at (search:piece/phase) ...")
        born = {}
        for s in d.searches:
            for top, vs, pi in s["tangles"]:
                t = next(i for i in range(len(d.tv)) if frozenset(v for v, _ in d.tv[i]) == vs and i not in born); born[t] = (s["index"], pi, top)
        fires = collections.defaultdict(list)
        for s in d.searches:
            for t, pi, ph in s["fired"]: fires[t].append(f"{s['index']}:{pi}/{ph}")
        for t in sorted(born, key=lambda t: born[t]):
            si, pi, top = born[t]
            print(f"  T{t} {si}/{pi} top {L(top)}(pr{pr(top)}) {S(frozenset(v for v, _ in d.tv[t]))} esc={S(d.tout[t])} | " + " ".join(fires[t]))
    # chain restarts per top
    last = {}; restarts = collections.Counter(); per_top = collections.Counter()
    for s in d.searches:
        for top, vs, _ in s["tangles"]:
            per_top[top] += 1
            if top in last and not vs >= last[top]: restarts[top] += 1
            last[top] = vs
    if per_top:
        print("\n== tangles per top: " + ", ".join(f"{L(t)}(pr{pr(t)}):{c}" for t, c in sorted(per_top.items(), key=lambda x: -x[1])))
        print("== chain restarts per top: " + (", ".join(f"{L(t)}:{c}" for t, c in restarts.items()) or "none"))


if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if not x.startswith("--")]
    arg = lambda k, dflt: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else dflt
    d = load(a[0], arg("--order", "oink"))
    pl = arg("--player", None)
    report(d, None if pl is None else int(pl), "--quiet" in sys.argv)
    if "--oink" in sys.argv:
        r = subprocess.run([arg("--oink", ""), "--dtl", "--no-single", "--no-wcwc", "--no-loops", a[0]], capture_output=True, text=True)
        m = re.search(r"found (\d+) dominions and (\d+) tangles.*?solved in (\d+) iterations", r.stdout + r.stderr, re.S)
        print(f"\noink: dominions {m.group(1)} tangles {m.group(2)} iterations {m.group(3)}  python: {d.dominions} {d.tangles} {d.iterations}  {'MATCH' if (int(m.group(1)), int(m.group(2)), int(m.group(3))) == (d.dominions, d.tangles, d.iterations) else 'DIFFER'}")
