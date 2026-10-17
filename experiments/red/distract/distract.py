#!/usr/bin/env python3
"""L-RED (2026-10-16, produced on Opus 5.5): van Dijk's "distractingly nice long path" recipe against DTL
("Solving parity games, very slowly", DOI 10.1007/978-3-031-75778-5_21, p.15, section 6 item 7; quoted by the Lead from
L-LIT's opened copy). Prose only in the source; this is one concrete reading of it.
Game: a hard region H (tc+ N from Oink's generator, priorities shifted above the path), a path x_1..x_L whose priorities
all have player p's parity (p "dominates" it), x_L entering H, and a small p-dominion D of LOW priority (chosen last).
Usage: distract.py TCPLUS_BIN N L p MODE > out.pg
 MODE: chain[-high][-back]  path owned by p, x_i -> x_{i+1} only, priorities increasing along the path (so x_1 dies last
             in pruning and is the argmax); -high puts the path ABOVE H (H shifted below); -back adds x_1 as an extra
             successor of every p-owned vertex of H; -qwin makes x_L enter only opponent vertices of H won by the
             opponent, and gives back edges only to p-owned vertices the opponent wins (no winner changes); D is disconnected
       own   path owned by p, x_i -> x_{i+1} and x_i -> D (p can leave to D anywhere)
       opp   path owned by the opponent, x_i -> x_{i+1} only; D reachable only from x_1 (entry choice of p)
       mix   alternate owners; the p-owned ones also edge to D
 Entry: x_L -> every opponent-owned vertex of H; H's vertices of the opponent also get an edge back to x_1 (a "lure")."""
import sys, subprocess


def read_pg(text):
    vs = []
    for line in text.splitlines():
        line = line.strip().rstrip(";")
        if not line or line.startswith("parity") or line.startswith("start"): continue
        parts = line.split()
        v, pr, ow = int(parts[0]), int(parts[1]), int(parts[2])
        succ = [int(x) for x in parts[3].rstrip(";").split(",")]
        vs.append((v, pr, ow, succ))
    return vs


def build(tcbin, N, L, p, mode):
    H = read_pg(subprocess.run([tcbin, str(N)], capture_output=True, text=True, check=True).stdout)
    q = 1 - p
    high = "high" in mode
    off = 2 * L + 4 if not high else 4                # even shift keeps every parity
    poff = 2 if not high else max(pr for _, pr, _, _ in H) + 4 + (max(pr for _, pr, _, _ in H) % 2)
    out = []                                          # (id, pr, owner, succ)
    nH = len(H)
    d0, d1 = nH, nH + 1                               # D: two p-owned vertices, priority p (lowest of p's parity)
    X = [nH + 2 + i for i in range(L)]
    oppH = [v for v, pr, ow, s in H if ow == q]
    win = None
    if "qwin" in mode:                                # -qwin: x_L enters only opponent vertices the OPPONENT wins (path losing for p)
        import tempfile, os
        f = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False); f.write(subprocess.run([tcbin, str(N)], capture_output=True, text=True).stdout); f.close()
        oink = os.path.join(os.path.dirname(tcbin), "oink")
        subprocess.run([oink, "--dtl", f.name, f.name + ".sol"], capture_output=True)
        win = {}
        for line in open(f.name + ".sol"):
            t = line.strip().rstrip(";").split()
            if len(t) >= 2 and t[0].isdigit(): win[int(t[0])] = int(t[1])
        os.unlink(f.name); os.unlink(f.name + ".sol")
        oppH = [v for v in oppH if win.get(v) == q]
    for v, pr, ow, s in H:
        s = list(s)
        if mode.startswith("chain"):
            if "back" in mode and ow == p and L and (win is None or win.get(v) == q): s.append(X[0])
        elif ow == q and L: s.append(X[0])
        out.append((v, pr + off, ow, s))
    out.append((d0, p, p, [d1])); out.append((d1, p + 2, p, [d0]))
    for i, x in enumerate(X):
        pr = 2 * (i + 1) + p + poff
        nxt = [X[i + 1]] if i + 1 < L else oppH
        if mode.startswith("chain"):
            ow = p; succ = nxt
        elif mode == "own":
            ow = p; succ = nxt + [d0]
        elif mode == "opp":
            ow = q; succ = nxt + ([d0] if i == 0 else [])
            if i == 0: ow = p
        else:
            ow = p if i % 2 == 0 else q; succ = nxt + ([d0] if ow == p else [])
        out.append((x, pr, ow, succ))
    lines = [f"parity {len(out) - 1};"] + [f"{v} {pr} {ow} {','.join(map(str, s))};" for v, pr, ow, s in sorted(out)]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    tcbin, N, L, p, mode = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    sys.stdout.write(build(tcbin, N, L, p, mode))
