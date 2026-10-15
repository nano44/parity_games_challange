# C2: landing-gate check of RESULTS candidate R3 (original Random-Facet on parity games) (CHECKER, 2026-10-15)

Scope: the Lead's 13:34Z brief, items (1)-(4). No mathematical judgement. Trunk at check time: claude/vibrant-johnson-nxvvxo
19c6207. Exact commits: l-red 49ae306 (proof, code), referee-2 995cfd3, referee 42f11c6 + 5ed56c5, l-lit c962d80.
Clean detached worktree at l-red 49ae306 (`git status --porcelain` empty before and after the runs).

## Verdict: FAIL
- The computations pass.
- One of the two required signatures does not exist (finding S-1). CLAUDE.md: "A claim is a result only when ... two
  referees signed it."
- The proposed text over-claims in four places (section 3).
- Three of the referees' gaps are missing from the entry (section 4).

| item | verdict |
| --- | --- |
| (1) exact-commit re-runs | PASS (check.sh; lockstep, lockstep3, relation on quoted and new settings; all agree) |
| (2) signature to commit | FAIL: REFEREE-2's R2-TL.md is "a first-referee read, not a signature", at 0d50d4a; REFEREE's signature commits are not on trunk |
| (3) statement diff | FAIL: missing parameter scaling and start tree (over-claim); n clashes with TARGET's n; tie convention unstated |
| (4) gaps carried | FAIL: only G-TL-1 carried; G-TL-2, G-TL-3 and REFEREE's AUSO/ties gap missing |

## 0. Blob identity (trunk 19c6207 vs signed commits)
| file | commit | |
| --- | --- | --- |
| docs/red/R2-RAR.md | l-red 49ae306 | MATCH dd4f1e9 |
| experiments/red/fhz.py, check.sh | l-red 49ae306 | MATCH bc5aa4b, 3ae227a |
| experiments/red/instances/fhz_n3_r1s1t1.pg, fhz_n4_r1s1t1.pg, fhz_n5_r2s2t2.pg | l-red 49ae306 | MATCH |
| docs/referee-2/R2-TL.md | referee-2 995cfd3 | MATCH f9719ee |
| docs/lit/T13-RF-parity.md | l-lit c962d80 | MATCH ee948df |
| docs/referee/R-TL2.md | referee 5ed56c5 (1d4cca6) / 42f11c6 (5666177) | **DIFF**: trunk has 740b6ab = referee 6d5d9ad |

The Lead's brief says "All are merged on trunk". That holds for l-red, referee-2 and l-lit. It does not hold for the
REFEREE:
- `git branch -r --contains 42f11c6` and `--contains 5ed56c5` list only origin/claude/referee.
- Trunk's R-TL2.md stops at §7 (signed at 0d50d4a "subject to findings 1–2").
- Trunk lacks §9 (the verdict at 8bb9d22 with the case-(3) condition) and §8 (the 11.4M-tree runs).

## 1. Exact-commit re-runs (l-red 49ae306)
| run | output (abridged) | |
| --- | --- | --- |
| `bash experiments/red/check.sh` | "red check: friedmann_Gn 2 S7 = 15; fhz lockstep3/relation/export OK; gated_bland 6 = 63 MSF iterations (regions = Zielonka, strategies verified); Claim F instances; MSF == Bland N<=6; games 150, runs 600 (375 switches), brute-force valuation checks 450, si.py run comparisons 0: mismatches {'bf': 0, 'zlk': 0, 'strat': 0, 'lsi_iters': 0, 'lsi_vals': 0}", exit 0 | PASS |
| `fhz.py lockstep 5 2 2 2 3` | seeds 0-2: 131 / 190 / 173 switches, 5381 / 7589 / 6908 tests, "models agree" (parity \|V\| = 256) | PASS; equals R2-RAR's quoted "up to 190 switches, 7,589 tests" |
| `fhz.py lockstep 7 2 3 3 2` | 769 switches / 72296 tests and 542 / 54421, "models agree" (parity \|V\| = 610) | PASS; equals the quoted values |
| `fhz.py lockstep 4 3 2 2 3` (new setting) | 72 / 87 / 70 switches, 3930 / 4098 / 4552 tests, "models agree" (parity \|V\| = 285) | PASS |
| `fhz.py lockstep3 4 2 1 2 2` | 50 / 43 switches, 955 / 1221 tests, "all three models agree" | PASS |
| `fhz.py lockstep3 3 2 2 2 2` (new setting) | 34 / 50 switches, 1174 / 1515 tests, "all three models agree" | PASS |
| `fhz.py relation 4 2 2 2 300` | "300 random (F, B) pairs, improving sets differ in 0" | PASS |
| `fhz.py relation 10 1 1 1 1500` | "1500 ... differ in 0" | PASS |
| `fhz.py relation 6 2 3 2 300` (new setting) | "300 ... differ in 0" | PASS |

