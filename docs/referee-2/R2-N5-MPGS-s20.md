# R2-N5-MPGS-s20: REFEREE-2 (successor 20) report on packet P-N5-MPGS (L-LIT): (A) Lemma MATCH-Φ (carried over from P-N5-MATCHPHI), (B) Lemma GATE-SHUT
Referee: REFEREE-2 successor 20, Opus 5.5 (D15, L37). Written 2026-10-29 from 11:20Z (date -u).

**Object.**
- docs/lit/P-N5-MPGS.md, sha1 24913a7f9efea437aa202b398113b7ce12890961, 246 lines, at l-lit freeze a23179b01be61d7f85e37aa93c0ae55a2dde7de8.
  Measured with `git show a23179b0:<path> | sha1sum`; equal to the Lead's figure.
- Superseded packet, for the diff: docs/lit/P-N5-MATCHPHI.md @ 12b7d12a, sha1 544705b7… (measured; equal to the Lead's).
- Pinned scripts, measured at a23179b0 and equal to the Lead's figures:
  - docs/lit/T34-gateshut-check.py 7c33508b2ef6639da2ce736028bcf013f152ed75;
  - docs/lit/P-N5-MPGS-quotecheck.py 74dbe8b4e6c4f37d4fdf7ca587eb479b5434579f;
  - docs/lit/T33-match-phi-check.py 6853179bf10bdf1c3d9cae61c939b1054aa4b70c.

**Independence.**
- I have not opened any file under docs/referee/ and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic mpgs` = 0 at 11:33:19Z (after `git fetch origin
  claude/referee`); 0 at 11:36:04Z (push turn, after a fresh fetch). Names only.
- The lane's three scripts were READ, then RUN as the pinned re-runs the Lead asked for. They ran with `python3 -I` in a detached worktree
  at a23179b0 (scratchpad). Output: R2-N5-MPGS-s20/logs/pinned_check.txt. They were never imported.
- My control is my own code: R2-N5-MPGS-s20/gs_check.py, on my lane's SPEC loop R2-N5-DUAL/dual_check.Runner and on si.py (SPEC S1's own
  implementation, read-only). Every quantity in it is written from the packet's B0 definitions. L-COMP's n5b and hn.py are not imported.
  Quotes are checked with my ../R2-N5-CORE/qcheck.py.

**Two REFEREE-2 reports on this packet (stated for the Lead).** Successor 19 (the previous REFEREE-2 session) also reviewed P-N5-MPGS and
pushed docs/referee-2/R2-N5-MPGS.md + R2-N5-MPGS/ (0c4524f0, 11:25:57Z; merge 52789f42). I found it only when my push was rejected at 11:37Z.
This report was written before I saw it and without reading it; I have not read it since. So my files are at -s20 paths. Which report
counts as REFEREE-2's is the Lead's call. The two do not share code (mine: gs_check.py; succ. 19: gateshut_check.py).

**Scope (D1).**
- (A) reduces the path-set changes of one vertex in one phase to its carries NM. NM is not bounded (OPEN).
- (B) is a structural lemma on Odd's improving edges. It bounds no count.
- Not a TARGET.md claim. No running time. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| A0 | definitions P_t ⊆ R_c, K, pos, w, Φ, MATCHED (M1)-(M3), CARRY, NM, P-change | SIGNED (identical in content to MATCHPHI §0-§1, signed 5ba3e21d; the new one-line justification of P_t ⊆ R_c is correct, §1) |
| A2 | Fact A1 | SIGNED (carried over: same statement and proof as MATCHPHI Fact 1; wording compressed) |
| A2 | Lemma MATCH-Φ | SIGNED (carried over: same statement and proof) |
| A2 | **Added statement (A)**: PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v), per vertex per phase, every game | SIGNED (carried over: MATCHPHI's Corollary minus its weaker "≤ (n²/2)…" tail) |
| A2 | "Uses" line (Fact A1 uses [DELTA]; not (MON), not TOP-SHAPE) | CORRECT. It repairs my predecessor's N-MP-1 |
| B0 | definitions G^d, Ξτ, τ̄, ⊴ / ⊴_d, Iτ, plays as lassos, V^d, gate e/h/d, π, Q, ρ, c_h, (H1)-(H3) | SIGNED (well formed; Q's vertices are distinct; Ξτ(x) = V^d_{τ,τ̄}(x) is SPEC S1-val's definition: N-GS-1) |
| B1 | Fact B1 (equal cycle nodes, P ≠ P′: X ◁_d X′ ⇔ X′ ◁ X) | SIGNED (and it holds without the restriction: N-GS-2) |
| B1 | Fact B2 ((VJ) on G^d) | SIGNED (a correct instantiation of RESULTS R57 (a), "on every game") |
| B2 | Lemma GATE-SHUT: τ(e) = h, (H1)-(H3) ⇒ (e, d) ∉ Iτ | SIGNED. Every step checked (§2), and each step is also checked mechanically (§3: GS2-GS5) |
| B2 | **Added statement (B)**: (H1)-(H3) at every state of a stretch with τ(e) = h ⇒ (e, d) ∉ Iτ there and τ never moves h → d at a transition from it | SIGNED (S4a, S4b, S4c and FIX 3 checked against SPEC, §2.7) |
| B2 | "What is not claimed" | CORRECT. (H1)-(H3) are state-dependent; reopenings in B3 are (H1)/(H2) failures |
| A3, B3 | pinned checks | DATA, not signed. Reproduced EXACTLY (§3.1) |
| A4, B4 | readings | READING, not signed |

No gap. No item FALSE. Notes N-GS-1..5 (§4).

## 1. Part (A): the diff against P-N5-MATCHPHI
Method: I read both texts side by side (MATCHPHI 133 lines; MPGS Part (A) lines 61-132). The texts are not byte-identical (the packet
re-states them), so I compared each item. Each verdict carried over is marked as such.

| MPGS (A) item | MATCHPHI item | difference | review |
| --- | --- | --- | --- |
| A0 setting and symbols | §0 setting, §1 definitions | Same objects and definitions. New: an explicit reason for P_t ⊆ R_c from [S1-rank]. Before, that line was cited from R84's setting (quote 4960) | The reason is correct. p′ = 2·rank + (0 or 1) and ranks are distinct integers, so rank(u) > rank(c) ⇒ p′(u) ≥ 2·rank(c) + 2 > p′(c). Conversely, rank(u) < rank(c) ⇒ p′(u) ≤ 2·rank(c) − 1 < p′(c). c = λ(v) is fixed on 𝒫 by [PHASE]. Verdict carried over |
| Fact A1 | Fact 1 | Statement and proof are the same. "≥ \|w(o)\| ≥ w(o)" is shortened to "≥ w(o)". The "so a MATCHED change is …" sentence moved into the to-sign table | Same content. Verdict carried over. N-MP-3 (additivity, one line) still applies to the table's wording |
| Lemma MATCH-Φ | Lemma MATCH-Φ | Same. The proof is written as one displayed sum | Same. Verdict carried over |
| Added statement (A) | Corollary | Drops the weaker tail "≤ (n²/2)(NM + 1) + NM". The proof is compressed (Φ changes only at P-changes is left implicit) | Same bound and proof. Verdict carried over |
| "Uses" line | premise sentence | Now "Fact A1 also uses [DELTA]. It does not use (MON) or R84's TOP-SHAPE" | Correct. This is exactly N-MP-1's repair |
| A3 DATA | §3 DATA | The alt_all "31" line and "pl130 157 = 41 + 116" are gone. It now says "at most 62 (n 581), max NM/n 1.18 (pl130_n40)" | DATA, not signed. Now consistent with my predecessor's N-MP-4 (62) |
| A4 READING | §4 READING | Shorter | Not signed |

Re-runs: T33-match-phi-check.py reproduces the packet's 9 output lines exactly (logs/pinned_check.txt). My predecessor's
R2-N5-MATCHPHI/mphi_check.py comb 6 was re-run (logs/carry_comb6.txt): same final lines as its 5ba3e21d log (TIGHT_K6 (21, 21, 63), 0 violations).
The predecessor's notes stand as follows. N-MP-1 is repaired. N-MP-2 (first term sharp at NM = 0), N-MP-3 and N-MP-5 still apply.
N-MP-4 is moot: the line it was about is gone.

## 2. Part (B): proof check of Lemma GATE-SHUT
Premises opened at the quoted commit, 9/9 quotes OK (logs/quotes.txt; SHIFT=1 control: 0/9 OK, so the checker bites). I also read SPEC
S1-S5 with FIX 1-4 in full at 1f15c91b (docs/new/N5-ssi-global.md l. 1-90), and RESULTS R57 (a), (b) at l. 2900-2918.

**2.0 Definitions (B0).**
- G^d's ranks are G's ([A3]). So p′_d(u) = 2·rank(u) + ((Ω(u) + 1) mod 2). On every cycle the maximal-p′ vertex is the same vertex in G and
  in G^d, so plays have the same cycle node and the same P in both readings.
- Q's vertices are distinct: the π_k are distinct Even vertices and e is Odd.
- "Ξτ(x) = V^d_{τ,τ̄}(x) by definition" is SPEC S1-val ("valuation of v under (σ, σ̄)" is the play value; Ξσ is it with σ̄ optimal). That
  the S1 procedure returns this play value is the standing premise of R57 (b) (SPEC conformance). See N-GS-1 and the ENGXI data.

**2.1 Fact B1.**
- G^d's signed weight of P is Σ ±2^rank with the sign of Ω + 1, which is −weight(P).
- Equal cycle nodes tie on reward, so both orders go to P. Since P ≠ P′, ℓ is never reached.
- Hence X ◁_d X′ ⇔ −weight(P) < −weight(P′) ⇔ X′ ◁ X. Correct.
- Checked on 76.3M random pairs (B1_pairs summed over the logs) with si.py's keys on G and on G^d (B1 counter in every log): 0 violations.

**2.2 Fact B2.**
- R57 (a) reads: "for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v)", on every game. It is read from VJ00
  "every finite game graph".
- On G^d: the "Even" strategy is τ and the "Odd" strategies are G's Even strategies σ′. Ξ there is SPEC's Ξτ (SPEC: "everything on the DUAL
  game"). The order there is ⊴_d.
- The instantiation is exact. It needs no restriction on priorities (G^d's start at 1). Correct.

**2.3 Step 1 (σ′).**
- σ′(π_k) = π_{k+1} and σ′(π_m) = e are edges of G, by the definition of π. The π_k are Even vertices of G.
- τ̄ is an Even strategy of G. So σ′ is a positional Even strategy that differs from τ̄ only on {π_1, …, π_m}. Correct.

**2.4 Steps 2-3 (the use of (H2)). Pressed as the Lead asked.**
- Step 2. The plays from h under (σ′, τ) and under (τ̄, τ) agree as long as they visit no vertex where σ′ ≠ τ̄. The only such vertices
  are π_1..π_m. ρ (prefix and cycle) visits none of them by (H2). By induction on the step, π(h; σ′, τ) = ρ, cycle included. Correct.
- Step 3. From d = π_1, σ′ walks π_1 → … → π_m → e. Then τ(e) = h, and from h the play is ρ (step 2).
  - Lasso shape: the vertices π_1..π_m, e are distinct, and none lies on ρ by (H2). So the first repeated vertex is the one where ρ itself
    closes its cycle.
  - The play from d has the prefix π·e·(ρ's prefix) and ρ's cycle. Its cycle node is c_h.
  - The vertices of π·e come before c_h is reached, so they enter P exactly when rank > rank(c_h). That holds for all of them by (H1).
  - (H2) also gives Q ∩ P(ρ) = ∅. ℓ = ℓ(ρ) + m + 1 = ℓ(ρ) + |Q|.
  - So V = (c_h, P(ρ) ⊔ Q, ℓ(ρ) + |Q|). Correct.
- What (H2) buys. Without it, σ′ could change ρ itself (step 2), or the walk along π could merge into ρ and close a different cycle
  (step 3). Both uses are needed by THIS proof. Whether the Lemma needs (H2) is another question; see N-GS-3.
- Also, (H1) already excludes e ∈ ρ. If ρ reached e, it would continue e → h, so e would lie on ρ's cycle and rank(c_h) ≥ rank(e),
  against (H1). So (H2) only adds that ρ avoids π.

**2.5 Step 4 (the use of (H3)).**
- P(ρ) ⊔ Q and P(ρ) differ exactly by Q ≠ ∅. The top differing rank is top(Q). It is even by (H3) and lies in the larger set.
- [DELTA] gives weight(P(ρ) ⊔ Q) > weight(P(ρ)). [DELTA]'s parity is Ω in G (R84 F5), the same as (H3)'s.
- Same cycle node, so Ξτ(h) ◁ V in G's order. Fact B1 (P ≠ P′) then gives V ◁_d Ξτ(h). Correct.

**2.6 Steps 5-6 (the dual (VJ) step).**
- Fact B2 with x = d gives Ξτ(d) ⊴_d V^d_{τ,σ′}(d) = V.
- So Ξτ(d) ⊴_d V ◁_d Ξτ(τ(e)). ⊴_d is a total preorder (a lexicographic key), so Ξτ(d) ◁_d Ξτ(τ(e)) strictly.
- [S2] on G^d needs strictly ▷_d for (e, d) ∈ Iτ (e is G^d-Even, d ≠ τ(e)). So (e, d) ∉ Iτ. Correct.
- The dual step uses only Ξτ's minimality on G^d, i.e. that it is Even-of-G's best. It does not use that τ̄ is a one-step minimiser at
  every vertex: the DF / FIX 2 trap (RESULTS R27, "DF FALSE") is not touched. Lengths never decide anything in the proof.

**2.7 Added statement (B).** The SPEC text at 1f15c91b gives:
- S4b: τ_new is S1 on H′, where Odd's v keeps only the edges to A(v) = {τ(v)} ∪ Iτ(v). So τ_{t+1}(e) ∈ A(e). The case Iτ = ∅ gives
  τ_new = τ.
- S4c, Odd's fallback: it sets τ(v) to an improving w, for Odd v with improving edges only. FIX 3: when Even falls back, τ is unchanged.
- S4a leaves τ unchanged. S4 computes both steps from the SAME (σ, τ) = state t, so A(e) is built from Iτ_t.
- The Lemma at t gives d ∉ A(e), so τ_{t+1}(e) ≠ d. Correct.
- Only the hypotheses at the source state t are used, and π may differ from state to state (N-GS-4).

## 3. Re-runs and own control
**3.1 Pinned (logs/pinned_check.txt).**
- P-N5-MPGS-quotecheck.py: `quotes=9 bad=0`, as expected.
- T33-match-phi-check.py: the 9 expected lines, exactly.
- T34-gateshut-check.py:
  - all four expected lines exactly: (3 0 0) 135/135/0/0/0; (3 200 3) 14385/14217/0/102/0; (4 100 4) 12045/11911/0/97/0;
    (5 30 5) 5783/5705/0/48/0;
  - S3 + F for n = 4, 5, 6, 8: 228, 350, 510, 872 gate-states, all with (H1),(H2), 0 violations, 0 flips;
  - 102 + 97 + 48 = 247 flips, 0 of them with (H1),(H2). As in B3.
- T34 tests (H1) only as rank(c) < rank(d1_i), and (H3) not at all. Both are valid on H_n mode fig: hn.py l. 46-49 give
  d1_i < d2_i < d3_i < e_i (8i+1+off, 8i+3+off, 8i+5+off, 8i+6+off), so d1_i is Q's lowest vertex and e_i its top, with even priority.

**3.2 Own control: R2-N5-MPGS-s20/gs_check.py.** At every state, for every Odd e, every Even successor d ≠ τ(e) and every simple Even path π
from d into e (at most 64 per (state, e, d)), it tests (H1)-(H3). When they hold, it asserts:
- GS: (e, d) ∉ Iτ;
- the proof's steps on the actual plays: GS2 (ρ unchanged under σ′), GS3 (V = (c_h, P(ρ) ⊔ Q, ℓ(ρ) + |Q|) as a play value), GS4
  (V ◁_d Ξτ(h) and Ξτ(h) ◁ V), GS5 (Ξτ(d) ⊴_d V);
- GSC: the Corollary on the run's next state.
It also checks B1 on random pairs, and the premise ENGXI: the engine's Ξτ(v) equals the play value of (τ̄, τ) from v, at every vertex
of every state.

| run | states | (state, e, d) with (H1)-(H3) | (H1)-(H3) paths (steps checked) | ENGXI checks | violations (GS, GS2-5, GSC, B1, ENGXI) |
| --- | --- | --- | --- | --- | --- |
| random 3000 games n 5-14, S3 + 3 random starts, N5 runs | 31,735 | 1,523 | 1,711 | 313,300 | 0 |
| random 600 games n 15-24, S3 + 2 random starts | 6,240 | 419 | 462 | 122,480 | 0 |
| library lib41_noref (410 files), S3 + 1 random start | 14,145 | 6,017 | 11,963 | 696,332 | 0 |
| Friedmann H3-H6 (experiments/friedmann-hn/instances), S3 + 3 random | 585 | 2,348 | 2,348 | 57,792 | 0 |
| tau: 40000 games n 5-10, 10 arbitrary (σ, τ) each (the Lemma at any τ) | 400,000 | 6,174 | 7,249 | 3,000,270 | 0 |
| tau: 20000 games n 8-14, 5 arbitrary (σ, τ) each | 100,000 | 2,219 | 2,551 | 1,100,040 | 0 |
| alltau: 60000 games n 4-8, EVERY τ (≤ 256 per game) | 306,593 | 7,778 | 8,488 | 1,994,599 | 0 |
| alltau: 20000 games n 8-11, EVERY τ (≤ 256 per game) | 166,372 | 5,193 | 6,133 | 1,623,852 | 0 |

Every run: RESULT PASS. On the run-based rows, GSC = 0 and FLIPH = 0: no h → d move of τ at a state with an (H1)-(H3) path, out of
FLIP = 21,280 / 6,658 / 11,412 / 80 h → d moves in total.

**Controls (each hypothesis dropped alone; counted per (state, e, d) with no (H1)-(H3) path but a path failing only that hypothesis; the
count is how often (e, d) ∈ Iτ there):**
| run | X1 (only (H1) fails) | X2 (only (H2) fails) | X3 (only (H3) fails) |
| --- | --- | --- | --- |
| random n 5-14 | 499 of 5,998 | 0 of 73 | 246 of 799 |
| random n 15-24 | 207 of 2,546 | 0 of 18 | 47 of 225 |
| lib41 | 903 of 27,080 | 0 of 778 | 233 of 10,881 |
| H3-H6 | 32 of 32 | — | — |
| tau n 5-10 | 13,317 of 34,877 | 0 of 235 | 7,401 of 10,532 |
| tau n 8-14 | 5,189 of 14,394 | 0 of 118 | 2,005 of 3,165 |
| alltau n 4-8 | 11,354 of 31,919 | 0 of 220 | 7,572 of 10,575 |
| alltau n 8-11 | 9,315 of 26,931 | 0 of 206 | 4,883 of 7,225 |

So (H1) and (H3) are each needed: dropping either one alone gives improving gate edges. Dropping (H2) alone never did (N-GS-3).
Also run: b1_general.py (logs/b1_general.txt), 200,000 random valuation pairs with arbitrary cycle nodes, 0 violations (N-GS-2).

## 4. Notes (not gaps)
- N-GS-1 (standing premise, as in R57 (b)). Steps 2-4 identify Ξτ(h) with the value of the (τ̄, τ)-play ρ. That is SPEC S1-val's
  definition of Ξ. That the S1 procedure (si.py, n5b) outputs it is SPEC conformance, the same standing premise R57 (b) records ("that S1's
  procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance"). DATA: ENGXI held at every vertex of every state of my runs (§3.2
  column, 0 mismatches), including own cycle nodes.
- N-GS-2 (Fact B1, stronger). G^d's order is the exact reverse of G's on ALL valuations, not only on equal cycle nodes with P ≠ P′.
  - Rewards reverse: reward_d(c) = −reward(c) − 1. For even Ω, 2r becomes −(2r+1). For odd Ω, −(2r+1) becomes 2r.
  - Signed weights reverse, as in B1.
  - The length rule reverses, because c's parity flips.
  - Checked: logs/b1_general.txt. One line; the Lemma needs only the packet's B1.
- N-GS-3 ((H2) and the data). In every run, no gate edge became improving when only (H2) failed (X2 = 0 over 1,648 (H2)-only
  (state, e, d) triples, 426 of them under EVERY τ of their game; (H1) and (H3) each bite, X1, X3 > 0).
  - (H1) already gives e ∉ ρ (§2.4). So (H2) only adds "ρ avoids π".
  - Whether (H1) + (H3) suffice is OPEN. It is a possible strengthening for L-LIT, NOT claimed by the packet and NOT signed here.
  - My partial argument: when ρ meets π first at π_j, Even's deviation at h along π_j..π_m, e, h closes a cycle C′ above c_h. By (VJ)
    at h, top(C′) must be odd. Turning this into "Ξτ(d) ⊵ Ξτ(h)" needs a case split on where top(Q) and top(C′) lie, which I have not
    completed.
  - B3's sentence "The hypotheses are needed" is right for the hypotheses together and for (H1) alone. My data add (H3) alone, but not
    (H2) alone.
- N-GS-4 (reading of the Corollary). The stretch condition can use a different π at each state. At the transition t → t + 1 only the
  hypotheses at t are used. Worth one clause in RESULTS, since B4's reading ("(H2) holds along the runs") is a per-state statement.
- N-GS-5 (pinned T34 scope). T34 checks the Lemma on one gate path per gate (d1, d2, d3) of H_n only, and tests (H1) through d1_i alone.
  That is valid there (§3.1). The general form, with every π, every e and arbitrary games, is my gs_check.py.

## 5. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-MPGS-s20/{gs_check.py, b1_general.py, hn.lst, run_all.sh, logs/ (pinned_check.txt included)}.
- FINDINGS:
  - Part (A): the content is identical to MATCHPHI. All verdicts carried over SIGNED. N-MP-1 is repaired; N-MP-4 is moot.
  - Part (B): Fact B1, Fact B2, Lemma GATE-SHUT and Added statement (B) are all SIGNED, with no gap. (H2) is used correctly in steps 2-3.
    The dual (VJ) step is an exact instance of R57 (a).
  - The pinned checks reproduce exactly. My own control (every π, arbitrary games and τ, proof steps on actual plays) shows 0 violations.
  - (H2) never bit alone: a possible strengthening, OPEN (N-GS-3).
- NEEDS: Lead: route N-GS-1..5 to L-LIT (N-GS-3 is optional work). I write §C after REFEREE's report.
