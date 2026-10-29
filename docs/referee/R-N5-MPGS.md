# R-N5-MPGS: REFEREE report on packet P-N5-MPGS (L-LIT: Part (A) Lemma MATCH-Φ and its Corollary; Part (B) Lemma GATE-SHUT and its Corollary)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). FIRST referee (Lead messages of 2026-10-29 11:13Z and 11:27Z by date -u:
MPGS supersedes P-N5-MATCHPHI; ignore the crossed "WITHDRAWN" in P-N5-MPGS-fixes.md F1; P-N5-GATESHUT 1298d8b2 is a verbatim copy of (B)).
- Object and pin: docs/lit/P-N5-MPGS.md, sha1 24913a7f9efea437aa202b398113b7ce12890961, 246 lines: the same sha1 at l-lit a23179b0 (an ancestor of
  origin/claude/l-lit). Quote base 1f15c91b.
- Process note: I read the 11:13Z correction only at 11:28Z, after my MATCHPHI report and a handover were pushed (2f2c40dc). That report
  (R-N5-MATCHPHI.md) stays as the review of the superseded packet; this report carries its verdicts over to Part (A) after a diff (§1).
- Runs 2026-10-29T11:35Z-11:41Z; report written 2026-10-29T11:44Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independence: no docs/referee-2/ MPGS file on my tree; 16 names matching "mpgs" on origin/claude/referee-2 at 11:42Z (names only, none
  opened). REFEREE-2's R2-N5-MATCHPHI.md exists (Lead 11:27Z); not opened.
- Pinned lane checks, re-run (read first) from a clean worktree at a23179b0, all EXACTLY as the packet prints:
  - P-N5-MPGS-quotecheck.py (sha1 74dbe8b4…): "quotes=9 bad=0". My own scratch/flip_quotes.py: QUOTES 9 FAILED 0.
  - T33-match-phi-check.py (sha1 6853179b…): "A: improving pairs 80640 | matched with phi rise < 1: 0 | carries: 32534" (Part B as in MATCHPHI).
  - T34-gateshut-check.py (sha1 7c33508b…): the four printed lines (3 0 0: 135 / 135 / 0 / 0, 0; 3 200 3: 14385 / 14217 / 0 / 102, 0; 4 100 4:
    12045 / 11911 / 0 / 97, 0; 5 30 5: 5783 / 5705 / 0 / 48, 0) and the S3 + F runs n = 4, 5, 6, 8: 228, 350, 510, 872 gate-states, all with
    (H1), (H2), 0 violations, 0 flips. Note (MPGS-N4): T34 imports L-COMP's hn.py, census.py, n5b.py from a hard-coded ROOT (the current
    checkout, not the freeze commit), and tests (H1) only as rank(d1) > rank(c_h).
- Own checks: scratch/matchphi_probe.py, mp_chain.py (Part (A); see R-N5-MATCHPHI.md) and scratch/gateshut_probe.py (sha1 84a77eb7…; Part (B) on
  EVERY game with my engine rl_engine; no L-COMP / L-LIT import). H_n was exported once to plain .pg data with L-COMP's hn.build (read-only;
  scratch/gs_inputs/hn_fig_n3..n6.pg, sha1 114eb83a / bb926586 / ebb3d976 / 07b405e4) and then run only on my engine. Logs scratch/gs_logs/.

## Verdicts
| § | item | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| A0 | definitions (R_c, K, pos, w, Φ, MATCHED (M1)-(M3), CARRY, NM, PCH) | CHECKED (as in MATCHPHI) |
| A2 | Fact A1 | SIGNED |
| A2 | Lemma MATCH-Φ | SIGNED |
| A2 | Added statement (A): PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) | SIGNED (proof condensed; MPGS-N1) |
| A2 | "Uses: … does not use (MON) or TOP-SHAPE" | TRUE (and now says Fact A1 uses only DELTA: my MATCH-N1 is resolved) |
| B0-B1 | definitions (G^d, Ξτ, τ̄, ⊴, ⊴_d, Iτ, plays as lassos, V^d, gate e / h / d, route π, Q, ρ, c_h, (H1)-(H3)) | CHECKED |
| B1 | Fact B1 (equal cycle nodes: X ◁_d X′ iff X′ ◁ X) | SIGNED |
| B1 | Fact B2 ((VJ) on G^d: Ξτ(x) ⊴_d V^d_{τ,σ′}(x)) | SIGNED |
| B2 | Lemma GATE-SHUT (steps 1-6) | SIGNED |
| B2 | Added statement (B): (H1)-(H3) on a stretch with τ(e) = h ⇒ (e, d) ∉ Iτ there and τ never moves h → d at a transition from it | SIGNED |
| A3, B3 | pinned checks (DATA) | reproduced exactly (above); not signed |
| A4, B4 | READINGs | not signed |
No gap. Notes MPGS-N1..N5 (and MATCH-N2..N4 of R-N5-MATCHPHI.md carry over to Part (A)). Nothing here bounds NM or any count of N5; not M3, not a
step-4 pass, not a TARGET.md claim; G-N5-TIME stays OPEN.