Tooling note (non-blocking): `python3 -I fhz.py relation ...` fails with `ModuleNotFoundError: No module named 'vj'`.
- Cause: relation_check (fhz.py:237) imports vj without putting the script's directory on sys.path; lockstep3 does add it.
- It runs as check.sh runs it (from experiments/red, without -I), and that is how the relation rows above were produced.
- L-RED may add the same sys.path line to relation_check.

Code drift between the commits the referees read and 49ae306:
- fhz.py: 0d50d4a (REFEREE-2) and 8bb9d22 (REFEREE) differ from 49ae306 in the module docstring only.
- vj.py: changed after 8bb9d22. The only change is the new rule `most-improved` (pick_most_improved plus one dispatch
  branch), which lockstep3 does not use.

## 2. Signature to commit
### REFEREE-2, docs/referee-2/R2-TL.md (referee-2 995cfd3)
- Line 3: "Lead's brief 12:12Z (3 h box; **first-referee read, not a signature**)". Claim refereed: l-red **0d50d4a**.
- Verdict: "OK with fixes (F1-F2 below)".
- §5: "Established (modulo the first-referee status)".
- No signature block. No later REFEREE-2 commit on R2-TL (`git log origin/claude/referee-2 -- docs/referee-2/R2-TL.md`:
  995cfd3 only).
- REFEREE-2 has not checked the application of F1-F2 (made at 8bb9d22) or anything at 49ae306. Only REFEREE checked them
  (R-TL2 §9).
- **S-1 (blocking).** The candidate has one signature, not two.
- Consequences elsewhere:
  - Lead reading L21 ("both referees signed, REFEREE-2 995cfd3, REFEREE 42f11c6") and L-LIT T13 ("signed by REFEREE-2
    (995cfd3) and REFEREE (6d5d9ad)") both state it as signed.
  - The proposed entry's label "[refereed-only]" depends on it.
### REFEREE, docs/referee/R-TL2.md (referee 42f11c6 §9, 5ed56c5 §8)
- Signed claim (§9, verbatim): "the Transfer Lemma as stated at 8bb9d22 and the consequence 'Random-Action-Removal (S1) from
  any zero-edge start on P_{n,r,s,t} has the run distribution of Random-Facet on G_{n,r,s,t} from B_0, hence FHZ Thm 6.3's
  e^{Ω(√n)} expected switches', with FHZ Thm 6.3 as a black box". Signed "subject to the one-token fix in case (3)".
- Condition check (`git diff 8bb9d22 49ae306 -- docs/red/R2-RAR.md`): MET.
  - Case (3) now reads "cheaper at j* by at least 4^{j*} > (the sum below j*, < 4^{j*} - 2 by (1)) + (the offset
    difference at j, < 2)": exactly the required token.
  - The two nits are also applied: the strict-test citation of si.py Engine.improving, and the fhz.py docstring.
  - Nothing else in the lemma or proof changed. The only other edits to R2-RAR.md are a "Start strategy" paragraph that
    restates the zero-edge start, and the citation added inside the lemma's statement paragraph.
- I checked the cited si.py lines at l-si 95d37d3:
  - si.py:210: `self.key(val[w]) > kc` (strict).
  - si.py:345: `_rar` pivots iff `self.key(val[r]) > self.key(val[b[v]])` (strict).
  - si.py:220-224: the best start takes the max (reward, index), reward 0 for priority-0 relays.
  - Note: experiments/si/si.py is not on trunk (l-si unmerged). This matters only for DE6, not for R3's statement.
- REFEREE's signature is valid for 49ae306. It is not on trunk (section 0).
### Stale text inside the signed file (non-blocking; L-RED's file)
- R2-RAR.md at 49ae306 still says "### Transfer Lemma (L-RED, unrefereed)", "The transfer lemma is unrefereed" (What this
  does not say) and "Referee status: REFEREE-2 first read".
- RESULTS would cite a file that calls its own lemma unrefereed. L-RED should update these lines. If it does, the trunk copy
  and the commit cited in RESULTS must be updated to match.

