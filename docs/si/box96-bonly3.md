# Box 96: the proviso «D's play avoids e_o» on IDEAL-CYC (PROVISO, independent check) and B-ONLY on Γ3 (lane lemma)
L-SI successor 50 (Opus 5.5), D18 / D14 / D1; Lead 2026-11-09 08:32Z (revised BOX 96) and 08:40Z («go»; notes on premises and scope).
Labels: PROVED (L-SI lane, unrefereed) / HYPOTHESIS (named, not landed) / DATA (unit, set, scope, counter) / DEAD / READING. Nothing
here is a TARGET.md claim, M3 or M4, or a gauntlet step; G-N5-TIME stays OPEN. The frozen packet docs/si/P-N5-GATE.md is NOT edited:
what lands from here goes into a fixes entry or a new packet (§4).

## 0. Answer
- (i) PROVISO on IDEAL-CYC holds; my own derivation from landed R123 B-ONLY (§1) is the argument the Lead relays from L-RED 63
  (claude/l-red 2730ab90, R229-box93 Addendum B; that commit was not on origin when I wrote this, so I checked against the Lead's
  08:32Z summary only, not against L-RED's text).
- (iii) B-ONLY carries over to Γ3 with its pads. Lemma B-ONLY3 (§2, PROVED, lane) is stated in R122's frozen frame (every Even strategy
  that agrees with the transported start off the movers, every optimal Odd counterstrategy), with premises that are all landed
  DEFINITIONS (R104, R117) plus R118 [VJ] and the pointwise optimality of σ̄ (R57 (b), as R122 uses it). The exceptions on Γ3 are c_W,
  the e-vertices whose successor is c_W AND THEIR pe PADS (their plays are pad, e, c_W: no choice). No pad configuration breaks it.
- To apply B-ONLY3 to N5′-xi's run on Γ3 one needs that the run's states 0, …, T3 are in the frozen frame (standard states). That is
  HYPOTHESIS [STD3]: R118 (k) REACH3-CYC (CONDITIONAL in its landed line) or P-N5-CHAIN §3 REACH3-ALL (pending as R125). P-N5-GATE's Γ3
  half already stands on P-N5-CHAIN, so [STD3] adds no new dependency there.
- Removed caveats (§3): with B-ONLY3 and [STD3], on Γ3 (a) G1's Γ3 clause (K10 is empty on Γ3), (b) E-FACE-PAYS (b)'s and (c)'s proviso,
  (c) WAIT-QUIET's proviso. On IDEAL-CYC the same three follow from landed R123 B-ONLY alone.
- DATA (§5): two engines, 19 frozen instances, rows identical; dpass, lamD, bonly, sfail, relD, unlD all 0; the control CTRL=anti (Odd
  made non-optimal) fires on 14 of 19; CTRL=nopad (pad exceptions dropped) fires on g3 only.

## 1. (i) Lemma PROVISO on IDEAL-CYC (independent check; PROVED from landed premises; credit L-RED 63, Lead 08:32Z)
Setting: IDEAL-CYC(G) (RESULTS R118 (a)), any genome, any state t; a gate o with e-vertex e_o and D := e_o's successor (R104: «e of even
priority above every β with one edge to the W-target or to the top even self-loop c_W»).
Statement. e_o ∉ P_t(D).
Proof. If D = c_W, P_t(D) is c_W's self-loop and e_o ≠ c_W. Otherwise D is a mover (a W-target). Suppose e_o ∈ P_t(D). The vertex after
e_o on the play is its only successor D, the play's first vertex; so the play closes there and its cycle is the whole play, which
contains e_o. The cycle node Λ_t(D) is the most relevant vertex of that cycle, so it is e_o or more relevant than e_o. RESULTS R123
Lemma B-ONLY («at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less relevant than
every e-vertex») applies to the mover D and says Λ_t(D) is less relevant than e_o. Contradiction. ∎
Consequence on IDEAL-CYC (no proviso left): P-N5-GATE §3.4 (b) holds at every step, so S(p_e) = S(D) for every gate (if D = c_W both
values are constant); (c) and WAIT-QUIET hold without «D's play avoids e_o»: relocks(o) ≤ ch_D, unlocks(o) ≤ 1 + ch_D, flips(o) ≤
2·ch_D + 1. G1 (K10 empty) and PROVISO now share one premise, R123 B-ONLY.