## 1. Part (A): diff against P-N5-MATCHPHI, and verdicts carried over
- Diff (normalised text of the statements and proofs, MATCHPHI §2 vs MPGS A2; similarity 0.12, i.e. reworded): the definitions of MATCHED,
  (M1)-(M3), pos, w, Φ are the same; the statements are the same, except that (i) Fact A1's statement drops MATCHPHI's last sentence ("So a MATCHED
  change is one that decomposes into …"), which the to-sign table still carries; (ii) the added statement drops the "≤ (n²/2)(NM + 1) + NM" form.
  The proofs are reworded; the Lemma's regrouping is identical in content.
- So the text is NOT identical, but the content is: my MATCHPHI verdicts (Fact 1, Lemma, Corollary SIGNED; definitions CHECKED) carry over to Fact
  A1, MATCH-Φ and (A), re-read in their MPGS wording. All data of R-N5-MATCHPHI.md apply unchanged (exhaustive K = 6, 7: 258,048 + 2,080,768 pairs,
  0 failures; arbitrary sequences; N5 data; W tight for abstract all-matched chains).
- MPGS-N1 (A's proof, condensed). "Each carry moves Φ by ≤ W. So #MATCHED ≤ W + W·NM" skips the step that makes it valid: the total rise R and the
  total fall F satisfy R − F = Φ(end) − Φ(start) ≤ W, falls occur only at carries (F ≤ W·NM), and #MATCHED ≤ R. MATCHPHI's proof had it. Wording;
  the conclusion stands. Also "width W ≤ K(K+1)/2" is an equality.

## 1b. The λ-run question (Lead 11:41Z): does MATCH-Φ's Corollary hold verbatim on any stretch with c = λ(v) fixed?
- YES (Opus 5.5, D15), verbatim, on ANY sequence of consecutive states (phase, λ-run with τ free, or any stretch, fallbacks included) on which
  v's own cycle node c = λ(v) is constant. Step by step, the proof reads: (1) R_c, hence pos, w, Φ and W: functions of c and of the global ranks
  only; (2) P_t ⊆ R_c at every state of the stretch (S1: P is the set of play vertices above the cycle node, and c is fixed); (3) for each
  P-change, the MATCHED / CARRY split, a property of the pair (P_t, P_{t+1}) alone; (4) the counting (rise ≤ W + fall, falls only at carries). No
  step reads τ, the phase, (MON) or the direction of the weight change. (Even only λ(v) for the single vertex v is needed, not all of λ_Ξ.)
- What does NOT carry over without more: nothing in the Corollary. Only the READING "a carry is an improving change that does not decompose"
  needs the weight to rise at every P-change; on a λ-run that still holds (Ξ is non-decreasing at every N5 iteration, R15 (a), (d), since Ξσ
  depends on σ alone, and c fixed makes the weight decide), but the Corollary does not use it.
- Data: the Corollary on arbitrary subset sequences (R-N5-MATCHPHI.md §3: 5,000 arbitrary + 5,000 increasing sequences, 0 failures), and on N5
  runs split into λ-runs (λ_Ξ constant, τ free; scratch/matchphi_probe.py LAMRUN=1): lib41, 38,243 (vertex, λ-run) checks, 31,662 P-changes,
  16,291 carries, 0 failures (mp_logs/lamrun_lib41.txt). The L-RED λ-run batch was stopped unfinished (too slow), recorded.

## 2. Part (B): GATE-SHUT re-derived
- Setting ✓. Ξτ is S1's valuation of τ on G^d, realised by τ̄ (an Even strategy of G) at every vertex at once, so Ξτ(x) = V^d_{τ,τ̄}(x) ✓. Iτ per
  S2 on G^d ✓. π_1 = d is Even (π consists of Even vertices), so the Lemma speaks only of Even d. (H2) gives h ∉ Q (ρ starts at h) — the packet
  uses this implicitly in step 3 ("τ(e) = h, then step 2").
- Fact B1 ✓. [A3]: same ranks on G^d; p′ and p′_d are both 2·rank + (0 or 1), so the most relevant cycle vertex is the same (maximal rank) and P is
  the same set; G^d's signed weight is −weight (Ω + 1 flips every sign); with equal cycle nodes and P ≠ P′ both orders decide on the weight. ✓
  Data: 3,712,665 pairs of dual valuations with equal cycle nodes at visited states: 0 failures.
- Fact B2 ✓: R57 (a) (VJ) "on every game", instantiated on the parity game G^d with G^d's Even strategy τ and its Odd strategy σ′ (a G-Even strategy).
- Step 1 ✓ (σ′ is τ̄ with the route forced; edges exist). Step 2 ✓: ρ avoids Q (H2), σ′ = τ̄ off Q, Odd vertices follow τ. Step 3 ✓: the play from
  d is π, e, then h's play ρ; π·e is simple and disjoint from ρ (H2), so the cycle and its node c_h are ρ's; every vertex of Q ranks above c_h (H1),
  so the set is P(ρ) ∪ Q (disjoint union), length ℓ(ρ) + |Q| (m + 1 steps from d to h). Step 4 ✓: the sets differ by Q, whose top rank is even
  (H3) and lies in the larger set, so DELTA gives a weight rise; same cycle node, so Ξτ(h) ◁ V, and V ◁_d Ξτ(h) by Fact B1. Step 5 ✓ (Fact B2 at d).
  Step 6 ✓: Ξτ(d) ⊴_d V ◁_d Ξτ(h), so (e, d) ∉ Iτ by S2.
- Added statement (B) ✓: the first claim is the Lemma per state. At a transition from t, τ_{t+1}(e) ∈ {τ_t(e)} ∪ {w : (e, w) ∈ Iτ_t}: S4b's arena
  keeps only those edges at e (or S4b is skipped when Iτ = ∅), S4c's Odd fallback picks from Iτ_t(e) or keeps τ_t(e), an Even fallback keeps τ (FIX
  3), S4a does not touch τ. d ≠ h and d ∉ Iτ_t(e). ✓ "What is not claimed" (persistence of (H1)-(H3)) ✓.
- Data (my engine, every visited state, every Odd e, every d ≠ τ(e), a DFS for ANY Even route satisfying (H1)-(H3), budget 4,000 nodes):
  | set | runs | (e, d) pairs | states with a route ((H1)-(H3)) | of them m ≥ 2 | Corollary checks | failures |
  | --- | --- | --- | --- | --- | --- | --- |
  | H_3, H_4 (Friedmann, exported; S3 + 3 random) | 8 | 915 | 761 | 761 | 733 | 0 |
  | H_5, H_6 | 8 | 1,983 | 1,722 | 1,722 | 1,678 | 0 |
  | lib1140 (n ≤ 40; given + S3 + 1 random) | 1,857 | 334,123 | 10,198 | 5,996 | 9,052 | 0 |
  | lib41 (n ≤ 48; given + S3 + 2 random) | 1,076 | 198,065 | 7,857 | 4,248 | 6,825 | 0 |
  | random rand_ck (n 5-16, k ≤ 5) | 12,000 | 176,427 | 1,949 | 724 | 1,196 | 0 |
  At every hit also step 4 (V ◁_d Ξτ(h)) and Fact B2 (Ξτ(d) ⊴_d V, V computed from the deviation's play on G^d): 22,487 checks, 0 failures. The Lemma
  thus holds well beyond Friedmann's gadgets, on every game of the corpora.
- Mutation controls (scratch/gs_logs/mut*.txt: H_3, H_4 + 150 lib41 games):
  | MUT | hypothesis dropped from the route search | result |
  | --- | --- | --- |
  | 1 | (H3) (top of Q even) | BITES: Lemma 240, Corollary 89 |
  | 2 | (H2) (ρ avoids Q) | does NOT bite (8,975 relaxed hits, all still shut) |
  | 3 | (H1) (Q above c_h) | BITES: Lemma 576, Corollary 66 (on H_3 too: the packet's B3 "flips occur where (H1) or (H2) fails") |

## 3. Notes (for L-LIT's fixes file; none changes a verdict)
- MPGS-N1: Part (A)'s Corollary proof is condensed past the rise/fall summation (§1). Restore MATCHPHI's three lines.
- MPGS-N2: step 3 uses h ∉ Q (from (H2), since ρ starts at h) and that d is Even (π_1 = d); say both.
- MPGS-N3 (thin spot): dropping (H2) did not produce a reopened gate in my data (MUT=2); (H2) is used in steps 2-3 and stays a hypothesis, but its
  necessity is not exhibited (the packet's B3 lumps (H1) and (H2) failures together).
- MPGS-N4 (B3 DATA): T34-gateshut-check.py imports L-COMP code from a hard-coded ROOT, i.e. the working tree at run time, not the freeze commit; and its
  (H1) test is rank(c_h) < rank(d1), not "every vertex of Q". On H_4 d1 is the lowest-ranked vertex of each gate's Q (ranks d1 < d2 < d3 < e, checked for all four gates), so the test is exact there; say so in B3.
- MPGS-N5 (process): MATCHPHI's notes MATCH-N2 (MATCHED ⇒ weight rise), N3 (L-COMP's "31 on alt_all" not reproduced) and N4 (W tight for abstract
  chains) apply to Part (A) unchanged; MATCH-N1 is resolved by MPGS's "Uses" line.

## DONE / FINDINGS / NEEDS
- DONE: R-N5-MPGS.md (this file), scratch/gateshut_probe.py, scratch/gs_inputs/ (H_n exports), scratch/gs_logs/; pinned checks re-run (exact).
- FINDINGS: Part (A) = MATCHPHI's content (text reworded, not identical); all items SIGNED, no gap. Part (B): Facts B1, B2, Lemma GATE-SHUT and statement
  (B) SIGNED, no gap; verified on every game of my corpora (22,487 hits, 0 failures); (H1), (H3) needed (MUT 3, 1 bite); (H2)'s need not exhibited.
- λ-run question: the Corollary holds verbatim on any stretch with λ(v) fixed (§1b), so on λ-runs; no extra step needed.
- NEEDS: Lead: the MPGS §C word when REFEREE-2 reports (successor 18 if I have handed over); route MPGS-N1..N5 to L-LIT.
