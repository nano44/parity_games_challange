# N5 on o-cyclic one-Odd-choice games: box 25 (CYC), what is settled, what is refuted, and the exact obstruction
L-NEW successor 9 (Opus 5.5, D15). Lead GO 2026-10-24 04:47Z (date -u); box to ~07:50Z; stop rule ~07:00Z.
Status: no polynomial bound is claimed and no induction survived. Every statement is labelled PROVED, READING, DATA or FALSE.
Nothing here is refereed. G-N5-TIME stays OPEN.
Object: N5 = docs/new/N5-ssi-global.md SPEC S1-S5 (experiments/new/n5.py, run unmodified). Notation as in docs/new/N5-1Oacyc-box24.md
§1 (packet P-N5-1OA, RESULTS R18) and docs/new/N5-1Ocyc-box24.md (box 24 o-cyclic notes): 𝒞^1O, o, d, X, Y, θ = Ξ(o), w = W(o),
U_τ, R (σ-path reaches o), pure transition (σ|X and τ unchanged), F_τ (frozen run).
Code: experiments/new/box25/ (read-only use of n5x.py, h1.py, pureY.py, si.py). Every instance cited is checked: Oink zlk OK,
strategies verified (check_sol2.py, Oink 8fbf0a7).

## 0. Result in one paragraph
- Lemma 1 of P-N5-1OA holds on ALL of 𝒞^1O. REFEREE-2's N-3 reading (argument and data its own) is correct; this box re-checks it
  independently, with a control. The signed text's §6 phrase "has no analogue" is
  inaccurate: on o-cyclic games the lemma holds verbatim and is vacuous when X = ∅ (§1).
- Reduction (READING, DATA-exact): Prop X lifts from X to Z := X ∪ Reach(o). So the core is G[Z], i.e. X plus o's strongly
  connected component (§2). The natural companion "Z frozen ⇒ θ = w" is FALSE (zfrozen_thr, n 13), so the part above Z is not
  automatically one-player.
- W-drops at fallbacks: box 21's open statement (WF), "fallback steps are W-flat", was first refuted in box 22 §3
  (i1h_fts_best16, n 11, canonical; sha1 3a54502c…). This box adds the following (§3):
  - smaller instances: n 4 from a random start (wdrop_cyc), n 8 from the canonical start (wdrop_canon);
  - the localisation: drops occur on o-cyclic games only (none found on o-acyclic games; i1h_fts_best16 is o-cyclic);
  - the rates;
  - a proof that fallbacks are W-flat under (h) at unthrottled states;
  - a climb with 12 W-dropping fallbacks in one phase (n 16).
  At throttled states under (h), W can drop. i1h_fts_best16 already does this (2 of its drops are at (h)-states); fbh_drop9 (n 9)
  is a smaller instance. In random samples drops are rare under (h) (0 of 1,010 fallbacks) and frequent off (h).
- Smallest σ̄-lap (σ̄(o) returns to an exit inside one (τ, joint-λ)-phase): n 6 (lap_n6). The previous smallest known lap was
  fts_best16 (n 16). Box 22 §3 had a fallback-driven return of an Even vertex at n 11, which is not a σ̄-lap. No lap was found at
  n 4-5 in 380,899 random games (§4).
- The exact obstruction (§5) is box 22's TRUST MODE (box 22 §1.3-§1.4; box 21 §3.6 (ii)), consolidated here with the W-drops and
  a parametric reading. Every candidate induction stalls on it. A vertex z ∈ R keeps a route through o because
  the selection evaluates o at w, while its honest value π_z ⊕ θ is below an o-free route of z. Such a z blocks the o-free
  Bellman-Ford progress of every exit whose route passes z, and θ can rise only through that progress. A trust routing ends only
  when (i) θ rises, (ii) z's o-free route beats π_z ⊕ w, or (iii) a fallback forces z out, which can lower W (§3; off (h), and
  under (h) at throttled states).
  Open statement (TRUST), §6.

