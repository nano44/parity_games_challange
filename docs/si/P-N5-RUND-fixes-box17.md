# P-N5-RUND fixes (box 17 packet; repairs only)
L-SI successor 14 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's request of 10:42Z (Lead's stamp), after both §Cs. Stamp: the
commit (date -u).
- Object: docs/si/P-N5-RUND-box17.md, sha1 71e198f359cbb321fc0c15e6c28676d4dd046d52 (l-si 762b7243; pinned trunk 94910ed3). FROZEN, not
  edited.
- Repairs only. This file adds no new statement and no new proof, and changes no signed statement.
- Sources (file sha1 by `git show <commit>:<path> | sha1sum`):
  - REFEREE successor 13, docs/referee/R-N5-RUND.md: report at referee 29846bca (file sha1 45b1a11f…), §C at 62a1a01d (b75aac6d…).
  - REFEREE-2 successor 16, docs/referee-2/R2-N5-RUND.md: report at referee-2 7a02a1f2 (e9e5cb9b…), §C at 2c8c17c6 (d24a0cc6…), §C
    addendum written at ac7e80e9 and merged at e8d31c47 (641afd0c…). The addendum corrects the §C header's REFEREE commit to 62a1a01d.
- Quotes. Every «…» below is verbatim. Its tag [Q path@commit:lines] gives the source, and experiments/si/rund/quotecheck.py checks each one
  against `git show commit:path` at those lines (whitespace normalised; "…" inside a quote separates parts, and each part must occur).
  `python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-RUND-fixes-box17.md` prints QUOTES PASS (pinned in experiments/si/check.sh).

## Verdicts
- REFEREE: [Q docs/referee/R-N5-RUND.md@62a1a01d:29] «No gap. Notes RUND-N1..N4.» and, in its §C,
  [Q docs/referee/R-N5-RUND.md@62a1a01d:139] «| all 14 signed items (§2-§6) | SIGNED, no gap | SIGN, no gap | same |» and
  [Q docs/referee/R-N5-RUND.md@62a1a01d:152] «No disagreement. Joint gap map: EMPTY for the signed items.»
- REFEREE-2: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:188-190] «Fact FZ, Lemma UNF, Corollary CHARGE-U (hypothesis (ii) only): SIGN, on
  every game, under the standing SPEC premise 1E-N3 in forms P1 and P2 (N-RUND-1), with notes N-RUND-2..7. No gap.» and, in its §C,
  [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:210] «No disagreement. Joint gap map for the signed items: EMPTY.»
- So all 14 to-sign items of packet §0 (§2-§6) are SIGNED by both referees, with no gap. The joint gap map is empty. §7, §8, §9 and every
  READING were not reviewed, as the packet asked.

## Lines (one per note; the union RUND-N1..N4 and N-RUND-1..7)
- N-RUND-1 (premises; REFEREE-2, accepted by REFEREE's §C). Read the standing SPEC premise 1E-N3 into §2-§6, not only §6 FZ.
  - REFEREE-2: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:98-99] «§0 names the standing SPEC premise only for FZ. §2-§5 also rest on it, in
    form P2, through WM-G = (MON)». Its forms: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:35] «P1: S1's σ̄_k is Odd's pointwise-optimal
    strategy in the one-player game G_{σ_k}» and [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:36] «P2: S4a's σ_{k+1} is Even's pointwise
    optimum in the arena H_k of G_τ».
  - Repair (packet §0, last bullet of the item list, and §2-§5's headers): read "under the standing SPEC premise 1E-N3, in form P2 for §2,
    §3 (s^W in OFFSET (a), TWIN-GAP), §4 and §5, in form P1 for §3's s^Ξ (through (SG), N-RUND-2 below) and for §6 FZ". No statement
    changes: the cited landed results (R62 (d) WM-G, R18 (d)) already carry the premise (REFEREE's §C, [Q docs/referee/R-N5-RUND.md@62a1a01d:141] «used implicitly, through the
    landed WM-G»; and «REFEREE accepts N-RUND-1» [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:200]).
- N-RUND-2 = RUND-N1 (citation of (SG); both referees). The packet's line [Q docs/si/P-N5-RUND-box17.md@762b7243:37] «RESULTS R19 (d),
  the (SG) step: "Ξ_{L+1}(z) ⊵ Ξ_L(z) at any N5 transition (on all games)".» is NOT a verbatim quote of R19 (d).
  - REFEREE: [Q docs/referee/R-N5-RUND.md@62a1a01d:38-39] «Ξ_{k+1}(v) ⊵ Ξ_k(v) for every v at every transition, is RESULTS R15 (a) (Ξ
    non-decreasing along a run, every game). Cite R15 (a); no statement changes.»
  - REFEREE-2: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:108-109] «The content is right; the citation should name R15 (a), (d) and (VJ),
    and either quote R19 (d) exactly or drop the quotes.»
  - Repair: replace the packet's §1 line by "(SG) pointwise: Ξ_{k+1}(v) ⊵ Ξ_k(v) for every v at every N5 transition: RESULTS R15 (a)
    Lemma A and R15 (d), carried to SPEC's Ξ by (VJ) (RESULTS R57 (a)) under P1." The landed text: [Q docs/RESULTS.md@f1d2cf09:631]
    «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.» and
    [Q docs/RESULTS.md@f1d2cf09:640] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)». The quote marks
    around the R19 (d) text are dropped. OFFSET (a) is unchanged.
