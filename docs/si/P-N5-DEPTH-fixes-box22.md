# P-N5-DEPTH fixes (box 22 packet; repairs only)
L-SI successor 19 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's GO of 2026-10-28 22:36Z (Lead's stamp), after both reports and both §Cs.
Stamp: the commit (date -u).
- Object: docs/si/P-N5-DEPTH-box22.md, sha1 549c7fb72d767293b6bf2ae5bbbb8809084df707 (l-si freeze 2201aa2d). FROZEN, not edited. The author was
  L-SI successor 18; I write these repairs as its successor.
- Repairs only. No signed statement changes in content; the joint gap map is EMPTY. Every changed sentence is one a referee wrote or asked for,
  and each is quoted.
- Sources (trunk 4eb5cbfb): REFEREE successor 16, docs/referee/R-N5-DEPTH.md, report 1d74c963 and §C f5081a6a (stamps at dc4e47b8; quoted at
  dc4e47b8); REFEREE-2 successor 18, docs/referee-2/R2-N5-DEPTH.md, report dad93591 and §C d8402f3d (quoted at 4eb5cbfb).
- Quotes are checked by experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh, with a shifted-line control that must fail).

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-DEPTH.md@dc4e47b8:121-122] «Verdicts identical: N-MONO (greatest reading), ABS-DEPTH, STATIC-DEPTH, PURE-END,
  GCI-LEN-ρF SIGNED; §4 instance confirmed by both. Joint gap map: EMPTY.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-DEPTH.md@4eb5cbfb:131] «Result: no disagreement. Joint map empty.»
- So Fact N-MONO (read as below), Theorem ABS-DEPTH, Theorem STATIC-DEPTH, Corollary PURE-END and Corollary GCI-LEN-ρF are SIGNED by both, with no
  gap. §4-§6 (instance, data, OPEN, CONJECTUREs, READING) were not to sign.

## F1. DEPTH-N1 = N-DEPTH-1: "pointwise maximal" means pointwise GREATEST (wording; §1, model and N-MONO)
- Packet text: [Q docs/si/P-N5-DEPTH-box22.md@2201aa2d:54-55] «Proof: s_t is valid and uses only its own choices, which are arena edges, so it is a
  candidate; s_{t+1}'s N is pointwise maximal among the candidates.»
- REFEREE: [Q docs/referee/R-N5-DEPTH.md@dc4e47b8:106-107] «N-MONO, and with it ABS-DEPTH's last step and (TERM)'s fixed point N*, need "pointwise
  maximal" read as pointwise greatest; say so (the same point as GCX-N4).»
- REFEREE-2: [Q docs/referee-2/R2-N5-DEPTH.md@4eb5cbfb:100-101] «"pointwise N-maximal" must mean pointwise GREATEST (dominating every candidate).
  Otherwise N_{t+1} ⪰ N_t does not follow.»
- Repaired: in §1's model and in N-MONO's proof, "pointwise maximal" reads "pointwise GREATEST (it dominates every valid arena strategy, s_t
  included)". This is the same repair as P-N5-GCX-fixes-box21 F6 (GCX-N4).

## F2. DEPTH-N2 = N-DEPTH-3: CONJECTURE ABS-DEPTH-TIE is FALSE as stated; restated for keep rules (not signed; §6)
- Packet text: [Q docs/si/P-N5-DEPTH-box22.md@2201aa2d:148-149] «CONJECTURE ABS-DEPTH-TIE: in the model, the run is fixed within max d* steps
  without GEN.»
- REFEREE: [Q docs/referee/R-N5-DEPTH.md@dc4e47b8:108-109] «False as stated for general deterministic rules (the one-vertex game, rules anti /
  sizedep; §3). Restate it for rules that keep a maximal current choice (or order-consistent rules), where my data show no counterexample.»
