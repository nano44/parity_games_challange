"""L-COMP box 37: glue for fast37.c (bin/fast37_w<w>, gitignored; build: gcc -O2 -DW=<w> -o bin/fast37_w<w> fast37.c, w in 1 8 16 48 96).
one(G) -> dict(T3, fb, C, Dmov, Dmov_x, rows=[((x, k), flips, lamch)]). Dmov = 1 + max over movers of #steps (Gamma3 run, states 0..T3)
at which the mover's class (Lambda, Pi & e-vertices) changes."""
import os, sys, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "box36"))
import fast36
def one(G):
    n = G["N"] + 8 * sum(len(o) for o in G["opts"]) + 10
    w = next(w for w in (1, 8, 16, 48, 96) if n <= 64 * w)
    out = subprocess.run([os.path.join(H, "bin", f"fast37_w{w}"), "one"], input=fast36.gtext(G), capture_output=True, text=True, check=True).stdout.split("\n")
    h = out[0].split(); rows = []
    for line in out[1:]:
        if line.startswith("gate"): z = line.split(); rows.append(((int(z[1]), int(z[2])), int(z[3]), int(z[4])))
    return dict(T3=int(h[1]), fb=int(h[3]), C=int(h[7]), Dmov=int(h[9]), Dmov_x=int(h[11]), rows=sorted(rows))
