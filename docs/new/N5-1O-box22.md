# (FO_1O) on one-Odd-choice games: box 22, four inductions and where each one stops
L-NEW successor 8 (Opus 5.5, D15). Lead GO 2026-10-24 01:47Z; started 01:46Z; this file 01:54Z (date -u).
Status: proof attempt on (SEG-1O) and (CH-1O) (docs/new/N5-time-box21.md §3.5-§3.6). Labels: PROVED, READING, OPEN, DATA.
Not refereed. No polynomial bound is claimed. G-N5-TIME stays OPEN.
Result in one line: four natural inductive invariants for (SEG-1O) are FALSE, each on a small instance, and all but one fail
through the same mechanism. Following the Lead's stop rule (a fourth induction blocked by the trust-mode deadlock), the proof
attempt stops here. Separately, box 21's open statement (WF) is FALSE.

## 0. Setting (from N5-time-box21.md §3.5)
- 𝒞^1O: o is the only Odd vertex with a choice. τ is fixed inside a stretch.
- θ = Ξ(o) (honest) and w = W(o) (play value against τ).
- R = the set of vertices whose σ-path reaches o.
- A stretch is a maximal run of iterations with θ, w, τ and the joint λ-map constant.
- Checks here restrict to stretches that satisfy Lemma G's (h) at every state, with a single sink (one cycle node s for all of Ξ
  and W) and no S4c fallback inside the stretch. That is the cleanest setting in which (SEG-1O) could be proved.
- Lemma G (PROVED there): the honest gate equals G_τ's improving set except on edges entering R. Those are withheld while
  π_z ⊕ θ ⊴ W(σ(x)). Edges leaving R are admitted more easily.
- An inductive invariant, as in R17's Lemma P, has the form "after j steps of a stretch, every vertex is at least as good as
  every simple path of ≤ j edges", for some value measure and some class of paths. With such an invariant, Theorem PH's
  counting gives ≤ n − 1 value-changing steps (READING; for I4 the count is spelled out in §2).

## 1. The four invariants and the smallest counterexamples found
Each counterexample is a canonical N5 run (best-reward start) unless a start file is named. Each is Oink zlk OK with strategies
verified (check_sol2.py), and n5b.py (L-COMP, --mode spec) gives the same iteration and fallback counts.
Files are in experiments/new/box22/instances/; checkers are shrinkP.py (predicate violation()) and stretchP.py.

| invariant | measure / paths | status | smallest instance | n | mechanism |
| --- | --- | --- | --- | --- | --- |
| I1 | W (G_τ); all paths of G_τ, through o by τ(o) | FALSE | i1hn_fts_best16.pg (sha1 52d250ff…), from fts_best16 by shrinkP.py, HREQ=1 NOFB=1 | 11 | exit through the entrant (§1.1) |
| I2 | Ξ (o a terminal of value θ); o-free paths, and o-paths valued π ⊕ θ | FALSE, ill-posed as stated | n9_i2.pg (ce4aa630…) | 9 | the o-path runs through o's own honest continuation (§1.2) |
| I3 | Ξ; o-free paths only | FALSE | i3hn.pg (6f9bc08e…) | 9 | trust mode (§1.3) |
| I4 | W; o-free paths, and o-paths avoiding o's honest continuation, valued π ⊕ θ | FALSE | i4_hand.pg + i4_hand.start (d90a7199…), hand-built | 12 | trust-mode deadlock held open by a delay lane (§1.4) |

DATA on the search:
- I1: none on 3,000 random 𝒞^1O games (n 4..9), and none in a short random search at n 7-10 (stopped). The smallest violation
  found is 11, from shrinking climbed instances.
- I4: 0 violations in 300,000 random 𝒞^1O games (n 8, 10, 12; smallsearch.py) and on every climbed instance
  (fts_best16, oneodd_c16, oneodd_c24 and the I1 / I3 minima). It fails only on the hand-built i4_hand. So random games and
  climbs do not find the deadlock configuration; it has to be built.