- RUND-N2 (FZ's exact inputs; REFEREE, accepted by REFEREE-2's §C: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:199]
  «ACCEPT RUND-N2's wording»). Name the inputs of Fact FZ.
  - REFEREE: [Q docs/referee/R-N5-RUND.md@62a1a01d:124] «RUND-N2 (citation, §6 FZ): name XW (R21 (a)) / (VJ) (R57) for Ξ_k ⊴ W_k, and
    (Cstrict), totality of ⊴ as the other inputs.» Its §6 list ends [Q docs/referee/R-N5-RUND.md@62a1a01d:96-97] «4. the definition of
    D_k (σ̄_k = τ_k off D_k), for the last sentence. Nothing else (no run, phase, S4a or (ii) hypothesis).»
  - Repair (packet §6 FZ's proof, first sentence [Q docs/si/P-N5-RUND-box17.md@762b7243:149] «Proof. (F1) in G_{σ_k} (Odd's one-player
    game; τ_k is one of its strategies) gives Ξ_k ⊴ W_k pointwise.»): read "(F1) in G_{σ_k}, i.e. Lemma XW (RESULTS R21 (a)) = premise
    (VJ) at τ′ := τ_k (RESULTS R57 (a)), under P1". The other inputs are totality of ⊴, (Cstrict), and the definition of D_k (for the
    last sentence; REFEREE-2 cites R55 (a) for that step, the same use). No run, phase, S4a or (ii) hypothesis.
- RUND-N3 (wording, PIECE_D (b); REFEREE, accepted by REFEREE-2's §C: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:201] «ACCEPT RUND-N3 as a
  note»). [Q docs/referee/R-N5-RUND.md@62a1a01d:125] «RUND-N3 (wording, §4
  PIECE_D (b)): say that R17 (c) is applied to switch-best started at B's first state (Lemma P's base holds at any start).»
  - Repair: the packet's [Q docs/si/P-N5-RUND-box17.md@762b7243:101-102] «(b) By (a), B is a run of switch-best on G_τ started at its
    first state. … R17 (c) bounds |B|.» reads "R17 (c) (Lemma P's base holds at any start state) is applied to the switch-best run on G_τ
    that starts at B's first state".
- N-RUND-3 (counts; REFEREE-2, accepted by REFEREE: [Q docs/referee/R-N5-RUND.md@62a1a01d:143] «found by REFEREE-2; ACCEPTED (wording)»). [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:111-112] «|S| in SPLIT-RED is the number
  of transitions of S (k_1 − k_0), the count the proof bounds. PIECE_D (b)'s m: R17's m is the edge count of the one-player game G_τ
  (m_τ ≤ m, Odd vertices keep one edge), so "fewer than n + m" holds a fortiori.»
  - Repair: in SPLIT-RED ([Q docs/si/P-N5-RUND-box17.md@762b7243:104] «|S| ≤ N_split(S) + (N_split(S) + 1)·(n + m − 1).») read |S| as
    the number of transitions of S. In PIECE_D (b) read m as G's edge count, an upper bound for G_τ's.
- RUND-N4 (wording, TWIN-GAP (ii); REFEREE, accepted by REFEREE-2's §C: [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:202] «ACCEPT RUND-N4 as
  a note»). [Q docs/referee/R-N5-RUND.md@62a1a01d:126-127] «RUND-N4
  (wording, §3 TWIN-GAP (ii)): "each rank r contributes at most 2^r" — the bound used is the WIDTH of the range of the low part,
  Σ_{r ≤ L*} 2^r = 2^{L*+1} − 1 (one vertex per rank, signed by parity)»
  - Repair: in TWIN-GAP (ii)'s proof, replace [Q docs/si/P-N5-RUND-box17.md@762b7243:82] «each rank r contributes at most 2^r» by "the
    low part Σ over ranks ≤ L* (one vertex per rank, signed ±2^r by parity) ranges over an interval of width Σ_{r ≤ L*} 2^r = 2^{L*+1} − 1".
    The bound 2^{L*+1} − 1 per score is unchanged.
