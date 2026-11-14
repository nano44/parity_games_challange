# Packet P-N5-QN (box 203): on IDEAL-CYC(G), every gate flip is a class change of one of the gate's two faces; hence quiet steps are p-steps, every quiet window has at most N steps, and per-gate flips are bounded by the faces' class heights; at every state the cycle nodes take at most k + 1 values
L-NEW successor 68 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-09 06:53Z: «freeze P-N5-QN = Theorem GATE-CLASS, Corollary GATE-FLIP, Corollary
QUIET-N (the sharpening of landed R123 T-QUIET: L → N), Lemma (k+1)-Λ — premises landed R-ids only …, each quoted by script with its
RESULTS line; cite L-RED 63's CLASS-PAYS / GATE-FLIP-MIN and L-SI 49's E-FACE-PAYS as related lane statements (not premises); DEAD list
…; DATA with counters and pins; TARGET scope paragraph». FROZEN at push. Later text goes to docs/new/P-N5-QN-fixes.md, append-only.
Source, history only: docs/new/N5-FLIP-box203.md (box 203, §1-§5.3). Every proof is carried here in full.
Labels: PROVED (L-NEW 68, unrefereed) / DEAD / DATA / READING (not to sign). Not a TARGET.md claim, not M3, not M4; G-N5-TIME stays OPEN.

## Scope (explicit)
- Model: IDEAL-CYC(G) of RESULTS R118 (a), for EVERY genome G (Ξ-cycles and Ξ self-loops allowed): R104's Γ(G), every non-mover Even
  vertex frozen at R104's start, Odd unrestricted, Howard steps at the movers; states 0, …, T_CYC. Nothing here is about Γ3, N5′-xi, N5,
  other games or other improvement rules.
- What it gives: (i) a local mechanism: a gate's optimal choice changes only when the class (Λ, E) of one of its two faces changes
  (GATE-CLASS); (ii) a per-gate bound flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) (GATE-FLIP); (iii) a sharpening of LANDED R123
  T-QUIET: every maximal window of quiet steps has at most N steps (R123: L = (M + 1)(2M + 1)(N + 1) + N(n − 1)), and T_CYC ≤ Q + (Q + 1)·N
  with Q the number of loud steps (QUIET-N); (iv) at every state at most k + 1 distinct cycle nodes, k the Ξ-feedback number ((k+1)-Λ).
- What it does NOT give: no new class on which T_CYC is polynomial (the classes of R123 ASC-T / UP-T are unchanged; only degrees drop);
  nothing at k = 1 beyond (iv) (the face class height at k = 1 is OPEN, §6); nothing on Γ3 or for N5′-xi (a Γ3 form would also be
  conditional on REACH3-CYC's premises, RESULTS R118).

## To sign
| § | statement | label | premises |
| --- | --- | --- | --- |
| §2 | Theorem GATE-CLASS | PROVED | [DEF], [VJ], R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2 |
| §3 | Corollary GATE-FLIP; its HUB-ASC-G form | PROVED | §2, R118 (e) (Λ rises), R121 E-MON; the second form also R121 HUB-ASC-G whole-run form (and UP-B under [E-LEV]) |
| §4 | Corollary QUIET-N | PROVED | §2, R118 BR-SEG (with its labels C / R / p), R123 NO-TIE, LOC-GATE, LOC-K2, the counting of §3 |
| §5 | Lemma (k+1)-Λ | PROVED | [DEF], R123 B-ONLY, LOC-K2 |
| §6 | DEAD list (with instances) | DEAD | instances frozen, §6 |
| §7-§10 | related lane statements, DATA, TARGET diff, machine checks | READING / DATA (not to sign) | |
No other premise: no lane packet, no L-RED or L-SI lemma (§7 lists related ones; none is used), no P-N5-CHAIN fact, no [E-LEV] except in
§3's second form.

## 1. Premises (landed R-ids, quoted by script from trunk claude/vibrant-johnson-nxvvxo b8408b39, docs/RESULTS.md, line numbers there)
- [DEF] RESULTS R104 (l. 9864), definitions of the genome and of Γ(G) only:
  - «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»;
  - «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone»;
  - «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»;
  - «an unused even self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far»;
  - «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}»;
  - «with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2».
  - Shape, from the frozen packet R118 cites (P-N5-XICYC §1, sha1 149e2414): «movers (Even, priority 0) → gates (Odd, priority 1) →
    {e-face e_g, β-face β_g}».
  - Readings of [DEF] used (no other source): (D1) each gate g has its own e-vertex e_g, whose only in-edge is from g; (D2) E-DOM: every
    vertex more relevant than an e-vertex is an e-vertex, c_W, K0 or K3; (D3) the core is entered from outside only at u = K0 (the β's
    escape edge); (D4) the unused self-loop c_X has no in-edge from another vertex; (D5) Ξ-graph: movers, an edge x → xt(x, j) for each
    option whose Ξ-target is a mover; k(G) := the minimum size of a set of movers meeting every cycle of it (self-loops count).
