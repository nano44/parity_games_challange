#!/usr/bin/env python3
"""L-RED successor 32 (R131): family against CONJECTURE TIED-RB (L-SI box 50 §6). Base = span/mkrw.py K m with LATE=1 (R127: one-world
mkr + late adopters v_J -> {d_J, c_J}). Gadget per J = 2..m-1:
  y_J (Even, prio 132) -> {v_J (start), z_J};   z_J (Even, prio 20) -> {a_(J+1), c_(J+1)} (start: the engine's 'best' initial choice).
The REPEAT target z_J is EVEN: every Xi-climb of z_J in the window is z_J's own switch (a_(J+1) <-> c_(J+1)), which moves its W-play too,
so no climb is tied. Found by a random gadget search on mkrw K 3 m 4 (one copy: y -> {v2, z}, z -> {a4, C3, c4}), then simplified.
Env TARGET=odd: y_J -> {v_J, o_J}, o_J (Odd, prio 22, single successor z_J): the target never switches, and its climbs are still untied.
Env ONE=1: the single-copy endgame instance first found on K 2 m 4: y (132) -> {r_2, q (start)}, q (Odd, 130) -> {d4, w1}, tau0(q) = w1.
Usage: mktied.py K m OUT.pg OUT.start"""
import sys, os, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gb
K, m, out, outs = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
with tempfile.TemporaryDirectory() as d:
    subprocess.run([sys.executable, os.path.join(HERE, "..", "span", "mkrw.py"), str(K), str(m), d + "/b.pg", d + "/b.start"],
                   env=dict(os.environ, LATE="1"), capture_output=True, check=True)
    G = gb.from_pg(d + "/b.pg", d + "/b.start")
if os.environ.get("ONE") == "1":
    G.v("y", 0, 126, ["r2", "q"]); G.start("y", "q"); G.v("q", 1, 130, ["d4", "w1"]); G.start("q", "w1")
else:
    for J in range(2, m):
        odd = os.environ.get("TARGET") == "odd"
        G.v(f"y{J}", 0, 132, [f"v{J}", f"o{J}" if odd else f"z{J}"]); G.start(f"y{J}", f"v{J}")
        G.v(f"z{J}", 0, 20, [f"a{J + 1}", f"c{J + 1}"])
        if odd: G.v(f"o{J}", 1, 22, [f"z{J}"])
G.write(out, outs); print(f"K {K} m {m} n {len(G.names)}")