- REFEREE-2's instance: [Q docs/referee-2/R2-N5-DEPTH.md@4eb5cbfb:108-109] «Non-terminals 0, 1; terminals T2 (h 0, T 2) and T3 (h 2, T 2); succ(0) =
  {T2}, succ(1) = {0, T2, T3}; w = (−2, −1); start s(1) = 0. … Run: s(1) = 0 → T2 → T3, fixed after 2 steps, against max d* = 1.»
- Repaired (§6, CONJECTURE): "DEAD for general deterministic rules (instances above; the mechanism of G-GCX-1). CONJECTURE ABS-DEPTH-TIE_keep: for
  tie rules that keep a maximal current choice, the run is fixed within max d* steps without GEN." CONJECTURE STATIC-DEPTH-TIE (N5's own S1 rule)
  is not touched, as REFEREE says.

## F3. DEPTH-N3: GCI-LEN-ρF does not use the global C-interval structure (scope; §3)
- Packet text: [Q docs/si/P-N5-DEPTH-box22.md@2201aa2d:115-116] «Let [a, b] be a global C-interval (quoted above) of a λ_W-constant fallback-free run in
  one phase. Suppose σ̄ is constant on it, it satisfies (H3) and (H4)»
- REFEREE: [Q docs/referee/R-N5-DEPTH.md@dc4e47b8:110-111] «The proof does not use that [a, b] is a global C-interval. The corollary is STATIC-DEPTH
  read on any interval of a λ_W-constant fallback-free in-phase run with σ̄ constant, (H3), (H4) and GEN_W.» REFEREE-2 accepted it
  ([Q docs/referee-2/R2-N5-DEPTH.md@4eb5cbfb:123-124] «CORRECT, I accept it (missed by me)»).
- Added after the corollary: "The proof does not use the global C-interval structure: the bound holds for every interval of a λ_W-constant
  fallback-free in-phase run on which σ̄ is constant and (H3), (H4), GEN_W hold."

## F4. N-DEPTH-2: STATIC-DEPTH's length step is global (scope remark; §2)
- REFEREE-2: [Q docs/referee-2/R2-N5-DEPTH.md@4eb5cbfb:102-104] «The bound b − a ≤ max d* uses "σ unchanged ⇒ fallback". So it needs every Even vertex
  of the game settled, not only those of one class. The class-restricted settling (each v settled from a + d*(v)) holds by the same induction for
  any set closed under H_b-successors.» REFEREE accepted it ([Q docs/referee/R-N5-DEPTH.md@dc4e47b8:128] «N-DEPTH-2 (STATIC-DEPTH's length step is
  global): ACCEPTED.»).
- Added after STATIC-DEPTH's proof: "The per-vertex part restricts to any set of vertices closed under H_b-successors. The length conclusion
  b − a ≤ max d* is global: it uses that σ is unchanged on the whole game. A per-class length bound does not follow." This is what breaks
  P-N5-DEPTH-add's PURE-LEN (G-DADD-1; see P-N5-DEPTH-add-fixes-box22 F2).

## F5. Data notes (DEPTH-N4, N-DEPTH-4, N-DEPTH-5): recorded, nothing to repair
- DEPTH-N4: [Q docs/referee/R-N5-DEPTH.md@dc4e47b8:112-113] «Sharpness (length = max d*) is common in natural data (920 intervals over the four sets).
  The theorem's bound is attained, not slack.»
- N-DEPTH-4 (GEN_W checked in its used form; 13 local failures with the conclusion intact in REFEREE-2's corpus, 0 in REFEREE's) and N-DEPTH-5
  (coverage: GCI-LEN-ρF covers 3,499 of 4,747 global C-intervals in REFEREE-2's corpus) are corpus notes. REFEREE accepted N-DEPTH-5 and called
  N-DEPTH-4 a corpus difference.

## Not changed
No signed statement changes in content. F1 is the model's reading. F2 concerns an unsigned conjecture. F3, F4 are scope remarks. F5 is data.
Scope as the packet states it: ABS-DEPTH is about an abstract model; STATIC-DEPTH and GCI-LEN-ρF bound only the intervals they cover; nothing here
bounds N5's running time; not a TARGET.md claim; G-N5-TIME stays OPEN.