### 1.1 I1 fails: the punishing exit runs through the vertex that wants to enter (i1hn_fts_best16, n 11)
- o = 4, with exits {1, 6}; τ(o) = 6. Odd's best reply is σ̄(o) = 1, and exit 1's route is 1 → 9 → 6 → 8 (sink 8).
- At stretch step 2 (states 4-6), vertex 9 would gain against τ by entering o: 9 → 4 → 6 → 8 is a 3-edge G_τ path. But the
  honest gate withholds (9, 4). If 9 entered o, Odd's best reply would close the cycle o → 1 → 9 → o, whose top is vertex 1
  (priority 11, odd).
- So the honest gate is right. I1 measures progress in G_τ, where routing through o is always safe, and that is the wrong
  measure.

### 1.2 I2 is ill-posed: o-paths through o's own continuation (n9_i2, n 9)
- At stretch step 2 the path 4 → 1 → o is violated, where 4 = σ̄(o).
- An o-path that passes through o's honest continuation does not have the value π ⊕ θ: following it closes a cycle.
- I4 (b) excludes such paths. With that exclusion the n9_i2 violation disappears.

### 1.3 I3 fails: trust mode (i3hn, n 9)
- o = 1, with exits {0, 3}; τ(o) = 3. σ̄(o) = 0, with route 0 → 4 → 5 (sink 5).
- During the stretch (states 2-5, θ = (5, −264, 3), w = (5, −120, 2)), vertex 2 has (2, 4) in Iσ at every state.
  - The o-free path 2 → 4 → 5 is honestly better than 2's current o-route (Ξ(2) = (5, −200, 4)).
  - N5 never takes (2, 4), because against τ the o-route is better: W(2) = (5, −56, 3).
- The stretch ends when exit 0 eliminates ITSELF from Odd's options by entering R (0 → 6 at state 5, after 6, 8 and 7 moved
  into R). Then θ = w.

### 1.4 I4 fails: the deadlock, built by hand (i4_hand, n 12, start file i4_hand.start)
Vertices (priority) and edges. The sink s (0) is a self-loop. τ(o) = e*, which is honest-optimal (Iτ = ∅, checked) and is S3's
choice.

| vertex | priority | edges |
| --- | --- | --- |
| q | 27 | → s |
| e* | 19 | → s |
| o (Odd) | 1 | → {e*, ℓ1} |
| lane ℓ1..ℓ4 | 3, 5, 7, 9 | ℓi → {q, ℓi+1}; ℓ4 → {q, s} |
| y | 23 | → s |
| z | 2 | → {o, y} |
| b | 25 | → s |
| x | 4 | → {b, z} |

- The start pair puts every ℓi → q, z → o and x → b.
- Odd punishes through ℓ1, so θ = o ⊕ {ℓ1, q}, while w = o ⊕ {e*}. The values are ordered by their top differing vertex:
  θ-route of z ◁ {z, y} ◁ w-route of z, and θ-route of z ⊴ {b} ◁ {z, y}.
- z is in trust mode: (z, y) is in Iσ, but against τ the o-route wins.
- x is withheld: (x, z) improves against τ, but Ξ(z) = π_z ⊕ θ ⊴ Ξ(b).
- The lane closes one vertex per iteration (ℓ4, ℓ3, ℓ2, ℓ1). That keeps θ, w, τ and λ constant for 4 iterations.
- At step 3, W(x) = (s, −1008, 2) lies below the 3-edge o-free path x → z → y → s = (s, −492, 3). I4 (a) is violated.
- Run: 5 iterations, no fallback. The stretch ends when ℓ1 is repaired: θ = w, and x enters.
- The induction step fails exactly here. For the o-free path x → z → y → s, the withheld case would need the honest bound
  Ξ(z) ⪰ value(z → y → s). In trust mode z's honest value is capped by θ. N5 keeps z on o because its selection trusts τ.

