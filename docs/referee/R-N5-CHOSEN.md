# R-N5-CHOSEN: REFEREE report on packet P-N5-CHOSEN (L-SI box 19: Lemma CHOSEN, Corollary RELAY-CHAIN (a), (b), Lemma TV-END; every game, inside one phase)
Referee: REFEREE (successor 15), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief; GO 13:44Z Lead stamp). REFEREE-2 successor 17 reviews in parallel.
- Object: docs/si/P-N5-CHOSEN-box19.md, sha1 764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (on the tree, at the l-si freeze b7189738 and at the pin
  trunk 9196c318, an ancestor of HEAD), 129 lines. Author: L-SI successor 15.
- Written 2026-10-26T14:12Z-14:45Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on CHOSEN or FBC on my tree, on trunk or on origin/claude/referee-2 at any of my
  fetches (re-listed in the same turns; 0 / 0 / 0 at 14:43Z). No lane code run (experiments/si/rund/chosen.py, tvend.py, flipcls.py, quiet.py,
  quotecheck.py neither executed nor imported; lane start files read as data). D1.
- Premises read against their text: P-N5-FLIP §1, §3, §4 (setting, EXIT / CLASS EXIT PATH, ROUTE / RELAY, additivity) and RESULTS R69 (c)
  ROOT-C corrected form (landed at a7c141b8, the joint repair quoted from my lane's R-N5-FLIP l. 161-162); RESULTS R15 (a), (d); R38 (a) KEY;
  R56 setting line (T, G_c, G_c^q, κopt_c, κopt^q, Q_c-run, Q-run), R56 (d) κ-Y-FORM_D (with N-FBRED-2 / N-FBRED-3: its "≤" half rests on
  R18 (d) Lemma S (a), every game), R56 (e) FREEZE-EXIT_D, R56 (g) Lemma TV; R57 (a) (VJ) and 1E-N3 (P1).
- Quotes: all 9 «…» passages with [Q path@commit:lines] tags PASS (my lane's own checker scratch/flip_quotes.py, whitespace normalised):
  RESULTS@6f9451e3 l. 2839-2841, 1825-1826, 631, 640, 2858-2859, 2868-2869; P-N5-FLIP@7ea3d8cf l. 48-50, 97; R-N5-FLIP@72db1b18 l. 161-162.
- Tool: scratch/chosen_probe.py (own engine rl_engine and my lane's flip_probe helpers; exact κopt_c, κopt^q by simple-path enumeration in
  G_c, G_c^q with a budget per class; checks listed in §4). Logs scratch/chosen_logs/.

## Verdicts
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §2 | Lemma CHOSEN | SIGNED (note CHOSEN-N1: the identity at t is the play decomposition; the step at t + 1 is R56 (d)'s "≤" half) |
| §3 | Corollary RELAY-CHAIN | SIGNED |
| §3 | consequence (a) | SIGNED (the parenthetical "the stronger … form of ROOT-C's consequence" is a READING, not signed: note CHOSEN-N2) |
| §3 | consequence (b) | SIGNED (note CHOSEN-N3: TOG_c counts events, so its factor \|Q_c\| is slack) |
| §4 | Lemma TV-END | SIGNED |
| §5 | obstruction map (READING), data | not signed (as briefed) |
No gap. Notes CHOSEN-N1..N5. Structural lemmas inside one phase; they bound no count (not ρ, not N_ep, not f) and no running time; not a
TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Setting and premises
- T := Q ∪ {c} for the class at hand. Within U_c it equals R56's T = C ∪ Q (U_c holds one honest cycle node, c), so R56's G_c^q = U_c ∖ (T ∖ {q})
  and "z ∈ U_c ∖ T" mean the same with either T ✓. U_c ∩ T = Q_c ∪ {c}, so "the first vertex of T on a play inside U_c" is the exit of
  P-N5-FLIP §3 ✓ (used in TV-END (ii)).
- Inside a class, λ is fixed on the phase (R38 (a) KEY) and Ξ's order is κ's; κ determines Ξ (a signed sum of distinct powers of two
  determines its set; the length is the second component) ✓.
- (SW) ✓: an Even switch of N5 is to an edge of Iσ: S4a's σ_new(v) ∈ A(v) = {σ(v)} ∪ Iσ(v), S4c switches to an edge of Iσ(v) (R15 (d)).
- ROOT-C in the landed corrected form (R69 (c): class exit path AND exit unchanged ⇒ κ unchanged on Q_c; P1 only) is what TV-END (iv) cites ✓.

## 2. Lemma CHOSEN, re-derived (parentheticals checked one by one)
- y* := σ̄_t(q) ∈ U_c "(λ(q) = c and q's optimal play enters y*)" ✓; y* ≠ q (a self-loop would put q on an honest cycle) ✓; y*'s play at t
  avoids q "(q on no honest cycle at t)" ✓ (q's play is q followed by y*'s), so y* ∈ Y^q_t ✓.
- κ_t(q) = κwt_c(q) + κ_t(y*) ✓. This is the decomposition of q's own play (q, then y*'s play, which avoids q; (V1)), true by definition of
  the play value. The packet attributes it to R56 (d) "(and its "≥" half, i.e. σ̄_t attains the minimum, P1)": the identity needs neither
  half, and the half that needs P1-type optimality is the "≤" half (R18 (d) Lemma S (a)), which the proof uses at t + 1, not at t
  (CHOSEN-N1, wording; the cited facts are all landed, so nothing is missing).
- RELAY: y* ∈ succ(q) ∩ U_c, so p and e are the same at t + 1 ✓. Additivity at s = t, t + 1 (P-N5-FLIP §1, signed as a proof step) ✓.
- Contradiction branch: "(κ(c) is constant in the phase)" ✓ (κ(c) = (0, 0)). y*'s play at t + 1 is p then e's play; p avoids q "(class exit
  paths stop at Q_c ∋ q)" ✓; e = c: c's play is c's cycle, which avoids q (q on no honest cycle at t + 1) ✓. So y* ∈ Y^q_{t+1} and
  κ_{t+1}(y*) = κ_t(y*) ✓. R56 (d) at t + 1 ("≤" half; q on no honest cycle at t + 1 ✓): κ_{t+1}(q) ⪯ κwt_c(q) + κ_{t+1}(y*) = κ_t(q) ✓.
  (SG) and "inside the class Ξ's order is κ's": κ_{t+1}(q) ⪰ κ_t(q) ✓. Equality, Ξ equal, no ρ event: contradiction ✓.
- Conclusion ✓, including its parenthetical "(e has a ρ event at t → t+1)": e ≠ c and e is the first vertex of Q_c ∪ {c} on y*'s play,
  so e ∈ Q_c ⊆ Q, and κ_t(e) ≠ κ_{t+1}(e) ⇔ Ξ_t(e) ≠ Ξ_{t+1}(e) inside the class ✓. Also e ≠ q (y*'s play avoids q) ✓.
- Remark "κ(q) is a minimum of option values that never decrease" ✓ as a reading (options in Y^q, (SG)).

## 3. RELAY-CHAIN, re-derived
- Each step ✓: e_i's event is RELAY, so e_i ∈ Q_c on no honest cycle at t, t + 1, and CHOSEN applies: e_{i+1} ∈ Q_c ∖ {e_i}; it has a ρ event
  or TOG holds at e_i. The sequence continues while e_{i+1}'s event is RELAY, whatever TOG does; it stops at a ROUTE or CYC event, or at
  e_{i+1} with no event, where TOG holds at e_i (the statement's "TOG step") ✓. Every ρ event at q ∈ Q_c is exactly one of CYC (q on an
  honest cycle at t or t + 1), ROUTE, RELAY ✓ ("q = c" in CYC's definition is vacuous for q ∈ Q_c).
- Order ✓: e_i's honest play at t is e_i, y*(e_i), its class exit path, e_{i+1}, then e_{i+1}'s play; so e_0's play passes e_0, e_1, … in this
  order, before c (each e_i ≠ c by CHOSEN). A repeat e_i = e_j (i < j) puts e_i on its own honest cycle at t, i.e. CYC, but e_i was continued,
  so its event was RELAY: contradiction ✓. Distinct elements of Q_c: ≤ |Q_c| − 1 steps ✓.
- (a) ✓. A ρ event at a terminal of the class is at some q ∈ Q_c (Ξ(c) is constant in the phase); ROUTE / CYC give (a) at once, RELAY by the
  chain. Its parenthetical "(This is the stronger, per-event form of ROOT-C's consequence, which only asks for a changed class exit path or
  exit.)" is not an implication: a chain ending at a CYC event or a TOG step names no changed class exit path or exit, so (a) does not by
  itself give ROOT-C's consequence (both hold at every ρ transition, since both are proved). What (a) does prove is P-N5-FLIP's not-signed
  CONJECTURE ROOT-C (strong form) ("every (class, transition) with a ρ event has a ROUTE or CYC event at a terminal of that class", RESULTS
  R69 not-signed list) up to the TOG alternative. Signed without the parenthetical (CHOSEN-N2).
- (b) ✓. Each ρ event at Q_c is ROUTE, CYC or RELAY; a RELAY event maps to the end of its chain at the same transition; events mapped to one
  end are at distinct vertices of Q_c, so ≤ |Q_c| per end; RELAY events ending in a TOG step are counted in TOG_c themselves. Hence
  Σ_q ρ_q ≤ |Q_c|(ROUTE_c + CYC_c) + TOG_c ≤ |Q_c|(ROUTE_c + CYC_c + TOG_c) ✓ (CHOSEN-N3: since TOG_c counts events, not chain ends, its
  factor |Q_c| is not needed; harmless).

## 4. TV-END, re-derived
- The trigger sentence ✓: a Q-run Θ′ (all of Q constant) lies inside a Q_c-run Θ, and κ_{Θ′}(q) = κ_Θ(q) for q ∈ Q_c, so R56 (g)'s formula at
  t ∈ Θ′ (after |U_c| − 1 fallbacks of the phase and of Θ′) is TV_Θ ✓. (My probe checks the landed R56 (g) as a sanity check: TVG.)
- (i) ✓. (SW) gives (x, z) ∈ Iσ_t. In the phase λ_{t+1}(x) = c and x ≠ c (x ∉ T), so x's play at t + 1 enters z and reaches c: λ(z) = c, z ∈ U_c
  (U_c fixed on the phase) ✓; σ_t(x) ∈ U_c likewise ✓. Ξ_t(z) ▷ Ξ_t(σ_t x) inside the class is κ_t(z) ≻ κ_t(σ_t x); κ_t(x) = κwt_c(x) +
  κ_t(σ_t x) (x's play, x not a cycle node) ✓; so κwt_c(x) + κ_t(z) ≻ κ_t(x) ✓.
- (ii) ✓. If x is not on z's play at t before its exit e "(if z ∈ T, then e = z and the play before e is empty)" ✓, then x · (z's class
  exit path) is simple, lies in U_c ∖ T except its end, uses an Even edge (x, z) and the honest edges of the exit path (Even σ_t-edges and
  forced Odd edges, all inside): a simple path of G_c (e = c) or G_c^e (e ∈ Q_c) ✓. Additivity: κ_t(z) = κwt_c(class exit path) + κ_t(e),
  κ_t(e) = κ_Θ(e) (t ∈ Θ; for e = c read κ_Θ(c) := κ(c) = (0, 0), CHOSEN-N4) ✓; so κwt_c(x) + κ_t(z) ⪯ κopt^e(x) + κ_Θ(e) (or κopt_c(x)) ⪯
  TV_Θ(x) = κ_t(x) by (H) — contradicting (i) ✓.
- (iii) ✓. Every switching x ∈ S lies on z(x)'s play at t before its exit; that segment lies in U_c ∖ T (inside U_c, before the first vertex of
  Q_c ∪ {c}); its Even vertices either switch (then they are in S) or keep σ_t; its Odd vertices are outside Q (T ⊇ Q), hence forced ✓. So
  x's play at t + 1 runs x, z(x), then the old segment up to its first S-vertex (which exists and precedes the exit, x being on the
  segment), and repeats from there: it never meets T, so never reaches c, and λ_{t+1}(x) ≠ c, contradicting the phase ✓. That every
  Odd vertex outside Q is forced is exactly why T contains ALL of Q and not only Q_c ✓.
