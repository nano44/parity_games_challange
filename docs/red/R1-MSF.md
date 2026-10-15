# R1: adversary report on L-SI's S2a "MSF" (most-significant-first single switch)

L-RED, 2026-10-15. Target: docs/si/candidates/S2.md at claude/l-si 95d37d3 (rule MSF), with L-SI's engine
experiments/si/si.py, the "Freezing observation" (Claim F) and the 11:20Z bound MSF iterations <= (n^2+1)(n^2+X+1)
in notes/L-SI.md, and L-LIT's barrier check docs/lit/T12-MSF-barriers.md. Lead brief 11:30Z, box 8 h.
All code and instances: experiments/red/ (vj.py engine, gens_red.py family, correspond.py, xcheck.py, instances/).

## Verdict
| front | verdict | one line |
| --- | --- | --- |
| (B) X / iteration count | **KILLED** | MSF takes exactly 2^N - 1 iterations on gated_bland N (n = 5N+2, m = 9N+2), best-reward start, on L-SI's engine and on mine; every switch is an escaped cycle-creating switch (X = 2^N - 1) |
| (A) the bound | **FLAW** | Claim F is false as stated (two counterexamples); its "cycle-creating" test (v in the path SET of w) is the wrong notion. The corrected Claim F' holds, and the bound's shape survives with the corrected X, which (B) makes exponential |
| (C) implementation fidelity | **HELD** | si.py's VJ valuation and MSF are the rule of S2.md: 0 mismatches against an independent engine (brute force over all counterstrategies, Zielonka, verify.py, switch-for-switch on 24,000 runs) |

Consequence for L-SI's assumptions in S2.md: A1 ("no sink-game gadget can make MSF re-do work at a fixed level exponentially
often") is false: in gated_bland the switch at the fixed level of gate 1 is taken 2^(N-1) times. L-SI's obstruction (b)
(notes/L-SI.md, 11:25Z; quoted in the Lead brief) is refuted by Friedmann's own Lemma 6.1 (section 3 below).

## (B) KILLED: the gated Bland counter

### The family (experiments/red/gens_red.py gated_bland N; instances/gated_bland_N6.pg, _N8.pg)
Start from the Disser-Loho-Maat-Mosis Bland counter G_N (arXiv 2512.16684 v2, Fig. 4.1 p.14, Lemma 4.4 p.13; L-SI's port
experiments/si/gens.py dlmm_bland): sink (Odd, priority 1, self-loop); levels i = 1..N with a_i (Even, 2i+1) and b_i (Odd,
2i+2); a_i and b_i have edges to a_{i+1} and b_{i+1}; a_{N+1} = sink; b_{N+1} (Odd, 2N+4) -> sink. Bland numbers:
(a_i, b_{i+1}) = 2i, (a_i, a_{i+1}) = 2i-1. Lemma 4.4: Bland's rule (lowest number first) takes 2^N - 1 iterations from
sigma_0(a_i) = a_{i+1}.

Gate relabelling: shift every priority of G_N by C = 4N+4 (parities kept) and route each choice of a_i through a simple
cycle in Friedmann's sense (arXiv 1106.0778, section 6.1, Table 1 p.10, Lemma 6.1):
- a_i -> d_i only; d_i (Even, priority 3) -> e_i^a, e_i^b;
- e_i^a (Odd, priority 4N+6-4i, even) -> {d_i, a_{i+1}};  e_i^b (Odd, priority 4N+4-4i, even) -> {d_i, b_{i+1}}.
All gate priorities (3 and 4..4N+2) lie below every shifted priority (>= 4N+7). Ids: sink 0; a_i = 5i-4, b_i = 5i-3,
d_i = 5i-2, e_i^a = 5i-1, e_i^b = 5i; b_{N+1} = 5N+1. PGSolver's best-reward start (S2.md's start) picks for d_i the higher
even priority e_i^a, which is sigma_0 of Lemma 4.4.

