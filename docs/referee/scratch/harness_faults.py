# REFEREE throwaway: planted-fault solvers against L-COMP harness (claude/l-comp de7ea19). Usage: python3 -I harness_faults.py <checkout-of-de7ea19>
"""REFEREE fault planting against L-COMP harness at de7ea19 (compare.py + verify.py). Writes 4 faulty solvers and runs
compare.py on a few corpus games with --ref py-zlk; prints the status each fault gets."""
import sys, os, subprocess, tempfile, glob
W = sys.argv[1]; H = os.path.join(W, "experiments", "harness")
sys.path.insert(0, H); import pg, gen, zielonka, verify, compare
S = os.path.dirname(os.path.abspath(__file__))
hdr = "import sys; sys.path.insert(0, %r)\nimport pg, zielonka, verify\ng = pg.read(sys.argv[1]); win, st = zielonka.solve_with_strategy(g); win, st = list(win), list(st)\n" % H
# F1: swap one vertex's winner (vertex 1 if it exists, else 0), strategies untouched
open(S + "/f1_swap.py", "w").write(hdr + "v = 1 if g.n > 1 else 0\nwin[v] ^= 1\npg.write_sol(win, sys.argv[2], st)\n")
# F2: regions right; one winner-owned vertex's strategy redirected to a successor OUTSIDE its region (if any such vertex)
open(S + "/f2_leave.py", "w").write(hdr + """
for v in range(g.n):
    if g.owner[v] == win[v]:
        out = [w for w in set(g.succ[v]) if win[w] != win[v]]
        if out: st[v] = out[0]; break
pg.write_sol(win, sys.argv[2], st)
""")
# F3: regions right; one winner-owned vertex's strategy redirected INSIDE its region so that the opponent can close a
#     losing cycle (search for such a redirect; leave the solution correct if none exists)
open(S + "/f3_cycle.py", "w").write(hdr + """
done = False
for v in range(g.n):
    if done or g.owner[v] != win[v]: continue
    for w in sorted(set(g.succ[v])):
        if w == st[v] or win[w] != win[v]: continue
        st2 = list(st); st2[v] = w
        errs = verify.check(g, win, st2)
        if errs and all('cycle' in e for e in errs):
            st = st2; done = True; break
pg.write_sol(win, sys.argv[2], st)
""")
# F4: parity-convention flip: solve the game as MIN-parity (lowest priority seen infinitely often decides), with strategies
open(S + "/f4_minparity.py", "w").write("""import sys; sys.path.insert(0, %r)
import pg, zielonka
g = pg.read(sys.argv[1])
M = max(g.prio); M += M %% 2
h = pg.Game([M - p for p in g.prio], g.owner, g.succ)   # max-parity game equivalent to reading g as min-parity
win, st = zielonka.solve_with_strategy(h)
pg.write_sol(win, sys.argv[2], st)
""" % H)
with tempfile.TemporaryDirectory() as td:
    cdir = os.path.join(td, "c"); gen.corpus(cdir, 40, 7, 3, 12)
    files = sorted(glob.glob(cdir + "/*.pg"))
    for name in ("f1_swap", "f2_leave", "f3_cycle", "f4_minparity"):
        # pick games where the fault actually bites (f2/f3 may be no-ops on some games); report counts per status
        from collections import Counter; c = Counter(); detail = ""
        for f in files:
            g = pg.read(f); out = os.path.join(td, "o.sol")
            r = subprocess.run([sys.executable, "-I", os.path.join(S, name + ".py"), f, out], capture_output=True, text=True)
            if r.returncode: c["crash"] += 1; detail = r.stderr[-200:]; continue
            text = open(out).read()
            ref, _ = zielonka.solve_with_strategy(g)
            stt, mm, det = compare.judge(g, text, list(ref))
            c[stt] += 1
            if stt != "ok" and not detail: detail = det
        print(f"{name}: " + ", ".join(f"{k}={v}" for k, v in sorted(c.items())) + f"   e.g. {detail}")
    # end-to-end through compare.main on 5 games with the real CLI, exit codes
    few = os.path.join(td, "few"); os.makedirs(few)
    for f in files[:8]: os.link(f, os.path.join(few, os.path.basename(f)))
    for name in ("f1_swap", "f2_leave", "f3_cycle", "f4_minparity"):
        rc = compare.main([few, "--ref", "py-zlk", "--solver", f"{name}=python3 -I {S}/{name}.py {{in}} {{out}}", "--quiet"])
        print(f"compare.main exit code with {name}: {rc}")
# direct verify.check unit cases
g = pg.Game([2, 1], [0, 1], [[1], [0, 1]])   # Even owns v0 (prio 2) -> v1; Odd owns v1 (prio 1) -> v0 or v1(self-loop, odd)
win, st = zielonka.solve_with_strategy(g); print("unit game truth:", win, st)
print("missing strategy ->", verify.check(g, win, [None, None]))
print("non-edge strategy ->", verify.check(g, [1, 1], [None, 5]))
print("wrong regions but closed ->", verify.check(g, [1, 1], [None, 1]))
