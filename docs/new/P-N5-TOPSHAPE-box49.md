# Packet P-N5-TOPSHAPE (box 49): inside one phase, the top of a vertex's path set only falls while it is odd and only rises to even ranks, so it changes at most n − 1 times per vertex per phase (Lemma TOP-SHAPE) — every game
L-NEW successor 30 (Opus 5.5), D14 / D18, Lead reading L40. Lead's wake-up of 04:57Z (message to L-NEW): "TARGET, a CONJECTURE to prove: TOP-MONO
… or more generally the sequence of P-changes is lexicographically monotone in a way that bounds "top changes" by n." Written 2026-10-29 from
05:10Z (date -u). FROZEN at push: later text goes into a fixes file.
What this is and is not, plainly:
- It bounds the changes of top(P(Ξ_t v)), the highest-ranked vertex of v's path set, by n − 1 per vertex per phase, on every game.
- It does NOT bound the P-changes under a fixed top (the "counting" changes). Those reach 71 per vertex in one phase in data
  (l121reader_n41, n 41).
- The Lead's literal TOP-MONO (the top rank of P_t Δ P_{t+1} non-increasing along the P-changes) is FALSE (§3).
- Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
Labels: PROVED (L-NEW 30, unrefereed) / DATA / DEAD.
Source: docs/new/N5-READER-box49.md §12 (working note). This packet governs.
Tool: experiments/new/box49/topmono.py (counters VIOL_rise_to_odd, VIOL_even_top_fell, VIOL_not_even_after_even; must be 0); outputs
experiments/new/box49/out/topmono_*.txt.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Fact DELTA (the set order is decided by the top of the symmetric difference) | PROVED (to sign; elementary) |
| §1 | Lemma TOP-SHAPE (a), (b), (c) and its Corollary (≤ n − 1 top changes per vertex per phase) | PROVED (to sign) |
| §2 | data | DATA (not to sign) |
| §3 | TOP-MONO in the Δ form | DEAD (not to sign; an instance) |
- Premises (LANDED):
  - SPEC docs/new/N5-ssi-global.md S1's valuation and order: [Q docs/new/N5-ssi-global.md@e2da18b0:30-31] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u))»
  - (MON), as P-N5-HONFF lists it: [Q docs/new/P-N5-HONFF-box47.md@e2da18b0:26] «(MON): RESULTS R15 (a) with R15 (d) (Ξ non-decreasing along a run, S4c fallbacks included»
  - Phases (RESULTS R38 (a)): λ_Ξ is constant on a phase by definition (P-N5-OFFMONO-fixes F1).
  - (INJ) (RESULTS R56 (a)): distinct path sets have distinct signed weights (powers of 2 at distinct ranks).

## 0. Setting
A phase P of N5; v a vertex; c := λ(v), constant on P. For a state t of P, P_t := P(Ξ_t v) ⊆ {u : rank(u) > rank(c)}, and
top_t := the largest rank in P_t, or ⊥ (below every rank) if P_t = ∅. A rank r is EVEN or ODD as the priority Ω of the vertex of rank r. For
sets A ≠ B, d(A, B) := the largest rank in A Δ B.

## 1. Fact DELTA and Lemma TOP-SHAPE (PROVED, every game)
Fact DELTA. For path sets A ≠ B of one class, weight(B) > weight(A) iff d := d(A, B) is even and d ∈ B ∖ A, or d is odd and d ∈ A ∖ B.
Proof. weight(B) − weight(A) = Σ_{r ∈ B∖A} s(r)2^r − Σ_{r ∈ A∖B} s(r)2^r, s(r) = +1 for even r and −1 for odd r. All ranks are distinct, so the
term at d dominates the sum of the others (Σ_{r<d} 2^r < 2^d). Its sign is s(d) if d ∈ B ∖ A and −s(d) if d ∈ A ∖ B. □
Lemma TOP-SHAPE. Let t → t + 1 be a transition of P with P_t ≠ P_{t+1}. Then:
- (a) if top_{t+1} > top_t, then top_{t+1} is even;
- (b) if top_t is even, then top_{t+1} ≥ top_t;
- (c) hence, along P: once top is even it stays even and never falls; before that, top is odd or ⊥, and an odd top only falls or stays
  until it is replaced (by a lower odd rank, by ⊥, or by a lower or higher even rank).
Proof. (MON) gives Ξ_{t+1}(v) ⊵ Ξ_t(v). The cycle node c is the same at both states (λ constant on the phase), so its reward is the same, and
S1's order compares the path sets next: weight(P_{t+1}) ≥ weight(P_t), and strictly, since P_{t+1} ≠ P_t (INJ). Let d := d(P_t, P_{t+1}).
- (a) If u′ := top_{t+1} > top_t, then u′ ∉ P_t, and no rank above u′ is in either set; so d = u′ ∈ P_{t+1} ∖ P_t. Fact DELTA with the strict
  rise forces d even.
- (b) If u := top_t is even and top_{t+1} < u, then u ∈ P_t ∖ P_{t+1} and no rank above u is in either set; so d = u ∈ P_t ∖ P_{t+1}. By Fact
  DELTA the weight would fall, since d is even and lies in the old set. That contradicts the strict rise.
- (c) From an even top, by (b) the next top is ≥ it, and by (a) any rise lands on an even rank; so tops stay even and non-decreasing, and
  P never empties again (⊥ is below every rank). From ⊥, a change makes top_{t+1} > ⊥, which is even by (a). From an odd top, a rise lands
  on an even rank by (a); otherwise the top stays or falls. □
Corollary (top changes). For every vertex v and phase P, top(P_t) changes at most n − 1 times on P.
Proof. By (c) the sequence of distinct top values is a strictly decreasing run of odd ranks, then possibly ⊥, then a strictly increasing run of
even ranks. The run of odd ranks has no ⊥ inside it, since from ⊥ the next top is even. So each rank above rank(c) occurs at most once, and ⊥
at most once. There are at most n − 1 ranks above rank(c) (c itself is not one), so there are at most n distinct values and at most n − 1
changes. □
- Reader-proofness (READING): the bound holds for every vertex of every game, so readers (docs/new/N5-READER-box49.md §1) cannot raise a
  vertex's top changes above n − 1. What they raise is the P-changes under a fixed top.

## 2. DATA (not to sign; experiments/new/box49/topmono.py)
| set | runs | P-changes | VIOL (rise to odd / even top fell / odd after even) | max top rises per (v, P) |
| --- | --- | --- | --- | --- |
| lib41, n ≤ 48, own start or S3 + 2 random, seed 7 (out/topmono_lib41.txt) | 1,047 | 59,663 | 0 / 0 / 0 | 3 (n5-exhaustive b5_os_n28, vertex 10: tops 10, 11, 22, 27, three rises, each to an even rank) |
| L-RED instances, n ≤ 200, own start or S3 (out/topmono_red.txt) | 311 | 27,587 | 0 / 0 / 0 | 48 (red/ul ladderd0_k48_n156, vertex 50: ⊥, 107, 108, …: an increasing even run) |
| long121, qpcclimb scale, pl130_n40, si/root/instances (out/topmono_long.txt) | 13 | 11,177 | 0 / 0 / 0 | 2 (cone_n69: ⊥, 67, 68) |
- The Lead's DATA sentence ("the top … moves monotonically down") is the odd run of (c). A gate example from lib41 (box25/instances/sc32,
  vertex 0, phase [4, 48]): tops 31, 30, 29, 27, 26, 21, 20 (all odd ranks), then ⊥, then 25, 28 (even ranks).
- The P-changes under a fixed top are not bounded here: up to 71 P-changes of one vertex in one phase (l121reader_n41), against ≤ n − 1 top
  changes.

## 3. DEAD: TOP-MONO in its Δ form
- Statement (Lead, 04:57Z): "the top rank of the symmetric difference between successive path sets P(Ξ_t(v)) at its P-changes is monotone".
- Instance: experiments/new/box48/instances/long121_n40 at its .start, phase [1, 122], vertex 0. The Δ-tops at its P-changes begin
  35, 37, 32, 33, 26, 39, 21, 29, 33, 36, …, with 20 rises in the phase. Max over the data: 47 rises for one vertex in one phase (ladderd0_k48_n156).
- Obstruction: the Δ-top is the carry position of a counter. A path set under a fixed top behaves like a binary counter below it (Fact DELTA:
  a rise flips the highest differing rank), and a counter's carry positions go up and down. Only the top of P itself is monotone in the sense
  of (c).

## 4. Quotes and pins
`python3 -I experiments/new/box49/quotecheck3.py docs/new/P-N5-TOPSHAPE-box49.md` prints QUOTES PASS (pinned in experiments/new/check.sh with a
shifted-line control and this file's sha1). topmono.py: sha1 in the push message.
