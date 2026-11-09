# Packet P-N5-BONLY3 (DRAFT, NOT FROZEN): B-ONLY on Γ3 with its pads, and the three caveats it removes
L-SI successor 50 (Opus 5.5), D18 / D14 / D1; Lead ruling 2026-11-09 09:24Z (b): «a NEW small packet, P-N5-BONLY3, frozen only after
L-RED 64 has attacked it». Lane record: docs/si/box96-bonly3.md (claude/l-si 6ee19b24). Labels: PROVED (L-SI lane, unrefereed) /
PROVED-CONDITIONAL (on a named HYPOTHESIS) / DATA / READING (not to sign). Not a TARGET.md claim; not M3 or M4; not a gauntlet step;
G-N5-TIME stays OPEN. Every premise quote below is checked verbatim by experiments/si/box96/pk/quotesB3.py.

## To sign, and what is not to sign
| § | statement | label | premises (§1) |
| --- | --- | --- | --- |
| §2 | Lemma B-ONLY3 | PROVED | [DEF], [DEF3], [FRAME3], [VJ], [OPT] |
| §2 | Corollaries NO-E-CYCLE3, PROVISO3, LAM-UP3 | PROVED | B-ONLY3, [DEF], [DEF3] |
| §3 | Corollary RUN3 (the four on N5′-xi's run, up to its first fallback) | PROVED-CONDITIONAL on HYPOTHESIS [STD3] | B-ONLY3 and its corollaries, [STD3] |
| §4-§5 | caveats removed, DATA, controls | READING / DATA | |

## 1. Premises (each by R-id; quotes verbatim)
- [DEF] RESULTS R104's definition of Γ(G) only: «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β; β of
  priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge to the
  W-target or to the top even self-loop c_W», «a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) →
  {K1, K2}, K3 (Even, top + 3) → {K1, K2}», and its start «with start σ = the genome start at movers, β → its Ξ-target (u when the target
  is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2». Read off (as landed R122's P-ACYC §1 does): [RANK] only c_W
  (even), K0 (even) and K3 (odd) are more relevant than an e-vertex; every e-vertex is even; every other vertex is less relevant than
  every e-vertex; the in-edges of c_W are its loop and the e-vertices whose successor is c_W; the only in-edge of an e-vertex is from its
  gate.
- [DEF3] RESULTS R117's definition of Γ3(G) only: single-successor Even pads of priority ≤ 2, «pA on K0 → K3, s on K1's loop, q on K1 → K0,
  r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k)». So on
  Γ3 the only in-edge of e_g is from pe_g, and the only in-edge of pe_g is from g.
- [FRAME3] (definition; R122's frozen frame): σ is «every Even strategy that agrees with the stated start off the movers (transported
  through the pads on Γ3)»: K0 → pA → K3, K1 → s → K1, K3 → K2, β_g → its Ξ-target or pb_g → u. Odd (the gates and K2) is free. [CORE]:
  in [FRAME3] nothing inside the core leads back to K0, and K3's only in-edge is from K0 (through pA).
- [VJ] RESULTS R118's premise «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)»: the reward of the cycle
  node is compared first (an even priority p gives +p, an odd one −p, priorities injective by rank).
- [OPT] σ̄ is an optimal counterstrategy to σ, as landed R122 uses it: «an optimal counterstrategy being pointwise optimal (at every
  vertex its play value is ⊴ the value under every Odd strategy; RESULTS R57 (b), [1E-N3], as landed in R104)».
- Model: on Γ(G) the same statement is landed RESULTS R123 B-ONLY («at every state t and every vertex v other than c_W and the e-vertices
  whose successor is c_W, Λ_t(v) is less relevant than every e-vertex»); this packet is its Γ3 transcription. No L-RED lane lemma is a
  premise.

## 2. Statements and proofs
**Lemma B-ONLY3.** Let σ be in [FRAME3] on Γ3(G), G any genome, and σ̄ any optimal counterstrategy to σ ([OPT]). For every vertex v other
than c_W, the e-vertices whose successor is c_W, and the pe pads of those e-vertices, the cycle node Λ(v) of the (σ, σ̄)-play from v is
less relevant than every e-vertex.
Proof.
- τ_β := σ̄ changed to the β-face (pβ_g) at every gate, σ̄(K2) kept; a positional Odd strategy.
- Under (σ, τ_β) no play passes an e-vertex after its first vertex unless it starts at e_g or pe_g: the only way into e_g is pe_g, and
  the only way into pe_g is g, which goes to pβ_g ([DEF3]). So no cycle of a τ_β-play contains an e-vertex.
- c_W lies on v's τ_β-play only if the play passes an e-vertex whose successor is c_W ([DEF]: c_W's in-edges), i.e. only if v is such
  an e-vertex or its pe pad: excluded.
