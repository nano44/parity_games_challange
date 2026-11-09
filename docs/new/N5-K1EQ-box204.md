# Box 204 (D18): at k = 1 the per-gate face problem IS the run-length problem — faces carry their targets' classes (L-NEW successor 68, Opus)
Written 2026-11-09 (date -u in the commit). Lead 07:34Z: «continue the open step, the smaller face's class height at k = 1 (run-level
argument; test on MWR / K1F21 / K1C16 / L-COMP B400_r32 and r34)».
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Setting and notation: IDEAL-CYC(G) and the premises of P-N5-QN §1 (frozen, l-new
e252182d, sha1 97254bd2), every genome. Tools: experiments/new/box204/k1eq204.py; outputs box204/out/; check204.sh («BOX 204 K1EQ»).

## 0. Answer
- No run-level bound at k = 1 is proved. What is proved instead shows the step is not a sub-lemma: it is the whole IDEAL-CYC run-length
  question restricted to k = 1.
- **Lemma FACE-TARGET (PROVED, lane; [DEF], R123 B-ONLY, CN2).** At every state: class(e_g) = (Λ(wt), E(wt) ⊔ {e_g}) when the W-target
  wt = wt(g) is a mover (constant (c_W, ∅) otherwise), and class(β_g) = class(xt) when the Ξ-target xt = xt(g) is a mover (constant
  otherwise). So D^tot(e_g) = D^tot(wt(g)) and D^tot(β_g) = D^tot(xt(g)): a gate's faces have exactly the class heights of two MOVERS.
- **Theorem EQ (PROVED, lane; premises P-N5-QN GATE-FLIP and FACE-TARGET, R118 T-CYC and CYC-COUNT, R123 LOC-K2).** For every genome,
  with D_mov := max over movers x of D^tot(x):
    D_mov − 1 ≤ T_CYC  and  T_CYC ≤ C + R + (C + R + 1)·N with C ≤ n(2M + 2) and R ≤ M·(2·D_mov − 2).
  So on any family of genomes (in particular k = 1), T_CYC is polynomial in N + M iff D_mov is, iff the faces' class heights are.
  With L-RED 63's CLASS-PAYS (lane, cited, not used above) «the smaller face» suffices on the right-hand side as well.
- Consequence for the Lead's question (READING): «the smaller face's class height at k = 1 is polynomial» is EQUIVALENT to «T_CYC is
  polynomial on IDEAL-CYC at k = 1». A proof needs the same idea that G-N5-TIME's IDEAL-CYC core needs, at the class k = 1; a kill is a
  k = 1 family with super-polynomial T_CYC.
- DATA (§3): the two mechanisms seen at k = 1. (M1) In MWR the cycle set of Ξ_σ never changes and Λ ≡ K1, yet the e-face of the
  flipping gate changes n times: a clock, not the feedback cycle. (M2) In the climbed records (K1F21, K1C16, B400_r32) almost every face
  class change falls on a step where the cycle set of Ξ_σ changes. Neither is a bound.

## 1. Lemma FACE-TARGET (PROVED, lane)
Let g be a gate, t a state.
(a) If wt := wt(g) is a mover: the play from e_g is e_g followed by the play from wt; e_g ∉ Π_t(wt); and class_t(e_g) =
    (Λ_t(wt), E_t(wt) ∪ {e_g}). If wt(g) is c_W: class_t(e_g) = (c_W, ∅) at every t.
(b) If xt := xt(g) is a mover: class_t(β_g) = class_t(xt). If the Ξ-target is X: β_g's frozen successor is u = K0 and class_t(β_g) =
    (K1, ∅) at every t.
