#!/usr/bin/env python3
"""Box 17 cross-check: box17.py (n5b) against L-SI's tools (lsi_side.py, separate process) on GAME [START]. Compares the state
sequence, fallback flags, sigma-bar, runs, REL segments, per-segment SEG-COUNT excess, max SEG, max L-WAVE' gap and f per phase.
Prints 'XCHECK name OK ...' or 'XCHECK name MISMATCH field ...'. Usage: xcheck.py GAME [START] ..."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import box17 as B
import pg  # noqa: E402  (experiments/harness via n5b's path)


def mine(path, spath):
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); e = B.Eng(g)
    s, t = map(list, e.start())
    if spath:
        for line in open(spath):
            p = line.split()
            if p and p[0] in ("SIGMA0", "TAU0"):
                tgt = s if p[0] == "SIGMA0" else t
                for x in p[1:]:
                    a, b = map(int, x.split(":")); tgt[a] = b
    R = B.trajectory(e, (tuple(s), tuple(t))); n = g.n
    rr, segs, exc, f = [], [], [], []
    for i, j in B.phases(R):
        f.append((i, j, sum(R[k]["fb"] for k in range(i, j))))
        for a, b in B.runs_of(R, i, j):
            rr.append((a, b))
            for x, y, RO in B.segments(e, R, a, b):
                segs.append((x, y))
                if y > x:
                    sw = {v for k in range(x, y) for v in e.Q if R[k]["s"][v] != R[k + 1]["s"][v]}
                    exc.append((x, y, (y - x) - len(sw)))
    an = B.analyse(e, R)
    allseg = max([len(B.segments(e, R, a, b)) for a, b in rr], default=0)
    return dict(n=n, states=[[[R[k]["s"][v] for v in range(n) if g.owner[v] == 0], [R[k]["t"][v] for v in range(n) if g.owner[v] == 1]] for k in range(len(R))],
                fb=[R[k]["fb"] for k in range(len(R) - 1)], sb=[[x if g.owner[v] == 1 else None for v, x in enumerate(R[k]["sb"])] for k in range(len(R))],
                runs=rr, segs=segs, exc=exc, segmax=allseg, lwgap_minus_n1=(an["gap"] - (n - 1)) if an["gaps"] else -10 ** 6, f=f), an


def main():
    args = sys.argv[1:]; i = 0
    while i < len(args):
        gp = args[i]; sp = args[i + 1] if i + 1 < len(args) and args[i + 1].endswith(".start") else None; i += 2 if sp else 1
        L = json.loads(subprocess.run([sys.executable, os.path.join(HERE, "lsi_side.py"), gp] + ([sp] if sp else []), capture_output=True, text=True, check=True).stdout)
        M, an = mine(gp, sp)
        L["sb"] = [[x if M["sb"][k][v] is not None else None for v, x in enumerate(row)] for k, row in enumerate(L["sb"])] if len(L["sb"]) == len(M["sb"]) else L["sb"]
        bad = [k for k in ("states", "fb", "sb", "runs", "segs", "exc", "segmax", "lwgap_minus_n1", "f") if json.loads(json.dumps(M[k])) != L[k]]
        name = os.path.basename(gp)
        if bad:
            print("XCHECK", name, "MISMATCH", bad, {k: (str(M[k])[:200], str(L[k])[:200]) for k in bad[:2]})
        else:
            print("XCHECK", name, "OK", "states", len(M["states"]), "segs", len(M["segs"]), "max_exc", max([x[2] for x in M["exc"]], default=None),
                  "segmax", M["segmax"], "lw'gap-(n-1)", M["lwgap_minus_n1"], "fmax", max([x[2] for x in M["f"]], default=None), "n", M["n"])
        sys.stdout.flush()


if __name__ == "__main__":
    main()
