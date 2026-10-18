# T19: literature check of the N1 kill, and the barrier entry for the map (L-LIT, 2026-10-18)

Asked by the Lead at 18:13Z. The kill is L-NEW 8ac5e5c, docs/new/N1-KILL.md (claude/l-new): "deep traps" on switchallexp give 11, 31, 71, 151, 311, 631, 1244 Even Howard switches (N = 1..7, n = 32N + 15), all inside ONE late phase. The Lead reproduced N = 1..5.

Status:
- DATA, unrefereed: one implementation (anneal.cpp), plus the Lead's re-run.
- This supersedes the step-3 verdict of T18 (441be35). Caveat 1 of T18 ("B8 by schedule only … a family where the warm start IS a bad start would put N1 inside B8's mechanism") is exactly what the kill does.

Every source below was opened in this session and is recorded in notes/L-LIT.md (T18 rows). Nothing new was needed beyond those.

## 1. Is the lower bound already known?
**Answer: NOT FOUND in the opened literature.** Searched for:
- (a) an exponential lower bound for IncreasingDiscountPI;
- (b) an exponential lower bound for discounted Howard started from the best-reward ("all traps") strategy at γ near 1.

| where looked (opened) | what it has | covers the kill? |
| --- | --- | --- |
| Loff-Skomra 2402.03975 v1 (Fig. 12, Thm 1.10, Thm 6.6) and 2610.22149 v1 (Fig. 7.2, Thm 7.14, §9) | smoothed upper bounds; halting for every input; worst case only via the anchor sentence (§1.2): "no upper-bound is known on the number of iterations, significantly better than the number of policies" | no lower bound |
| every citer of 2402.03975 (Semantic Scholar, 8 records), incl. Asadi-Chatterjee-Luo 2610.14150 (PDF p.24: warm start "not used in our analysis"; Lemma 11 is an n^n-type UPPER bound for their restart variant) | — | no |
| Friedmann 1106.0778 v2 §9 (Thm 9.5–9.8, Cor. 9.10) | discounted switch-all exponential on IndDPG(IndMPG(G_n)) at β_G = 1 − 1/(4\|V\|³·max\|r\|), for strategies reachable from **his start ι_Gn** (p.15: ι_Gn "will correspond to the global counter state" 0; §9 assumes "Ξ_ιG ⊴ Ξ_σ"); 1-sink games only | (b) partly: same counter, but the trap game is not 1-sink, its start is "all traps", and the long phase is IncreasingDiscountPI's, not Puri's algorithm |
| Hollanders thesis Thm 2.18 (printed p.48); Fearnley 1003.3418 Thm 17–18 | discounted / undiscounted Howard exponential on stochastic MDPs, "particular starting policy" | no: MDPs, fixed start |
| Blackwell-threshold papers 2610.10295 v1, 2506.18545 v1 | upper and lower bounds on the threshold α_Bw ("hard-instance bound", 2610.10295 p.2); [LS24] cited for strategy iteration | not a PI iteration bound; they only explain why a discount threshold can be exponentially close to 1, which the trap uses |
| web and arXiv search (T18 §4) | nothing on worst-case increasing-discount or homotopy PI | no |

## 2. How the kill relates to Friedmann §9 and to the anchor sentence (L-LIT reading, unrefereed)
**Friedmann §9 (Thm 9.5 [Vög00]; Lemma 9.6–9.7; Thm 9.8; Cor. 9.9).** For a 1-sink game G at β_G:
- discounted valuations order exactly as parity valuations do (Cor. 9.9, "⟺");
- Odd's discounted best response equals the parity one (Thm 9.8);
- so discounted switch-all replays the parity run from ι_G.

The proof of Lemma 9.7 bounds error terms only through upper bounds on 1 − β (p.37–38, the Δ1–Δ4 estimates). L-LIT reading: it therefore holds for every β ≥ β_G, not just β_G.

The kill composes two effects. Each needs its own proof.
- **(K1) Late release.** A trap at v has value about n^P − H·n^q at H = 1/(1−γ). It dominates every original option while H < n^(P−q), so the optimum in every earlier phase is "all traps", whatever the start. With P − q = 2k + 1 > B + 2, the release horizon n^(P−q) exceeds 4n³·n^B ≥ 1/(1 − β_G(G_N)) (B = the original maximum priority, rounded up to even). **So the release phase lies inside Friedmann's range for the original game.** This is the T18 caveat-4 issue reversed: the ablation was below β_G, the release phase is above it.
- **(K2) Bad start.** From "all traps" (= the best-reward start), Howard at that γ runs Friedmann's counter on the original part. L-NEW box 1 data: plain VJ from all traps takes Friedmann + 3 iterations (33, 73, 153, …).
- **What a proof must add to §9.** The trap game G'_N is not 1-sink: each c_v is an extra Odd-won self-loop, while Lemma 9.6 and Thm 9.8 need the 1-sink property. So two things must be shown:
  - (i) after release no trap edge is ever improving, i.e. the run stays on the original edges;
  - (ii) the strategy after the first switch from all traps is reachable from ι_Gn (Ξ_ιG ⊴ Ξ_σ), or is ι_Gn itself.
  - Then Thm 9.5–9.8 (at β ≥ β_G) give the rest. This is a referee-sized gap, not a literature fact.

