# R230 item 4: adversary vs L-NEW 69 BOX 205 (Lemma BETA-LOC, Corollaries NOCYC-NOFLIP, K1-BASIN)
L-RED successor 64 (Opus 5.5), D1 / D18 / D14. Lead routing 2026-11-11 22:00Z. Written 2026-11-11T23:04Z (date -u).
Object: claude/l-new 1478886e docs/new/N5-BETALOC-box205.md; `git show 1478886e:docs/new/N5-BETALOC-box205.md | sha1sum` = 8431936c
(79 lines). Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.

## 0. Verdict
- BETA-LOC SURVIVES on IDEAL-CYC. Every case of the proof checks against R123 (B-ONLY, LOC-GATE, LOC-K2, [OPT]), R118 [VJ] and P-N5-QN's
  readings D2 / D3 of R104's [DEF]. I found no counterexample: independent engine, 3,000 random genomes and a climb (§3).
- NOCYC-NOFLIP and K1-BASIN SURVIVE as mathematics. Their LABEL is wrong: both use P-N5-QN Lemma (k+1)-Λ, which is signed but NOT
  landed (trunk RESULTS.md mentions «P-N5-QN» 0 times). The box labels them «PROVED (lane)»; they are PROVED-CONDITIONAL on (k+1)-Λ
  (G1). §4 of the box does name the dependence, but the labels in §0 and §2 do not carry it.
- SCOPE: everything is on IDEAL-CYC(G) (box l. 6). Nothing is claimed on Γ3 or for N5′-xi, and nothing transfers there for free (G2;
  the B-ONLY3 lesson).
- G-items G1-G5, none of which changes a statement.

## 1. Proof read (box §1-§2), case by case
- (i) and the play P0. By (i) the movers x_1, …, x_m on the Ξ_σ-path from xt(g) are distinct and x_m's option has Ξ-target X.
  - On IDEAL-CYC every β is frozen at R104's start (R118 (a)): β → xt if xt ≠ X, else β → u = K0. Then K0 → K3 → K2 (frozen), K2 → K1
    (Odd), K1 → K1. So P0 is a (σ_s, τ) play for the stated τ.
  - Distinctness of the β's before K0, including β_g itself: if some x_i is g's owner x, then σ_s(x) ≠ j, because otherwise x's Ξ edge
    is xt(g) = x_1, the path from x_1 cycles, and (i) fails. So β_(x, σ_s(x)) ≠ β_g, and the Odd strategy is well defined. The box
    states distinctness but not this reason (→ G4).
- V0. Cycle node K1 (priority 5). Π0 = {β's on P0, K0, K3}: movers (0), gates (1) and K2 (3) are below K1. Correct. [OPT] gives
  Ω(β_g) ⊴ V0.
- Λ(e_g) even, c_W included. A positive reward beats K1's negative reward. Correct.
- Λ(e_g) = K1. By B-ONLY, K1 is less relevant than e_g, so e_g ∈ Π(e_g) \ Π0, and the most relevant z of the symmetric difference
  satisfies z ⪰ e_g.
  - By D2 (P-N5-QN l. 43-44 «(D2) E-DOM: every vertex more relevant than an e-vertex is an e-vertex, c_W, K0 or K3»), z is one of
    those. c_W lies on no K1-play.
  - K0 and K3 are in both Π's: by D3 («the core is entered from outside only at u = K0»), K0 → K3 is frozen.
  - Π0 has no e-vertex. Π0 \ Π(e_g) holds only β's, which are below every e.
  - So z ∈ Π(e_g) is an even e-vertex, and Ω(e_g) ▷ V0 ([VJ]: same cycle node, so the symmetric difference decides).
  Correct.
- Λ(e_g) odd and ≠ K1: excluded by (ii).
- LOC-GATE (R123: «σ̄_t chooses the face of strictly ⊴-smaller value») then gives σ̄_s(g) = β_g. Correct.
- NOCYC-NOFLIP. P-N5-QN §5 (l. 122-131, l-new 1478886e, sha1 97254bd2): «the cycle nodes Λ_t(v), over all vertices v other than c_W,
  c_X and the e-vertices whose successor is c_W, take at most k + 1 values: K1, and the most relevant vertex of each cycle of …
  Ξ_σ». With Ξ_σs acyclic, Λ(e_g) ∈ {K1, c_W}, so (ii) holds; and (i) holds at every gate. Correct. Both states acyclic means
  σ̄ = β at every gate at t − 1 and at t, so there is no flip.
- K1-BASIN. Correct as written: «Ξ_σs has at most one cycle» is (k+1)-Λ's last sentence, at k = 1. My check (§3, kfail) tests the
  per-state form at every state with exactly one Ξ cycle, on any genome. There c_s is the most relevant vertex among Z's movers and
  their chosen gates and β's, the Γ-cycle of (k+1)-Λ's proof.

### G-items (no statement changes)
- G1 Labels. NOCYC-NOFLIP and K1-BASIN should be «PROVED-CONDITIONAL on P-N5-QN Lemma (k+1)-Λ (signed by both referees, not landed)»,
  in §0 and §2, not «PROVED (lane)». Alternative: inline (k+1)-Λ's proof. It is 9 lines, and its premises are landed R123 B-ONLY,
  LOC-K2 and [DEF] (P-N5-QN §5), so the corollaries would become unconditional at lane level.
- G2 Scope sentence. Add: «IDEAL-CYC only. Nothing here is claimed on Γ3 or for N5′-xi.» A Γ3 form would need:
  - B-ONLY3 (P-N5-BONLY3, l-si 681bfccf) in [FRAME3];
  - LOC-GATE and LOC-K2 on Γ3 (not landed);
  - P0 rebuilt through the pads (pβ, pb, pA, r, s);
  - [STD3] for N5′-xi's run, which gives nothing after the first fallback (L-RED R230, MWR4_2 states 32-33, where B-ONLY3's
    conclusion fails).
