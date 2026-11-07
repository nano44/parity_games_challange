# N5-RET (box 60): the Ξ-side return charge (Lemma KEY-RETURN) is PROVED for every improving-switch SI, but its counting form is already RESULTS R95's RET-ΞRISE, it holds for classical switch-all SI with exponentially many returns, and one Ξ-change pays returns of up to 5N + 2 distinct edges under N5. So it is a relocation onto XI-CH-POLY again, with the degree factor intact
L-SI successor 38 (Opus 5.5; D18). Lead 2026-10-31 22:19Z, BOX 60: «Turn [R167's restart obstruction] into a lane lemma. Candidate
statement: "inside one W-run, an Even vertex y that has moved to a target b cannot return to an earlier target a unless Ξ(a) has risen
strictly past Ξ(b) since y left a" … Then say what it bounds … Check it against XI-CH-POLY: is it a relocation again, or does the
per-option charge avoid the degree factor?» Written 2026-10-31 from 22:2xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING / CONJECTURE / DEAD. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a packet.
- Sources opened: docs/red/R167-restart.md §§0-2 (claude/l-red 339374383); docs/RESULTS.md R95 (Lemma RET-ΞRISE, Theorem XI-RUN,
  Corollary WRUN-EQ; l. 7476); docs/si/N5-ANC-box58.md §§1-2, §5 (ULT, INT, SUCC-MONO, ARM, the switch-all barrier); docs/red/R156-twosource.md §1.
- Premises: [IMP] (SPEC S2, S4a, S4c: a switched Even vertex enters an improving target), [R15a] (Ξ_(k+1) ⊵ Ξ_k pointwise), and box 58's
  SUCC-MONO / ULT / INT (lane-proved from these two). Nothing else: no W-run hypothesis, no S4a optimality, no [R57].

## 1. Lemma KEY-RETURN (PROVED, lane)
- Setting. Even y leaves a for b at t0 (σ_(t0)(y) = a, σ_(t0+1)(y) = b) and next enters a again at t1 > t0 (σ_(t1)(y) = c ≠ a,
  σ_(t1+1)(y) = a): a RETURN of y to a. Let g := key(Ξ_(t0)(a), Ξ_(t0)(b)), the GAIN of the leave (box 58 §1 keys).
- Statement.
  - (i) Ξ_(t0)(a) ◁ Ξ_(t0)(b) ⊴ Ξ_(t1)(c) ◁ Ξ_(t1)(a). In particular Ξ_(t1)(a) ▷ Ξ_(t0)(b): Ξ(a) has risen strictly past the value b had
    when y left a (the Lead's candidate, read with b's value at the leave).
  - (ii) If y returns directly (c = b), then Ξ_(t1)(a) ▷ Ξ_(t1)(b) too. If c ≠ b, nothing is claimed about the current Ξ(b).
  - (iii) Some change of Ξ(a) at a transition u ∈ [t0, t1) has key κ_u(a) ≥ g.
- Proof. (i) [IMP] at t0: (y, b) ∈ Iσ_(t0), so Ξ_(t0)(b) ▷ Ξ_(t0)(a) (S2). [R15a]: Ξ_(t0)(b) ⊴ Ξ_(t0+1)(b) = Ξ_(t0+1)(σ_(t0+1)(y)).
  SUCC-MONO (box 58 §2): Ξ_(t0+1)(σ_(t0+1)(y)) ⊴ Ξ_(t1)(σ_(t1)(y)) = Ξ_(t1)(c). [IMP] at t1: (y, a) ∈ Iσ_(t1), so Ξ_(t1)(a) ▷ Ξ_(t1)(c).
  (ii) c = b in (i). (iii) From (i), Ξ_(t0)(a) ◁ Ξ_(t0)(b) ◁ Ξ_(t1)(a), so INT gives g ≤ key(Ξ_(t0)(a), Ξ_(t1)(a)), and ULT along
  t0, …, t1 bounds that by max_(t0 ≤ u < t1) κ_u(a). □
- Relation to what exists. (iii) is box 58's ARM read from the leave instead of the arming time. Its counting consequence (returns of y
  to a in a W-run ≤ the transitions changing Ξ(a): distinct returns have disjoint windows [t0, t1)) is RESULTS R95's Lemma RET-ΞRISE
  (RET_F(X, g) ≤ ΞCH_F(g)), landed and refereed. KEY-RETURN adds only the crossing (i) and the key level (iii).
- DATA (experiments/si/anc58/retxi.py; corpus output anc58/retxi_corpus.txt, 1,132 games): 6,265 returns inside W-runs; PASSV 0,
  CURV 0, KEYV 0, CHARGEV 0. R167's pin sr_K2_m6_m4 (copied read-only from claude/l-red 339374383 into anc58/inst/; startcheck OK,
  n5b identical, Oink zlk OK, strategies verified): 24 returns, 0 violations, MAXRET 2.