- [XICYC] RESULTS R118 (l. 13607):
  - header: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)» ([VJ]: first the reward of Λ, distinct for
    distinct cycle nodes since priorities are made injective by rank; then Π by the most relevant vertex of the symmetric difference; then k);
  - the step labels: «labelled C if some vertex's cycle node Λ changes, else R if Odd's optimal counterstrategy σ̄ (any fixed deterministic
    choice) changes somewhere, else p»;
  - (a) «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2).»;
  - (d) Theorem BR-SEG: «every maximal run of p-steps has at most N steps»;
  - (e) with its reason: «each vertex's Λ moves only to a vertex of strictly larger reward among at most 2M + 3 possible cycle nodes»;
  - Theorem T-CYC (cited for comparison only): «T_CYC ≤ C + R + (C + R + 1)·N».
- [ASC] RESULTS R121 (l. 14320): «(Lemma E-MON) if Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v)»; HUB-ASC-G's whole-run form: «over the
  whole run the number D_E(v) of distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M)» (when every seq_t(v) has at most B ascents); UP-B:
  «so under [E-LEV] every seq_t(v) has at most U(G) ascents (U(G) := the number of options whose Ξ-target has a higher level)».
- [QUIET] RESULTS R123 (l. 15076):
  - «(Lemma CN2) the cycle node of every play under every positional pair has priority ≥ 2, so no gate or mover is a cycle node or in a set Π»;
  - B-ONLY: «at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than
    every e-vertex»;
  - «(Corollary NO-TIE) at every state and gate g, Ω_t(e_g) ≠ Ω_t(β_g)»;
  - «(Lemma LOC-GATE) at every state t and gate g, Odd's optimal counterstrategy σ̄_t chooses the face of strictly ⊴-smaller value»;
  - «(Lemma LOC-K2) σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2) at every state»;
  - the class and loud / quiet steps: «with class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the e-vertices of Π_t(v), a step loud if some vertex
    changes class and quiet otherwise»; Theorem QUIET's bound (compared in §4): «every maximal window of quiet steps has at most L := (M +
    1)(2M + 1)(N + 1) + N(n − 1) steps, n = N + 3M + 6»; «(Corollary T-QUIET) T_CYC ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L + 1), D^tot_E(v)
    the number of distinct classes of v over the run».
