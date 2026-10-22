"""REFEREE-2, packet P-C1P. Independent checks on the PINNED C++ A_DTL (oink 8fbf0a7 + logging-only patch r2log.patch:
depth-0 best_vertices calls of every search, and search boundaries). Written from GAP-A-M §27b/§28e/§33b/§35b and R46 §1-§3 text,
not from L-ALG's or L-RED's tools.
Games: class C_C^dist: q = 1 - C; every q-owned vertex has exactly one successor; q-parity priorities pairwise distinct
(mode 'all': all priorities distinct; mode 'qdist': only q-parity distinct, C-parity priorities may tie).
Per q-phase (consecutive searches of player q with the same game G'): depth-0 chain c(s) = [(R_p, res, e, V_p, piece_p)].
Checks:
  CTRL     #searches of player C <= n + 1
  CHANGE   (CHAIN-CHANGE): c(s) != c(s+1) for consecutive searches of a q-phase
  LEX      c(s') < c(s'') tree-lexicographically for ALL s' < s'' of a q-phase (per-context order of §35b)
  LEXW     the weak form: never c(s'') < c(s') and never incomparable (identical allowed)
  K        R46 §1: within a window, #transitions at p <= longest per-context chain; reports the max observed run
  NEST*    of the first-difference sequence P (R46 §2b definition), and the bound S-1 <= (2(d+2)(n+1)^2 K)^d."""
import sys, os, random, subprocess, itertools
OINK = sys.argv[1]
def gen(n, C, mode, rnd):
    q = 1 - C
    if mode == 'all': prio = rnd.sample(range(2 * n), n)
    else:
        prio = []; used = set()
        for v in range(n):
            while True:
                p = rnd.randint(0, 2 * n)
                if p % 2 == q and p in used: continue
                break
            used.add(p); prio.append(p)
    owner = [rnd.randint(0, 1) for _ in range(n)]
    succ = [rnd.sample(range(n), 1 if owner[v] == q else rnd.randint(1, min(3, n))) for v in range(n)]
    return prio, owner, succ
def pgtext(g):
    prio, owner, succ = g
    return 'parity %d;\n' % (len(prio) - 1) + ''.join('%d %d %d %s;\n' % (v, prio[v], owner[v], ','.join(map(str, succ[v]))) for v in range(len(prio)))
def run(g, path):
    with open(path + '.pg', 'w') as f: f.write(pgtext(g))
    env = dict(os.environ, R2_LOG=path + '.log')
    r = subprocess.run([OINK, '--dtl', '--no-single', '--no-wcwc', '--no-loops', path + '.pg'], env=env, capture_output=True, text=True, timeout=120)
    if r.returncode != 0: raise RuntimeError(r.stderr[-300:])
    return open(path + '.log').read().split('\n')
def parse(lines):
    searches = []; cur = None
    for ln in lines:
        if not ln: continue
        k = ln[0]
        if k == 'S':
            a, b = ln[2:].split(':'); cur = dict(pl=int(a), G=frozenset(map(int, b.split())), calls=[]); searches.append(cur)
        elif k == 'C':
            h, R, V = ln[2:].split(':'); res, e = map(int, h.split())
            cur['calls'].append((frozenset(map(int, R.split())), res, e, frozenset(map(int, V.split()))))
        elif k == 'X': cur['ret'] = int(ln[2:])
    for s in searches:
        ch = []; cl = s['calls']
        for i, (R, res, e, V) in enumerate(cl):
            piece = R - cl[i + 1][0] if i + 1 < len(cl) else frozenset()
            ch.append((R, res, e if res == -1 else 0, V if res != 0 else frozenset(), piece))
        s['chain'] = ch
    return searches
def out_lt(a, b):   # outcome order of OUTCOME-MONO-1P: a < b strictly
    (r1, e1, V1), (r2, e2, V2) = a, b
    if r1 == 0 or r2 == 0: return False
    if r1 == -1 and r2 == 1: return True
    if r1 == 1 and r2 == -1: return False
    if r1 == -1: return e1 < e2 or (e1 == e2 and V1 < V2)
    return V1 < V2
def st_lt(a, b):
    oa, ob = (a[1], a[2], a[3]), (b[1], b[2], b[3])
    if oa != ob: return out_lt(oa, ob)
    return a[4] < b[4]
def first_diff(c1, c2):
    for p in range(max(len(c1), len(c2))):
        if p >= len(c1) or p >= len(c2): return p
        if c1[p] != c2[p]: return p
    return None
def cmp_chain(c1, c2):
    p = first_diff(c1, c2)
    if p is None: return '='
    if p >= len(c1) or p >= len(c2): return 'len'
    if c1[p][0] != c2[p][0]: return 'Rdiff'
    if st_lt(c1[p], c2[p]): return '<'
    if st_lt(c2[p], c1[p]): return '>'
    return 'inc'