Proof. (a) e_g's only successor is wt ([DEF]). If wt's play passed e_g, e_g would lie on the cycle of its own play, so Λ_t(e_g) would be e_g
or more relevant; but B-ONLY applies to e_g (its successor is not c_W): contradiction. So e_g's play is e_g · (wt's play), with the same
cycle: Λ_t(e_g) = Λ_t(wt); e_g is more relevant than Λ (B-ONLY) and so in Π_t(e_g); Π_t(e_g) = Π_t(wt) ∪ {e_g} ([F3] of R118 (b): ext),
and E_t(e_g) = E_t(wt) ∪ {e_g}, a disjoint union. If wt(g) = c_W, e_g's play is e_g, c_W, c_W, …: Λ = c_W, Π = ∅ (nothing on the path is
more relevant than c_W).
(b) β_g's only successor at every state is its frozen start successor xt ([DEF], R118 (a)). If β_g is not on its own play's cycle, its play
is β_g · (xt's play), same cycle, and β_g is not an e-vertex: Λ and E agree. If β_g is on the cycle, so is xt (the next vertex), both
have the same cycle node and their paths before the cycle are empty: E_t(β_g) = E_t(xt) = ∅. Escape: β_g → K0 → K3 → K2 → K1 (LOC-K2)
→ K1: Λ = K1, Π = {K0, K3} (no e-vertex): class (K1, ∅). ∎
- Corollary: D^tot(e_g) = D^tot(wt(g)) (the map class(wt) ↦ (Λ, E ∪ {e_g}) is injective) and D^tot(β_g) = D^tot(xt(g)) (or 1).
- With P-N5-QN GATE-FLIP: flips(g) ≤ (D^tot(wt(g)) − 1) + (D^tot(xt(g)) − 1). With L-RED 63's CLASS-PAYS (lane): flips(g) ≤
  2·min(D^tot(wt(g)) − 1, D^tot(xt(g)) − 1) + 1.

## 2. Theorem EQ (PROVED, lane)
For every genome G: (i) every vertex's class changes at most T_CYC times, so D_mov ≤ T_CYC + 1; (ii) R (R118: steps with no Λ change at
which σ̄ changes somewhere) ≤ Σ_g flips(g), since σ̄ changes only at gates and K2 and σ̄(K2) = K1 at every state (LOC-K2); (iii) by
GATE-FLIP and FACE-TARGET, flips(g) ≤ 2·D_mov − 2, so R ≤ M·(2·D_mov − 2); (iv) by R118's T-CYC and CYC-COUNT (landed), T_CYC ≤ C + R +
(C + R + 1)·N with C ≤ n(2M + 2), n = N + 3M + 6. Hence T_CYC ≤ poly(N, M)·D_mov and D_mov ≤ T_CYC + 1. ∎
- The same holds with D_face := max over gates of max(D^tot(e_g), D^tot(β_g)) in place of D_mov (D_face ≤ D_mov by FACE-TARGET, and
  (iii) uses only D_face). With CLASS-PAYS, D_minface := max over gates of min(D^tot(e_g), D^tot(β_g)) also suffices for (iii):
  flips(g) ≤ 2·D_minface − 1.
- Compare P-N5-QN QUIET-N: T_CYC ≤ Q + (Q + 1)N with Q ≤ Σ_v (D^tot(v) − 1) uses all vertices' heights; Theorem EQ needs only the movers'
  maximum, at the price of the factor M from (iii).

## 3. DATA
Tool k1eq204.py (IDEAL-CYC; box203 gfc203.hist_ideal). Must-0 counters (TOTALS): wfail (unit (gate, state): FACE-TARGET (a) violated,
or e_g ∈ E(wt)), dfail (unit gate: D^tot(e_g) ≠ D^tot(wt(g))), bfail (unit (gate, state): FACE-TARGET (b) violated).
- out/k1eq204_rand_k1_s7.out: 2,000 k = 1 genomes (box202 k1srch202.mk, seed 7): wfail 0, dfail 0, bfail 0.
- out/k1eq204_rand_s2.out: 1,000 rand191 genomes (d 1-6, w 1-3, degree 2-3, seed 2): wfail 0, dfail 0, bfail 0.
- out/k1eq204_k1records.out: MWR4/8/16_2, K1F21_n48, K1C16_n400, L-COMP 15's B400_r32 (copy inst/B400_r32_a13d9661.json, claude/l-comp
  0eb92268, sha1 a13d9661), k1fail_202: wfail 0, dfail 0, bfail 0 on each.
