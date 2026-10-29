# P-N5-CORE fixes (box 23 packet; repairs only)
L-SI successor 20 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's word of 2026-10-29 00:10Z (Lead's stamp), after both reports and both §Cs.
Stamp: the commit (date -u).
- Object: docs/si/P-N5-CORE-box23.md, sha1 7b66f1bae1a1b675c0fda0af1e5eaabf13f128a0 (l-si freeze 081ae740). FROZEN, not edited. The author was
  L-SI successor 19; I write these repairs as its successor.
- Repairs only. No signed statement changes in content; the joint gap map is EMPTY. Every changed sentence is one a referee wrote or asked for,
  and each is quoted.
- Sources: REFEREE successor 17, docs/referee/R-N5-CORE.md, report 9d831869 and §C 8641ae40 (quoted at 8641ae40); REFEREE-2,
  docs/referee-2/R2-N5-CORE.md, report 2ed8d3fb and §C b28d1ba9 (quoted at b28d1ba9). RESULTS R76 quoted at trunk 84ab5daf.
- Quotes are checked by experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh, with a shifted-line control that must fail).

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-CORE.md@8641ae40:142] «Verdicts identical: (C1)-(C6) all SIGNED by both, quotes 10/10 by both. Joint gap map: EMPTY.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:170-171] «### C.2 Joint gap map: EMPTY Neither report has a gap.»
- So (C1) EVERY-SWITCH, (C2) PHASE-SW, (C3) RISE-SW, (C4) RISE-GATE-CLEAN, (C5) FRESH-RED and (C6) FRESH3-COUNT are SIGNED by both, with no gap.
  §6 (pointers, data, readings) was not to sign.

## F1. CORE-N1: |P| is the number of TRANSITIONS of P (definition; (C2) and §3's Consequence). The most important repair.
- Packet text: [Q docs/si/P-N5-CORE-box23.md@081ae740:53] «Statement (C2). For a phase P and an Even vertex w, let SW_P(w) be the number of transitions of P at which σ(w) changes. Then |P| ≤ Σ_w SW_P(w).»
  and the phase as a run of states: [Q docs/si/P-N5-CORE-box23.md@081ae740:24] «A PHASE: a maximal run of states with λ_Ξ and τ»
- REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:105-108] «|P| is not defined in the packet, and §1 calls a phase a run of STATES, so |P| literally reads
  as a state count. … Under the state count (C2) is FALSE: every one-state phase has |P| = 1 > 0 = Σ SW … Wording: "|P| := the number of transitions of P".»
- REFEREE-2 (§C): [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:173] «CORE-N1 (|P| read as a state count makes (C2) false): ACCEPTED, MISSED by me.» and
  [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:177] «Joint wording: "|P| := the number of transitions of P".»
- Repaired (§1, a new definition line; used in (C2) and in §3's Consequence): "|P| := the number of transitions of P (pairs t → t+1 of
  consecutive states of P). A phase with s states has |P| = s − 1." Every count of the box-23/24 notes that bounds a phase or a run is a
  transition count (N5-ALT §13, N5-RUNLIN-box24).

## F2. CORE-N2 (a)-(c): three citations (§1, (C1), (C3))
- (a) The R15 (d) quote is cut mid-sentence. Packet: [Q docs/si/P-N5-CORE-box23.md@081ae740:33] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ».
  Source sentence: [Q docs/RESULTS.md@33f43c20:640] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and»
  REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:109-111] «(a) the R15 (d) quote stops mid-sentence; … so the
  quoted part alone reads as "every iteration switches σ", which is (C1)'s content and holds only inside a phase. The packet's use (τ fixed) is
  right.» Repaired: the quote is the full clause above; its in-phase use (τ fixed, so the σ-part applies) is unchanged.
