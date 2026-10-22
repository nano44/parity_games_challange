# R12: realising L-ALG's APP(k) as an A_DTL game: a partial design and the wall it hits (L-RED, 10:05Z by date -u; produced on Opus 5.5)
Target (Lead 10:00Z): claude/l-alg docs/alg/GAP-A-M.md section 10. APP(k) is an abstract binary counter on n = 2k+1
vertices with 2^k + 1 searches. Levels i < k are Dom(prevV) pieces whose return set {x_i^{b_i}} leapfrogs between two
p-tops. The bottom stable piece learns t(c) = {z} + {x_i^{1-c_i}} (the leftovers). In the next search t(c) flips the
deepest zero i*. Status words: READING (mine, unrefereed) / DATA. No game is built in this file.

## 1. A wiring of t(c) and what it forces (READING)
- t(c) as a real tangle: the bottom top z (highest priority among the leftovers) -> r (opponent hub) -> q_m^0, q_m^1 for
  every level m, with q_m^b -> x_m^b and x_m^b -> z. At the bottom, the removed copy x_m^{c_m} lies in D_m together with
  q_m^{c_m} (q is attracted into Dom(x_m^{c_m})). So t(c) = {z, r} + {q_m^{1-c_m}, x_m^{1-c_m}}, and its ESCAPES are
  exactly the removed relays {q_m^{c_m} : m < k}. Escapes are always opponent edges leaving the SCC: every leftover-encoding
  hub has the removed copies' relays (or the removed tops themselves) as escapes. That is the source of the wall in
  section 3.
- How t(c) can change piece i*. Redundancy (R10, interim 1): while its top is alive and its escapes are covered, plain
  attraction rebuilds it. So the rescue of x_{i*}^1 must be a LIFT: t(c) fires in the region of a higher top H (here
  H = x_{i*}^0, which is alive for d(x_{i*}^0) - 1 rounds), and x_{i*}^1 -> y with pr(x_{i*}^1) < pr(y) <= pr(H), y -> a
  vertex of t(c). Without the lift, y is threshold-attracted only at pr(y) > pr(x_{i*}^1), so it forgives nothing.
  With it, x_{i*}^1 survives every round in which t(c) fires in H's region. To reach d(x_{i*}^0) + 1, t(c) must fire in
  rounds 1..d(x_{i*}^0) - 1 of piece i*. Each such round requires all its escapes to be covered or outside R.

