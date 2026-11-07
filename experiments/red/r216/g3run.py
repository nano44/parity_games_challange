#!/usr/bin/env python3
"""L-RED 53 R216: real-game check of an IDEAL genome: N5 (n5v.py mode spec @ claude/l-new acdbd28b, env WT) on Gamma3(G) (box189
gamma3.build, pads K, pe, pb, m), from S3. P-N5-REACH (not landed) predicts iterations = IDEAL T + 3. Usage: g3run.py g.json [mode]"""
import sys, os, json, time
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box189"), os.path.join(WT, "experiments/harness")]
import n5v, gamma3
f = sys.argv[1]; m = sys.argv[2] if len(sys.argv) > 2 else "spec"; t0 = time.time()
g = gamma3.build(json.load(open(f)), {"K", "pe", "pb", "m"})[0]; st, fb, E = n5v.run(g, m, cap=5000)
print(f"{os.path.basename(f)}: Gamma3 n {g.n} N5 mode {m} iterations {len(st) - 1} fallbacks {fb} ({time.time() - t0:.0f} s)", flush=True)
