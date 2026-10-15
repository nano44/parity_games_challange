# L-LOWER notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-15 07:40Z. L1 box ends 23:01Z. RESULT: B_1(5) = 8 = 2n-2 (cegar5_k8_b.json, verified on all 916e6 five-vertex games +
independent checks); window-1 chains need >= 12, window-2 >= 9 at n = 5. Report docs/lower/L1-report.md §1, §4, §5 updated;
statement §2 known picture updated. Lead messaged with DONE/FINDINGS/NEEDS at ~07:45Z. RUNNING (cegar5b.py, checkpoints
cegar5_<tag>.subset.json): window-3 k=8 (cegar5_k8_w3_b.log), window-2 k=9 resumed (cegar5_k9_w2_b.log). Memory: keep <= 2
runs (cgroup ~16 GB; a run with 20e6 clauses reaches 8 GB). If both finish, add them to report §4 and push.
Open: uniform O(n) construction (would refute T-L1), or a proof of super-linearity for n >= 6 (no search possible there).

## Queue
1. n = 5: B_1(5) = 8 or > 8 (cegar5.py). 2. If = 8: look for the uniform O(n) construction (report §3 has the n=4 chain).
3. Report §4-5; message Lead. 4. Later: two-player Büchi B_2(n) at n = 4 (Q_4 two-player ~ 10^5-10^6 classes; not built yet).

## Things only I know
- The ANP asymmetric algorithm (Lemma 3.6) is a worklist, hence adaptive; the T7 reading "C(n,d) ≤ n^{lg(d/lg n)+O(1)}"
  for SLPs is not established by ANP's text. The symmetric recursion (Lemma 3.2) IS straight-line: |U|·|V| queries.
  CDHS 1909.04983 Algorithm 1 is also a worklist (popActiveSet). Both checked in the opened PDFs.
- With the "successor priority" query f'(x) = Cpre_E(∪_p P_p ∩ x_p) each ANP query is one Cpre gate; with the vertex-priority
  form g(x) = ∪_p P_p ∩ Cpre_E(x_p) it is d+1 gates. Exponent unchanged. Equivalence with W_E: standard, no primary source opened.
- SAT trick: UNSAT on a successor-closed subset of the quotient is a valid lower bound; the n = 4 UNSAT at k = 5 is on a subset.
- vec5.py packs sets as k-bit masks per game; the full 5-vertex sweep of a 25-gate program takes ~10 min; W per pattern cached.
- The two-player quotient for n = 4 was not built (13·10^6 games; memory ~ fine but slow); not needed for L1.
- Depth theorem's off-by-one: proof gives 2n-1, data says 2n-2 is exact for n ≤ 4.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| Chatterjee-Dvořák-Henzinger-Loitzenbauer, arXiv 1711.09148 v1 (SODA 2018) | §1 p.1-2 model and the "2n one-step operations" remark; §2 Preliminaries (Pre/Post, Set Disjointness, Thm 2.1); Reduction 3.1; Lemma 3.4 (O(1) bits per one-step op); Reduction 3.9 (p.7); Thm 3.10 (p.7) and its proof (p.13); Thm 3.11; §4 upper bounds (Büchi O(min(SCC+D, |T|·D))) | 2026-10-14 | pdftotext of arXiv v1 PDF; Reduction 3.9 graph has out-degree ≥ 1 everywhere |
| Arnold-Niwiński-Parys, LIPIcs.CSL.2021.9 (DOI 10.4230/LIPIcs.CSL.2021.9) | §2 fixed-point expressions, f_{A,B}, trees, Prop. 2.5 (S_{n,h} universal, width n^{lg(h/lg n)+O(1)}); §3.1 definition of ‖F‖_{U,V} (cases (1)-(3)), Lemma 3.1, Lemma 3.2 (|U|·|V| queries), Remark 3.3; §3.2 Algorithm 1, Lemma 3.4, 3.5, 3.6 (worklist, |V| to |V|(1+nd) queries), Cor. 3.7; Thm 5.1; Remark 5.5 | 2026-10-14 | DROPS PDF; intro p.9:2 states the symmetric bound n^{2·lg(d/lg n)+O(1)} explicitly |
| Bradfield-Walukiewicz, "The mu-calculus and model-checking", Handbook of Model Checking (author copy www.labri.fr/perso/igw/Papers/igw-mu.pdf) | formula (1), p.19 (after Theorem 7): μZ_{2d+1}.νZ_{2d}...νZ_0.γ with γ = ∧_i (p_i ⇒ (p_Eve ∧ ⟨b⟩Z_i) ∨ (p_Adam ∧ [b]Z_i)); Acc = limsup even (p.13) | 2026-10-15 | unnumbered display; typo γ(Z_0..Z_d); used for Transfer 2.4's vertex-priority form |
| Emerson-Jutla-Sistla, TCS 258 (2001) 491-522 (people.irisa.fr/Nicolas.Markey/PDF/Papers/tcs258(1-2)-EJS.pdf) | Theorem 3.2 (parity tree automaton emptiness as μ-calculus model checking), Lemma 3.5 | 2026-10-15 | numbered primary statement for the nested-fixpoint characterisation (automata form; index convention shifted) |
| Chatterjee-Dvořák-Henzinger-Svozil, arXiv 1909.04983 v1 | Algorithm 1 (black-box set-based progress measure), lines 3-16: worklist (popActiveSet) | 2026-10-14 | adaptive; used only for the CAUTION in Transfer 2.4 |
| REFEREE report R-L1 (claude/referee 9b01cbb, docs/referee/2026-10-14-L1-statement-check.md) and L-LIT T9 (trunk 735a4c7, docs/lit/T9-L1.md) | findings 1-9, gaps G1-G6; T9 (a), (b) | 2026-10-15 | fleet documents, not sources; drove v2 of the statement |

## Dead ends
(none)
