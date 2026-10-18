# Box 1 (i): S5 (Zadeh, index tie-break) and S6 (Cunningham, index order) as a fast kill test (L-NEW, 2026-10-18)

Rules exactly as L-SI's S5.md / S6.md (engine: experiments/new/renum.cpp, which runs a verbatim copy of L-SI's vjfast.cpp;
best-reward start; identity counts equal vjfast on 5 pinned instances, check.sh pins zadehexp_N5 = 271).
Adversary: a hill climb over vertex renumberings (1-3 random swaps per step, sideways moves allowed; identity, reversal and
3 random restarts, 400 steps each). A renumbering moves (a) the priority-rank ties, (b) the best-reward start ties,
(c) the zadeh tie-break / the cunningham cyclic order. Earlier work on the same question: L-RED R4, R6, R7 (docs/red/),
which found no super-polynomial scheme and showed DFH's and Avis-Friedmann's orders are not index orders.

## Verdict so far: NOT KILLED (neither rule). No numbering with super-polynomial growth found.
Iterations, identity numbering -> best numbering found (experiments/new/out/renum/summary.csv; sweep still running for
gated_*, switchallexp, switchbestexp, recursiveladder; Oink hard bench not yet included):
| family (N = 2..6) | zadeh identity | zadeh best | cunningham identity | cunningham best |
| --- | --- | --- | --- | --- |
| zadehexp | 19, 71, 155, 271, 419 | 39, 111, 189, 323, 469 | 15, 41, 53, 73, 85 | 37, 81, 149, 213, 323 |
| cunninghamexp | 3, 6, 9, 12, 15 | 7, 30, 63, 104, 155 | 3, 6, 9, 12, 15 | 7, 24, 49, 76, 101 |
| randomfacetsubexp (n = 20, 68, 90, 207, 248) | 8, 71, 99, 320, 389 | 13, 136, 219, 759, >=1162 (timeout) | 4, 59, 88, 280, 354 | 13, 110, 186, 623, >=798 (timeout) |
| dlmm_ML | 6, 10, 14, 18, 22 | same | 2, 2, 2, 2, 2 | 6, 10, 18, 22, 24 |
| dlmm_bland | 1, 2, 5, 8, 13 | same | 1, 2, 5, 6, 9 | 1, 2, 5, 8, 11 |
| gated_bland | 3, 5, 7, 9, 11 | same | 3, 5, 9, 11, 15 | 3, 5, 9, 13, 17 |
| fhz_padded (n = 64..322) | 16, 36, 64, 100, 144 | 22, 45, 74, 112, 161 | 16, 32, 48, 64, 80 | 23, 40, 67, 83, 113 |
| gated_zadehexp (n = 82..294) | 24, 47, 70, 93, 116 | 48, 105, 202, 323, >=476 (timeout) | 34, 73, 98, 131, 156 | 52, 109, 168, 249, >=354 (timeout) |
| gated_switchallexp (N = 2..4, n = 117..219) | 77, 172, 305 | 123, 235, 381 | 58, 94, (stopped) | 117, 233, (stopped) |
Growth of the best-found counts is at most quadratic in N on every family (e.g. zadehexp/zadeh second differences 0..+70
over N; cunninghamexp/zadeh 23, 33, 41, 51 first differences). randomfacetsubexp grows with n (n jumps 90 -> 207 at N = 5);
per vertex it is not faster than the identity.

## Why the rules might still fall (honest)
- A hill climb over n! numberings is weak evidence; R7 showed the best-found Zadeh numberings on zadehexp fall to 13% of the
  published tie-break's count by N = 7 while still growing by 1.5-1.9 per level at N <= 6. A counter built for a FIXED order
  (R7 section 5: one cycle per level or a fixed cycle order, escape records separating closed from open levels) is the open
  design problem for S5; a block-order (contiguous per vertex) round-robin counter is the one for S6 (R4).
- Neither rule is covered by a published lower bound (L-SI S5.md, S6.md; L-RED R4, R7).
Not recorded as dead ends. Status in docs/new/README.md: "not killed (fast test), not defended".

