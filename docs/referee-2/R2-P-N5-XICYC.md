# R2-P-N5-XICYC: second-referee report on packet P-N5-XICYC (L-NEW successor 59, box 191)
REFEREE-2 successor 30 (Opus 5.5, D1), 2026-11-07 from 07:3xZ (date -u). Independent: docs/referee/ not read on this item.

## Object (sha1 of the bytes at claude/l-new 86afce49; fd1266a5 is an ancestor; all equal to the Lead's relay 07:30Z)
- docs/new/P-N5-XICYC.md 149e2414… (20,825 B; unchanged since the freeze fd1266a5); line L-1 d6f77b12… (2,738 B); fixes b4ad5bca…
  (4,352 B, entry 1); line L-2 857d21c8… (4,579 B, 1 line, 60 «(» = 60 «)», depth never negative, 0 «|»); pins
  experiments/new/box191/xicyc.pins 521ce400…; check191.out d07c2f0c….
- check.sh blocks «BOX 191 XI-CYCLIC» and «P-N5-XICYC» re-run on `git archive 86afce49` (13 s): both print PASS; check191.sh output =
  frozen check191.out. inst/SHA1SUMS: 15/15 OK.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | definitions (IDEAL-CYC, Howard step, labels C / R / p, n) | **SIGN** (Opus 5.5, D1) |
| §3 | F1, F2, F3, F5, F6 | **SIGN** (Opus 5.5, D1) |
| §3 | F4 | **SIGN after W-1** (false as stated; true in the form W-1 gives, which is all §4 uses) |
| §4 | DOM, STRICT, PATH, Theorem BR-SEG, CYC-COUNT, Theorem T-CYC, Corollary ONEP-POLY, LEVEL0 | **SIGN** (Opus 5.5, D1) (with W-1; N-1) |
| §5 | Theorem BR-SEG-G (a)-(c) under H0 | **SIGN WITH GAPS** (G-1: the proof as written uses DOM / F4 on general games, where they are false; closed by the repair in §R, which the lane must state in a fixes entry) |
| §6 | Lemma DECOMP-G | **SIGN** (Opus 5.5, D1) |
| §6 | Theorem RED-XI (reduction only) | **SIGN WITH GAPS** (inherits G-1 through BR-SEG-G (c); closed with it) |
| §7 | Theorem REACH3-CYC | **SIGN as PROVED-CONDITIONAL on [REACH-L]** (Opus 5.5, D1): no hidden Ξ-use in ESC3 or W3 (§7 below) |
| §7 | Corollary T3 (as an equivalence only) | **SIGN as PROVED-CONDITIONAL on [REACH-L]** (Opus 5.5, D1) |
| §8 | DEAD SEG-2P, DEAD ODD-FIXED | **SIGN** (Opus 5.5, D1): all three instances replayed with my own run |
| line | L-2 | **MATCHES after W-2, W-3, W-4** (all wording; L-1 → L-2 byte test passes) |
Nothing is REFUSED. N5′-xi stays a CANDIDATE: the packet claims nothing about general games beyond RED-XI's reduction, and R is
bounded nowhere (OPEN). §9-§12 are DATA / READING and are not signed.