### Growth (iterations; si.py and vj.py agree on every row; regions = Zielonka and strategies verified for N = 4, 6, 8)
| N | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| n | 12 | 17 | 22 | 27 | 32 | 37 | 42 | 48 | 53 | 58 | 63 | 68 |
| m | 20 | 29 | 38 | 47 | 56 | 65 | 74 | 83 | 92 | 101 | 110 | 119 |
| MSF | 3 | 7 | 15 | 31 | 63 | 127 | 255 | 511 | 1023 | 2047 | 4095 | 8191 |

vj.py alone continues: N = 14 (n = 73): 16383 in 38 s; N = 15 (n = 78): 32767 in 91 s.
MSF iterations = 2^N - 1 = 2^((n-2)/5) - 1. Every switch is cycle-creating and escaped (Odd reroutes, no cycle node changes),
so X = 2^N - 1 in L-SI's bound. L-SI's variants msfa and msfc (si.py): identical counts for N = 3..8. The other rules on the
same games are fast (N = 3..8, si.py): lsf 1, steepest 1, switch-all N, random-edge 1-9, rar 3-13: the family is built for
MSF and for nothing else. Wall time of vj.py at N = 13: 17 s.

### Why it works (L-RED proof, unrefereed; empirically confirmed switch for switch for N = 2..10 by correspond.py)
Write sigma for a strategy of G_N (choice c_i in {a, b} per level) and sigma' for the gated strategy d_i -> e_i^{c_i}.
1. (Odd escapes.) Under sigma' the 2-cycle d_i e_i^{c_i} is dominated by e_i^{c_i} (even), so Odd at e_i^{c_i} exits to the
   target of c_i (a sink valuation beats any even cycle node for Odd; Friedmann Lemma 6.1(1)). Hence
   Xi'(d_i) = {d_i, e_i^{c_i}} cup Xi'(target(c_i)) and Xi'(a_i) = {a_i} cup Xi'(d_i). The unused gate e_i^{not c_i} has d_i as
   its only predecessor and d_i does not point to it, so it lies on no play.
2. (Underlying valuations are preserved.) By downward induction on the level, Xi'(u) restricted to the vertices of G_N equals
   Xi(u) for every u of G_N, and the gate junk in Xi'(u) sits below every shifted priority. The only Odd choices with an effect,
   at b_i, compare Xi'(a_{i+1}) with Xi'(b_{i+1}); b_{i+1} lies in the second and never in the first (a_{i+1}'s play never visits
   b_{i+1}), so the maximum of the symmetric difference is a shifted vertex and the comparison is the one in G_N.
3. (Improving edges correspond, with designer levels.) The only Even vertices with a choice in G'_N are the d_i. Let e be the
   closed gate e_i^{c_i} with target t', and e* the other gate with target t. Odd at e* chooses between d_i (value
   {d_i, e} cup Xi'(t')) and t. If Xi(t) succ Xi(t') (the underlying edge (a_i, t) is improving), the maximum of the symmetric
   difference of Xi'(t) and Xi'(d_i) is a shifted vertex favouring t, so Odd loops to d_i: Xi'(e*) = {e*, d_i, e} cup Xi'(t'),
   which differs from Xi'(sigma'(d_i)) = {e} cup Xi'(t') exactly in {e*, d_i}; e* is even and above d_i, so (d_i, e*) is improving
   at level (2, rank(e*)) (Lemma 6.1(3), 6.2(3)). If Xi(t) prec Xi(t'), Odd at e* takes t and (d_i, e*) compares {e*} cup Xi'(t)
   with {e} cup Xi'(t'): decided by a shifted vertex in favour of t', so not improving (Lemma 6.1(2)). So the improving edges of
   sigma' are exactly the gates of the improving edges of sigma, and the level of the gate of (a_i, t) is the priority of e_i^t.
