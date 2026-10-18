# R44: (NO-PRE-a) is false; do the box-14 kills point to a lower bound? (L-RED box 14; produced on Opus 5.5)
Status: KILL (DATA, both orders, L-ALG's unmodified scanner) plus a READING for the owner's reassessment, unrefereed.
Written 2026-10-18 22:20Z (date -u). Lead requests of 22:10Z (date -u): attack the survivors (VR-NEW_all), (FD-WITNESS_all),
(CHAIN-CHANGE) and (NO-PRE-a), and write one paragraph on super-polynomial potential.

## 1. Status of the four survivors after this box
| statement | status | instance (sha1) | reference |
| --- | --- | --- | --- |
| (VR-NEW_all), class AND general games | FALSE, both orders | vrall_viol_n20 (ed5058576554) | R42 §5; b12_pot K-v-all 1, with and without CLASS |
| (FD-WITNESS_all) | FALSE, both orders (implied by the line above) | vrall_viol_n20 | b12_fdwit: no new-key vertex at j* nor at j* − 1 |
| (CHAIN-CHANGE) on 𝒞^1P | survives (0 of 1,046; climbs) | — | R42 §3, necessary conditions (α), (β), (γ) |
| (NO-PRE-a) | FALSE, both orders | nopre_viol_n20 (9a93a8e24832) | §2 below |

Earlier in this box: (XCTX@p0) FALSE on 𝒞^1P (R42 §1) and (TREE-PIECE⁺) FALSE in two-player games (R43).

## 2. (NO-PRE-a) is FALSE (both order data)
Statement (GAP-A-M §28c, quoted): "a vertex of a tangle that fired at top τ in round r is never a round-r top above τ at the next
visit".
Instance: experiments/red/nopre/instances/nopre_viol_n20.pg, sha1 9a93a8e24832a2440206658fc0f4fdca63cb1574. Two-player, n = 20,
priorities tied (a case-(a) vertex needs pr(y) = pr(τ), GAP-A-M §31a).
- Pinned Oink: 4 iterations (odd 3, even 1), 1 dominion, 9 tangles, solution verified. The model (b12_nopre.run) also makes 4
  iterations, and Zielonka solves the game.
- L-ALG's `b12_nopre.py scan`, unmodified, prints "PRECONDITION".
  - Counts (pre, near, surv, max gap, above): stable (1, 2, 6, 4, 6), oink (1, 1, 5, 4, 5).
  - First example: Odd's phase (1, 0), context of 20 vertices.
- How it was found: L-ALG's own climb, unmodified (`b12_nopre.py climb 20 12 30000 51`, stable), started from L-ALG's near miss
  instances/nopre_near_n20.pg. It was reached within the first few hundred steps. The Oink-order run (seed 52) ended with pre = 5.
  L-ALG's §31 climbs differed only in seed and start file.
- Consequence (reading, from §28c): without (NO-PRE-a), STEAL-ENTRY is not a pure strategy-conflict statement, and the
  "NOSTEAL-1P without distinct priorities" extension has no support. NOSTEAL-1P as signed is untouched, because it assumes distinct
  q-priorities (𝒞^1P) and a case-(a) vertex needs a tie.

## 3. Do these kills point to a super-polynomial family? (reading, for the owner's reassessment)
In my judgement the kills of this box ((XCTX@p0), (VR-NEW_all) / (FD-WITNESS_all), (TREE-PIECE⁺) and (NO-PRE-a)) are
"proof route dead" results. None of them is a step toward a lower bound, and none could grow into one by itself. The reasons:
- They are failures of compression, not of polynomiality. Each killed statement said that a poly-size label (a key, a signature,
  a position) never repeats inside a phase. The counterexamples repeat a label once, in phases of 3-6 searches on n = 20-22
  (pinned Oink: 4-8 iterations). On 𝒞^1P, Lemma LEX (L-ALG §35b, a reading, mechanically checked) still makes the depth-0 chains
  strictly increasing in a tree-lexicographic order, so a phase never repeats a chain. What the kills show is that the chain is
  not determined by poly-size data: the context SET at a position matters, not only its size, signature or first-changed position.
- Counting the sets is exactly (CTX⁺). A super-polynomial phase on 𝒞^1P needs exponentially many distinct chains, which by LEX
  means positions whose context is re-cut with fresh sets again and again. That is a COMPOUNDING reset, a counter, and no fleet
  family shows one:
  - best NEST 4 at n = 80 (R41);
  - lagfam, leanT and chainfam are linear (R39, R40);
  - the instances of this box have NEST ≤ 2 (fixd_fdpos.py, stable order: xctx_viol_n20 has positions [0, 0, 2, 0], so NEST 2;
    vrall_viol_n20, xcov11_n20, tpp_viol_n22, tpp_viol_n63 and nopre_viol_n20 have NEST 1).
- The XCTX and VR-NEW mechanism does not compound as it stands. It is ONE swap: a vertex trades places between positions 1 and 2,
  so position 2 sees two context sets of equal size. A counter would need k independent swap gadgets, together with resets that
  return a lower gadget to an earlier set after a higher one rises. LEX allows that only if the higher position's outcome rises
  between returns, so each gadget level costs a rise at a higher position. Whether those rises can be nested k deep at
  polynomial size is the open (CTX⁺) question. Nothing found here answers it in either direction.
- (TREE-PIECE⁺)'s mechanism (the same key under a different parent X) lives at depth ≥ 1, which EMPTY-REC (R42 §2) rules out on
  𝒞^1P. In two-player games it repeats one key per re-cut of a parent subgame, and it gives no growth unless parent re-cuts
  compound: the same counter question.
- (NO-PRE-a) concerns one steal case for tied priorities. Steals per context are already bounded by the signed R14 term
  (F_R ≤ 3·#fired⁺(R)), and the open part is (FIRED⁺-R), which this instance does not stress (9 tangles, 4 iterations).
- (CHAIN-CHANGE), the one survivor, could not give super-polynomial growth on 𝒞^1P even if false. By EMPTY-REC, an identical-chain
  transition learns only in sptl at a fixed stable context. Runs of such transitions are bounded by the per-context budget
  (R9 (c) with F_R = 0 on the class, the L-ALG §34c / §36c reading), so a violation costs at most a polynomial factor.
Net reading: after this box, every known route from a local no-repetition statement to GAP-A on 𝒞^1P is closed. The question that
remains is the global one ((CTX⁺): how many distinct context sets one position can see in a phase). The only known way to make it
fail is a compounding counter, and no construction of one is known. The kills neither bring a lower bound closer nor rule one out.

## 4. Files
- experiments/red/nopre/instances/nopre_viol_n20.pg. It is pinned in experiments/red/check.sh: sha1, and b12_nopre scan pre = 1
  in both orders.
