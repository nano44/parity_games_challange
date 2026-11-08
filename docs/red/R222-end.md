# R222 item 3: adversary vs L-NEW 63 box 195 (Theorem ENDGAME-3 / ENDGAME-3-N5, Lemmas E0-E4, Corollary EXACT-L) (L-RED successor 57)
Lead target 03:22Z 2026-11-08. Target: claude/l-new a42838357, docs/new/N5-END-box195.md (211 lines, 21,627 B, sha1
b4da3523e2a08b66adc65d4d848a982673b96fdc via `git show a42838357:docs/new/N5-END-box195.md | sha1sum`).
- Addendum 1 (EXACT-L scope, d46de131) was NOT on origin when I fetched (03:2xZ; claude/l-new head = a42838357). It is not covered here.
- Referee files not read. L-NEW's eg195.py / check195.sh / quotes195.py not run and not imported.
Labels: SURVIVES / BROKEN (frozen instance + sha1) / GAP / DATA (unit, set, scope, counter) / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/red/r222/end222.py, selfl222.py.
- The RUNS use the algorithm objects themselves: box 190 n5v.step in modes spec (N5), xi (N5′-xi) and idx (S4a's TIE broken by the
  largest index), on box 189 gamma3.build (all pads), from box 191 n5x.start_pair (S3). These are the objects the theorems are about.
- Every CHECK is L-RED code: own.py's VJ order and Odd optimisation re-evaluate the states. Nothing is read from n5v's Engine values.
- L(G) comes from L-RED's r187 ideal.traj.

## 0. Verdicts
| statement (box 195) | verdict | evidence |
| --- | --- | --- |
| Lemma E0 (τ fixed) | SURVIVES | proof re-derived (§1); premise TAU3 checked at its source: «standard state» τ = τ0 exactly, signed «every genome» (R117 entry, RESULTS l. 13438, 13807); DATA e0 = 0 |
| Lemma E1 (core frozen; (K0, K1) ∈ Iσ; S4a keeps pA) — Lead's (b) | SURVIVES | genome-independent arena computation re-derived (§2); DATA pre = 0, e1a = 0 at S3 and at every fallback input |
| Lemma E2 (first fallback → κ1) | SURVIVES | DATA e2 = 0 |
| Lemma E3 (K1 → q) | SURVIVES | DATA e3 = 0 |
| Lemma E4 (K3 → K1, every β → pb; final ties) — Lead's (a) | SURVIVES | E4 (b)'s values are all (c_W, ∅, ·) or have node K0; no pad / gate / β priority can enter Π (§3); DATA fin = 0 (own valuation: Iσ = ∅, mover options tie, gate optimum strict, gate value (c_W, ∅, 5ℓ + 3)) |
| Lemma TERM-XI | SURVIVES | R15 (c) applies as stated (σ_new = Switch_I(σ), I ⊆ Iσ) |
| Theorem ENDGAME-3 (N5′-xi) | SURVIVES | 0 counterexamples (§4 table) |
| Theorem ENDGAME-3-N5 — Lead's (c) | SURVIVES | (H) is used only at K0, K1, K3 and the β's, where the TIE is a singleton (§2-§3); DATA: N5, N5′-xi and the idx tie rule all give exactly one fallback and F + 2 in every run, while F itself differs between the rules in many runs |
| Corollary EXACT-L — Lead's (d) | GAP (wording) | true for G ∈ IDEAL-ACYC (R104: «self-loops count as cycles»), which is what R117 (f) REACH3 states and what eg195.acyclic tests; FALSE if «acyclic Ξ-graph» is read without that clause: SELFL_n3 (§5) |
| Corollary END-T3 | SURVIVES as a conditional | it is ENDGAME-3 + R118 (k); nothing new to attack |

## 1. E0 (re-derived)
- [SPEC] computes Iτ «on G^d»: Ξτ uses τ and Even's optimal counterstrategy τ̄ to τ. So Iτ is a function of τ alone; σ does not enter.
- TAU3 (P-N5-REACH §6.4, «every genome», signed in R117's entry) states Iτ = ∅ in the standard state.
- The standard state's τ is «τ(g) = pe_g at every gate, τ(K2) = K2» (P-N5-REACH §3, «Transport»). That is box 195's τ0.
- So Iτ(τ0) = ∅. S4b then never fires, and S4c touches τ only when Iσ = ∅. E1 gives Iσ ∋ (K0, K1) before the fallback; E4 (b) gives
  Iσ = ∅ only at the end.
- Small reading note, not a gap: TAU3's proof handles K2 through K3 (c). K3 is «every genome» in R117 (e), and the XC-3 note concerns
  K3 (b), not (c).

## 2. E1, E3 and the core part of E4 (re-derived; the Lead's (b))
- The core Kc = {K0, K1, K2, K3, pA, s, q, r} is closed. Its values depend only on κ and on Odd's choice at K2. So E1-E4's core claims are
  one finite computation per κ, the same for every genome. I re-did each one with own.py's VJ on a real Γ3 (end222.py «e1a» at S3 and
  at each fallback input). The data agrees with the hand derivation.