## switchbestexp: the steepest growth found (11:30-12:00Z), checked in detail
Part 2 sweep (2 restarts x 200 steps; out/renum/summary_part2.csv): Zadeh best 268, 493, 976 (N = 2, 3, 4; identity 138,
328, 596); Cunningham best 341, 928 (N = 2, 3; identity 91, 147). Identity counts for N = 2..10 (no search): Zadeh 138 ... 3842
(second differences ~78, quadratic), Cunningham 91 ... 651 (+72 per N, linear).
Both best instances reproduce with vjfast (341, 928; regions = Zielonka, strategies verified) and with L-SI's independent
si.py engine (928): out/renum/switchbestexp_2_cunningham.pg sha1 94090514e570198de282c293fc37b4a007ff58e5,
out/renum/switchbestexp_3_cunningham.pg sha1 172ff9bf599fd1a33cb1625b2e23433fb32e58e5 (scratch, not committed).
Per-vertex switch counts on these runs (s6_trace.py): max 16 (N = 2, 341 iterations), max 31 (N = 3, 928): flat, spread over
many vertices; no vertex's count doubles with N, i.e. no binary-counter signature. Lifted chain (numbering of N lifted by
labels to N + 1, then climbed; s6_chain.sh): Cunningham N = 2: 395; N = 3: lifted start 688, climbing; Zadeh chain running.

## UPDATE 12:10Z: S6 on switchbestexp looks super-polynomial (data, not a claim)
Part 2 sweep (2 x 200 steps, from scratch): Cunningham 341, 928, 1887, >= 3882 (N = 2..5; N = 5 hit the 600 s cap while
climbing). Lifted chain (s6_chain.sh, 800 steps per N): 395, 939, 2837 (N = 4 still climbing at 668/800). Ratios 2.4-3.0
per N while n grows x1.29-1.42 per N: a polynomial fit needs a degree rising from 2.8 to 4.3. Identity numbering on the same
family is linear (91 ... 651, N = 2..10). Zadeh (S5) on the same family: 268, 493, 976, 1363 (ratios falling to 1.40).
Rest of the part-2 sweep (Oink bench, recursiveladder, switchallexp to N = 5): all small and polynomial-looking (e.g. tc+
Zadeh 9, 47, 131, 279; Cunningham 6, 34, 116, 291; counter_rob Zadeh 24, 56, 98, 142); summary_part2.csv.

