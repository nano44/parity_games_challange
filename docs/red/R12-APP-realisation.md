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