- (iv) ✓. With S = ∅, every class exit path of class c (from every y ∈ succ(q′) ∩ U_c, q′ ∈ Q_c) runs through Even non-switching or forced
  Odd vertices of U_c ∖ T, so paths and exits are equal at t and t + 1; R69 (c) gives κ_{t+1} = κ_t on Q_c, so t + 1 ∈ Θ ✓; for z ∈ U_c ∖ T,
  additivity with the unchanged exit value gives κ_{t+1}(z) = κ_t(z) = TV_Θ(z), with Θ the same run ✓. Induction to the phase's end ✓, and
  "no switch in U_c ∖ T and no ρ event" in the class from t on ✓.
- Remark ✓ as a reading (R56 (e) FREEZE-EXIT_D: S_c = ∅ at late fallbacks; TV-END: every in-phase transition after (H)).

## 5. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks: CLS (every ρ event at Q_c is exactly one of CYC / ROUTE / RELAY), CHO (CHOSEN: y* ∈ U_c with play avoiding q; e ≠ c; ρ at e or
TOG), CHOX (e ∈ Q_c ∖ {q}), CHAIN (RELAY-CHAIN: distinct, ≤ |Q_c| − 1 steps, ends at ROUTE / CYC or a TOG step), CNTB ((b) per phase and
class), TVE (TV-END at EVERY state where (H) holds, with TV_Θ from exact κopt_c, κopt^q; not only after R56 (g)'s trigger), TVG (landed
R56 (g), sanity). Starts: S3 and random start pairs (lane instances: their start files, read as data).
| sample | runs | phases | ρ events ROUTE / RELAY / CYC | CHOSEN checks (TOG alternative seen, always with a ρ event at e) | chains: max length; ends ROUTE / CYC / TOG | (H) states | TV-END checks (with \|Q_c\| ≥ 1) | UNK classes (TV budget) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scratch/fbc_lib.txt (1,140 .pg files of experiments/ and docs/referee/, none of docs/referee-2/), n ≤ 24 (592 files), S3 + 4 random | 2,960 | 12,115 | 2,482 / 678 / 92 | 678 (59) | 11; 658 / 20 / 0 | 12,361 | 788 (385) | 110 |
| random 3,000 games (n 6-20, ≤ 8 Odd choice vertices, seed 251), S3 + 4 random | 15,000 | 44,621 | 644 / 101 / 47 | 101 (3) | 4; 97 / 4 / 0 | 51,832 | 1,698 (811) | 0 |
| random 3,000 games (n 8-24, ≤ 12 Odd choice vertices, seed 252), S3 + 4 random | 15,000 | 49,289 | 780 / 175 / 36 | 175 (8) | 5; 163 / 12 / 0 | 58,279 | 1,870 (949) | 0 |
| lane instances at their start only (NOS3): nep90_n40, nep76_n40, frz40, pp_K12_n161, pp_K48_n449 | 5 | — | 153/139/0, 129/48/0, 21/13/0, 18/13/0, 54/49/0 | 262 (59) | 2; all ROUTE | — | (CHOSEN / chain only) | — |
| the same five, their start and S3, TV budget 3·10⁵ | 10 | 79 | 478 / 311 / 0 | 311 (60) | 2; 311 / 0 / 0 | 101 | 24 (0) | 12 |
- The lane's event counts are reproduced exactly at the five start files (packet §5: nep90 153 / 139, nep76 129 / 48, frz40 21 / 13, pp_K12
  18 / 13, pp_K48 54 / 49), and the library's longest chain is 11, the packet's lib41 figure. TVG: 210 trigger states (38 + 90 + 82), (H) at
  all of them. Per class, CTRL (switches in U_c ∖ T at states where (H) fails) is non-zero in every row with TV-END checks (8,332 in the library batch):
  the switch detection works and TV-END's hypothesis is what separates the two.