- K0 and K3 lie on no cycle in [FRAME3], whatever Odd does ([CORE]).
- So the cycle node w′ of v's τ_β-play is not an e-vertex, c_W, K0 or K3; by [RANK] it is less relevant than every e-vertex, so its
  reward is below every e-vertex's reward (an e-vertex is even; a less relevant vertex has a smaller reward whatever its parity).
- [OPT]: Ω_σ̄(v) ⊴ Ω_τβ(v), and [VJ] compares rewards of cycle nodes first, so reward(Λ(v)) ≤ reward(w′).
- Λ(v) is a cycle node, so not K0 or K3. If it were an e-vertex or c_W (both even, [RANK]), its reward would be at least the least
  e-vertex's reward, above reward(w′). So it is none of these, and by [RANK] it is less relevant than every e-vertex. ∎
**Corollary NO-E-CYCLE3.** In [FRAME3], under (σ, σ̄) no cycle contains an e-vertex.
Proof. A cycle through e_g contains its successor D; D ≠ c_W (c_W's cycle is its loop); so D is a mover, not an exception, and its cycle
node would be e_g or more relevant, against B-ONLY3. ∎
**Corollary PROVISO3.** In [FRAME3], for every gate o with e-vertex e_o and D := e_o's successor: e_o ∉ P(D).
Proof. If D = c_W, P(D) is c_W's loop. Else, e_o ∈ P(D) closes the play at D (the vertex after e_o), so its cycle carries e_o:
NO-E-CYCLE3. ∎
**Corollary LAM-UP3.** In [FRAME3], for every gate o: if Λ(pe_o) = Λ(pβ_o) then e_o is more relevant than Λ(pe_o).
Proof. pβ_o is not an exception, so Λ(pβ_o) ≠ c_W (B-ONLY3). If e_o's successor is c_W, Λ(pe_o) = c_W ≠ Λ(pβ_o). Otherwise pe_o is not
an exception and Λ(pe_o) is less relevant than e_o (B-ONLY3). ∎
- The exception list differs from R123's by the pe pads of the e-vertices with successor c_W only (their plays are pad, e, c_W: no
  choice). No other pad has a forced route to c_W, and pads (priority ≤ 2) are never more relevant than an e-vertex.

## 3. On N5′-xi's run (PROVED-CONDITIONAL on HYPOTHESIS [STD3])
HYPOTHESIS [STD3] (a HYPOTHESIS, not a premise): N5′-xi's states 0, …, T3 on Γ3(G) from S3, i.e. up to its FIRST FALLBACK (iteration
T3 + 1) and not after, are in [FRAME3], and each σ̄_t is an optimal counterstrategy to σ_t.
- Landed form: RESULTS R118 (k) says the run «visits only standard states and makes Howard steps at the movers until its first fallback»,
  but its Theorem is «Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome»; RESULTS R117
  signs ESC3 and W3 for acyclic Ξ-graphs only, and its line states S3-START and PAD for acyclic Ξ-graphs only. So for a Ξ-cyclic G,
  [STD3] rests on R118 (k), which is CONDITIONAL, and is a HYPOTHESIS here.