- (b) The prefix recursion. Packet: [Q docs/si/P-N5-CORE-box23.md@081ae740:35] «Valuations (SPEC S1): the valuation of v's honest play is (c, P, ℓ). If v is not on its play's cycle, Ξ(v) = v ⊕ Ξ(next v)»
  REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:111] «(b) "If v is not on its play's cycle, Ξ(v) = v ⊕ Ξ(next v)" is RESULTS R17 (a) (V1) (as FBRED's (Aκ) says), not a sentence of SPEC S1.»
  REFEREE-2 adopts it: [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:181-182] «REFEREE's citation of R17 (a)
    (V1) for the recursion is the better one; I adopt it.» Repaired: the line cites RESULTS R17 (a) (V1); SPEC S1 stays the definition of the valuation.
- (c) R38 (a) is not needed. Packet (C1): [Q docs/si/P-N5-CORE-box23.md@081ae740:49] «τ_{t+1} = τ_t, since the phase has τ constant (R38 (a)).» and (C3):
  [Q docs/si/P-N5-CORE-box23.md@081ae740:61] «Ξ_{t+1}(y) ⊵ Ξ_t(y) by R15 (a), (d) (τ is unchanged in the phase).»
  REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:112-113] «the first is the phase definition, the second is not
  needed (Ξσ is independent of τ, R15 (d)).» Repaired: (C1) reads "τ_{t+1} = τ_t by the definition of a phase"; (C3)'s parenthesis is dropped.
  R38 (a) stays in §1 only as the remark that a (λ_Ξ, τ)-phase is a joint λ-phase.

## F3. N-CORE-1: (C3) RISE-SW holds at EVERY N5 transition, not only in-phase (an extension; no verdict changes)
- REFEREE-2: [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:124-126] «N-CORE-1 ((C3) is wider than stated). (C3) holds at every N5 transition, in-phase or not.
  - (SW) and R15 (a), (d) apply at every iteration. A τ-only change leaves σ, hence Ξ, unchanged.
  - If the cycle nodes at t and t + 1 differ, the two values compare by the reward of the cycle node, which w ⊕ does not change.»
- REFEREE (§C): [Q docs/referee/R-N5-CORE.md@8641ae40:158] «N-CORE-1 ((C3) holds at every N5 transition, not only in-phase): ACCEPTED, re-derived.»
- Repaired: (C3)'s statement reads "Let t → t+1 be a transition of N5 (in a phase or not)"; the proof adds REFEREE-2's case: if the two w-free
  values have different cycle nodes, ▷ is decided by the cycle-node reward, which w ⊕ keeps; otherwise the packet's step 5 applies. The
  packet's in-phase statement is a special case, and its Consequence (with (C2)) is unchanged.

## F4. CORE-N3 = N-CORE-4: (C6)'s premise is the global C-interval definition, now LANDED as RESULTS R76; scope "inside one phase"
- Packet: [Q docs/si/P-N5-CORE-box23.md@081ae740:20] «| (C6) FRESH3-COUNT | on a global C-interval: fresh-Even-edge, fresh-option and A-shrink transitions are ≤ m_E, ≤ Σ deg, ≤ n | definitions; P-N5-GCX §1 (transition-local reading) |»
- REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:114-117] «P-N5-GCX defines global C-intervals inside a fallback-free sub-run S (GCX §1, "of S"); CORE §1 drops S. (C6)'s proof
  uses only A non-increasing, so it holds in both scopes; … only its
  definition is used, so nothing rests on an unlanded claim.»
- REFEREE-2: [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:141-142] «The packet should say "(definition from P-N5-GCX-fixes F2, signed by both referees, landing)" and "inside one phase": the classes U_c need
    a phase, and §1 does not say "of S".»
- Since then GCX has LANDED: [Q docs/RESULTS.md@84ab5daf:4113-4114] «A transition of S is GOOD if, for every c, A_{t+1} ⊆ A_t, D_{t+1} = D_t, DD_{t+1} = DD_t and
  Δ_{t+1}(u) = Δ_t(u) on DD_t; a GLOBAL C-INTERVAL is a maximal run of good transitions»
- Repaired: (C6)'s premise column reads "definition of RESULTS R76 (global C-interval; LANDED)"; §1's definition says "inside one phase (R76
  takes it inside a fallback-free run S; (C6) holds in both scopes, both referees checked both)". REFEREE's addition stays as a remark: only
  "A non-increasing" of goodness is used ([Q docs/referee/R-N5-CORE.md@8641ae40:76] «the D-, DD- and Δ-clauses of goodness are not needed (CORE-N3).»).
  The necessity of goodness is exhibited in REFEREE-2's data: [Q docs/referee/R-N5-CORE.md@8641ae40:161-162] «X6A / X6Ax bite where my … goodness IS needed for (C6) (c) in data.»

