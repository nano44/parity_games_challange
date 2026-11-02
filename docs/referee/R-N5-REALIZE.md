# R-N5-REALIZE: REFEREE report on P-N5-REALIZE (L-RED successor 45)
REFEREE successor 22, 2026-11-02T03:36Z by date -u (Opus 5.5, D15). Packet claude/l-red e609c5d2, docs/red/P-N5-REALIZE.md (sha1 067f06b6…, 278
lines); line docs/red/P-N5-REALIZE-line.txt (sha1 53dd6e9f…). Written before reading docs/referee-2/ on this packet. Lead readings:
L41 (lane-authored; nothing referee-originated), L43 (no DEAD here), L45 (not needed), L46 (the [RULE] citation).
Sources checked:
- SPEC docs/new/N5-ssi-global.md S1-S5, FIX 2-4, Q1-Q4.
- RESULTS R57 (1E-N3); R103 (its citing line is quoted verbatim in the packet, 1 match in trunk RESULTS c7522b86); R15 side finding.
- L-LIT T21-VJ00-check.md (c) «Unaffected: a stop with no improvement is optimal: BRICS Lemma 5.8 "1 ⇒ 2"».

## 0. Verdicts
| § | item | verdict |
| --- | --- | --- |
| 1 | Fact DUAL | **SIGNED** |
| 2 | Fact X | **SIGNED** |
| 3.2 | Lemma K (a)-(d) | **SIGNED** |
| 3.3 | Lemma PLAY | **SIGNED** |
| 3.4 | Lemma SBAR | **SIGNED** ([VJ-LOC] used only in the «1 ⇒ 2» direction ✓) |
| 3.5 | Lemma TAU | **SIGNED** |
| 3.6 | Lemma ESC | **SIGNED** |
| 3.7 | Lemma W | **SIGNED** |
| 3.8 | Lemma KEY (a), (b) | **SIGNED** (KEY (b) needs the e-index layout; see REAL-L1) |
| 4 | Theorem REALIZE | **SIGNED** (the IDEAL stop is an S4c fallback ✓; precisions REAL-P2, REAL-P3) |
| 5 | Corollary REAL-IDEAL (a), (b) | **SIGNED** |
| — | [RULE] citation vs Lemma W (iii) | the **bridge B** part is redundant; the **Lemma R + TB steps** part is NOT (REAL-P1) |
| 6, 7, 8 | scope, DATA, READING | ✓ labelled; pins re-run by my engine (§5) |
| — | RESULTS line | **REQUIRED REAL-L1** (the e-index order is missing from the line's Γ(G)) |

No gap in the mathematics.

## 1. §1-§2: Fact DUAL, Fact X, premises
- Fact DUAL ✓. Ω + 1 keeps the ranks (sorted by (Ω, v)), and P-membership is rank > rank(c). Rewards map by x ↦ −x − 1, which
  reverses the order (2r ↦ −2r − 1; −(2r + 1) ↦ 2r). The signed weights flip sign. The length rule flips with c's parity. So G^d's
  order is Γ's reversed: Iτ(v) = {w : Ξτ(w) ◁ Ξτ(τ(v))}, and τ̄ maximises Γ's order.
- Fact X ✓. b is a bijection on options, so b(x, k) belongs only to (x, k). After its first option, the chain of (x, k′) visits only
  movers reachable from x by ≥ 1 Ξ-edge. In an acyclic Ξ-graph that excludes x, so b(x, k) ∈ B(x, k) \ B(x, k′). The cycle node (T)
  is common, so the β of top rank in the symmetric difference decides, and lengths never do.
- [VJ-LOC] ✓. SBAR (ii) uses «no Odd-improving switch for ρ ⇒ φ_(σ,ρ) = Ξσ»: Lemma 5.8 «1 ⇒ 2» in G^d's one-player game Γ_σ. That is
  the direction T21 (c) lists as unaffected. The failing «2 ⇒ 1» (an improvement at a maximum) is not used anywhere.
- [1E-N3] ✓ for S4a (R57) and for S1's σ̄ (SBAR (iii)). S4b is never run (Iτ = ∅), so R102 / L45 is not needed.

## 2. §3: the lemmas (checked step by step against §3.1's construction)
- Rank facts ✓ (Ω 0, 1, 2, 3 < 5 < 6 … bmax < eb … < top < top + 2 < top + 3).
- Lemma K ✓.
  - (a) The plays and P-sets are as stated. σ̄(K2) = K1: the K1-cycle has reward −p′(K1) < −p′(K2).
  - (b) The three comparisons are correct: K3 odd at the top of {K3}; K3 above K0 in {K0, K3}; the odd node K1 with the longer K2.
  - (c) τ(K2) = K2. Even can close K1 → K0 → K1 (node K0 even), so Ξτ(K1) ⊳ Ξτ(K2).
  - (d) In H, K0 → {K3, K1} and K0 is on no cycle. K3's branch ends at K2 (reward −p′(K2) > −p′(K1)), so the optimum keeps K0 → K3.
- Lemma PLAY ✓.
  - The β-chains are finite and repeat no mover (acyclic). They end via u in K, which is closed, and pass no e, c_W or c_X.
  - P = B(g) ∪ {K0, K3}: movers, gates and K2 lie below K1; the β, K0 and K3 lie above.
  - φ(g) = g ⊕ φ(β_g): g is not on β_g's play (acyclic).
- Lemma SBAR ✓.
  - (i) At a gate of level ≥ 1, the symmetric difference of the two P-sets has top e_g, which is even, so β is strictly better for Odd.
    At level 0, the node is c_W (even) against K1 (odd). At K2 the longer play has an odd node, so the switch is worse for Odd.
  - (ii) [VJ-LOC].
  - (iii) Uniqueness against SPEC's σ̄. Both cases hold:
    - g on its own cycle: that cycle avoids K, c_W and c_X, so an e-vertex is its top and its node is even.
    - otherwise: g ⊕ φ(e_g) ≠ g ⊕ φ(β_g), by the cycle node at level 0 and by e_g ∈ P at level ≥ 1.
    - K2's self-loop has node K2 ≠ K1.
- Lemma TAU ✓. Under τ (e at every gate), Even can never reach a β from e_g: β-vertices are entered only from gates, by the β-edge τ
  does not take. So every play from e_g ends at c_W. From β_g, Even closes β_g → u → K1 → K0 → K1 (node K0 above c_W). Strict. The
  ESC remark is consistent.
- Lemma ESC ✓.
  - From xt(g) every H-play ends at c_W (even). From u every H-play ends in an odd cycle (K (d)).
  - β_g has in-edges only from gates, which follow τ to e in H, so β_g is on no cycle of H and the optimum keeps β_g → xt(g).
  - K: by K (d). e, c_X and c_W have single edges.
- Lemma W ✓.
  - Three steps per level: mover → gate → e → lower mover, ending e → c_W. All of these lie below c_W, so P = ∅ and the length is
    3ℓ + 3. The value does not depend on s or on the H-strategy at movers.
  - (iii) x ⊕ (c_W, ∅, 3ℓ + 2) = (c_W, ∅, 3ℓ + 3) for every option. No corner: an option's play visits only lower levels before c_W.
    So TIE(x) = R(x).
- Lemma KEY ✓.
  - (a) S2 compares Ξσ at the gates (SBAR + PLAY). Fact X decides by the top β. The β order (Ω = 6 + 2br + bp) and parity match
    fastcyc's (4 + 2br + bp above T).
  - (b) Read root-first, the key is (e_(g_0), g_0, m_0, e_(g_1), …, e_(g_ℓ), g_ℓ), of length 3ℓ + 2. The first difference is at an
    e-vertex, because a gate determines its owner and its e. The keys compare as gate-index sequences, i.e. as the IDEAL keys, **if and
    only if e-INDICES follow gate-index order**. §3.1 builds them that way («allocated in GATE-INDEX order»); see REAL-L1. (e's
    PRIORITY order by (lev, gate index) is not used by any lemma; only «even and above every β» is.)

## 3. §4 Theorem REALIZE, §5 Corollary REAL-IDEAL
- Induction on standard states ✓.
  - τ is kept (TAU). Iσ ≠ ∅ (ESC). σ is kept off the movers (ESC).
  - Movers, by level: [RULE] at x, which is not its own W′-cycle node (c_W), with TIE = R(x) (W (iii)). R(x) = the gates of A_s(x)
    (KEY (a)). The κ order is the IDEAL key order (KEY (b), with σ_new = σ^(s′) below level ℓ by the inner induction).
  - So the next state is standard and the transition is FL: W is the same for every standard state (W (i)), and σ changes.
- **The IDEAL stop is an S4c fallback ✓.** In both cases σ_new = σ and τ_new = τ:
  - «opt»: R(x) = {σ(x)}, so σ_new(x) = σ(x).
  - «stuck»: the κ-least choice is s_L(x).
  Iσ ∋ (K0, K1) ≠ ∅, so S4c fires on Even's side. FIX 3 keeps τ.
- Maximality ✓. [0, L] is a maximal FL run.
- Corollary ✓.
  - Sizes: bmax = 2M + 5, eb = 2M + 6, max Ω(e) = 4M + 4, top = 4M + 6, K3 = 4M + 9. n = N + 3M + 6 ≤ 3(N + M) + 6, and with p
    nondecreasing, q(t) = p(3t + 6).
  - (a) needs FL-POLY over EVERY start pair, and (σ_0, τ_0) is a valid one.
  - (b) holds from the given start only, as stated. The converse and S3 are not claimed ✓.
- Precisions (optional):
  - REAL-P1: in [RULE], «with bridge B» is redundant here, since Lemma W (iii) gives full optimality of EVERY option directly. The
    citation of R24 (a) Lemma R + TB steps 1, 3-5 is NOT redundant: it gives «σ_new(x) is the κ-least element of TIE(x)», which no lemma
    of the packet proves. Keep the CF-1 line, or say «bridge B's conclusion by Lemma W (iii)».
  - REAL-P2: for L(G) = 0 there is no FL transition, so «[0, L] is one FL run» should read «no FL run» (or «of length 0»). §7 has
    random genomes with L = 0.
  - REAL-P3: L(G)'s finiteness (§2) is argued via REALIZE plus termination (R15). That is not circular: the induction realises every
    IDEAL step that exists, so an infinite IDEAL run would give an infinite N5 run. Say so in one clause.

## 4. Line (53dd6e9f)
- **REAL-L1 (REQUIRED).** The line's description of Γ(G) gives priorities and edges but no vertex INDICES. The TB / [RULE] key compares
  vertex indices, and KEY (b) equates them with the IDEAL keys only because e-vertices are indexed in gate-index order. With another
  e-index order the proof of REALIZE does not go through. I have not built a counterexample: this is a gap in the line's
  construction, not a claimed failure. Add «e-vertices indexed in the order of their gates' gate indices (packet §3.1)», or cite §3.1
  for the construction.
- Optional: REAL-P1 (bridge B); «top» is defined only implicitly («the top even self-loop c_W»); the line has no «lane-authored» label
  (L41 needs none here, since nothing is referee-originated).
- Otherwise ✓:
  - The premises match §1 (R57, the R103 citing line, VJ00 5.8 «1 ⇒ 2»).
  - The genome, step and key descriptions match §2.
  - The theorem and corollary clauses match §4-§5.
  - DATA is labelled «DATA» with its exact scope.
  - «a REDUCTION / NECESSITY statement only (no count is bounded …); G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md
    claim» ✓. No DEAD (L43 ✓). TARGET.md diff: no bound, no algorithm claim.

## 5. DATA: pins re-run (own engine; docs/referee/scratch/realize_probe.py, realize_logs/)
realize_probe.py uses rl_engine only. It takes the layout from §3.1 (M = #Odd − 1, N = n − 3M − 6) and checks, at every state from the
pin start:
- the state is standard (σ = σ_0 off the movers, τ = τ_0);
- SBAR (σ̄ at every gate is its β, σ̄(K2) = K1), TAU (Iτ = ∅), ESC ((K0, K1) ∈ Iσ), Iσ ∩ K = {(K0, K1)} (K (b)), W_j = W_0;
- FL transitions 1..L and a fallback at L + 1.

| pin (sha1 .pg / .start = packet) | n, N, M | my L_FL | fallback at | violations |
| --- | --- | --- | --- | --- |
| x3_L8_n48 (158ca15d / f07be770) | 48, 6, 12 | **8** | 9 | 0 |
| g4_L12_n62 (658f4e23 / 9f3e1f92) | 62, 8, 16 | **12** | 13 | 0 |
| stab_d4_n126 (06f81991 / 337b0115) | 126, 12, 36 | **32** | 33 | 0 |
| stab_g24_n246 (55295dd8 / 3cd50ed1) | 246, 24, 72 | **64** | 65 | 0 |

- Honest limit: I did NOT check that the mover states equal the IDEAL ones (that needs an IDEAL simulator; lemck / realck are the lane's).
- I did not re-run Oink or n5b on these pins.
- My engine's run has exactly the stated FL-run length, starting at state 0, with every gadget lemma holding at every state.
- The [RULE] at movers is covered by my earlier games-wide check (R-R24-L44 Addendum 1, R-N5-ANCHOR §6).

## DONE / FINDINGS / NEEDS
- DONE: this report; scratch/realize_probe.py; scratch/realize_logs/.
- FINDINGS:
  1. Every to-sign item is SIGNED, with no gap: Facts DUAL and X, Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY, Theorem REALIZE (the IDEAL
     stop is an S4c fallback) and Corollary REAL-IDEAL (a), (b).
  2. [VJ-LOC] is used only as «1 ⇒ 2».
  3. [RULE]: the bridge B part is redundant (Lemma W (iii)); the Lemma R + TB-steps part is needed.
  4. Line: REQUIRED REAL-L1. The e-index order (gate-index order) is missing from the line's construction, and Lemma KEY (b) depends
     on it.
  5. All 4 pins reproduced by my engine: FL runs of 8 / 12 / 32 / 64 from state 0, a fallback right after, and 0 lemma violations.
- NEEDS: Lead: REAL-L1 (and optional REAL-P1..P3) to L-RED; I word-diff the revision when sent.

## §C (2026-11-02T05:57Z by date -u, successor 22; Opus 5.5, D15): word-diff of line L-1
- Revision: claude/l-red 02dfc35c. Line L-1 is docs/red/P-N5-REALIZE-line-L1.txt (sha1 1d72ee31…). The fixes file is
  docs/red/P-N5-REALIZE-fixes.md (sha1 864cad59…), entry 1. The frozen packet (067f06b6) and line (53dd6e9f) are unchanged at
  02dfc35c (sha1s re-taken). Diff: `git diff --no-index --word-diff` against 53dd6e9f.
- Exactly the six listed changes. Nothing else changed:
  1. 1E-N3 gloss (REFEREE-2 REAL-L1): R57 (b)'s words, verbatim, «read on every valid input of S1's procedure (Lead reading L45, RESULTS
     R102)», in two forms. First, S1's σ̄ and τ̄ on the dual game are pointwise optima. Second, S4a's σ_new is a pointwise optimum of
     its arena, before S4c. This is accurate and covers every use: SBAR (iii) uses σ̄, K (c) and TAU use τ̄ via Fact DUAL, and the
     theorem uses S4a. The arena's σ, τ are generic, which is fine.
  2. Parity direction (REFEREE-2 REAL-L2): «the option whose set contains that β is the better one if its parity is even and the worse
     one if odd». This matches Fact X ✓.
  3. **My REAL-L1: met.** «vertex indices: movers, gates in gate-index order, β-vertices, e-vertices in the order of their gates' gate
     indices, the unused loop, c_W, K0 to K3 (packet §3.1), on which the root-first key comparison depends». This matches §3.1. «top» is
     defined («the least even number at least 2 above every other priority so far» = §3.1's «least even ≥ 2 + max Ω so far») ✓.
  4. β → «its Ξ-target (u when the target is X)» (REFEREE-2 P-1) ✓ (§3.1 start).
  5. «so, if L(G) ≥ 1, [0, L(G)] is one FL run … (no FL run if L(G) = 0)». My REAL-P2 ✓.
  6. «(2026-11-02; revision L-1 2026-11-02)» ✓.
- Parentheses balance (57/57, depth never negative); «» 2/2. Scope words, DATA clause, «G-N5-TIME stays OPEN; not M3, …» unchanged ✓.
- The fixes file's REAL-P1 (Lemma R + TB essential; bridge B redundant via W (iii)) and REAL-P3 (finiteness) record my optional
  items. They are not in the line, which is fine.
- Verdict: line L-1 **MATCHES**.

### §C addendum 1 (2026-11-02T08:58Z by date -u): CHECKER C115 E-1, line L-2 (l-red c374be8f)
- **My error, recorded.** My §1 accepted [VJ-LOC] as «BRICS Lemma 5.8 "1 ⇒ 2", the direction that holds», on the strength of L-LIT
  T21 (c). RESULTS records that route as NOT established: R15 (iii), trunk RESULTS l. 649-650, «rests on VJ00 Lemma 5.8 "1 ⇒ 2",
  which uses VJ00's unproved Lemma 5.9 and Prop. 5.10». R36's Reading says «It does NOT discharge the two-player VJ00 Lemma 5.8».
  T21's «Unaffected» only says that the FAILING direction does not touch it. That is not a proof. CHECKER C115 E-1 is right. The
  lesson is in my notebook.
- (b) **Explicit confirmation: RESULTS R36 (c) Lemma P1, applied on G^d, covers SBAR (ii), in hypothesis and in orientation.**
  - Hypothesis. P1's setting is a ONE-PLAYER game: every non-Even vertex has one successor, with SPEC S1 values and order. Take Γ_σ
    (Γ with every Even vertex restricted to σ(v)) and pass to its dual: owners swapped, Ω + 1. Γ's Odd vertices (the gates and K2) are
    the dual-Even players. Γ's Even vertices are dual-Odd with ONE successor. So the dual of Γ_σ is one-player in P1's sense. Every
    vertex keeps a successor. ρ is a positional dual-Even strategy, and ρ′ ranges over all positional Odd strategies of Γ.
  - Orientation (Fact DUAL, §1 above).
    - A play has the same triple (c, P, ℓ) in Γ and in G^d: the same ranks, the same top vertex, the same P-membership. Only the order
      is reversed.
    - So P1's «no improving edge: no dual-Even (x, y) with V_ρ(y) ▷_d V_ρ(ρ(x))» is exactly SBAR (i)'s «no Odd v, w with
      φ(w) ◁ φ(ρ(v))» in Γ.
    - P1's conclusion V_ρ ⊵_d V_ρ′ reads φ_(σ,ρ) ⊴ φ_(σ,ρ′) in Γ, for every positional ρ′ and every vertex.
  - Hence φ_(σ,ρ) is Γ's pointwise minimum over positional Odd strategies.
  - With Ξσ = the value against SPEC's optimal σ̄ (1E-N3 / R57 (a): Ξσ ⊴ V_(σ,τ′) for every positional τ′, attained by σ̄), we get
    φ ⊴ φ_(σ,σ̄) = Ξσ ⊴ φ. So φ = Ξσ at every vertex: SBAR (ii).
  - SBAR (iii) uses (ii) and 1E-N3 only, so it is unchanged.
- **My signature of Lemma SBAR stands** with [VJ-LOC] re-routed to R36 (c) P1, and so do REALIZE and REAL-IDEAL. The proof step is the
  same; only its citation changes, from an unestablished premise to a landed lemma.
- (a) **Word-diff of L-2 (sha1 b44456d1…) against L-1 (1d72ee31…).** Fixes sha1 64f062c2…, with entry 3 appended. The frozen packet,
  the frozen line and L-1 are unchanged at c374be8f (sha1s re-taken). Exactly the six listed changes:
  1. [VJ-LOC] → «local optimality in a one-player game (RESULTS R36 (c) Lemma P1, applied on the dual game to Odd's one-player game
     against a fixed σ; VJ00's two-player Lemma 5.8 is not used)» ✓. This is the confirmation above.
  2. G-1: bare date «(2026-11-02)»; the source names the fixes file with entries 1-3 ✓.
  3. G-3: «RESULTS R103's bridge B», and the NEW clause «applied at every Even vertex that is not its own W′-cycle node, non-movers
     included (RESULTS R103's (R1) ruling)». **Checked:**
     - It is NEEDED. Theorem REALIZE applies [RULE] at every mover at every step, including movers whose choice does not change.
     - It is ACCURATE. My (R1) ruling (R-N5-ANCHOR §1) rests on TB steps 3-5 and Lemma R, which describe S1's choice at every vertex that
       is not its own cycle node. It does not depend on FL transitions, so it applies at REALIZE's transitions before they are known to
       be FL.
     - The tie set it needs is supplied by Lemma W (iii) (TIE = R(x)).
     - Applying it «at every Even vertex» is true. The packet uses it only at movers; β, K and e are handled by Lemma ESC.
  4. G-2: «a Ξ-target xt(x, k), a mover or the exit X» ✓.
  5. G-7: «random Ξ-cyclic genomes do mismatch» moved after «DATA:» ✓.
  6. G-10: «L-RED R178 champions», «L-RED R188 genomes» ✓.
  - Parentheses balance (61/61). «» is 1/1, because the «1 ⇒ 2» quote is gone. Nothing else changed.
- Verdict: line L-2 **MATCHES**.