## 2. Requirement (3) of section 10.4 is not the hard part (READING)
Give every level its own clock, so that its pair (x_i^0, x_i^1) has the same distances (d_i; 1 or d_i + 1) at EVERY piece
<= i, and separate the levels: d_{j} >= d_{j+1} + 2. Then a bottom tangle that fires at pieces j < i* only raises
x_{i*}^1 to d_{i*} + 1 < d_j, so piece j's return set and V do not change. The first difference is at piece i* as APP
requires, and no blocking escape above i* is needed. After the flip, x_{i*}^1 lies in D_{i*}, so t(c) is dead at deeper
pieces (f1), and old tangles t(c') are alive at piece j exactly when c' agrees with c on the levels < j. That matches APP's
r(c, T).

## 3. The wall: the deeper ONES' escapes (READING)
In state c = p.0.1^m, the escapes of t(c) at piece i* are:
- q_j^{c_j} for j < i* (removed above, so forgiven);
- q_{i*}^0 (covered while x_{i*}^0 is alive, through its region);
- q_j^1 for every deeper level j > i* (c_j = 1). These lie in R_{i*} and must be covered in rounds 1..d_{i*} - 1.
What can cover q_j^1 for that long:
 (a) x_j^1 itself (q_j^1 -> x_j^1). x_j^1 is alive at piece i* only for its own distance, which is d_j + 1 < d_{i*} even
     when its own tangle rescues it (levels are separated, section 2). It covers too few rounds.
 (b) a shallower level top that lives long enough at piece i* (q_j^1 -> x_i^0 for i <= i*). Whenever b_i = 0, Dom(x_i^0)
     ATTRACTS q_j^1 (an Even vertex with an edge into the Dom). The relay then vanishes from every later piece, also in
     states where c_j = 0, where it must carry x_j^1 into the bottom tangle. Making q_j^1 opponent-owned stops the eating
     but requires ALL its successors covered, including x_j^1, which brings back (a).
 (c) any vertex that is covered for d_{i*} - 1 rounds at piece i* is either a top surviving that long (so it ties into
     piece i*'s return set) or lies in a region that long, i.e. in the attractor of a top that survives that long. Inside
     piece i* only x_{i*}^0 (and tops that tie with it) survive that long, so this is case (b) with i = i*.
So with leftover-encoding bottom tangles, the deepest zero cannot be flipped: the rescue lasts at most max over j > i* of
(d_j + 1) rounds, which is below d_{i*}. Alternatively the shallow level's Dom eats the deeper relays and destroys the
encoding of the deeper digits.

## 4. What a realisation would need instead (for L-ALG / the Lead)
Either (i) a bottom tangle whose vertex set encodes the state WITHOUT opponent edges into the removed copies of the deeper
1-digits (so the encoding is by presence of player vertices only, and the hub's SCC must still reach every leftover), or
(ii) escapes of the deeper ones that are covered at piece i* through regions of tops that do not survive into its return
set. By (c) that needs a region-partition effect (lift or straddle) at piece i*: R10's (M2) self-reinforcing shape, or a
deficit. I see no way to get (i): reaching a leftover from the hub needs an edge into it, and an opponent hub edge into
the copy that is removed in the current state is an escape. An Even hub vertex reaches one successor only. Sections 1-3
are readings on this wiring, not a proof for all wirings. They say where APP's abstraction hides a cost: it lets t(c) fire
at piece i* "for free", while in DTL its escapes into deeper levels must be kept covered there.

## 5. Correction to section 2: the carry's top TIES into the return set (READING, 10:27Z by date -u)
Section 2 handles the pieces above i*, but at piece i* itself there is a second problem, the APP form of R10's MIRROR.
While t(c)'s top z is alive, z survives a round exactly when t(c)'s escapes are covered in that round (redundancy: plain
attraction rebuilds the tangle). The rescued x_{i*}^1 survives a round exactly when the lift happens, i.e. when t(c)
fires, i.e. when the same escapes are covered. So at piece i* in search s+1, z and x_{i*}^1 lose their support in the SAME
round. The return set (the V of the last round) then contains both. A delay that keeps x_{i*}^1 one round longer would
need a support that is covered in a later round but not earlier. Coverage only shrinks over the rounds of one call
(without deficits), so that support would also cover x_{i*}^1 in search s, where nothing is rescued.
Consequence: with ONE bottom top z shared by all t(c) (as in section 1), Dom of piece i*'s return set removes z whenever
level i* holds a 1, and the bottom loses the top of every future tangle. What survives: one bottom top PER LEVEL, z_i, as
the top of every t(c) whose deepest zero is i. z_i is then removed at piece i exactly in states with b_i = 1, which are the
states that need no new deepest-zero-i tangle. Whether the rest of the wiring survives this change (other levels' z_j must
not join z_i's region; the deeper ones' escapes of section 3 remain) is OPEN. Section 3's wall is untouched by this change.

## Stamp correction (10:13Z by date -u)
Section 5's heading says "10:27Z by date -u". That is wrong: the `date -u` reading taken in the same command was 10:10Z (commit e7cf65d). From now on headings are generated from `date -u` inside the command that writes them.

## 6. (M2) loops are impossible for LIFT-based rescues, so APP via lifts is blocked by MIRROR (READING, 10:20Z by date -u)
R10's (M2) says that a working pruning-driven carry t must be self-reinforcing: from some round on, an escape of t is
covered only by vertices that t keeps alive. For a rescue by LIFT (t fires in the region of a host H above t's top and
carries a vertex y with pr(t's top) < pr(y) <= pr(H) into Z) this cannot happen:
 (i) the lift covers only vertices of priority <= pr(H) (cap), and every vertex rescued through y has priority < pr(y)
     (else the threshold phase forgives it anyway). So everything t keeps alive lies BELOW H;
 (ii) t fires in H's region only if its escapes are covered at H's turn, i.e. lie in regions computed before H's or
     already in H's region before t fires (t's own products cannot count: firing needs the escapes first);
 (iii) vertices below H are processed after H, so they cannot provide (ii) in the same round;
 (iv) a vertex w ABOVE H that points into the lifted part (w -> y) is, in the earlier search, forgiven by the threshold
     phase at pr(y) < pr(w) for as long as y's successor (a vertex of t, e.g. its top) is in Z. That holds exactly while
     t's top is alive, i.e. (redundancy) exactly while t's escapes are covered: the same condition under which t fires
     in the later search. So w's survival does not distinguish the two searches and cannot reinforce anything.
So a lift-based carry is never self-reinforcing, and by (M1) it cannot move a domfirst piece's return set to the rescued
vertex. Its top survives with the rescued vertex, and Dom removes it before the carry can be learned. Since redundancy
leaves only lifts and straddles as ways for a stored tangle to change a pruning round, APP's level digits in A_DTL would
need the straddle (a deficit), not a lift. That matches the 2CE result, where the (S) gate also reduced to a triggered
deficit.
Caveats: equal priorities (the cap test is <=, and processing order among equal priorities is by index) are not
analysed; the redundancy reading itself is unrefereed; "coverage only shrinks over the rounds of one call" is used and is
false in general (deficits). So this is a statement about deficit-free calls.

## 7. DATA for the redundancy reading used in R10 (MIRROR) and section 6 (10:28Z by date -u)
experiments/red/carry/redundancy.py replays every pruning round of every best_vertices call twice from the same V: with
all tangles, and with every tangle whose top is in V disabled. It strategy-saves, and its full replay reproduces the actual
call (0 mismatches). A round where the survivor sets differ is a LIFT if some disabled tangle fired, in the full replay,
inside the region of a top other than its own; otherwise it is OTHER (an OTHER would contradict the reading).
- 116 files (tc+ 2-4, dtl_mviol_n20, every L-ALG instance, this lane's R9/R10 instances): 11,895 rounds, 452 survival
  changes by top-alive tangles, all 452 LIFT, 0 OTHER.
- 2,000 random games with n <= 18 (`--random 2000 18 21`): 14,542 rounds, 8 changes, all LIFT, 0 OTHER.
The classifier is permissive: a LIFT label says a lift happened in that round, not that the lift alone caused the
difference. So this supports the reading but does not prove it.

## 8. Scope of sections 3, 5 and 6, after L-ALG's dead-top cap carries (10:32Z by date -u; answers the Lead 10:28Z and 10:31Z)
- Section 6 (and R10's MIRROR) covers ALIVE-top carries only. MIRROR's first step (death_s(h) >= r0 + 1) uses that h is
  a candidate in round r0 and is forgiven exactly when the carry's escapes are covered below pr(h). A DEAD-TOP CAP carry
  (L-ALG GAP-A-M.md section 11: top pruned before r0 in both searches) fires in the threshold phase, or a higher region,
  at a threshold theta >= the priority of an escape ABOVE h. That escape is attracted only at such thresholds, which is
  why h itself is never forgiven. So it rescues only candidates of priority > theta, and its top dies early in both
  searches. Neither MIRROR nor (i)-(iv) applies. So section 6's "digits need deficits" holds for alive-top lifts only.
  Dead-top cap carries remain a lift route for APP, as the Lead wrote.
- Section 5 (the tie) is about alive-top carries and does not apply to cap carries: their top is dead, so it is not in
  the return set.
- Section 3 (WALL 1) does NOT generalise; L-ALG is right. My cases (a)-(c) assumed the deeper ones' relays are covered in
  REGIONS. A relay of priority above the shallow level top's cap is never in that top's Dom (so not eaten), but it is still
  attracted in the threshold phase at its own priority while the shallow top is alive. That covers it for a cap carry
  whose rescued vertex lies above the relay. So WALL 1 holds only for region coverage and alive-top lifts.
- Climb report (Lead's question): the fresh-context fitness (dtl_search fitness `fresh`) is gameable. Its best scores
  (16 at n = 38 from dtl_replay4_n32, 8 from dtl_replay2deep_n32) come from depth-1 replays at deep piece indices (levels
  8, 0, 8 and 6, 0, 6 in experiments/red/carry/levels.py), which the weight (j + 1) rewards. That is no new structure,
  i.e. an ARTEFACT. Separate climbs on `resets` from dtl_mviol_n20 reach 42 at n = 20 (vs 30) through cut-attractor
  growth at an unchanged result (a known uncovered case, GAP-A-M section 6), also no counter.

## 9. Anatomy of a dead-top cap carry, and where APP's deepest level gets stuck (READING, 10:39Z by date -u)
Let C (top h) rescue a candidate u at a -1 piece i through the threshold phase, with h dead (L-ALG's type (b)).
 (C-a) C fires at a threshold theta >= pr(e) for some escape e with pr(h) < pr(e), and u is forgiven only if
       pr(u) > theta. So pr(h) < pr(e) < pr(u).
 (C-b) While h is alive at piece i, e lies in NO region: any region holding e has a top of priority >= pr(e) > pr(h), is
       computed before h's, and consumes e, so (with C's other escapes covered) h's own region closes and C is an alive-top
       carry. So e is covered at piece i only in the threshold phase.
 (C-c) At the learning piece P (where C is extracted), e is outside R_P or consumed by a region of P computed before h's.
   - If piece i's own Dom removed e, then e lies in Dom(M_i), which is contained in piece i's final-round region, which
     (without deficits; coverage only shrinks over the rounds of one call) lies in the union of regions at every earlier
     round. That contradicts (C-b). So e is removed by a piece DEEPER than i (a later level piece, its Dom or a cut), or
     consumed at P.
   - Consumed at P by a top zeta of P with pr(zeta) >= pr(e): zeta must not hold e in a region at piece i while h is
     alive (C-b), so zeta is pruned at piece i by then. Yet zeta is alive at P. What revives zeta is forgiven only between
     piece i and P, i.e. removed by a deeper piece again (removal by piece i's Dom puts it in every region of piece i, as
     above).
For APP this means: the carry that flips level i needs, between level i and the bottom, a piece that removes its high
escape (or what keeps that escape's consumer alive). For the DEEPEST level k-1, the only pieces between it and the bottom
are cuts or pieces outside APP's level structure. So APP's least significant digit cannot be driven by a dead-top cap
carry unless an extra (cut) piece is inserted below it. Such a cut is a cut-eaten level, where R10's (F) applies again:
its driver is learned in the stable piece right after the cut, before any deeper level runs.
Status: a reading, under the same no-deficit premise as MIRROR. It is the precise shape a realisation must take. It is
not a proof that APP is unrealisable, because the inserted cut's own constraints are not worked out here.

## 10. Section 9 restated after L-ALG's data (l-alg 145204d, GAP-A-M 11c, C6; via the Lead 11:13Z) (11:36Z by date -u; produced on Opus 5.5)
Two steps of section 9 fail on data. The conclusion "APP's least significant digit needs an extra cut" is WITHDRAWN. It
is now an open question.
- (C-a) is FALSE as stated. In 12 dead-top carries no escape in R has priority above pr(h). Smallest: dtl_proof_c3,
  search 1, piece 0. Tangle {y, s} (top y, pr 2) has its only escape w at pr 1, but covering w needs threshold 3, because
  of a vertex x on w's attraction path.
  Corrected form (L-ALG's): some escape e of C is covered only at a threshold theta > pr(h), witnessed by a vertex x with
  pr(x) = theta on e's attraction path, and pr(h) < theta < pr(u).
- (C-b) survives with x in place of e (READING). If x lay in a region at piece i while h is alive, that region's top has
  priority >= pr(x) > pr(h) and is computed before h's. With the cap at least theta, the same attraction path then
  covers e in the region phase. Lower regions have caps below pr(h) < pr(x). So x lies in no region at piece i while h
  is alive, and e is covered only in the threshold phase.
- (C-c), first step, is REFUTED. "Dom(M_i) is contained in piece i's final-round region, which is contained in the union
  of the regions at every earlier round" fails in 17 cases: a high escape left R at piece i itself, in the learning
  search, with P > i. Example: cross_h_k1_n10_m16_27, search 1, piece 0, tangle 0 (top 2, high escapes 4 and 9).
  Lead/L-ALG reading: the inclusion runs opposite to Lemma D3's. My reading: with more tops, a vertex whose successors
  are split over two regions is attracted into neither (the straddle of Lemma E), so the region union is not monotone
  in V and the second inclusion has no basis. In the other cases P > i held throughout: 225 where the escape left
  between i and P, 36 where it was consumed at P.
- What remains: a dead-top cap carry at piece i needs its high-threshold witness x to be in no region while h is alive
  at i, and covered in the threshold phase. Whether the deepest APP level can host one without an inserted cut is open.
  L-ALG's phi_idx_flat_n20 (R13, last section) is a single-level instance at a domfirst index 2, whose driver is learned
  in piece 3's cut recursion (P = 3 > i = 2). The k=2 build starts from it.
