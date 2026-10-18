# L32 reassessment of GAP-A (Lead draft, 2026-10-18 by date -u) — SENT via OWNER-DESK 2026-10-18 04:00Z by date -u (trigger met: L-RED box 10 ended 03:54Z without a (CTX⁺) family)

Trigger (L32 (2), docs/DECISIONS.md): "the Fable reset, 2026-10-21 21:00Z, or earlier when both lanes' boxes end with no new
GAP-A reduction". L-ALG box 10 ended 03:43Z (l-alg 434f92a, ledger GAP-A-M §24h). L-RED box 10 (serialized-context attempt on
(CTX⁺)) ends near 560k context. If that box does not produce a (CTX⁺) family, the trigger is met.

## 1. Criterion check (L32 (2))
"Progress" = a reduction of GAP-A to ONE named statement with a proof route, or a proved polynomial bound on a nontrivial
subclass. Status: NOT MET.
- Signed since L32 (all [refereed-only], two Opus 5.5 referees under D12, CHECKER-gated): RESULTS R7-R14.
- What they achieved: GAP-A ⇐ (CTX⁺) ∧ X, with X one of (STEAL-POLY_sum) (R12 (a)), (EXITS-POLY) (R13 (b)), (FIRED⁺-R) (R14).
  Both referees confirmed that R13 and R14 are EQUIVALENCES with GAP-A up to polynomial factors (reformulations, not
  reductions). Every LOCAL/CONSTANT premise that would have given a proof route is now false on a uniform family (DE19-DE21:
  STEAL-ONCE*, STEALER-MONO, STOLEN-PERM, STAYS-MET, STEAL-DEPTH_D for every constant D, EXIT_c for every constant c), each
  Lead-verified in both order data and the last checked on an independent pinned-C++ build (REFEREE-2 R2-FAITH-lagfam).
- No proof route exists for (CTX⁺) or for any polynomial-total premise (L-ALG §24h: "L32 NOT met").
- No proved polynomial bound on a nontrivial subclass.

## 2. What still stands (no immediate-stop condition, L32 (1))
- No Oink-verified incorrect or incomplete run, under any order datum, in any lane, at any time.
- No family with super-polynomially many searches per phase: the strongest adversarial family (lagfam, n = 7D+22) has
  D + 8 iterations; every total on it is polynomial (degree ≤ 3; L-ALG §24g and L-RED R39 §8 independently).
- So A_DTL remains an open candidate: not refuted, not proved.
- The open core, stated once (L-ALG §24h, Lead reading): every live route needs (CTX⁺) plus one polynomial-total premise, and
  each total is bounded by (phase length at one context) × poly; the only remaining threat is a super-polynomially long phase
  at one context, i.e. super-polynomially many NEW tangles firing at one context (Lemma CHANGE-NEW, R14). That is GAP-A itself.
  L-ALG names it (LONG-PHASE) (GAP-A-M §24i): "no context sees super-polynomially many NEW firing tangles in one phase"; a
  counter at one context would cost about 2^D new firing tangles there (combinational-in-T remark, §24f, from signed results).
- GAP-C (completeness): reduced to the KT frame with one open hypothesis (ACYC) for Step 5 (R4), but single-search progress
  statements are dead (DE13, DE15); a proof needs a cross-search measure of GAP-A type.

## 3. The three options L32 (2) requires the Lead to put to the owner (the owner decides)
(a) Bank the refereed partial results and write up DTL's status as an open candidate. Deliverable: one status document (the
    reduction chain R4-R14 with its signatures, the dead ends DE13-DE21 with instances, the open core in one paragraph), for the
    owner's own use; no external contact (D11). Cost: one Lead session plus CHECKER, about a day of small spend.
(b) Keep only the cheap adversarial side on GAP-A (L-RED climbs and constructions aimed at a long phase at one context), no
    proof lane. Cost: one lane at the current rate; the referees and CHECKER idle unless a kill needs verification.
(c) A new candidate or a new approach. Literature lanes (L-LIT, L-SI, L-LOWER) are parked with maps on file; choosing (c) needs
    an owner-chosen direction.
Lead recommendation (a Lead reading, not a decision): (a) now, plus (b) for a bounded period (until the Fable reset), then stop
unless (b) produces a long-phase family. Reason: since L32 the proof lanes produced conditional reductions that the referees judged
equivalent to GAP-A (reformulations), while each adversarial box produced a verified kill; the refereed record is worth banking before the Opus period ends.

## 4. Spend at drafting
get_session on all 38 roster ids at 2026-10-18 04:00Z: total $1,950 (up $169 since 2026-10-17 19:51Z); Lead $304, CHECKER $103,
OWNER-DESK $53. isUsingOverage false on all 38; seven_day 'allowed_warning'; the two paused Fable sessions are 'rejected' until
the reset 2026-10-21 21:00Z. All lane sessions are parked; nothing is running.