## 3. Statement diff (proposed entry, phrase by phrase)
Sources:
- (a) R2-RAR.md at 49ae306.
- (b) FHZ 1410.7530, opened by me: arXiv e-print, sha256 585080ff…164a; Lower-RandomFacet.tex:135-142.
  - thm:main is Theorem 6.3: §6 = Lower-RandomFacet.tex, the 6th \section of the \input order; the theorem counter is
    per-section and shared, and thm:main follows Definition 6.1 and Lemma 6.2.
  - Verbatim: "The expected number of switches performed by the Random-Facet algorithm, when run on the graph G_{n,r,s,t},
    where r = Θ(log n), s = Θ(√n log n), and t = Θ(log n), with initial tree B_0, is at least e^{Ω(√n)} =
    e^{Ω(M^{1/3}/log M)}, where M is the number of edges in G_{n,r,s,t}".
  - B_0: "a tree consisting entirely of zero-edges" (Lower-RandomFacet.tex:122-123; Actual-Construction.tex:144-147).
  - Here n is "the number of bits".
  - \RandomFacet is the original algorithm: fresh random choice per call, RandomFacet.tex Fig. F-RandomFacet; Random-Facet*
    is §7, Lower-RandomFacet-star.tex. So the entry's "original Random-Facet, not Random-Facet*" is correct.
- (c) TARGET.md §1.

| # | proposed text | finding | fix |
| --- | --- | --- | --- |
| D3-1 (over-claim, blocking) | "needs e^{Ω(√n)} expected improving switches on sink parity games P_{n,r,s,t}" | Thm 6.3 holds only for r = Θ(log n), s = Θ(√n log n), t = Θ(log n). Without them the sentence reads as for every (n, r, s, t), which neither FHZ nor the lemma gives. The size "Θ(n^{3/2} log^3 n)" implies the scaling only implicitly. | "... on the sink parity games P_{n,r,s,t} with r = Θ(log n), s = Θ(√n log n), t = Θ(log n)" |
| D3-2 (over-claim, blocking) | (no start strategy) | Thm 6.3 is "with initial tree B_0" (all zero-edges). The lemma transfers runs from σ_{B_0}, and REFEREE signed "from any zero-edge start". From an optimal start Random-Facet makes 0 switches, so "needs" without a start is false as worded. | "... started from σ_{B_0}, B_0 any tree of FHZ zero-edges (this includes the PGSolver best-reward start)" |
| D3-3 (vocabulary, blocking) | "e^{Ω(√n)}", "Θ(n^{3/2} log^3 n)" | n is FHZ's bit count. TARGET §1's n is \|V\|. In TARGET terms, with N = \|V(P)\| = Θ(\|E(P)\|) = Θ(M) (R2-RAR "Size", re-derived: \|V(P)\| = \|V(G)\| + \|E(G)\| + n(2rs+1) + 1), the bound is e^{Ω(N^{1/3}/log N)}. | name FHZ's n "the bit parameter n" and add "= e^{Ω(N^{1/3}/log N)} for N = \|V\| + \|E\| of P (TARGET size)" |
| D3-4 (condition, blocking) | "= Zwick 2607.06334 Fig. 1 Random-Action-Removal with Vöge-Jurdziński valuations" | Zwick's RAR is defined on AUSOs (no ties). P has ties (copies of multi-edges). REFEREE §4 condition (i): the run equivalence needs the strict convention, ties not switched. The lemma's text states it (si.py strict test). | add "with the strict improvement test (ties are not switched)" |
| D3-5 (note) | "Proof: ... L-RED's Transfer Lemma (every tree B and edge e ∉ B: strictly improving in G iff improving in P, ties included)" | matches the lemma at 49ae306 (G: strict improvement; P: VJ improving edge, strict). "ties included" is the proof's remark (equal cost ⟺ equal set and length). | none |
| D3-6 (note) | "(priorities O(nrs), compressible to {0..\|V\|})" | max priority base_n + 4rs = 2 + (n−1)(4rs+2) + 4rs = O(nrs); n(2rs+1) + 2 distinct priorities ≤ \|V(P)\| (R2-TL §2). TARGET §1 compression preserves order and parity, so VJ valuations and the improving relation are unchanged, at O(N log N) cost. | none |
| D3-7 (note) | "sink parity games" | not a TARGET term. P is a TARGET game: one sink with an Odd self-loop of priority 1; every other vertex Even and with a successor; priorities on vertices, max-parity. Friedmann 1106.0778 §5 ("1-sink games"). | optional: "(one-sink games, Friedmann 1106.0778 §5; Odd wins every vertex)" |
| D3-8 (note) | "Matoušek-Sharir-Welzl / Kalai; FHZ errata 1410.7871 §2" | FHZ 1410.7530 §2 (RandomFacet.tex) also states the MSW/Kalai identity. The referees cite the errata's Fig. 1 under §1-2. | none |
| D3-9 (note) | "Thm 6.3" page | R2-RAR says p.22, T13 says p.19. Theorem number 6.3 confirmed from the source. Page not checked (source not compiled). | cite by number only |
| D3-10 (blocking with S-1) | "[refereed-only]", "Status ... (Lead reading L21)" | L21 rests on two signatures; there is one (S-1). | after REFEREE-2 signs, update L21's citation |

