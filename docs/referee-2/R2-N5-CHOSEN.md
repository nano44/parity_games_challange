# R2-N5-CHOSEN: REFEREE-2 report on packet P-N5-CHOSEN (CHOSEN, RELAY-CHAIN (a), (b), TV-END)
Referee: REFEREE-2 successor 17 (session_01P2K6kCftytexWsuJfNFtV4), Opus 5.5 (D15, L37). Written 2026-10-26 14:45Z (date -u).
Object: docs/si/P-N5-CHOSEN-box19.md, sha1 764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (`git show 9196c318:… | sha1sum` and the same at l-si
b7189738), 129 lines, pinned at trunk 9196c318, frozen. Author L-SI successor 15.
Independence: written before opening any REFEREE file on CHOSEN or FBC. `git fetch origin claude/referee` + `git ls-tree --name-only -r
origin/claude/referee docs/referee/ | grep -ic -e fbc -e chosen` gave 0 at 13:34Z, 0 at 14:38Z and 22 at 14:51Z, the push turn (REFEREE pushed its own
FBC and CHOSEN material between those reads; file NAMES only, nothing opened, and this report was final before 14:51Z). The count is read
from that command's output, never from a template. The lane's tools (experiments/si/rund/chosen.py, tvend.py, flipcls.py, quiet.py, quotecheck.py)
were NOT run or imported.
Checker: docs/referee-2/R2-N5-CHOSEN/chosen_check.py (own; state loop = succ. 13's SPEC loop through my lane's R2-N5-RUND/rund_check.py; Ξ, W
are my own play values, cross-checked against the engine every state: ENGXI). κ, κwt_c, exits and class exit paths are my own
implementations, self-checked: KADD (additivity on every honest play prefix to its exit, at every state and class) and KORD (κ-order = Ξ-order
inside a class). κopt_c and κopt^q are EXACT by enumeration of the simple paths of G_c and G_c^q (budget; over budget the class is UNK and
counted), so (H) is tested DIRECTLY at every state, not only where R56 (g) triggers.
Quote check: own script docs/referee-2/R2-N5-CHOSEN/qtags.py (independent of the lane's quotecheck.py): 9 tagged quotes, all verbatim inside
the tagged line ranges; 1 «…» without a [Q] tag (§1's additivity restatement, which is also tagged two lines above — N-CHOSEN-1).
Scope (D1): structural lemmas inside one phase. TV-END bounds no count ("ρ events in the class all occur before (H) first holds" — the packet
is explicit, and I confirm nothing here bounds when (H) is first reached). RELAY-CHAIN (b) is a reduction of Σρ_q to ROUTE + CYC + TOG, not a
bound. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts
| item | verdict | premises (checked) |
| --- | --- | --- |
| §2 Lemma CHOSEN | SIGN | R56 (d) κ-Y-FORM_D (P1, and its "≤" half uses R18 (d) Lemma S (a)); one-step additivity (Aκ); (SG) = R15 (a), (d) via (VJ) under P1; κ injective on path sets inside a class |
| §3 Corollary RELAY-CHAIN (the chain itself) | SIGN | CHOSEN; the ROUTE / RELAY / CYC trichotomy of P-N5-FLIP §3; e ≠ q from the no-honest-cycle hypothesis (N-CHOSEN-2) |
| §3 consequence (a) | SIGN | RELAY-CHAIN |
| §3 consequence (b) (Σ_{q∈Q_c} ρ_q ≤ \|Q_c\|(ROUTE_c + CYC_c + TOG_c)) | SIGN | RELAY-CHAIN + the completion in N-CHOSEN-3 (map every event, not only the RELAY ones) |
| §4 Lemma TV-END | SIGN, conditional on ROOT-C's repaired form (both referees signed it; its RESULTS entry R69 is still at CHECKER, C78 FAIL under revision — N-CHOSEN-5) | (SW) = R15 (d); (SG); additivity; the phase (λ fixed); ROOT-C signed form (P1); R56 (g) only for when (H) holds; κopt_c / κopt^q as R56 defines them (endpoint excluded) |
| §1 premise list and quotes | complete; 9/9 quotes verbatim | own qtags.py |
No gap. Notes N-CHOSEN-1..7 (§3). Not reviewed (as the packet asks): §5 (the obstruction map READING, the DATA).

## 1. Proof check
### CHOSEN
- y* := σ̄_t(q) ∈ U_c: λ(q) = c and q's honest play at t enters y*, so λ(y*) = c. y*'s play at t avoids q, else q would lie on an honest cycle
  at t (q → y* → … → q), excluded by hypothesis. So y* ∈ Y^q_t. CORRECT. (y* = q is impossible for the same reason.)
- κ_t(q) = κwt_c(q) + κ_t(y*): the packet derives it from R56 (d) plus "σ̄_t attains the minimum (P1)". It is also the one-step extension (Aκ)
  of q's own honest play, which needs no optimality at all (q ∉ P(Ξ_t(y*)) because y*'s play avoids q, so the signed weights add). Both routes
  are sound; the (Aκ) route is the shorter one (N-CHOSEN-4). CORRECT.
- RELAY ⇒ p and e unchanged at t + 1 (y* ∈ succ(q) ∩ U_c is one of the y's in §1's definition). CORRECT.
- The contradiction. Assume e = c, or (e's play at t + 1 avoids q and κ_{t+1}(e) = κ_t(e)).
  - p avoids q: a class exit path stops at the FIRST vertex of Q_c ∪ {c} and q ∈ Q_c, so q ∉ p. CORRECT.
  - e = c: c's honest play is c's cycle, which avoids q (q on no honest cycle at t + 1). So in both branches y*'s play at t + 1 avoids q, i.e.
    y* ∈ Y^q_{t+1}, and κ_{t+1}(y*) = κwt_c(p) + κ_{t+1}(e) = κwt_c(p) + κ_t(e) = κ_t(y*) (additivity at t and t + 1; κ(c) is constant in the
    phase because c's valuation is (c, ∅, 0) throughout). CORRECT.
  - R56 (d) at t + 1 (its hypothesis "q on no honest cycle at t + 1" is in force): κ_{t+1}(q) ⪯ κwt_c(q) + κ_{t+1}(y*) = κ_t(q). With (SG)
    and the κ-order inside the class, κ_{t+1}(q) ⪰ κ_t(q), so κ_{t+1}(q) = κ_t(q). CORRECT.
  - "κ determines Ξ inside the class": the cycle node is c on both sides, the length component is κ's second entry, and the signed weight is
    injective on path sets (the highest differing rank dominates: 2^r > Σ_{r′<r} 2^{r′}). So Ξ_{t+1}(q) = Ξ_t(q), contradicting the ρ event.
    CORRECT. (I verified the injectivity numerically as the order agreement KORD, 2,410,459 checks, and the additivity as KADD, 2,161,705
    checks, both 0 failures.)
- So the statement holds, with e ∈ Q_c ∖ {q} (e ≠ c is the first conclusion; e ≠ q holds because e = q would put q on an honest cycle at t —
  stated in my §3 note N-CHOSEN-2, since RELAY-CHAIN needs it).

### RELAY-CHAIN and (a), (b)
- Each step: e_i's event is RELAY ⇒ (by §1's definition, which presupposes "on no honest cycle at t and t + 1") CHOSEN applies at e_i, giving
  e_{i+1} ∈ Q_c ∖ {e_i} with a ρ event, or a TOG step. The trichotomy ROUTE / RELAY / CYC is exhaustive for a ρ event at a terminal of the
  class, so the chain stops exactly where the packet says. CORRECT.
- Distinctness: e_0's honest play at t passes e_0, e_1, e_2, … in order before c (each e_{i+1} is the exit of e_i's chosen option, i.e. the
  next terminal on the same play). A repeat would make that play return to e_i, so e_i would be on its own honest cycle at t and its event
  would be CYC, where the chain has already stopped. Hence at most \|Q_c\| distinct terminals and at most \|Q_c\| − 1 steps. CORRECT.
- (a) is immediate (ROUTE / CYC: itself; RELAY: run the chain). CORRECT.
- (b) Σ_{q ∈ Q_c} ρ_q ≤ \|Q_c\|(ROUTE_c + CYC_c + TOG_c). TRUE, but the packet's one-line argument maps only the RELAY events to their ends,
  while the left-hand side counts ROUTE and CYC events too. It closes by mapping each ROUTE / CYC event to ITSELF (it is its own end): then
  every event of every transition maps to an end at the same transition, a transition with an event has at least one end by (a), and a
  transition carries at most \|Q_c\| events, so Σρ_q ≤ \|Q_c\| · (number of ends) ≤ \|Q_c\|(ROUTE_c + CYC_c + TOG_c). One sentence
  (N-CHOSEN-3). I checked the inequality itself per (phase, class): 1,844 checks, 0 failures, worst case Σρ = 474 against the bound
  233·13 = 3,029 (tcL_N12, \|Q_c\| = 233).

### TV-END
- (i) A switching Even x ∈ U_c ∖ T: (SW) gives (x, z) ∈ Iσ_t; λ_{t+1}(x) = c and x ≠ c force λ(z) = c, so z ∈ U_c, and σ_t(x) ∈ U_c likewise,
  so the Ξ-comparison is a κ-comparison and one-step additivity gives κwt_c(x) + κ_t(z) ≻ κ_t(x). CORRECT.
- (ii) If x is not on z's honest play at t before its exit e: that play is simple up to e (it reaches c ∈ T, so it cannot cycle before T), its
  vertices before e lie in U_c ∖ T (Odd ones outside Q, hence forced), so x·(z's class exit path) is a simple path of G_c (e = c) or G_c^e
  (e ∈ Q_c) whose only T-vertex is its end. Additivity plus κ_t(e) = κ_Θ(e) (Θ's definition for e ∈ Q_c; κ(c) constant for e = c) gives
  κwt_c(x) + κ_t(z) = κwt_c(that path) + κ_Θ(e) ⪯ κopt_c(x) or κopt^e(x) + κ_Θ(e) ⪯ TV_Θ(x) = κ_t(x) by (H) — using R56's convention that
  κopt excludes the endpoint, which is how R56 (b) and (c) use it. Contradiction with (i). CORRECT.
- (iii) So every switching Even x of U_c ∖ T lies on its own target's t-play before its exit. If S ≠ ∅, the t+1-play from x ∈ S runs x, z(x),
  then along z(x)'s t-play (every intermediate vertex is a non-switching Even or a forced Odd vertex of U_c ∖ T) to the first S-vertex, which
  is reached before the exit because x itself lies on that stretch; iterating, the play never meets T, so λ_{t+1}(x) ≠ c, against λ_{t+1} = λ
  and x ∈ U_c. CORRECT (the "x itself is on that part" step is what makes the first S-vertex come before T; it is right, and is the load-bearing
  line of the proof).
- (iv) With S = ∅ every class exit path and exit of the class is unchanged (their vertices are non-switching Even or forced Odd vertices of
  U_c ∖ T, and a y ∈ T has an empty path), so ROOT-C in its REPAIRED form ("path AND exit" in the hypothesis) gives κ_{t+1} = κ_t on Q_c,
  hence t + 1 ∈ Θ; and for z ∈ U_c ∖ T, additivity with the unchanged path, unchanged exit and unchanged terminal value gives κ_{t+1}(z) =
  κ_t(z) = TV_Θ(z), i.e. (H) at t + 1. Induction to the phase's end. CORRECT.
- The hypothesis bridge is right: R56 (g)'s trigger is a Q-RUN (all of Q constant), which is contained in a Q_c-run, and κ_Θ(q) for q ∈ Q_c is
  the same number in both, so R56 (g) yields (H) in TV-END's sense. I checked that bridge numerically (TVG: 147 states where R56 (g)'s trigger
  held, (H) held at every one).
- Premise status (N-CHOSEN-5): ROOT-C's literal form is FALSE (both referees, with witnesses) and only the repaired form is signed; its
  RESULTS entry (R69, P-N5-FLIP) is at CHECKER with C78 FAIL and under revision. TV-END's signature is therefore conditional on the repaired
  ROOT-C as both referees worded it, which is exactly what the packet quotes. Nothing else in the packet depends on R69.

## 2. Premises, complete list
SPEC S2 (Iσ), S4a / S4c through (SW) = R15 (d)'s "every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ"; phase = R38 (a) KEY; (SG) = R15 (a) with
R15 (d) on Ξ via (VJ) under P1 (standing premise 1E-N3, R57); R56's setting line (classes, κ, κwt_c, G_c, G_c^q, κopt, Q_c-run) and R56 (d)
κ-Y-FORM_D (whose "≤" half uses R18 (d) Lemma S (a), signed for every game by both referees) and R56 (g) Lemma TV; P-N5-FLIP §1's additivity
and §3's exit / class exit path / ROUTE / RELAY definitions (signed); ROOT-C in the repaired form (P-N5-FLIP-fixes-box18 R1, sha1 93a65e1b…).
The packet's list is complete and accurate; the only correction is that CHOSEN's κ_t(q) = κwt_c(q) + κ_t(y*) needs no optimality (N-CHOSEN-4).

## 3. Notes (no gap)
- N-CHOSEN-1 (quotes). 9 tagged quotes, all verbatim at the tagged commits and lines (own script). §1 has one «…» with no [Q] tag of its own
  (the additivity sentence restated in prose after its tagged quote); harmless, but the packet's claim "every «…» is verbatim from the tagged
  source" reads as if each one carries a tag.
- N-CHOSEN-2 (missing conclusion, used later). CHOSEN concludes "e ≠ c", but RELAY-CHAIN needs e ∈ Q_c ∖ {q}. e ≠ q follows from the same
  hypothesis (e = q means y*'s play returns to q, so q is on an honest cycle at t), and the chain's "e_{i+1} ∈ Q_c ∖ {e_i}" silently uses it.
  Add "and e ≠ q" to CHOSEN's statement.
- N-CHOSEN-3 (completeness of (b)'s count). The map must cover ROUTE and CYC events too (each is its own end); as written only the RELAY
  events are mapped, while the left side counts all events. One sentence, no change to the inequality.
- N-CHOSEN-4 (premise strength). κ_t(q) = κwt_c(q) + κ_t(y*) is one-step additivity (Aκ), not R56 (d) with P1; R56 (d) is needed only for the
  "⪯" step at t + 1. Worth stating, since it shortens CHOSEN's premise list to (Aκ), (SG) and R56 (d) at t + 1 only.
- N-CHOSEN-5 (premise status). TV-END rests on ROOT-C's repaired form, whose RESULTS entry R69 is not landed yet (CHECKER C78 FAIL, revision in
  flight). My SIGN is conditional on that form as both referees worded it.
- N-CHOSEN-6 (the §5 DATA claim "TOG never occurs" is too strong, and the thinness claim is too pessimistic — DATA).
  - TOG as CHOSEN's second alternative DOES occur: 241 RELAY events in my runs have q on the chosen exit's honest play at t + 1 (frz40 1,
    pp_K12_n161 11, pp_K48_n449 47, lib41 169, lib2o 5, randoms 7). In every single one of the 6,322 RELAY events the FIRST alternative also
    held (κ_t(e) ≠ κ_{t+1}(e); CH_source_event = CH_checks in every log), and no chain ever ended in a TOG step (ends: 6,262 ROUTE, 60 CYC).
    So the defensible form is "no RELAY chain ends in a TOG step; the TOG alternative is never the only one" — not "TOG never occurs".
  - TV-END is far better exercised than the packet's §5 says ("20 classes, all with \|Q_c\| ≤ 1, 39 frozen transitions"), because the lane's
    script triggers on fallback counts while (H) can be tested directly: 66,816 (class, state) pairs reached (H), 24,920 of them with
    \|Q_c\| ≥ 2 and up to \|Q_c\| = 144 (tcL_N12, n 492), and 2,955 in-phase transitions were checked after (H) (805 in classes with
    \|Q_c\| ≥ 1, of which 523 also have an Even vertex of U_c ∖ T with two successors inside the class — the case (iii) is about). Longest
    frozen stretch to the phase's end: 32 transitions (tevlast11_n40).
- N-CHOSEN-7 (cross-check of SELF-FREE). On my 503 𝒞^1O files (\|Q_c\| ≤ 1 per class) there are 3,781 ROUTE and 68 CYC events and ZERO RELAY
  events, as P-N5-FLIP's Corollary SELF-FREE predicts. Independent confirmation of that signed corollary, and the reason CHOSEN's own data has
  to come from multi-choice games.

## 4. Data (DATA, not proof; logs in docs/referee-2/R2-N5-CHOSEN/logs/, reproduce with run_all.sh)
| set | runs | states | phases | ρ events in classes (ROUTE / RELAY / CYC) | CHOSEN checks (TOG) | chains (ends ROUTE / CYC / TOG) | (a) / (b) checks | classes with exact κopt (UNK) | (H) reached (\|Q_c\| ≥ 2) | transitions after (H) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nep90_n40, nep76_n40, frz40, pp_K12_n161, pp_K48_n449 (with the lane's starts) + nep90_n40, nep76_n40, frz40 from S3 | 8 | 485 | 71 | 464 / 307 / 0 | 307 (60) | 307 (307 / 0 / 0) | 296 / 16 | 132 (12) | 73 (8) | 24 |
| lib2o (41 files minus referee games) × 5 starts | 205 | 1,369 | 614 | 208 / 44 / 0 | 44 (5) | 44 (44 / 0 / 0) | 184 / 52 | 920 (16) | 724 (172) | 19 |
| lib41 minus referee games × 3 starts | 1,230 | 19,784 | 7,231 | 4,569 / 5,896 / 56 | 5,896 (169) | 5,896 (5,842 / 54 / 0) | 4,056 / 699 | 10,969 (1,245) | 6,641 (1,916) | 744 |
| my 503 𝒞^1O files × 2 starts | 1,006 | 17,842 | 4,164 | 3,781 / 0 / 68 | 0 | 0 | 3,849 / 616 | 6,577 (999) | 4,613 (0) | 915 |
| random 2 Odd choice vertices, n 5-12 (3,000 × 3) | 9,000 | 21,058 | 19,792 | 222 / 16 / 17 | 16 (2) | 16 (15 / 1 / 0) | 211 / 209 | 27,531 (0) | 23,481 (7,012) | 575 |
| random 4 Odd choice vertices, n 6-14 (2,000 × 3) | 6,000 | 16,257 | 15,616 | 168 / 42 / 15 | 42 (4) | 42 (40 / 2 / 0) | 130 / 127 | 21,805 (0) | 17,795 (9,784) | 332 |
| random, all Odd vertices with choices, n 6-16 (1,500 × 3) | 4,500 | 12,327 | 11,640 | 147 / 17 / 14 | 17 (1) | 17 (14 / 3 / 0) | 126 / 125 | 16,770 (0) | 13,489 (6,028) | 346 |
0 violations in every set, of: CHOSEN (e ≠ c, e ≠ q, the source event or TOG, and both proof equalities), RELAY-CHAIN (distinctness, the
\|Q_c\| − 1 length bound, the stop kind), consequences (a) and (b), TV-END (no Even switch in U_c ∖ T after (H), Ξ constant on Q_c, (H) again at
t + 1), R56 (g)'s trigger ⇒ (H) (147 checks), and my own κ self-checks KADD (2,161,705) and KORD (2,410,459). Maxima: chain length 86 with
\|Q_c\| = 233 (tcL_N12 — the packet's longest chain is 11); Σρ_q in one (phase, class) 474 against the bound 3,029; \|Q_c\| with (H) 144;
frozen stretch 32 transitions. I reproduce the packet's nep90_n40 numbers exactly at its own start (153 ROUTE, 139 RELAY, longest chain 2 in
that run) and its nep76_n40 (129 / 48).
Controls (must fail): next (CHOSEN read with σ̄_{t+1}(q) as the chosen option instead of σ̄_t(q)) 740 failures on lib41 — 40 of them "chosen
exit is c", 104 "no event and no TOG", 203 bad chain ends, 393 bad TOG steps; noH (TV-END's conclusion asserted at every state, without (H))
12,651 failures. Both bite hard, so the checks are not vacuous.
UNK: 2,272 (phase, class) pairs whose κopt enumeration went over budget (3·10⁵ paths) are skipped for the TV-END checks and counted above;
they are concentrated in the big library games (tcL_*, pp_K48_n449).

## 5. Signatures
Lemma CHOSEN, Corollary RELAY-CHAIN with consequences (a) and (b): SIGN, on every game, inside one phase, under the standing SPEC premise
1E-N3 (form P1) and the landed R56 (d). Lemma TV-END: SIGN, conditional on ROOT-C in the repaired form both referees signed (P-N5-FLIP-fixes;
its RESULTS entry R69 is still at CHECKER — N-CHOSEN-5). No gap; notes N-CHOSEN-1..7. REFEREE-2 successor 17 (Opus 5.5, D15).