## 1. Lemma 1 on o-cyclic 𝒞^1O (settles N-3 against signed §6)
Statement (P-N5-1OA Step 2): at a pure transition from state k, σ_k|X has G[X]'s optimal valuation.
- PROVED on all of 𝒞^1O, conditional on (P) for one-player G[X], exactly as in P-N5-1OA Step 2. That proof uses:
  - Prop X, which holds on every 𝒞^1O game, o-acyclic or not (RESULTS R18 (a));
  - R17 (F1)/(F2);
  - (P) on the one-player game G[X].
  o-acyclicity is first used in Step 3 (Lemma 2: every exit of o lies in X). So Lemma 1 transfers verbatim. When X = ∅
  (fts_best16), it says nothing.
- So the signed text's §6 sentence "Lemma 1 has no analogue (X may be empty)" should read "Lemma 1 holds and is vacuous when X = ∅".
  This is a wording item, not a gap.
- Credit: REFEREE-2 N-3 (docs/referee-2/R2-N5-1OA.md l.100) gave this argument with 225 o-cyclic pure states; R18 (iii) records it as
  accepted. What this section adds is an independent check (G[X]'s optimum computed separately, rank-free), with a control that
  fails, on 15 times as many pure states.
- DATA (box25/lemma1cyc.py; it checks Ξ_k|X against G[X]'s optimal valuation, computed independently, rank-free; it also checks
  Prop X itself):

  | sample | runs with X ≠ ∅ | pure states | Lemma 1 failures | Prop X failures |
  | --- | --- | --- | --- | --- |
  | random o-cyclic, n 4-14, canonical, seed 25 | 1,101 | 502 | 0 | 0 |
  | random o-cyclic, n 6-20, random starts, seed 26 | 2,034 | 1,964 | 0 | 0 |
  | random o-cyclic, n 6-20, canonical, seed 27 | 1,363 | 943 | 0 | 0 |
  | negative control: seed 25 at ALL states (`--allstates`) | 1,101 | 1,166 | 266 | — |
  | cyc4 / i1h_fts_best16 / i1hn_fts_best16 | 3 | 1 / 8 / 8 | 0 | 0 |

  The control shows the check can fail: Lemma 1 is about pure states only.

## 2. Reduction to G[Z], Z := X ∪ Reach(o)
Proposition Z (READING; proof sketch; DATA-exact). Let Reach(o) be the vertices reachable from o, and Z := X ∪ Reach(o).
- Z is closed under successors. A successor of a vertex reachable from o is reachable from o, and X is closed.
- Every Odd choice lies in Z (o ∈ Z).
- Hence, along any N5 run on a 𝒞^1O game G, the sequence of distinct values of (σ|Z, τ) is N5's run on G[Z] from the restricted
  start.
Proof sketch: L-RED's argument for Prop X (docs/red/R58-n5-width.md §9) uses only three facts:
- the closure of X;
- the locality of S1's valuation procedure on a closed set;
- the decomposition of S4a, S4b and S4c along a closed set. A fallback in G waits while the outside moves, and then switches the
  same edges.
Z satisfies all three, with o inside. The point that needs care is the delayed fallback: G[Z] would fall back while vertices
outside Z still move. During the delay (σ|Z, τ) stays constant, since S4a and S4b on Z return it unchanged, so only repeated
values are inserted. This is a reading, not a refereed proof.
- DATA (box25/propz.py): exact identity in 2,124 runs (canonical, n 4-16, seed 31) and 2,462 runs (random starts, n 6-20, seed 32);
  0 failures. Games with Z = V are skipped (1,283 / 853).
- fts_best16, cyc4 and lap_n6 have Z = V. The obstruction lives inside G[Z].
What it does not give.
- Let A := V \ Z: the vertices that reach o but are not reachable from o. A moves alone only while (σ|Z, τ) is constant.
- The tempting lemma "while only A moves, θ = w" (then A would run as a one-player N5 segment in G_τ, bounded by R17) is FALSE:
  box25/zfrozen_thr.pg + .start (n 13, sha1 93c6030c54d5…, random start).
  - At state 0, G[Z] is stalled: its S4a and S4b return (σ|Z, τ), and its next step would be a fallback. Meanwhile A's vertex 10
    switches 12 → 9.
  - Odd's honest σ̄(o) = 7 closes the Odd cycle o-7 (priority 9), while τ(o) = 0 gives the Even cycle o-0-7 (priority 10). So θ ◁ w.
  - (o, 7) ∉ Iτ: U_τ(7) and U_τ(0) lie on the same Even cycle.
- DATA: stretches in which only A moves have length ≤ |A| in every sample.
  - Random o-cyclic games, n 6-18, seeds 41/42: 3,633 + 3,626 runs, 0 throttled states.
  - Planted above part (box25/abovebig.py: m-vertex o-cyclic core plus k Even vertices into it), (m, k) = (8, 8), (10, 12),
    (12, 16): 3,800 runs, longest stretch 5, 1 throttled state (random start).
- So 𝒞^1O reduces to G[Z] up to the A-stretches, and an A-stretch is the "two-terminal" problem of §5 with Z frozen.
  READING: this is no easier in principle than the core. In the data it is short.

## 3. W-drops at Even fallbacks: smaller instances, localisation to o-cyclic games, and the (h) split
Box 21 §2.5 proved W_{k+1} ⊵ W_k at arena steps of an F_τ run and W_{k+1} ⊴ W_k at fallback steps. It left "fallbacks are W-flat"
(WF) OPEN, with 52 fallbacks, all flat, in 1,500 random games.
- FIRST REFUTATION: box 22 §3 (docs/new/N5-1O-box22.md), i1h_fts_best16 (n 11, sha1 3a54502c…, canonical; 3 fallbacks, each lowers
  W). i1h_fts_best16 is o-cyclic. By wdrop_h.py, 2 of its drops are at states satisfying (h) and 1 is not.
- New here: smaller instances and the localisation (DATA, verified instances; box25/wdrop_find.py, wdrop_canon.py, wmono_cyc.py):
- n 4, random start: box25/wdrop_cyc.pg + .start (sha1 d2684b7b752d…). Priorities 0:2, 1:6, o = 2:2 (Odd), 3:3. Edges: 0 → {0,1,3},
  1 → {0,3}, o → {0,1,2,3}, 3 → {0,2,3}. Start σ = (0:0, 1:3, 3:3), τ(o) = 2 (o's self-loop).
  - State 0. θ = Ξ(o) is o's Odd cycle through 3 (σ̄(o) = 3); w = (o, ∅, 0), o's own Even self-loop. Iτ = ∅. Arena step: 3 → 2 (into R).
  - State 1. σ = (0, 3, -, 2). Iσ = {(1,0), (3,0)}, both edges leave R (type d2): honest-improving, since 0's self-loop (priority 2)
    beats the Odd cycle 3-o.
    - Against τ, both 1 and 3 do better staying routed through o: cycle node o, rank 1, against cycle node 0, rank 0. So the arena
      returns σ.
    - S4c (Even switch-all on Iσ) switches 1 → 0 and 3 → 0. W(1) falls from (o, {1,3}, 2) to (0, {1}, 1), and W(3) from
      (o, {3}, 1) to (0, {3}, 1).
  - N5: 3 iterations, 1 fallback. Oink zlk OK, strategies verified.
- n 8, canonical start: box25/wdrop_canon.pg (sha1 a5007dfe1ac7…), smaller than box 22's n 11. At state 1, vertex 1 leaves R by
  the fallback and W(1) drops. N5: 4 iterations, 1 fallback. Oink zlk OK, strategies verified.
- Rates (wmono_cyc.py, o-cyclic, n 5-16): canonical starts 0 drops in 195 fallbacks (5,126 runs, seed 61); random starts 4 drops in
  261 fallbacks (5,137 runs, seed 62).
- o-acyclic 𝒞^1O: no drop in 20,000 random games with random starts for each n = 3..10 (wdrop_find.py --acyclic, seed 8). This is
  consistent with P-N5-1OA Lemma 3: at pure steps Ξ = W, so an honest switch is a W-switch.
- Many drops in one phase (climb box25/wdropclimb.py, canonical start, fitness = W-dropping fallbacks inside one (τ, joint-λ)-phase):
  see §7 for the final numbers.
Where it happens (box25/wdrop_h.py, fbh.py, fbhclimb.py).
- In random samples every W-drop violates box 21's hypothesis (h) at the dropping state. That is: o lies on a cycle of the
  (σ, σ̄)-play or of the (σ, τ)-play from o, or Ξ(o) and W(o) have different cycle nodes. Under (h), drops exist but are rare in
  random samples: box 22's i1h_fts_best16 and fbh_drop9 below.
  - wdrop_cyc and wdrop_canon: τ(o) is o's own self-loop, so w is a cycle at o, and σ̄(o) closes an Odd cycle through o.
  - Samples: 21 drops in 17,974 random-start runs (n 4-12, seed 81); 0 in 5,210 canonical runs (n 8-16, seed 82). The climb bests
    of §7 have 7 and 14 drops. Every one of these is non-(h).
- Fallbacks under (h) (fbh.py):
  - n 5-16, seeds 91 / 92 (canonical / random starts): 147 / 227 of 254 / 378 fallbacks satisfy (h); none is at a throttled
    state; none lowers W.
  - n 8-20, random starts, seed 93: 636 of 1,032 satisfy (h); 1 is at a throttled state; none lowers W.
  - That one: box25/fbh_thr.pg + .start (n 9, o = 1). State 1: θ ◁ w, Iσ = {(7, 4)}, an edge leaving R (type d2). Its W is a TIE:
    W(4) = W(o) = (3, ∅, 1). So the fallback is W-flat. Oink zlk OK, strategies verified.
- PROVED (uses Lemma G (a)-(b), R17 (F1) and P-N5-1OA's flat-case analysis; NOT (P)): under (h) at an unthrottled state (θ = w),
  a fallback is W-flat.
  - By Lemma G (a)-(b) with θ = w, Ξ = W everywhere. So the gate (Ξ-improving edges) is exactly G_τ's improving set.
  - S4a's arena is the arena of the one-player game G_τ over {σ(x)} ∪ I(x). It returned σ.
  - So, by the case analysis of P-N5-1OA Step 2 (b) (B1/B2, run in G_τ with valuation W; it uses only (F1) and the order), every
    improving edge is flat: x = λ(x), and z lies in x's region.
  - The fallback switches at most one edge per vertex, each of them flat. Switching flat edges changes no valuation (R17 Theorem
    PH, last paragraph; P-N5-1OA Step 2, "Flat switches"). □
- FALSE (FB-H), "under (h), every fallback is W-flat". It was already refuted by box 22's i1h_fts_best16 (n 11, canonical; 2 drops
  at (h)-states). A smaller instance is box25/fbh_drop9.pg + .start (n 9, sha1 f25c9990…, random start; found in 21 s by
  fbhclimb.py, n 9, seed 1).
  - Priorities 0:1 (Odd, → 7), 1:0 (self-loop), 2:5 (Odd, → 1), 3:6 → {4, 5}, o = 4:4 (Odd) → {3, 6, 8}, 5:2 → {2, 3}, 6:2 → 1,
    7:3 (Odd, → 0), 8:7 → 5.
  - State 0: σ(3) = 4, σ(5) = 2, σ(8) = 5, τ(o) = 6.
    - w: o → 6 → 1, giving (1, {4, 6}, 2). θ: σ̄(o) = 8, o → 8 → 5 → 2 → 1, giving (1, {2, 4, 5, 8}, 4). So θ ◁ w. (h) holds: neither
      play from o returns to o, and both have cycle node 1.
    - Iσ = {(3, 5)}, leaving R. Honestly, 3 → 5 drops the odd 8 from 3's path, so it improves. Against τ, 3 → 4 → 6 avoids the odd 2
      (priority 5 > 4), so 3 stays: the arena returns σ.
    - Odd's gate is empty: U(8) ⊵ U(6), because 8's best reply against τ runs 8 → 5 → 3 → o: self-throttling.
    - The fallback switches 3 → 5, and W(3) falls.
  - N5: 2 iterations, 1 fallback. Oink zlk OK, strategies verified.
  So (WF) fails under (h) too, at throttled states, as box 22's instance already showed. New here: the unthrottled case is PROVED
  W-flat.
Why it happens off (h) (READING). A fallback fires when the arena against τ returns σ while Iσ ≠ ∅. In wdrop_cyc, vertices 1 and 3 are
routed into o's Even self-loop: W through o is the cycle at o, while honestly o continues into the Odd cycle 3-o. Their o-free edge
to 0 is honest-improving but W-worse, so the arena refuses it; the fallback forces it. This is the trust → honest reset of §5,
in the configuration where o's plays are cycles (box 24 §2's "second mechanism", a ∈ R).
Consequences.
- As box 22 §3 already said, W is not a monotone potential once fallbacks occur. New here: on o-acyclic games no drop was found,
  and under (h) drops need a throttled state. Box 21's Lemma PT (consecutive arena steps) is untouched.
- Under (h), Lemma W holds in full at unthrottled states. At throttled states it fails (fbh_drop9).
- For L-RED (READING): W-resets exist both off (h) (o on a cycle of its W-play, e.g. τ(o) closing a cycle at o) and under (h) at
  throttled states (i1h_fts_best16; fbh_drop9, a self-throttled exit 8 whose best reply runs through o). Box 22 §3 already
  called the fallback "a second return mechanism".

## 4. σ̄-laps: smallest instance n 6
A LAP is a return of σ̄(o) to an exit it left earlier inside the same (τ, joint-λ)-phase. θ is then strictly higher, since θ is
non-decreasing (R15 (a)) and changed in between. Laps are what let the θ-count of a phase exceed d − 1.
- box25/laps/lap_n6_s1_110421.pg (n 6, sha1 4f4fe69c51e1…, canonical start). Priorities 0:3, 1:1, o = 2:7 (Odd), 3:3, 4:2, 5:1.
  Edges: 0 → {2,4,5}, 1 → {2,3}, o → {0,4}, 3 → {0,5}, 4 → {0,1}, 5 → {2,5}.
  - σ̄(o) goes 0 → 4 → 0 within one phase. At state 1, θ ◁ w. Exits 0 and 4 lie on one σ-path at state 0 (0 → 4 → 1 → 3 → 5).
  - 2 iterations; θ changes twice in the phase, with d = 2.
  - Oink zlk OK, strategies verified.
- n 9: box25/laps/lap_n9_s1_32427.pg (sha1 9e8262cafb96…), 1 lap, Oink zlk OK, strategies verified.
- n 4-5: no lap in 380,899 random o-cyclic games (lapsearch.py, seed 2; not exhaustive).
- fts_best16 (lapsearch.py): 4 laps in the run, at most 8 θ-changes in one phase.
How σ̄(o) changes inside a phase (sbclass.py; a → a'):

| sample | DOWN (a' on a's new σ-path) | INR (a now routes through o) | OTHER |
| --- | --- | --- | --- |
| fts_best16 | 0 | 4 | 4 |
| theta_thf16 (L-RED) | 0 | 4 | 6 |
| theta_thc24 (L-RED) | 0 | 0 | 9 |
| 20,000 random o-cyclic, n 5-14 | 32 | 84 | 129 |

So the "ring walk" is mostly not a downstream move along one path. INR is box 22 §4's "the argmin exit ELIMINATES itself by entering
R"; the classification only adds counts.
- Ring check (ringcheck.py): at throttled states, consider the non-minimal exits that Even's best reply to τ routes through o. On
  random games 159 of 1,620 lie on o's honest continuation; on fts_best16, 10 of 72. Rings exist, but most self-throttling sits
  off the ring.

## 5. The exact obstruction: trust routing (= box 22's "trust mode"; READING with DATA; every step is PROVED in box 21 §3.5-§3.6, box 22 §1, or above)
Attribution: box 21 §3.6 (ii) found trust mode; box 22 §1.3-§1.4 showed that invariants I3 and I4 die on it; box 22 §4 gave θ's two
ways up. This section consolidates them, adds the W-drop link (Case A) and the parametric reading (6), and states (TRUST) with data.
Fix a τ-stretch (τ(o) = b; by Theorem B it is a prefix of the F_b run) and a joint λ-phase in which (h) holds.
1. Gate = honest. Under (h), Lemma G: for v ∉ R, Ξ(v) = W(v). For v ∈ R, Ξ(v) = π_v ⊕ θ and W(v) = π_v ⊕ w. The gate is the improving set of
   the one-player game G^θ (o a terminal of value θ); the selection is the optimum of G^w over the gate.
2. θ moves only through o-free progress. In-phase, θ = o ⊕ min over exits e ∉ R of Ξ(e), and Ξ(e) is the value of e's o-free route.
   An exit in R would close a cycle through o; that is a λ-change, bounded by Lemma Φ.
3. Where R17's induction breaks on o-free paths. Take R17's Lemma P in G^w: "W_k(x) ⪰ value(r) for every o-free simple path r of
   ≤ k edges from x" (r ends on a cycle of the phase's start strategy).
   - Case A needs W non-decreasing. This holds at arena steps (Lemma W) and fails at some fallbacks (§3).
   - Case B goes through at every edge (x, z) of r with z ∉ R. If σ(x) ∉ R, then Ξ = W at both ends. If σ(x) ∈ R, then
     W(z) ▷ π_x ⊕ w ⊵ π_x ⊕ θ = Ξ(σ(x)), with Ξ(z) = W(z). Either way a G^w-improving edge to z ∉ R is in the gate.
   - Case B fails exactly at a WITHHELD edge (x, z), z ∈ R (Lemma G (d1)): π_z ⊕ θ ⊴ W(σ(x)) ◁ π_z ⊕ w.
   - Box 21 §3.6 (i): the repair needs z's HONEST value to dominate the o-free suffix, π_z ⊕ θ ⪰ value(r[z..]). It fails exactly
     when z is TRUST-ROUTED: z ∈ R, and π_z ⊕ θ ◁ value(r[z..]), while the selection keeps z on o because π_z ⊕ w is at least as
     good. Then z's o-free edge is honest-improving (type d2, in the gate) but refused, and every vertex whose o-free route passes z
     is blocked at z.
   - Exits are such vertices. By (2), θ rises only through exits' o-free progress, so trust routings throttle θ itself.
4. Trust routings end in three ways only:
   - (i) θ rises to π_z ⊕ θ ⊵ value(r[z..]);
   - (ii) z's o-free route value rises above π_z ⊕ w, so W agrees;
   - (iii) the arena stalls and the fallback forces z out, lowering W(z): §3, under (h) (fbh_drop9) and off it.
   (i) needs θ-progress, which (3) may block: that is the self-throttling deadlock of box 24 §2. (ii) needs o-free progress
   downstream of z. (iii) needs a global stall.
5. Why each induction tried so far fails at exactly this point:
   - per-path invariants (box 22 §1): I3 and I4 die on trust mode; I1 dies on an exit through the entrant; I2 is ill-posed (its
     o-path runs through o's honest continuation);
   - the G^w induction (box 21 §3.6 (i)): withheld entering edges, whose release is (i);
   - the G^θ induction (§3.6 (ii)): trust-routed z;
   - the joint induction (§3.6 (iii)): the throttle propagates along routes, a chain of trust-routed vertices;
   - completion counting (box 24 §2; box25/complete.py): fts_best16 completes 0 vertices in 23 consecutive transitions (states
     2-25), then 11 at state 26;
   - W-monotonicity counting (this box, §3): resets.
   - Z-reduction plus one-player A (§2): A can run while θ ◁ w.
6. Parametric picture (READING; it shows where the trouble is NOT). Within a phase, compare G^t (o a terminal of value t) for two
   values of t. For a vertex v off o's honest continuation, the comparison of two through-o routes π ⊕ t, π' ⊕ t does not depend on t:
   the same cycle node, and path sets that differ only on π Δ π'. So v's optimal choice in G^t flips from o-free to through-o at
   most once as t rises.
   - If N5's selection used G^θ, the honest optimum, the phase would be R17-like (Lemma PT with gate = G^θ's improving set).
   - The whole excess therefore comes from the selection evaluating o at w instead of θ: that is the set of trust-routed vertices.
   - Vertices ON o's continuation, the ring, cannot route through o without closing a cycle. They are the minority (§4 ring
     check).

## 6. Open statements for a successor or for L-RED
- (TRUST) In an F_b run on o-cyclic 𝒞^1O, the number of transitions inside one joint λ-phase at which some vertex becomes
  trust-routed (§5 (3)) is poly(n).
  - (TRUST) plus a per-stretch R17 bound with no trust events, (SEG-1O) of box 21 §3.6, would bound F_b runs, and with Theorem B
    (C_τ ≤ d − 1) N5 on 𝒞^1O. READING; neither half is proved.
  - DATA (box25/trustcount.py). It counts trust EVENTS = (state, vertex) pairs where a vertex enters
    T_k = {z ∈ R_k : some honest-improving edge (z, y), y ∉ R_k}. That is an upper bound on the number of transitions with a trust
    event, and it can exceed the phase length, since several vertices can enter T at once:
    - max per (τ, joint-λ)-phase: fts_best16 4 (phase of 27 states); theta_thf16 2; theta_thc24 0 (its θ-changes need no d2
      trust event); the n 16 wdropclimb best 12 (phase of 13 states, all fallbacks);
    - 15,000 random o-cyclic canonical runs, n 5-16: max 3-6 per n, no growth visible.
    - Trust events stay below n everywhere, and (TRUST) is not refuted.
- (FB-H) is FALSE at throttled states (fbh_drop9, §3). PROVED at unthrottled states.
- (FB-1O) The number of fallbacks in one joint λ-phase of an F_b run is poly(n). Off (h) each fallback can reset W (§3). DATA: §7.
- (CYC) of box 24 §4 (θ-changes inside throttled stretches) is implied by (TRUST) via §5 (2)-(4). READING.
- A-stretches (§2): with Z frozen, prove that only-A stretches are ≤ |A|, or find one longer.
Smallest instances, in one place:

| phenomenon | smallest known | file (sha1) |
| --- | --- | --- |
| Lemma 2 fails (θ ◁ w survives a pure step) | n 4 | box22/instances/cyc4.pg (bff7a8c2c4ae…) |
| σ̄-lap in one (τ, λ)-phase | n 6 | box25/laps/lap_n6_s1_110421.pg (4f4fe69c51e1…) |
| W drops at a fallback (first refutation: box 22 i1h_fts_best16, n 11, canonical) | — | box22/instances/i1h_fts_best16.pg (3a54502c70ed…) |
| W drops at a fallback, random start | n 4 | box25/wdrop_cyc.pg + .start (d2684b7b752d…) |
| W drops at a fallback, canonical start | n 8 | box25/wdrop_canon.pg (a5007dfe1ac7…) |
| W drops at a fallback under (h) (throttled; box 22's n 11 already has two) | n 9 | box25/fbh_drop9.pg + .start (f25c999053aa…) |
| θ ◁ w while only the above part moves | n 13 | box25/zfrozen_thr.pg + .start (93c6030c54d5…) |
| pure block in one λ-phase > n − 1 (beats R17 per phase) | n 16 (none at n ≤ 15 in climbs) | box21/instances/fts_best16.pg (5534245f603f…) |

## 7. Climbs (DATA; canonical starts; every best checked with Oink)
- wdropclimb.py (fitness: W-dropping Even fallbacks inside one (τ, joint-λ)-phase, then the total; canonical start; o-cyclic 𝒞^1O
  only), 2,400 s per seed, from 05:09Z. INTERIM numbers at 05:23Z; final numbers below if they change.

  | n | seed | W-drop fallbacks in one phase (total) | iterations (fallbacks) | phases | instance (sha1) |
  | --- | --- | --- | --- | --- | --- |
  | 12 | 1 | 7 (7) | 8 (7) | [7, 1] | box25/instances/wd12_s1.pg (500a10efd59a…) |
  | 16 | 2 | 12 (14) | 19 (14) | [1, 1, 2, 1, 13, 1] | box25/instances/wd16_s2.pg (b71ddf0f130e…) |

  - Both: Oink zlk OK, strategies verified. Every drop is at a non-(h) state: τ(o) closes a cycle at o, so w is a cycle value.
  - Mechanism (thtrace.py on wd16_s2): each fallback peels ONE trust vertex out of R. The trust set has one element at each of
    states 5-18.
  - The long phase has 13 states, below n − 1 = 15, so the per-phase bound of R17 is NOT beaten. This is a reset chain of length
    < n, not a kill.
- cycclimb.py (box 24's fitness: longest pure run inside one joint λ-phase − (n − 1)) at n 15, seeds 1 and 2, stopped by me after
  ~12 min each (best reached at 123 s and 94 s, flat afterwards): best −4 and −6. With box 24's n 8-14 finals, no o-cyclic instance
  with n ≤ 15 beats R17's per-phase bound in any climb. fts_best16 (n 16) stays the smallest known.
- fbhclimb.py (fitness: W-drops at (h)-throttled fallbacks; random start in the genome): n 9 seed 1 hit after 21 s (fbh_drop9,
  §3); the n 12 run was stopped after that hit.

## 8. Files (experiments/new/box25/)
- common.py: helpers (rank-free valuations, one-player optimum, random 𝒞^1O generator).
- lemma1cyc.py (§1), propz.py (§2), abovestretch.py / abovebig.py / abovefind.py (§2), complete.py (§5 (5)), thtrace.py (per-state
  θ, w, R, trust set), lapsearch.py (§4), sbclass.py (§4), ringcheck.py (§4), wmono_cyc.py / wdrop_find.py / wdrop_canon.py /
  wdrop_h.py / fbh.py / fbhclimb.py (§3), trustcount.py (§6), wdropclimb.py (§7).
- Instances: laps/lap_n6_s1_110421.pg, laps/lap_n9_s1_32427.pg, wdrop_cyc.pg + .start, wdrop_canon.pg, fbh_thr.pg + .start,
  fbh_drop9.pg + .start, zfrozen_thr.pg + .start, and the §7 climb bests under instances/.
- Reproduce (from experiments/new/box25): `python3 lemma1cyc.py --random 3000 4 14 25`, `python3 propz.py --random 4000 4 16 31`,
  `python3 wmono_cyc.py 6000 5 16 62 --randstart`, `python3 lapsearch.py laps/lap_n6_s1_110421.pg`; check instances with
  `cd .. && python3 n5.py n5 box25/<file>.pg out/x.sol [--start ...] && python3 check_sol2.py box25/<file>.pg out/x.sol 60`.
