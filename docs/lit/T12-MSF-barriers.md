# T12: published barriers vs L-SI's MSF rule (gauntlet step 3, first pass) (L-LIT, 2026-10-15)

Asked by the Lead at 11:06Z. The rule checked is L-SI's S2a MSF, as defined at claude/l-si c73f69e, docs/si/candidates/S2.md "The rule, exactly":
- single-switch strategy improvement for Even, on the Vöge–Jurdziński valuation, against Odd's best response;
- it switches one improving edge of maximal *level*, where the level is the most relevant position at which Ξ(σ(v)) and Ξ(w) first differ;
- ties go to the smallest v, then the smallest w;
- it is memoryless and deterministic.

All sources below were opened, by L-LIT or by two L-LIT search agents. L-LIT re-checked the quoted lines in the downloaded texts. "p." means the PDF page unless marked "printed". The rows are logged in notes/L-LIT.md.

**Verdict: no published lower bound covers MSF on parity games. Every Dantzig-type exponential bound is for stochastic MDPs, and its key gadget uses transition probabilities that parity games lack. Status: NOT KILLED by the literature. The killer, if one exists, must be two-player with mixed-owner cycles.**

## 1. Where MSF sits (L-LIT reading)
- On a sink parity game the valuation is the multiset of priorities on the path to the sink, ordered by Σ(−t)^p, with t ≥ |V| (DLMM 2512.16684 §2, pp.4–5).
- The reduced cost of a switch (v, w) is then Val(w) − Val(σ(v)). Its magnitude is decided by the most significant priority in the symmetric difference of the two multisets, which is MSF's level.
- So MSF is **Dantzig's rule coarsened to the leading term**, with index tie-breaks inside a level. When all improving switches at a strategy have distinct levels, MSF and Dantzig choose the same switch.
- This means MSF is **not** a {Bland, Dantzig, LargestIncrease}-ranking-based rule in DLMM's sense (Def. 3.7, p.11, which allows only the relative orders). Whether two switches share a level is not a function of the Dantzig preorder.
- Maat 2509.16075 Thm 3.5 item 5 (p.10) gives the reduced costs of its LP for these games: H = t^{−w(j1,j2)}(walks^σ_{j2,i}(t) − walks^σ_{j1,i}(t)). That is the valuation difference times an edge-dependent factor t^{−w}. So "Dantzig on the parity-game LP" and MSF are not obviously the same rule.

## 2. Framework by framework