## Pinned S6 data on switchbestexp (12:25Z; experiments/new/instances/s6/, numbering files *.perm = "old new" per line)
All counts reproduced with vjfast (verbatim copy of L-SI's engine); regions = Zielonka, strategies verified (check_sol.py).
| instance | sha1 | n | Cunningham iterations | how produced |
| --- | --- | --- | --- | --- |
| sbe_cun_chain_N2.pg | 080beed81aba76b0a6e8dce49161c188ad4ae4ea | 60 | 395 | renum2 cunningham switchbestexp_2 --restarts 2 --steps 800 --seed 7 |
| sbe_cun_chain_N3.pg | 6b9e7001b86391b439c0613c845467ffbb7d5680 | 85 | 939 | lift.py from N2 (start 688), --restarts 1 --steps 800 --seed 3 --init |
| sbe_cun_chain_N4.pg | 5ec65bf85f1e81bdb018e629a9718f99273c33e2 | 110 | 2935 | lift.py from N3 (start 1346), --restarts 1 --steps 800 --seed 4 --init |
| (N5, lift only) | (not pinned: chain still climbing at handover) | 135 | 3886 at the lifted start | lift.py from N4, no climbing |
| sbe_cun_sweep_N2.pg | 94090514e570198de282c293fc37b4a007ff58e5 | 60 | 341 | renum (run_renum.sh part 2) --restarts 2 --steps 200 --seed 2 |
| sbe_cun_sweep_N3.pg | 172ff9bf599fd1a33cb1625b2e23433fb32e58e5 | 85 | 928 | same, --seed 3 |
| sbe_cun_sweep_N4.pg | 0b436945225060a7bf4bdf96881a3a0cd6271949 | 110 | 1887 | same, --seed 4 (N = 5: >= 3882 at the 600 s cap, not written) |
Instances use switchbestexp from experiments/hard-families/pgsolver_port.py (N = 2..5) renumbered; source games in
out/inst are regenerated by the port. Per-vertex maximum switch counts on the chain instances (s6_trace.py, L-SI's si.py
engine, which reproduces the counts): 27 (N = 2), 47 (N = 3), 119 (N = 4) — growing, unlike the flat sweep instances.
Mechanical lift starts (lift.py of the previous climbed numbering, before climbing): 688, 1346, 3886 (N = 3, 4, 5).
STATUS: suggestive, NOT a family. The bar (Lead 12:14Z): a numbering produced by an explicit rule or a mechanical lifting
map N -> N+1, generating N = 2..8, with super-polynomial counts in n. Counts in the thousands at n = 60-135 are compatible
with n^4.

## Mechanical lift test (12:35Z): the lifted family is POLYNOMIAL; S6 not killed
lift.py applied mechanically (NO climbing) from sbe_cun_chain_N4.perm to N = 5, 6, 7, 8 (n = 135, 160, 185, 210), counts by
renum2's runner (= vjfast's loop): 3886, 4719, 5626, 6602 (identity: 291, 363, 435, 507). Differences 833, 907, 976: linear to
mildly quadratic in N. So the steep growth at N = 2..4 came from per-N climbing; the one mechanically defined family we have
grows polynomially. VERDICT for box 1 (i): S5 and S6 NOT KILLED; no super-polynomial growth found under renumbering on 13
bench families plus the lifted switchbestexp family. Rules still not defended (no barrier statement; R7's open problem stands).
Chains stopped at handover (12:40Z): Cunningham N = 5 climb from the lifted 3886 had reached 4186 (ratio 1.43 over N = 4's 2935);
Zadeh N = 5 climb from the lifted 1230 had reached 1506 (chain 274, 540, 983, 1506: ratios 1.97, 1.82, 1.53, falling).
The C++ N1 sweep (summary_c.csv) was stopped after switchallexp N <= 14 and switchbestexp N <= 13 (both polynomial-looking;
rows in N1-disc-anneal.md); the other families' N1 data are the Python sweep's (N <= 8, plots/).

## Box 2 (1), 2026-10-18 13:10-14:20Z (date -u): S6 numbering RULE on switchbestexp. NOT killed (data)
The climbed numberings of box 1 (instances/s6/*.perm) have no readable structure when listed by label (checked again: N = 2, 3, 4
orders look random), so a rule was SEARCHED in a space of rules, each defined for every N from the labels alone
(experiments/new/rule_s6.py): an order of the 24 label classes (q, s, p, c, t, x, y, w, d, k, l, a, b, e, e', f, f', g, g', h, m, z,
v, r), a bit direction per class, and a mode (class-major or bit-major). The climb is over RULES; fitness = vjfast Cunningham
iterations at one N; the best rule is then applied unchanged to N = 2..8 (10). Counts = vjfast (verbatim copy of L-SI's
engine); regions = Oink zlk and strategies verified (check_sol2.py) at N = 4, 8 (rule_s1) and N = 10 (rule6_s11).
| rule (experiments/new/instances/s6rule/) | fitted at | N = 2..8 (10) Cunningham iterations | n = 60 + 25(N - 2) |
| --- | --- | --- | --- |
| rule_s1.json (2,500 steps, seed 1) | N = 4 | 275, 758, 1608, 2320, 3042, 3842, 4717 | |
| rule_s2.json (seed 2) | N = 4 | 234, 605, 1139, 1610, 2158, 2783, 3483 | |
| rule_s3.json (seed 3) | N = 4 | 207, 661, 1021, 1483, 2025, 2640, 3325 | |
| rule6_s11.json (1,500 steps from rule_s1) | N = 6 | 311, 874, 1681, 3035, 4027, 4425, 5394, 6429, 7524 | |
| rule6_s12.json (1,500 steps, fresh) | N = 6 | (fitness 2249 at N = 6; not applied further) | |
Per-N sha1 of every rule-generated instance: instances/s6rule/apply_*.txt (columns N, n, iterations, sha1); regenerate with
`python3 rule_s6.py apply <rule> --maxN 10 --write DIR` (deterministic: pgsolver_port.py + the rule).
Reading: every rule grows polynomially in n. The climb produces a bump at the N it is fitted at (rule6_s11: +1354 into N = 6,
then +398, +969, +1035, +1095), and the tail is quadratic in N (log-log slope in n about 1.6 at N = 9..10). No rule beats
the box-1 mechanical lift (lift: 3886, 4719, 5626, 6602 at N = 5..8; best rule: 3035, 4027, 4425, 5394), and the lift itself is
polynomial. So the steep box-1 numbers came from per-N search over n! numberings, which a label rule of this class does not
reproduce. VERDICT (box 2 (1)): S6 NOT killed on switchbestexp; no rule in the
class (class order x directions x mode) found with super-polynomial counts. Not defended either: the rule class is small
(it cannot express interleavings that depend on two bit indices, e.g. lane j of bit i), and R7's open design problem stands.
