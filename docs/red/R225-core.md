# R225 item 2 (D18 own item): the open core Σ_v D^tot_E(v) of N5′-xi on Γ3(G) (L-RED successor 59, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Lead GO 08:46Z: «Start item 2 now; state (a) or (b) and why in your first report, with a first measurable step.»
Labels: PROVED (lane, unrefereed) / PROVED-COND (named premise) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) /
READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
Tools: experiments/red/r225/ (sig225.py = Σ_v D^tot_E on IDEAL-CYC via R221's independent own.py; bin225.py; lad2json.py; climb225.py).

## 0. Answers so far (first report, 08:5xZ)
- CHOICE: (a), build. Reasons, in order:
  1. Lemma EQUIV (§1, PROVED-COND on box 196's premises): Σ_v (D^tot_E(v) − 1) and T3 are polynomially equivalent on HOW3. So (b) is not
     a weaker target than G-N5-TIME on Γ3: it IS polynomiality of N5′-xi on Γ3 (under [E-LEV]), and (a) IS an exponential N5′-xi run.
     CHAIN3's «residue» is a restatement, not a reduction.
  2. Lemma BIN (§2, PROVED, lane): the abstract chain system CS(M) of P-N5-ASC §2 has, for EVERY M, a run whose hub takes 2^M − 1 values
     (M − 1 ascents). So no proof of (b) can live in CS(M) (E-MON + CHAIN-DECOMP + cycle-node counting). It must use Howard's switching
     rule, i.e. the full dynamics. REFEREE-2's N-3 (2^M at B = 2, M ≤ 6) showed this as DATA for small M only.
  3. Every route to (b) I can see needs exactly what L-SI's DEAD towers expose (ACCESS-LATCH, LEAPFROG, POOL-ALT) turned into a global
     potential, and none is in hand. A build is decided by one instance; a proof is not in sight.
- The tower route does not transfer (§3, DATA): HIT7 (L-COMP 11 / L-LOWER, F(6) = 254, 299 IDEAL steps) runs 8 Howard steps on IDEAL-CYC
  with Σ_v (D^tot_E − 1) = 0, although U(G) = 43. This agrees with L-SI 43's ACYC-LIN (N5′-xi has R = 0 on Ξ-acyclic genomes).
  So for N5′-xi a counter needs Ξ-cycles; unbounded U(G) alone buys nothing (HIT7 here; SL(k) of R221 §2).
- First measurable step (§4): climbs with score T (≡ Σ D by EQUIV) on Ξ-cyclic genomes, N 12 / 15. Running; first values T 17 (N 12) and
  T 16 (N 15), both with at most 2 ascents per play.

## 1. Lemma EQUIV (Σ D^tot_E ≍ T3)
Setting: box 196 (claude/l-new 08801298, docs/new/N5-CHAIN-box196.md). HOW3(G) is the Howard run of N5′-xi on Γ3(G) from S3, up to its
first fallback, with T3 steps (REACH3-ALL). n3 = N + 7M + 10. D^tot_E(v) is the number of distinct classes (Λ_t(v), E_t(v)) over the
run (P-N5-QUIET l. 121).
**Lemma EQUIV.** Σ_v (D^tot_E(v) − 1) ≤ n3·T3, and T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1).
- Left: the run has T3 + 1 states, so v has at most T3 + 1 classes, D^tot_E(v) − 1 ≤ T3. Sum over the n3 vertices. No premise. ∎
- Right: box 196's Corollary T-QUIET3, verbatim (PROVED, lane, on box 196's premises: P-N5-END, P-N5-ASC (R121), P-N5-QUIET not all
  landed, as box 196 §6 lists them).
- Consequence: T3 is super-polynomial iff Σ_v (D^tot_E(v) − 1) is, since L3 and n3 are polynomial in N + M. So the target of item 2 (a)
  is an exponential N5′-xi run on Γ3, and (b) is G-N5-TIME restricted to Γ3 (under [E-LEV] if (b) goes through CHAIN3).
- DATA (unit: genome = one IDEAL-CYC Howard run by own.py; counter: sig225.py; set: the frozen instances named):

  | genome | N | n | U(G) | T | Σ(D−1) | max D | Σ(D−1)/T |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | LEAP_k8 (R217) | 37 | 244 | 17 | 17 | 212 | 18 | 12.5 |
  | LEAP_k16 (R217) | 69 | 468 | 33 | 33 | 420 | 34 | 12.7 |
  | CL2_21 (L-SI box 85) | 108 | 732 | 59 | 23 | 169 | 9 | 7.3 |
  | TC4m (L-SI box 85) | 258 | 1737 | 136 | 37 | 1432 | 11 | 38.7 |

  T here equals the clean-run T3 that box 196's own engine gives on Γ3 for CL2_21 (23) and TC4m (37) (R224-chain.md §5): two routes agree.

