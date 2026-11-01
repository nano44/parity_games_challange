# N5-ITAU (box 62): a τ-stretch, and even a W-run, does NOT have I_τ = ∅. S4b keeps τ whenever τ is Odd's optimum in its arena against σ, and a σ̄-deviation's own edge can be τ-improving while τ stays (lcount2_n23, a W-run). The closest true form of the Lead's lemma (Lemma ESC-SQUEEZE) holds only at τ-stable states, so it excludes nothing inside a τ-stretch by itself, and R168's ITAU constraint is stronger than N5 requires
L-SI successor 38 (Opus 5.5; D18). Lead 2026-11-01 00:06Z, BOX 62: «Prove, as a lane lemma: "inside one τ-stretch (I_τ = ∅ against τ̄ by
S4b's stop rule), an Odd vertex o whose Ξ-play escape level-matches a gate (the gate's comparison side and o's target read the same
vertex) has a τ-improving edge", or the closest true statement. State what it bounds … If it fails, give the instance (real engine, valid
start).» Written 2026-11-01 from 00:1xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING / DEAD. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a packet.
- Sources opened: docs/red/R168-twolines.md §§0-3 (claude/l-red dcfb682fb: the ITAU constraint and its UNSAT core); docs/new/N5-ssi-global.md
  S2, S4b; docs/RESULTS.md R18 (l. 778) and its source docs/new/N5-time-box21.md §2.2 (Lemma S (a)-(c), with Lemma R: G^d values read on
  G in reversed order); docs/DECISIONS.md L42 (S4b optimality, [S4b-OPT], is NOT covered by R57's premise).
- Notation. At state k: L_k := Ξ_(σ_k) (= Ξ_k), W_k := val(σ_k, τ_k), U_k := U_(τ_k) = val(τ̄_k, τ_k), τ̄_k Even's optimal reply to τ_k. I_τ_k =
  N5's Odd improving edges (S2 on G^d). D_k := {Odd o : σ̄_k(o) ≠ τ_k(o)} (deviators). By Lemma R, (o, w) ∈ I_τ_k ⟺ w ≠ τ_k(o) and
  U_k(w) ◁ U_k(τ_k(o)) (strictly better for Odd under τ̄, in G's order).

## 1. The premise «inside a τ-stretch, I_τ = ∅» is false, even inside W-runs (DEAD, instances verified)
- Why. SPEC S4b: if I_τ ≠ ∅, τ_new is Odd's optimal counterstrategy in the arena H′ (Odd keeps {τ(v)} ∪ I_τ(v)) AGAINST σ (not against
  τ̄). An edge that improves against τ̄ need not be chosen against σ, so τ_new = τ is possible with I_τ ≠ ∅. Then the transition is a
  τ-stretch transition (and, if σ moves, not a fallback).
- Smallest instance: experiments/n5-exhaustive/instances/n3all_maxph_0.pg (n 3, sha1 77f592fe…) with its start (sha1 ed221977…). State 0:
  I_τ = {(2, 1)}, τ_1 = τ_0 (τ(2) = 0 kept), σ moves (Is = {(0, 1), (1, 1)}), no fallback.
- Inside a W-run, with the deviation's OWN edge τ-improving: experiments/red/h3/instances/lcount2_n23.pg (n 23, sha1 dd9847c6…) with its
  start (sha1 7d3626aa…). W-run transition 1: Odd 22 has σ̄_1(22) = 3 ≠ τ(22) = 9, (22, 3) ∈ I_τ_1 = {(22, 3)}, τ kept, σ moves, no fallback.
  - Also red/n5/instances/sym_h8_s1.pg (n 16, default start written out as experiments/si/anc58/inst/sym_h8_s1_default.start): state 3,
    deviations (5 → 9, τ(5) = 6) and (6 → 2, τ(6) = 1) both in I_τ, τ kept (a τ-stretch transition, not in a W-run).
- Faithfulness (this box, all three): startcheck OK; n5b (red/seg/xeng.py) state sequences identical; n5.py's solutions = Oink zlk, both
  strategies verified.
- DATA (experiments/si/anc58/itau.py; corpus output anc58/itau_corpus.txt, 1,132 games):
  - 17,841 τ-stretch transitions; 3,768 have I_τ ≠ ∅ (3,422 not fallbacks; 341 games).
  - 2,647 W-run transitions have I_τ ≠ ∅.
  - Stretch states where some deviation edge (o, σ̄(o)) is itself in I_τ: 896 (1,528 deviations), 585 of them at W-run transitions.
  - On L-RED's builds I_τ = ∅ at every stretch state (ITNE 0 on sr_K2_m6_m4, fbg_K4_m6_m24, fbA_K4_m8_m8). So their runs happen to be
    τ-stable, but N5 does not force it.

## 2. Lemma ESC-SQUEEZE (PROVED, lane): the closest true form, at τ-stable states
- Premises: R18's Lemma S (a)-(b) and Lemma R (source docs/new/N5-time-box21.md §2.2): L_k ⊴ W_k ⊴ U_k pointwise; [PLAY] / Φ for the
  (τ̄_k, τ_k)-play.
- Statement. Let k be a state with I_τ_k = ∅ (τ-STABLE). Then for every Odd o and every successor w of o:
  U_k(w) ⊵ U_k(τ_k(o)) ⊵ W_k(τ_k(o)) ⊵ L_k(τ_k(o)).
  In particular, for a deviator o ∈ D_k with escape x := σ̄_k(o): U_k(x) ⊵ W_k(τ_k(o)). If x's (τ̄_k, τ_k)-play reaches a vertex q after a
  prefix π that avoids that play's cycle node, then Φ(π; U_k(q)) ⊵ W_k(τ_k(o)).
- Proof. I_τ_k = ∅ and Lemma R give U_k(w) ⊵ U_k(τ_k(o)) for all w ∈ succ(o) (no strictly Odd-better successor under τ̄). Lemma S (b) at
  τ_k(o) gives the rest of the chain. [PLAY] on x's (τ̄_k, τ_k)-play gives U_k(x) = Φ(π; U_k(q)). □
- The Lead's form, as a contrapositive (PROVED, same proof). If a deviator's escape x reaches q (in the τ̄-play) along π with
  Φ(π; U_k(q)) ◁ W_k(τ_k(o)), then (o, x) ∈ I_τ_k: o has a τ-improving edge. A «level-matched» escape in R168's sense (in Ξ the escape and
  the gate's comparison side both read q) survives τ-stability only if q's τ̄-value, carried back along the escape, is at least the W-value
  of o's τ-choice (the rider's own reactor side).