4. (MSF = Bland.) Gate priorities decrease strictly with the Bland number, so MSF's maximal level is Bland's minimal number;
   ties never occur. After the switch Odd escapes (step 1), so the new gated strategy corresponds to Bland's new strategy.
   By induction over the run and Lemma 4.4, MSF on G'_N from the best-reward start makes exactly 2^N - 1 switches.
In a sink game every cycle node is the sink and the length equals the size of the path set (Friedmann p.8), so levels (3, .)
and (1, 0) never arise; MSF's tie-break (smallest v, then w) is never used.

### Gate Lemma (L-RED, unrefereed; the reusable obstruction)
Setting. G is a 1-sink parity game (Friedmann section 5: Odd sink of priority 1 with a self-loop, reachable from everywhere,
every other priority >= 2); V_E^2 = Even vertices with at least two successors; lab : {(v, w) : v in V_E^2, w in vE} -> positive
integers, injective. The gated game gate(G, lab) is: every priority of G shifted by C = 2 max(lab) + 4; for each v in V_E^2 a
hub d_v (Even, priority 3) and, for each successor w of v, a gate e_{v,w} (Odd, priority 2 lab(v,w) + 2) with edges
e_{v,w} -> d_v and e_{v,w} -> w; v keeps the single edge v -> d_v; d_v -> e_{v,w} for every w. (vertices + 2 edges per gated
edge, one hub per gated vertex.) Strategies correspond: sigma of G <-> sigma' of gate(G, lab) with sigma'(d_v) = e_{v,sigma(v)}.
Claim. For every strategy sigma of G, writing t for the sink and restricting to strategies reachable by improvements from a
sigma_0 whose plays all reach t (sink-seeking, Friedmann Lemma 5.1): (i) Xi'_{sigma'}(u) cap V(G) = Xi_sigma(u) for every u in
V(G), and Odd's optimal choices at the Odd vertices of G are the same in both games; (ii) the improving edges of sigma' are
exactly the edges (d_v, e_{v,w}) for the improving edges (v, w) of sigma; (iii) the MSF level of (d_v, e_{v,w}) at sigma' is
(2, rank(e_{v,w})), so the first-difference position of the gated switch is a strictly increasing function of lab(v, w) alone;
(iv) the strategy obtained from sigma' by switching (d_v, e_{v,w}) corresponds to sigma[v -> w].
Hence, for every single-switch rule R on gate(G, lab) whose choice among the improving edges is a function of their
first-difference positions (MSF: maximal, LSF: minimal, any fixed order of positions), the run of R on gate(G, lab) from sigma_0'
is, switch for switch, the run on G from sigma_0 of the index-based rule that ranks the edges of G by lab in the corresponding
order (DLMM 2512.16684 Def. 3.7 and Thm 4.3: index-based rules need m^omega(1) iterations on sink parity games). In particular
MSF with lab = (reversed Bland numbers) and LSF with lab = (Bland numbers) on gate(G_N, lab) make exactly 2^N - 1 switches
(DLMM Lemma 4.4), with every switch an escaped cycle-creating switch.
Proof. (i) Under sigma', the 2-cycle d_v e_{v,sigma(v)} has the even dominator e_{v,sigma(v)}, and t is reachable from w = sigma(v),
so Odd at e_{v,sigma(v)} exits (an even cycle node is worse for Odd than t; Lemma 6.1(1)); thus Xi'(d_v) = {d_v, e_{v,sigma(v)}} cup
Xi'(sigma(v)) and Xi'(v) = {v} cup Xi'(d_v); a gate e_{v,w'} with w' != sigma(v) has d_v as its only predecessor and lies on no play.
By induction along the plays (all end in t), Xi'(u) = Xi(u) cup (gate junk below C) for every u of G; every Odd comparison of
G compares two sets whose symmetric difference is non-empty (different successors give different plays, and the play from a
vertex contains it) and whose maximum is therefore a shifted vertex, so Odd's choices agree. (ii) Let e* = e_{v,w},
w != sigma(v), e = e_{v,sigma(v)}. Odd at e* compares {d_v, e} cup Xi'(sigma(v)) with Xi'(w); the maximum of the symmetric
difference is a shifted vertex (w's play contains w, sigma(v)'s play does not contain w unless w's play ... in a sink game
plays are simple paths, and w lies on sigma(v)'s play only if w's play is a suffix of it, in which case the difference contains
sigma(v)'s own vertex), so Odd loops to d_v iff Xi(w) succ Xi(sigma(v)). If so, Xi'(e*) = {e*, d_v, e} cup Xi'(sigma(v)) differs
from Xi'(e) = {e} cup Xi'(sigma(v)) exactly in {e*, d_v}, whose maximum e* is even: improving at level (2, rank(e*)). If not,
Xi'(e*) = {e*} cup Xi'(w) against {e} cup Xi'(sigma(v)) is decided by a shifted vertex in favour of sigma(v): not improving.
(iii) is the level just computed and rank(e*) is increasing in lab. (iv) After the switch Odd escapes at e* (as in (i)), so the
new gated strategy is the gate of sigma[v -> w]. The rule statement follows by induction over the run, and the 2^N - 1 figure is
DLMM Lemma 4.4 (checked switch for switch by experiments/red/correspond.py for N <= 10 and by gate.py for LSF).

### What the gadget shows in general (Lead reading of the mechanism, for the next candidates)
The simple cycle decouples the three quantities L-SI's obstruction (b) assumed to be read "at the same first-difference
position": the SIGN of the switch (d, e) is Odd's current choice at e, i.e. the underlying comparison (Lemma 6.1(3)); the
LEVEL is the priority of e, chosen by the designer; the EFFECT after the switch is the exit's value (Odd escapes). Applied to
every Even edge of any sink game with any priority assignment to the gates, it turns MSF into an arbitrary index-based rule in
DLMM's sense (Def. 3.7, Thm 4.3), so MSF inherits every index-based lower bound, and the same holds for every rule that ranks
improving edges by the position of the first difference (LSF: give the gates increasing priorities; any fixed ranking of
levels). The gate costs 3 vertices and 4 edges per underlying edge. experiments/red/gate.py implements the transform for any
sink game with any distinct labels: on G_N with labels = reversed Bland numbers MSF takes 2^N - 1, with labels = Bland numbers
LSF takes 2^N - 1 (N = 4, 6, 8, 10 run; the same games, only the gate priorities differ).

## (A) FLAW in the bound: Claim F is false as stated; the corrected claim holds
L-SI's definition (notes/L-SI.md, si.py rule_msfa/msfc, freeze_test.py, adversarial.py --objective escapes): the switch (v, w)
is "cycle-creating" iff v lies in the path SET of Xi(w), i.e. (val[w][1] >> rank[v]) & 1. The path set holds only vertices
more relevant than w's cycle node (1106.0778 p.4: {v_i > w_1}), so a v on Odd's play from w that is less relevant than the
cycle node is called non-cycle-creating. Such a switch closes a cycle; Odd escapes; bits far above the level change while
every cycle node stays. Claim F ("a non-cycle-creating switch at level r changes nothing above r") fails:
- instances/claimF_len_cf1.pg (6 vertices, best-reward start = sigma(2) = 1): the single improving edge (2, 3) has level (1, 0)
  and passes L-SI's bit test as non-cycle-creating; after it, Odd at 3 reroutes to 4 and val[2], val[3] gain the path bit of
  vertex 5, the most relevant vertex; cycle node 0 unchanged. Checked on si.py and vj.py.
- instances/claimF_bit_cf2.pg (7 vertices, same start): switch (2, 3) at level (2, rank 5), bit test says non-cycle-creating,
  the bit of rank 6 changes, cycle nodes unchanged.
Scale: re-running L-SI's freeze test with the corrected notion ("v lies on Odd's (sigma, tau)-play from w before the first visit
of w's cycle node") on 20,000 random games with n = 3..9 (11,795 MSF switches): the bit test flags 914 switches, the play test
3,563 (2,649 misclassified); Claim F is violated 6 times among bit-test "non-cycle-creating" switches, 5 of them at level (1, 0),
which freeze_test.py never examines (it checks only lv[0] == 2); violations among play-test non-cycle-creating switches: 0.
Corrected Claim F' (L-RED reading, unrefereed): if v is not on Odd's play from w before w's cycle node, then under (sigma', tau)
every play either avoids v (value unchanged) or is P v (play from w), whose value agrees with the old one above r; Friedmann
Thm 3.2 and Odd's optimality sandwich Xi_sigma'(u) between two valuations agreeing above r, so it agrees above r. The gap L-SI
names ("cannot re-enter") closes because v is not on the play from w. The stretch argument then gives at most n switches per
level (2, r) and at most n per vertex at level (1, 0), so the bound keeps its shape with X := escapes in the corrected sense,
which is >= every X L-SI measured. Section (B) shows X = 2^N - 1 is attainable, so the bound is correct and useless.

