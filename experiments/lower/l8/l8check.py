#!/usr/bin/env python3
"""BOX L8 (L-LOWER successor 8) check block, run by experiments/lower/check.sh: (1) pins of the frozen genomes in l8/rec/;
(2) sim6 on HS2_d3 and HS2a11_d4: two capped levels, F as in docs/lower/L8-design.md; (3) hsched2 decides h = 2, d = 3 both ways
(alpha1 = 0 realized, alpha1 = 1 none); (4) ONE-READ XOR sanity (Lemma ONE-READ XOR, L8 §3): random acyclic wirings with random ranks
and signs, reader x, inputs a, b, all other states random and fixed: pref_x is never XOR/XNOR of (s_a, s_b). Prints «L8 CHECK PASS»."""
import sys, os, hashlib, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, os.path.join(H, '..', 'l7')); sys.path.insert(0, H)
from sim6 import rd, run, Fprof, caps, chain
P = {'HS2_d3.txt': '8ddebddc55e255843bde61f4026a2f448e6b136d', 'HS2a11_d4.txt': '68c8f2792bad28d7404b65d44d01ffbfd2307c8d'}
for f, h in P.items(): assert hashlib.sha1(open(os.path.join(H, 'rec', f), 'rb').read()).hexdigest() == h, f
print('pins OK:', len(P), 'files')
FX = {'HS2_d3.txt': (6, [2, 6, 2]), 'HS2a11_d4.txt': (8, [2, 6, 6, 4])}
for f, (T, F) in FX.items():
    D = rd(os.path.join(H, 'rec', f)); S, O = run(D); assert len(S) - 1 == T and Fprof(D, O) == F and caps(F) == 2, f
print('sim6: HS2_d3 T 6 F 2 6 2; HS2a11_d4 T 8 F 2 6 6 4 (two capped levels each)')
import hsched2
from sched import schedule
for al, want in (([1, 0], True), ([1, 1], False)):
    _, LS = schedule(2, alpha=al); LS = [tuple(s[:4]) for s in LS]
    gate = [0, 2, 1, 3] + [v for l in range(1, 3) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
    r = hsched2.realize(3, 2, gate, LS, {'solve': 0}, 90); assert (r is not None) == want, al
print('hsched2: h = 2, d = 3: alpha1 = 0 realized, alpha1 = 1 none')
rng = random.Random(8); n = nb = 0
for it in range(40000):
    N = rng.randint(3, 7); order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}
    xt = []
    for x in range(N):
        for k in (0, 1):
            later = [y for y in range(N) if pos[y] > pos[x]]; xt.append(rng.choice(later + [-1, -1]))
    D = {'d': (N + 1) // 2, 'xt': xt, 'br': rng.sample(range(2 * N), 2 * N), 'bp': [rng.randint(0, 1) for _ in range(2 * N)]}
    x, a, b = rng.sample(range(N), 3); base = [rng.randint(0, 1) for _ in range(N)]; prefs = []
    for sa in (0, 1):
        for sb in (0, 1):
            s = list(base); s[a], s[b] = sa, sb
            A = set(chain(D, s, x, 0)); B = set(chain(D, s, x, 1)); dd = A ^ B
            if not dd: prefs.append(None); continue
            t = max(dd); prefs.append(int((t in B) != bool(t[1])))
    if None in prefs: continue
    n += 1; nb += (prefs[0] != prefs[2] or prefs[1] != prefs[3]) and (prefs[0] != prefs[1] or prefs[2] != prefs[3])
    assert prefs not in ([0, 1, 1, 0], [1, 0, 0, 1]), (D, x, a, b, base)
print('ONE-READ XOR sanity:', n, 'random (wiring, ranks, reader, inputs, context) cases,', nb, 'depending on both inputs; XOR/XNOR never realized')
print('L8 CHECK PASS')
