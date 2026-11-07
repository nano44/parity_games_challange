# N5-WRE (box 59): the repaired W-REOPEN (an Even vertex of the escaped cycle SWITCHES between the two escapes) holds on all data, and reduces to a witness lemma WIT through two PROVED transfer lemmas. But the per-escape form of the data mechanism is DEAD (frz40), and the repaired form bounds PLAT only by W-changes or Even switches, both still the open core
L-SI successor 38 (Opus 5.5; D18). Lead 2026-10-31 (successor-38 brief, ITEM 1, BOX 59): «Test the repaired form on the corpus and the
pins with your predecessor's wrise.py. If it holds, attempt a proof using signed ODD-STEP / NO-RET (P-N5-ODD) and S4a W-monotonicity
(L-RED R164, lane). Also record what it would give … say whether the repaired W-REOPEN bounds PLAT by a quantity that is NOT itself the
open core.» Written 2026-10-31 from 20:5xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING / CONJECTURE / DEAD. Not a TARGET.md claim. G-N5-TIME stays OPEN. Not a packet.
- Sources opened: docs/si/N5-ANC-box58.md §§1-11 (this lane; W-REOPEN §8, ESC-XCH §9, WCH §11); docs/red/R166-wreopen.md
  (claude/l-red b31f9477); docs/si/P-N5-ODD-box57.md §§1-3 (frozen, sha1 03eec41d; ODD-STEP, NO-RET, [R15a], [R57], [PLAY], Φ-comp);
  docs/red/R155-recursion.md §2 (ONE-SOURCE) and docs/red/R156-twosource.md §1 (k-SOURCE); docs/new/N5-ssi-global.md S1-S5.
- Premises: as box 58 (P-N5-ODD §1: [R15a], [R57], [PLAY] / Φ / Φ-comp) plus [W-MON] (L-RED R164, lane-proved, NOT refereed): inside a
  W-run F, W_(k+1) ⊵ W_k pointwise, where W_k := val(σ_k, τ) and τ is F's fixed Odd strategy. Every result below that uses W-MON is
  CONDITIONAL on it (lane-proved only).
