# P-N5-MPGS fixes (L-LIT)
- F1 (2026-10-29 ~11:2xZ, Lead's message of 11:01Z): P-N5-MPGS (frozen a23179b0) is WITHDRAWN. The Lead routed P-N5-MATCHPHI
  (12b7d12a) to both referees and asked for GATE-SHUT as a separate packet. Part (A) = P-N5-MATCHPHI (same statements); Part (B) =
  docs/lit/P-N5-GATESHUT.md (verbatim, premises restricted). No statement changes. Referees sign P-N5-MATCHPHI and P-N5-GATESHUT.
- F2 (2026-10-29 ~11:3xZ): "Lead ruling 11:27Z: F1 withdrawn; P-N5-MPGS is the review object." P-N5-MPGS (a23179b0, sha1 24913a7f…)
  stands as frozen and is the packet under review (REFEREE-2 20 has diffed Part (A) against P-N5-MATCHPHI and is reviewing Part (B)).
  No statement changes.

## Referees' joint notes (appended 2026-10-29 from 12:33Z by date -u; L-LIT successor 2, Opus 5.5, D15/D18)
Both referees SIGNED every item of P-N5-MPGS (a23179b0, sha1 24913a7f…) with NO gap: REFEREE §C (docs/referee/R-N5-MPGS.md, referee
8da7b717) and REFEREE-2 §C (docs/referee-2/R2-N5-MPGS-C.md, referee-2 e1ec568a; reports of record R2-N5-MPGS.md 0c4524f0 and concurring
R2-N5-MPGS-s20.md). The frozen packet text is NOT edited. Each item below quotes the note(s) verbatim (checked by
docs/lit/P-N5-MPGS-fixes-quotecheck.py, whitespace collapsed; expected output at the end of this file), then gives either an appended
statement or "no change, because …". Labels: PROVED (L-LIT, unrefereed; the referees' notes ask for it) / DATA / READING / OPEN.
- Classing. REFEREE-2 classes C.4 items 1-5 as E (a text fix for this file); REFEREE: [Q docs/referee/R-N5-MPGS.md@8da7b7179:145-146] «- E-ITEMS (must change before landing): NONE. Every signed statement and proof is correct as frozen at a23179b0. The landing text should carry J6 (standing premise) and may carry J7, J8, J12 as referees' remarks; J1-J5, J13, J15 go to L-LIT's fixes file as optional.»
  Both agree no statement or proof changes. Lead reading needed only for the landing text; F3-F7 below are written as E items either way.
- Record (no action): REFEREE's §C says [Q docs/referee/R-N5-MPGS.md@8da7b7179:147-148] «- λ-runs (my §1b): the MATCH-Φ Corollary holds verbatim on any stretch with λ(v) fixed. REFEREE-2 did not address this question (it was asked of the first referee); nothing in either REFEREE-2 report contradicts it (N-MPGS-6: the Lemma uses no phase).» REFEREE-2's later §C (e1ec568a) does address
  it and agrees: [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:37-40] «**The λ-run question (REFEREE §1b; Lead 11:41Z).** REFEREE: the MATCH-Φ Corollary holds verbatim on any stretch with λ(v) fixed, so on λ-runs; no step reads τ or the phase. REFEREE-2 20 reached the same conclusion independently in R2-N5-COMPOSE §2.5 (pushed 4b8afa95 before §1b was read), and added that the Odd side reads parities on G^d (N-C3). REFEREE's λ-run data: lib41, 38,243 checks, 0 failures. Mine: 56,999 Even and 21,286 Odd (vertex, λ-run) pairs, 0 failures. Joint: AGREED. This is the premise P-N5-COMPOSE §6 needs.»

### F3. Part (A), Corollary proof: the rise/fall summation; W is an equality (C.4 item 1; MPGS-N1 = J4 = D1)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:65-65] «1. E: (A) Corollary proof: restore the rise/fall summation; write "W = K(K+1)/2" (D1).»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:99-99] «- MPGS-N1: Part (A)'s Corollary proof is condensed past the rise/fall summation (§1). Restore MATCHPHI's three lines.»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:132-132] «| J4 Corollary (A)'s proof skips the rise/fall summation (R − F = ΔΦ ≤ W, F ≤ W·NM, #MATCHED ≤ R) and leaves "Φ changes only at P-changes" implicit | MPGS-N1 | R2-20 §1 table ("proof compressed") | optional, recommended: the inference is valid as a sketch; restore MATCHPHI's three lines |»
- APPENDED PROOF of Added statement (A) (replaces nothing; to be read after A2's three-line proof). Fix v, 𝒫, c = λ(v). Write Φ_t := Φ(P_t).
  - W := max Φ − min Φ over subsets of R_c = Σ_{even r} pos(r) + Σ_{odd r} pos(r) = Σ_{k=1}^{K} k = K(K+1)/2 (an EQUALITY; the
    frozen "W ≤ K(K+1)/2" is true and not sharp in form only).
  - Φ_t changes only at P-changes (Φ is a function of P_t).
  - Let R := Σ of the positive increments Φ_{t+1} − Φ_t over the P-changes of 𝒫, and F := Σ of the absolute values of the negative
    ones. Then R − F = Φ_end − Φ_start ≤ W.
  - Every MATCHED change has increment ≥ 1 (Lemma MATCH-Φ), so it contributes ≥ 1 to R and nothing to F: #MATCHED ≤ R.
  - Negative increments occur only at carries, each of absolute value ≤ W: F ≤ W·NM_𝒫(v).
  - So #MATCHED ≤ R ≤ W + F ≤ W + W·NM_𝒫(v), and PCH_𝒫(v) = #MATCHED + NM_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v). □

### F4. Part (B), step 3: h ∉ Q and d Even (C.4 item 2; MPGS-N2 = J5 = D2)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:66-66] «2. E: step 3: state h ∉ Q (from (H2)) and that d = π_1 is Even (D2).»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:100-100] «- MPGS-N2: step 3 uses h ∉ Q (from (H2), since ρ starts at h) and that d is Even (π_1 = d); say both.»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:133-133] «| J5 step 3 uses h ∉ Q and d Even (π_1 = d) | MPGS-N2 | R2-19 §2 (Q distinct, π Even), R2-20 §2.4 | optional (wording) |»
- APPENDED CLAUSE to step 3 of GATE-SHUT's proof: "Here h ∉ Q, because ρ starts at h and (H2) says ρ contains no vertex of Q; so the
  play, after π·e, enters ρ at its first vertex h and then follows step 2. And d = π_1 is an Even vertex of G (π consists of Even
  vertices, B0), so σ′(d) = π_2 (or e if m = 1) is set by step 1." No statement changes.

### F5. B3 (DATA): T34's (H1) test via d1 is exact on H_n; T34's imports read the working tree (C.4 item 3; MPGS-N4 = J2 + J3, N-MPGS-2, N-GS-5, D3)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:67-68] «3. E: B3: T34's (H1) test via d1 is exact on H_n because d1_i is Q's lowest vertex (hn.py l. 46-49); pin or state T34's imports from the working tree (D3, C.2).»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:103-104] «- MPGS-N4 (B3 DATA): T34-gateshut-check.py imports L-COMP code from a hard-coded ROOT, i.e. the working tree at run time, not the freeze commit; and its (H1) test is rank(c_h) < rank(d1), not "every vertex of Q". On H_4 d1 is the lowest-ranked vertex of each gate's Q (ranks d1 < d2 < d3 < e, checked for all four gates), so the test is exact there; say so in B3.»
- [Q docs/referee-2/R2-N5-MPGS.md@e1ec568a4:111-115] «- N-MPGS-2 (the pinned T34 tests (H1) on d1 only). Its line `hyp = rank[c] < rank[d1] and not ({d1, d2, d3, e} & set(seen))` checks rank(c_h) < rank(d1), while the Lemma's (H1) asks it for every u ∈ Q = {d1, d2, d3, e}. - This is DATA, not to sign. It is the right test only if d1 has the lowest rank in each Friedmann gate. - My check takes the full Q on the same H_n instances, and found 0 violations, so the DATA conclusion is unaffected. The script's comment should say so.»
- [Q docs/referee-2/R2-N5-MPGS-s20.md@e1ec568a4:218-219] «- N-GS-5 (pinned T34 scope). T34 checks the Lemma on one gate path per gate (d1, d2, d3) of H_n only, and tests (H1) through d1_i alone. That is valid there (§3.1). The general form, with every π, every e and arbitrary games, is my gs_check.py.»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:130-131] «| J2 T34 tests (H1) through d1 only; exact on H_n since d1 < d2 < d3 < e in each gate (hn.py l. 46-49) | MPGS-N4 (second half) | N-MPGS-2, N-GS-5 | optional (DATA comment in B3) | | J3 T34 imports L-COMP code from a hard-coded ROOT (the working tree at run time, not the freeze commit) | MPGS-N4 (first half) | — (both ran it in a worktree; not raised) | optional (DATA reproducibility; one line in B3 or pin ROOT to the script's commit) |»
- APPENDED DATA NOTE to B3:
  - (H1) in T34. T34 line 35 tests `rank[c] < rank[d1]`. In H_n (experiments/friedmann-hn/hn.py l. 46-49) the gate vertices have
    priorities d1_i = 8i+1+off, d2_i = 8i+3+off, d3_i = 8i+5+off, e_i = 8i+6+off (off = −6 in mode fig, 0 otherwise), so
    rank(d1_i) < rank(d2_i) < rank(d3_i) < rank(e_i) and d1_i is the lowest-ranked vertex of Q = {d1_i, d2_i, d3_i, e_i}. Hence
    rank(c_h) < rank(d1_i) iff (H1) for this π. The test is exact on H_n; it is not a test of (H1) on other games. T34 checks one route
    (d1_i, d2_i, d3_i) per gate only; the general form (every π, every Odd e, arbitrary games) is in the referees' own checks
    (REFEREE scratch/gateshut_probe.py; REFEREE-2 gs_check.py), 0 failures.
  - Imports. T34 sets `ROOT = "/home/user/parity_games_challange"` (line 7) and imports hn, census, n5b from ROOT/experiments/{friedmann-hn,
    n5-epoch, n5-exhaustive, n5-second, harness, hard-families}, i.e. from the checkout at that path at run time, not from the freeze
    commit (also when T34 itself is run from a worktree). Measured 2026-10-29 12:3xZ: the git tree ids of these six directories are the
    same at the freeze commit a23179b0 and at trunk 923b5b12 (n5-epoch 3a595735, n5-exhaustive 516cf115, n5-second d097ed34, harness
    10ca616f, hard-families c3353706, friedmann-hn 8d5ff634; blobs at a23179b0: hn.py 6872b413, census.py 04e8e1c3, n5b.py 3c29263d).
    To reproduce B3 at the freeze, check these six tree ids in the checkout at ROOT first (`git rev-parse HEAD:experiments/<dir>`).
    The pinned script (sha1 7c33508b…) is not changed.

### F6. B3: which hypotheses are needed; (H2)'s necessity is not exhibited (C.4 item 4; MPGS-N3 = J1, N-MPGS-1, N-GS-3)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:69-70] «4. E: B3's "the hypotheses are needed" is true for (H1) and (H3) separately; (H2)'s necessity is not exhibited (C.2). opt: the OPEN question whether (H1) + (H3) suffice.»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:101-102] «- MPGS-N3 (thin spot): dropping (H2) did not produce a reopened gate in my data (MUT=2); (H2) is used in steps 2-3 and stays a hypothesis, but its necessity is not exhibited (the packet's B3 lumps (H1) and (H2) failures together).»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:129-129] «| J1 (H2) necessity not exhibited; (H1) alone already gives e ∉ ρ (if ρ reaches e it continues to h = τ(e), so e is on ρ's cycle and rank(c_h) ≥ rank(e), against (H1)); whether (H1) + (H3) suffice is OPEN | MPGS-N3 | N-MPGS-1, N-GS-3 | optional (a possible strengthening for L-LIT; not claimed, not signed). I checked the e ∉ ρ step: correct |»
- [Q docs/referee-2/R2-N5-MPGS.md@e1ec568a4:107-110] «- N-MPGS-1 ((H2)'s necessity is not exhibited). Where only (H2) fails, (e, d) was never improving in my data (0 of 15,528). (H2) is used in steps 2-3, so it stays. Data do not show it is needed. - (H1) and (H3) are needed: their controls bite (5,673 and 4,422 cases), including on H_n for (H1) (28 / 28). This matches §B3's example (a cycle node above the gate).»
- [Q docs/referee-2/R2-N5-MPGS-s20.md@e1ec568a4:207-215] «- N-GS-3 ((H2) and the data). In every run, no gate edge became improving when only (H2) failed (X2 = 0 over 1,648 (H2)-only (state, e, d) triples, 426 of them under EVERY τ of their game; (H1) and (H3) each bite, X1, X3 > 0). - (H1) already gives e ∉ ρ (§2.4). So (H2) only adds "ρ avoids π". - Whether (H1) + (H3) suffice is OPEN. It is a possible strengthening for L-LIT, NOT claimed by the packet and NOT signed here. - My partial argument: when ρ meets π first at π_j, Even's deviation at h along π_j..π_m, e, h closes a cycle C′ above c_h. By (VJ) at h, top(C′) must be odd. Turning this into "Ξτ(d) ⊵ Ξτ(h)" needs a case split on where top(Q) and top(C′) lie, which I have not completed. - B3's sentence "The hypotheses are needed" is right for the hypotheses together and for (H1) alone. My data add (H3) alone, but not (H2) alone.»
- APPENDED CORRECTION to B3's last bullet ("The hypotheses are needed: the unhypothesised form is false on these instances."): it is
  true of the three together, of (H1) alone and of (H3) alone; it is NOT exhibited for (H2) alone.
  - DATA (referees, three independent engines): dropping (H1) bites (REFEREE MUT 3: Lemma 576, Corollary 66, on H_3 too; REFEREE-2 19
    noH1 5,673 incl. 28 H_n gate-states; REFEREE-2 20 X1 > 0, 32 of 32 on H_3-H_6); dropping (H3) bites (MUT 1: Lemma 240, Corollary
    89; noH3 4,422; X3 > 0); dropping (H2) alone never bites (MUT 2: 8,975 relaxed hits, all shut; noH2 0 of 15,528; X2 0 of 1,648,
    426 of them under every τ of their game). B3's own flips (247) all fail (H1) or (H2); its example (rand4) fails (H1).
  - PROVED (L-LIT, unrefereed; REFEREE checked the step, J1): (H1) alone gives e ∉ ρ. If ρ visited e, it would continue to τ(e) = h,
    its first vertex, so e and h lie on ρ's cycle and rank(c_h) ≥ rank(e), against (H1) (e ∈ Q). So (H2) adds only "ρ avoids
    π_1, …, π_m".
  - OPEN (labelled CONJECTURE H2-FREE, not claimed, not signed): at a state with τ(e) = h, (H1) and (H3) imply (e, d) ∉ Iτ. Support:
    0 counterexamples in the three data sets above. Obstruction to the present proof: if ρ meets π (first at some π_j), the deviation
    σ′ of step 1 changes the play from h (step 2 fails): the play from h, and from d, ends in a new cycle C′ through π_j, …, π_m, e
    with top rank ≥ rank(e) > rank(c_h), so V^d_{τ,σ′}(d) no longer shares Ξτ(h)'s cycle node and step 4 does not apply. A proof
    needs another deviation or a case split on top(Q) vs top(C′) (REFEREE-2 20's partial argument, quoted above).

### F7. B4 (READING): "(H1) automatic" only where c_h is the sink (C.4 item 5; N-MPGS-4 = J9 = D4)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:71-71] «5. E: B4: "(H1) automatic" holds only where c_h is the sink (D4).»
- [Q docs/referee-2/R2-N5-MPGS.md@e1ec568a4:118-120] «- N-MPGS-4 (B4 READING, not signed). "(H1) is automatic in Friedmann's 1-sink games (the cycle node is the sink)" is consistent with my H_n data only where c_h is the sink. My noH1 control bites on 28 H_n gate-states, i.e. states where Ξτ(h)'s cycle node lies above the gate. These are the reopenings §B3 describes.»
- [Q docs/referee/R-N5-MPGS.md@8da7b7179:137-137] «| J9 B4 READING "(H1) automatic in Friedmann's 1-sink games" holds only where c_h is the sink; (H1) fails on some H_n gate-states | MUT 3 bites on H_3 (§2) | N-MPGS-4 | optional (READING, not signed) |»
- APPENDED CORRECTION to B4's first bullet (READING, not to sign): "In Friedmann's 1-sink games the cycle node of Ξτ(h) is the sink,
  below every gate, at the states where the (τ̄, τ)-play from h ends in the sink; there (H1) holds. It does NOT hold at every state:
  where Ξτ(h)'s cycle node lies above the gate (B3's rand4 example: c = e2 above gate 1), (H1) fails, and these are exactly the
  reopenings B3 observes (REFEREE-2 19: 28 H_n gate-states; REFEREE MUT 3 bites on H_3; REFEREE-2 20: X1 32 of 32 on H_3-H_6). Along
  the runs from S3 and F, T34 found (H1) and (H2) at every gate-state (B3: 228, 350, 510, 872 for n = 4, 5, 6, 8)." The rest of B4
  is unchanged.

### F8. Optional one-liners (C.4 item 6; D6/D7, J7, J8, N-GS-2, N-GS-4, N-MPGS-6, REFEREE §1b)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:72-73] «6. opt: the full order reversal (D7); the Corollary uses only the hypotheses at the source state, and π may vary (D6); MATCH-Φ's Corollary holds on any stretch with λ(v) fixed (§1b; worth one line in (A), since P-N5-COMPOSE §6 uses it).»
- (a) Full order reversal. [Q docs/referee-2/R2-N5-MPGS-s20.md@e1ec568a4:202-206] «- N-GS-2 (Fact B1, stronger). G^d's order is the exact reverse of G's on ALL valuations, not only on equal cycle nodes with P ≠ P′. - Rewards reverse: reward_d(c) = −reward(c) − 1. For even Ω, 2r becomes −(2r+1). For odd Ω, −(2r+1) becomes 2r. - Signed weights reverse, as in B1. - The length rule reverses, because c's parity flips. - Checked: logs/b1_general.txt. One line; the Lemma needs only the packet's B1.» [Q docs/referee/R-N5-MPGS.md@8da7b7179:135-135] «| J7 Fact B1 holds without its restriction: G^d's order is the exact reverse of G's on ALL valuations (reward_d(c) = −reward(c) − 1, weights negate, the length rule flips with c's parity) | — | N-GS-2 | optional (one line). I re-derived it: Ω(c) even, p′ = 2r → p′_d = 2r + 1, reward −(2r + 1); Ω(c) odd, −(2r + 1) → 2r; both = −reward − 1. Correct |»
  APPENDED REMARK after Fact B1 (referees' remark; REFEREE re-derived it, REFEREE-2 20 checked 200,000 pairs; L-LIT re-derives: on
  G^d, Ω + 1 flips the parity of every vertex and keeps ranks [A3], so reward_d(c) = −reward(c) − 1 (Ω(c) even: 2r ↦ −(2r+1); odd:
  −(2r+1) ↦ 2r), signed weights negate, and the ℓ rule's direction is chosen by c's parity, which flips): "For ALL valuations X ≠ X′,
  X ◁_d X′ iff X′ ◁ X. GATE-SHUT uses only the case of Fact B1."
- (b) Per-state reading of (B). [Q docs/referee-2/R2-N5-MPGS-s20.md@e1ec568a4:216-217] «- N-GS-4 (reading of the Corollary). The stretch condition can use a different π at each state. At the transition t → t + 1 only the hypotheses at t are used. Worth one clause in RESULTS, since B4's reading ("(H2) holds along the runs") is a per-state statement.» [Q docs/referee-2/R2-N5-MPGS.md@e1ec568a4:123-124] «- N-MPGS-6 (scope wording). The Lemma holds at any state of any N5 run, in-phase or not (it uses no phase). The added statement (B) is per transition. Both are stated that way; nothing to repair.»
  [Q docs/referee/R-N5-MPGS.md@8da7b7179:136-136] «| J8 the Corollary (B) uses only the hypotheses at the transition's source state; π may differ per state | §2 "the first claim is the Lemma per state" | N-GS-4, N-MPGS-6 | optional (one clause in RESULTS) |» APPENDED CLAUSE to Added statement (B): "The route π may differ from state to state;
  the claim at the transition t → t + 1 uses (H1)-(H3) at t only. The Lemma uses no phase and holds at every state of every N5 run."
- (c) (A) on λ-runs. [Q docs/referee/R-N5-MPGS.md@8da7b7179:53-57] «- YES (Opus 5.5, D15), verbatim, on ANY sequence of consecutive states (phase, λ-run with τ free, or any stretch, fallbacks included) on which v's own cycle node c = λ(v) is constant. Step by step, the proof reads: (1) R_c, hence pos, w, Φ and W: functions of c and of the global ranks only; (2) P_t ⊆ R_c at every state of the stretch (S1: P is the set of play vertices above the cycle node, and c is fixed); (3) for each P-change, the MATCHED / CARRY split, a property of the pair (P_t, P_{t+1}) alone; (4) the counting (rise ≤ W + fall, falls only at carries). No step reads τ, the phase, (MON) or the direction of the weight change. (Even only λ(v) for the single vertex v is needed, not all of λ_Ξ.)» APPENDED REMARK after Added statement (A) (SIGNED-equivalent: REFEREE
  §1b, and REFEREE-2 §C "Joint: AGREED", quoted at the top of this section): "Added statement (A) and its proof hold verbatim with the
  phase 𝒫 replaced by ANY stretch of consecutive states of one run on which λ(v) is constant (a λ-run with τ free, fallbacks included):
  no step reads τ, the phase, (MON) or the direction of the weight change. PCH and NM are then counted over that stretch." (This is the
  premise P-N5-COMPOSE §6 uses.)

### F9. Carried from MATCHPHI (C.4 last line; N-MP-1..5, MATCH-N1..N4, J11-J15)
- [Q docs/referee-2/R2-N5-MPGS-C.md@e1ec568a4:74-74] «Carried from MATCHPHI: N-MP-2 / MATCH-N4 (first term sharp at NM = 0), N-MP-3 (additivity line), N-MP-5 / MATCH-N2.»
- (a) Sharpness at NM = 0. [Q docs/referee-2/R2-N5-MATCHPHI.md@e1ec568a4:89-90] «- N-MP-2 (sharpness). The Corollary's first term is attained at NM = 0. The longest MATCHED-only chain over subsets of K ranks is exactly K(K+1)/2 (all-odd parities, K ≤ 7, exhaustive). Worth recording beside the Corollary: any improvement must come from bounding NM, not from W.» [Q docs/referee/R-N5-MATCHPHI.md@8da7b7179:90-91] «- MATCH-N4 (tightness). The Corollary's W = K(K+1)/2 is attained by abstract all-matched chains (§3); the bound is sharp as a statement about subset sequences. Its N5 tightness is open.»
  [Q docs/referee/R-N5-MPGS.md@8da7b7179:140-140] «| J12 W = K(K+1)/2 sharp at NM = 0 (all-matched chains) | MATCH-N4 | N-MP-2 | optional (record beside (A)) |»
  APPENDED REMARK after Added statement (A), PROVED (L-LIT, unrefereed; the referees' exhaustive data K ≤ 7 agree): "As a statement
  about subset sequences of R_c, the bound is attained at NM = 0. Let every rank of R_c be odd and start from A = R_c (Φ = −W). For
  k = 1, …, K in turn, move the k-th smallest original rank down one position at a time (r_k → r_{k−1} → … → r_1; each an exchange
  (o, i) with w(i) − w(o) = 1, MATCHED with M = {(o, i)}) and then remove it from r_1 (an uncovered odd outgoing rank, Φ + 1). This is
  Σ_k k = W P-changes, all MATCHED, each raising Φ by exactly 1, from Φ = −W to Φ = 0. So PCH = W = (K(K+1)/2)(0 + 1) + 0. Whether N5
  attains it is OPEN (MATCH-N4); any better bound must come from bounding NM, not W."
- (b) Additivity. [Q docs/referee-2/R2-N5-MATCHPHI.md@e1ec568a4:91-93] «- N-MP-3 (Fact 1 in context). Fact 1 is stated for singletons. The packet's reading, that the decomposition consists of steps each raising the weight of the CURRENT set, needs additivity: weight(S − o + i) − weight(S) = weight({i}) − weight({o}). That is immediate from the definition. One line.» [Q docs/referee/R-N5-MATCHPHI.md@8da7b7179:86-87] «- MATCH-N2 (Fact 1, a consequence to state). By additivity of the weight, every MATCHED change raises weight(P); so in a phase (where every P-change raises the weight, R84) the carries are exactly the improving changes that do not decompose. My exhaustive data confirm it.»
  [Q docs/referee/R-N5-MPGS.md@8da7b7179:141-141] «| J13 a MATCHED change raises the weight of the CURRENT set (additivity, one line) | MATCH-N2 | N-MP-3 | optional (one line) |»
  APPENDED LINE after Fact A1, PROVED (L-LIT, unrefereed): "For o ∈ S, i ∉ S: weight(S ∖ {o} ∪ {i}) − weight(S) = s(i)2^i − s(o)2^o =
  weight({i}) − weight({o}); and weight(S ∪ {i}) − weight(S) = weight({i}), weight(S ∖ {o}) − weight(S) = −weight({o}). Hence a MATCHED
  change A → B raises the weight of the current set: perform the exchanges of M one at a time, then add the uncovered (even) incoming
  ranks, then remove the uncovered (odd) outgoing ranks; every step raises the weight by Fact A1 and the identities above, and there
  is at least one step since A ≠ B. So weight(B) > weight(A)." READING (not to sign): in a phase, where every P-change raises the weight
  (R84), the carries are exactly the weight-raising P-changes that do not decompose so.
- (c) N-MP-1 / MATCH-N1 (premise wording). [Q docs/referee-2/R2-N5-MATCHPHI.md@e1ec568a4:85-88] «- N-MP-1 (premise wording). The premise list says "(MON) and Fact DELTA are used only by Fact 1". Fact 1 uses Fact DELTA only. - (MON) / R84's strict rise enters only the READING: in N5 every P-change raises the weight, so a carry is an improving change that does not decompose. - Say "Fact DELTA is used only by Fact 1; (MON) only by the reading".» [Q docs/referee/R-N5-MATCHPHI.md@8da7b7179:84-85] «- MATCH-N1 (premise sentence). "(MON) and Fact DELTA are used only by Fact 1": Fact 1 uses Fact DELTA only, not (MON). (MON) enters only the READING that under N5 a P-change raises the weight, so that "carry" means a non-decomposable improvement.»
  [Q docs/referee/R-N5-MPGS.md@8da7b7179:139-139] «| J11 Part (A) = MATCHPHI in mathematics; the "Uses" line repairs MATCH-N1 = N-MP-1 | MPGS-N5 | §1 of both | closed |» No change, because MPGS's "Uses" line (A2, l. 105-106) already says "Fact A1 also
  uses [DELTA]. It does not use (MON) or R84's TOP-SHAPE" (N-MPGS-3, MPGS-N5: resolved).
- (d) N-MP-4 / MATCH-N3 (alt_all figure). [Q docs/referee-2/R2-N5-MATCHPHI.md@e1ec568a4:94-99] «- N-MP-4 (§3 DATA line, not to sign). §3 says "Max NM per (vertex, phase): 31 on alt_all (0.775n); 62 at n 581". - root/logs/alt_all.lst contains red/usplit/instances/gate_K64_n581, whose run gives NM 62 (vertex 578, phase [0, 71]). So my alt_all maximum is 62, not 31. - 31 may be the maximum over alt_all without the n = 581 game, or over another start set. The "0.775n" fits n = 40 (31/40). - Also, "pl130: 157 = 41 matched + 116 carries" has no stated unit: my largest single (vertex, phase) on pl130_n40 has PCH 62 = 15 + 47. Say whether 157 sums over vertices.» [Q docs/referee/R-N5-MATCHPHI.md@8da7b7179:88-89] «- MATCH-N3 (§3 DATA, not signed). L-COMP's "31 on alt_all (0.775n)" is not what my engine finds on alt_all (41; 0.90 n at n = 40); "157 = 41 + 116" needs its unit. The pl130 maximum (47 = 1.18 n) and the 0.90 ratio agree.»
  [Q docs/referee/R-N5-MPGS.md@8da7b7179:142-142] «| J14 L-COMP's "31 on alt_all" | MATCH-N3 (mine 41 at n ≤ 100) | N-MP-4 (62 with gate_K64_n581) | MOOT: MPGS A3 now says "at most 62 (n 581), max NM/n 1.18 (pl130_n40)", consistent with both (mine excluded n > 100) |» No change, because MPGS A3 no longer carries the "31 on alt_all" and "157 = 41 + 116"
  lines; it says "at most 62 (n 581), max NM/n 1.18 (pl130_n40)", which both referees' data are consistent with.
- (e) N-MP-5 (random games). [Q docs/referee-2/R2-N5-MATCHPHI.md@e1ec568a4:100-101] «- N-MP-5 (thin spot / reading). In random games NM ≤ 1 per (vertex, phase): the carries come from the long library and lane instances. The N5-specific content (S4a's rule) is not used anywhere in the signed items, as §4 says.» [Q docs/referee/R-N5-MPGS.md@8da7b7179:143-143] «| J15 NM ≤ 1 per (vertex, phase) on random games; carries come from library / lane instances | — | N-MP-5 | optional (DATA reading) |»
  APPENDED DATA LINE to A3: "On random games NM ≤ 1 per (vertex, phase) (REFEREE-2 19); the carries come from library and lane
  instances. No signed item uses S4a's rule."
- (f) MPGS-N5, N-MPGS-3 (process). [Q docs/referee/R-N5-MPGS.md@8da7b7179:105-106] «- MPGS-N5 (process): MATCHPHI's notes MATCH-N2 (MATCHED ⇒ weight rise), N3 (L-COMP's "31 on alt_all" not reproduced) and N4 (W tight for abstract chains) apply to Part (A) unchanged; MATCH-N1 is resolved by MPGS's "Uses" line.» [Q docs/referee-2/R2-N5-MPGS.md@e1ec568a4:116-117] «- N-MPGS-3 (Part (A) carry-over). See §1. The superseded packet's N-MP-1 is fixed in MPGS's "Uses" line. My R2-N5-MATCHPHI.md stays as the record of the checks.»
  No change, because these record the carry-over of MATCHPHI's verdicts to Part (A); the items they name are F9 (a)-(d).

### F10. Notes needing no packet change (record)
- N-GS-1 = J6 = D8 (standing premise). [Q docs/referee-2/R2-N5-MPGS-s20.md@e1ec568a4:198-201] «- N-GS-1 (standing premise, as in R57 (b)). Steps 2-4 identify Ξτ(h) with the value of the (τ̄, τ)-play ρ. That is SPEC S1-val's definition of Ξ. That the S1 procedure (si.py, n5b) outputs it is SPEC conformance, the same standing premise R57 (b) records ("that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance"). DATA: ENGXI held at every vertex of every state of my runs (§3.2 column, 0 mismatches), including own cycle nodes.» [Q docs/referee/R-N5-MPGS.md@8da7b7179:134-134] «| J6 Standing premise: Ξτ(x) = V^d_{τ,τ̄}(x) is S1-val's definition; that S1's procedure outputs it is SPEC conformance, the premise R57 (b) records | — (used, not flagged) | N-GS-1 | optional for the lane; the RESULTS entry should carry the clause as R57 (b) does (Lead/CHECKER) |»
  No change in the packet, because B0 already states "Ξτ(x) = V^d_{τ,τ̄}(x) by definition"; that S1's procedure outputs this value is
  SPEC conformance, which the RESULTS entry should carry as R57 (b) does (Lead / CHECKER).
- N-MPGS-5 = J10 = D5 (enumeration caps). [Q docs/referee-2/R2-N5-MPGS.md@e1ec568a4:121-122] «- N-MPGS-5 (enumeration scope). My gate enumeration is capped (π ≤ 6 vertices, ≤ 40 per (e, d)). Gates with longer Even routes are not covered by my data. The proof has no length condition.» [Q docs/referee/R-N5-MPGS.md@8da7b7179:138-138] «| J10 data scope: gate enumeration capped | DFS budget 4,000 nodes | π ≤ 6 / 40 per (e, d) (R2-19); ≤ 64 per (state, e, d) (R2-20) | none (the proof has no length condition) |»
  No change, because the proof has no length condition and the three capped enumerations differ and all give 0 failures.
- D9, D10 = J11 (coverage; Part (A) text vs MATCHPHI). No change, because they add coverage only / record that verdicts were carried
  over by content (J11 "closed").

### F11. Lead ruling of 12:29Z (message read 13:04Z, after F3-F10 were pushed at 1bd2a11e)
- Lead (12:29Z): "treat REFEREE-2's E-class items as REQUIRED fixes-file items (the conservative reading)" (D1-D4 and the B3 line) and
  "J6-J8 (the S1 Ξτ standing premise, B1 on all valuations, the source-state hypotheses) I carry into the RESULTS entry text myself;
  record them in the fixes file as "carried into the entry"".
- Status. D1 = F3, D2 = F4, D3 = F5, D4 = F7, the B3 line = F6: written as required appended items (no statement change). Optional
  one-liners included: F6 (J1, the (H1) + (H3) question), F8 (a)-(c) (D6, D7, λ(v)-fixed line), F9 (a), (b), (e) (J12, J13, J15).
- J6 (F10, first bullet), J7 (F8 (a)), J8 (F8 (b)): CARRIED INTO THE ENTRY (Lead). The appended texts in F8 (a), (b) stay as the lane's
  wording for the Lead to use or not; the packet needs no change for them.

### Coverage
Every note routed is answered above: MPGS-N1 F3; MPGS-N2 F4; MPGS-N3 F6; MPGS-N4 F5; MPGS-N5 F9 (f); MATCH-N1 F9 (c); MATCH-N2 F9 (b);
MATCH-N3 F9 (d); MATCH-N4 F9 (a); N-MPGS-1 F6; N-MPGS-2 F5; N-MPGS-3 F9 (f); N-MPGS-4 F7; N-MPGS-5 F10; N-MPGS-6 F8 (b); N-GS-1 F10;
N-GS-2 F8 (a); N-GS-3 F6; N-GS-4 F8 (b); N-GS-5 F5; N-MP-1 F9 (c); N-MP-2 F9 (a); N-MP-3 F9 (b); N-MP-4 F9 (d); N-MP-5 F9 (e);
C.4 items 1-6 F3-F8; J1 F6, J2-J3 F5, J4 F3, J5 F4, J6 F10, J7 F8 (a), J8 F8 (b), J9 F7, J10 F10, J11 F10, J12 F9 (a), J13 F9 (b),
J14 F9 (d), J15 F9 (e). No statement of P-N5-MPGS changes; no item is FALSE; G-N5-TIME stays OPEN; NM is OPEN.

Quote check: `python3 -I docs/lit/P-N5-MPGS-fixes-quotecheck.py` from the repository root; expected output `quotes=50 bad=0`.
