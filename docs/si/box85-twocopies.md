# Box 85: TWO COPIES PER LEVEL (L-SI successor 45; Lead GO 05:06Z 2026-11-08)
Written 2026-11-08 (date -u in the commit). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box85/ (two85.py builder from cfg/*.json; ana85.py; dec85.py; flipu85.py; pool85.py; climb85.py; sweep85.py;
runout85.sh; check85.sh, wired in experiments/si/check.sh). Pinned box 81-84 tools: meas83, census81, priv84, lb84 (box84/m2, m3).

## 0. Answer
- TWO COPIES PER LEVEL is DEAD as a counter (§4): at h = 2 it re-arms bit 1 once (the MIRROR picture); at h = 3, 4, 5 the bit sequence
  is MIRROR's, with bit 1 set 3 times and hub e-set height 8 / 11 / 15 (exactly HP3-HP5_mup's, linear). Climbs over 13 wiring kinds and
  lane lengths give CNT ≤ 5 of 8 at h = 3, always with premature resets.
- Exact obstruction: **Lemma FLIP-U (PROVED, lane, §2)**: L-RED's Lemma FLIP holds with every e-set replaced by its part at least as
  relevant as e_S. **Corollary LOW-NULL**: the LOW copy of bit l (e below e_SET_l), and every lower e, cannot add a single flip to B_l's
  SET. The low copy is visible only to lower bits, where it is one more digit value (TC4m: bit 2 toggles 7 times vs HP4_mup's 5; bit 1
  unchanged). So the design's premise («serves as E-MON's carry in B_l's waiting hub») is right about E-MON and wrong about effect: a
  carry e below e_SET_l is invisible to every decision of B_l.
- **Lemma POOL-ALT (PROVED, lane, §3)**: a bit whose upper e-pools (from w and from its other gates) are disjoint is re-set at most
  linearly often. A doubling bit needs a LAGGING copy of the upper counter that merges into the SAME upper e's (§5).
- FLIP-U, FLIP (= FLIP-U's weaker form), PRIV-FLIP, LOWER-BLIND (keep) and POOL-ALT: 0 exceedances on all 11 frozen instances (§4) and
  on 882 sweep genomes (FLIP only). No finding against L-RED's FLIP.
- Reduction (CONJECTURE, §6), with L-RED R223's new split: a SET counter needs (Q1) U-projection heights doubling per level, which needs
  lagging merged copies; a non-SET counter needs (Q2) β/P-decided switches compounding. Neither is realised.

## 2. Lemma FLIP-U (PROVED, lane): FLIP counts only e's at least as relevant as e_S
Setting and premises exactly as L-RED's Lemma FLIP (R222 §4, claude/l-red 5fdb96b3): B a mover, S a SET-type option of B (Ξ-target B,
any β-parity), gate g_S, e-vertex e_S, w = succ(e_S); I an interval with Λ(B) = λ ∈ {K1, K2} and Λ(w), Λ(g_o) constant for o ≠ S.
For a set X of e-vertices let π(X) := {v ∈ X : v is at least as relevant as e_S} (the U-projection). D_U,I(v) := number of distinct
π(E_t(v)), t ∈ I.

Claim: #flips of [σ(B) = S] on I ≤ 1 + (D_U,I(w) − 1) + Σ_(o ≠ S) (D_U,I(g_o) − 1). Since D_U ≤ D_E, this sharpens FLIP.

Two order facts (lex order on finite sets of e's = compare at the most relevant element of the symmetric difference):
- (PROJ) If e_S ∈ X and e_S ∉ Y, then X >lex Y ⟺ π(X) >lex π(Y). Proof: e_S ∈ X Δ Y, so z := max(X Δ Y) is at least as relevant
  as e_S; hence z ∈ π(X) Δ π(Y) = π(X Δ Y) and is its maximum, on the same side. ∎
- (PROJ-MON) X ≤lex Y ⇒ π(X) ≤lex π(Y). Proof: if max(X Δ Y) is at least as relevant as e_S, it is also max(π(X) Δ π(Y)); otherwise
  π(X) = π(Y). ∎

Proof of the claim. Define P^U_t := [Λ(w) = λ, and for every o ≠ S: reward(Λ(g_o)) < reward(λ), or (Λ(g_o) = λ and
π({e_S} ∪ E_t(w)) >lex π(E_t(g_o)))]. FLIP's P_t is the same with π dropped.
- (4′) on → off forces ¬P^U_t. Let σ_t(B) = S and P^U_t. For each o with Λ(g_o) = λ:
  - if g_o's play does not pass B, it does not pass g_S (only in-edge from B), so e_S ∉ E_t(g_o); by (PROJ), P^U's clause for o equals
    P's clause for o;
  - if g_o's play passes B, it continues B g_S e_S w …, so E_t(g_o) ⊇ {e_S} ∪ E_t(w), π(E_t(g_o)) ⊇ π({e_S} ∪ E_t(w)), and the clause
    for o fails, so P^U_t fails: excluded.
  So P^U_t ⇒ P_t, and FLIP (4) gives σ_(t+1)(B) = S.
- (5′) off → on forces P^U_t. If σ_t(B) ≠ S, FLIP (2) gives e_S ∉ E_t(g_o) for every o, so by (PROJ) P^U_t ⟺ P_t, and FLIP (5) applies.
- (6′) P^U_t changes only where some π(E_t(w)) or π(E_t(g_o)) changes. By E-MON each E_t(v) is lex-nondecreasing on I, so by
  (PROJ-MON) each π(E_t(v)) is too, and it changes at most D_U,I(v) − 1 times. FLIP (6)'s counting finishes the proof. ∎

**Corollary LOW-NULL (PROVED, lane).** An e-vertex less relevant than e_S never enters the bound for S. Under [E-LEV] (e's ordered by
level, R104 packet 3.1) this covers every e of a level below lev(B), and a copy of bit l whose e lies at level l BELOW e_SET_l (the
two-copies LOW copy). So the low copy of bit l and the whole lower counter cannot raise the number of flips of B_l's SET by even one:
B_l's flips are bounded by the distinct UPPER parts of the plays of w_l and of B_l's other gates.
- The low copy of bit l is visible only to bits j < l (there it lies above e_SET_j): to them it is one more e at level l, i.e. one more
  digit value, as box 84's CYC option was.

## 3. Lemma POOL-ALT (PROVED, lane; order fact) and what it asks of a counter
**Lemma POOL-ALT.** Let c_1 <lex c_2 <lex … <lex c_m be finite sets of e-vertices, c_i ⊆ P_A for odd i and c_i ⊆ P_B for even i, with
P_A ∩ P_B = ∅. Then m ≤ |P_A| + |P_B| + 1.
Proof. For consecutive c_i <lex c_(i+1) from disjoint pools, c_i Δ c_(i+1) = c_i ∪ c_(i+1), so its maximum lies in c_(i+1):
max c_(i+1) is more relevant than max c_i (max ∅ := −∞). The maxima strictly increase and lie in P_A ∪ P_B ∪ {−∞}. ∎
Use (READING, from FLIP-U's proof): between two consecutive ON events of S, P^U fails at least once, and each ON event needs
a_t := π({e_S} ∪ E_t(w)) >lex b_t := max_o π(E_t(g_o)) (over the o with node λ), each OFF event needs b_t ≥lex a_t. Both chains are
monotone (PROJ-MON). Under PRIV (no play from w or from the g_o passes B), e_S ∈ a_t \ b_t at every t, so b_t ≠ a_t. Then for
ON events t_1 < t_3 < … with OFF events t_2, t_4, … between them: b_(t1) < a_(t1) ≤ a_(t2) < b_(t2) ≤ b_(t3) < a_(t3) < …, so k ON
events give a strict interleaved chain of length ≥ 2k − 1, alternating between a's (pool: e_S and the e's above it reachable from w)
and b's (pool: the e's above e_S reachable from the other gates). By POOL-ALT, if the e's above e_S reachable from w and
from the other gates form disjoint pools, k is at most linear in the number of e's. So an exponential bit needs plays from w and from
another gate of B that reach COMMON e's above e_S, with a's reaching each new common value one step later than b's: a lagging copy
of the upper counter that merges into the same upper e's.

## 1. The build (two85.py; R104 IDEAL format, as pair84.py with MUP = 1)
- Real bits B_1..B_h, mirrors M_2..M_h (HIGH copies: e above e_l, gate key (9, 1, l)), top T = B_(h+1) = M_(h+1), dummies D_l.
- NEW: LOW copies L_l (l ≥ lmin) at level l, same rule as a bit (UP, RS2 lane of length LL_l, SET); their SET e has gate key
  (9, −1, l): at level l, BELOW e_SET_l = (9, 0, l), above every lower level ([E-LEV]).
- NEW: B_l's SET W-target w_l is a mover with options cont → M_(l+1) (MIRROR's) plus cfg "w" (kinds L = L_l, L− = L_(l−1),
  B− = B_(l−1), M− = M_(l−1), B+ = B_(l+1), L+ = L_(l+1), Lw = L_l's own W-target lw_l). Optional extra B_l options cfg "wait"
  (β → target, dead e-face). L_l's UP / lane exit go to cfg lup / lexit; its W-target lw_l has options cfg "lw".
- The brief's design is TC*: w_l = {cont → M_(l+1), carry → L_l}; TC*m also sends L_l's UP and lane exits to M_(l+1); TC*d adds a
  downward option w_l → B_(l−1).

| instance | cfg (h; w; wait; lw; lup / lexit; lmin) | N | M | sha1 (.json) |
| --- | --- | --- | --- | --- |
| TC2 | 2; L; –; M+; B+ / B+; 1 | 62 | 111 | acc300d452b6b84a9aee628209209a8a129ec408 |
| TC2d | 2; L, B−; –; M+; B+ / B+; 1 | 62 | 112 | 0edea23294da38e88066079f6e3f69d94903630d |
| TC3 | 3; L; –; M+; B+ / B+; 1 | 118 | 217 | 2d23725d9a62d61893264e6999389a9f50bcc70e |
| TC3d | 3; L, B−; –; M+; B+ / B+; 1 | 118 | 219 | 19f41dd366162244b917d23e100fc88f5cb9e42f |
| TC3m | 3; L; –; M+; M+ / M+; 1 | 118 | 217 | b75e0184ec4f9579d02d5700ffbd75f84392fc39 |
| TC4m | 4; L; –; M+; M+ / M+; 1 | 258 | 491 | bc3361460cd8e807eb97c9891d87b3ecc5280071 |
| TC5m | 5; L; –; M+; M+ / M+; 1 | 416 | 801 | 4d36d59d5a3a1d87be80f7550331db6ead3e5c61 |
| CL2_21 | climb best (cfg/CL2_21.json) | 108 | 206 | 4d177035f33c53efb66bc1c987351dfd47c81b6c |
| CL2_22 | climb best | 156 | 304 | b86b7f5b9bfc5028ff3501f7adc73111c094bcd1 |
| CL3_31 | climb best | 103 | 193 | bd519fdc6324e9ccde289dd3e58a44e3ff30698d |
| CL3_32 | climb best | 166 | 320 | 36dc2d583e521311697d7f1b6d7aafcdc513efb1 |
Lane lengths in cfg/*.json (TC*m use HP*_mup's L and LM). sha1 = working-tree file at the commit adding it; re-take with
`git show <commit>:experiments/si/box85/inst/<name>.json | sha1sum`.

## 4. DATA (outputs in experiments/si/box85/out/)
Unit: one Howard run of IDEAL-CYC(G) from the stored start; set: the 11 instances of §1; scope: box81/ref idealcyc. Counters (ana85):
tog(l) = steps where bit l changes (bit l = B_l's play passes e_SET_l); CNT = largest k with 0, 1, …, k−1 (bit words as binary
numbers) a subsequence; REARM = bit 1 set → carry reset → set again; hubH (meas83); U(G), maxDE (census81); flipex (priv84, max over
PRIV / non-PRIV SET units of flips − PRIV-FLIP bound).

| instance | T | R | C | tog (B1..Bh) | CNT (full 2^h) | REARM | premature resets | hubH | U(G) | flipex |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TC2 | 12 | 7 | 0 | 3 1 | 4 (4) | 1 | none | 7 | 34 | 0 / – |
| TC2d | 10 | 5 | 1 | 2 2 | 2 | 0 | t 7 | 3 | 34 | 0 / −1 |
| TC3 | 18 | 11 | 0 | 3 3 1 | 2 (8) | 1 | none | 9 | 64 | 0 / – |
| TC3d | 14 | 5 | 4 | 2 2 2 | 2 | 0 | t 5, 9 | 3 | 64 | 0 / −2 |
| TC3m | 17 | 10 | 0 | 5 3 1 | 2 | 2 | none | 8 | 64 | 0 / – |
| TC4m | 37 | 17 | 0 | 5 7 3 1 | 2 (16) | 2 | none | 11 | 136 | 0 / – |
| TC5m | 43 | 20 | 0 | 5 7 7 3 1 | 1 (32) | 2 | none | 15 | 217 | 0 / – |
| CL2_21 | 23 | 9 | 0 | 7 1 | 4 | 1 | t 19, 22 | 9 | 59 | 0 / – |
| CL2_22 | 28 | 9 | 0 | 5 1 | 4 | 1 | t 23 | 8 | 85 | 0 / – |
| CL3_31 | 15 | 9 | 0 | 5 1 2 | 4 | 2 | t 11 | 8 | 55 | 0 / −3 |
| CL3_32 | 24 | 5 | 5 | 4 2 2 | 5 | 1 | t 7, 17 | 4 | 90 | 0 / −5 |
- Against MIRROR (box 84): TC3m's bit sequence equals HP3_mup's word for word; TC4m and TC5m equal HP4 / HP5_mup's except one extra
  toggle of bit 2 (and bit 3 at h = 5) right after the first lane phase (0111 → 0101 → 0111): a low copy acting as a digit value for
  the bits below it. hubH 8 / 11 / 15 = HP3-HP5_mup's. B1 is set 3 times at h = 3, 4, 5 (pool85 ON counts).
- The brief's success test (RF(1) ≥ 2 RF(2) + 2 WITH a re-arm, hub heights doubling) fails on every instance. The climbs reach
  tog(1) ≥ 2 tog(2) + 2 only with premature resets (bit 1 clears without a carry: a digit value, not a re-arm).
- Deciders (dec85; unit: a step where [σ(B_l) = SET] changes; z = most relevant e of the symmetric difference of SET's e-face and
  the best other option): every OFF of every bit is decided ABOVE e_SET_l; every ON is decided by e_SET_l itself (upper parts equal)
  or above. Never below (LOW-NULL, observed: 0 of 96 events).
- Lemma checks, 0 exceedances everywhere: flipu85 (FLIP-U and FLIP over all SET-type units: max flips − bound = 0 on 11 / 11; the
  U-bound is strictly smaller than the E-bound on 28 units); lb84 (LOWER-BLIND keep form: 1,035 steps, 0 mispredictions); pool85
  (POOL-ALT: 0 violations; B1's pools always SHARE upper e's: 2-9 shared, the doubling route that POOL-ALT leaves open, but with ≤ 4 ONs);
  priv84 (PRIV-FLIP).
- Sweeps (unit: one random cfg genome, 882 genomes, h = 2 (715) and 3 (167), seeds 201-204 / 301-304; scratch, not frozen): tog(1) ≤ 6 (with premature resets);
  FLIP excess > 0 on 0 genomes. Climbs (climb85, score (CNT, REARM, tog(1) − 2 tog(2), hubH); seeds 21, 22 (h = 2), 31, 32 (h = 3);
  logs in out/climb/; stopped early at 255-505 / ~250 iterations to free the CPU for verify): best CNT 4 (h = 2, full), 5 (h = 3, of 8).

## 5. Why two copies cannot double (READING from FLIP-U + POOL-ALT)
- By FLIP-U, bit l's flips are charged only to changes of the upper projections a_t = π({e_l} ∪ E_t(w_l)) and b_t = max_o π(E_t(g_o)).
  Bit l sets 2^(h−l) times only if both chains take about 2^(h−l) values, i.e. the hubs w_l and B_(l+1) see an upper counter.
- Interleaving: b < a < b < a … strictly. With disjoint pools, POOL-ALT caps this at the pool size. With a shared pool the standard
  pattern is a_i = {e_l} ∪ X_i, b_(i+1) = X_(i+1): w_l's play shows the SAME upper e's as B_(l+1)'s, one count behind.
- MIRROR's high copies give w_l a pool of mirror e's above the real ones: m(p_i) >lex p_(i+1) whenever a bit above the carry is set,
  so B_l re-sets too early or not at all (box 84 §0). Low copies lie below and are invisible (LOW-NULL). Neither is «same e's, one
  count behind».
- Plays that pass a common e-vertex coincide from there on, so at one time t «same upper e's» means «same route»: no lag. A lag needs
  w_l to reach the same upper e's by a DIFFERENT route at a later time: a lagging copy of each upper hub, merging into the real chain
  right above the current carry level (a «lag tower», one copy per (level, lag depth): O(h²) movers if it worked). Not built; READING.

## 6. The reduction (CONJECTURE), with its strongest DATA
**CONJECTURE TWO-COPY-RED.** On IDEAL-CYC under [E-LEV], every exponential counter for N5′-xi needs at least one of:
(Q1) for SET options (FLIP-ALL, L-RED R223: the whole run under B-ONLY): hubs whose U-projection heights (FLIP-U) double per level,
which needs lagging copies that merge into the real upper e's (§5); (Q2) non-SET options whose switches are β- or P-decided and
compound between e-set changes (L-RED R223 (b)-(c): not charged to e-set changes; DEAD as a bound, frozen
flip223_E_NS_K12_rand_2235_10.json). Copies at fixed relevance offsets (high mirrors, low copies, or both) realise neither.
- PROVED parts: FLIP (L-RED), FLIP-A / FLIP-ALL (L-RED R223), FLIP-U, LOW-NULL, POOL-ALT (here), LOWER-BLIND keep form, LIVE-BREAK,
  LOCK-UP (box 83-84).
- DATA: §4 (11 frozen instances, 882 sweep genomes, 4 climbs): no counter beyond CNT 5 at h = 3; heights linear (8 / 11 / 15).
- Not excluded: the lag tower of §5 (Q1) and a β/P-decided re-arm (Q2). Next (proposal): Q2 first, from L-RED's seed: give each real bit
  a NON-SET option whose e-set ties with its current option (same route above), so that its switch is decided by β's, and measure
  whether a lower bit's P-switches can re-arm it; L-RED takes Q2's bounding side.