## 2. Lemma BIN (CS(M) admits 2^M − 1 hub values)
**Lemma BIN (PROVED, lane).** In CS(M) (items 1..M by rank; P-N5-ASC §2), let S_t := {i : bit i − 1 of t is 1} for t = 1..2^M − 1,
next_t(x) := min{y ∈ S_t : y > x} (⊥ if none), h_t := min S_t. Then (next_t) is a run, (h_t) is a hub, the hub's value is S_t, and it takes
2^M − 1 distinct values, with |S_t| − 1 ≤ M − 1 ascents.
- Forest: next_t(x) > x, so there are no cycles.
- chain_t(x) = {x} ∪ (S_t ∩ (x, M]). Read as a binary word with the most relevant item most significant, this is 2^(x−1) + (the bits of t
  above position x − 1), and those bits form a non-decreasing number in t. Lex order on these sets is numeric order of the words
  (R221 §5 NO-REFLECT's proof). So every chain is lex non-decreasing.
- chain_t(h_t) = S_t, strictly increasing numerically in t. ∎
- Machine check: bin225.py M ≤ 10: 2^M − 1 values, 0 violations.
- Reading: P-N5-ASC's HUB-ASC(B) is the right kind of bound (it needs the ascent count), and F_B's squaring is not an artefact. Any
  polynomial bound in n alone must come from the game's dynamics (Howard switching against an optimal Odd), not from the chain
  structure. In the game, BIN's forest is the «route to the next set bit» forest, which is exactly the shape L-SI's towers try to drive.

## 3. HIT7 under N5′-xi (DATA)
- Instance: claude/l-lower experiments/lower/l8/rec/LCOMP_L6_HIT7_F254_d28.txt, sha1 6a3b274d3af4d0d8f057f82c8f2919c84b7dd446 (frozen copy
  experiments/red/r225/inst/HIT7_d28.txt, same sha1). Converted by lad2json.py, with sim6.okeys's W-convention: option k of a level-l
  mover goes to mover 2(l − 1) + k.
- Unit: one IDEAL-CYC Howard run (own.py, [E-LEV]). Counter: sig225.py. N 56, M 112, n 398, U(G) 43, T 8, Σ(D−1) 0, max ascents 0
  (out/hit7_sig.txt).
- Scope note: HIT7's 299 steps are R104 IDEAL steps (least-key choice among improving options; N5 with the S4a root-first-key tie). The
  Howard choice is the Ξσ-best option. Ξ-acyclic, so ACYC-LIN applies (NOW.md M4 row). No conflict; this records the gap between the two
  candidates on the fleet's best tower.
- Caveat: the W-convention is read from sim6.okeys, not stated in a frozen spec. It does not matter here: with Σ(D−1) = 0 no e-vertex
  ever enters a Π, so W-targets do not affect the values.

## 4. First measurable step: T-climbs on Ξ-cyclic genomes (DATA, running)
- climb225.py: R221 ladclimb's mutations (Ξ-targets anywhere, self-loops included, so Ξ-cycles and SET options allowed); score (T, Σ(D−1)).
  Seeds: random genomes, levels × width × degree 4 × 3 × 2 (N 12, seed 2251) and 5 × 3 × 2 (N 15, seed 2252).
- Values at 08:5xZ (unit: best genome so far; scope own.py IDEAL-CYC, cap 3000 steps): N 12: T 17, Σ(D−1) 1004, max D 16, U 9, max
  ascents 1. N 15: T 16, Σ(D−1) 1222, U 9, max ascents 2.
- For comparison (R221 §3, other scores): R63K5 N 18 T 28; L-SI box 86 climbs CB3_61 / CB3_62.
- FINAL (09:0xZ; out/c12_2251.*, c15_2252.*, c18_2253.*): N 12: T 18, Σ(D−1) 1073, U 8, max ascents 2 (4000 iterations); N 15:
  T 19, Σ(D−1) 1258, U 9, max ascents 2 (3000); N 18: T 20, Σ(D−1) 1912, U 12, max ascents 3 (STOPPED at iteration ~2460 to free CPU for
  item 1). Best T grows by about 1 per 3 movers here: no sign of super-linear growth (DATA, weak: three climbs, one seed each).
- Next: (i) more seeds / N and fit best T against N (12 / 15 / 18); (ii) a designed family on BIN's forest («route to the next set
  bit», bits = SET options forcing Odd onto e) whose bit reset avoids L-SI's ACCESS-LATCH. A reset must come from an overtaking copy
  route (LEAPFROG), so the design question is POOL-ALT's pool-size cap.

