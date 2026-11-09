# R230: adversary vs L-SI 50 Lemma B-ONLY3 on Γ3 (BOX 96, claude/l-si 6ee19b24, docs/si/box96-bonly3.md sha1 f90e872d)
L-RED successor 64 (Opus 5.5), D1 / D18 / D14. Lead «go» 09:27Z (date -u at receipt), item 1 sharpened: (a) proof read, (b) counter
census and climb. Written 2026-11-09T10:06Z (date -u). Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
Object: `git show 6ee19b24:docs/si/box96-bonly3.md | sha1sum` = f90e872d0cf174e777dafc6a15ba9e689a02d6c5 (116 lines), equal to the Lead's pin.

## 0. Verdict
- B-ONLY3 SURVIVES. I checked every case of the proof (§2 of the object) against the landed text and against the built games. All 8
  «…» quotes are verbatim in trunk (script, §1). The structural premises [RANK], [CORE] and the in-edge facts hold on every built Γ3
  (struct230.py: 0 fails on 524 genomes). Corollaries NO-E-CYCLE3, PROVISO3 and LAM-UP3 follow as written.
- The pad exception list is COMPLETE. With τ_β, the only route into c_W is e → c_W. An e can be entered only from its pe pad, and a
  pe pad only from its gate, which τ_β sends to pβ. So the vertices whose τ_β-play is forced into c_W are exactly c_W, the e's with
  successor c_W, and their pe pads.
- FRAME: B-ONLY3 is a statement about [FRAME3] states only. It covers N5′-xi's run ONLY under [STD3] and ONLY up to the first fallback.
  After the first fallback the conclusion FAILS (§3, witness MWR4_2). For Ξ-cyclic G, [STD3] rests on R118 (k) REACH3-CYC, which is
  CONDITIONAL; R117's own line states S3-START and PAD for Ξ-acyclic genomes only. If R125 (P-N5-CHAIN REACH3-ALL) lands, it would
  remove that condition (pending).
- No proof gap. There are 5 small fixes (G1-G5, §2), none of which changes a statement.
- DATA (§3): 0 in-frame violations; 0 [STD3] failures before the first fallback.

## 1. Proof read, case by case (object §2)
Quotes, checked by script: every «…» in the object (8 quotes) is a substring of the whitespace-normalised trunk text (98e1c8bee: RESULTS.md,
P-ACYC.md, P-N5-QUIET-fixes.md, P-N5-REACH.md, P-N5-REALIZE.md) or of l-si P-N5-GATE / P-N5-CHAIN: 8 FOUND, 0 MISSING.
Steps:
- [DEF3] / [RANK]. P-N5-REALIZE l. 94 «movers, gates, c_X, K2 < K1 < every β < every e < c_W < K0 < K3», plus R117's pads of priority
  ≤ 2. Checked on the built Γ3 (gamma3.build, l-new fcba92fc, all pads): the set of non-e vertices that outrank the least e is exactly
  {c_W, K0, K3}, and every e is even. 0 fails on 524 genomes (500 random Ξ-cyclic, seed 2303, plus 24 pinned r228 / r229 instances).
- In-edges. e_g's only in-edge is from pe_g, pe_g's only in-edge is from g, and c_W's in-edges are its loop plus the e's with successor
  c_W. 0 fails on the same 524 genomes.
- «level-0 e» in the proof versus «e whose successor is c_W» in the statement. These are the same set by P-N5-REALIZE l. 89 «single
  edge to wt(g), or to c_W if lev = 0». DATA: 5,725 options with W-target c_W on the 24 pinned instances, 0 of them at level > 0. → G4.
- [CORE] / K0, K3 on no cycle. In [FRAME3], σ(K0) = pA, σ(K1) = s and σ(K3) = K2. K3's only in-edge is pA, and pA's only in-edge is
  K0. Every edge from outside the core ends at K0. So nothing returns to K0, whatever Odd does. 0 fails on 524 genomes.
- τ_β step. τ_β is positional. Under (σ, τ_β) no e is on a cycle, and c_W is on v's play only for v in the exception list (§0).
- Reward step. w′ is less relevant than every e. A less relevant vertex has a smaller reward whatever its parity, because the e's are
  even. Then [OPT] and [VJ] give reward(Λ(v)) ≤ reward(w′) < the least e-reward, which excludes e's and c_W (K0 and K3 are excluded as
  cycle nodes). Correct.
- NO-E-CYCLE3. A cycle through e_g passes D = succ(e_g). D = c_W is impossible, since c_W's cycle is its own loop. So D is a mover, not
  an exception, and B-ONLY3 at D contradicts the cycle containing e_g. Correct. Note that e's successor on Γ3 is the mover itself, not
  a pad (gamma3.build: succ[e] = [wt]).
- PROVISO3. If e_o were on D's play, the play would close at D through e_o, contradicting NO-E-CYCLE3. Correct.
- LAM-UP3. Correct as written.

