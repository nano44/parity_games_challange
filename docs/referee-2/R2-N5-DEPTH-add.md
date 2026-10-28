# R2-N5-DEPTH-add: REFEREE-2 report on packet P-N5-DEPTH-add (CONDITIONAL: GATE-PUSH, PURE-LEN, MONO-REF, E-ONEWAY)
Referee: REFEREE-2 successor 18 (session_01WT4cukhJyjxHKaBJWikCkK), Opus 5.5 (D15, L37). Written 2026-10-28 from 21:50Z (date -u).
Object: docs/si/P-N5-DEPTH-add-box22.md, sha1 4d51aa5ea4e1a1d145da4cb825deab75198abae7 (on trunk since b2f68f21 = the pin; l-si aa6061d1), 71
lines, frozen. Author L-SI successor 18. Quotes pinned at 78bc0e6a8.
Independence: written before opening any REFEREE file on DEPTH-add. In the push turn, after `git fetch origin claude/referee`, `git ls-tree
--name-only -r origin/claude/referee docs/referee/ | grep -ic depth` gave 16 at 2026-10-28 22:00:42Z (2026-10-26 19:04:54Z: 0). Names only; none opened.
Lane tools (evenside.py, exitx.py) NOT run.
Checker: docs/referee-2/R2-N5-DEPTH/depth_check.py (own; GP, GPC, PL, PLR, MR, MR_after, EOW, EOW_after), mkunion.py (union instances).
Quotes: own qtags.py, 5/5 VERBATIM.
Premise status (each named in the packet; checked):
- FREEZE-A (b) and (R-LEN) of P-N5-ROOT-box20: signed by both referees (REFEREE 15; REFEREE-2 successor 17, R2-N5-ROOT, all SIGN); not yet
  landed in RESULTS.
- ZCH-COUNT of P-N5-OFFMONO-add: signed by both (REFEREE 15; REFEREE-2 today, R2-N5-OFFMONO).
- OFFSET-MONO: signed by both.
- STATIC-DEPTH of P-N5-DEPTH: signed by me today (R2-N5-DEPTH); REFEREE's review pending to my knowledge.
- Landed: (M2κ), κ-Y-FORM_D (R56), (SW) (R72), (Aκ), (M1κ).
So every item below is CONDITIONAL on its named premise landing.
Scope (D1): conditional reductions. Nothing here bounds N5's running time. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)"; each CONDITIONAL on the premises named in the packet)
| § | item | verdict |
| --- | --- | --- |
| §1 | Lemma GATE-PUSH and its Count | SIGN (never exercised in my data: 0 qualifying σ̄ changes; rests on proof) |
| §2 | Proposition PURE-LEN | FALSE AS STATED (gap G-DADD-1): the length b − a of a per-class pure C-interval is NOT bounded by class quantities. Counterexamples on natural games, including the lane's own pure_22. SIGN for the repaired PURE-LEN′, which bounds the transitions of [a, b] with an Even switch in U_c by the same expression |
| §3 | Lemma MONO-REF | SIGN with the scope the proof uses: m at or before z's first visit of c. AS STATED (any m ∈ T on z's play) FALSE (gap G-DADD-2): counterexample b4_theta_n7 |
| §3 | Lemma E-ONEWAY | SIGN when e1 lies at or before c on w's honest play at every state of [t + 1, t′] (then MONO-REF applies). The case "e1 after c" is NOT covered by the proof (gap G-DADD-3; 0 returns in 711 such windows in data, so not refuted) |
| §4 | data | not signed |
Gaps G-DADD-1..3. Notes N-DADD-1..3.

## 1. Proof check
### 1.1 GATE-PUSH
- u ∈ D, and σ̄(u) ∈ A, a set holding no gate whose W-plays are honest. So u's honest play avoids u after its first step, and u is on no honest
  cycle at t or t + 1.
- y2 ∈ A_{t+1} ⊆ A_t (direct at t + 1; A non-increasing), so y2 ∈ Y^u_t. y1 ∈ A_{t+1}, so y1 ∈ Y^u_{t+1}. And y1 = σ̄_t(u) ∈ Y^u_t.
- κ-Y-FORM_D at t and t + 1, with (M2κ): κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1), the last strict unless tied.
- FREEZE-A (b) with s = a (P-N5-ROOT §3: any [s, e] of S4a steps with A non-increasing; the same L = max(|A_a| − 1, 0)), at t, t + 1 ≥ a + L and
  y1 ∈ A_{t+1}, gives M_{t+1}(y1) = M_t(y1). CORRECT.