## 2. What it bounds (REDUCTION, already landed)
- Per Even y and W-run F: SW_F(y) ≤ deg(y) + Σ_(a ∈ succ(y)) ΞCH_F(a) (one first entry per option, then returns).
- Summed: |F| ≤ m_E + Σ_c d_E(c)·ΞCH_F(c). That is R95's Theorem XI-RUN, and R95's WRUN-EQ already states WRUN-POLY ⇔ XI-CH-POLY.
- So the return charge bounds switches, and hence W-run length, by Ξ-changes of the options. It is a relocation onto XI-CH-POLY, the
  same as R95.

## 3. Does the per-option charge avoid the degree factor? NO (DATA, READING)
- Fan-out. One Ξ-change (a, u) pays one return for EVERY Even y with an edge to a that is waiting to come back. The factor is d_E(a),
  exactly the coefficient in XI-RUN. retxi.py's SHARE = the largest number of returns whose first key-≥-gain charge is the same change:
  | game | n | RET (W-runs) | SHARE |
  | --- | --- | --- | --- |
  | switchbestexp_4 … _8 (new/box54/out) | 109, 134, 159, 184, 209 | 76, 92, 112, 128, 148 | 22, 27, 32, 37, 42 |
  | fc_3 … fc_8 (new/box59/out) | (L-NEW family) | 60, 71, 85, 103, 117, 135 | 17, 22, 27, 32, 37, 42 |
  - SHARE = 5N + 2: one Ξ-change pays linearly many returns. Corpus maximum 42.
- Composition up the levels. Ξ(y) changes only when y switches or Ξ(σ(y)) changes (Ξ(y) = Φ(y; Ξ(σ(y))), [PLAY]). So
  ΞCH_F(y) ≤ SW_F(y) + Σ_a ΞCH_F(a) ≤ deg(y) + 2·Σ_a ΞCH_F(a). Over a depth-d dependency this compounds to a factor up to (2·deg)^d,
  and shared options are counted once per edge. That is the same shape as k-SOURCE's (K_b + 1) per level (R156), and no better.
- Barrier (DEAD as a route to a polynomial bound). KEY-RETURN uses only [IMP] and [R15a], so classical switch-all SI satisfies it.
  anc58/retxi.py --si on switchallexp_N (anc58/inst):
  | N | RET | MAXRET (one (y, a)) | SHARE | violations (PASSV, CURV, KEYV, CHARGEV) |
  | --- | --- | --- | --- | --- |
  | 4 | 1,077 | 36 | 14 | 0 |
  | 5 | 2,745 | 76 | 17 | 0 |
  | 6 | 6,589 | 156 | 20 | 0 |
  - Every return is charged, and the run is exponential (box 58 §5). So no polynomial bound can follow from KEY-RETURN plus generic SI
    facts. The extra ingredient has to be N5-specific: τ fixed and λ_W constant on the W-run, S4a's W-optimum, W-MON.

## 4. Reading of R167 through KEY-RETURN (READING)
- R167's RESTART (hs2 from its top rider dd5 back to dd1 at a new phase) is a return of hs2 to dd1. By KEY-RETURN (i) / (iii) it needs
  Ξ(dd1) to cross the value Ξ(dd5) had when hs2 left dd1, at a key ≥ that climb's gain. In R167 every rider's Ξ ends at hps (the
  self-referential escape). So the needed key is a band marker, and R167's z3 UNSAT is about placing those markers jointly with the gate
  (CLOSED / WAVE / FLIP). That joint constraint is model-specific. It is NOT a consequence of KEY-RETURN, which switch-all SI satisfies
  while it counts exponentially.
- The N5-specific part of R167's obstruction is the split: S4a takes only Ξ-improving edges but chooses among them by W. A restart that
  W wants (the ladder dominates) waits for a Ξ-crossing. A lemma that would use this must say that the Ξ-crossing a restart needs
  cannot be produced, inside one W-run, by the very level it restarts. That is the open core (XI-CH-POLY / DESC) in another form. I have
  no proof of it. Not stated as a conjecture: I have no precise statement that the data supports.

## DONE / FINDINGS / NEEDS
- DONE: this note; anc58/retxi.py, runretxi.sh, retxi_corpus.txt; pin anc58/inst/sr_K2_m6_m4.{pg, start}; check.sh «box 60»; DEAD.md «box 60».
- FINDINGS:
  - PROVED (lane): KEY-RETURN (crossing past b's value at the leave; key ≥ gain). Its counting form is already R95's RET-ΞRISE.
  - REDUCTION: it bounds switches / |F| by Ξ-changes of options (R95 XI-RUN). A relocation onto XI-CH-POLY.
  - DEAD as a route: switch-all SI satisfies it (switchallexp_6: 6,589 returns, 0 violations).
  - DATA: the per-option charge keeps the degree factor (SHARE 5N + 2 on switchbestexp_N and fc_N; corpus max 42).
- NEEDS: none from the owner.
