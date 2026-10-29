# R2-N5-MPGS: REFEREE-2 report on packet P-N5-MPGS (L-LIT): Part (A) MATCH-Φ, Part (B) Lemma GATE-SHUT
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-29 from 11:18Z (date -u).
Object: docs/lit/P-N5-MPGS.md, sha1 24913a7f9efea437aa202b398113b7ce12890961, 246 lines, l-lit freeze a23179b01be61d7f85e37aa93c0ae55a2dde7de8. Measured
with `git show a23179b0:<path> | sha1sum`, as were the pinned scripts:
- T33-match-phi-check.py 6853179b;
- T34-gateshut-check.py 7c33508b;
- P-N5-MPGS-quotecheck.py 74dbe8b4.
All equal the Lead's figures.
SUPERSEDES P-N5-MATCHPHI (fixes F1: "Referees sign P-N5-MPGS, not this packet"). My R2-N5-MATCHPHI.md (5ba3e21d) was written on the superseded
packet. Its checks carry over to Part (A) (§1 below).
INDEPENDENCE:
- I have not opened any file under docs/referee/ on MPGS or MATCHPHI, and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic 'mpgs\|matchphi'`: 0 at 2026-10-29 11:17:40Z; 0 at 2026-10-29 11:25:43Z (push turn, after `git fetch origin claude/referee`).
  Names only.
- The lane's three scripts were READ, then run as the Lead's pinned re-runs, in a detached worktree at a23179b0 with `python3 -I` (removed
  after). T34 imports L-COMP's hn.py / census.py / n5b.py read-only, as it says.
- My checks use my own code: docs/referee-2/R2-N5-MATCHPHI/mphi_check.py for (A); docs/referee-2/R2-N5-MPGS/gateshut_check.py for (B), on my lane's
  SPEC loop, with Ξτ recomputed as a play value. No lane module is imported. Friedmann's H_n are read as the .pg / .start files in
  experiments/friedmann-hn/instances.
Scope (D1): (A) is a REDUCTION to NM (OPEN). (B) is a structural lemma that bounds no count. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| A0 | definitions pos, w, Φ, MATCHED (M1)-(M3), CARRY, NM | SIGNED |
| A2 | Fact A1 | SIGNED |
| A2 | Lemma MATCH-Φ | SIGNED |
| A2 | Added statement (A): PCH_𝒫(v) ≤ (K(K+1)/2)(NM + 1) + NM per vertex per phase, every game | SIGNED. The first term is SHARP at NM = 0 (N-MP-2) |
| B0 | definitions G^d, Ξτ, τ̄, ⊴ vs ⊴_d, plays as lassos, gate e / h / d, Even route π, Q, ρ, c_h, (H1)-(H3) | SIGNED (well formed) |
| B1 | Fact B1 (the dual order on equal cycle nodes reverses the set comparison) | SIGNED |
| B1 | Fact B2 ((VJ) of R57 (a) on G^d) | SIGNED |
| B2 | Lemma GATE-SHUT (6 steps) | SIGNED |
| B2 | Added statement (B): (H1)-(H3) at every state of a stretch with τ(e) = h ⇒ (e, d) ∉ Iτ there and τ never moves h → d | SIGNED |
| — | pinned re-runs T33, T34, quotecheck | REPRODUCED exactly (§3) |
| — | quotes | 9/9 VERBATIM (lane quotecheck "quotes=9 bad=0"; my qcheck 9/9, SHIFT=1 control 0/9) |
| A3, A4, B3, B4 | DATA, READING | not signed. Notes N-MPGS-4, -5 |
No gap. Notes N-MPGS-1..6 (with N-MP-2..5 of R2-N5-MATCHPHI carried over).

## 1. Part (A): the diff against P-N5-MATCHPHI, and the carry-over
- The mathematics is IDENTICAL: the same definitions, the same Fact (renamed A1), the same Lemma proof (written as one sum, the same three
  groups), the same Corollary bound.
- The text differs in four places. None changes a statement:
  - Fact A1 drops the sentence "So a MATCHED change is one that decomposes …". The table's line keeps that reading.
  - The width is written "W ≤ K(K+1)/2" instead of "W = Σ k = K(K+1)/2". Both are correct; W equals K(K+1)/2.
  - The added statement omits the "≤ (n²/2)(NM + 1) + NM" form. It follows from K ≤ n − 1, which A0 states.
  - The "Uses" line now says that Fact A1 uses [DELTA] and that nothing uses (MON). This FIXES my N-MP-1 on the superseded packet.
- Quote base moved from 6abea2e6 to 1f15c91b. The quoted lines are verbatim at the new base (§3).
- So every check of R2-N5-MATCHPHI §1-§2 applies verbatim. That includes the exhaustive K ≤ 7 combinatorics (Fact A1, additivity, MATCHED ⇒
  weight rise, MATCH-Φ, my matcher = brute force), the 25,000 arbitrary sequences, the N5 data (0 violations) and the tightness result.
- The pinned T33 output at a23179b0 is byte-identical to the one at 12b7d12a (logs/pinned_T33.txt; diff empty).
- Carried-over notes: N-MP-2 (sharpness at NM = 0), N-MP-3 (additivity line), N-MP-4 (the alt_all NM figure; §A3 now gives only "62 (n 581),
  1.18 (pl130_n40)", which my data reproduce, so N-MP-4's "31" no longer applies), N-MP-5.

## 2. Part (B): proof check
- B0.
  - G^d, Ξτ and τ̄ are as SPEC S1 Odd's side (quoted). Ξτ(x) = V^d_{τ,τ̄}(x) is the definition of S1's valuation as a play value: my DENG
    check found 0 differences at all states.
  - Plays under positional strategies are lassos.
  - Q's vertices are distinct, because π's are distinct Even vertices and e is Odd.
- Fact B1. By [A3], G^d keeps G's ranks, so P (rank > rank(c)) and the cycle node (maximal rank on the cycle) read the same in both games, and
  G^d's signed weight is −weight. With equal cycle nodes and P ≠ P′ both orders decide on P, in opposite directions. ✓
  - B1: 0 failures on 10,036,398 same-cycle-node pairs of actual Ξτ values (746,800 on H_n).
- Fact B2. (VJ) "on every game" applies to the game G^d, whose Even strategy is τ and whose Odd strategies are G's Even strategies. ✓
- Step 1. σ′ is a positional Even strategy, equal to τ̄ off π. ✓
- Step 2. By (H2) ρ never visits π, where σ′ differs, so the play from h is unchanged. ✓
- Step 3.
  - The play from d is π, e, then h's play, because τ(e) = h. Its prefix π·e is simple and disjoint from ρ by (H2), so it has ρ's cycle and
    cycle node c_h.
  - Its set is P(ρ) ∪ Q by (H1) and the P-rule.
  - S3: computed as a play value on G^d at every hypothesis-satisfying gate, 0 failures.
- Step 4. The two sets differ exactly by Q (disjoint, by (H2)). Its top-rank vertex is even (H3) and lies in the larger set, so [DELTA] gives
  a higher G-weight. With the same cycle node, Ξτ(h) ◁ V, and Fact B1 gives V ◁_d Ξτ(h). ✓ (S4: 0 failures.)
- Step 5. Fact B2 with x = d and σ′: Ξτ(d) ⊴_d V. ✓ (S5: 0 failures.)
- Step 6. Ξτ(d) ◁_d Ξτ(τ(e)), so it is not strictly better for G^d's Even, and [S2] gives (e, d) ∉ Iτ. ✓
- The places where each hypothesis is used are exactly the steps the Lead lists:
  - (H2) in steps 2-3;
  - (H1) in step 3;
  - (H3) with DELTA in step 4;
  - (VJ) in step 5.
- Added statement (B).
  - S4b's τ_new(e) lies in A(e) = {τ(e)} ∪ Iτ-targets, because its arena restricts Odd to A.
  - S4c's Odd fallback moves e only to an Iτ-target.
  - An Even fallback and S4a leave τ (FIX 3).
  - d ∉ A(e) at each state of the stretch, so τ_{t+1}(e) ≠ d. ✓ (CORB: 0 failures at 38,289 transitions from hypothesis states.)
- What is not claimed (persistence of (H1)-(H3)) is correctly not claimed. My data contain 8,829 h → d moves of τ at gates where some
  hypothesis fails (CTL_flip_nohyp).

## 3. Pinned re-runs and own data
- Pinned (logs/pinned_T34.txt, pinned_T33.txt, pinned_quotes.txt). T34 at a23179b0, all exit 0:
  - "3 0 0" → 135 / 135 / 0 / flips 0, 0;
  - "3 200 3" → 14385 / 14217 / 0 / 102, 0;
  - "4 100 4" → 12045 / 11911 / 0 / 97, 0;
  - "5 30 5" → 5783 / 5705 / 0 / 48, 0;
  - the S3 + F runs for n = 4, 5, 6, 8 → 228, 350, 510, 872 gate-states, all with (H1), (H2), 0 violations, 0 flips.
  - All exactly as §B3 says.
  - T33 is identical to §A3. Quotecheck "quotes=9 bad=0".
- Own GATE-SHUT data (gateshut_check.py). Every gate (e, d, π) with π a path of distinct Even vertices from d into e (≤ 6 vertices, ≤ 40 paths
  per (e, d)) at every state, on every game. 0 violations of DENG, B1, GS, S3, S4, S5, CORB:
| corpus | runs | states | gates with (H1)-(H3) (GS) | CORB transitions | controls: noH1 / noH2 / noH3 bite (of checks) |
| --- | --- | --- | --- | --- | --- |
| Friedmann H_n (experiments/friedmann-hn/instances: 71 runs, every .pg with S3 and each of its .start files) | 71 | 3,734 | 22,798 | 22,412 | 28/28 / — / — ((H3) holds on every gate there) |
| lib41_noref × 3 | 1,230 | 19,519 | 33,572 | 8,934 | 2,938/214,496 / 0/10,837 / 2,777/210,912 |
| alt_all (413; 1 start entry validated) | 413 | 10,604 | 12,713 | 4,820 | 871/104,971 / 0/4,450 / 1,064/239,267 |
| random kO n 8-20 / k2 n 6-16 (5,000 × 3 each) | 30,000 | 83,553 | 3,902 | 2,123 | 1,836/20,780 / 0/241 / 581/2,539 |

## 4. Notes (not gaps)
- N-MPGS-1 ((H2)'s necessity is not exhibited). Where only (H2) fails, (e, d) was never improving in my data (0 of 15,528). (H2) is used in
  steps 2-3, so it stays. Data do not show it is needed.
  - (H1) and (H3) are needed: their controls bite (5,673 and 4,422 cases), including on H_n for (H1) (28 / 28). This matches §B3's example
    (a cycle node above the gate).
- N-MPGS-2 (the pinned T34 tests (H1) on d1 only). Its line `hyp = rank[c] < rank[d1] and not ({d1, d2, d3, e} & set(seen))` checks rank(c_h) <
  rank(d1), while the Lemma's (H1) asks it for every u ∈ Q = {d1, d2, d3, e}.
  - This is DATA, not to sign. It is the right test only if d1 has the lowest rank in each Friedmann gate.
  - My check takes the full Q on the same H_n instances, and found 0 violations, so the DATA conclusion is unaffected. The script's comment
    should say so.
- N-MPGS-3 (Part (A) carry-over). See §1. The superseded packet's N-MP-1 is fixed in MPGS's "Uses" line. My R2-N5-MATCHPHI.md stays as the record
  of the checks.
- N-MPGS-4 (B4 READING, not signed). "(H1) is automatic in Friedmann's 1-sink games (the cycle node is the sink)" is consistent with my H_n data
  only where c_h is the sink. My noH1 control bites on 28 H_n gate-states, i.e. states where Ξτ(h)'s cycle node lies above the gate. These are
  the reopenings §B3 describes.
- N-MPGS-5 (enumeration scope). My gate enumeration is capped (π ≤ 6 vertices, ≤ 40 per (e, d)). Gates with longer Even routes are not
  covered by my data. The proof has no length condition.
- N-MPGS-6 (scope wording). The Lemma holds at any state of any N5 run, in-phase or not (it uses no phase). The added statement (B) is per
  transition. Both are stated that way; nothing to repair.

## 5. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-MPGS/{gateshut_check.py, hn.lst, run_all.sh, logs/ (including the pinned re-runs)}. Part (A)'s tools and
  logs: docs/referee-2/R2-N5-MATCHPHI/.
- FINDINGS:
  - Every item of (A) and (B) SIGNED, no gap. (A) is identical in mathematics to MATCHPHI.
  - GATE-SHUT: 0 violations at 72,985 gates (22,798 on H_n). (H1) and (H3) are necessary in data; (H2) is not shown necessary (N-MPGS-1).
  - T34 tests (H1) on d1 only (N-MPGS-2).
- NEEDS: Lead: the §C word; route N-MPGS-1..6 (+ N-MP-2..5) to L-LIT.