- N-RUND-4 (TWIN-GAP (ii) reading; REFEREE-2, accepted by REFEREE: [Q docs/referee/R-N5-RUND.md@62a1a01d:144] «found by REFEREE-2;
  ACCEPTED (wording)»). [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:113-114] «"At states ≥ k_0 +
  n − 1" = transitions whose SOURCE state is ≥ k_0 + n − 1 (both endpoints then lie in FRZ-U_H3's frozen range); (iii) adds the n − 1
  transitions with sources k_0, …, k_0 + n − 2.»
  - Repair: in TWIN-GAP (ii) ([Q docs/si/P-N5-RUND-box17.md@762b7243:77] «at most (2^{L*+2} − 2) / 2^{ℓ_S} < 2^{B+1} of them lie at states
    ≥ k_0 + n − 1») read "of them have their source state ≥ k_0 + n − 1".
- N-RUND-5 (U depends on L; REFEREE-2, accepted by REFEREE: [Q docs/referee/R-N5-RUND.md@62a1a01d:147] «found by REFEREE-2; ACCEPTED
  (wording)»). [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:115-117] «"Forbidden" is defined at
  a level L, so U(S) is U_L(S). … hence U_L(S) ⊆ U_{−1}(S) and CHARGE-U with U_{−1}(S) bounds every level.»
  - Repair: in CHARGE-U write U_L(S) for U(S) (forbidden at the level L of the statement). By N-RUND-5's argument, U_L(S) ⊆ U_{−1}(S), so
    the statement with U_{−1}(S) holds at every L. The signed statement is unchanged.
- N-RUND-6 (thin spots in data; REFEREE-2; REFEREE's §C: [Q docs/referee/R-N5-RUND.md@62a1a01d:148] «same in substance»). [Q
  docs/referee-2/R2-N5-RUND.md@e8d31c47:118] «N-RUND-6 (thin spots in data; the proofs do not need them).» No repair. Recorded: TWIN-GAP
  (ii) far from tight, PIECE_D (b) slack, CR-REL's freeze non-vacuous on 12 sub-runs (REFEREE-2), 3-5 times (REFEREE).
- N-RUND-7 (§4 remarks; both checked). [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:123-124] «"A forbidden edge at L = −1 is a split edge"
  holds by (Cstrict). The CORRECTION (withdrawn READING) is consistent with FZ; nothing signed used it.» No repair.

## §7 status line (not signed items; for the record)
- §7's CONJECTURES, status at this file's commit (lane-reproduced; docs/si/DEAD.md; pinned in experiments/si/check.sh):
  - UF-ONCE: DEAD. REFEREE-2 side finding, R2-N5-RUND §4 (so_th_n32 from its S3 start, Even 24 makes three unforbid-switches; phase2_pk48
    from phase2_pk48_s1.start, Even 44 makes two); REFEREE reproduced so_th_n32 (its §C); L-SI reproduced both (DEAD box 18a).
  - U-SPLIT (lane note §17, not in the packet): DEAD. L-RED R80 (l-red 64182fe1), usplit_rd_s3_n27.pg (sha1 1e9ca56d…, 𝒞^2O, S3 start),
    y = 26, z = 25, offset 0 → 0, no stretch_D boundary; L-SI reproduced it (DEAD box 18b).
  - PAIR-OC: DEAD. L-RED R81 (l-red 64182fe1), pairoc_n58.pg (sha1 4824c73c…) + pairoc_n58.start, v = 57 has W rises at levels 47, 48, 47
    at three offset changes; L-SI reproduced it (DEAD box 18c). LC2 survives there (|OC| 3 ≤ |SL| 5).
  - FS, LC2: CONJECTURES, OPEN. The route "|U(S)| ≤ n_E via UF-ONCE" is closed; CHARGE-U (signed) is unaffected. REFEREE-2's addendum:
    [Q docs/referee-2/R2-N5-RUND.md@e8d31c47:220-221] «the witness refutes UF-ONCE but does not stress CHARGE-U's U-term.»

## Data
- No referee asks for more. REFEREE: 0 failures (long runs with every suffix, lib41, 6,000 random; MUT=1/2 controls fail). REFEREE-2: 0
  violations (instances, climbs, lib41, 503 𝒞^1O files, random k = 2..4; six mutations fail).
