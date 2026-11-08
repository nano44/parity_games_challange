# R223 item 1: adversary on packet P-N5-END (L-RED successor 58, Opus 5.5, D1 / D18 / D14; 2026-11-08, date -u)
Target: packet P-N5-END, FROZEN at claude/l-new 131b4c1c0b98cca2c0b40f6e9cf96c840a4deb25, docs/new/P-N5-END.md.
- Checked: `git show 131b4c1c…:docs/new/P-N5-END.md | sha1sum` = 5cae845b1da1a1c40b52e73da6edae3d6aadbf29 and `wc -c` = 22,967, both
  equal to the Lead's freeze message.
- Statements: E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5, EXACT-L (G ∈ IDEAL-ACYC, self-loops count as cycles), END-T3 (conditional).
- Lead brief (05:05Z), in order:
  - attack E0, E1, E4 with hand-built Γ3 instances;
  - check that the premises are landed and quoted exactly (R117 (f) REACH3, TAU3, R15 (c));
  - check that [OPT] for the SPEC-run σ̄ is [1E-N3] / R57 (b) (Lead reading);
  - re-run the 9 families of R222 (end222.py) on the frozen tools;
  - check Addendum 2's IDEAL-ACYC wording against my predecessor's witness SELFL_n3.
Labels: SURVIVES / BROKEN per statement; PROVED / CONJECTURE / DATA / DEAD for my own items. Every DATA clause names its counter.

## 0. Verdict
| statement | verdict | basis |
| --- | --- | --- |
| E0 (τ fixed, Iτ = ∅) | SURVIVES | proof checked (§2); [TAU3] landed for every genome; 0 failures in §3 |
| E1 (core frozen until the first fallback) | SURVIVES | proof checked line by line (§2); exhaustive N ≤ 2 (§3.2) |
| E2, E3 | SURVIVE | proof checked (§2); §3 |
| E4 (a), (b) | SURVIVE | proof checked, including the Γ3 pad lengths 5ℓ + 3 / 5ℓ + 4 (§2); §3 |
| TERM-XI | SURVIVES | [TERM] = R15 (c) is quoted exactly and applies to SPEC runs (§1) |
| ENDGAME-3, ENDGAME-3-N5 | SURVIVE | §2; 8,100 + 146,448 + 90,000 runs (§3), and 515 genomes on the SECOND implementations n5b / n5bxi + Oink (§3.3) |
| EXACT-L (IDEAL-ACYC, self-loops count) | SURVIVES | [REACH3] = R117 (f) landed (§1); wording now excludes SELFL_n3 (§4); 8,000 IDEAL-ACYC genomes incl. random topological orders (§3.4) |
| END-T3 | SURVIVES as PROVED-CONDITIONAL | one-line consequence of ENDGAME-3 and [R3C]; R118 (k) is labelled CONDITIONAL in RESULTS, as the packet says |
No break. One wording gap (W-1, §1) and one tool remark (T-1, §1); neither changes a statement.

## 1. Premises: landed, quoted exactly, scope
- Quotes. I re-ran the packet's quote check against CURRENT trunk 4aaba7d52 (`git show`) for all five source files. The packet's own
  quotes_end.py takes only RESULTS from `git show TRUNK`; it reads SPEC / XICYC / REACH / QFIX from the working tree, so at the freeze
  it read l-new's copies (T-1, a tool remark).
  - Result: 33 of 33 «…» in §1 and §6 occur verbatim (whitespace normalised) in trunk 4aaba7d52. Tool: scratch re-implementation of
    quotes_end.py with `git show` for every source; the counter is missing quotes, unit = one «…», set = §1 + §6 of the frozen packet.
    Missing: 0.
- [REACH3] = RESULTS R117 (f) (trunk 4aaba7d52, l. 13362 ff.):
  - «(f) Theorem REACH3 (§7 l. 242-258) [IDEAL-ACYC]: «Let G ∈ IDEAL-ACYC with IDEAL run …»».
  - R117 is [refereed-only], and its signature block has every row SIGN at both referees.
  - The packet uses it only for EXACT-L, with hypothesis IDEAL-ACYC. That matches.
- [TAU3]: RESULTS R117 (e) «[IDEAL-ACYC; K3 and TAU3 every genome]». P-N5-REACH §6.4 (trunk), «In the standard state, Iτ = ∅, so S4b
  leaves τ unchanged.», with the STANDARD STATE of §3: «τ(g) = pe_g at every gate, τ(K2) = K2», which is τ0 of the packet (S). So E0's
  induction base is the landed lemma.
  - TAU3's proof cites K3 (c) for K2. K3's «every genome» label was flagged as incomplete in R117's XC-3 NOTE and fixed («K3 is signed
    for every genome with fixes entry 1's reply as its proof of σ̄(K2) = r», R117 signatures). So the chain is landed for every genome.
  - E0's step «Iτ is the same at every state with τ = τ0» is the dual of R15 (d) «Iσ depends on σ alone (Ωσ is against ⊖'s optimal
    reply, not against τ)». The packet gets it from the SPEC text directly. That is correct, and R15 (d) is a second source for it.