- Notation: Ω_t(v) = (Λ_t(v), Π_t(v), k_t(v)) the value under (σ_t, σ̄_t); E_t(v) and class_t(v) as in R123; sets of e-vertices compared
  lexicographically by the most relevant differing element (R121); flips(g) := #{t ≥ 1 : σ̄_(t−1)(g) ≠ σ̄_t(g)}; D^tot(v) := the number of
  distinct classes of v over the run (= R123's D^tot_E(v)).
- Counting (C1), used in §3-§4: the classes of a vertex v appear in strictly increasing order and never repeat: Λ_t(v) only moves to a
  vertex of strictly larger reward (R118 (e)'s reason), and while Λ_t(v) is fixed E_t(v) only rises (E-MON). So class(v) changes at
  exactly D^tot(v) − 1 steps.

## 2. Theorem GATE-CLASS (PROVED)
For every genome G, every gate g and every step t of IDEAL-CYC(G): if σ̄_(t−1)(g) ≠ σ̄_t(g), then class_(t−1)(e_g) ≠ class_t(e_g) or
class_(t−1)(β_g) ≠ class_t(β_g).
Proof. Write a = e_g, b = β_g. Assume that neither class changes at t; we show that σ̄(g) does not change. Then Λ_(t−1)(a) = Λ_t(a) =: w_a,
Λ_(t−1)(b) = Λ_t(b) =: w_b, E_(t−1)(a) = E_t(a) and E_(t−1)(b) = E_t(b). Let s range over {t − 1, t}.
- Case 1: w_a ≠ w_b. Distinct cycle nodes have distinct rewards ([VJ]), so Ω_s(a) and Ω_s(b) are ordered by Λ alone, the same way at both
  s. By LOC-GATE σ̄_s(g) is the face of strictly smaller value: the same face at both s.
- Case 2: w_a = w_b =: w. If a's successor is c_W, then Λ_s(a) = c_W, while b (a β) is not an exception of B-ONLY, so Λ_s(b) is less
  relevant than every e-vertex and ≠ c_W: Case 1. Otherwise B-ONLY applies to a: w is less relevant than every e-vertex, in particular
  than a. So a is not its own cycle node and, being the first vertex of its play and more relevant than w, a ∈ Π_s(a): e_g ∈ E_s(a).
  - Case 2a (PRIV at s: e_g ∉ Π_s(b)). Π_s(a) Δ Π_s(b) contains e_g; let z be its most relevant vertex, so z is e_g or more relevant. By
    (D2) z is an e-vertex, c_W, K0 or K3. c_W lies in no Π: a play reaching c_W ends in c_W's self-loop, so its cycle node is c_W, excluded
    by B-ONLY for a and b. K0, K3: by (D3) a play from a non-core vertex enters the core at K0, then follows the frozen K0 → K3 → K2, then
    σ̄_s(K2) = K1 (LOC-K2), then the frozen K1 → K1; so a play contains K0 iff it contains K3 iff its cycle node is K1. Both plays have
    the cycle node w, so K0 and K3 lie in both Π's or in neither. Hence z is an e-vertex, z = e_g or more relevant, and z is the most
    relevant element of π(E_s(a)) Δ π(E_s(b)), π(X) := {f ∈ X : f = e_g or f is more relevant than e_g}. By [VJ] the value whose Π holds
    z (even) is the larger. With LOC-GATE: σ̄_s(g) is the face whose π(E_s) is lexicographically smaller. So on PRIV states σ̄_s(g) is a
    function of the pair (π(E_s(a)), π(E_s(b))).
  - Case 2b (non-PRIV at s: e_g ∈ Π_s(b)). b's play passes e_g; by (D1) its only in-edge is from g, so b's play passes g and continues
    to e_g: σ̄_s(g) = a.
  - If s = t − 1 and s = t are both PRIV, the π-pairs are equal (the e-sets are), so σ̄(g) does not change (2a). If both are non-PRIV,
    σ̄_(t−1)(g) = σ̄_t(g) = a (2b). If exactly one is non-PRIV, then e_g lies in Π_s(b) for exactly one s, and as e_g is more relevant than
    w, e_g ∈ Π_s(b) ⟺ e_g ∈ E_s(b): E(b) changes at t, against the assumption. ∎

## 3. Corollary GATE-FLIP (PROVED)
(a) flips(g) ≤ (D^tot(e_g) − 1) + (D^tot(β_g) − 1) for every gate g.
(b) If every seq_t(e_g) and every seq_t(β_g) has at most B ascents, then flips(g) ≤ 2·((2M + 3)·F′_B(M) − 1); under [E-LEV] (HYPOTHESIS,
as in R121 / R123), B = U(G) may be taken.
Proof. (a) Each flip step is a class-change step of e_g or of β_g (§2), and each face's class changes at exactly D^tot − 1 steps (C1).
(b) R121's whole-run form bounds D^tot(v) = D_E(v) by (2M + 3)·F′_B(M) for v = e_g, β_g; UP-B gives B ≤ U(G) under [E-LEV]. ∎
- Only the two faces' class heights enter; no factor lamch(g) and no Ξ-feedback number.

## 4. Corollary QUIET-N (PROVED; sharpens landed R123 Theorem QUIET / Corollary T-QUIET)
In IDEAL-CYC(G), for every genome G: every quiet step is a p-step of R118; every maximal window of quiet steps has at most N steps; and
T_CYC ≤ Q + (Q + 1)·N, where Q := the number of loud steps, Q ≤ Σ_v (D^tot(v) − 1).
Proof. At a quiet step no vertex changes class, so no Λ changes (no C label). The Odd vertices with a choice are the gates and K2 ([DEF]).
At a gate σ̄ does not change (§2: a change would be a class change of a face); at K2, σ̄_t(K2) = K1 at every state (LOC-K2). σ̄ is unique at
every state (NO-TIE with LOC-GATE at gates; LOC-K2's strict ◁ at K2), so R118's «any fixed deterministic choice» is that σ̄, and no R label
occurs. So the step is a p-step. A maximal quiet window lies inside a maximal run of p-steps, which has at most N steps (BR-SEG). The run's
T_CYC steps are Q loud steps and at most Q + 1 maximal quiet windows. Each loud step changes the class of some vertex; by (C1) there are
at most Σ_v (D^tot(v) − 1) such steps. ∎
- Against R123: Theorem QUIET's window bound L = (M + 1)(2M + 1)(N + 1) + N(n − 1) becomes N; T-QUIET's T_CYC ≤ (1 + Σ_v (D^tot(v) − 1))·
  (L + 1) becomes T_CYC ≤ Q + (Q + 1)·N ≤ Σ_v (D^tot(v) − 1)·(N + 1) + N. R123's ASC-T and UP-T hold with L + 1 replaced by N + 1. The
  classes of genomes on which T_CYC is proved polynomial are unchanged.

## 5. Lemma (k+1)-Λ (PROVED)
For every genome G with Ξ-feedback number k (D5) and every state t of IDEAL-CYC(G), the cycle nodes Λ_t(v), over all vertices v other than
c_W, c_X and the e-vertices whose successor is c_W, take at most k + 1 values: K1, and the most relevant vertex of each cycle of the
functional graph Ξ_σ on the movers, x → xt(x, σ_t(x)) (options whose Ξ-target is X omitted). Ξ_σ has at most k cycles.
Proof. Let Z be the cycle of v's play under (σ_t, σ̄_t) and w its most relevant vertex (= Λ_t(v)). By B-ONLY w is less relevant than every
e-vertex, so Z has no e-vertex, and Z is not c_W's self-loop. If Z meets the core, then (as in §2, Case 2a) the play reaches K1 → K1 and
w = K1. Z ≠ c_X's self-loop: v ≠ c_X and (D4). Otherwise Z consists of movers, gates and β's; on Z a mover x is followed by its gate
(x, σ_t(x)), the gate by its β-face (no e-vertex on Z), the β by its frozen start successor, which is the Ξ-target xt(x, σ_t(x)) (a target
X would lead to u = K0, into the core). So the movers of Z form a cycle of Ξ_σ, and Z with w is determined by that cycle. Ξ_σ has
out-degree ≤ 1, so its cycles are vertex-disjoint; each is a cycle of the Ξ-graph, so it meets every set of movers meeting all Ξ-cycles;
a minimum such set has k elements; so Ξ_σ has at most k cycles. ∎
- At k = 0 the lemma gives Λ ≡ K1 off c_W, c_X (the Λ part of RESULTS R122's LAMBDA-CONST); at k = 1, Λ_t(v) ∈ {K1, c_t}. It bounds Λ only:
  on MWR(n) (k = 1) Λ ≡ K1 at every state and vertex (C = 0) while one face takes 2n + 2 classes (§9).

## 6. DEAD list (each with the instance that kills it)
- D1. CONJECTURE K1-FLIP «at k = 1 each gate flips at most 2·lamch(g) + 1 times» (box 202): box202/k1fail_202.json (sha1 99bba752; gate
  (4, 0): 2 flips, lamch 0). L-NEW 67.
- D2. CONJECTURE K1-FLIP(c) «at k = 1 every gate flips at most c·(lamch(g) + 1) times», every constant c: L-RED 63's MWR(n) (claude/l-red
  406ef2fd, R229-box202 §2; copies experiments/new/box203/inst/MWR4_2.json sha1 856d369b, MWR8_2.json 918f1414, MWR16_2.json 2ccda9a9):
  gate (qz, 0) flips 2n + 1 times with lamch 0. Also any bound with the number of global Λ-changes as the denominator: MWR has C = 0 on
  IDEAL-CYC.
- D3. «Every e-sequence has at most k + 1 ascents» (box 203 §5.2; with R123 ASC-T it would have made T_CYC polynomial for each fixed k):
  at k = 1 the staircase ST(m) (experiments/new/box203/stair203.py; inst/ST4_k1.json sha1 3fa71a98, 3 ascents; inst/ST8_k1.json sha1
  9dbf71f4, 7 ascents), and on real k = 1 runs K1C16_n400 (L-RED 63, claude/l-red fa4e50fe; copy inst/K1C16_n400.json sha1 99da972a)
  and K1F21_n48 (inst/K1F21_n48.json sha1 2e7460da), 3 ascents each; at k = 2 L-SI's WC family (box202/inst/WC4_2, WC8_2, WC16_2: 4, 8,
  16 ascents). Obstruction: an ascent needs only an upward Ξ-edge (R121 UP-JUMP), and upward Ξ-edges can be acyclic.

## 7. Related lane statements (READING; cited, NOT premises, not re-proved here)
- L-SI 49 (claude/l-si f723957b, docs/si/box93-k7k6.md §1-§2; on Γ3 with LOC-GATE3 / NO-TIE3): Lemma NP-SHAPE («a non-PRIV state of gate o
  has Odd on the e-face p_e, and p_b's play = A · o · (p_e's play)»; §2 Case 2b is its first half on IDEAL-CYC) and Corollary E-FACE-PAYS
  («relocks(o) ≤ ch(p_e), unlocks(o) ≤ 1 + ch(p_e)»; flips(g) ≤ 2·min_f ch_f + 1). L-SI 48's GATE-LOW-NULL (box 92 §1): §2 Case 2a is its
  argument on IDEAL-CYC, where B-ONLY supplies its hypothesis «e_o above Λ».
- L-RED 63 (claude/l-red fa4e50fe, docs/red/R229-box93.md; relayed by the Lead 05:29Z): Lemma REL-G, and with R123 B-ONLY CLASS-PAYS:
  flips(g) ≤ 2·min(D^tot(e_g) − 1, D^tot(β_g) − 1) + 1, sharper than §3 (a) (min instead of sum) and exact on MWR (2n + 1).

## 8. What stays OPEN (READING)
- k = 1: whether the smaller face's class height, max_g min(D^tot(e_g), D^tot(β_g)), is polynomial in N + M. §5 bounds Λ, D3 removes the
  ascent route; MWR, K1F21, K1C16 and L-COMP 15's B400_r32 (§9) are linear-looking records.
- In general: Σ_v D^tot(v) with U(G) unbounded and unboundedly many ascents (as R123 states). This is G-N5-TIME's IDEAL-CYC core.

## 9. DATA (not to sign; tools experiments/new/box203/, engine box191/idealcyc.py + experiments/si/si.py's Engine, IDEAL-CYC from the
## genome's start, cap 20,000 states; outputs pinned in box203/qn.pins)
- gfc203.py must-0 counters (TOTALS): odd (a flip with face Λ's unequal and constant), vfail (a flip with both face values unchanged),
  glnfail (§2 Case 2a: a PRIV flip with both π's unchanged), emon (a face's value or e-set decreasing at constant Λ), hfail / hefail
  (per-interval height bounds), tieflip (a flip at a face tie), lfail (GATE-CLASS: a flip with neither face changing class), gfail (unit
  gate: GATE-FLIP (a) violated), qflip (unit step: σ̄ changes at a quiet step), qfail (unit run: a quiet window > N), Tfail (unit run:
  T_CYC > Q + (Q + 1)N). All 0 on: the 57-genome corpus (out/gfc203_corpus.out: the 53 box 202 genomes, MWR4/8/16_2, k1fail_202);
  1,000 rand191 genomes, d 1-6, w 1-3, degree 2-3, seed 2 (out/rnd203_rand_s2.out); 5,000 k = 1 genomes, k1srch202.mk seed 202
  (out/rnd203_k1_s202.out); K1C16_n400 and K1F21_n48 (out2/gfc203_k1extra.out). Γ3 (N5′-xi from S3 to the first fallback; DATA only,
  nothing claimed): the same counts on MWR4_2, MWR8_2, k1fail_202, C4_NM50, C6G8_n54, RWX_n95 (out/gfc203_g3.out).
- GATE-FLIP (a) is attained (slack 0 at some gate) on MW, the C-frontier family and FW (out/gfc203_corpus.out, column slack). Longest
  quiet window: 10 at N 108 (DSALT6_n108); most runs have none.
- (k+1)-Λ, lam203.py (unit: states; lfail = states with more than k + 1 values, TOTAL): 0 on 2,000 k = 1 genomes (seed 7), 1,000 k = 2
  genomes (seed 8), 1,000 rand191 genomes (seed 2) (out2/lam203_*.out); control LAM_CTRL=1 (bound k) fires: 3,492 on the k = 1 set.
- k = 1 per-gate records (unit: the gate with most flips; all flips at lamch 0; C = 0): MWR4/8/16_2 9 / 17 / 33, face classes (n + 1,
  2n + 2); K1F21_n48 (N 48) 21, (12, 22); K1C16_n400 (N 113) 31, (22, 37). L-COMP 15's BEST_B400_r32 (claude/l-comp 0eb92268, sha1
  a13d9661; run by me, record not in a lane file): gate (82, 0) 32 flips, faces (18, 34). Each within L-RED's CLASS-PAYS (§7).
- Controls (check203.out, each fires): GFC_CTRL=1 (π := the part strictly below e_g) glnfail 4; GFC_CTRL=2 hefail 5; GFC_CTRL=3 (only the
  e-face's class looked at) lfail 9 on MWR4_2; LAM_CTRL=1 lfail 173 on 100 k = 1 genomes.

## 10. TARGET.md diff and scope
- TARGET.md §2 (M4) asks for an algorithm polynomial on every parity game, and §4 says a bound on a restricted class is not M4. This packet
  proves (a) a mechanism lemma and a per-gate bound on one model, IDEAL-CYC(G) of R104 / R118 genomes, and (b) a sharpening of a landed
  bound (R123 T-QUIET: window L → N). It makes no new class polynomial and proves nothing about N5′-xi, N5 or general games.
- Not M3, not M4, not a gauntlet step-4 pass, not a TARGET.md claim. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).

## 11. Machine checks
- check.sh block «BOX 203 FLIP»: re-runs box203/check203.sh (gfc203.py on MWR4_2, MWR8_2, k1fail_202, C4_NM50 and three controls;
  rnd203.py on 100 + 100 genomes; asc203.py on ST4_k1, ST8_k1, MWR4_2; lam203.py and its control), diffs check203.out, requires every
  must-0 counter 0, the controls firing and the ST8 ascent witness, and checks box203/inst against SHA1SUMS.
- check.sh block «P-N5-QN»: sha1 of this packet, its source note, the quote check's tool and output, every tool, output and instance cited,
  and the engine modules the tools load, against experiments/new/box203/qn.pins.
- Quote check (record tool; it needs git objects): experiments/new/box203/quotesqn.py b8408b39 → box203/quotesqn.out: every «…» in §1
  verbatim (whitespace normalised) in trunk docs/RESULTS.md or docs/new/P-N5-XICYC.md.
