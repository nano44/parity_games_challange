"""L-SI succ. 7, box 12: hand-built 9-vertex (β)-candidate (c odd, low cycle {q, e′} = {5, 8}). Prints the state: NOT a fallback (gate (5, 8); Odd has Iτ = {(0, 4)}, x0 ∈ Iτ). Usage: hand9.py"""
import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import betasearch as B
from betasearch import *
# ids: o0 t1 h2 c3 x0=4 q5 d1=6 d2=7 e'=8
prio  = [0, 2, 10, 9, 2, 0, 2, 2, 0]
owner = [1, 1, 1, 0, 0, 0, 1, 1, 0]
succ  = [[1,4],[2],[3],[3,5],[3],[6,8],[7],[3],[0,5]]
g = pg.Game(prio, owner, succ); o = 0
E, Ed = n5.Engine(g), n5.Engine(n5.dual(g)); B.E_key = E.key
s = tuple([-1,-1,-1,3,3,6,-1,-1,0]); t = tuple([1,2,3,-1,-1,-1,7,3,-1])
a = info(g, E, Ed, o, s, t)
print("Xi", a["Xi"]); print("W", a["W"]); print("Is", a["Is"], "It", a["It"], "fb", a["fb"], "R", a["R"], "h", a["h"])
print("new", a["ns"], a["nt"])
U, sst = Ed.evaluate(t); print("U", U, "sst", sst)
if a["fb"]:
    b = info(g, E, Ed, o, a["ns"], a["nt"]); print("classify", classify(g, o, a, b))