def nest_star(Q):
    if not Q: return 0
    best = 1
    for p in set(Q):
        i0 = Q.index(p); i1 = len(Q) - 1 - Q[::-1].index(p)
        if i0 < i1: best = max(best, 1 + nest_star([x for x in Q[i0 + 1:i1] if x > p]))
    return best
def kmax(P):
    """max number of occurrences of p inside one window (between consecutive occurrences of positions < p)"""
    best = 0
    for p in set(P):
        run = 0
        for x in P:
            if x < p: run = 0
            elif x == p: run += 1; best = max(best, run)
    return best
def analyse(searches, n, C, st):
    q = 1 - C
    st['ctrl_viol'] += sum(1 for s in searches if s['pl'] == C) > n + 1
    phases = []
    for s in searches:
        if s['pl'] == q and phases and phases[-1][-1]['pl'] == q and phases[-1][-1]['G'] == s['G']: phases[-1].append(s)
        elif s['pl'] == q: phases.append([s])
    for ph in phases:
        st['phases'] += 1; S = len(ph); st['maxS'] = max(st['maxS'], S)
        P = []
        for a, b in zip(ph, ph[1:]):
            st['trans'] += 1
            r = cmp_chain(a['chain'], b['chain'])
            if r == '=': st['change_viol'] += 1; st.setdefault('change_ex', None) or st.__setitem__('change_ex', (n, C))
            else: P.append(first_diff(a['chain'], b['chain']))
        for i, j in itertools.combinations(range(S), 2):
            st['pairs'] += 1; r = cmp_chain(ph[i]['chain'], ph[j]['chain'])
            if r != '<': st['lex_viol'] += 1
            if r not in ('<', '='): st['lexw_viol'] += 1; st['lexw_kinds'][r] = st['lexw_kinds'].get(r, 0) + 1
        d = nest_star(P); K = kmax(P) if P else 0
        st['maxNEST'] = max(st['maxNEST'], d); st['maxK'] = max(st['maxK'], K)
        Kb = (n + 2) ** 2 * (n + 1)
        if K > Kb: st['K_viol'] += 1
        if P and len(P) > (2 * (d + 2) * (n + 1) ** 2 * Kb) ** d: st['bound_viol'] += 1
if __name__ == "__main__" and sys.argv[2] != "files":
    N, nmin, nmax, seed, mode = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    tmp = sys.argv[7]
    rnd = random.Random(seed)
    st = dict(games=0, phases=0, trans=0, pairs=0, maxS=0, ctrl_viol=0, change_viol=0, lex_viol=0, lexw_viol=0, lexw_kinds={},
              K_viol=0, bound_viol=0, maxNEST=0, maxK=0)
    for k in range(N):
        n = rnd.randint(nmin, nmax); C = rnd.randint(0, 1); g = gen(n, C, mode, rnd)
        searches = parse(run(g, os.path.join(tmp, 'g')))
        st['games'] += 1; analyse(searches, n, C, st)
        if st['change_viol'] and 'change_game' not in st:
            st['change_game'] = pgtext(g); open(os.path.join(tmp, 'change_first.pg'), 'w').write(pgtext(g))
    st.pop('change_game', None); st.pop('change_ex', None)
    print(mode, 'N=%d n=%d..%d seed=%d' % (N, nmin, nmax, seed), st)

def readpg(path):
    lines = [l.strip() for l in open(path) if l.strip() and not l.startswith('parity') and not l.startswith('start')]
    ent = {}
    for l in lines:
        l = l.rstrip(';').split('"')[0].strip().rstrip(';')
        parts = l.split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2]); ent[v] = (p, o, [int(x) for x in parts[3].split(',')])
    n = max(ent) + 1
    return [ent[v][0] for v in range(n)], [ent[v][1] for v in range(n)], [ent[v][2] for v in range(n)]
def classof(g):
    prio, owner, succ = g
    multi = {owner[v] for v in range(len(prio)) if len(set(succ[v])) >= 2}
    if len(multi) != 1: return None
    C = multi.pop(); q = 1 - C
    qp = [p for p in prio if p % 2 == q]
    return C if len(qp) == len(set(qp)) else ('nodist', C)
def files_main(oink, tmp, files):
    for f in files:
        g = readpg(f); C = classof(g)
        st = dict(games=0, phases=0, trans=0, pairs=0, maxS=0, ctrl_viol=0, change_viol=0, lex_viol=0, lexw_viol=0, lexw_kinds={},
                  K_viol=0, bound_viol=0, maxNEST=0, maxK=0)
        if not isinstance(C, int): print(os.path.basename(f), 'NOT in C^1P:', C); continue
        searches = parse(run(g, os.path.join(tmp, 'f'))); st['games'] = 1; analyse(searches, len(g[0]), C, st)
        print(os.path.basename(f), 'n=%d C=%d' % (len(g[0]), C), {k: v for k, v in st.items() if k not in ('games',)})
if __name__ == '__main__' and sys.argv[2] == 'files':
    files_main(sys.argv[1], sys.argv[3], sys.argv[4:])