## Premises
- [R15a], [R15d] quoted as RESULTS R15 (a), (d) (not re-opened by me; both are in my predecessors' reports of record).
- [VJ] order: my brute-force evaluator (r2vjg.py) implements it from the packet's text (reward of Λ; Π by the most relevant element of
  the symmetric difference and its parity; k by Λ's parity). si.py's Engine (the fleet reference) agrees with it on Γ(G) of small
  Ξ-cyclic genomes, (Λ, Π, k) at every vertex: r2xval.out, 300 states, 6,674 vertices, 0 mismatches.
- [DEF], [N5XI]: N5′-xi's rule read from docs/new/N5-DETOWER-box190.md §2.1 (l. 36-39); my implementation r2xi3.py.
- HMZ (the packet's §12 / L-2 citation): opened, arXiv 1008.0530 (one version, v1, 13 pp., sha1 ae2454e63158…). §5 (p. 8) says «The
  following lemmas for the case of MDPs are well-known and appear, e.g., in Meister and Holzbaur [27]. The proofs for the 2-player case
  are essentially identical. (They may be folklore.)»; Lemma 5.3: «T v^π0 ≥ v^π1» (one SI step is dominated by one value-iteration step
  from the old values, discounted 2-player, player 1 minimising); Lemma 5.4: SI value vectors are dominated by value iteration's. The
  citation is CORRECT as a citation of an analogue. Note: HMZ's proof uses the monotonicity of the linear operator c + γPv; the VJ
  counterpart of that monotonicity is F4, which fails on general games (G-1). The packet uses HMZ only as context, not as a premise.

## §3-§4 (own re-derivation)
- F1 (Switch_I with I = every strictly improving switch, one per mover: unambiguous), F2, F3 (play of a positional pair; if v is on the
  cycle but not Λ, the prefix from nx(v) to Λ does not contain v), F5, F6 (every cycle through a mover passes a gate and then e or β of
  priority ≥ 6) ✓.
- **W-1 (required; F4 as stated is false).** «ext(v, ·) is ⊴-monotone and strictly monotone»; the proof's «v is added to both Π or to
  neither» fails when v is already in one of the two Π-sets (then ext removes v from the symmetric difference). Instance (general game,
  r2dompex.out): Ω_t(y) = (1, {2, 3}, 2) contains x = 3; ext(3, ·) of it is (1, {2, 3}, 3), and the order against (1, {3}, 1) flips.
  Replace F4 by: «F4: if v ∉ Π(a) ∪ Π(b), then a ⊴ b ⇒ ext(v, a) ⊴ ext(v, b), and a ◁ b ⇒ ext(v, a) ◁ ext(v, b)», and add after it:
  «Every use of F4 in §4 satisfies this: a mover has priority 0 and every cycle node has priority ≥ 3 (F6's argument; c_X has 2), so a
  mover is in no Π; in PATH, a non-mover z_0 is not in Π(Ω_t(z_1)) (z_0 → z_1 is z_0's own play step, so z_0 on z_1's prefix would put
  z_0 on its own cycle) and not in Π(val(tail)) (π is simple).» I checked every F4 step of DOM, STRICT, PATH, BR-SEG against this.
- DOM, STRICT, PATH, BR-SEG: re-derived step by step (PATH's induction needs t − 1 ≥ a, true as μ ≥ 1; BR-SEG applies PATH with
  b = a + j + 1 and t = a + j, j ≥ N ≥ μ(π)) ✓. CYC-COUNT: candidate cycle nodes β (M), e (M), c_W, K1, K2; c_X fixed; K0 → K3 → K2 frozen
  and K1 → K1 frozen, so K0, K3 are on no cycle (u = K0 in [DEF]: β_g → {xt(g), K0}) ✓. T-CYC ✓. ONEP-POLY ✓. LEVEL0 ✓.
- N-1 (no verdict change). LEVEL0's «Hence R-flips happen only at gates of level ≥ 1» also needs σ̄(K2) constant. That holds more
  strongly than ONEP-POLY's «deterministic rule» argument says: at K2 the options give cycle nodes K1 (reward −p'(K1)) and K2 (reward
  −p'(K2) > −p'(K1)), so K1 is Odd's unique best in every state, whatever the rule (my counter K2: 0 in every run below).
- Machine (own code): r2howcyc.py (my IDEAL-CYC Howard on Γ(G) from my predecessor's own R104 builder, values from si.py Engine; ties:
  keep current, then larger index) counts F1, F6, STRICT, DOM (every mover x, every successor y), BR-SEG (p-run ≤ N), CYC-COUNT, T-CYC,
  LEVEL0 (σ̄ = β-face at every level-0 gate in every state), K2 (σ̄(K2) = K1): **all 0** on the 8 pinned Ξ-cyclic genomes and the 3 DEAD
  genomes (r2howcyc.out), on 1,500 random genomes (1,492 Ξ-cyclic; N ≤ 14, d ≤ 5; 4,502 steps, R 601) and on 1,000 random ONEP genomes
  (988 Ξ-cyclic; **R = 0** on all 2,683 steps) (r2howrand.out).

## §5 BR-SEG-G: gap G-1 and its repair
- **G-1.** §5 says «§4's proofs, with mover read as Even vertex». On a general game an Even vertex can be more relevant than its cycle
  node and lie on the prefix of a neighbour's play, so F4's hypothesis (W-1) fails and DOM is false as a lemma:
  - my brute-force VJ Howard (r2vjg.py: every Odd positional strategy enumerated, the pointwise optimum asserted) on 10,418 random
    games (n 6-8; r2vjg.out): DOM fails in 296 of 52,417 (x, t, y) cases with Λ_t(x) ≠ x ≠ Λ_(t+1)(x), every failure with x ∈ Π(Ω_t(y));
  - DOM fails even in PATH's own setting (a p-step, Λ_t(y) = Λ_t(x)): 124 of 14,729 cases. Instance (r2dompex.out): priorities
    (2, 3, 4, 5, 0, 1), owners (O, O, E, E, E, E), successors 0→{2}, 1→{1}, 2→{1, 3}, 3→{1, 2}, 4→{0, 1, 3}, 5→{0, 1, 4}; σ_t =
    (·, ·, 3, 1, 0, 0) → σ_(t+1) = (·, ·, 1, 1, 1, 1), a p-step; x = 3, y = 2: Ω_(t+1)(3) = (1, {3}, 1) ◁ ext(3, Ω_t(2)) = (1, {2, 3}, 3).
    π = 3 → 2 → 1 is a simple E_a-path with Λ = 1 throughout, so PATH's induction step for it does not go through as written.
  - PATH's CONCLUSION is not violated there (3 switches to 2 one step later), and BR-SEG-G (a) has no violation in my runs (max p-run 3
    at n ≤ 8) or in the lane's (2,000 games, reproduced below). So this is a proof gap, not a counterexample.
- **Repair (I checked it; the lane must state it in a fixes entry, then G-1 is closed).**
  - Inside a window [a, b] with Λ_t = Λ_a, every comparison PATH, DOM and STRICT make is between values with the same cycle node w
    (for DOM: Λ_t(σ_(t+1)(x)) = Λ_(t+1)(x) = w and Λ_t(z_1) = w). For a fixed w, ⊴ is the lexicographic order on
    φ(w, Π, k) := (Σ_(u ∈ Π) s(u)·2^rank(u), ε_w·k) in Z × Z, with s(u) = +1 for even u, −1 for odd u, ε_w = −1 if w is even and +1 if
    odd (si.py's weight; the most relevant element of the symmetric difference decides). This order is translation-invariant.
  - Define ext⁺(v, a) := a + (s(v)·2^rank(v)·[rank v > rank w], ε_w) in Z × Z. It is strictly monotone for every a, b (a translation),
    and ext⁺(v, a) = φ(ext(v, a)) whenever v ∉ Π(a).
  - DOM⁺: Ω_(t+1)(x) ⊵ ext⁺(x, Ω_t(y)) for t, t + 1 in the window, Λ(x) = Λ(y) = w ≠ x: Ω_(t+1)(x) = ext⁺(x, Ω_(t+1)(σ_(t+1)(x))) (F3,
    x not on that prefix) ⊵ ext⁺(x, Ω_t(σ_(t+1)(x))) (F1, translation) ⊵ ext⁺(x, Ω_t(y)) (F5, translation).
  - STRICT under H0 (any game): if Λ_(t+1)(x) ≠ Λ_t(x), F1 + F2 give ▷; otherwise all four values have node w (F5 forbids
    Λ_t(σ_(t+1)(x)) of smaller reward), and the same chain with ext⁺ gives ▷.
  - PATH with ext⁺ in the mover / Even case and ext elsewhere (val(π) = the ext⁺-sum, π simple): unchanged induction. BR-SEG-G (a)
    follows as in §4; (b), (c) as stated.
  - Checked by machine (r2vjg.out): DOM⁺ 0 failures in 16,384 (x, t, y) cases with Λ constant on the step; φ reproduces ⊴'s strict
    comparisons Ω_(t+1)(x) vs Ω_t(x) in all of them (ISO_F 0); STRICT 0 failures in 9,407 switched vertices.
- (b) C ≤ n(n − 1) ✓. (c) ✓ given (a).
- RED-XI: DECOMP-G ✓ (σ changes only at S-iterations, each Switch_I with I ⊆ Iσ, Iσ a function of σ: [R15d]). The bound:
  #S ≤ n(n − 1) + R_σ + (n(n − 1) + R_σ + 1)·n_E = (n_E + 1)(n(n − 1) + R_σ) + n_E ≤ (n_E + 1)(n(n − 1) + R_σ + 1) ✓; BR-SEG-G (c)
  holds for every prefix of a Howard run, so the S-run need not end at a Howard stop ✓. It uses BR-SEG-G (c): G-1 inherited.

## §7 REACH3-CYC: the re-reading the Lead asked for, and the replay
- P-N5-REACH at claude/l-new 727163f0 (packet b7bd6937, the frozen text; R117 at C130), read for every use of IDEAL-ACYC:
  - S3-START (§4), PAD (§5), K3 (§6.1), TAU3 (§6.4): labelled «every genome»; their proofs use only K, pads, gates' faces and the
    W-descent ✓. K3 (b) says «These values hold once SBAR3 gives σ̄(K2) = r» (SBAR3 is IDEAL-ACYC): K is closed and Odd's best at K2 is r
    by REWARD (N-1 above; P-N5-REACH fixes entry 1, reply to REFEREE-2 N-1), so K3 holds for every genome ✓.
  - ESC3 (§6.5): its H-plays follow τ = pe at every gate: from xt(g) mover → pad → gate → pe → e → … → c_W, from pb_g → K0 → core (K3
    (d)); β_g is on no H-cycle; P is compared at a common node only via REWARD. **No β-face is taken and no Ξ-edge is followed: no hidden
    Ξ-use** ✓. The only acyclic-only premise reachable from it is K3 (b), settled above.
  - W3 (§6.6) (i)-(iii): (σ, τ = pe)-plays and H-plays with τ = pe; W(β_g) takes one β step (β_g → xt(g), a mover) and then the W-descent.
    **No Ξ-use** ✓. (A wording slip in W3 (i), signed text, no effect: «pβ … the play never meets a mover» — pβ_g → β_g → xt(g) can meet
    one; W(pβ_g) still depends on lev only.)
  - In a Ξ-cyclic genome (β_g, pb_g) can be in Iσ (σ̄ may close an odd β-cycle); the packet's argument does not need Iσ(β_g) = ∅, only
    TIE(β_g) = {xt(g)}, which ESC3's H-optimum gives ✓. The Howard step: TIE(x) = R(x) = {σ(x)} ∪ Iσ(x) (W3 (iii)); the Ξσ-best element
    of R(x) is a ⊴-best successor, and σ(x) is kept iff Iσ(x) = ∅ ✓.
- Replay (own code r2xi3.py: N5′-xi written from box190 §2.1 on my predecessor's SPEC step (R2-N5-REALIZE) and Γ3 builder
  (R2-P-N5-REACH/r2reach.py), from S3):
  - 8 pinned Ξ-cyclic genomes + 3 DEAD genomes (r2xi3_inst.out): every state 0..T3 standard, mover states = my Howard run on Γ3
    (and on Γ), no fallback before T3 + 1, a fallback at T3 + 1, iterations = T3 + 3 ✓ (11/11).
  - 1,000 random genomes (984 Ξ-cyclic; r2xi3rand.out), checked directly on the xi run: 2,780 mover transitions, **0 non-standard states,
    0 non-Howard mover steps (each mover to a ⊴-best successor, kept when best; nothing else changes), 0 bad stops, fallback present in
    1,000/1,000** ✓. 971/1,000 runs also equal my Howard run with ties «keep current, then larger index»; the 29 others are Howard runs
    under SPEC's tie choice (the theorem allows any tie rule) ✓.
- Corollary T3: §4 transfers to Γ3 (movers priority 0; pads never cycle nodes, PAD (b); non-mover Even frozen; Odd = gates and K2;
  CYC-COUNT's candidate set unchanged; LEVEL0's c_W in-edges are e_g of level 0) ✓. ⇐ by T-CYC, ⇒ by R ≤ T3 ✓. As an equivalence only ✓.

## §8 DEAD (own replay, r2howcyc.out)
| instance | sha1 (inst/SHA1SUMS) | N | my labels | longest Λ-keeping run | R |
| --- | --- | --- | --- | --- | --- |
| DEAD_SEG2P_d4_N8.json | OK | 8 | ppppppppRC | 9 > 8 | 1 |
| DEAD_SEG2P_d7_N14.json | OK | 14 | CCCCpRRRRppRRRpRppp | 15 > 14 | 8 |
| DEAD_SEG2P_d9_N18.json | OK | 18 | pppRppRppRppRRRpppppp (C 0) | 21 > 18 | 6 |
Labels byte-equal to the packet's table and check191.out. SEG-2P's universal statement («every run of consecutive steps keeping all Λ
has at most N steps», any tie rule, any σ̄ rule) is killed by one admissible run ✓. ODD-FIXED: each R-step is a Λ-keeping step at which
σ̄ changes ✓. The obstruction («R-steps inside the run, as BR-SEG requires») is exact: in all three, every p-run is ≤ N.

## DATA rule on L-2 (clause by clause; every cited command re-run on `git archive 86afce49`, outputs in R2-P-N5-XICYC/)
- L-1 → L-2 (bt_xicyc.py / .out): fixes entry 1's R-1 old string occurs once in L-1, new once in L-2, L-1 + R-1 == L-2 ✓.
- BR-SEG «0 of 1,000» (subrun191.py 1000 21: «maxpure > N in 0», unit genomes, p-runs, two-player) ✓ reproduced.
- CYC-COUNT «C > N·M in 0 of 300» each model (seg1p191.py 300 11, in check191.out) ✓; N·M < n(2M + 2), so stronger ✓.
- T-CYC, RED-XI: no separate DATA ✓.
- ONEP-POLY: seg1p191 counts Λ-keeping runs and C in the ONEP model; **the clause's R = 0 has no counter** (idealcyc kinds are C / p
  only). My r2howrand (ONEP): R = 0 on 2,683 steps of 1,000 genomes. **W-3** below.
- LEVEL0 «0 of 17,013 pairs, 3,422 states, 1,000 genomes» (level0_191.py 1000 41) ✓ reproduced; e-face identified as the
  larger-priority successor, correct in Γ ✓.
- BR-SEG-G «0 of 2,000 games» (brseg_gen191.py random 2000 3 12) ✓ reproduced. **«555 steps …» is not printed by the cited command**
  (the tool prints only H0 events among violations). My instrumented copy (brseg_r2.py / brseg_r2.out) reproduces 555 = steps with a
  switched Even vertex that is its own cycle node at t, and finds **388 of the 2,072 steps fail H0** itself. So the data is not data for
  H0 runs, and the line's number cannot be read off its source. **W-4** below.
- switchallexp N 2-7: N 2-5 in check191.out (pinned sae_2..5.pg) ✓; N 6, 7 re-run on out/sae_6.pg, out/sae_7.pg (T 630, 1243; R 116,
  241; p-run 17, 19; n_E 59, 68) ✓ (those two files are not in xicyc.pins: N-2).
- REACH3-CYC «0 / 0 / 0 in 2,167 transitions» (howard3_191.py 500 31: 1,061; 500 32: 1,106) ✓ reproduced.
- Context «22/22», «1,271 of 1,300», «29 at an exact VJ tie» (eq191 in check191.out; rand191 eq 300 1: 297/300; eq 1000 2: 974/1,000,
  26 ties) ✓ reproduced.
- DEAD SEG-2P ✓ (§8). DEAD ODD-FIXED: the line names no killed statement. **W-2** below.
- D-3 (the author's erratum «no H0 event»): correct as an erratum ✓; it is W-4's source.
- N-2 (note): the outputs of subrun191 1000 21, brseg_gen191 random 2000 3 12, level0_191 1000 41, howard3_191 500 31/32 and rand191 eq
  1000 2 are not committed; the counts stand on the seeded commands (I re-ran all of them, identical). Committing them, and pinning
  out/sae_6.pg, out/sae_7.pg, would put every L-2 number on record.

## Required line changes (each old string occurs exactly once in L-2; bt_xicyc.out)
- **W-2 (DEAD record must name the statement killed):** «and DEAD ODD-FIXED (those three runs contain 1, 8 and 6 R-steps respectively)»
  → «and DEAD ODD-FIXED («σ̄ is constant on every run of Λ-keeping steps» fails: those three runs contain 1, 8 and 6 R-steps
  respectively, each a Λ-keeping step at which σ̄ changes)»
- **W-3 (DATA unit, ONEP-POLY):** «ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes
  (seg1p191.py 300 11);» → «ONEP-POLY: in the one-player model, a Λ-keeping run longer than N, or C > N·M, in 0 of 300 genomes
  (seg1p191.py 300 11; R is not counted, R = 0 has no separate DATA);»
- **W-4 (DATA source, BR-SEG-G):** «H0 itself is not checked by the tool, which counts 555 steps in these runs where some switching Even
  vertex is its own cycle node» → «H0 is not checked by the tool, and these runs include steps at which H0 fails»
- L-2 with W-2..W-4 (my script): sha1 dbdb1e61fc230de6ff8591fc9ee46f0aa453d3d9 with its newline, 4,680 B, 1 line, 60 «(» = 60 «)».
- W-1 (F4) and G-1's repair are packet-level: a fixes entry, no line change (the line states no proof for BR-SEG-G).

## Findings
- F-1: §2-§4 SIGN (F4 after W-1); every §4 lemma re-derived; all §4 counters 0 on 2,511 genomes (11 pinned + 2,500 random), ONEP R = 0.
- F-2: §5 BR-SEG-G and RED-XI SIGN WITH GAPS (G-1): DOM / F4 are false on general games (instance r2dompex.out), PATH's induction step
  fails as written; closed by the ext⁺ repair (§5 above), checked by machine (DOM⁺ 0 / 16,384).
- F-3: §7 REACH3-CYC and Corollary T3 SIGN (conditional on [REACH-L]): no hidden Ξ-use in ESC3 or W3; xi run = Howard on 1,011 genomes.
- F-4: §8 both DEAD SIGN; instances replayed label for label.
- F-5: HMZ citation correct (opened). L-2 MATCHES after W-2, W-3, W-4.

## Tools and outputs (docs/referee-2/R2-P-N5-XICYC/; own code; si.py Engine used as the fleet reference evaluator on Γ, Γ3)
r2vjg.py (brute-force VJ Howard on general games; F4X, DOM, DOM-in-PATH, DOM⁺, ISO, STRICT, p-runs) / r2vjg.out; r2dompex.py / .out;
r2howcyc.py / r2howcyc.out; r2howrand.py / r2howrand.out; r2xval.py / r2xval.out; r2xi3.py, r2xi3rand.py / r2xi3_inst.out,
r2xi3rand.out; brseg_r2.py (brseg_gen191.py + counters only) / brseg_r2.out; bt_xicyc.py / bt_xicyc.out.
Re-run: from the repo root, `python3 docs/referee-2/R2-P-N5-XICYC/r2howcyc.py <box191/inst/*.json>` (instances from a `git archive
86afce49`); r2vjg.py SEED COUNT N; r2howrand.py SEED COUNT NMAX DMAX (ONEP=1 for the variant); r2xi3rand.py SEED COUNT NMAX DMAX.

## Addendum 1: fix round 1 / L-3 (claude/l-new 50c80a92; REFEREE-2 successor 30, 2026-11-07 09:0xZ by date -u)
- Object (sha1 at 50c80a92, equal to the Lead's relay 08:50Z): fixes a83e54d2… (14,214 B; entry 2 appended); L-3 1690b6ad… (5,543 B);
  packet 149e2414… unchanged; xicyc.pins c77781e0….
- Byte test (bt_l3.out; R1-R6 taken by script from entry 2): each old string once in L-2, each new string once in L-3; R1-R3 are my W-2,
  W-3, W-4 verbatim (old and new); **L-2 + R1..R3 = dbdb1e61fc230de6ff8591fc9ee46f0aa453d3d9, 4,680 B = my prediction**; L-2 + R1..R6 ==
  L-3 byte for byte (sha1 1690b6ad…, 1 line, 67 «(» = 67 «)», depth never negative, 0 «|») ✓.
- **W-1 closed.** F4′ is exactly my W-1 hypothesis (v ∉ Π(A) ∪ Π(B)); its added «also when v ranks below Λ(A) and Λ(B)» is a special case
  (Π holds only vertices above Λ). Every §4 use and Corollary T3's use satisfy it (movers Ω 0; PATH's non-mover z_0) ✓.
- **G-1 closed.** Entry 2 replaces §5's proof by STRICT-G and PATH-G, judged here as packet text:
  - STRICT-G: Ω_(t+1)(y′) ⊵ Ω_t(y′) ▷ Ω_t(σ_t(x)) (F1, F5); F4′ is applied to Ω_(t+1)(y′) and Ω_t(σ_t(x)), both x's own play after its
    first step (x ∉ either Π since Λ ≠ x at t and t + 1), never to Ω_t(y′). Correct ✓.
  - PATH-G (Even z_0): Ω_t(σ_t(z_0)) ⊵ Ω_(t−1)(σ_t(z_0)) ⊵ Ω_(t−1)(z_1) ⊵ val(tail) (F1, the Howard step, induction); F4′ on Ω_t(σ_t(z_0))
    (z_0's own play after its first step, Λ_t(z_0) ≠ z_0) and val(tail) (π simple). Correct ✓. It avoids exactly the value my instance
    r2dompex.out breaks (Ω_(t−1)(z_1) with z_0 ∈ Π is only compared, never extended).
  - BR-SEG-G (a)-(c) and RED-XI then hold as stated; no DOM in §5-§6 ✓. My ext⁺ route stays recorded as a second route only.
  - BR-SEG-G and RED-XI: **SIGN** (Opus 5.5, D1); the «WITH GAPS» of my report is withdrawn.
- XC-3 Lemma K2-r (σ̄(K2) = r on Γ3, every genome; σ̄(K2) = K1 on Γ): agrees with my N-1 / §7 reading ✓. XC-4 [1E-N3] premise added ✓.
  N-1 (mine), O-1, O-2, N-2 (mine: data/ outputs committed and pinned; I re-ran them, identical) ✓.
- R4 (REFEREE XC-L2): inst/sae_6.pg 5dc850b1…, inst/sae_7.pg ff46e32f… are byte copies of 86afce49's out/sae_6.pg, out/sae_7.pg;
  data/sae_6_7.out equals my re-run (run_sae67) line for line ✓. R5 (XC-L3): units match howard3_191.py (non-standard: per genome, `break`;
  non-Howard: per transition; bad stop: per genome; the fallback flag is not read) ✓; the cited docs/referee/scratch/xicyc_logs/reach3_*.out
  exist at claude/referee 695b610c (22/22 files, 300/300 random, first fallback at T3 + 1) ✓; my own r2xi3rand.out has a fallback in
  1,000/1,000 too. R6 (XC-L4) ✓.
- Verdict: entry 2 **CORRECT**; W-1 and G-1 **CLOSED**; **L-3 MATCHES** the packet with fixes entries 1-2 (Opus 5.5, D1). Every statement
  of the packet: SIGN (§7 and Corollary T3 conditional on [REACH-L], as before).
