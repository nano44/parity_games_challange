# R91: CONJECTURE UL_C is DEAD (the READER construction); UL_G untouched
L-RED successor 22 (Opus 5.5; D14/D15/D18, Lead GO 16:34Z "(1a) CONJECTURE UL_C ... the MAIN target ... You do CONSTRUCTIONS").
Written 2026-10-26 ~17:2xZ (date -u). Labels (D18 / L40): DEAD / PROVED (lane, unrefereed) / DATA / OPEN.
Target: docs/si/N5-GCX-box21.md §4 (l-si f984baa0; §7 at 5b01a939), statement quoted:
> CONJECTURE UL_C (late freeze). No U event at index ≥ |U_c| − 1 of its C-interval: for every C-interval [a, b] of class c and every U event
> (k′, (y, z)) with y ∈ U_c and a ≤ k′ < b: k′ − a < |U_c| − 1.

## 1. Result (DEAD, verified)
Family reader_L (experiments/red/ul/mkreader.py L), n = 2L + 16. The class S of cycle node c_s has |U| = 8 for every L, and its only
C-interval is [0, L + 1]. It is impure, A_S = ∅, D ∩ U = {u1, u2, u3} constant, DD = ∅, λ_W constant, BIG (|U| ≥ 3, Q_c ≠ ∅).
That C-interval contains one U event (y, z) at index k′ = L, so UL_C fails as soon as L ≥ 7, and the slack L − 7 grows linearly in n.
Every run below is fallback-free and lies in one phase (phase@0).

| instance (experiments/red/ul/instances/) | sha1 game | sha1 start | n | iterations n5 / n5b (fb) | C-interval | U event k′ | |U| − 1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| reader_L10_n36 | 31644312… | c2552ebd… | 36 | 13 / 13 (0) | [0, 11] | 10, edge (15, 14) | 7 |
| reader_L20_n56 | c9f3c948… | 6e8cc192… | 56 | 23 / 23 (0) | [0, 21] | 20, edge (25, 24) | 7 |
| reader_L40_n96 | cb6b7c76… | 884c0d54… | 96 | 43 / 43 (0) | [0, 41] | 40, edge (45, 44) | 7 |

Evidence (experiments/red/ul/vrun.sh GAME START, all three):
- n5.py (SPEC) and n5b.py --mode spec agree on the iteration count.
- `check_sol2` prints "zielonka(oink zlk) OK strategies verified" for both solutions.
- My checker ulx.py prints UL_C_VIOL = 1.
- L-SI's own gcx.py (UEV=1, reference, run unmodified from l-si 721de60a) prints UL_C = 1 with the same example ((15, 14) at k′ = 10 in
  [0, 11] for L = 10). For L = 6 it prints UL_C = 0 (index 6 < 7), as predicted.
Control: ulx.py on lib41 (experiments/new/box41/lib41.txt, S3 + 2 random starts, n ≤ 64; 1,101 runs of N5) gives UL_C_VIOL = 0, and the
largest inside index is |U| − 1 − 7. That is L-SI's own figure in N5-GCX §4, so the two checkers agree on the library.

## 2. The construction (why it works; each step seen in the trace)
- B: an Even-only class with cycle node b (an Even self-loop).
  - It contains a Bellman-Ford chain v_0 … v_L: v_i → {o_i, v_{i+1}}, v_L → {o_L, G}. All o_i, G, p1, p2, q, ql lead straight to b.
  - Ranks: c_s < a < r2 < b < o_L < … < o_0 < ql < q < p1 < p2 < G, all even. Chain vertices, gates, z and y sit below c_s (weight 0).
  - The wave: v_L takes G at step 0 and v_i takes v_{i+1} at step L − i. W = Ξ on B, because no gate is there.
- S (8 vertices): c_s → {u1, q}; u1, u2, u3 are Odd with u_i → {c_s, p_i} (p3 = v_1); a → c_s; y → {a, z}; z → {u2, r2}; r2 → u3.
  The start has σ(c_s) = u1, σ(y) = a, σ(z) = u2, τ(u_i) = p_i.
- Odd's side never moves: I_τ = ∅ throughout. τ is Odd-optimal, because Even's best reply to τ runs c_s → q → v_0 → … → G (it contains G
  and q), which beats every p_i for Even. Odd's best reply σ̄ closes c_s ↔ u1 (top c_s is worse for Even than b), so D = {u1, u2, u3}.
- Two W-traps keep S's class alive:
  - (c_s, q) is Ξ-improving (class b) but W(u1-route) = W(p1) ≻ W(q).
  - (z, r2) is Ξ-improving (r2 ranks above a) but W(z via u2) = W(p2) ≻ W(v_1) until the wave reaches v_1.
