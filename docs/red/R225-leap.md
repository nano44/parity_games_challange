# R225 item 1 (second target): adversary on L-SI 45's BOX 87 Lemma LEAPFROG-ASC (L-RED successor 59, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Target (Lead 10:28Z): claude/l-si fe9c688a + addendum 6391f53c, docs/si/box87-leapfrog.md (read at 6391f53c, §0-§6). Asked:
- attack Claims B and C and the bound;
- say whether my CX4 / depth-2 race constructions produce type-II nesting.
Labels: SURVIVES / BROKEN; DATA (unit, set, scope, counter). Not a TARGET.md claim; G-N5-TIME stays OPEN.
Tool: experiments/red/r225/leap225.py, my own census on R221's independent IDEAL-CYC Howard run own.py. No L-SI code is used.

## 0. Verdict
| statement | verdict | basis |
| --- | --- | --- |
| (F1)-(F3), Claim A | SURVIVE | §1; Afail 0, F2fail 0 |
| Claim B (opposite type-I events raise M) | SURVIVES | proof re-derived for both orders (§1); Bfail 0 |
| Claim C (type II ⇒ ascent in the deciding e-sequence) | SURVIVES | §1 (needs the common suffix to have node λ on both sides, which (NODE) + the choice of b give); Cfail 0 |
| Lemma LEAPFROG-ASC (#events ≤ \|E_U\| + 2k) | SURVIVES | counting re-derived; boundfail 0 on 158 + 5,553 units |
| Corollary LEAPFROG-NOASC | SURVIVES | k = 0 ⇒ ≤ \|E_U\| |
| §3 obstruction (type-II flips nest; depth not bounded by SAME-E-MERGE / E-MON) | AGREE | nesting depth measured: ≤ 3, grows with h on HP (§2) |
No break. One sharper DATA fact: in every unit, #events ≤ |E_U| − 1. The 2k term was never needed (§2).

## 1. Proof read
- (F1): E-MON at w and at every g_o (gates included; each node is constant on I) plus PROJ-MON (projection onto an upper segment
  of the relevance order keeps lex order). A max over a fixed family of nondecreasing chains is nondecreasing. OK.
- (F2): ON uses FLIP-U (5′) and OFF uses FLIP-U (4′); both SURVIVED R223-si85. Strictness at OFF: e_S ∈ a_t, and e_S ∉ π(E(g_o)) by PRIV
  plus the in-degree-1 chain (R225-lag §1). OK.
- Claim B, t OFF then t′ ON, both type I:
  - m = z_t = M_t ∈ b_t \ a_t (type I gives M = z), so max b_t = m.
  - If M_t′ = m, then m ≤ max b_t′ ≤ M_t′ = m, so m ∈ b_t′. But type I with ON puts M_t′ = z_t′ in a_t′ \ b_t′. Contradiction.
  - The ON-then-OFF order swaps a and b and reads the same. OK.
- Lemma: after the k type-II events are deleted, a run of type-I events alternates (F3), so M rises strictly inside a run (Claim B) and
  never falls between runs (Claim A). All values lie in E_U, so the count is ≤ |E_U| + (runs − 1) ≤ |E_U| + k, plus k. OK.
- Claim C:
  - s ∈ a_t ∩ b_t with s ≠ e_S, so s lies on w's play and on g_o*'s play.
  - Both plays have node λ (w by FLIP (1) when an ON is possible; g_o* by the definition of b). So the common suffix from s's mover
    (SAME-E-MERGE) has the same Π-membership on both sides, and z_t, being in the symmetric difference, lies before the merge.
  - The e-sequence holding z_t ((e_S, seq(w)) or seq(g_o*)) therefore reaches s after z_t, which gives an ascent. OK.
  - If Λ(w) ≠ λ on I, no ON happens on I (FLIP (5)(i)) and there is at most one event. The census includes such units.

## 2. DATA (leap225.py; out/leap87.txt, out/leap_rand2271.txt)
- Unit: (mover B, SET option S, maximal interval I with Λ(B) ∈ {K1, K2} and Λ(B), Λ(w), every Λ(g_o) constant). These intervals can
  be LONGER than L-SI's, which keep every node constant, so the test is stronger.
- Every SET option of every mover is included, not only the real bits.
- PRIV and NODE are checked on each unit. Units failing them are counted apart (ev_nohyp).
- Scope: own.py IDEAL-CYC, [E-LEV], cap 3000.
- Counters: ev, type I / II (k), maxk, maxdepth (number of distinct heads min(H) over the type-II events of a unit), boundfail
  (ev > |E_U| + 2k), F2fail, Afail, Bfail, Cfail, maxexcess = max(ev − |E_U|).

| set | units (PRIV + NODE) | ev | type I | type II | maxk | maxdepth | boundfail / F2 / A / B / C fail | maxexcess |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HP2 / HP3 / HP4 / HP5_mup (box 84; copies inst84/, sha1 HP4 d7ebbea0… = box 84's table) | 3 / 5 / 7 / 9 | 5 / 13 / 23 / 33 | 5 / 9 / 12 / 13 | 0 / 4 / 11 / 20 | 0 / 3 / 4 / 5 | 0 / 2 / 3 / 3 | 0 | −1 |
| box 85: TC2, TC2d, TC3, TC3d, TC3m, TC4m, TC5m, CL2_21, CL2_22, CL3_31, CL3_32 (r223/inst_si85) | 81 | 160 | 102 | 58 | 5 (CL2_21) | 3 | 0 | −1 |
| box 86: 11 instances (inst86/, sha1 = pins.sha1) | 51 | 76 | 72 | 4 | 1 | 1 | 0 | −1 |
| CX4_n21 (mine) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | −4 |
| total, 27 genomes | 158 | 310 | 213 | 97 | 5 | 3 | 0 | −1 |
| random, latch225 rgen seed 2271, 3,000 genomes | 5,553 | 214 | 212 | 2 | 1 | 1 | 0 | 0 |

- 10 units on the frozen instances fail PRIV or NODE (12 events). The lemma does not apply there, and none exceeds |E_U| − 1 either.
- maxexcess ≤ −1 on all 27 genomes: #events ≤ |E_U| − 1, without the 2k term. Type-II events exist (97), but they never push a unit
  past |E_U|. On these instances they replace type-I events rather than add to them.
- Nesting depth grows with h on the MIRROR family HP: 0, 2, 3, 3 at h = 2-5. Linear like the hub heights, as L-SI says.

## 3. Do my CX4 / depth-2 races produce type-II nesting?
- CX4_n21 has no event at all: its two SET options never flip. Its multiplication is at a NON-SET router (x0 switches between two
  β-options, x9 and x10).
- So CX4's mechanism lives in P-QUIET's branch (non-SET switches, charged to e-set heights under QUIET), not in LEAPFROG-ASC's
  SET-bit branch.
- The connection is structural, not literal. A type-II event is decided under a shared head, between two plays that merge. CX4's race
  is two routes from one router that merge into the same High chain, decided by the bonus e10 below the shared High. That is exactly
  a type-II decision, made at a mover's option choice instead of a SET flip.
- A depth-2 race (not built) would be type-II nesting at depth 2 at that router. So the open quantity is the same in both: the nesting
  depth of decisions under shared heads, which HUB-ASC's recursion and ASC-EXP leave unbounded.
- READING: a common formulation would count «type-II decisions» at every mover with ≥ 2 options, not only at SET bits. CONJECTURE
  TWO-COPY-RED's SET branch and my ADD(c) are then two faces of one statement: decisions under shared heads nest only polynomially.