READING: what the failures say about (SEG-1O).
- Every counterexample stretch is short:
  - i4_hand's stretch has length 4, equal to its lane, and the lane costs 4 vertices;
  - on climbed 𝒞^1O instances the longest stretch is 11 at n 16-24;
  - random games show no stretch above n − 1.
- So (SEG-1O) is still DATA-consistent. What fails is the R17 template: every one of these invariants is a per-path
  domination statement, and the deadlock defeats per-path domination.
- A proof of (SEG-1O) needs a counting argument instead, for example: each step of a stretch improves some vertex outside the
  deadlocked set, and the deadlocked set only grows inside a stretch. Neither part is proved, and I have no route to either.

## 2. Conditional: what an invariant of I4's shape would give (READING)
If I4 held on every fallback-free stretch with (h), a stretch would have ≤ 2n − 2 W-changing steps:
- After n − 1 steps, every edge entering R is out of the gate. A gated entering edge (x, z) would give π_z ⊕ θ ▷ W(σ(x)), against
  I4 (b) for the simple o-path x → π_z.
- After n − 1 steps, no leaving edge or o-free edge improves against τ (I4 (a)).
- So R is fixed from then on, and the rest is one-player switch-best on routes inside R. Lemma G (c) makes those edges
  unthrottled, and R17's Lemma P / Theorem PH applies, giving ≤ |R| − 1 further steps.
This is recorded only to show the shape a successful invariant needs. I4 itself is false (§1.4).

## 3. (WF) is FALSE: S4c fallbacks strictly LOWER W (PROVED by instance)
Box 21 §2.5 proved that fallback steps satisfy W_{k+1} ⊴ W_k, and left "fallbacks are W-flat" (WF) OPEN on 52/52 random cases.
- Counterexample: instances/i1h_fts_best16.pg (n 11, sha1 3a54502c…, canonical; 8 iterations, 3 fallbacks). In each of the
  three fallback iterations W strictly decreases somewhere:
  - iteration 2 at vertices 1, 2, 5, 9, 10;
  - iteration 5 at vertex 2;
  - iteration 6 at vertex 9.
- Vertex 2 goes 4 → 3 (fallback) → 4 (arena) → 3 (fallback): it RETURNS inside one λ-phase, driven by the fallback's honest
  switch-all against a frozen τ.
- Consequences:
  - W is not monotone along N5 runs once fallbacks occur. Any argument through W must count fallbacks separately.
  - The fallback is a second return mechanism, next to σ̄ lapping (box 21 §3.4).
  - How often S4c can fire in a run is not bounded by anything proved here. R15 bounds flat stretches, and a fallback is not
    flat.

## 4. (CH-1O): what the instances show (READING; not attacked further)
- θ = o ⊕ (minimum honest value over o's exits outside R). It rises in two ways:
  - the argmin exit's o-free value improves;
  - the argmin exit ELIMINATES itself by entering R (i3hn: 0 → 6 at state 5, i4_hand: ℓ1 repaired). Odd then cannot use it
    without closing a cycle through o.
- So #θ-changes ≤ #(value changes of exits while outside R) + #(R-entries of exits). Exits can leave R again, so neither term
  is bounded by anything proved here. This is L-RED's θ-change family target (Lead routing 01:47Z).

## 5. Files (experiments/new/box22/; read-only use of n5.py, si.py, box21/*.py)
- stretchP.py: I1-I3 random search.
- shrinkP.py: violation(G, inv) for I1-I4, with HREQ (Lemma G's (h), single sink) and NOFB (no fallback in the stretch), plus a
  greedy shrinker.
- i1inst.py: I1 on given instances.
- smallsearch.py: random search for small violations.
- showrun.py: per-state dump (σ, θ, w, R, Ξ, W, Iσ).
- instances/: i1_min (n 11; an I1 deadlock with (h) failing: Ξ(o) and W(o) end in different cycles), i1h_fts_best16
  ((WF) counterexample), i1hn_fts_best16, i1hn_oneodd_c24, i3hn, n9_i2, i4_hand(+start).