- The forbidden edge: (y, z) has W(z) (via p2) ≻ W(a) (via c_s, u1, p1), while Ξ(z) = {z, u2} ⊴ Ξ(a) = {a}.
- Release:
  - At L − 1 → L, v_1 takes v_2, so W(v_1) contains G. In the same S4a step, z's arena optimum moves to r2 (Ξ(z) jumps above Ξ(a)).
  - At L → L + 1, y takes z. That is a U event (forbidden at state L − 1 ≥ k′ − n + 1) at index L.
  - At L + 1 → L + 2, q and c_s join b together, and the phase ends after the event.
- Why the class bound fails: the clock is in another class. S's gates read B's W-values through τ (cross-class gates, xgate = 3). S's
  C-interval only asks D ∩ U to be constant, A non-increasing and DIRECT offsets constant. S's gates are non-direct (τ(u) ∉ A_S), so B's
  dynamics, of length L, enter S without a C-cut. ABS-HEIGHT (§7) does not apply: the interval is impure (gap (iv)) and its exits are
  not constants.

## 3. What this does and does not kill
- DEAD: UL_C as stated (§4), on impure C-intervals with cross-class non-direct gates.
- NOT touched: the global form UL_G (§5), which is what Corollary UL-RED uses. Here the global C-interval is the same [0, L + 1] (B has
  no gate, A_b = B is constant), but UL_G's threshold is n − 1 = 2L + 15 and the index is L. UL_G needs a U event later than the whole
  game size inside one global C-interval. That is the open target now.
- NOT touched: UL_C restricted to PURE C-intervals (D ∩ U = DD), where L-SI's §7 lift applies. The reader needs non-direct gates. A pure
  version would need S's gate exits inside A_S with constant offsets, so B's clock could not enter through them.
- PROVED (lane, unrefereed; elementary) for the record: in a C-interval with D ∩ U_c = ∅, no Even vertex of U_c switches at index
  ≥ |U_c| − 1.
  - Proof sketch: A_c = U_c and W = Ξ on U_c. In-phase switches stay in U_c, and S4a there is a one-player optimum over Ξ-improving
    edges, which dominates value iteration from Ξ_a.
  - Every Even-closable cycle in U_c is worse than reaching c (otherwise an improving cycle-closing edge exists and the phase ends).
    So value iteration reaches the class optimum within |U_c| − 1 rounds, and a later switch would raise Ξ above that optimum.
  - So any UL_C kill needs gates in U_c where W ≠ Ξ, as the reader has.

## 4. Next (OPEN)
- UL_G: a λ_W-constant fallback-free run with a U event at index ≥ n − 1 of its global C-interval. The reader shows the index can be
  linear in the clock's length. The clock (a BF wave) is bounded by the size of its class, and a clock longer than n inside one global
  C-interval is exactly the open long-run question (R89 R_max ≈ n). Next: chain readers. A reader's own released switch could re-arm
  another class's clock, so one global C-interval would hold several sequential clocks.
- UL_C on pure intervals (Lead (1a) gap (i)): data from L-SI's abscyc.py (climbs at n = 5 reach exactly n = 5 steps, my 4 runs).
  I have no cyclic-model run longer than n.

## Sources opened
- docs/si/N5-GCX-box21.md, l-si 721de60a, sha1 04f79afc…: §1, §4, §5, §6, §7.
- docs/si/N5-RUND-box17.md: §13 (FORBIDDEN AT k), §16 (CHARGE-U, U(S)).
- docs/new/N5-ssi-global.md: SPEC S1-S5 and FIX 1-4.
- experiments/si/root/gcx.py and common.py, plus abscyc.py (l-si; reference only).

## 5. UL_G (Lead 17:08Z: first): global data and why the reader does not reach it (DATA, READING; written ~17:4xZ)
- Checker: ulx.py now also computes GLOBAL C-intervals, from the frozen packet text (P-N5-GCX-box21.md, trunk sha1 5a91bebb, §1 / §3).
  Over every class at once, A is non-increasing, D is constant, and DD with its offsets is constant (strict reading: the DD dict must be
  equal). The threshold is n − 1. Each interval also reports whether λ_W is constant.
- DATA:
  - lib41 (S3 + 2 random starts, n ≤ 64): UL_G_VIOL = 0. The best is G_IDX_SLACK −7 (j5_n16 rs) and G_LEN_SLACK −2 (b6_xs_n24, global
    C-interval [0, 21] at n = 24).
  - b6_xs_n24 is gate-free (D = ∅ throughout) and has no U events. It is a Bellman-Ford wave through 21 of its 23 Even vertices, so the
    D ∩ U = ∅ bound of §3 governs it.
  - L-RED pins: run49_n32's longest global C-interval is 17 at n = 32, although the run is 49 long (cut 4 times).
  - reader_L: the global C-interval is [0, L + 1] at n = 2L + 16.
