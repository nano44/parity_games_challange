"""Box 63 probe: [S4b-OPT] by brute force. At every N5 state k with I_tau != {}, S4b's tau_new (n5x.step, before any fallback) is compared,
pointwise, with EVERY Odd strategy rho of the arena H' (Odd v keeps {tau(v)} u I_tau(v); Even v keeps sigma(v)): the value of the
(sigma, tau_new)-play must be <= (better for Odd, Even's order) the value of the (sigma, rho)-play at every vertex.
  STATES   states with I_tau != {}.   CHECKED  of them with at most CAP arena strategies (enumerated in full).   SKIPPED  the others.
  RHOS     strategies compared.   OPTV  (state, rho, vertex) where rho is strictly better for Odd than tau_new ([S4b-OPT] violation: expected 0).
  TAUNEW_EQ_RUN  states where the run's tau_(k+1) equals S4b's tau_new;  ODDFB  Odd fallbacks (I_sigma = {}, sigma_new = sigma, tau_new = tau;
  then tau_(k+1) != tau_new by S4c).   S4AV  control: the same brute force for S4a's sigma_new against tau on H (Even maximises): violations.
  MUT=1 (env): replace S4b's tau_new by the old tau (a mutation control: OPTV > 0 expected where S4b changes tau).
Usage: s4bopt.py GAME.pg [START] [CAP]   (CAP default 4096)."""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
sys.path.insert(0, os.path.join(HERE, "..")); from startcheck import check_start
a = sys.argv[1:]; CAP = 4096
if a and a[-1].isdigit(): CAP = int(a.pop())
g = load(a[0]); st = readstart(a[1]) if len(a) > 1 else None; check_start(g, st, a[1] if len(a) > 1 else ""); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st)
def playval(sig, rho):
    """Values of the (sig, rho)-plays: evaluate sig on the game where Odd v keeps only rho(v)."""
    G1 = pg.Game(list(g.prio), list(own), [[rho[v]] if own[v] == 1 else g.succ[v] for v in range(n)])
    E1 = Engine(G1); return [E1.key(x) for x in E1.evaluate(tuple(sig))[0]]
T = dict(STATES=0, CHECKED=0, SKIPPED=0, RHOS=0, OPTV=0, TAUNEW_EQ_RUN=0, ODDFB=0, S4ACHK=0, S4AV=0)
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, Is, It, fb, vs, vt = r
    if It:
        T['STATES'] += 1
        opt = {v: sorted({t[v]} | {w for x, w in It if x == v}) for v in range(n) if own[v] == 1}
        # S4b's tau_new, recomputed exactly as n5x.step does (before the fallback branch)
        succ = [opt[v] if own[v] == 1 else [s[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(own), succ)); _, best = Er.evaluate(tuple(s[v] if own[v] == 0 else -1 for v in range(n)))
        tnew = [best[v] if own[v] == 1 else t[v] for v in range(n)]
        if os.environ.get('MUT') == '1': tnew = list(t)   # mutation control: the OLD tau in place of S4b's output
        T['TAUNEW_EQ_RUN'] += tnew == list(nt)
        T['ODDFB'] += bool(fb and not Is)
        odds = [v for v in range(n) if own[v] == 1 and len(opt[v]) > 1]
        size = 1
        for v in odds: size *= len(opt[v])
        if size > CAP: T['SKIPPED'] += 1
        else:
            T['CHECKED'] += 1; base = playval(s, tnew)
            for combo in itertools.product(*[opt[v] for v in odds]):
                rho = list(tnew)
                for v, w in zip(odds, combo): rho[v] = w
                T['RHOS'] += 1; val = playval(s, rho)
                T['OPTV'] += sum(1 for v in range(n) if val[v] < base[v])
    if Is and not fb:   # control: S4a's sigma_new is Even's pointwise optimum on H against tau
        opt = {v: sorted({s[v]} | {w for x, w in Is if x == v}) for v in range(n) if own[v] == 0}
        evs = [v for v in range(n) if own[v] == 0 and len(opt[v]) > 1]; size = 1
        for v in evs: size *= len(opt[v])
        if size <= CAP:
            T['S4ACHK'] += 1
            Gt = pg.Game(list(g.prio), list(own), [[t[v]] if own[v] == 1 else g.succ[v] for v in range(n)]); Et = Engine(Gt)
            base = [Et.key(x) for x in Et.evaluate(tuple(ns))[0]]
            for combo in itertools.product(*[opt[v] for v in evs]):
                sg = list(ns)
                for v, w in zip(evs, combo): sg[v] = w
                val = [Et.key(x) for x in Et.evaluate(tuple(sg))[0]]
                T['S4AV'] += sum(1 for v in range(n) if val[v] > base[v])
    s, t = ns, nt
print("S4BOPT", os.path.basename(a[0]), " ".join(f"{k} {v}" for k, v in T.items()))
