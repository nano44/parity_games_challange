# L-SI notebook (strategy-improvement design loop toward M4 / M4-R)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Lane brief: Lead 2026-10-15 10:10Z, 12 h box to 22:10Z.

## Resume point (successor 4, box 9; Lead GO 04:52Z 2026-10-25; session_019zCLqPUCjkJxMD4vZoJ8TA)
Handover check 1cef5052 (Lead 5/5). Trunk merged a08c41d8. Box 9 write-up: docs/si/N5-C-box9.md. Code: experiments/si/coarse/
fbw.py, reltrace.py, levcheck.py, jclimb.py modes HEQ / REP. Logs: experiments/si/coarse/logs/box9/.
### DONE (PROVED by L-SI succ. 4, unrefereed)
- (1) Tool fix bf8be06f: level ∞ = mono.INF = 10**6 (mono, fbcount, xing/carries); 15 re-run logs byte-identical (n ≤ 64); levcheck in check.sh.
- (2) Lemma FBW (every game): at an Even S4c fallback every gate has level ≤ max(δ, −1), δ = Ξ/W gap at its two ends (premise:
  R18 Lemma S (c) = R17 (F1) applied to S4a's computation, which returns σ_k at a fallback). Corollary FBW-S: in-scope M_k ≤ max(r_k, −1).
  Theorem CLS2: fallback levels non-increasing along a whole scope run, every kind. (H-EQ) CLOSED, (H-KIND) unnecessary.
- (3) FLAT-ALL, STRETCH, Theorem PL: level-M block N ≤ n_E(1 + D_M), D_M = dirty intervals; first break of a dirty interval is an
  absorption above M (U-loc + Lemma OR); with r > M on the block D_M ≤ d_o − 1 + REL_M (ABS-L + NL (ii)). Corollary PL-S additive.
  Also ONE-RISE, CONSEC, FB-RE.
### DATA
- FBW: named 272 fb / 837 gates, library 694 / 2,384, random 141 fb: 0 failures. In-scope u* = none fallbacks: 0 anywhere.
- reltrace: 75 + 169 blocks; COARSE_M breaks inside blocks 0, gates above M inside blocks 0, tail repeats per block 0.
- Lemma ABS-O (PROVED): the cycle an absorption closes has, above max(g, rank c), only vertices of P(Ξ_j x0); so rank o ≤ max(g, rank c).
  DEAD END as a route to NJB: every in-scope R→F gate has level >= rank o when rank o > rank c, so no block has M < rank o (0 / 778).
- CONJECTURE NJ-INT (stronger than NJB): no θ-change above L = M_k0 between consecutive in-scope fallbacks with r > L. DATA 562 / 0.
- Packet P-N5-FBW FROZEN: docs/si/P-N5-FBW-box9.md, sha1 88337bd6, l-si cd42f088; Lead PINNED at trunk e69772b, with both referees.
  NEVER edit it; referee items go to docs/si/P-N5-FBW-fixes-box9.md.
- §7 (cda41216): PL-I, the bridge to L-NEW box 34 (L1). PL holds inside frozen r = ℓ blocks without w constant; NJB => (L1) polynomial.
- §8: Lemma NO-RF-OLD (PROVED): after a θ-change above L in an interval with r > L, vertices already in R have no gate into F.
  So the next evicting fallback's tails are all entrants (CONJECTURE ENT). DATA: 54 rises above L after a fallback, all after the
  run's last fallback; NORF climbs (seeds 9201/9202, 20 min each, from 06:01Z) reached 16 / 23 post-rise states, 0 violations.
### NEXT
1. Prove ENT (entrant tails after a rise above L). That closes NJ-INT, then NJB, then (L1).
2. Blocks where r drops to M (NL / ABS-L unavailable); level −1 fallbacks.
3. Record the NORF climb results in box 9 §9 (outputs in the scratchpad: climb/norf_*.pg); pin the bests if useful.

## Resume point (successor 3, box 8; superseded by box 9; PARKED 2026-10-25 ~02:35Z at ~500k context after freezing P-N5-CLS; LANE-RESTART step 1)
IN FLIGHT: nothing running (all climbs finished; outputs in experiments/si/xing/out/jclimb/, local only).
NEEDS: none. Lead pinned P-N5-FB (R25 landed trunk 40ef7ed); fixes1 8548c3fc / fixes2 4d5b3716 are cited by sha1: never edit them.
(Box 8 header: Lead GO 00:18Z 2026-10-25; R25 LANDED trunk 40ef7ed from P-N5-FB.)
Box 8 write-up: docs/si/N5-C-box8.md. Code: experiments/si/coarse/cls2.py, rfinv.py (+ jclimb modes CLS2, RF).
### DONE (PROVED by L-SI succ. 3, unrefereed)
- OFFGATE (gates into F never exceed M_k, at every in-phase transition incl. jumps); CN (in-phase cycle-node switches have level -1);
  switched-edge classification at in-scope fallbacks (§3: (a)(b) flat, (c) none at THR u*≠none, (d) CLU; (c) at EQ / THR u*=none
  and (e) F→F non-cycle-node OPEN).
- TRANSFER; FRZ/LV from (A)+(B1); (A)-step; Theorem CL-S-RED: the first half of (CL-S) under (H-B1), (H-KIND), (H-EQ).
  (B1) PROVED at THR(u*≠none) and EQ fallbacks; OPEN at arena-step leaves and THR u*=none fallbacks.
- Lemma AL: after a fallback, arena leaves need rank u* <= L (given (A), FRZ).
### DATA
- OFFGATE 7,134/0; CN 7/0; (A) 0; FRZ 28,311/0; R-ROUTE 10,293/0; LV 588/0; (B1) 588/0; AL 4/0; in-scope fallbacks 260 THRu, 4 EQ,
  0 THR u*=none. OG' (MF form) FALSE on x31_re24 1->2 (mass arena leave carries a level-22 gate into F).
- Arena reversals of (Z): 39/45 occur before the first fallback at the current w (box 8 §7).
- Box 8 later: P-N5-SO check (socheck.py unmodified, 0 failures, box 8 §8); adversarial climbs vs (CL-S) 0 violations (§9);
  Lemma EQ-STRETCH (EQ runs < n+m transitions, from R17) + EQ-PERSIST (§10); (Z) map (§11): fallbacks (FB + CL-S/SO), EQ runs
  (PROVED poly), out-of-scope (O, w-changes), THR arena reversals (all within n-1 of a θ-change: reduce to Θ_scope).
- Box 8b (Lead go 02:00Z): Lemma NL + Theorem CLS1 PROVED (c47be183): fallback levels non-increasing at THR u*≠none fallbacks
  of a scope run, with no (H-B1) (minimal-counterexample induction along new plays + WM + Lemma G). (H-B1) is no longer needed there.
  Per-level count reduced to θ-changes above the level; item 2 = box 3's multiplicative recursion (box 8 §13).
### NEXT (for a successor)
1. Packet P-N5-CLS FROZEN: docs/si/P-N5-CLS-box8.md, sha1 5bbfd872, l-si 04ca0b8c (CLU, TRANSFER, OFFGATE, CN, NL, CLS1; logs
   experiments/si/coarse/logs/cls_*.txt via run_cls.sh). NEVER edit it; referee items go to docs/si/P-N5-CLS-fixes-box8.md.
   SIGNED by both referees (REFEREE a0b92ec, REFEREE-2 ffe10e1 §C 848839e). Fixes record docs/si/P-N5-CLS-fixes-box8.md
   (CLS-1..4, N-CLS-1); REFEREE §C pending. Lead note: L-NEW 13 ABS-L / per-level count via releases of absorbed exits
   (docs/new/N5-K-box33.md §8-§9) bears on open item 2.
2. Additive bound on tame θ-changes below M (box 8 §13); the per-level count and Θ per scope run hang on it.
3. EQ / THR u*=none fallbacks: their non-R->F switched edges (H-EQ incl. §3 (e)).

## Resume point (successor 3, box 7; superseded by the box 8 point above; Opus 5.5 D18/L40; started 21:31Z 2026-10-24; end-of-box ~23:45Z)
Handover check 78a764d8 (Lead 5/5). Box 7 = proof side of (C). Lane write-up: docs/si/N5-C-box7.md §0-§13. Code: experiments/si/coarse/
(mono, fbcount, tame, jump, jumpeq, dpot, ju2, clscope, eng1, jclimb; run_all.sh regenerates the packet logs; named.txt = 53 one-o files).
Climb output: experiments/si/xing/out/jclimb/ (local only, excluded via .git/info/exclude; never git add -A).
### DONE (PROVED by L-SI succ. 3 unless marked)
- Packet P-N5-FB (docs/si/P-N5-FB-box7.md, sha1 9ece9994; pinned trunk 348393b), SIGNED by both referees (§C no disagreement),
  R25 drafted by Lead. Contents: (T), COARSE-SI (a)/(b) TAME, MONO, NOINF, Theorem FB (#fallbacks per phase <= n_E(2n-1)(J+1)+J,
  +1 phase-exit), J1/OFF/CAP on 1O; (JUMP-EQ) FALSE (x31_rx32 53->54); A: L <= M signed, L >= M OPEN.
- Fixes: part 1 docs/si/P-N5-FB-fixes-box7.md (8548c3fc, REFEREE items), part 2 docs/si/P-N5-FB-fixes2-box7.md (4d5b3716, REFEREE-2
  items + concordance). Never edit the packet or a fixes file whose sha1 was sent.
- Box doc only (not refereed): §9 MIN, D1', D2, D3, NOREL-A, Corollary JD (J_in(S) <= |succ(o)| + releases into D at fallbacks).
- FALSE (own conjectures): (JU2) on jcl_x31_cu32i; (REL-NJ) naive form (4/18).
- CONJECTURE (CL-S) (§13): fallback M-levels non-increasing across a whole scope run, <= n_E per level. DATA 67 runs / 246 fb / 0.
  Reduction (READING): (CL-S) => J <= (1+N_out)|succ(o)|(1+n_E(2n-1)) + N_out => (C) <= poly(n)(1+N_out), N_out <= O + #w-changes + ...
- Pinned climb bests (all reverify.sh OK, one o): experiments/si/coarse/instances/jcl_* (J 5-17), rel_* (release-paid jumps 10-16).
- SCOPE CORRECTION (CHECKER C34 Addendum 1, Lead 23:40Z; R25 scopes it): fixes2 G-FB-3 says "the Corollary of §4 holds on every game".
  That is right for W-lowerings and WRONG for (C), which is 𝒞^1O-only (R and (C) are defined through o). fixes1/fixes2 are cited by
  sha1 in R25: never edit them; carry this scope in every later lane file.
### NEXT
1. Prove (CL-S) (box 7 §13 ideas: FBL + CLU bound THR fallback levels by rank u*; need: jumps do not undo β-flips). Then a packet.
2. Rest of (Z): arena '−' reversals and '±' (box 7 §10 split).
3. Last climbs done (box 7 §14): release-paid jumps 18 at n 48; adversarial CLS climb 0 violations of (CL-S). Nothing running.

## Previous resume point (successor 2, Opus 5.5 D15/D18; PARKED 2026-10-24 ~21:30Z at ~500k context; LANE-RESTART step 1)
Boxes done this session: handover check f0bbb5e0; box 4 (docs/si/N5-X-box4.md); box 5 (a) packet P-N5-Z (docs/si/P-N5-Z-box5.md v1,
pinned trunk fba7177, sha1 a027638f; R23 with CHECKER as C32; lane fixes docs/si/P-N5-Z-fixes-box5.md incl. referee items Z-1..Z-3,
N-Z-2); box 5 (b) + box 6 (docs/si/N5-C-box5.md §1-§6). Code: experiments/si/xing/ (every script asserts n5.run equality and
one-Odd-choice). Climb output experiments/si/xing/out/ is excluded locally via .git/info/exclude (NOT .gitignore; never git add -A).
### DONE (box 6)
- (CL) reduced (READING) to Step 1 COARSE-SI (write out the telescoping) + A (carry changes ≤ its level; DATA 198/0) + CONJECTURE
  (JUMP-EQ) (an INR jump above the last carry level lands in θ = w; DATA 4/4 first failures, 19/20 post-carry jumps).
- Step 2 PROVED: COARSE_L(Ξ) constant at k->k+1 and G(L) at k => G(L) at k+1.
- DATA: I(L) 784/0, FREEZE(L) scoped 638/0, G(L) fails at 11 states (all F->R entries, after INR jumps).
### NEXT (for a successor), in order
1. Write Step 1 (COARSE-SI) as a full proof: L-coarse super-solution in G_{σ̄_k}, telescoping, simple-path bookkeeping (VAL), and
   the exact cycle-closing exclusion.
2. Look at the one post-carry jump landing in THR (find it with freeze.py's pre-scope variant: ex entries 'F' after lastc), then try
   to prove (JUMP-EQ).
3. Prove A (carry changes Ξ only at levels ≤ L): evictees ≤ their eviction level (CLU), passive vertices inherit, F-switches flat
   (R21 (c) FBL-N (ii)), θ via exits.
4. Then (C) needs "carries per level": refills are θ-changes strictly below the level (data §3).
L-RED box 34 is nesting carries with '+−' fallback reversals as fitness (Lead 21:1xZ).

### Box 5 (GO 20:2xZ): (a) packet P-N5-Z v1 pinned (trunk fba7177, sha1 a027638f), referee items answered in
docs/si/P-N5-Z-fixes-box5.md (Z-1, Z-2, Z-3, N-Z-2; s_rt32_final OUT OF CLASS, two Odd choice vertices). (b) docs/si/N5-C-box5.md:
Lemma CLU PROVED; CONJECTURE (CL) carry levels non-increasing while w constant (0 violations, 118 carries + 3 adversarial climbs, carries
up to 33/phase in drains); (H-VL) and per-vertex CL FALSE. Next: prove (CL) (§3b: only o-free progress and entries can raise the pending
level) and bound carries per level. Pinned bests: experiments/si/xing/instances/zcl_*, ccl_*.
- Never edit a file after sending its sha1 for pinning: the Lead pins at once; corrections go to a separate fixes file.
### DONE in box 4 (PROVED by L-SI successor 2, UNREFEREED)
- Lemma ACT: every crossing transition has an active crosser (entry: switched F_k -> R̄_k edge; leave: switched R_k -> F_k edge or a new
  cycle inside R_k). Lemma LOOP: no such cycle inside a joint λ-phase when H1 holds at k.
- Fallbacks: NOFE (a switched F_k -> R̄_k edge at a fallback starts on o's W-play or on a cycle; first form "fallbacks never enter" FALSE,
  nofe_cyc_n8); NOFL-E (from Ξ = W with H2: no R_k -> F_k switch at a fallback); GAP (THR fallback leaves land in the trust gap
  Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ W_k(σ_k y)).
- Lemma LV': X ≤ (n−1)(Z+1) + Z, Z = reversals of R; |R| is the amortized ("number of ones") potential; (X) <=> (Z) up to n.
- Lemma WM: W never decreases at an arena transition; W-lowerings = carries = fallbacks (data: exactly the evicting fallbacks).
- Lemma TROP (terminal-parameter one-player game: one breakpoint per vertex) PROVED but inapplicable: N5's θ is o's own play (NG4).
- READING with box 28 §5c: O(n^5 (1 + Z + O)) transitions per joint λ-phase.
### FALSE in box 4 (own conjectures, never sent as lemmas)
- NOFE first form (nofe_cyc_n8, sha1 f3868b39 + .start). (U*-DROP): 19/19 violations. (W-LAY) ≤ n−1 W-changes between W-lowerings:
  thclimb_n16_s12 (16 at n 16). Φ(R,θ,w) potentials: x31_re24/ru24. Φ(R-side only): lev_l_sc (R = ∅ at states 8 and 32).
### OPEN
- (Z) reversals of R per joint λ-phase, hard part (C) carries = evicting fallbacks (data: Z ≤ 7 on 31 named instances; climbs Z 18 /
  carries 13 at n 32, Z 22 at n 48 with 0 carries; box 4 §6, §10); (NH'); (ELIM-poly), (LEVEL-poly), (CYC-u*) as
  before. G-N5-TIME OPEN.

## Previous resume point (successor 1, Opus 5.5 D15; PARKED 2026-10-24 ~17:35Z at ~563k context, Lead 17:3xZ; LANE-RESTART step 1)
Boxes done this session: handover check (96469356), box 1 OR lens (docs/si/N5-OR-lens.md), box 2 (N5-OR-lens-box2.md), box 3
(N5-OR-lens-box3.md). Last box SHA 8314ce9c. Code: experiments/si/orlens/ (README-level docstrings in each script); pinned instances
in experiments/si/orlens/instances/ (all Oink zlk OK, strategies verified). Oink must be rebuilt in a new container
(scripts/setup_oink.sh) before check_sol2.py / the verify Oink smoke.
### DONE — statements and status (all PROVED by L-SI successor 1, UNREFEREED unless noted)
- Box 1 (N5-OR-lens.md §2-§3): Lemma U (lev ultrametric); E1 (gap level monotone in a joint lambda-phase vs target T = Xi at phase
  end); E2/E3 (a used Even edge certifies its slack; gone for the phase once g < s); E4 (Odd best-reply exits, same); E5 (gap <= max
  slack on the play); E6 (<= n(n+1) non-flat transitions per phase, any SI rule); Lemma D + Corollary D1 (switch-all satisfies
  Howard >= VI in VJ valuations, yet exponential in one phase on switchallexp: no lexicographic contraction); (ELIM-poly) =>
  N5 < (2n(n-1)+1)(m+1)w(n); recursive depth D => < (n(n+1)+1)^D value-changing transitions.
- Box 2 (N5-OR-lens-box2.md): Lemma VIS (in a (w,u*)-run, a self-elimination (INR) of the argmin exit whose loop rho+{o} adds a
  vertex above u* retires that exit from sbar(o) for the run; <= d visible INRs per run) and VIS' (general form: after e enters R
  with loop top-new vertex t, e is sbar(o) again only if theta changed at level >= t). Data checks 0 violations.
- Box 3 (N5-OR-lens-box3.md): Lemma LEN (<= n-1 length-only theta-changes between path-set changes); Lemma CH (a SELF/OVER
  theta-change at level r is paid by a rise of the argmin exit's o-free value at level >= r); counter bound m_r <= 1 + sum_{r'>r}
  m_{r'}; hence #theta-changes <= n(1 + sum_r m_r).
### FALSE / refuted (instances pinned)
- (ELIM-n): L-RED elimn_cex_n48 (window 49 at n 48). (CYC-ELIM) with constant d: cycelim_cex_n32, s_tp32_final. 'every sbar-lap
  retires an edge': theta_tp32 states 4-9. 'one INR per exit per run': inr2_n32. 'RISE <= 2 per exit per run': rise3_n32,
  run_x_inr2 (4). PIECE does not give phase-sense elimination: fts_best16 7->8, theta_tp32 9-19. HMZ max-slack elimination:
  returns_rt48 (77/78). N5 satisfies Howard >= VI: i4_hand z = 9.
### The multiplicative obstruction (box 3 §3) and the potential a successor should look for
- SELF/OVER are paid (CH) by o-free progress of exits, a one-player resource (R17 layering in G[F]) that only holds inside a PIECE
  (R constant). Every INR is a theta-change AND a crossing, so it ends the piece and resets that resource (layering fails at
  trust-routed vertices, box 21 §3.6 (ii)). VIS' charges repeated INRs to higher theta-changes, up to d exits per change.
  => T(>=r) <= poly*(1+T(>r)): multiplicative, depth = levels used.
- Additive would need (i) a potential that RISES AT EVERY INR / crossing and is NOT restored by o-free progress, or (ii) m_r <=
  poly without the '+T(>r)' term. Lead's box 4 for the successor: (i) for crossings (X) (L-NEW box 28 §5c: transitions per phase
  O(n^4(1 + X + O))).
### OPEN
- (ELIM-poly), (LEVEL-poly) (data: max m_r 11 at n 32, lev_l_sc/lev_l_x: two nested counter digits, no third), (CYC-u*).
- Kill design (routed to L-RED): a carry above 24/21 in lev_l_sc that replays the two-digit block.

## Queue (for a successor)
1. Rerun `python3 experiments/si/families.py --engine fast --rules zadeh,cunningham --families fhz_padded --sizes 2..12`
   and the adversarial/famsearch for S5/S6 with --engine fast if S5/S6 stay live.
2. Keep check.sh green: it compiles vjfast_check and re-checks the pinned killer instances (instances/pinned.txt).

## Things only I know
- (successor 3) pgrep -f with a pattern from the same command line never ends (it matches its own shell): wait on a log line instead.
- (successor 3) Bitten again 22:0xZ by `for p in $(pgrep -f "jclimb.py 95")`: it killed my own shell (exit 144). List with
  `ps -eo pid,args | grep "[j]climb"` (the bracket stops self-match), then `kill <pid>` by number in a separate command.
- (successor 3) The predecessor's carry level L (leavers) equals M_k (max gate level) at every carry seen; use M_k, it is the one with
  proofs (MONO, FB).
- (successor 2) Never edit a file after sending its sha1 for pinning; corrections go to a separate fixes file (Lead rule, 20:4xZ).
- (successor 2) Background watchers: wait on a file condition (e.g. 'FINAL' in logs), never on pgrep -f of a pattern in the same command line.
- (successor 2) pkill -f with a pattern that occurs in the same bash command line kills that shell (exit 144): start/stop climbs with
  setsid in their own command; stop them by PID.
- (successor 2) experiments/new/box28/fbre.profile does NOT assert equality with n5.run; xclass.assert_run does (use it).
- (successor 2) xclass.py label LL = "leave through a target that was in R_k and left in the same transition", not a loop (Lemma LOOP).
- (successor 1) orlens conventions: phase = maximal run of STATES with equal (cycle-node map of Xi_sigma, of Xi_tau on G^d); a phase
  of k states has k-1 transitions (box 21's phases.py counts may differ by 1). Phase target T = Xi at the phase's last state, not
  the global optimum (earlier phases have other cycle nodes, so g would be stuck at level n+1). lev levels: -1 equal, 0 length,
  1+rank, n+1 cycle node. 'eliminating' = an edge of sigma (or tau, noelimrun_st) abandoned at that transition and absent from
  every later state of the phase; transitions where only tau moves count as non-eliminating in the sigma-only column.
- (successor 1) ortrace.run_states copies n5.run's loop; gaps.analyse asserts (iterations, fallbacks) == n5.run's; climb.py and
  sweep.py call elim_g without that assert (speed). Re-check any climb best with gaps.py before citing it.
- (successor 1) The name trace.py shadows the stdlib module 'trace': keep ortrace.py.
- Engine conventions: priorities made injective by rank (p' = 2·rank + parity, rank by (pr, index)); path component a bitmask
  over ranks; comparison key = (reward of cycle node, signed weight Σ ±2^rank, ±length). Odd's final strategy = the
  restricted-graph counterstrategy recorded during evaluation (the argmin-over-successors shortcut is WRONG: it fails
  verify.py on 3/600 random games and on switchallexp, because a successor's path may pass through the vertex itself).
- The port counts the final non-improvable evaluation as an iteration: port K = my iterations + 1.
- Family generators: Oink tools in tools/oink/build (tc, tc+, counter_*), pgsolver_port.py for recursiveladder,
  switchallexp, switchbestexp. Sizes: switchallexp n = 14N + 7, switchbestexp n = 25N + 10, tc+ grows fast (N=8: 624).
- Hansen's 2012 thesis: pure.au.dk/portal/files/52906897/thesis.pdf → HTTP 403; www.cs.au.dk/~tdh/papers/dissertation.pdf
  (the URL the errata gives) → HTTP 404 (both 2026-10-15 ~10:10Z). Not opened. What it contains, per the errata 1410.7871
  p.2: an alternative 2^Ω~(m^{1/3}) lower bound for the original Random-Facet on MDPs (the published form is 1410.7530).

## Sources opened (arXiv id or DOI, theorem/section)
- (successor 3) Vöge-Jurdziński, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48, pdf from
  www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de… (same file as R15), opened 2026-10-24 21:35Z: p. 13-14 Remark (closed
  semiring), (6)-(10); p. 14 definition of σ̄ (minimises Ω_σ over successors) and of Prog (conditions 1-3); p. 15 Lemma 5.2
  (locally progressive ⟺ Θ_στ; cycle node = max of the cycle); p. 16 (11) Ω_σ = Θ_σσ̄ and Θ_σσ̄ ⊴ Θ_στ for all τ.
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF opened 2026-10-15). Section 3: valuations, arena A_{G,σ}, improvement policy (conditions (1),(2)),
  Thm 3.2 (strict improvement), Thm 3.3 (regions from a non-improvable σ). Section 4: Lemma 4.1 (locally optimizing policy in
  poly time), Thm 4.2 (globally optimizing, [Sch08]), Lemma 4.3 ([Vög00]) with proof p.7: policy I^lin from a ≺-optimal σ*,
  at most |V_0| iterations; p.7 remark on intransitivity of optimal updates. Section 5: 1-sink games (definition). Thm 6.14:
  switch-all needs ≥ 2^n steps on G_n from ι_{G_n}; Thm 8.4: switch-best ≥ 2^n on H_n from ι_{H_n}.
- Zwick, "Improved subexponential analysis of the Random-Action-Removal algorithm for 2-player turn-based games and
  non-binary AUSOs", arXiv 2607.06334 v1. Section 4 (algorithm, steps 1-5), Appendix D Fig. 1 (pseudocode Rand-Act-Rem),
  Thm 8.2 (F(n,k) ≤ U(n,k), subexponential), section 3 (SI as AUSO on strategies with VAL_a ≺ VAL_b orientation).
- Friedmann-Hansen-Zwick, "Errata for: A subexponential lower bound for the Random Facet algorithm for Parity Games",
  arXiv 1410.7871 v1: abstract and p.1-2 (the RF = RF* claim is false; "The main result of [1] is thus flawed"; RF* bound
  stands; [5] Hansen thesis gives 2^Ω~(m^{1/3}) for RF on MDPs; [3] transfers it to shortest paths); section 2 (RF on
  shortest paths pseudocode).
- Friedmann-Hansen-Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths",
  arXiv 1410.7530: Thm 6.3 (Random-Facet: ≥ e^Ω(√n) = e^Ω(M^{1/3}/log M) expected switches on G_{n,r,s,t}); p.1-2 (the SODA
  2011 bound was for parity games; the corrected bounds are for shortest paths / MDPs).
- van Dijk-Loho-Maat, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223: Def. 2 (sink parity
  game), the generalisation J_σ(τ), J_τ(σ) (p.9, local valuation comparison), conclusion p.19-20 ("more than only local
  information", robustness against preprocessing).
- Disser-Loho-Maat-Mosis, "Lower bounds for ranking-based pivot rules", arXiv 2512.16684 v2: Thm 1.1 (informal: index-based,
  o(N/log N) memory, N^ω(1) on SI), Thm 1.2 (informal: MDP/LP rules ranking by index, reduced cost and objective improvement:
  2^Ω(√N); NOT stated for parity games), Thm 4.3 (ℓ-index-based rules, m^ω(1) on sink parity games), Lemma 4.6, Def. 3.4
  (neighbour ranking), p.3 "every deterministic memoryless pivot rule can be formulated as a ranking-based rule", Obs. 4.1
  (an N-memory rule solves a given game in linear time).
- Disser-Friedmann-Hopp, "An exponential lower bound for Zadeh's pivot rule", arXiv 1911.01074 v2: title page only (B8 source;
  not needed beyond the barrier table).
- Fearnley-Savani, LMCS 14(4:9) 2018, arXiv 1507.04500: title page only (B12).
- Fleet docs: TARGET.md v1.0; docs/DECISIONS.md D1-D6, L18-L19; docs/RESULTS.md DE1-DE3; docs/lit/RANKING.md §4;
  docs/lit/BARRIERS.md B8-B14; experiments/hard-families/README.md and pgsolver_si.py (port, stratimpralgs.ml line map).

- (successor 1, 2026-10-24) Hansen-Miltersen-Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based stochastic
  games with a constant discount factor", arXiv 1008.0530 v1 (pdf sha256 f53a6b51...): Lemma 3.7 (optimality), 4.2 (contraction of
  T), 4.8, 5.1-5.2 (SI monotone), 5.3 (T v^{pi0} >= v^{pi1}: Howard >= VI), 5.4, 5.5 (||v^k - v*|| <= gamma^k ...), 6.1 (used action =>
  gap >= reduced cost), 6.2 (l1 gap <= n/(1-gamma) max reduced cost), 6.3, 6.4 (every sigma^k has an action absent after k+L,
  L = log_{1/gamma} n^2/(1-gamma); only player-1 actions are eliminated), Thm 6.5 ((m+1)(1+L)), §7 (Friedmann: exponential when
  gamma is part of the input or undiscounted).
- (successor 1) Scherrer, "Improved and generalized upper bounds on the complexity of policy iteration", arXiv 1306.0386 v4 (pdf
  sha256 391b6481...): Thm 1 (quotes Ye 2011: O(mn/(1-gamma) log n/(1-gamma))), Thm 2 (HMZ), Thm 3-4, Thm 5 (Post-Ye), Lemmas 4-5
  (= Post-Ye Lemmas 3.4, 3.5: new cycle every O(n^2 m log n) iterations; progress per new cycle), Def. 1 (tau_t, tau_r), Thm 6,
  Assumption 1 + Thm 7 (Howard PI O~(m(n^2 tau_t + n tau_r)) for MDPs only), §2 remark: removing 1/(1-gamma) impossible for Howard's
  PI (Fearnley 2010).
- (successor 1) Post-Ye, "The simplex method is strongly polynomial for deterministic MDPs", arXiv 1208.5083 v2 (pdf sha256
  c51876eb...): abstract (O(n^3 m^2 log^2 n), any discount; "layers" measure of progress), Lemmas 3.4, 3.5.
- NOT opened: Ye 2011, Math. Oper. Res. 36(4):593-603, DOI 10.1287/moor.1110.0516 (cited only through Scherrer Thm 1).

## Dead ends (details in docs/si/DEAD.md)
- (box 9, succ. 4) ABS-O as a route to NJB: vacuous, since every block has M >= rank o when o counts in θ's path set (abso.py fb_hi = 0 of 778;
  obstruction: R→F gates differ at o). docs/si/N5-C-box9.md §3b.
- (successor 3, box 8) OG′ ("gates into F at k+1 never exceed MF_k = the max level of the gates INTO F at k") FALSE:
  experiments/red/xing/instances/x31_re24.pg (sha1 49eaf50e, 𝒞^1O), transition 1 -> 2: MF_1 = -1, while gate (4, 8) at state 2
  has level 22. At state 1, 4 and 8 are in R (the level-22 gate is (8, 14), R -> R); at the arena step R collapses from 21 vertices
  to {12}, carrying the high level into F. The true form is OFFGATE (bound M_k, all gates). Box 8 §1.
- (successor 3) CONJECTURE (JUMP-EQ) (box 6 §6.2) FALSE: experiments/red/xing/instances/x31_rx32.pg (sha1 4fe9ec0e), transition
  53 -> 54: w constant since the carry at level 24, σ̄(o) 24 -> 31 (INR), θ rises at level 25, lands THR with θ ≠ w; θ = w only at 55.
  Re-verified n5 55/3, Oink zlk OK, strategies verified. Not needed: Theorem FB (box 7 §4).
- (successor 2, 2026-10-24) Parametric/tropical lens for (X): o as a terminal of value θ is ill-posed for N5 (optimal routes run through
  θ's own play: 247 vertex-states on lev_l_sc; switch-all on the abstract game does not converge on fbref_cex_n32). Gadget version
  (frozen copy of θ's play) has a rank artefact (copies rank differently from originals): its "R* constant" output is void.
- (successor 2) (U*-DROP) "rank(u*) drops between consecutive evicting fallbacks with w fixed": FALSE, 19/19 (ustar.py; fbref_cex_n32,
  lev_l_x, run_x_inr2, x31_lem_t32, s_rt32_final). u* stays at the top rank through every carry.
- (successor 2) (W-LAY) "≤ n−1 W-changing transitions between W-lowerings": FALSE, thclimb_n16_s12 (16 at n 16; θ gates entries).
- (successor 1, 2026-10-24) HMZ-literal elimination for N5 ("the max-slack action of sigma_k is gone within L transitions"): fails on
  returns_rt48 (experiments/red/n5inj/instances; a max-slack edge survives 77 of 78 phase transitions; hmzL.py). Obstruction: the
  gap level max_v g stays constant for ~ the whole phase (gaps.py gmaxrun 77/78, 102/103 on returns_ph64).
- (successor 1) Lexicographic contraction (HMZ Lemma 4.8/5.5 with VJ valuations): impossible. switch-all satisfies Howard >= VI (Lemma
  D, PROVED) yet is exponential in one lambda-phase on switchallexp; VI from Xi_0 stalls at a spurious (c,P) fixed point (switchallexp
  N 3: 45/49 wrong after 300 rounds). Instance: si/instances/switchallexp_N3.pg.
- (successor 1) N5 satisfies Howard >= VI: FALSE (i4_hand + start, vertex z = 9, states 0-2: trust mode; vi.py).
- (successor 1) "abandoned edge => eliminated for the phase": FALSE (fts_g43: 67 returns to positive-slack edges; returns.py).
- S4 subgame-optimal start: switchallexp, counts identical to switch-all (2486 at N=8, doubling).
- S2b LSF: zadehexp 33..15301 (N=2..10, doubling); DLMM Bland counter 2^n - 1; M_L port 2^(L+1) - L - 2.
- S3 steepest: M_L port, identical run to LSF, 2^(L+1) - L - 2.
- S2a MSF (+ msfa, msfc): L-RED's gated Bland counter, 2^N - 1 exactly (reproduced on si.py); the gate decouples level from
  effect through an escaped cycle-creating switch; my obstruction (b) was wrong.
- S1 Random-Action-Removal: FHZ 1410.7530 Thm 6.3 transferred by L-RED (conditional on the transfer lemma).
- Obstruction (a) still stands: Disser-Mosis B_n does not port faithfully to lexicographic valuations (arithmetic rewards).
- Claim F as first stated (bit notion) was false (L-RED's cf1, cf2); F' (play notion, cycle included) holds in the data.

## Freezing observation for MSF (2026-10-15 11:00Z; data + proof sketch, UNREFEREED, not a result)
Setting: VJ valuations, lexicographic order (cycle node first, then path set by rank, then length). Level of an improving edge
(v, w) = rank of the first difference between Ξσ(w) and Ξσ(σ(v)) (docs/si/candidates/S2.md). Call the switch cycle-creating
if v lies on the path set of Ξσ(w).
Claim F: a NON-cycle-creating single improving switch at level r changes no vertex's cycle node and no path bit of rank > r.
Data: experiments/si/freeze_test.py: 0 violations over ~6000 MSF switches on 6000 random games and ~6000 on 6000 1-sink
games (n ≤ 9), same for msfa and msfc; every observed violation is a cycle-creating switch (2-3 per 6000 games) or a
cycle-node change (all of them cycle-creating switches, to be re-checked).
Proof sketch: let τ be Odd's optimal counterstrategy for σ. Under (σ', τ) with σ' = σ[v→w], the play from any u either avoids v
(value unchanged) or runs P·v·(τ-path from w); the τ-path from w cannot re-enter P∪{v} (it would then reach v, contradicting
v ∉ path(w)), so its value is P ∪ {v} ∪ path(w) with the old cycle node, which agrees with the old value P ∪ {v} ∪ path(σ(v))
above rank r. Ξσ'(u) lies between Ξσ(u) (Friedmann Thm 3.2) and this value; two valuations agreeing above r sandwich only
valuations agreeing above r. Gap: the "cannot re-enter" step needs the τ-path from w under σ' to equal the one under σ,
true because the only changed edge is at v and the path avoids v.
Consequence (if F holds): in a run with no cycle-creating switches, MSF makes ≤ n switches at the top level, and level r is
revisited only after a higher-level switch; this gives only an exponential bound by itself (S_r ≤ n(1 + S_{>r})). The
adversary's tool is a high-level improving edge that is cycle-creating until low-level switches change the paths; then it
fires late and unfreezes everything below. Variants: msfa (prefer non-cycle-creating edges), msfc (prefer cycle-creating).

## Refinement (11:20Z, unrefereed): where MSF's iteration count can hide
Under Claim F and Friedmann Thm 3.2, in a stretch of an MSF run with no cycle-creating switch: a level-r switch at v makes
bit r of Ξ(v) good and bits above r never change (F) while Ξ(v) only improves, so bit r of v stays good until a switch at a
level > r; MSF takes the highest level available, and lower switches never create higher-level improving edges (F), so once
level k is exhausted it never recurs; hence at most n switches per level: ≤ n(n+1) switches in the stretch (sketch only; the
DLMM Bland counter shows the mechanism: MSF needs 1 switch, Bland/LSF 2^n - 1).
A cycle-creating switch (v on the path of w; the new cycle through v is even-dominated, level = rank of its dominator) either
changes some cycle node (at most n^2 such events in a run: each vertex's cycle node improves ≤ n times) or is "escaped" (Odd
reroutes, cycle nodes unchanged, high bits may change arbitrarily). So: MSF switches ≤ (n^2 + 1)·(n^2 + X + 1) with X = the
number of escaped cycle-creating switches. MSF is polynomial iff X is (modulo the sketch). The adversarial search now has an
objective "escapes" (adversarial.py --objective escapes) to maximise X directly.

## T12 section 4 follow-up (11:25Z): D_n with Odd gates, why not built as a port
Sources opened: Disser-Mosis arXiv 2309.14034 (ISAAC 2023): section 3 B_n (Table 1: travel/enter/skip/board/stay/leave,
rewards 2^l for enter, 0.75 for stay, -2^l+1.25 for board), Definition 6 (canonical policies), section 4 D_n (Fig. 4: every
edge (v,w) replaced by v -> x_{v,w} -> y_{v,w} (randomisation, p_v to z_{v,w} -> w, 1-p_v back to v)), Thm 28
(p_v = 2^{-N_V(v)(n+5)}; Dantzig prefers small vertex numbers). DLMM 2512.16684 Lemma 5.4 and M_L (Fig. 5.1).
(a) B_n's reward bookkeeping is arithmetic (three 0.75-stays beat one enter(1) = 2); the VJ set order is lexicographic, so
B_n does not port faithfully for n >= 3; M_L does (rewards L^l, see gens.py dlmm_ML) and its port behaves as Lemma 5.4
predicts for the least-preferred rule (LSF 2^(L+1)-(L+2)); the same run kills steepest (S3).
(b) The D_n trick decouples a switch's reduced-cost magnitude (scaled by p_v) from its effect. In the VJ order the sign
and the level of an improving edge are both read at the first-difference position, so I found no gate that gives
"level decreasing in l while the sign follows B_n": an even designer vertex on one route makes the edge always improving,
an odd one never, and a loop back to v makes it cycle-creating with the dominator's parity deciding. Not built; the
gadget-chain search (famsearch.py --seed-template dlmm) and the escapes objective stand in for it.

## MSF bound argument, step by step (for L-RED and referees; 11:35Z). Each step is marked PROVED (here), CITED, or OBSERVED.
Setting. G a parity game, priorities made injective by rank (p' = 2·rank + parity; the game's winner on every cycle is
unchanged: PROVED, since the max-priority vertex of a cycle keeps its parity and order). VJ valuations Ξσ(v) = (c, P, ℓ):
cycle node c (the most relevant vertex on the cycle Odd's optimal counterstrategy τσ reaches from v), path set P (vertices
on the path more relevant than c), length ℓ. Order ≺ as Friedmann 1106.0778 section 3 (CITED). Sink game: Friedmann
Definition 5 (1-sink, sink-seeking) (CITED); in a sink-seeking run every cycle node is the sink.
S1 (CITED, Friedmann Thm 3.2 = [VJ00]): if σ' = I(σ) for an improvement policy I (in particular a single improving switch),
    then Ξσ(u) ⪯ Ξσ'(u) for every u, with strict inequality somewhere.
S2 (definition). An improving edge (v, w) of σ has level r = the rank of the first difference between Ξσ(w) and Ξσ(σ(v)):
    if the cycle nodes differ, the level class is (3, max rank of the two cycle nodes); else (2, max rank in P(w) Δ P(σ(v)));
    else (1, 0). MSF switches one improving edge of maximal level (ties: smallest v, then w). The switch is cycle-creating
    if v ∈ P(w).
S3 (Claim F, OBSERVED, proof sketch): let (v, w) be a non-cycle-creating improving edge of level (2, r) (same cycle node c
    for w and σ(v); path sets agree above r), σ' = σ[v→w]. Then for every u: Ξσ'(u) has cycle node c(u) unchanged and
    P'(u) agrees with P(u) on all ranks > r.
    Sketch. (i) Let τ = τσ (optimal counter for σ). Under (σ', τ) the play from u is either the old play (if it never
    visits v: value unchanged) or P_u · v · (play from w under (σ, τ)) where P_u is the old play prefix from u to v; the
    play from w under (σ, τ) does not visit v (v ∉ P(w) and v is more relevant than ... [GAP G1: v ∉ P(w) says v is not on
    w's path AMONG THE VERTICES MORE RELEVANT THAN c; if rank(v) < rank(c) the vertex v could lie on w's path without
    appearing in P(w). In a sink game every non-sink vertex is more relevant than the sink, so G1 is void there; in general
    the claim must be stated with "v not on w's play" instead of v ∉ P(w)]; and it does not re-enter P_u (else it would
    reach v along P_u). So the (σ', τ)-value of u is P_u ∪ {v} ∪ P(w) with cycle node c: it agrees with the old value
    P_u ∪ {v} ∪ P(σ(v)) above r. (ii) Odd's optimum for σ' is ≤ this value (τ is one Odd strategy; needs: the (σ',τ) play
    value is ≥ Ξσ'(u) by optimality of τσ' [PROVED by definition of the optimal counterstrategy]). (iii) Ξσ'(u) ≥ Ξσ(u) by S1.
    (iv) In a lexicographic order, a value between two values that agree above r (same cycle node, same bits above r)
    agrees with them above r [PROVED: the first difference of the bounds, if any, is at rank ≤ r]. Lengths are below all
    path bits in the order [CITED, definition of ≺]. Data: 0 violations in ~24,000 non-cycle-creating MSF switches
    (freeze_test.py; random and 1-sink games, n ≤ 9).
S4 (PROVED from S1, S3): in a stretch of a run with no cycle-creating switch, no cycle node changes (S3 with the cycle
    component), and a switch at level (2, r) changes no bit above r of any vertex.
S5 (PROVED from S3, S4, S1): in such a stretch, after a level-(2, r) switch at v, bit r of Ξ(v) is the good value (the
    first difference of Ξσ(w) over Ξσ(σ(v)) is at r in Even's favour; Ξσ'(v) = ext_v(Ξσ'(w)) with Ξσ'(w) ⪰ Ξσ(w) agreeing
    above r, so its bit r is at least as good; v itself has rank ≠ r [PROVED in sink games: rank(v) = r would put v on
    one of the two paths, i.e. on its own play, a cycle through v other than the sink, contradicting sink-seeking;
    OBSERVED only in general]) and it stays good until a switch at a level > (2, r): lower switches do not touch bit r
    (S4); same-level switches elsewhere change Ξ(v) only upward (S1) with bits above r fixed (S4), so bit r cannot
    worsen.
S6 (PROVED from S4): a switch at a level < (2, r) never creates a level-(2, r) improving edge: the improving status at
    level (2, r) of (v, w) depends only on bits ≥ r of Ξ(w) and Ξ(σ(v)) [PROVED: by S2, with agreement above r required
    and the comparison at r], which lower switches do not change (S4); σ(v) changes by a lower-level switch at v only to a
    w'' agreeing with σ(v) at all ranks ≥ r [PROVED: that is what level < (2, r) means].
S7 (PROVED from S5, S6 and the MSF order): in a stretch with no cycle-creating switch, MSF exhausts level (2, R) (R the
    top rank) with at most n switches (each vertex at most once, S5), never returns to it (S6), then exhausts (2, R-1)
    with at most n switches, and so on: at most n per level, at most n(n+1) + (level-(1,0) switches) in the stretch.
    [GAP G2: level (1, 0) switches (length only). OBSERVED small; PROVED bound: none written. Sketch: with all path sets
    frozen (S4 with r = -1), a length-only switch at v strictly improves ℓ(v) in Even's direction, ℓ ∈ [0, n], and other
    vertices' lengths move monotonically by S1 with path sets fixed, so ≤ n per vertex, ≤ n² in the stretch.]
S8 (PROVED): a cycle-creating switch at v is improving iff the most relevant vertex d of (P(w) \ P(σ(v))) ∪ {v} ... more
    precisely of the cycle C through v and w under (σ', τσ), is even [sketch: P(w) = C-part ∪ P(v)-part disjointly, the
    comparison with P(σ(v)) is decided at the max of the cycle part]. After it either some vertex's cycle node changes
    (CYCLE EVENT) or none does (ESCAPE).
S9 (PROVED): cycle events ≤ n·(number of distinct cycle nodes) ≤ n²: a vertex's cycle node strictly improves in the
    reward order at each change (S1).
S10 (PROVED from S7-S9, modulo G1, G2): #switches ≤ (n(n+1) + n² + 1) · (n² + X + 1), X = number of escapes.
    [Lead/REFEREE wording: MSF is polynomial iff X is polynomially bounded.]
OBSERVED about X: hill-climb maxima of X: 2, 5, 5, 7, 10, 14 (n = 5..10, small search), 14 at n = 8 with a larger search;
one vertex escaped 7 times in an 8-vertex game (out/adv_msf-esc2_n8.pg), so repeated escapes at one vertex are possible.
No argument bounds X. This is the open point.

## CORRECTION (2026-10-15 11:50Z, credit L-RED via the Lead 11:47Z): "cycle-creating" must be the play notion
L-RED found that si.py's test "(val[w][1] >> rank[v]) & 1" checks membership of v in the path SET of Ξ(w), which holds
only vertices more relevant than w's cycle node; a v on Odd's play from w but less relevant than the cycle node was
wrongly classed non-cycle-creating, and Claim F fails for such switches (L-RED: 6 violations in 11,795 switches on 20,000
random games under the bit notion, 0 under the play notion; 2,649 of 3,563 cycle-creating switches were misclassified).
Counterexamples reproduced with si.py (instances/red_cf1.pg, red_cf2.pg, start sigma(2)=1): cf1's edge (2,3) has level
(1,0), bit-notion 0, play-notion 1, and changes the cycle nodes of 2 and 3; cf2's edge (2,3) has level (2,5), bit-notion 0,
play-notion 1, and changes 2, 3, 6. This is exactly gap G1 of the step-by-step argument above.
Fix (si.py Engine.cycle_creating): v is cycle-creating for (v, w) iff v lies on Odd's (σ, τσ)-play from w before that
play first reaches w's cycle node. msfa / msfc now use it (their docstrings were wrong before; the earlier msfa/msfc sweep
numbers measured the bit-notion rules and are withdrawn). freeze_test.py now also checks level-(1,0) switches (must
change no cycle node and no path bit at all) and reports cycle-node changes by non-cycle-creating switches separately.
Claim F' (restated): a NON-cycle-creating (play notion) single improving switch at level (2, r) or (1, 0) changes no
vertex's cycle node and no path bit of rank > r (all path bits, for level (1, 0)). Data after the fix: 0 violations of
either kind over 8,000 random and 8,000 1-sink games (n ≤ 9), msf; 0 for msfa on 4,000.
Second slip (12:05Z, found by freeze_test after the first fix: 34 of 4,154 random-game switches and 13 of 4,015
sink-game switches classed non-cycle-creating still changed a cycle node): the play from w must be followed INTO its final
cycle, not stopped at the cycle node; v on that cycle after the cycle node also closes a cycle. cycle_creating now walks the
(σ, τ)-play from w until a vertex repeats and reports whether v was visited.
Sandwich argument with the play notion (closes G1): the (σ, τ)-play from w never visits v (definition, cycle included), so
after the switch the (σ', τ)-play from any u is either the old play (never visits v) or P_u · v · (the old play from w),
which does not re-enter P_u ∪ {v} (it would reach v): its value is P_u ∪ {v} ∪ P(w) with cycle node c(w) = c(σ(v)); the
rest is S3 (ii)-(iv). Data after both fixes: see the freeze_test lines below.
Every X measured before this correction (escapes objective) is an undercount; re-measured with the play notion in
out/adv_msf_esc3.log.
freeze_test.py after both fixes (12:10Z): msf, 8,000 random games n ≤ 9, 4,154 switches: cycle-node changes by
cycle-creating switches 1,447, by non-cycle-creating 0; path bits above the level changed (cycle nodes fixed) by
cycle-creating 6, by non-cycle-creating 0; level-(1,0) switches included. Same on 8,000 1-sink games (4,015 switches:
1,130 / 0 / 7 / 0) and for msfa on 4,000 random games (2,065 switches: 717 / 0 / 2 / 0). F' holds in the data.
Consequence for the bound S10: X now counts play-notion escapes, and cycle-creating switches are about a third of all MSF
switches on random small games (1,447 of 4,154), so X is of the order of the iteration count itself there; the bound
(n(n+1) + n² + 1)(n² + X + 1) is correct but says nothing until X is bounded. Re-measured X: out/adv_msf_esc3.log.
The msfa/msfc family sweep (out/fam_msfvar.log, bit notion) is withdrawn; rerun with the play notion: out/fam_msfvar2.log.