### Small fixes (no statement changes)
- G1 [OPT] citation. The lemma only needs σ̄ to be pointwise ⊴-optimal against σ. That is [OPT] as R123 lists it: «= RESULTS R118's
  σ̄ … (F3's proof … «σ̄_t is optimal at every vertex at once ([VJ])»)». R123 says of R57 (b): «concerns the output of SPEC's S1
  procedure and is not used». The object cites R57 (b) / [1E-N3]; that premise belongs to the APPLICATION in §3, where N5′-xi's σ̄ is
  S1's output, not to the lemma itself. Separate the two.
- G2 Scope sentence. Add to §3: «B-ONLY3 says nothing about N5′-xi's states after its first fallback; there its conclusion fails (L-RED
  R230, MWR4_2 states 32-33).» Also name [STD3]'s status for Ξ-cyclic G: R118 (k) is CONDITIONAL, and R125 is pending.
- G3 Face transport. P-N5-GATE's K10 / LAM / UP are read on the gate faces. On Γ3 the faces are pe_o and pβ_o. For every
  single-successor vertex v, Λ(v) = Λ(succ v): v's play is v followed by succ(v)'s play, and if v is on the cycle it is the same cycle.
  So Λ(pe_o) = Λ(e_o) and Λ(pβ_o) = Λ(β_o). Add this one line before «(a) G1's Γ3 clause».
- G4 Wording. Write «e whose successor is c_W» in the proof (it currently says «level-0 e»), or cite P-N5-REALIZE l. 89 for the
  equality.
- G5 DATA counter. d96.py's exceptions are a run-dependent closure: «single-successor vertices whose successor is an exception», with
  successors collected over the run, so the closure is wider than the stated list in principle. By the in-edge facts (above) it equals
  the stated list (only pe pads have an exception as successor), so the DATA is unaffected. Say so, or use the static list as
  bonly3_230.py does.

## 2. Counter side (DATA; tool experiments/red/r230/bonly3_230.py, l-red 328a6fe28, sha1 09e5866d)
Engines: values from L-SI si.Engine; Γ3 from L-NEW gamma3.build (all pads); N5′-xi from L-NEW n5v.py mode xi (l-new fcba92fc); second
engine BRUTE = minimum over all Odd positional strategies (M ≤ 8). Exceptions: c_W, e's with successor c_W, and their pe pads (static).
Violation: v not an exception, and rank(Λ(v)) ≥ the least e-rank. Unit: (state, vertex) pairs unless stated.
| set (count of genomes) | FRAME-X pairs / viol | Howard states / tie states / viol | XI-STD states / viol | XI-NSTD viol | brute states / diff | early non-std |
| --- | --- | --- | --- | --- | --- | --- |
| rand 2301 (400, d 1-4, w 1-3, deg 2-3, XCAP 512) | 10,429,449 / 0 | 1,293 / 294 / 0 | 1,293 / 0 | 46,510 | 2,045 / 0 | not counted |
| rand 2302 (1,500, same, XCAP 32) | 3,760,023 / 0 | 4,926 / 1,177 / 0 | 4,925 / 0 | 178,138 | — | 0 |
| 24 pinned r228 / r229 instances (XCAP 128) | 4,898,560 / 0 | 1,235 / 2 / 0 | 1,235 / 0 | 54,013 | — | not counted |
- FRAME-X: every mover state with σ = transported start off the movers (exhaustive if ∏ deg ≤ XCAP, else XCAP random states).
  Howard: Howard at the movers on Γ3; tie states have some mover with ≥ 2 equal best keys (exact VJ tie). XI-STD / XI-NSTD: N5′-xi
  states from S3 that are / are not standard. Early non-std: non-standard states before the first fallback, i.e. an [STD3] failure
  (unit: states).
- Tie divergence. On 13 of the 1,900 random genomes, N5′-xi's trajectory differs from my Howard tie rule (keep current, then larger
  index). Every one of the 13 has a Howard tie state, and every state on both runs is standard with 0 violations.
- Climb: SKIPPED for in-frame violations. The proof makes the in-frame score identically 0, so a climb has nothing to climb. The
  [STD3] score «early non-std» was 0 on all 1,500 seed-2302 genomes. A climb on it targets R118 (k) / R125, not B-ONLY3; I left it
  for the Lead to route.

## 3. Out of frame (DATA; a witness, not a refutation)
- Witness: experiments/red/r229/inst/MWR4_2.json, `git show 328a6fe28:experiments/red/r229/inst/MWR4_2.json | sha1sum` = 856d369b.
  N5′-xi from S3 on Γ3: T3 = 30, first fallback at iteration 31 (switches K0), iteration 32 switches K1. At states 32 and 33, 820
  (state, vertex) pairs at non-exception vertices have Λ = c_W (vertex 340).
- All XI-NSTD violations above (278,661 pairs) are at post-fallback states. 275,877 of them have Λ ∈ {c_W, K0, K3}; the rest have Λ an
  e-vertex (rand 2301: 663; rand 2302: 2,121; pinned: 0).
- So PROVISO3, LAM-UP3, NO-E-CYCLE3 and the three removed caveats of object §3 hold for N5′-xi on states 0, …, T3 only, under [STD3].

## 4. Sources opened
docs/RESULTS.md R117, R118 (a), (k), R122, R123 (trunk 98e1c8bee); docs/new/P-N5-QUIET-fixes.md entry 1 (B-ONLY's proof);
docs/red/P-N5-REALIZE.md l. 89-94 (trunk); l-new fcba92fc experiments/new/box189/gamma3.py, box190/n5v.py; l-si 6ee19b24
docs/si/box96-bonly3.md, experiments/si/box96/d96.py.