- [TERM] = RESULTS R15 (a), (c): quoted exactly (l. 624 ff.). R15's Object is N5 as specified by SPEC, with SPEC's injective ranks
  (SPEC S1 «rank(v) = position of v in V sorted by (Ω(v), v)»), so Γ3's repeated pad priorities are covered.
- [OPT] for the SPEC-run σ̄. The packet uses [1E-N3] = RESULTS R57 (b) as landed in R104 (both forms, including S4a's σ_new as a
  pointwise optimum of H). It says explicitly that R118 (b)'s [OPT] is not used. This matches the Lead reading (R118 (b) + R21 (a) is
  the source for IDEAL-CYC's σ̄_t only; SPEC runs use 1E-N3). AGREE.
- W-1 (wording gap; changes no statement). In RESULTS, 1E-N3 is a STANDING SPEC PREMISE, not a theorem:
  - R57's heading: «under the standing SPEC premise 1E-N3»; R57 (b): «Standing premise, as in R51 (d): … that S1's procedure realises
    an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1)»;
  - R104's and R117's headings carry it the same way.
  - The packet lists [1E-N3] in §1, and E1, E3, E4 and (H) use it. But its «To sign» table gives the hypotheses of E0-E4, TERM-XI and
    ENDGAME-3(-N5) as «every genome» only.
  - Suggested fixes-file line: «Hypotheses of every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 /
    R117.»
  - E0 and TERM-XI use it too, through [TAU3] and through «τ̄ is Even's optimal counterstrategy». A packet can land with this premise
    exactly as R117 did.
- Scope (§9 of the packet) checked against TARGET.md §2 / §4. The packet bounds nothing: it does not claim M3 or M4, and G-N5-TIME stays
  OPEN. AGREE.

## 2. The proofs, re-derived (E0-E4, TERM-XI)
I re-derived every value table in §4-§5 from SPEC S1's definitions:
- p′ = 2·rank + parity, rank by (Ω, index);
- P = vertices on the play before c that are more relevant than c;
- order: reward, then signed P-weight, then length.
Points where a break could hide, and why none does:
- E1 (a), K3's options at κ0: K1 = (K1, ∅, 0) and K2 = (K1, ∅, 2) (K2 → r → K1). The node K1 is odd, so the longer is better: K2 is
  kept and (K3, K1) ∉ Iσ.
- E1 (b): A(K0) = {pA, K1}, and τ0(K2) = K2 in H. The pA-play ends in K2's loop (node K2, reward −p′(K2) > −p′(K1)). K0 lies on no
  H-cycle (A(K1) = {s}). So (H) applies and σ_new(K0) = pA, in both modes. This is the mechanism that freezes the core: Odd's τ0(K2) =
  K2 inside H.
- E3: K1 is on the H-cycle K1 q K0 but is not its node (the node is K0). TIE(K1) = {q}:
  - W*(K1) = (K0, ∅, 2) = K1 ⊕ W*(q);
  - K1 ⊕ W*(s) = (K0, ∅, 4).
- E4 (a): (β_g, pb_g) ∈ Iσ needs Ξσ(xt(g)) ◁ Ξσ(pb_g). The packet gets it from [1E-N3]: σ̄ is a pointwise optimum, so Ξσ(y) ⊴ the
  value under Odd's pe-play, which ends in c_W, and c_W has smaller reward than K0. This is correct, and it does not depend on σ at the
  movers.
- E4 (b), Γ3 lengths. Gate → pe → e → (W-target mover) → m → gate is 5 steps per level, and a level-0 gate → pe → e → c_W is 3 steps.
  So gates have (c_W, ∅, 5ℓ + 3) and mover pads (c_W, ∅, 5ℓ + 4). All options of a mover are equal, so there is no improving edge. No
  vertex above c_W lies on these plays: e's are below c_W, and K0 / K3 are not reached.
- E4 (b), Odd's reply. Every deviation from pe at a gate h goes pβ_h → β_h → pb_h → K0, node K0, the maximum reward. K2 cannot be
  reached from a gate under σ* (only K3 enters K2, and σ*(K3) = K1). So ρ* is Odd's unique optimum at gates, and the loop is its optimum
  at K2.