**The anchor sentence.**
- (K1)+(K2) would give the first explicit worst-case lower bound for IncreasingDiscountPI (with Howard), and so a concrete instance behind the LS remark "no upper-bound is known … significantly better than the number of policies". It would be a lower bound, not just the absence of an upper bound.
- Mechanism in one line: a late Blackwell threshold, placed above β_G, turns the warm start into an adversarially chosen cold start at a parity-faithful discount. That removes the only thing separating N1 from B8 (T18 §2).
- **Transfer to LS's literal Fig. 7.2.** Three gaps remain:
  - (a) Mirror. N1 has Max switch-all against Min best response; Fig. 11 has Min switch against Max best response. The dual parity game (owners swapped, priorities +1) maps one to the other.
  - (b) Best-response choice. N1's Odd uses Dantzig while Fig. 11 uses repeated Howard. They agree when the best response is unique. L-NEW reported identical Even counts under both on four instances (box 1).
  - (c) Stop test. LS's mean-payoff test fires no earlier than N1's certificate, so LS's run is at least as long.
  - L-LIT reading: none of these looks like an obstruction, but none is checked.

## 3. Barrier-style entry for the map (added to BARRIERS.md as B20; the dead end for docs/RESULTS.md is the Lead's call)
| id | framework | statement | kind | covers | outside it |
| --- | --- | --- | --- | --- | --- |
| B20 | increasing-discount policy iteration (LS24 IncreasingDiscountPI, Howard) on parity-induced rewards | deep-trap switchallexp (L-NEW 8ac5e5c, gen_deeptrap.sh N; instances deeptrap_sae_N1..N7.pg with sha1 in deeptrap_sae.csv): 5·2^(N+1)-type Even switches in ONE phase, n = 32N + 15; Lead reproduced N = 1..5 | DATA (one implementation + Lead re-run); proof route (K1)+(K2) via 1106.0778 §9, gaps (i)–(ii) | N1 = IncreasingDiscountPI with warm starts, any start, any schedule γ_j → 1 that lands a phase after the release horizon | IncreasingDiscountPI with a non-Howard rule for the switching player (e.g. Dantzig for both, LS Thm 7.13 option): untested; schedule changes do not escape (any phase after release is parity-faithful, N1-KILL.md item 3) |

**Dead end (for the fleet record).**
- **N1**, Loff-Skomra IncreasingDiscountPI on rewards ±n^pr.
- **Obstruction:** trap gadgets with a priority gap P − q > B + 2 keep the all-traps strategy optimal in every phase until a release phase beyond Friedmann's β_G. That phase is switch-all from a bad start and replays Friedmann's counter.
- **Instance:** experiments/new/instances/killer/deeptrap_sae_N7.pg (claude/l-new 8ac5e5c, sha1 835ce1326ca3…): 1244 Even switches in one phase, n = 239.
- **Not yet refereed:** REFEREE item 1 of N1-KILL.md (anneal.cpp against Fig. 12) and gaps (i)–(ii) above.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - No opened source contains an exponential lower bound for IncreasingDiscountPI, or for discounted Howard from the best-reward start at γ near 1 on parity-induced games. The kill is not known in the literature (best effort: LS papers, all 8 citers, §9 of Friedmann, the MDP lower bounds, Blackwell-threshold papers).
  - The kill is (K1) a late release placed above β_G plus (K2) Friedmann's counter from the all-traps start. Friedmann §9 covers (K2) only for 1-sink games from ι_G, so two lemmas are missing (§2).
  - If proved, it is the first worst-case lower bound for LS's algorithm. It is consistent with the anchor sentence and makes it concrete.
  - T18's SIGNED verdict is superseded. Its caveat 1 was the kill route.
- NEEDS:
  - Lead: B20 is in BARRIERS.md (marked DATA). Decide whether REFEREE checks (i)–(ii) and whether DE goes to RESULTS.md.
  - owner: nothing.
