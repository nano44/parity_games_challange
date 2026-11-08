Read-only copies from claude/l-comp at e5eb526b (not edited):
- replay30_lcomp.py = experiments/comp/box30/replay30.py, sha1 000fa38fcc2a9cdc5a83d063cac0298536630157
- lcomp_box27_sim.py = experiments/comp/box27/sim.py, sha1 f494b4e67e3f03b509adbf5a80cec2ec3d07014c
replay30 imports box27/sim.py from ../box27: to run, place them as <dir>/box30/replay30.py and <dir>/box27/sim.py (copies),
then python3 -I <dir>/box30/replay30.py GENOME.