- READING (not a lemma). Every mechanism I can build spends at least one fresh vertex per time step of a causal chain:
  - a BF clock spends one chain vertex per step;
  - a reader's W-trap release adds one step per reader vertex;
  - a ladder (one Even vertex with k gated rungs reading k clock positions) makes k switches, but only at the clock's k tick times;
  - a mutual loop (x's switch raises Ξ of q, which r reads by Ξ; r's switch raises W, which x reads through a gate's τ) re-uses x and r,
    but each round needs a fresh Ξ-higher rung for both.
  The reason: options that read the SAME dynamic vertex keep a static W order, and options read through the same gate keep a static
  W − Ξ order. So every flip needs its own vertex. A W-reading loop closes a W-cycle (λ_W moves), and a Ξ-reading loop closes a Ξ-cycle.
- So UL_G needs a global C-interval longer than n − 1 with a gate. Equivalently, a causal chain that re-uses vertices faster than it
  spends fresh ones. I have not found one.
- Candidate lemma to PROVE instead (OPEN): GCI-LEN. Every global C-interval of a λ_W-constant fallback-free run has length ≤ n − 1.
  - GCI-LEN implies UL_G, so Corollary UL-RED would become a bound in K(S) alone.
  - Known: GCI-LEN holds when D = ∅ (§3's argument, applied per class).
  - The data maximum is n − 3.

## 6. UL_G re-use attempts (Lead 17:31Z, (a), time-boxed): no kill; the exact obstruction (PROVED steps marked; READING otherwise)
Written ~17:4xZ (date -u). The target is a global C-interval longer than n − 1 that contains a gate, i.e. a causal chain re-using vertices.
The strongest design I found is TWO WAVES ON ONE CHAIN.
- The design:
  - Wave 1 runs backward through a gate-free chain v_1 … v_L inside A, from a top G1 at v_1, for L − 1 steps.
  - A W-trap at a witness ω reads wave 1's arrival at v_{L−1} through a gate β's τ. Its release injects Ξ-content into v_L (via γ, ω).
  - Wave 2 then runs forward over the SAME chain (edges v_i → v_{i+1}), for another L − 1 steps.
  - A reader (as in §2) placed at v_1 would give a U event at index ≈ 2L at n ≈ L + 10. Here is why it cannot work:
- (O1) GATE INEQUALITY (PROVED, one line). At every state and every u ∈ D: Ξ(σ̄ u) ⊴ Ξ(τ u) ⊴ W(τ u).
  - The first inequality: σ̄ is Odd's best response.
  - The second: Fact FZ / (F1), Ξ ⊴ W pointwise.
  - So a W-trap that reads a structure R through a gate's τ can carry, behind the gate, Ξ-content of at most W(R) at every earlier state
    of the interval (while u ∈ D, which a global C-interval keeps).
  - If R is low until the trigger (that is what makes the trigger late), the Ξ-content behind the gate is low. The injected Ξ-content must
    then sit BEFORE the gate, on the vertices of the trapped option's own path. That is how the reader of §2 works: r2's weight.
- (O2) RANK ARGUMENT (PROVED for the lexicographic weight order). Let the trapped option ω_1 carry the bonus vertex B (Ξ-content) and read
  R (W). Let the incumbent ω_0 hold the trap.
  - W(ω_0) ≻ W(ω_1) before the trigger and W(ω_1) ≻ W(ω_0) after, where the trigger adds wave 1's top G1 to W(R).
  - So the top vertex separating W(ω_0) from W(ω_1) must rank strictly between B and G1. In particular rank(B) < rank(G1).
  - Wave 2 starts from B's level, so it cannot beat wave 1's routes, which carry G1. The chain is never reused.
- (O3) LENGTH VERSION (READING). With equal weights and length as the separator, the incumbent's W-path must be longer than the trapped
  option's early path by about the length the trigger adds. That costs a fresh tail of vertices of that length, so it gains nothing.
- (i) σ̄ leapfrogs between two non-τ successors at a gate (D constant): Ξ(u) is Odd's minimum over the σ̄-candidates. It rises only when
  the minimum rises, so it adds no time, and (O1) still bounds every candidate by W(τ u).
- (ii) Ties and lengths: (O3). In a gate-free class, lengths are already inside the §3 bound (value iteration on (weight, length)).
- Conclusion (READING, to the design lanes with GCI-LEN): every injection of new Ξ-content late in a global C-interval costs vertices
  that rank between the trigger's increment and the content. That is the "one fresh vertex per causal step" of §5, here made exact for
  the trigger step. The best instance stays reader_L (index L at n = 2L + 16).
