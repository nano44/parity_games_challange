#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: MEMBERSHIP of a genome in RESULTS R104's class (the IDEAL genomes with an acyclic Xi-graph), clause by clause,
against the definition quoted by this script from docs/red/P-N5-REALIZE.md par. 2 (R104's packet; a file of trunk, read through git).

Clauses (each a must-0 counter; the text of every clause is printed from the packet with --quote):
  c1 movers/levels/options : N movers, lev(x) in {0..d-1} with every level 0..d-1 used, every mover has >= 1 option; M = sum of degrees
  c2 GRADED                : wt(x, k) is a mover of level lev(x) - 1 if lev(x) >= 1, and -1 (none) if lev(x) = 0
  c3 Xi-target             : xt(x, k) is a mover or -1 (the exit X)
  c4 beta-id               : b(x, k) is a bijection of the options onto 0..M-1
  c5 gate index            : gate(x, k) is a bijection of the options onto 0..M-1
  c6 rank / parity         : br is a bijection of 0..M-1 onto 0..M-1; bp(b) in {0, 1}
  c7 start                 : an option per mover
  c8 IDEAL-ACYC            : the Xi-graph (x -> xt(x, k), xt != X) is acyclic, self-loops count as cycles
Descriptive: deg (set of degrees), samew (#movers with two options on one W-target), allexit (#movers with every Xi-target = X),
odd (#options with bp = 1).
--norm OUTDIR writes G with its gate numbers replaced by their rank 0..M-1 (order kept: no key comparison changes) as <name>.json.
--ctrl i (1..8): the genome is first damaged so that clause i fails (must fire).
Usage: b6member.py [--quote PACKET.md] [--norm OUTDIR] [--ctrl i] G.json ..."""
import sys, os, json, hashlib, copy


def clauses(G):
    v = {f"c{i}": 0 for i in range(1, 9)}
    N = G.get("N")
    lev, opts, gate, br, bp, start = (G.get(k) for k in ("lev", "opts", "gate", "br", "bp", "start"))
    if not (isinstance(N, int) and N >= 1 and isinstance(lev, list) and len(lev) == N and isinstance(opts, list) and len(opts) == N):
        v["c1"] = 1
        return v, {}
    d = max(lev) + 1
    if set(lev) != set(range(d)) or any(len(o) < 1 for o in opts):
        v["c1"] += 1
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    M = len(O)
    for (x, k) in O:
        wt, xt, b = opts[x][k]
        if lev[x] == 0:
            v["c2"] += int(wt != -1)
        else:
            v["c2"] += int(not (isinstance(wt, int) and 0 <= wt < N and lev[wt] == lev[x] - 1))
        v["c3"] += int(not (isinstance(xt, int) and -1 <= xt < N))
    v["c4"] += int(sorted(opts[x][k][2] for (x, k) in O) != list(range(M)))
    okg = isinstance(gate, list) and len(gate) == N and all(len(gate[x]) == len(opts[x]) for x in range(N))
    v["c5"] += int(not okg or sorted(gate[x][k] for (x, k) in O) != list(range(M)))
    v["c6"] += int(not (isinstance(br, list) and sorted(br) == list(range(M)))) + int(not (isinstance(bp, list) and len(bp) == M and all(p in (0, 1) for p in bp)))
    v["c7"] += int(not (isinstance(start, list) and len(start) == N and all(isinstance(start[x], int) and 0 <= start[x] < len(opts[x]) for x in range(N))))
    col = [0] * N
    cyc = 0
    for r in range(N):                       # iterative DFS on the Xi-graph
        if col[r]:
            continue
        st = [(r, 0)]
        col[r] = 1
        while st:
            x, i = st.pop()
            if i < len(opts[x]):
                st.append((x, i + 1))
                y = opts[x][i][1]
                if isinstance(y, int) and 0 <= y < N:
                    if col[y] == 1:
                        cyc += 1
                    elif col[y] == 0:
                        col[y] = 1
                        st.append((y, 0))
            else:
                col[x] = 2
    v["c8"] += cyc
    desc = {"N": N, "M": M, "d": d, "deg": sorted({len(o) for o in opts}),
            "samew": sum(1 for x in range(N) if len(opts[x]) >= 2 and len({o[0] for o in opts[x]}) < len(opts[x])),
            "allexit": sum(1 for x in range(N) if all(o[1] == -1 for o in opts[x])),
            "odd": sum(1 for p in bp if p == 1) if isinstance(bp, list) else -1}
    return v, desc


def normalise(G):
    H = copy.deepcopy(G)
    vals = sorted(g for row in G["gate"] for g in row)
    assert len(set(vals)) == len(vals), "gate numbers not distinct"
    rk = {g: i for i, g in enumerate(vals)}
    H["gate"] = [[rk[g] for g in row] for row in G["gate"]]
    return H


def damage(G, i):
    H = copy.deepcopy(G)
    N = H["N"]
    top = max(range(N), key=lambda x: H["lev"][x])
    if i == 1:
        H["lev"][top] += 2                                  # a level is skipped
    elif i == 2:
        H["opts"][top][0][0] = top                          # a W-target of the same level
    elif i == 3:
        H["opts"][0][0][1] = N + 3                          # a Xi-target that is no mover
    elif i == 4:
        H["opts"][0][0][2] = H["opts"][0][1][2]             # two options with one beta-id
    elif i == 5:
        H["gate"][0][0] = H["gate"][0][1]                   # two options with one gate index
    elif i == 6:
        H["bp"][0] = 2                                      # a parity outside {0, 1}
    elif i == 7:
        H["start"][0] = len(H["opts"][0])                   # a start that is no option
    elif i == 8:
        H["opts"][0][0][1] = 0                              # a Xi self-loop
    return H


if __name__ == "__main__":
    a = sys.argv[1:]
    norm = ctrl = None
    if a and a[0] == "--quote":
        txt = open(a[1], encoding="utf-8").read()
        lines = txt.split("\n")
        i0 = next(i for i, l in enumerate(lines) if l.startswith("## 2. The IDEAL model"))
        i1 = next(i for i in range(i0 + 1, len(lines)) if lines[i].startswith("- Values under a state"))
        print(f"[Q {a[1].split('/')[-1]} sha1 {hashlib.sha1(txt.encode('utf-8')).hexdigest()} l. {i0 + 1}-{i1}]")
        for l in lines[i0:i1]:
            print("  «" + l + "»")
        a = a[2:]
    if a and a[0] == "--norm":
        norm = a[1]
        os.makedirs(norm, exist_ok=True)
        a = a[2:]
    if a and a[0] == "--ctrl":
        ctrl = int(a[1])
        a = a[2:]
    for fn in a:
        G = json.load(open(fn))
        G = G.get("genome", G)
        raw_v, _ = clauses(G)
        H = normalise(G)
        if ctrl:
            H = damage(H, ctrl)
        v, d = clauses(H)
        name = os.path.basename(fn)
        sha = ""
        if norm and not ctrl:
            out = os.path.join(norm, name)
            json.dump(H, open(out, "w"))
            sha = " norm_sha1 " + hashlib.sha1(open(out, "rb").read()).hexdigest()
        tot = sum(v.values())
        print(f"{name} ctrl {ctrl or 0} member {int(tot == 0)} viol {tot} " + " ".join(f"{k} {v[k]}" for k in sorted(v)) +
              f" raw_c5 {raw_v['c5']} N {d.get('N')} M {d.get('M')} d {d.get('d')} deg {d.get('deg')} samew {d.get('samew')} allexit {d.get('allexit')} odd {d.get('odd')}{sha}", flush=True)
