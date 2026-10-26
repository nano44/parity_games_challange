#!/usr/bin/env python3
"""GATE-LAG measurements (L-SI 16, docs/si/N5-ROOT-box20.md §8.1/§8.4, l-si d842ca95), from its definitions:
A_t = F_D(t) cap U_c; DD_t = {u in D_t cap U : sigma-bar_t(u) in A_t and tau(u) in A_t}; offset Delta_t(u) = M_t(tau u) - M_t(sigma-bar_t u),
M_t(z) = signed weight of P(Xi_t z) (ranks above c). A LAG at t: Even z in U whose first D_t-vertex on its (sigma_t, tau)-play is u in DD_t,
and a successor x in A_t with Xi_t(x) > Xi_t(sigma_t z) (Xi-improving), x != sigma_{t+1}(z), and M_t(x) - M_t(sigma_t z) < Delta_t(u).
Per phase and class: per fallback-free run, the RE-RAISES of Delta(u) (transitions with u in DD at both ends and Delta strictly rising), the
drops, and the lag count; max over gates. Usage: lag.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
from cuts import plays_avoid
def analyse(g, st, out=print):
  E, rows = n3x.trace(g, st); n = g.n; best = 0
  for r in rows:
      D = {u for u in range(n) if g.owner[u] == 1 and r["nxt"][u] != r["tau"][u]}
      r["D"] = D; r["nxW"] = [r["nxt"][v] if g.owner[v] == 0 else r["tau"][v] for v in range(n)]; r["FD"] = plays_avoid(r["nxW"], D, n)
      r["M"] = [E.weight(r["vs"][v][1]) for v in range(n)]
  def firstD(r, z):
      x, seen = z, set()
      while x not in seen:
          if x in r["D"]: return x
          seen.add(x); x = r["nxW"][x]
      return None
  keys = [(r["lam"], r["tau"]) for r in rows]; i = 0
  while i < len(rows):
      j = i
      while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
      if j - i >= 5:
          lam = rows[i]["lam"]
          for c in sorted({lam[u] for r in rows[i:j + 1] for u in r["D"] if lam[u] != u}):
              U = {v for v in range(n) if lam[v] == c}
              def DD(k):
                  r = rows[k]; A = {v for v in U if r["FD"][v]}
                  return {u: r["M"][r["tau"][u]] - r["M"][r["nxt"][u]] for u in r["D"] & U if r["nxt"][u] in A and r["tau"][u] in A}, A
              dd = [DD(k) for k in range(i, j + 1)]
              raises, drops, lags, runs, cur, runr, runl = {}, {}, 0, [], [0, 0, 0], {}, {}
              for k in range(i, j):
                  d0, A0 = dd[k - i]; d1, _ = dd[k + 1 - i]; r = rows[k]
                  if r["fb"]:
                    runs.append(tuple(cur)); cur = [0, 0, 0]; best = max([best] + [min(runr[x], runl.get(x, 0)) for x in runr]); runr = {}; runl = {}; continue
                  for u in d0:
                      if u in d1:
                          if d1[u] > d0[u]: raises[u] = raises.get(u, 0) + 1; cur[0] += 1; runr[u] = runr.get(u, 0) + 1
                          elif d1[u] < d0[u]: drops[u] = drops.get(u, 0) + 1; cur[1] += 1
                  for z in U:
                      if g.owner[z] != 0 or z == c: continue
                      u = firstD(r, z)
                      if u not in d0: continue
                      a = r["nxt"][z]
                      for x in set(g.succ[z]):
                          if x in A0 and x != rows[k + 1]["nxt"][z] and E.key(r["vs"][x]) > E.key(r["vs"][a]) and r["M"][x] - r["M"][a] < d0[u]:
                              lags += 1; cur[2] += 1; runl[u] = runl.get(u, 0) + 1
              runs.append(tuple(cur)); best = max([best] + [min(runr[x], runl.get(x, 0)) for x in runr])
              QP = sum(1 for v in range(n) if g.owner[v] == 1 and len({rows[i]['tau'][v]} | {rows[k]['nxt'][v] for k in range(i, j + 1)}) >= 2)
              out(f"phase@{i} c={c} QP={QP} T={j-i} f={sum(rows[k]['fb'] for k in range(i, j))} re-raises per gate {raises} drops {drops} lags {lags} "
                    f"per fallback-free run (raises, drops, lags) {runs}")
      i = j + 1

  return best
if __name__ == "__main__":
  g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]) if len(sys.argv) > 2 else None
  print("max over (fallback-free run, gate) of min(re-raises, lags behind that gate):", analyse(g, st))