## 5. Composition test: does a hub's height MULTIPLY or ADD its segments' heights? (Lead 09:31Z: «name exactly what add means»)
Definitions (comp225.py; IDEAL-CYC Howard by own.py, [E-LEV]). Fix a vertex v and a maximal interval I with Λ_t(v) constant.
- seq_t(v) = (c_1, …, c_p). a := the first ascent index (c_(a+1) more relevant than c_a), else a := p.
- Low_t := {c_1, …, c_a}; High_t := {c_(a+1), …, c_p}. These are SKELETON's R(s) / chain(y) split at the first ascent (P-N5-ASC §4).
- D := #distinct seq-sets on I, Hn := #distinct High_t, Ln := #distinct Low_t.
- X := D − (Hn + Ln − 1), the ADDITIVE EXCESS. RES := #steps inside I with Low_t <lex Low_(t−1) (low resets).
- Facts: D ≤ Hn·Ln always. X ≤ 0 unless Low or High returns to an EARLIER value after leaving it: if neither repeats non-consecutively,
  every new pair brings a new Low or a new High.
**CONJECTURE ADD(c) (the precise form asked for).** There is an absolute constant c such that X ≤ c for every genome, every v and
every Λ-interval I.
- What it would buy: inside HUB-ASC's proof (P-N5-ASC §4) it would replace the product F_(B−1)(M)·F_(B−1)(M) by a sum.
- What it would NOT buy by itself: the level factor (M² + M + 1) and the sum over entry nodes y still multiply at each ascent, so
  F_B ≤ (M² + M + 1)(1 + 2M·F_(B−1) + c) is still exponential in B.
- A polynomial bound in n alone would need ADD plus a global count (each chain(y) charged once across hubs). That is NOT claimed.
DATA (unit: (genome, v, I); scope own.py; counter comp225; max X over the set):
| set | max X | at (D, Hn, Ln) | max D per I | max RES |
| --- | --- | --- | --- | --- |
| LEAP_k4 / LEAP_k8 (R217) | 1 / 1 | (6, 2, 4) / (10, 2, 8) | 10 / 18 | 4 / 8 |
| T-climb bests c12 / c15 / c18 (§4) | 0 | — | 3 | 1 |
| L-SI box 86 LT3_1_0, CB3_61; box 85 TC3m | 0 | — | 6 / 7 / 8 | 1 / 1 / 2 |
| X-climb from LEAP_k4 (SCORE=X, 2500 iterations, seed 2261) → frozen inst/CX4_n21.json (sha1 ef29debbc3f8e0ed2fa43aac2e0814c74849ec2e) | 4 | (11, 6, 2) | 11 | 5 |
| X-climb random 4 × 3 × 3 (seed 2262; stopped at ~2400 of 4000 to keep ≤ 2 jobs) | 1 | (13, 3, 10) | 13 | 3 |
So ADD(c) needs c ≥ 4. Whether X grows with N decides between ADD(c) and DEAD; the climbs in §6 test that.
- Mechanism of CX4_n21 (READING from the play trace, out/cx4_show.txt):
  - The hub e15.0 has D = 11 = T + 1. Its Low part is {e15} or {e15, e10}, alternating at EVERY step. Its High part takes 6 values, each
    held for 2 steps.
  - The level-0 router x0 races two routes into the same High chain: via x9 (β) and via x10, whose gate gives e10 (Odd takes e).
  - The x10 route carries the bonus e10 but sees each High improvement one step later. So every High value gives two hub values,
    without e10 and then with e10: a factor-2 multiplication per High value.
  - It needs the High source to change at most once per 2 steps. Here x17, the W-target of e10, changes only at the odd steps 1, 3, 5, 7, 9.
  - No play from the High part returns to the router (no feedback), and the depth is 1.
- READING (the obstacle to iterating): a race with r staggered routes multiplies by r only if the High part holds each value for r
  steps. At the next level up the same race needs a High that is r² times slower. In feed-forward (Ξ-acyclic on the hub's plays)
  Howard all levels move at once, so a slow High must come from a long delay path, i.e. size linear in the product. Feedback through
  Ξ-cycles (a carry from the low race back into the High chain) is the only other source of slowness. This agrees with ACYC-LIN.

## 6. Does X grow with N? (DATA, weak; 09:4xZ)
| climb (SCORE=X) | seed genome | N | iterations | final X | (D, Hn, Ln) | max D per I |
| --- | --- | --- | --- | --- | --- | --- |
| cx_cx4_2263 | CX4_n21 | 21 | 4000 | 4 (no strict gain) | (11, 6, 2) | 11 |
| cx_leap8_2264 | LEAP_k8 (R217) | 37 | 1500 | 1 (no strict gain) | (10, 2, 8) | 18 |
- No growth of X was found beyond 4. Weak: two climbs, one seed each, and the mutations rewire single options only.
- What would kill ADD(c), by the READING of §5 (not built): a race router with r staggered routes in front of a High source that holds each
  of its K values for r steps. Then X = (r − 1)(K − 1), and T ≥ rK stays polynomial, so killing ADD(c) would not refute (b).
- The question that matters for (a) is nesting: whether a High that is slow BECAUSE it is itself a race output can be built (depth 2).
  CX4_n21 has depth 1: its slow High (x17 at odd steps) is not a race output.
- STATUS: CONJECTURE ADD(c), c ≥ 4 by CX4_n21. Open whether c is constant. A depth-2 race is the next build.