- Count.
  - Per (u, y1) the pushes are at most y1's length rises: ≤ |U_c| − 2 by (R-LEN), lengths in [1, |U_c| − 1], monotone.
  - A switch away from a y1 ∉ A_{t+1} (y1 ∈ A_t, since the gate is direct at t) removes y1 from A for good: ≤ |A_a| such transitions.
  - Ties are counted apart.
  - A transition with several switches is charged once. CORRECT.

### 1.2 PURE-LEN: FALSE as stated (G-DADD-1); the repaired PURE-LEN′
- The proof cuts [a + L, b] into pieces and applies STATIC-DEPTH "on U_c" to bound each piece by |U_c| − 1. STATIC-DEPTH's induction does
  restrict to U_c: H_b-paths from U_c stay in U_c, as the packet argues. So every Even vertex of U_c is settled from piece start +
  d*(v) ≤ piece start + |U_c| − 1.
- But STATIC-DEPTH's LENGTH conclusion comes from its global last step: "σ unchanged ⇒ a fallback, excluded" (N-DEPTH-2). It needs every
  Even vertex of the GAME settled. A per-class C-interval of c is not cut when U_c is frozen and other classes go on switching inside the
  same fallback-free, λ_W-constant phase. So b − a can be as long as the other classes' activity.
- Counterexamples (depth_check.py; logs named.txt, lib41_x3.txt): PL_FAIL in 1,326 of 6,742 per-class pure C-intervals, all with 0 Even
  switches in U_c after the bound.
  - union/reader40_plus2 = L-RED's reader_L40_n96 ⊎ the 2-vertex Even-only class {p (Even, priority 2, self-loop), q (Even, priority 0,
    → p)} (mkunion.py; docs/referee-2/R2-N5-DEPTH/union/reader40_plus2.pg sha1 8b233aa5, reader10_plus2.pg 89db88d3, reader20_plus2.pg 39d2a506). Class c = p, |U_c| = 2, gateless (pure vacuously), N_σ̄ = N_cyc = 0, bound 2; its pure
    C-interval is [0, 41], length 41. reader10_plus2: [0, 11], length 11, bound 2.
  - Natural games, at given or random starts: the lane's own experiments/new/box22/instances/pure_22.pg (class 10, |U_c| = 3, bound 4,
    intervals [9, 18], [23, 33]); experiments/red/xing/instances/kw25_n32.pg (class 2, |U_c| = 3, bound 4, interval [0, 25]);
    experiments/si/xing/instances/ccl_w48_n48.pg (class 27, |U_c| = 3, interval [1, 27]). All gateless.