- TV-END is NOT thin here (unlike the packet's own data, which waits for the R56 (g) trigger): (H) holds at many states long before it, and
  my check tests the lemma at every such non-final state: 4,356 checks in the library and random rows, 2,145 of them in classes with |Q_c| ≥ 1, 0 failures.
- Mutations (each bites; random 1,500 games, seed 251, S3 + 4 random): MUT=1 (CHOSEN with σ̄_{t+1}(q), the lane's control): CHO fails 5
  times, CHAIN 3 times; MUT=2 ((H) read with TV′ := κopt_c only, the q-terms dropped): TVE fails 24 times.
- A library batch at n ≤ 40 (S3 + 2 random) is still running at the push; its result goes into the §C.
## 6. Notes (none blocks a signature)
- CHOSEN-N1 (wording, §2 first bullet). κ_t(q) = κwt_c(q) + κ_t(y*) is the play decomposition (no half of R56 (d) needed); the step that
  needs optimality is R56 (d)'s "≤" half at t + 1 (Lemma S (a), every game). Relabel the parenthetical.
- CHOSEN-N2 (parenthetical in (a)). "(This is the stronger, per-event form of ROOT-C's consequence …)" is not an implication (CYC and TOG
  ends name no changed class exit path); (a) is P-N5-FLIP's CONJECTURE ROOT-C (strong form) proved up to the TOG alternative. Reword; I
  sign (a) without the parenthetical.
- CHOSEN-N3 ((b)). TOG_c counts RELAY events, not chain ends, so Σ_q ρ_q ≤ |Q_c|(ROUTE_c + CYC_c) + TOG_c; the stated bound holds a fortiori.
- CHOSEN-N4 (notation, TV-END (ii)). κ_Θ(e) for e = c means κ(c) = (0, 0); say so.
- CHOSEN-N5 (data). "TOG never occurs" (§5) holds for TOG-ended chains (0 in my data too), but CHOSEN's second alternative does occur
  together with the first, in every case I saw (frz40 at its start, t 44, class 30, q 0, e 11; pp_K12_n161 at its start, t 3, class 0,
  q 159, e 160, a relay flip 159 ↔ 160; 130 cases in the library, random and lane-with-S3 rows of §5, each with a ρ event at e). The DATA sentence should say "no chain ends at a TOG step".
