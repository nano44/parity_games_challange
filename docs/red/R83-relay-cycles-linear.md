# R83: relay 2-cycles repeated Θ(n) times in ONE phase on a constructed family (mkpp); ρ_q and N_ep grow linearly, exponent 1 over 4 sizes; where a super-polynomial family would have to come from (L-RED successor 20, box 50; Lead 10:42Z, date -u)
Target: the re-thaw loop of docs/si/N5-RUND-box17.md §22 (L-SI 14, l-si 24a70938), O2 plus a cycle in the phase's relay graph. The Lead's
ask: a family on 𝒞^kO (k fixed) on which the relay cycle repeats and ρ_q or N_ep per phase grows faster than any fixed polynomial, or
at least a growth exponent over ≥ 4 sizes. Labels per L40. DATA, READING. Every game. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Result
- **No super-polynomial family.**
- **A family whose phase relay graph has the 2-cycle q1 ↔ q2, used about K/2 times in each direction.** Its growth exponent is 1:

| K | n | iterations (n5.py) | phases | fallbacks | N_ep (one phase) | max ρ_q | relay events per q (L-SI relay.py) | CYC2 phases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 113 | 13 | 1 | 0 | 9 | 8 | 4 | 1 |
| 12 | 161 | 19 | 1 | 0 | 15 | 14 | 7 | 1 |
| 24 | 257 | 31 | 1 | 0 | 27 | 26 | 13 | 1 |
| 48 | 449 | 55 | 1 | 0 | 51 | 50 | 25 | 1 |

  - n = 8K + 65, N_ep = K + 3, max ρ_q = K + 2, and relays per q = K/2 + 1: all linear in n. The raw log-log slope over n 113 → 449 is
    1.26 (N_ep) and 1.33 (ρ_q), from the additive constants. In terms of K (n = 8K + 65) both are exactly linear, so the exponent is 1.
  - The whole run is one phase; τ never changes.
  - relay.py (l-si 24a70938, read only) shows the relay graph {q1: [GA, q2], q2: [GB, q1]}: the 2-cycle, plus the line gates as sources.
    It reports RELAY PASS (ROOT, ROUTE-RELAY, SELF-FREE hold).
  - My rec0_20 (N_ep, Oink): no FAIL, OUT_OINK OK. n5.py and check_sol2 give "zielonka(oink zlk) OK strategies verified" at K 12 and 48.
- Pins (start pairs; experiments/red/usplit/instances/):

| file | sha1 (.pg) | .start | .start.json |
| --- | --- | --- | --- |
| pp_K12_n161.pg | 8808ba5dcf518ee56285860075ec31e932b0f6ac | eb95d52b | 602efbe8 |
| pp_K48_n449.pg | a161569d654c3df9922e260aaddced82fbb09203 | ead17654 | 508176df |

- So the relay cycle of §22.5 is not a rare accident: it can be repeated Θ(n) times in one phase, on purpose. L-SI's data had at most one
  per phase.
  - Any proof of a ρ_q bound for m_c ≥ 2 must allow Θ(n) relay cycles per phase.
  - (b) of §22.6 (an acyclic relay graph per phase) is false on this family in a strong sense: the cycle is used Θ(n) times.

## 1. The construction (experiments/red/usplit/mkpp.py K LG OUT)
- It reuses mkgrow's machinery (R82), with two risers: vA takes the routes x_j for odd j (line A) and vB those for even j (line B). Their
  Ξ values leapfrog K times, through C_1 < C_2 < … taken alternately.
- Two Odd choice vertices in the class:
  - q1 has successors aq1, vA and e1 → q2; q2 has aq2, vB and e2 → q1. e_i are even and relevant, so the relay route is worse for Odd
    under τ's valuation.
  - Odd's best response takes the LOWER riser directly and routes the other q through it, so the relay direction flips at every rise.
- Keeping one phase:
  - aq_i → Ta (even, above every C_j) → Z, so σ̄(q_i) ≠ aq_i throughout.
  - A permanently Ξ-blocked route xst_i, with even g* above Ta, behind the top-odd gate GH, makes Even's best response against τ value
    v_i above Ta. So τ(q_i) = aq_i stays Odd-optimal (Iτ = ∅).

## 2. Where a super-polynomial family would have to come from (READING; the argument is a sketch, not a proof)
- In a phase, τ is fixed. So W(q) = W(τ(q)) for Odd q: a relay changes Ξ(q) but not W(q).
- Even's S4a step is W-optimal inside the gate arena. So Ξ-relays reach Even's moves only through GATING (which W-improving edges are
  Ξ-improving now). In mkpp, every relay is invisible to Even.