- DATA: at the 14,073 τ-stable stretch states of the corpus, 32,179 deviations, 0 violations of U(x) ⊵ U(τ(o)) (SQV 0, a check of the
  dual-side tool). 31,353 of them are strict on both sides: L(x) ◁ L(τ(o)) (Odd prefers x against σ) and U(x) ▷ U(τ(o)) (Odd would not
  take x against τ̄).
  - A naive companion check «L(x) ⊴ L(τ(o))» fails 276 times. That is not an engine fault. [R57] gives Ξ(o) ⊴ val(σ, ρ)(o) for o's
    τ-choice, and that value equals Φ(o; L(τ(o))) only when o is not on τ(o)'s (σ, σ̄)-play. In the 276 cases it is.

## 3. What it bounds (READING)
- Inside a τ-stretch: nothing by itself. ESC-SQUEEZE applies only at τ-stable states. §1 shows τ-stretches and W-runs contain τ-unstable
  states, and even deviations whose own edge is τ-improving, with τ kept. So «a level-matched escape forces a τ-improving edge» does NOT
  give «a level-matched escape forces τ to move». S4b moves τ only when Odd's optimum in H′ against σ differs from τ. That condition
  ([S4b-KEEP]: τ_k is Odd's S1-optimum in H′_k against σ_k) needs an S4b-optimality premise, which L42 says is not covered by R57.
- R168's model. Its ITAU constraint (I_τ = ∅ at every intended state) is SUFFICIENT for τ to stay but not NECESSARY. So R168's
  ITAU-UNSAT («one phase without restart is UNSAT once I_τ = ∅») does not exclude N5 runs in which the level-matched escapes ARE
  τ-improving while S4b keeps τ. The faithful constraint is [S4b-KEEP], i.e. for each deviator o, τ(o) beats every I_τ-edge of o in
  Odd's optimum of H′ against σ. Re-running srz3b.py with [S4b-KEEP] in place of ITAU is the test (handed to L-RED via the Lead).
- Level-3 product generally: ESC-SQUEEZE does not exclude it. Even on τ-stable stretches it is a per-state condition on one escape's
  τ̄-value. It excludes only escapes whose target's τ̄-value, carried back, falls below the rider's W, i.e. the self-referential gate in
  R168's placement with q's τ̄-value low. R168 itself lets q's τ̄-value float (QS free, may sit above the root T), and its UNSAT comes
  from the joint constraints, not from ESC-SQUEEZE alone.

## DONE / FINDINGS / NEEDS
- DONE: this note; anc58/itau.py (+ runitau.sh, itau_corpus.txt); pin anc58/inst/sym_h8_s1_default.start; check.sh «box 62»; DEAD.md «box 62».
- FINDINGS:
  - DEAD (instances verified): «I_τ = ∅ inside a τ-stretch» (n3all_maxph_0, n 3), also inside a W-run with the deviation edge itself
    τ-improving (lcount2_n23, transition 1). Corpus: 3,768 of 17,841 stretch transitions and 2,647 W-run transitions have I_τ ≠ ∅.
  - PROVED (lane): ESC-SQUEEZE at τ-stable states (U(x) ⊵ U(τ(o)) ⊵ W(τ(o)) for every deviator's escape x), and the Lead's form as its
    contrapositive.
  - READING: it excludes nothing inside a τ-stretch by itself. R168's ITAU is stronger than N5 requires: re-test R168 with [S4b-KEEP].
- NEEDS: none from the owner.