## 2. (iii) Lemma B-ONLY3 (PROVED, L-SI lane) and its corollaries
Premises (each named; all landed except where marked):
- [DEF3] RESULTS R104's definitions of the genome and of Γ(G) (priorities and edges: Odd gates of priority 1 with a W-face e and a Ξ-face
  β; e even, above every β, one edge to the W-target or to c_W; c_W's in-edges are from those e's and its own loop; the core K0 → {K1,
  K3}, K1 → {K0, K1}, K2 → {K1, K2}, K3 → {K1, K2}) and RESULTS R117's definition of Γ3(G) («4M + 4 single-successor Even pads of
  priority ≤ 2»: pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every
  β_g → u, m_(x,k) on every mover edge). Read off as in R122's P-ACYC §1 (landed): [RANK] only c_W, K0 (even) and K3 (odd) are more
  relevant than an e-vertex, every e-vertex is even, everything else (β's, K1, K2, gates, movers, the unused loop, pads) is less
  relevant than every e-vertex; [CORE] in the frozen frame the only edge into the core is into u = K0, and inside K0 → pA → K3 → K2,
  K2 → r → K1 or its loop, K1 → s → K1.
- [FRAME3] (definition, R122's FROZEN FRAME on Γ3): σ is an Even strategy of Γ3(G) that agrees with R104's start, transported through
  the pads, at every Even vertex that is not a mover; Odd (gates, K2) is free.
- [VJ] RESULTS R118's order ⊴ on values (Λ, Π, k) (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3): the reward of the cycle node first
  (even p gives +p, odd −p, priorities injective by rank).
- [OPT] σ̄ is an optimal counterstrategy to σ: Ω_σ̄(v) ⊴ Ω_τ(v) for every Odd strategy τ and every v (RESULTS R57 (b), [1E-N3], as
  landed in R104 and used by R122).
Statement. In [FRAME3], for every optimal σ̄ and every vertex v other than c_W, the e-vertices whose successor is c_W and the pe pads of
those e-vertices, the cycle node Λ(v) of the (σ, σ̄)-play from v is less relevant than every e-vertex.
Proof.
- τ_β := σ̄ changed to the β-face (pβ_g) at every gate; σ̄(K2) kept. A positional Odd strategy.
- Under (σ, τ_β) no cycle contains an e-vertex: e_g's only in-edge is from pe_g, whose only in-edge is from g ([DEF3]), and g goes to
  pβ_g. No cycle contains c_W unless the play reaches c_W, which needs a level-0 e (c_W's in-edges, [DEF3]); a play enters a level-0
  e only through its pad, i.e. it starts at that pad or e. So for v as in the statement, c_W is not on v's τ_β-play.
- K0 and K3 lie on no cycle in [FRAME3], whatever Odd does: [CORE], nothing inside the core leads back to K0, and K3's only in-edge
  is from K0 (through pA).
- So the cycle node w′ of v's τ_β-play is none of the e-vertices, c_W, K0, K3: by [RANK] it is less relevant than every e-vertex, and
  its reward is below every e-vertex's reward (an e-vertex is even; a less relevant vertex has a smaller reward whatever its parity).
- [OPT]: Ω_σ̄(v) ⊴ Ω_τβ(v), and [VJ] compares rewards of cycle nodes first: reward(Λ(v)) ≤ reward(w′).
- Λ(v) is a cycle node, so not K0 or K3. If it were an e-vertex or c_W (both even, [RANK]), its reward would be at least the least
  e-vertex's reward, above reward(w′). So it is none of these, and by [RANK] it is less relevant than every e-vertex. ∎
Corollary NO-E-CYCLE3. In [FRAME3] under (σ, σ̄) no cycle contains an e-vertex. (A cycle through e_g contains its successor D; D ≠ c_W,
since c_W's cycle is its loop; so D is a mover, not an exception, and its cycle node would be e_g or more relevant: B-ONLY3.)
Corollary PROVISO3. In [FRAME3], for every gate o: e_o ∉ P(D). (§1's proof with B-ONLY3 in place of B-ONLY.)
Corollary LAM-UP3. In [FRAME3], for every gate o: if Λ(pe_o) = Λ(pβ_o) then e_o is more relevant than Λ(pe_o). (pβ_o is not an
exception, so Λ(pβ_o) ≠ c_W; if e_o → c_W, Λ(pe_o) = c_W: LAM fails; else pe_o is not an exception and Λ(pe_o) is below e_o.)
- On Γ(G) the same proof is R123's B-ONLY proof (P-N5-QUIET fixes entry 1, credit L-RED R221 §3), and R122's BETA-ACYC (1)-(4) uses the
  same τ′ move on Ξ-acyclic genomes. B-ONLY3 is not new mathematics; it is the Γ3 transcription with the pads named.
- Where it could have failed: a pad whose play is forced into c_W (the pe pad of a level-0 e) is an exception and is listed; no other
  pad has a forced route to c_W, and pads (priority ≤ 2) are never more relevant than an e-vertex. No pad configuration of R117's Γ3
  breaks the proof; I built none (nothing to build).

## 3. Application to N5′-xi's run on Γ3, and the caveats it removes
HYPOTHESIS [STD3]: N5′-xi's states 0, …, T3 on Γ3(G) from S3 are standard, i.e. each σ_t is in [FRAME3] and σ̄_t is an optimal
counterstrategy. Sources: RESULTS R118 (k) REACH3-CYC (landed CONDITIONAL on P-N5-REACH's [REACH-L] items for every genome; «§4
applies on Γ3 (movers priority 0, pads never cycle nodes by PAD (b), non-mover Even vertices frozen in standard states, Odd = gates and
K2)»); P-N5-CHAIN §3 Theorem REACH3-ALL removes the condition (PENDING, R125). The DATA below measures the run, not the hypothesis.
Under [STD3] (and with no other premise), on Γ3:
- (a) G1's Γ3 clause: K10 (LAM ∧ PRIV ∧ not UP) is empty (LAM-UP3), so GATE-LOW-NULL (b) covers every flip between LAM ∧ PRIV steps.
- (b) E-FACE-PAYS (b) and (c): the proviso «D's play avoids e_o» holds at every state (PROVISO3): S(p_e) = S(D), relocks ≤ ch_D,
  unlocks ≤ 1 + ch_D, with no proviso.
- (c) WAIT-QUIET: a gate whose W-target D changes value at most K times flips at most 2K + 1 times, with no proviso.
On IDEAL-CYC the same three are §1 + R123 B-ONLY (landed), with no hypothesis.
Placement (Lead 08:40Z): never in the frozen P-N5-GATE. Proposed: P-N5-GATE fixes entry 2 for IDEAL-CYC (PROVISO, citing L-RED 63
2730ab90 for the lemma, R123 B-ONLY as the shared premise with G1); B-ONLY3 and its corollaries as a new small packet (or entry 3), so
that L-RED's successor can attack them separately. Lead to decide.

## 4. Reading (not to sign)
- What this buys: on both models, every gate's flips are paid by value changes of ONE mover, its W-target D: flips(o) ≤
  2·min(ch_D, ch_(p_b)) + 1. Summed: R ≤ Σ_o (2·ch_(wt(o)) + 1) ≤ M·(2·max_w ch_w + 1), w over movers. So the R-side of T3 ≤ C + R + (C
  + R + 1)·N is reduced to the movers' own value-change counts. That is a reduction, not a bound: ch_w ≤ T (STEP-BOUND) is circular.

## 5. DATA (experiments/si/box96: d96.py, run96.sh, check96.sh; engines and pins as box91/pins.txt)
- Set: box 91's 11 frozen instances (box91/inst/SHA1SUMS) and box 93's 8 (k1fail_202, Ku_4, Ku_8, Ku_16, Kprev_8, MWR4_2, MWR8_2,
  MWR16_2; box93/inst/SHA1SUMS) = 19. Engines: own (IDEAL-CYC, R221 own.py, cap 3000), g3 (Γ3 N5′-xi from S3, to the first fallback or
  the cap 20000). Unit and counters (TOTALS; must be 0): dpass (gate, t): e_o on P_t(D) [PROVISO, PROVISO3]; lamD (gate, t), D ≠ c_W:
  Λ_t(D) ⪰ e_o [B-ONLY at D]; bonly (t, v), v not an exception: Λ_t(v) ⪰ the least e-vertex [B-ONLY / B-ONLY3]; sfail (gate):
  S(p_e) ≠ S(D); relD / unlD (gate): relocks > ch_D / unlocks > 1 + ch_D.
- Results: on all 19 instances, both engines, dpass = lamD = bonly = sfail = relD = unlD = 0 (883 states, 4,480 gates, 307,737 (gate, state)
  pairs per engine, 3,715 of the gates with D = c_W); the two engines' rows are IDENTICAL (out/own96.out, out/g396.out). tight (gates
  with relocks = ch_D ≥ 1): 1 on MW8_2, MW32_2, MWR*, DWT20_2803; 2 on Ku_*, Kprev_8; 4 on DHIB18_2805; 5 on RWX_n95 (both engines).
- Control CTRL=anti (own engine; Odd at o forced to the e-face, β-face at every other gate, K2 kept; not optimal): aptpass counts (gate,
  t) with e_o on D's play under that Odd strategy. aptpass > 0 on 14 of 19 instances, 648 in all (e.g. C6G8_n54 40,
  DHIB26_2804 99, MWR16_2 102; 0 on FW8_2, FW16_2, MW8_2, MW32_2, Kprev_8; out/ctrl96.out). So the lemma uses Odd's optimality, and the counter can fire.
- Control CTRL=nopad (both engines; WC4_2, C6G8_n54, k1fail_202, MWR4_2; out/nopad96.out by run96b.sh): with the pe pads of the level-0
  e's dropped from the exceptions, bonly = 0 on the own engine (Γ has no pads) and 175 / 1,512 / 45 / 2,821 on g3: the pad clause of
  B-ONLY3 is needed, and it is the only change from R123's list.

## 6. Sources opened (this box)
- docs/RESULTS.md R118 (a), (k), R122, R123 (trunk 547985a10); docs/new/P-N5-QUIET-fixes.md (entry 1, B-ONLY's proof); docs/si/P-ACYC.md
  §1-§2 (frozen frame, [RANK], [CORE], BETA-ACYC); claude/l-red 98143eab docs/red/R229-box94.md Addendum A; claude/l-red fa4e50fe
  docs/red/R229-box93.md §0-§2 (dexact, dpass).