- TERM-XI: the N5′-xi σ_new lies in A(v) at every v, so it is Switch_I with ∅ ≠ I ⊆ Iσ, unambiguous. A fallback is a switch-all of best
  improving edges. R15 (c) applies to both. Correct.
- ENDGAME-3: «F ≥ 1» allows F = 1 (the first iteration is the fallback). This happens in the data: SELFL_n3 and exhaustive genomes with
  no movable mover.

## 3. DATA: attacks and re-runs on the frozen tools
Algorithm objects are frozen at 131b4c1c: box189 gamma3.py 8758456f…, box190 n5v.py aeaa8d01…, harness pg.py 70d23b61…, box21 n5x.py
e9c14eb4…, n5.py e3919977…, si.py e688b963…. All equal the sha1 rows of end.pins. They run in a detached worktree of 131b4c1c (WT = WT3).
Every CHECK uses L-RED's own.py (VJ order, Odd optimisation), not n5v's Engine. Modes: spec = N5, xi = N5′-xi, idx = TIE broken by the
largest index.

### 3.1 The 9 families of R222, re-run (end222.py unchanged; driver experiments/red/r223/sweep_end223.sh, seed 2231, NEW genomes)
Counter: runs with any fail counter > 0 (e0, pre, e1a, e2, e3, e4, len, nofb, fin, capped; end222.py docstring). Unit: run = (genome,
mode). Set: 9 families × 300 genomes × 3 modes. Output: experiments/red/r223/out/end_*.txt.
| family | genomes | N max | M max | runs (3 modes) | fail counters | max F (spec / xi / idx) | T = F + 2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rand | 300 | 15 | 45 | 900 | 0 | 5 / 10 / 5 | 900 / 900 |
| esc | 300 | 15 | 45 | 900 | 0 | 4 / 6 / 3 | 900 / 900 |
| noesc | 300 | 15 | 45 | 900 | 0 | 6 / 13 / 4 | 900 / 900 |
| deep | 300 | 18 | 54 | 900 | 0 | 7 / 12 / 5 | 900 / 900 |
| dense | 300 | 15 | 60 | 900 | 0 | 6 / 11 / 5 | 900 / 900 |
| lvl0 | 300 | 19 | 76 | 900 | 0 | 6 / 12 / 5 | 900 / 900 |
| late | 300 | 15 | 45 | 900 | 0 | 5 / 13 / 5 | 900 / 900 |
| self | 300 | 15 | 45 | 900 | 0 | 5 / 10 / 5 | 900 / 900 |
| wide | 300 | 9 | 54 | 900 | 0 | 5 / 10 / 5 | 900 / 900 |
Total: 8,100 runs, 0 failures. Control (CTRL=1: κ2 / κ3 swapped and «fin» evaluated at F's result; out/ctrl_rand.txt): 100 of 100
genomes BAD in every mode (e3, e4, fin fire). So the counters can fire.

### 3.2 E0, E1, E4 by exhaustive enumeration (the «hand-built Γ3 instances», all of them up to size 2)
Tool: experiments/red/r223/exh223.py, which reuses end222.check. Enumerated: EVERY genome with
- N ≤ 2 movers, level patterns [0], [0, 0], [0, 1];
- degree 1-2 per mover, every W-target;
- every Ξ-target in {X, movers}, self-loops included;
- every start, every β-parity vector;
- β-ranks identity or reversed, gate index order identity or reversed.
These are the corner cases for E0 / E1 / E4 that hand-built instances would target:
- degree-1 movers (no mover choice at all);
- all-X genomes (every β single-successor);
- all-self genomes (every β a SET loop);
- reversed index orders (SPEC's index ties);
- both β-parities.
Counter: genomes with any end222 fail counter > 0, in any mode; unit: genome × 3 modes.
- Exhaustive: 48,816 genomes (146,448 runs): 0 failures; max F 3 in every mode.
- N = 3 random (levels [0,0,0] / [0,0,1] / [0,1,1] / [0,1,2], degree 1-3, seed 2232): 30,000 genomes (90,000 runs): 0 failures; max F 4 / 6 / 4 (spec / xi / idx).
Output: experiments/red/r223/out/exh223.txt (it lists only BAD lines and the summaries).

### 3.3 Second implementations (gauntlet-step-2 style; experiments/red/r223/xend223.py)
- N5 = L-COMP's experiments/n5-second/n5b.py (mode spec, start = its own S3, fbtrace gives each fallback's position).
- N5′-xi = box190 n5bxi.py.
- Neither shares valuation code with n5v. Both are taken from the frozen tree.
- Regions are checked against Oink 8fbf0a7 --zlk (built by scripts/setup_oink.sh in this container), and strategies by
  harness verify.check.
- Counter: genomes with any failure of: n5b exactly 1 fallback, total = F + 2, (T, F) = n5v spec's; n5bxi exactly 1 fallback, total =
  n5v xi's; regions = Oink; verify clean. Unit: genome.
- Set: the 14 R117 corpus genomes (box189/corpus) + SELFL_n3 + families rand, deep, late, self, wide × 100 (seed 2234). 515 genomes,
  0 failures (out/xend223.txt).
- Corpus totals, n5b = n5v: RECT_d11_T59 62 = L + 3 with L = 59; REC_d12_mu42 51; KILL_M2D_d8_mu21 27; A_d4_W3_k3 18. N5′-xi on the same
  games: 6-12.

### 3.4 EXACT-L beyond «smaller index» (experiments/red/r223/exactl223.py)
- L-NEW's acyc family and my predecessor's selfl222 both point every Ξ-edge to a SMALLER index. SPEC's ties depend on indices, so I
  also tested IDEAL-ACYC genomes whose Ξ-edges follow a RANDOM topological order π.
- L(G) is from L-RED's experiments/red/r187/ideal.py (traj). N5 is the frozen n5v spec.
- Counter: genomes with F ≠ L + 1, T ≠ L + 3, or any end222 counter > 0. Unit: IDEAL-ACYC genome. Output: out/exactl223.txt.
  - Exhaustive: every N ≤ 2 genome of §3.2 whose Ξ-graph is acyclic (no self-loop): 5,000 genomes, 0 mismatches (L ≤ 2).
  - Random topological orders: d 1-5, width 1-3, degree 2-3, seed 2233, 3,000 genomes, 0 mismatches (L ≤ 4).
- Weak in L: the larger-L evidence remains the corpus (L up to 59, §3.3, and the packet's own 4,297).

## 4. Addendum 2's IDEAL-ACYC wording vs SELFL_n3
- The frozen packet defines IDEAL-ACYC with R104's own words: «G is in IDEAL-ACYC iff its» «Ξ-graph is ACYCLIC (self-loops count as
  cycles).» Both quotes sit in RESULTS R104 (trunk 4aaba7d52, l. 9910, inside R104's l. 9864-10154).
- SELFL_n3 (frozen copy experiments/red/r222/inst/SELFL_n3.json = the packet's inst copy, both sha1
  27bc7f725c3ae8373ee1b27ddba673c15a16dd9a) has Ξ-edges 0 → 0 and 1 → 1. These are self-loops, so it is NOT in IDEAL-ACYC.
- EXACT-L therefore does not claim it, and the gap of R222-end.md is closed.
- Replay on the frozen tools: L(G) = 1, N5 total 3, F = 1 (n5v; n5b gives T 3 / F 1 / 1 fallback; n5bxi T 5 / 1 fallback). This agrees
  with the packet's data/selfl195.out «SELFL_n3: IDEAL-ACYC False L(G) 1 N5 total 3 F 1».
- The packet's §6 also names SELFL_n3 as the necessity witness. AGREE.

## 5. Tools and reproduction (no absolute paths; WT = WT3 = `git worktree add --detach <dir> 131b4c1c0b98cca2c0b40f6e9cf96c840a4deb25`)
- `experiments/red/r223/sweep_end223.sh 2231 300 experiments/red/r223/out` (§3.1, about 15 min).
- `python3 experiments/red/r223/exh223.py experiments/red/r223/out/exh223.txt 30000 2232` (§3.2).
- `python3 experiments/red/r223/xend223.py <scratch dir> <corpus>/*.json SELFL_n3.json` and `… --fam FAM 2234 100` (§3.3; needs
  tools/oink/build/oink).
- `python3 experiments/red/r223/exactl223.py 2233 3000` (§3.4).
Not a TARGET.md claim; not M3 or M4; G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).

## 6. Sources opened
- claude/l-new 131b4c1c docs/new/P-N5-END.md (whole), experiments/new/box195/end.pins, quotes_end.py, quotes_end.out, data/selfl195.out.
- trunk 4aaba7d52 docs/RESULTS.md: R15 (l. 624-670: (a), (c), (d), limits); R57 heading and (b) standing premise (l. 2893-2952); R104
  heading (l. 9864) and IDEAL-ACYC (l. 9910); R117 heading, (e), (f), XC-3 NOTE, signatures (l. 13362-13606); R118 (k) (via the quote
  check).
- trunk 4aaba7d52 docs/new/P-N5-REACH.md §3 (standard state, l. 130-139), §6.4 TAU3 (l. 202-206); docs/new/N5-ssi-global.md SPEC S1
  (l. 25-45).