## (C) HELD: si.py is faithful to S2.md
experiments/red/vj.py is an independent engine written from the definitions of 1106.0778 section 3 (play decomposition,
path component including the start vertex, set order by the maximum of the symmetric difference, length order by the parity of
the cycle node), with Odd's optimal counterstrategy built as in VJ00 (best cycle node first, then path bits in decreasing
relevance, then shortest/longest path), the same injective-priority tie-break as S2.md (part of the rule), and the S2.md level
and tie-break. Validation (experiments/red/xcheck.py, two seeds):
- evaluate() equals the pointwise minimum over ALL of Odd's positional counterstrategies on 15,810 (game, strategy) pairs
  (n <= 7), and the returned tau realises the valuation;
- 24,000 runs (msf and lsf, best and first start, 6,000 random games n <= 9): final regions = harness zielonka.solve,
  strategies pass harness verify.check, and the switch sequence equals si.py's on every run;
- the family table above and the Claim F instances agree between the two engines.
No fidelity bug found. The only remark: the "escapes" statistic and the msfa/msfc rules in si.py implement the wrong notion
(section A), which does not affect msf itself.

## Evidence (commands, from the repo root)
```
python3 experiments/red/gens_red.py gated_bland 8 > /tmp/g.pg && python3 experiments/red/vj.py msf /tmp/g.pg > /tmp/g.sol   # 255
python3 experiments/harness/zielonka.py /tmp/g.pg | diff - <(cut -d' ' -f1,2 /tmp/g.sol)                                   # regions
python3 experiments/red/correspond.py 2 3 4 5 6 7 8                      # MSF on G'_N == Bland on G_N, switch for switch
python3 experiments/red/xcheck.py --games 500 --nmax 8 --lsi <worktree of claude/l-si>
python3 experiments/red/vj.py msf experiments/red/instances/claimF_len_cf1.pg --start spec:2:1 --trace
```
L-SI's engine on the same instances (read-only worktree of claude/l-si): `python3 -I si.py msf gated_bland_N8.pg` prints
"solved with 255 iterations".

## DONE / FINDINGS / NEEDS
- DONE: this report; experiments/red/{vj.py, gens_red.py, gate.py, correspond.py, xcheck.py, check.sh, instances/}; pushed at claude/l-red 85a83bf and the follow-up commit; notes/L-RED.md.
- FINDINGS: (1) MSF killed: 2^N - 1 iterations on gated_bland N, n = 5N+2, both engines, X = 2^N - 1. (2) Claim F false as
  stated (wrong notion of cycle-creating); corrected F' holds; L-SI's X measurements undercount. (3) si.py faithful.
  (4) The gate gadget makes any first-difference-ranked single-switch rule an arbitrary index-based rule (DLMM Thm 4.3 class).
- NEEDS: Lead: route (4) to L-SI before its next candidate (any level-ranked single switch dies the same way); REFEREE if the
  kill is to be recorded in docs/si/DEAD.md with the proof above rather than the tables alone.