| framework / source (opened) | rule class, setting | covers MSF? |
| --- | --- | --- |
| DLMM 2512.16684 v2, Thm 4.3 (p.13); Thm 1.1 (p.2) | ℓ-index-based rules with o(m/log m) memory: decisions use only the global-index order of the improving edges. Sink parity games, n^{ω(1)} | **Does not cover.** MSF reads valuation content, not only index ranks. Lemma 4.4's counter G_n (Fig. 4.1, p.14) is in L-SI's bench, where MSF was linear |
| DLMM Thm 5.3 (p.33) = Thm 1.2 (p.3) | memoryless {Bland, Dantzig, LargestIncrease}-ranking-based rules. **Weak unichain MDPs**, Ω(2^√N) | **Does not cover.** (i) The setting is MDPs, and §5 says the definitions carry over "via the correspondence between PolicyIteration and the simplex method" (p.33), not to games. (ii) The Dantzig-greedy case f_Π(k)=k (Lemma 5.6, pp.39–43) scales reduced costs with randomized actions of probability p_{αℓ} = M^{−2ℓ+2}, p_{βℓ} = M^{−2ℓ+1} (Fig. 5.2). (iii) MSF is not in the class (§1) |
| Disser–Mosis 2309.14034 (ISAAC 2023), Thm 1 (p.2), Thm 28 (p.19) | Dantzig, Bland, LargestIncrease and any combination; single-switch policy iteration on **MDPs**, Ω(2^n) | **Does not cover.** Thm 28 needs "p_v = 2^{−N_V(v)(n+5)}" on the randomization vertices of Fig. 4 (p.14) so that "Dantzig prefers improving switches belonging to vertices with a small vertex number" (p.19). The Bland part (§3, B_n) is deterministic, but MSF is not Bland. p.2: "no exponential lower bounds are known for Dantzig's rule … in the setting of single switches" |
| Fearnley–Savani 1404.0605, Thms 3–4 (p.3) | Dantzig on MDPs is PSPACE-complete to predict; p.3: "Melekopoglou and Condon have shown an exponential-time lower bound for Dantzig's rule" | **Does not cover** (stochastic MDPs) |
| Melekopoglou–Condon, ORSA J. Comput. 6(2) 1994, DOI 10.1287/ijoc.6.2.188 | single-switch deterministic rules on MDPs (second-hand: Fearnley 1003.3418 p.1; FHZ STOC'11 preprint p.3) | **Unclear: NOT opened** (INFORMS 403, Semantic Scholar/OpenAlex "closed") |
| Friedmann 1106.0778 (LMCS 2011), Thm 6.14 (p.23), Thm 8.4 (p.33) | switch-all (locally optimal) and Schewe's globally optimal rule, two-player parity games | **Does not cover** (multi-switch; the timing needs simultaneous lane and cycle updates, §8 p.32) |
| Friedmann Zadeh (IPCO 2011 preprint) Thm 2 (p.14); Disser–Friedmann–Hopp 1911.01074 Thm 6.18 (p.31) | Zadeh's least-entered rule with designer-chosen tie-breaking (1911.01074 p.3: "it cannot be avoided to fix a tie-breaking rule") | **Does not cover** (history-based) |
| Avis–Friedmann 1305.3944 Thm 4 (p.15) | Cunningham's round-robin rule with a designer-chosen ordering | **Does not cover** (history-based) |
| Friedmann–Hansen–Zwick SODA'11 Thm 8.1 (p.11); STOC'11 preprint Thm 4.4 (p.12); errata 1410.7871 p.1 | Random-Facet, Random-Edge (randomized). The errata withdraw the Random-Facet = Random-Facet* claim; "the lower bound for Random-Facet∗ remains correct" | **Does not cover** (randomized) |
| Fearnley 1003.3418 Thm 17–18 (p.12) | "greedy policy iteration, which selects the most appealing switchable action at every state" (p.4), all states at once, MDPs | **Does not cover** (multi-switch) |
| Matoušek–Szabó (author's .ps, DOI 10.1016/j.aim.2005.05.021) Thm 1 (p.3) | RANDOM EDGE on AUSOs | **Does not cover.** It is randomized, and AUSOs have no reduced-cost magnitudes. Matoušek 1994 (RSA) was NOT opened |
| Friedmann PhD thesis (LMU 2011, author's copy) | tables of switch-all, switch-best, Random-Facet, Random-Edge, switch-half, least-entered (§4.2) | **Does not cover.** No Dantzig or most-significant rule for games. Printed p.93: "a sufficiently poor choice of a deterministic single-switch rule causes an exponential number of iterations … [BV07]. However, there is no particularly clever way to define a deterministic oblivious single-switching rule" |
| [BV07] Björklund–Vorobyov (Lebedev's examples, per Fearnley thesis printed p.58) | "a sufficiently poor choice" of a single-switch rule on games | **Unclear: NOT opened** (not attempted in this box). It is the only cited game example for single-switch rules |
| Fearnley PhD thesis (Warwick 2010, WRAP) printed pp.58–59 | single-switch exponential examples (Lebedev / [BV07]); Schewe's optimal switching killed by Friedmann | no MSF-like rule named |

## 3. Positive results that constrain any killer (opened; all for Dantzig, not literally MSF)
- **Post–Ye 1208.5083.** Thm 3.7 (p.9) and Thm 4.8 (p.12): Dantzig's single-switch simplex is strongly polynomial on **deterministic one-player discounted MDPs**, "regardless of the discount factor" (p.1). p.2: "Our results do not extend to policy iteration".
- **Zhong–Ye 2609.40147 v2** (13 Oct 2026, very recent, unrefereed). Thm 7.1 (p.31): Dantzig's rule (5.3), a lexicographic maximum of (gain difference, bias residual), is strongly polynomial on **deterministic one-player average-reward MDPs**.
- **Mei–Sun–Ye 2606.29568.** Thm 1 (p.16): single-switch "smallest negative reduced cost" for player 1 with an optimal response by player 2 is strongly polynomial on **two-player deterministic discounted forward games** ("no directed cycle contains actions controlled by both players", p.1).
- **Consequence (L-LIT reading).** If MSF's level ranking agrees with Dantzig's on the instance (no level ties among improving switches), then an MSF killer cannot be one-player, and in the discounted analogue it cannot be a forward game. It needs Odd choices **and cycles that mix Even and Odd vertices**, like Friedmann's simple cycles d_i (Even) ↔ e_i (Odd).
- **Caveats.** These results are for discounted or mean-payoff Dantzig with exact magnitudes, not for MSF's coarse tie-break, and not for the sink-game total-reward setting. They are guidance, not theorems about MSF.
- **Not opened:** Hansen–Kaplan–Zwick SODA 2014, DOI 10.1137/1.9781611973402.63 (SIAM 403; not on arXiv).

## 4. Best candidate construction for a killer (L-LIT reading; for L-SI to build)
**The obstruction to porting Dantzig lower bounds.** In both MDP proofs (DLMM Lemma 5.6; Disser–Mosis Thm 28), each counter edge (x, y) becomes a chain x → δ(x,y) ⇢ ε(x,y) → y. The randomized action at δ(x,y) exits with a small probability p_x, so:
- the switch's reduced cost is p_x·(Val(ε) − Val(x)) (DLMM eq. (5.5), p.42);
- once it is applied, values are as in the plain counter (DLMM eq. (5.4)).

This decouples a switch's **rank** from its **effect**, so low-level switches can be ranked first. In a one-player sink parity game the two cannot be decoupled: the level of (v, w) is the top priority of Val(w) Δ Val(σ(v)), and after the switch every predecessor of v sees the same difference.

**The candidate: an Odd gate in place of the probability gadget.** Disser–Mosis D_n (2309.14034 §4, Fig. 4 p.14, built on the deterministic counter B_n of §3, Fig. 1) with every randomization vertex replaced by an **Odd-owned gate**, in the style of Friedmann's cycle gates (1106.0778 §5):
- Odd can leave the δ-ε chain to a vertex of high odd priority, so Odd's best response hides most of the switch's effect from v's predecessors.
- The priorities are chosen so that the switch at counter level ℓ is decided at a priority **decreasing in ℓ** (the analogue of p_v = 2^{−N_V(v)(n+5)}).
- The cycle x → δ → Odd gate → x is mixed-owner, as §3 requires.

**What L-SI must check on each visited strategy:**
1. the improving set is exactly D_n's, plus gadget switches;
2. MSF's maximal level picks the switch D_n's Bland order would pick;
3. no level ties remain, or the index tie-break agrees.

**Cheaper first test, for LSF rather than MSF.** DLMM Lemma 5.4 (pp.34–38) uses M_L (Fig. 5.1), which is deterministic up to an ε-perturbation used only to avoid relying on tie-breaking (p.38). It is the f_Π ≡ 1 case, "least-preferred improving switch in the common ranking", i.e. LSF's choice.
- **Port:** levels ℓ = 1..L, states α_ℓ, β_ℓ (Even); actions α_ℓ/β_ℓ → α_{ℓ+1} (no reward) or → β_{ℓ+1} (reward L^ℓ); α_{L+1} → sink with reward L^{L+1}; β_{L+1} → sink.
- **Translation:** put each reward on a fresh vertex of distinct even priority 2ℓ+c, increasing in ℓ. Index α_ℓ before β_ℓ, and lower levels first.
- Start from Lemma 5.4's σ_0. Lemma 5.4 predicts Ω(2^L) switches for a rule that always takes the least significant improving switch, if L-SI's level order matches DLMM's reduced-cost order there. This is a one-player game, so the positive results of §3 (about Dantzig, the opposite end) do not forbid it.

## 5. Hansen's 2012 thesis
- One other route was tried, the Wayback Machine:
  - archive.org/wayback/available for cs.au.dk/~tdh/papers/thesis.pdf returned no snapshots (that path is a guess);
  - the web.archive.org CDX query was "Blocked by egress policy";
  - the https retry reset the connection twice.
- Semantic Scholar returned 429 and OpenAlex's budget was exhausted. **NOT opened.**

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - No published lower bound covers MSF on parity games.
  - DLMM Thm 4.3 covers index-only rules; DLMM Thm 5.3 and Disser–Mosis cover Dantzig only on stochastic MDPs, via probability scaling.
  - MSF is a coarsened Dantzig, outside DLMM's ranking class.
  - Dantzig is polynomial for one-player deterministic games (Post–Ye; Zhong–Ye, unrefereed) and two-player forward games (Mei–Sun–Ye), so a killer needs mixed-owner cycles.
  - Killer candidate: Disser–Mosis D_n with Odd gates replacing the probabilities.
  - Cheap test for LSF: the sink-game port of DLMM M_L (Lemma 5.4).
  - Not opened: Melekopoglou–Condon, [BV07], HKZ 2014, Hansen's thesis.
- NEEDS:
  - owner: library access to Melekopoglou–Condon 1994, Hansen–Kaplan–Zwick SODA 2014 and Hansen's thesis, only if MSF survives L-SI's construction attempts.
  - L-SI (via the Lead): build and run the §4 candidates.