- Notation (box 58): an escape (s, u) is an Odd s leaving x := σ̄_u(s) at u whose new choice closes s into a cycle
  Z_u := s, x, … (x's (σ_(u+1), σ̄_(u+1))-play back to s). Consecutive escapes u1 < u2 of one (s, x) in one W-run form a REPEAT.
  x₂ ranges over s's other choices in (u1, u2].

## 1. The repaired statement and the data (DATA)
- CONJECTURE W-REOPEN′ (L-RED R166's repair): inside a W-run, if some Even vertex e of Z_(u1) ∪ Z_(u2) switches at a transition
  t ∈ [u1, u2], then W(x) or W(x₂) strictly rises between u1 and u2.
- Tool experiments/si/anc58/wrise2.py (execs anc.py, so startcheck applies). It splits repeats by six readings of «switches between»
  (open (u1, u2), half-open [u1, u2), closed [u1, u2]; on Z1 ∪ Z2, on Z1, on Z2, on Z1 ∩ Z2) and EVEN_NOSW (both cycles have an Even
  vertex, none switches in [u1, u2]: R166's shape). Corpus output anc58/wrise2_corpus.txt (anc58/corpus_fixed.lst, 1,132 games).
  | input | repeats | SW_CLOSED (in scope) | SW_CLOSED no rise | EVEN_NOSW | EVEN_NOSW no rise | Odd-only |
  | --- | --- | --- | --- | --- | --- | --- |
  | corpus (1,132 games) | 121 | 63 (SW_OPEN 62) | 0 | 54 | 0 | 4 |
  | lean_29_35 (R166 pin) | 2 | 1 | 0 | 1 | 1 | 0 |
  | leanc_29_35 (R166 pin) | 2 | 1 | 0 | 1 | 1 | 0 |
  | fbA_K8_m8_m8 (R164 pin) | 28 | 28 | 0 | 0 | 0 | 0 |
  | pp_K48_n449 | 45 | 0 | 0 | 45 | 0 | 0 |
  | switchbestexp_5 | 3 | 3 | 0 | 0 | 0 | 0 |
  - Every one of the six readings has 0 violations everywhere. R166's violating repeat (s 35, x 29, u 12 → 21, swap key (1, 45)) has
    no switching Even vertex on either cycle (the subdivision vertex e is forced, or never takes its second edge), so it falls outside
    the repaired scope (EVEN_NOSW 1, EVEN_NOSW_NOWRISE 1), as R166 predicted.
  - Pins copied read-only from claude/l-red b31f9477 into experiments/si/anc58/inst/ (sha1s match red/wre/pins.sha1). startcheck OK,
    n5b (red/seg/xeng.py) state sequences identical, n5.py solution = Oink zlk, both strategies verified (this box, both pins).
- So W-REOPEN′ SURVIVES on all data. Its scope is narrow: 63 of the 117 corpus repeats with an Even vertex on the cycles.

## 2. Mechanism (DATA): the rise happens at the FIRST escape, carried along x's W-play by a switching vertex of Z
- Tool anc58/wsw.py (corpus output anc58/wsw_corpus.txt). For every in-scope repeat (63 corpus, 28 fbA_K8_m8_m8, 3 switchbestexp_5,
  1 on each R166 pin):
  - x ≠ τ(s) at both escapes (XTAU 0; SIND1 = SIND2 = 63), and s escapes TO τ(s) in 61 of 63 (X2TAU), and in all 28 on fbA.
  - The strict W-rise is at x itself (RISE_X 63; CH_X2 0).
  - WIT holds for every one (CH_PFXC 63 / 28 / 3 / 1 / 1). Definition: some Even e of Z_(u1) ∪ Z_(u2) switches at a transition
    t ∈ [u1, u2) with W_(t+1)(e) ▷ W_t(e), and x's W-plays (σ_j, τ) at j = t and j = t + 1 both begin with the same prefix π before
    their first visit of e, with x's W-cycle node λ_W(x) not on π.
  - In every printed case the witness is at t = u1, on Z_(u1), and π has no Odd vertex off τ (WIT_Z1 63, WIT_BEFORE_D 63).
- Side data: W-run Even switches with W(e) unchanged at the switch: 397 of 33,794 in the corpus (WSW_FLAT). So «an S4a switch raises W
  at its own vertex» is false in general. But at every closing escape some switching Even vertex of Z has a strict W-rise
  (CLOSE_EFLAT 0 of 1,301, anc58/escw.py).

## 3. Two transfer lemmas (PROVED, lane; W-MON-conditional where marked)
- Lemma W-PROP. Let t be a transition of a W-run, e and x vertices, and suppose x's (σ_j, τ)-plays for j = t, t + 1 both have the form
  π followed by e's (σ_j, τ)-play, with π a fixed finite sequence not containing e and not containing the W-cycle node c := λ_W(x).
  If W_(t+1)(e) ▷ W_t(e), then W_(t+1)(x) ▷ W_t(x).
  - Proof. By [PLAY] (any positional pair), W_j(x) = Φ(π; W_j(e)) for j = t, t + 1. Since π avoids c and x's play reaches c after π,
    c is also the cycle node of W_j(e). By Φ-comp it suffices to treat π = q, one vertex, q ≠ c. Then Φ(q; (c, P, ℓ)) = (c, P ∪ S_q,
    ℓ + 1), S_q ⊆ {q} ([PLAY]'s case split). Claim: q ∉ P_j, the path set of W_j(e). If e's play visited q before c, then x's play
    would visit q in π and again before c, and a positional play is periodic from its first repeated vertex, so it would never
    reach c, a contradiction. Hence (P_t ∪ S_q) Δ (P_(t+1) ∪ S_q) = P_t Δ P_(t+1): the top rank of the symmetric difference and its
    parity are unchanged (Q1), the cycle node is the same, and both lengths shift by 1 with c's parity fixed. So Φ(q; ·) preserves
    the strict order between W_t(e) and W_(t+1)(e) (SPEC S1). □
- Lemma TIGHT-REOPEN (W-MON-conditional). Let u1 < u2 be a repeat of (s, x) in a W-run. If Ξ_k(x) = W_k(x) at some state
  k ∈ [u1 + 1, u2], then W_(u2+1)(x) ▷ W_k(x) ⊵ W_(u1)(x): W(x) strictly rises at a transition in [k, u2].
  - Proof. ESC-XCH (box 58 §9, from signed ODD-STEP) at the escape (s, u2): Ξ(x) changes at u2, since x = σ̄_(u2)(s). By [R15a] the
    change is a strict rise, and Ξ is monotone, so Ξ_(u2+1)(x) ▷ Ξ_(u2)(x) ⊵ Ξ_k(x) = W_k(x) ⊵ W_(u1)(x) (W-MON; the transitions u1 … u2
    lie in the W-run, which is a contiguous block). [R57] with ρ = τ at state u2 + 1 (τ is unchanged across u2) gives
    W_(u2+1)(x) ⊵ Ξ_(u2+1)(x). □
  - DATA (anc58/tight.py, output anc58/tight_corpus.txt): every corpus in-scope repeat is W-tight at x or at some x₂ (SW_TIGHT 63, TIGHT1
    59 already at u1 + 1); TIGHTV 0 (no tight vertex without the rise). But fbA_K8_m8_m8's 28 in-scope repeats are NOT tight
    (SW_NOTIGHT 28): there the rise comes only through W-PROP. pp_K48_n449's 45 EVEN_NOSW repeats are not tight either.
- Corollary WIT ⇒ REOPEN (W-MON-conditional, PROVED, lane). Every repeat that has a WIT witness (§2) satisfies W-REOPEN′'s conclusion
  at x: W_(u2)(x) ⊵ W_(t+1)(x) ▷ W_t(x) ⊵ W_(u1)(x) (W-PROP, then W-MON on both sides). The same holds for every W-tight repeat
  (TIGHT-REOPEN, with u2 + 1 in place of u2).
- So W-REOPEN′ ⇐ CONJECTURE WIT′: «every in-scope repeat has a WIT witness or is W-tight at x». A REDUCTION, data 0 violations
  (corpus 63, fbA 28, switchbestexp_5 3, R166 pins 1 + 1).

## 4. The per-escape form is DEAD (DEAD, instance verified)
- The data says the witness sits at the FIRST escape u1. The natural per-escape statement is therefore CLOSE-W: «at every W-run escape
  (s, u) whose cycle Z_u has an Even vertex switching at u, W(x) strictly rises at u». Tool anc58/escw.py, corpus output
  anc58/escw_corpus.txt: 1,434 escapes, 1,301 with a closing switch, 1,281 with the rise, 20 WITHOUT it (14 corpus entries).
- Smallest instance: experiments/red/n5inj/instances/frz40.pg (n 40), default start S3, written out as anc58/inst/frz40_default.start.
  At u = 44, Odd s = 0 escapes from x = 36 (τ(0) = 22), Z = 0, 36, 11, 4, 25, 24, 1, 26, 29, 9; the closing switch is Even 9, with
  W(9) strictly rising. W(36) does not change at 44. x's W-play at 45 is 36, 11, 31, 17, …: it leaves Z at the Odd vertex 11, which is
  in D (σ̄(11) = 4 ≠ τ(11) = 31). So the switching vertex is invisible to x's W-play.
  - Faithfulness: startcheck OK; n5b (red/seg/xeng.py) state sequence identical (90 iterations, 7 fallbacks); n5.py's solution = Oink
    zlk, both strategies verified (check_sol2.py).
  - This escape is not repeated in frz40, so it does not violate W-REOPEN′.
- READING. In the data the repeat hypothesis is not what produces the rise: the rise is a per-escape event (W-PROP at u1), and in every
  repeat of the data Z_(u1) happens to be W-visible from x up to the switching vertex (WIT_BEFORE_D 63). frz40 shows that a closing
  escape can hide its switch behind a D-vertex of x's W-play. KILL SHAPE for W-REOPEN′ (handed to the Lead for L-RED): make a
  frz40-type escape REPEAT (same s, same x, Z's Even switches only behind an Odd vertex of D on x's W-play, x and x₂ not W-tight in
  between). I expect W-REOPEN′ to be killable this way. Not attempted in this box.

## 5. What W-REOPEN′ would give (READING; the Lead's question)
- Answer: NO. W-REOPEN′ does not bound PLAT by a quantity outside the open core.
  - (a) Through its conclusion. In-scope repeats of (s, x) per W-run ≤ 2·(WCH_F(x) + Σ_(x₂) WCH_F(x₂)) (each W-change is in at most
    two windows [u1, u2]; in the data only WCH_F(x) is used). W-changes per vertex are ~|F| (box 58 §11: topfix_n10 has 36 at one vertex
    in a source-free W-run; ratio to |F| up to 1.000). So this is the circular route again.
  - (b) Through its hypothesis. In-scope repeats of (s, x) per W-run ≤ 2·Σ_e SW_F(e), over Even e on (s, x)'s escaped cycles. This
    holds BY DEFINITION of the scope (a repeat is in scope only if such a switch lies in [u1, u2], and consecutive windows share only
    an endpoint), so it needs no conjecture at all. W-REOPEN′ adds nothing to it. By k-SOURCE (R156 §1), SW_F(e) ≤ K_0 + Σ_b K_b(1 +
    WCH_F(u_b)) for an Even selector e whose options ride on sources u_b. That is again W-changes of the sources, with a degree factor
    per level (R156's own reading). So this is the open core too.
  - (c) The residue outside the scope is not small. EVEN_NOSW repeats: 54 in the corpus and 45 on pp_K48_n449 (linear in K, box 58 §7),
    plus 4 Odd-only. These are bounded only by ESC-XCH (Ξ-changes of x), which is circular as well (box 58 §9).
- The open quantity is unchanged: DESC per vertex per W-run (STAIR / ASC-RUN, R99; R162 / R163), as box 58 §11 said.

## DONE / FINDINGS / NEEDS
- DONE: this note; tools anc58/wrise2.py, wsw.py, tight.py, escw.py (+ runwrise2.sh, runwsw.sh, runtight.sh, runescw.sh); corpus
  outputs anc58/{wrise2, wsw, tight, escw}_corpus.txt; pins anc58/inst/{lean_29_35, leanc_29_35}.{pg, start} (copied read-only from
  claude/l-red b31f9477), anc58/inst/frz40_default.start; check.sh «box 59».
- FINDINGS:
  - DATA: W-REOPEN′ (repaired) 0 violations in all six readings (corpus 63 in scope, fbA 28, switchbestexp_5 3, R166 pins excluded).
  - PROVED (lane): W-PROP; TIGHT-REOPEN and WIT ⇒ REOPEN (W-MON-conditional). REDUCTION: W-REOPEN′ ⇐ WIT′.
  - DEAD: per-escape CLOSE-W (frz40, u 44; n5b identical, Oink OK). Kill shape for W-REOPEN′ stated (§4).
  - READING: W-REOPEN′ bounds PLAT only by W-changes or Even switches on escaped cycles, both the open core (§5).
- NEEDS: none from the owner.