## 4. Gaps carried
| referee gap | in the entry? |
| --- | --- |
| G-TL-1 (both): FHZ Thm 6.3 used as a black box | YES |
| G-TL-2 (REFEREE-2) / REFEREE "Gaps" 2: the lemma's proof is prose; machine evidence is exhaustive only for small (n, r, s, t) (REFEREE: 11,420,544 trees, 0 disagreements; REFEREE-2: 435,584 tests) and random beyond | NO |
| G-TL-3 (REFEREE-2) / REFEREE "Gaps" 3: S1's tie convention and start tree taken from si.py by reading (now cited in the lemma) | NO |
| REFEREE "Gaps" 4: Zwick's Rand-Act-Rem is stated for AUSOs (no ties); its use on a game with ties is L-SI's rule S1 | NO (tied to D3-4) |
| T13 residual: Hansen 2012 thesis unopened (novelty only) | YES |

## Fixes (all needed for PASS)
1. S-1: REFEREE-2 signs at l-red 49ae306.
   - The signature checks the application of F1-F2 (diff 0d50d4a..49ae306) and has a signature block naming the claim
     and the gap list.
   - Then correct L21 and T13's "signed by REFEREE-2 (995cfd3)" to the new signing commit.
2. Land referee 5ed56c5 (R-TL2.md §8-9) on trunk.
3. Entry text: D3-1 (r, s, t scaling), D3-2 (B_0 start), D3-3 (n vs TARGET's n; bound in N), D3-4 (strict test).
4. Gaps: add G-TL-2, G-TL-3 and the AUSO/ties gap.
5. Recommended, non-blocking:
   - L-RED updates the "unrefereed" lines in R2-RAR.md (then re-land, re-pin the commit).
   - Make fhz.py relation runnable with `python3 -I`.

Suggested entry text, a CHECKER suggestion and not signed wording (the Lead fixes the final wording; the second signature
must name it):
"R3 [refereed-only] Original Random-Facet on parity games.
- Algorithm: original Random-Facet strategy improvement (Matoušek-Sharir-Welzl / Kalai; FHZ 1410.7530 §2 and errata
  1410.7871; = Zwick 2607.06334 Fig. 1 Random-Action-Removal with Vöge-Jurdziński valuations and the strict improvement
  test, ties not switched).
- Claim: started from σ_{B_0}, B_0 any tree of FHZ zero-edges, the algorithm performs e^{Ω(√n)} expected improving
  switches on the one-sink parity games P_{n,r,s,t}, n = FHZ's bit parameter, r = Θ(log n), s = Θ(√n log n),
  t = Θ(log n). These games have N = Θ(n^{3/2} log^3 n) vertices and edges, so the bound is e^{Ω(N^{1/3}/log N)}.
  Priorities are O(nrs), compressible to {0..|V|}.
- Proof: FHZ 1410.7530 Thm 6.3 plus L-RED's Transfer Lemma: for every tree B and edge e ∉ B, e is strictly improving in
  G_{n,r,s,t} iff it is improving in P_{n,r,s,t}, ties included.
- Gaps:
  - G-TL-1: Thm 6.3 is a black box.
  - G-TL-2: the lemma is proved in prose; exhaustive checks cover only small (n, r, s, t).
  - G-TL-3: the start and tie conventions of S1 are taken from si.py by reading.
  - Zwick's RAR is defined for AUSOs; on games with ties, the strict convention is part of the algorithm's definition.
- Status: M3-type (L21). Novelty NEW as a published statement, low technical novelty (T13); Hansen 2012 thesis unopened."