- Pending form (P-N5-CHAIN DEPENDENCE): P-N5-CHAIN (L-NEW, frozen claude/l-new 93531b03, landing as R125) §3 Theorem REACH3-ALL: «For every
  genome G, the N5′-xi run from S3 on Γ3(G) visits only standard states and its mover parts form a run of HOW3(G) (tie rule: Ξσ-best,
  then SPEC's choice, then the larger index) until its first fallback, at iteration T3 + 1.» When R125 lands, [STD3] is a landed premise.
**Corollary RUN3.** Under [STD3], at every state t ≤ T3 of N5′-xi's run on Γ3(G) from S3 (up to the first fallback only): B-ONLY3,
NO-E-CYCLE3, PROVISO3 and LAM-UP3 hold for (σ_t, σ̄_t). ∎ (Each is a statement about one pair in [FRAME3].)
- The frame is NEEDED (DATA, L-RED 64, claude/l-red 328a6fe2, experiments/red/r230/out/inst.out, bonly3_230.py): after the first
  fallback the conclusion FAILS. On MWR4_2 (frozen, sha1 856d369b…, claude/l-red 406ef2fd r229/inst; L-SI copy box93/inst/MWR4_2.json,
  same sha1) T3 = 30; the fallback at iteration 31 switches K0, then K1, and at the non-standard states 32 and 33 non-exception vertices
  (e.g. 0, 1, 48, 49) have Λ = c_W (vertex 340): 820 violating (state, vertex) pairs. In all, on the pinned instances' non-standard
  states (54,013 violating pairs on 72 such states over 24 pinned genomes). Nothing here is claimed after the first fallback.

## 4. Caveats removed (READING; P-N5-GATE stays frozen)
Under [STD3], in P-N5-GATE (claude/l-si 4066f579, with fixes entries 1-2) on Γ3:
- G1's Γ3 clause (fixes entry 1: «On Γ3 that step needs B-ONLY on Γ3, which is not among this packet's premises»): K10 is empty on Γ3 by
  LAM-UP3.
- E-FACE-PAYS (b), (c) on Γ3: the proviso «D's play avoids e_o» holds at every state by PROVISO3, so S(p_e) = S(D) and relocks ≤ ch_D,
  unlocks ≤ 1 + ch_D, with no proviso.
- WAIT-QUIET on Γ3: no proviso (same reason).
On IDEAL-CYC the same three need no hypothesis: landed R123 B-ONLY (P-N5-GATE fixes entries 1-2; L-RED 63's Lemma PROVISO, claude/l-red
2730ab90).

## 5. DATA and controls (not to sign; experiments/si/box96, check96.sh; engines and pins as box91/pins.txt)
- Set: box 91's 11 and box 93's 8 frozen instances (19; their inst/SHA1SUMS). Engines: own = L-RED R221 own.py (IDEAL-CYC, cap 3000);
  g3 = L-NEW's Γ3 N5′-xi from S3 (to the first fallback or the cap 20000). d96.py counters (TOTALS, must be 0): dpass (unit (gate, t)):
  e_o on P_t(D); lamD ((gate, t), D ≠ c_W): Λ_t(D) at least as relevant as e_o; bonly ((t, v), v not an exception): Λ_t(v) at least as
  relevant as the least e-vertex; sfail (gate): S(p_e) ≠ S(D); relD / unlD (gate): relocks > ch_D / unlocks > 1 + ch_D. All 0 on 19
  instances, both engines, rows identical (883 states, 307,737 (gate, state) pairs per engine).
- Controls: CTRL=anti (Odd non-optimal: e-face at o, β-face at every other gate; own engine): aptpass > 0 on 14 of 19 (648). CTRL=nopad
  (the pad exceptions dropped): bonly 175 / 1,512 / 45 / 2,821 on g3 for WC4_2, C6G8_n54, k1fail_202, MWR4_2, 0 on own: the pad clause is
  needed.
- L-RED 64's independent census (claude/l-red 328a6fe2, R230, bonly3_230.py; Γ3 by L-NEW gamma3, values by si.Engine): IN FRAME
  0 violations (unit (state, vertex); FRAME-X every mover state in the frame (exhaustive up to 2,048, else 2,048 random), the Howard run,
  and N5′-xi's standard states; 24 pinned genomes and 1,900 random Ξ-cyclic genomes, with the exact-VJ-tie Howard states counted apart);
  a brute-force pointwise Odd minimum (M ≤ 8) agrees with si.Engine. OUT OF FRAME (N5′-xi's non-standard states after the first
  fallback): violations, as in §3. Quoted from L-RED's outputs; not re-run here.