- out/k1eq204_corpus_v1.out: the 53 box 202 genomes and the same k = 1 records, run with the tool BEFORE the bfail column was added
  (wfail 0 and dfail 0 on all 60 rows; bfail not measured there).
- Controls (check204.out): K1EQ_CTRL=1 (e_g not added) wfail 186 on MWR4_2; K1EQ_CTRL=2 (e_g added on the β side) bfail 1,727. Both fire.
### 3.1 Mechanism census at k = 1 (unit: the gate with most flips; class changes of its faces; Ccyc = steps at which the set of cycles of
### Ξ_σ changes; IDEAL-CYC; out/k1eq204_k1records.out, out/k1eq204_corpus_v1.out)
| genome | N | T | C | R | flips | D^tot (e, β) = D^tot (wt, xt) | e-face changes (at Ccyc) | β-face changes (at Ccyc) | Ccyc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MWR4_2 / MWR8_2 / MWR16_2 | 48 / 84 / 156 | 30 / 54 / 102 | 0 | 13 / 25 / 49 | 9 / 17 / 33 | (n + 1, 2n + 2) | n (0) | 2n + 1 (0) | 0 |
| K1F21_n48 | 48 | 31 | 0 | 21 | 21 | (12, 22) | 11 (11) | 21 (21) | 21 |
| K1C16_n400 | 113 | 51 | 0 | 44 | 31 | (22, 37) | 21 (16) | 36 (33) | 35 |
| B400_r32 (L-COMP 15) | 91 | 49 | 0 | 40 | 32 | (18, 34) | 17 (17) | 33 (33) | 33 |
| MW8_2 (k = 2, for comparison) | 84 | 55 | 52 | 2 | 34 | (18, 35) | 17 (17) | 34 (34) | 34 |
- READING: (M1) MWR: Λ ≡ K1, Ξ_σ's cycle set constant for the whole run; the clock lane drives the W-target's class. (M2) the climbed
  k = 1 records and MW: face class changes ride on changes of Ξ_σ's cycle set. In every row the β-face changes about twice as often as
  the e-face (β follows the e-face at non-PRIV states, L-SI 49 NP-SHAPE, plus its own changes).
### 3.2 Scaling of the per-gate record at k = 1 (climbs, aclimb203.py AC_OBJ=flip AC_FREE=1; unit: max flips at one gate)
- From MWR4_2 (N 48): 21 after 2,500 iterations, two seeds (box 203 §5.3; K1F21_n48). From MWR8_2 (N 84): CLIMBS STILL RUNNING at this
  commit; best so far 34 (seed 32) and 23 (seed 31) after 325 iterations (record in the next commit). Both ≈ 0.4·N: no sign of
  super-linear growth at these sizes (two sizes only: says nothing asymptotic).

## 4. What is open, sharpest form (READING)
- k = 1: is D_mov (equivalently T_CYC, Theorem EQ) polynomial on IDEAL-CYC for genomes with Ξ-feedback number 1? Proof side: (k+1)-Λ
  (P-N5-QN §5) pins Λ to {K1, c_t}; a proof must bound how often a mover's e-set can rise under one of two cycle nodes, with the single
  feedback cycle either fixed (M1) or toggling (M2). Kill side: a k = 1 family whose W-targets' e-sets rise super-polynomially often.
- No packet from this box yet: FACE-TARGET and EQ are short consequences of P-N5-QN's premises; they can join P-N5-QN's fix round as a
  remark if the referees ask, or a later packet.
