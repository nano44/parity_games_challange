# Box 215 (D18): KEYSIDE-ALL — R111's key-side lemmas (LOCAL-KP, PAIR-KF, KEYFLIP / PAIR-MOVES, CASCADE, F ≤ T, LADDER) for N5 on Γ3(G) of EVERY genome, Ξ-cycles included, CONDITIONAL on KEY-TAU (i) (box 213); MERGE, RETURN, RENEW not transferred (value side). Not a bound; G-N5-TIME stays OPEN
L-NEW successor 75 (session_01V5yGRWimvjsi2nZhjaevtK), D1 / D14 / D18 / D21. Written 2026-11-13 04:31Z (date -u). Statement to the Lead 04:30Z;
Lead 04:31Z: «go», with amendments «(1) … CONDITIONAL on KEY-TAU (i) (box 213) … «Transfers verbatim» means the proof text carries over given
[M]; say exactly that. (2) For each «verbatim» claim, quote the R111 / P-IDEAL-KEYS proof steps by script (file, commit, lines) and mark the
one place, if any, where IDEAL-ACYC or ENC enters. Your three-line re-proof of KEYFLIP goes in full in the box. (3) The «not transferred»
list … is part of the record.» Labels: CONDITIONAL (on KEY-TAU (i), a lane CANDIDATE of box 213); DATA. Not M3, not M4.