- G3 Premise quotes. The box names its premises (B-ONLY, LOC-GATE, LOC-K2, [OPT], D2, D3) but quotes none. Its one external quote
  («Odd takes the β-face at every gate», R122) is verbatim (script). Quote the five lines; I did above, and they match trunk 98e1c8bee /
  l-new 1478886e.
- G4 Distinctness of P0. Add the one-line reason (§1, first bullet): σ_s(x) ≠ j whenever g's owner is on the path, by (i). Also cite
  R118 (a) for the frozen β edge β → xt / u.
- G5 DATA engine. The box's DATA uses one engine family (box203 gfc203 + box191 idealcyc). My engine (r221q/own.py: own builder, own
  VJ order, Odd SI) is independent and also finds 0 (§3). Cite it as a second engine if wanted.

## 2. DEAD instance re-check
inst/naive_k1_s71.json: `git show 1478886e:experiments/new/box205/inst/naive_k1_s71.json | sha1sum` = 335a5709, equal to box205
inst/SHA1SUMS. On my engine the control (premise (i) only, e-face) fires 3 times, with bfail = nfail = kfail = 0. That matches the box's
«naive 3» and K1-BASIN case (b).

## 3. Counter side (DATA; experiments/red/r230/betaloc230.py, sha1 cc834746; climbbl230.py)
Engine: L-RED r221q/own.py (IDEAL-CYC from the genome's start; Howard ties keep current, then larger index; Odd SI). No L-NEW code.
Counters (unit (gate, state) pairs unless named):
- prem: pairs meeting (i) and (ii).
- bfail: prem pairs on the e-face.
- nfail (unit: gate flips): flips at steps with Ξ_σ acyclic at t − 1 and t.
- kfail: at states with exactly one Ξ cycle Z, pairs on the e-face with (i) and not (Λ(e_g) = c and c odd).
- ctrl: pairs with (i) only, on the e-face (the control).
- multi (unit: states): states with ≥ 2 Ξ cycles.
| set | states | prem | bfail | nfail | kfail | ctrl | flips | acyc steps | multi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| naive_k1_s71, MWR4_2, MWR8_2, K1C16_n400 (4) | 142 | 15,788 | 0 | 0 | 0 | 3 | 166 | 3 | 0 |
| rand seed 2310 (3,000; d 1-6, w 1-3, degree 2-3, Ξ-cyclic allowed) | 11,652 | 53,631 | 0 | 0 | 0 | 4,079 | 18,947 | 362 | 3,633 |
| climb P (seed 2309, from naive_k1_s71, N ≤ 16, deg ≤ 3; score (bfail + nfail + kfail, ctrl, flips)) | see out/climbblP.out | | 0 | 0 | 0 | best 346 | | | |
- The control fires (4,079 random pairs; climb best 346 in one genome), so the counters can see e-face pairs off the premise; premise
  (ii) is what keeps them at 0.

## 4. Sources opened
docs/RESULTS.md R118 (a), R122, R123 (trunk 98e1c8bee); l-new 1478886e docs/new/N5-BETALOC-box205.md, docs/new/P-N5-QN.md §1 (l. 43-44),
§5 (l. 122-131), experiments/new/box205/inst/naive_k1_s71.json + SHA1SUMS; L-RED r221q/own.py (engine).