- The W-dynamics of a fallback-free, λ_W-constant run is monotone optimisation in the FIXED one-player game G_τ with delayed edges. By
  Lemma P^c_sch / CHARGE-U (N5-RUND §14, §16, lane-PROVED), W can be delayed only by forbidden (edge, state) pairs on a path's
  schedule. Coarse W-changes per vertex per run are ≤ (n − 1)(1 + |U(S)|).
- By ROOT (§22.3) every ρ-transition has an Even switch on a Q-exit path, and an S4a switch is a W-change or a tie. So, roughly:
  ρ per run ≤ |Q|·(#W-changes on exit paths + #tie switches), and that is ≤ |Q|·n·(n − 1)(1 + |U(S)|) + ties.
  - The steps not covered: length-only W changes (coarse_{−1} ignores lengths) and tie switches. Each needs its own count.
- So a super-polynomial ρ_q (or N_ep) per phase needs one of:
  - (i) super-polynomially many unforbid-switches |U(S)| in one run;
  - (ii) super-polynomially many runs per phase, cut by fallbacks or λ_W changes;
  - (iii) super-polynomially many tie or length-only switches.
- My families reach |U(S)| = Θ(n) (R82). Each U event there is paid by a fresh content level C_j, because RULER allows a level's reuse
  only after a higher rise.
  - (i) therefore needs Ξ-blocks that re-arm. An edge must be forbidden, unforbidden, and forbidden again, many times, each time
    released by a Ξ event rather than by new content.
  - The re-armable delay line (exits to one leapfrogging terminal, end at the other) is the obvious device. A one-player obstruction
    limits it: in an F_D region (Ξ = W, every W-improving edge available) G_τ re-equilibrates within n + m steps after the last
    terminal change (Lemma P / EP-0). So doubling stages cannot be built from F_D pieces; each stage must itself be Ξ-gated.
  - I did not build such a stage. The key open question for (i): can a Ξ-gate re-arm without fresh content (a gate u leaving D and
    re-entering it within one phase, many times)?

## 3. Tools
- mkpp.py (generator; the pins are byte-identical to `mkpp.py 12 18` and `mkpp.py 48 54`, cmp).
- rec0_20.py (N_ep, Oink), show.py.
- L-SI's relay.py was run read-only from a detached worktree of origin/claude/l-si at 24a70938.

## 4. ADDENDUM (Lead 10:52Z target: ρ_q > n in ONE phase on a class with m_c ≥ 2): why my devices stop at ρ_q ≤ phase length ≲ n (READING, DATA)
- Trivially ρ_q ≤ T, the number of in-phase transitions: q's Ξ changes at most once per transition. So ρ_q > n needs a phase LONGER than n.
- mkrho.py (experiments/red/usplit/; DATA) adds to mkpp ONE re-armable delay line m_1 … m_L between the two risers, read by an Odd q at
  every position:
  - m_i → {z_i, m_{i+1}}, with exit lengths increasing in i;
  - when vA overtakes vB, a wave runs down the line and Odd's best response at q follows it, so Ξ(q) changes at every wave step;
  - when vB overtakes vA, all of the line switches back to its exits at once (re-armed).
  The line does re-arm inside one phase, as designed. But mkgrow's risers rise one per iteration, so the waves are cut short:
  `mkrho.py 6 5 12` gives n 119, ITER 13, ρ_q 11, one phase, 0 fallbacks.
- Spacing the rises L apart with mkgrow's taps costs a timing line of length about K·L. So T ≈ K·L ≲ n again, and ρ_q ≤ T stays linear.
- What would beat it is EVENT-DRIVEN re-triggering: rise j + 1 unblocked by the completion of wave j, so one line is traversed K times at
  O(1) vertices per rise. I tried two forms:
  - a trigger w_{j+1} that switches into the line head when its value passes a threshold T_{j+1};
  - a gate whose b-branch reads the line.
  Both put the line (whose end is the riser) on the route of the riser's own next option. That closes a cycle riser → x_{j+1} → w_{j+1}
  → line → riser, or, with the partner riser, a 2-cycle vA → … → vB → … → vA. Any unblocking of a route needs a ROUTE change of that
  route (or a gate change on it), and a route that reads a riser's value passes through the riser.
- So, in my toolkit, feedback closes a cycle. The super-linear phase needs feedback that does not pass through the risers. Two
  candidates:
  - gates whose σ̄ flips are driven by a chain disjoint from the risers;
  - Even-controlled cycles in Friedmann's style, which the class structure (every honest cycle in U_c is c's cycle) forbids inside one
    class, but not across classes.
  Neither is built. Open.