## 1. Setting and the premise [M]
- G any genome (R104's definition; Ξ-cycles and Ξ self-loops allowed); N5 (SPEC S1-S5) from S3 on Γ3(G); s_0, …, s_T the movers' options
  at the states before the first fallback; Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}. Keys, KP, KF, W(x), flips, 𝓛^R_d: P-IDEAL-KEYS §0's
  definitions (docs/new/P-IDEAL-KEYS.md at l-new b302bbf5, sha1 62b35bf7…, = trunk e8b6abf0's copy), read with the genome's W-targets and
  gate indices. The e-vertices of Γ3 are indexed in gate order (experiments/new/box189/gamma3.py, «for q in sorted(O, key=lambda q:
  gate[q[0]][q[1]])»), so box 213's root-first e-index key orders options as this key does.
- [M] (CONDITIONAL; box 213 KEY-TAU (i), lane CANDIDATE, premises R125 W3-ALL, ESC3-ALL and R117 TAU3 as quoted and checked there):
  s_(t+1)(x) is the option of A_t(x) with the least key under s_(t+1), where A_t(x) = {s_t(x)} ∪ {Ξσ_t-improving options} ∋ s_t(x). A_t is
  computed from the two-player values Ξσ_t; nothing about A_t is used below except «s_t(x) ∈ A_t(x)». Also used where said: [NE] every
  step before the first fallback moves at least one mover (RF-D's [IMP3], lane: R15 (d) with τ constant).
- In P-IDEAL-KEYS the same rule is the model's step (§0, l. 59): [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «s_t(x) := the option in A_(s_(t−1))(x) with
  the least key_(s_t)(x, ·) (keys under the NEW state)». THIS is the one place where the IDEAL-ACYC model enters the key-side proofs: through
  the step rule, which [M] replaces. ENC enters none of them.

## 2. The transferred statements (each CONDITIONAL on KEY-TAU (i) (box 213))
«Transfers verbatim» means: the proof text of P-IDEAL-KEYS carries over word for word once [M] stands for the model's step rule.
- **LOCAL-KP (a), (b).** R111: [Q R111] «(LOCAL-KP) at any degree, if two states agree on W(x) then they give every option of x the same key,
  so KP(x) is the same and KF_x ≤ WE_x». Proof steps (P-IDEAL-KEYS §2, l. 87-92): [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «lev(x) = 0:
  key_s(x, k) = (g(x, k)) = key_(s′)(x, k).» and «If Mv_t ∩ W(x) = ∅, then s_t and s_(t−1) agree on W(x), so KP_(s_t)(x) = KP_(s_(t−1))(x)
  by (a).» The packet's own scope line: «LOCAL-KP is about keys only; R105's LOCAL is not used». Not even [M] is used: (a) is about two
  states, (b) about any sequence of states. Transfers verbatim.
- **PAIR-KF (a), (b).** R111: [Q R111] «for a mover x of degree 2 and level ≥ 1 with W-targets a, b of its two options, KF_x = 0 if a = b, and
  KF_x = flips(a, b) if a ≠ b». Proof step (§3, l. 100): [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «key_s(x, k) = key_s(wt(x, k), s(wt(x, k)))
  followed by g(x, k), the prefix having length lev(x) (F1).» Keys and (F1) only ([Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «(F1) key_s(x, k) is
  a tuple of length lev(x) + 1 whose last entry is g(x, k)»); no step rule. Transfers verbatim.
- **KEYFLIP and PAIR-MOVES.** R111 uses R105's KEYFLIP: [Q R111] «if every mover has degree ≤ 2, moves(x) ≤ 1 + flips(a, b) for such x with
  a ≠ b and moves(x) ≤ 1 for every other mover, so T ≤ N + the sum of those flip counts». I do not lean on R105's proof of KEYFLIP; my
  re-proof from [M], in full:
  - KEYFLIP′ (CONDITIONAL on [M]). Let deg(x) = 2. If x ∈ Mv_t, then s_t(x) is the option of x with the least key under s_t: KP_(s_t)(x).
    Proof: A_(t−1)(x) ∋ s_(t−1)(x) and s_t(x) ≠ s_(t−1)(x) are both in A_(t−1)(x), which is then the whole option set; [M] picks its key-least
    option. Consequence: if x moves at t_1 < t_2 and not in between, then s_(t_2)(x) = KP_(s_(t_2))(x) ≠ s_(t_2 − 1)(x) = s_(t_1)(x) =
    KP_(s_(t_1))(x), so KP(x) changes at some step of (t_1, t_2]; distinct consecutive move pairs give disjoint intervals. Hence moves(x)
    ≤ 1 + KF_x. ∎ (Value side used: only «s_(t−1)(x) ∈ A_(t−1)(x)», SPEC's definition of A.)
  - PAIR-MOVES then follows as in §3 of the packet (§3, l. 109: [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «KEYFLIP gives moves(x) ≤ 1 + KF_x.»), with
    PAIR-KF and «T ≤ Σ_x moves(x)», which needs [NE].
- **CASCADE (a), (b) and F ≤ T.** R111: [Q R111] «(CASCADE) at any degree, at every step at which two distinct movers p, q of one level l
  flip, p or q moves, or l ≥ 1, neither moves, their current W-targets w_p ≠ w_q and (w_p, w_q) flips at the same step, and flips(p, q) ≤
  T». Proof steps (§4, l. 122-127): [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «(own) and (below) exclude each other by definition.» and «A flip
  of (p, q) is then a flip of (w_p, w_q).» Keys, Mv_t and (F1) only. Transfers verbatim.
- **LADDER** (on every genome whose W-structure is 𝓛^R_d, ANY Ξ-targets). R111: [Q R111] «on 𝓛^R_d with F(l) := flips(2l, 2l + 1), F(0) ≤
  2, F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1) and moves(x) ≤ 1 + F(lev(x) − 1) for lev(x) ≥ 1, so F(l) ≤ 2 + 3F(l − 1) ≤ 3^(l+1) − 1».
  Proof step (§4, l. 138-139): [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «Every mover x of level l ≥ 1 has wt(x, k) = 2(l − 1) + k, distinct, so
  PAIR-MOVES gives moves(x) ≤ 1 + F(l − 1).» Uses CASCADE, PAIR-MOVES (so [M], [NE]) and the W-side definition of 𝓛^R_d only.
- What it gives: on Ξ-cyclic genomes N5's key run before its first fallback has the IDEAL model's key-side skeleton; with degree ≤ 2,
  T ≤ N + Σ flips and every flip is own or below. So O1′'s difficulty is on the value side (which options are Ξ-improving when), as for
  O1. No bound on any flip count is claimed.

## 3. Not transferred (value side; the record)
- MERGE: its proof (§6, l. 182-183) unrolls ENC along a Ξ-chain and needs it acyclic: [Q docs/new/P-IDEAL-KEYS.md@b302bbf5] «the two Ξ-sets differ: β(x, a)
  lies only in the first, since x does not recur on an acyclic chain». On Γ3 with Ξ-cycles the Ξ-values are VJ values against Odd's
  replies; ENC's integer encoding is not available.
- RETURN (and RETURN-COUNT): premises R105 ENC, MONO and the Ξ-target's current value cv.
- RENEW: premises R105 XI-NEW, RISE.

## 4. DATA (experiments/new/box215/keyside215.py: keys computed from the genome alone; outputs out/, pinned)
Numbers from out/summ215.txt (summ215.py; outputs pinned in out/SHA1SUMS). Must-0: lkp, pkf, pkfa, kflip, casc, ftt, ladder.
| set | genomes | Ξ-cyclic | 𝓛^R_d-shaped | flips checked | every must-0 |
| --- | --- | --- | --- | --- | --- |
| FROZEN (box 212's 81 + 5 towers + box 213's 2 TAUESC) | 88 | 83 | 5 (the towers, Ξ-acyclic) | 14,425 (12,000 on Ξ-cyclic genomes) | 0 |
| RANDOM, Ξ-cyclic only (eg195 modes rand, dense, deep, noesc; seeds 2150-2153; 300 each) | 1,200 | 1,200 | 32 (Ξ-cyclic ladders: LADDER tested) | 1,756 | 0 |
- No generator of 𝓛^R_d-shaped Ξ-cyclic genomes exists in the tree (eg195.gen draws W-targets at random); none was built (Lead 04:31Z).
  The 32 random genomes that happen to be 𝓛^R_d-shaped are small (maxF 1); the LADDER test on Ξ-cyclic ladders is therefore weak.
- Towers (Ξ-acyclic, a cross-check with R111's setting): maxF 254 = HIT7's F(6), maxmoves 127 (box 213's kcount213: maxsw 127).
- Controls (check215.out): KM_MODE=xi (N5′-xi, Howard's tie rule): kflip 4 (DBL4), 21 (CFI3_n48); KS_CTRL=1 (gate indices permuted, seed
  5): kflip 7 (DBL4); KS_CTRL=2 (CASCADE without «own»): casc 124 (CFI3_n48). A gate order REVERSAL is not a control: every comparison
  flips at the same steps, so KP changes at the same steps (found while building the tool; recorded so nobody uses it).

## 5. Kill criteria; not claimed
- Any must-0 counter (lkp, pkf, pkfa, kflip, casc, ftt, ladder) > 0 under SPEC on any genome before its first fallback kills the transfer
  (instance named) and restricts the lemma to Ξ-acyclic genomes again. A kflip > 0 would also contradict KEY-TAU (i).
- Not claimed: any bound on flips, F(l), T; anything after the first fallback; MERGE, RETURN, RENEW on Ξ-cyclic genomes. Not M3, not M4.
  **G-N5-TIME stays OPEN.**

## Addendum A (L-NEW successor 76, written 2026-11-13 08:40Z by date -u; Lead 08:40Z: «Box 215 Addendum A (append-only): restate KEYSIDE-ALL with e-index keys, cite R241 and credit L-RED 69 (L41), and keep the gate-key form as history labelled «depends on numbering (R241)».»)
- **Finding (L-RED 69, R241; credit under L41).** [Q docs/red/R241-keytau.md@df801a6f] «box 215 KEYSIDE-ALL, as stated (gate-index keys of
  P-IDEAL-KEYS) | **DEPENDS ON NUMBERING**» and [Q docs/red/R241-keytau.md@df801a6f] «box 215 with e-index keys (the numbering-free form) |
  **SURVIVES** | every *_e counter 0 under every numbering, incl. the 14 instances». The 14 instances are experiments/red/r241/inst/NUMB_*
  on claude/l-red df801a6f (each 0 on box 189's numbering, firing when renumbered; n5v xdiff 0). The cause is §1's identification of the
  e-index key with the gate-index key, which holds only for box 189's numbering (e-vertices in gate order): [Q docs/red/R241-keytau.md@df801a6f]
  «that identification is the only place the numbering enters, exactly R240's pattern for FLAT-IDX.»
- **History.** §0-§5 above (gate-index keys g(x, k)) stand as written, labelled: **depends on numbering (R241)**. They are correct for
  Γ3(G) numbered as box 189 numbers it, and only there; keyside215.py computes gate-index keys and so tests that numbering only.
- **KEYSIDE-ALL, restated (CONDITIONAL on KEY-TAU (i), as before; numbering-free).** In every statement of §2 ([M], LOCAL-KP (a), (b),
  PAIR-KF (a), (b), KEYFLIP′ and «moves(x) ≤ 1 + KF_x», PAIR-MOVES, CASCADE (a), (b), F ≤ T, LADDER) read P-IDEAL-KEYS's key with g(x, k)
  replaced by ε(x, k), the vertex index of e_(x,k) in the game on which N5 is run: key_s(x, k) := (ε(x, k)) at level 0 (or wt < 0), else
  key_s(wt(x, k), s(wt(x, k))) followed by ε(x, k). KP, KF, flips and 𝓛^R_d are defined from these keys. No proof changes:
  [Q docs/red/R241-keytau.md@df801a6f] «The proofs of box 215 §2 use nothing about g but that it is an injective index per option, so the e-index
  form needs no new proof.» (my reading agrees: §2's proofs compare keys as tuples of distinct per-option indices and never use their values
  otherwise). This is box 213's KEY-TAU key («the tuple of its e-vertices' indices read from c_W»), so [M] is KEY-TAU (i) restated.
- **DATA for the restated form.** L-RED 69's own engine (n5s237, R237) with e-index twins *_e: 0 under the numberings none / e / all on
  8,047 runs, including the 14 NUMB instances (R241 §0, §4, as cited above; not re-run here). L-NEW's keyside215.py data (§4) are DATA for
  the restated form on box 189's numbering only, where ε and g order the options identically (R241's eord 0).
- Consequence for box 217: its one-player model 1P(G) uses the same keys; it is switched to ε (box 217 §1 note) and its climb searches
  over the e-order (the adversary chooses the numbering).