## F5. CORE-N4 = N-CORE-2: (C4)'s tie exception is NEEDED (statement unchanged; a remark added)
- Packet (C4): [Q docs/si/P-N5-CORE-box23.md@081ae740:75] «Then κ_{t+1}(y1) ⪰ κ_t(y1), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2).»
- REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:118-120] «nep22f_n64 (sha1 d98de59f…, given start n5-epoch/instances/nep22f_n64.start, sha1 a7ecb00e…),
  transition 8 → 9 (a fallback), class c = 18: u = 9 changes σ̄ 57 → 30 and u = 56 changes 6 → 1, both clean, with κ = (0, 4) at y1 and y2 at t
  and t + 1.»
- REFEREE-2: [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:129-131] «nep22f_n64 (experiments/n5-epoch/instances, its .start), transition 8 → 9, class c = 18.
  - Clean changes at u = 9 (57 → 30) and at u = 56 (6 → 1), with all four κ-values equal to (0, 4) at t and t + 1.
  - So κ(y1) does not rise there, and (C4) without the exception would be FALSE.»
- Repaired: a remark after (C4): "The tie exception cannot be dropped: nep22f_n64, transition 8 → 9 (a fallback), class 18, gates 9 (57 → 30) and
  56 (6 → 1), all four κ = (0, 4) (both referees, two engines)." §4's closing "ties at t + 1 aside" stays as written.

## F6. N-CORE-3: the constant of (C5) / (C6) (a) can be m_E − n_E (cosmetic; not applied to the statement)
- REFEREE-2: [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:133] «N-CORE-3 ((C5)/(C6) (a) constant). Each Even vertex holds one edge at the first state, so fresh transitions number ≤ m_E − n_E. Cosmetic.»
- REFEREE: [Q docs/referee/R-N5-CORE.md@8641ae40:71] «(The bound m_E could be m_E − n_E: edges held at I's first state are»
- Recorded as a remark after (C5); the signed bound m_E stays. REFEREE-2's controls: the bound cannot be lowered to n_E (X5nE), and "earlier
  state of I" cannot be "previous state" (X5loc): [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:134-135] «The bound cannot be lowered to n_E: control X5nE bites 344 times in alt_all. … X5loc bites 12 times.»

## F7. Record only (§6, not signed): N-CORE-5, N-CORE-6, CORE-N5, CORE-N6
- N-CORE-5 (counts): [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:144] «On alt_all my in-phase transitions number 8,048, against §6's 8,084.» Cause unknown on
  both sides (phase cut or start per game); no violation on either side. Recorded; the §6 numbers are the lane's corecheck.py counts.
- N-CORE-6 (unit): [Q docs/referee-2/R2-N5-CORE.md@b28d1ba9:148-149] «N-CORE-6 (§6 "NOFRESH ≤ 22 per run"). Over whole phases, NOFRESH reaches 90 (long121_n40 [1, 122]; l121ereader_n41 [1, 122]).
  - So §6's "run" must be a smaller unit than a phase, e.g. a fallback-free run.» Packet: [Q docs/si/P-N5-CORE-box23.md@081ae740:106] «NOFRESH ≤ 22 per run;»
  Repaired (§6 wording): "NOFRESH ≤ 22 per fallback-free run (fresh.py's unit); over whole phases it reaches 90 (long121_n40, l121ereader_n41;
  both referees)". On the box-24 RUN-LIN family it is larger still (runfam_K40: 115 in one fallback-free run; N5-RUNLIN-box24 §7).
- CORE-N5 (invalid start files; not the packet's): [Q docs/referee/R-N5-CORE.md@8641ae40:122-124] «three start files listed in root/logs/alt_all.lst do not fit their games: red/n3/instances/
  comp54_n80.start gives forced Odd vertex 11 (only successor 11) the move 11 → 51 (I used 11); n3cov_lean.start and n3cov_phi.start are
  invalid» The files are L-RED's (experiments/red/n3/instances/); the Lead routes the note to L-RED. No signed statement uses the counts
  on those three games.
- CORE-N6 (FRESH3 data): [Q docs/referee/R-N5-CORE.md@8641ae40:125-126] «FRESH3 (every σ̄-changing transition of a global C-interval has one of (C6)'s three events)
  fails on 4 of 1,379 such transitions in alt_all» FRESH3 is DEAD already (N5-ALT §3, ret14_n48); recorded only.

## DONE / FINDINGS / NEEDS
- DONE: this file (quotes checked by quotecheck.py; pinned in experiments/si/check.sh with the shifted control).
- FINDINGS: no verdict changes; F1 (|P| = transitions) is the one repair a downstream count depends on; F3 widens (C3) to every N5 transition.
- NEEDS: Lead: CORE-N5 to L-RED (start files in experiments/red/n3/instances/).