- E1 (b), «S4a keeps pA»: in H, Odd follows τ0 (K2 → K2), so K0 → pA → K3 → K2 ↺ has node K2. K0 → K1 → s ↺ has node K1. Even prefers
  node K2 (reward −p′(K2) > −p′(K1)), and K0 is on no H-cycle.
  - So the arena comparison under the CURRENT τ keeps pA. Under the best response σ̄(K2) = r, by contrast, (K0, K1) is improving.
  - That is exactly the S4a / Iσ split R221 E1 read. The proof uses the landed SPEC text for both, and nothing else.
- The (H) uniqueness (Lead's (c)):
  - K0 at κ0: K0 ⊕ W*(K1) has node K1 ≠ node K2.
  - K1 at κ1: K1 ⊕ W*(s) = (K0, ∅, 4) ≠ (K0, ∅, 2).
  - K3 at κ2: node K0 vs node K2.
  - β_g at κ2: node K0 vs node c_W.
  - In each case the other element of A(v) gives a different value, so every pointwise optimum of H makes the same choice there.
  - Movers are never used. ENDGAME-3-N5 inherits nothing from SPEC's tie key.

## 3. E4 (b), the tie claim (the Lead's (a))
At σ* (κ3, every β on pb), Odd's least value at every gate is (c_W, ∅, 5ℓ + 3). Leaving the pe-play at any gate h leads through pβ_h,
β_h, pb_h to K0 → K1 → q → K0 ↺ (node K0, the largest reward), so that optimum is strict.

Why no priority choice can break the tie:
- Every vertex on a pe-play other than c_W is below c_W: pads ≤ 2, gates 1, movers 0, e-vertices below top. Π of a value with node
  c_W holds only vertices above c_W, i.e. K0 and K3, and those are not on the play. So Π = ∅ for every gate value. Mover option values
  differ only in length, and length is 5ℓ + 4 for every option of a level-ℓ mover.
- The pad / gate / β priorities that a genome can vary (br, bp, gate order, the start's m-pads at Ω 2) enter neither the node nor Π.
- [G3] fixes every pad's Ω, so «unusual pad priorities» are outside Γ3's definition.

The real premise is (W): «W-targets have level lev − 1; level-0 e's go to c_W». It is R104's genome format, and the length count
5ℓ + 3 depends on it. A genome outside R104's format (a W-target two levels down) would give unequal lengths; that is not a genome.

DATA: fin = 0 in every run (§4). The check re-evaluates the final state with own.py and tests:
- Iσ = ∅ at every Even vertex;
- all options of every mover equal;
- pe strictly below pβ at every gate;
- each gate's value is exactly (c_W, ∅, 5·lev + 3).

## 4. DATA (end222.py; outputs experiments/red/r222/out/end_*.txt)
Unit: one genome, run in the three modes spec / xi / idx. Scope: n5v on Γ3 from S3; checks by own.py.
- Counters (0 = the claim held): e0, pre, e1a, e2, e3, e4, len, nofb, fin, capped (definitions in end222.py's docstring).
- Families: L-RED 56's spost221 generators (rand, esc, noesc, deep, dense, lvl0), L-RED's REAL «late» (each mover starts at its
  option of LEAST own.py final IDEAL-CYC value; L-NEW used an index stand-in), self (60 % Ξ self-loops), and wide (degree 4-6).
- Seed 2221, 300 genomes per family.
- Control (CTRL=1, κ2 / κ3 swapped, fin evaluated at F's result state): e3, e4 and fin fire in 3 / 3 runs per mode, so the counters work.

| family | genomes | N max | M max | runs (3 modes) | fail counters | max F (spec / xi / idx) | genomes with F not equal in all 3 modes | T = F + 2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| rand | 300 | 15 | 45 | 900 | 0 | 5 / 11 / 4 | 255 | 900 / 900 |
| esc | 300 | 15 | 45 | 900 | 0 | 4 / 6 / 4 | 211 | 900 / 900 |
| noesc | 300 | 15 | 45 | 900 | 0 | 6 / 9 / 6 | 258 | 900 / 900 |
| deep | 300 | 18 | 54 | 900 | 0 | 5 / 11 / 5 | 289 | 900 / 900 |
| dense | 300 | 15 | 60 | 900 | 0 | 6 / 11 / 5 | 258 | 900 / 900 |
| lvl0 | 300 | 19 | 76 | 900 | 0 | 7 / 12 / 5 | 272 | 900 / 900 |
| late | 300 | 15 | 45 | 900 | 0 | 6 / 11 / 5 | 277 | 900 / 900 |
| self | 300 | 15 | 45 | 900 | 0 | 5 / 12 / 5 | 245 | 900 / 900 |
| wide | 300 | 9 | 54 | 900 | 0 | 6 / 10 / 5 | 259 | 900 / 900 |

Total: 2700 genomes, 8100 runs, 0 with a failing counter; 2324 genomes have different F in different modes.
- Every counter is 0 in every run of every mode. N5 (spec), N5′-xi (xi) and the idx rule give different F in 2,324 of the 2,700 genomes
  (the tie rule matters before the fallback), and still each has exactly one fallback and T = F + 2.
- Deep reaches d 9 (N 18); wide has degree up to 6; lvl0 reaches N 19, M 76. Raw lines: out/end_<family>.txt (out/end_table.txt).

## 5. EXACT-L's scope (the Lead's (d)): GAP in wording, frozen witness
- R117 (f) states REACH3 for «G ∈ IDEAL-ACYC». R104 defines «G is in IDEAL-ACYC iff its» «Ξ-graph is ACYCLIC (self-loops count as
  cycles).» (RESULTS l. 9910).
- Box 195's EXACT-L says «For every genome G with an acyclic Ξ-graph» (l. 13, l. 167) and never mentions self-loops. eg195.acyclic does
  count a self-loop as a cycle (col[x] = 1 when y = x), so L-NEW's DATA is on IDEAL-ACYC.
- selfl222.py (unit: genome; L from r187 ideal.traj; N5 = n5v spec on Γ3 from S3):
  - Ξ-edges to smaller indices only (IDEAL-ACYC): 200 genomes, 0 mismatches of F = L + 1 / T = L + 3.
  - Ξ self-loops allowed (p = 0.3): 22 of the 274 genomes with a self-loop mismatch. Their IDEAL runs end «stuck».
  - Smallest witness: experiments/red/r222/inst/SELFL_n3.json (sha1 27bc7f725c3ae8373ee1b27ddba673c15a16dd9a; N 3, M 6, two Ξ
    self-loops).
    - L(G) = 1 (IDEAL run (1,0,1) → (1,0,0), stuck).
    - N5 from S3: F = 1, T = 3 ≠ L + 3 = 4.
    - ENDGAME-3 itself holds there: T = F + 2 in all three modes.
- Fix: say «G ∈ IDEAL-ACYC (R104: self-loops count as cycles)» in EXACT-L's statement and in the Consequence sentence. With that
  wording, EXACT-L follows from R117 (f) (premises as landed in R117's title) and ENDGAME-3-N5, and it SURVIVES.
- I have not seen Addendum 1 (d46de131). If it already says this, the GAP is closed.

## 6. What this does not give (READING)
- ENDGAME-3 accounts exactly for the end of the run: one fallback, then 2 iterations. All the open cost is in F, i.e. T3 or L(G).
- With R222-cyc.md's RHO-CYC-0, the gate-flip part of T3's accounting has no open A-premise under [OPT]. What remains open for N5′-xi on
  Γ3:
  - REACH3-CYC (R118 (k), CONDITIONAL);
  - the Γ3 transfer of T-QUIET / UP-T (box 195 §6 READING);
  - unbounded U(G).

## 7. Sources opened
- claude/l-new a42838357 docs/new/N5-END-box195.md (all); experiments/new/box195/eg195.py l. 38-46 (acyclic()) only.
- trunk docs/RESULTS.md: R117 entry l. 13362 (title), l. 13438-13460 ((e) transfer lemmas, (f) REACH3, (g)); R104 l. 9910 (IDEAL-ACYC
  definition); R118 l. 13707-13708, 13807 (TAU3 every genome).
- trunk docs/new/P-N5-REACH.md §3 (standard state, «Transport»), §6.4 (TAU3).
- claude/l-new f09f67ec experiments/new/box189/gamma3.py (the Γ3 builder, read to map vertices).