- PURE-LEN′ (SIGN). For a pure C-interval [a, b] of class c, under GEN_W on U_c: the number of transitions of [a, b] at which some Even
  vertex of U_c switches is ≤ L + (1 + N_σ̄ + N_cyc)(|U_c| − 1) + N_σ̄ + N_cyc.
  - Proof: the packet's, with the class-restricted settling of STATIC-DEPTH's induction (on each piece every Even v ∈ U_c is constant from
    piece start + d*(v)) in place of its length conclusion. (H3) and (H4) on U_c hold as the packet argues: c's cycle is common and constant
    on a piece, and PURE-END restricted to U_c.
  - Data: PLR 0 violations in 6,742 intervals.
  - The stated length form holds when the per-class C-interval is replaced by a global C-interval in which EVERY class is pure (then
    STATIC-DEPTH's global last step applies); not checked separately.
- Effect: the lane's data statement ("no pure C-interval has an Even switch at index ≥ (|A_a| − 1) + |U_c|") is a statement about Even
  switches, so it supports PURE-LEN′, not PURE-LEN.

### 1.3 MONO-REF: scope (G-DADD-2)
- The proof telescopes along the T-vertices x_1, …, x_h = m of z's (t+1)-play with par_{t+1}(x_i) = x_{i+1}. That holds only for T-vertices up
  to z's FIRST visit of c: par is defined "before c", and a term off(c; ·) is not an OFFSET-MONO term. With m at or before the first c, each
  piece of the proof is correct:
  - the first term is OFFSET-MONO (z ∈ Q), or OFFSET-MONO's Step 1 on the Q-free path, whose vertices are ≠ c;
  - the level terms are OFFSET-MONO under the stated no-cycle hypothesis, which OFFSET-MONO⁺ (P-N5-OFFMONO-add3, signed by both) now makes
    unnecessary.
  SIGN with that scope.
- As stated ("m ∈ T on z's honest (t+1)-play, m ≠ z"), m may lie after c, on c's cycle, and then MONO-REF is FALSE.
  - Instance: experiments/n5-exhaustive/instances/b4_theta_n7.pg (sha1 5627745306a45f1a98387c53bba40065375acd5e) from
    docs/referee-2/R2-N5-DEPTH/mr/b4_theta_n7_mrafter.start (σ0 = 0:3 1:6 2:0 3:1 4:3 5:4, τ0 = 6:5).
  - Class c = 1 (Ω odd, s_c = +1), z = 3, m = 6 ∈ Q. At 0 → 1, an in-phase S4a step, Even vertex 0 switches 3 → 4. c's cycle grows from
    1→6→0→3→1 to 1→6→0→4→3→1.
  - 3's (t+1)-play is 3 → 1 → 6 → …: m = 6 comes after c, and there is no Q-vertex between 3 and 6.
  - κ(3) = (0, 1) is unchanged while κ(6) rises from (0, 3) to (0, 4), so off(3; 6) falls from (0, −2) to (0, −3).
- Data: with m at or before c, 1,087,965 checks, 0 violations. With m after c, 610 failures of 43,388.

### 1.4 E-ONEWAY: proof covers e1 at or before c (G-DADD-3)
- The proof (h, g_s, the two MONO-REF applications, the switch-back condition h ≻ g_{t′}) is CORRECT when MONO-REF applies to (b, e1) at
  t → t + 1 and to (w, e1) on [t + 1, t′], i.e. when e1 lies at or before c on those plays.
  - κ_{t′}(a) = κwt(π_a) + κ_{t′}(e1), because π_a and e1 are unchanged and π_a has no c.
  - The switch-back condition κ_{t′}(a) ≻ κ_{t′}(σ_{t′} w) is equivalent to h ≻ g_{t′} by (Aκ) at w.
- e1 can lie after c on w's play: e1 is the first T-vertex on a's play, but w's play via b may reach c first. Then e1 lies on c's honest cycle,
  and MONO-REF is out of scope there (§1.3). That case is NOT proved.
- Data: E-ONEWAY windows with e1 at or before c: 63,065 checks, 0 returns. With e1 after c: 711 windows, 0 returns. The statement may well
  hold there, but it needs its own argument.

## 2. DATA (depth_check.py; the same runs as R2-N5-DEPTH §2: 21,775 N5 runs, 46 RESULT lines, all OK)
| check | checks | violations / counted |
| --- | --- | --- |
| GATE-PUSH at qualifying σ̄ changes (t ≥ a + L, y1 ∈ A_{t+1}, pure per-class C-interval) | 0 | — (never exercised; 1,398 pure intervals have gates) |
| GATE-PUSH count N_σ̄ ≤ Σ deg(u)(\|U_c\| − 2) + \|A_a\| + TIES | 6,742 intervals | 0 |
| PURE-LEN as stated (b − a ≤ bound) | 6,742 | 1,326 FAIL (counted; G-DADD-1) |
| PURE-LEN′ (Even-switch transitions ≤ bound) | 6,742 | 0 |
| MONO-REF, m at or before c (with the no-cycle hypothesis) | 1,087,965 | 0 |
| MONO-REF, m after c | 43,388 | 610 FAIL (counted; G-DADD-2) |
| E-ONEWAY, e1 at or before c / after c | 63,065 / 711 | 0 / 0 returns |

## 3. Notes
- N-DADD-1 (premises). MONO-REF's and E-ONEWAY's no-cycle hypotheses can be dropped by citing OFFSET-MONO⁺ (P-N5-OFFMONO-add3, signed by
  both referees) instead of OFFSET-MONO.
- N-DADD-2 (GATE-PUSH, data). No qualifying σ̄ change occurs in my corpus. GATE-PUSH and its count rest on proof alone, and their
  conditional premise FREEZE-A (b) is not landed yet.
- N-DADD-3 (repairs, suggested wording).
  - G-DADD-1: replace "b − a ≤ …" by "the transitions of [a, b] with an Even switch in U_c number ≤ …" (PURE-LEN′), or restrict to global
    C-intervals in which every class is pure.
  - G-DADD-2: add "m at or before z's first visit of c".
  - G-DADD-3: add "e1 at or before c on w's honest play at every state of [t + 1, t′]", or prove the e1-on-c's-cycle case separately.
