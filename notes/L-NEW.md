# L-NEW notebook ((c) design lane under D14; Lead reading L35)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Box 1 started 2026-10-18 09:10Z (date -u).

## Resume point
SUCCESSOR 2, box 5 (GO 22:47Z, end ~01:30Z), written 22:52Z by date -u; context ~410k (hand over at ~580k).
Box 5 DONE (docs/new/N5-dlm-box5.md):
- The condition "N5 ≈ SSI iff τ̄ ⊆ A_σ" is shown. It fails almost everywhere on DLM's SSI paths.
- N5's step applied to SSI's states only ADDS switches, exactly where the distraction withholds them.
- Module (Odd blunder dummies on DLM's games): SSI stays exponential, N5 needs 2-15 iterations. n5.py, n5b spec and n5b orig agree on every row.
- K6 written. NOT killed.
- Tools: dlm_diag.py, dlm_agree.py, dlm_module.py.
- L-COMP's n5b.py (claude/l-comp 29a6ed17) runs read-only from scratchpad/lcomp/n5-second/n5b.py, with symlinks to
  experiments/hard-families and experiments/harness. Run it with --start FILE (a COMPLETE start pair) and --mode spec|orig.
Box 5 part 2 (23:10Z by date -u):
- Skip states characterised. Harmful skips can be forced in ≤ 88% of iterations, but runs stay ≤ n/2.
- Switch-best coincidence lemma (τ = τ_sb ⇒ N5 step = switch-best step). On switchbestexp N5 follows switch-best's path for 13
  iterations and then leaves it: τ_sb changes 2^N-ish times and N5's Odd step misses every change.
- K7 written (N5-dlm-box5.md §7).
- Tools: n5_skip.py, n5_adv4.py, n5_vs_sb.py, sb_traj.py, sb_tauvar.py.
Attempt 9 (sb_follow.py): a fully followed switch-best run reaches only 37 < 58 under perturbation.
G-N5-TERM reading: REFEREE-2 SIGNED WITH GAPS; N1-N4 applied at e7157417 (theorem unchanged); REFEREE pending.
NEXT candidate for a successor (the sharpest remaining lead): a switch-best family whose arena reply τ_sb changes only in ways that
OddStep(σ_k, ·) reproduces. Test it with sb_tauvar.py (misses at changes must be 0).
NEXT: "N5 ⊇ SSI" is FALSE in general (random games, n5_superset.py); it holds on DLM only. Untried lead: exploit the states where
N5 skips an SSI switch. Otherwise the box-4 NEXT items (a)-(d) below.
Box 4 (kept):
DONE, all pushed (docs/new/N5-killer-box4.md, G-N5-TERM-reading.md, N5-ssi-global.md additions):
- SPEC vs A1-A10 (6014db7) and Q1-Q4 (7039eb5).
- Deeptrap trace (even-N chain).
- Stall lemma (proved, checked).
- Locks: ≤ 2 from all starts; climbs 8 / 11 / 9 / 7.
- Sandwich K4 proved.
- K1-K5 obstruction.
- Killer attempts 4, 4b, 4c (dummy gifts on switchallexp), 5 (label gadget) and 6 (per-bit gadget): all linear, all verified.
- Cycling attack: no repeated state; Ξ-flat climb ≤ 2.
- G-N5-TERM: repair proved as an unrefereed reading (Lemmas A, B + potential).
- VJ00 Lemma 5.8 "2 ⇒ 1" fails at cycle nodes (instance, vj_bruteforce.py).
- VJ00 opened, cost corrected.
N5 NOT killed.
NEXT for a successor:
- (a) DLM-distraction module (caveat 1), not built. Condition: N5 ≈ SSI exactly when Even's best reply τ̄ to τ uses only
  current-or-improving edges.
- (b) A lock that reads the counter (K3). The lesson of 4c: ALL of Odd must stay frozen (K2), since any Odd improvement changes τ̄ and Iτ.
- (c) Referees for G-N5-TERM-reading.md (Lemma B's multiset cancellation).
- (d) L-LIT: check the VJ00 Lemma 5.8 observation against the CAV version.
(Successor 1's handover notes kept below.)
### DONE (all pushed on claude/l-new; docs/new/README.md has one row per approach)
- Box 2: N1 gauntlet step 2 (N1-step2.md, step2/*.csv); S6 numbering rule not killed (S5S6-renum.md).
- Box 3: N1 KILLED (N1-KILL.md, deep traps, gen_deeptrap.sh, instances/killer/); N2 KILLED (padded switchallexp, gen_padsae.sh);
  N3 DEAD AS STATED (N3-blackwell-path.md, n3grid.cpp); deep-trap lemma (DEEP-TRAP-LEMMA.md, optional, gaps 1-2 closed);
  N4 proposed only (N4N5-proposals.md; Lead: do not implement); N5 SSI-GLOBAL = STEP-2 SURVIVOR on data (N5-ssi-global.md:
  SPEC section = the exact reference for L-COMP's independent second implementation; STEP-2 REPORT; killer attempts 1-2).
### IN FLIGHT
- Nothing running. L-COMP: independent N5 implementation from the SPEC section. REFEREE-2: N1-kill faithfulness check.
### NEEDS
- Lead: route the N5 killer design (below) to successor 2.
### NEXT: N5 killer plan (what the global optimum ignores; the fallback trigger)
- What N5 ignores: its Even step optimises against Odd's CURRENT τ (not τ̄ or the optimal Odd strategy), restricted to "keep or take
  an improving edge". A gadget where τ is bad (DLM p. 15 "distracted by the opponent's bad strategy") makes the τ-optimal choice
  among improving edges a WRONG move for the real valuation: e.g. Even prefers an improving edge into a region that Odd's current τ
  leaves open but Odd will close next step; Odd symmetric. Goal: alternating distraction that resets a counter each round.
- Fallback trigger: N5's selection keeps σ and τ when every improving switch is worse than staying against the opponent's current
  strategy (non-sink games; random n = 11 example r00008). If a family forces this at EVERY step, N5 = classical switch-all SI, and
  Friedmann's switchallexp counter behind the stall gadget would be exponential. Adversarial climbs reached 25-42% fallbacks
  (n5_adv.py ... fb); the bench <= 4%.
- Ideas: (1) per Friedmann bit, a stall gadget g_i whose improving switches lose against τ until bit i's lane is set; (2) make τ
  oscillate (Odd's τ-step flips each iteration) so Even's τ-optimum flips too; (3) seed the climb with switchallexp + random
  gadgets instead of random games; (4) climb with fitness = fallbacks on DLM-style sink games (Lemma 5 holds there, so fallbacks
  are impossible on sink games: use non-sink).
- Tools: n5.py (modes n5/ssi; run(g, mode, start, cap) importable), n5_adv.py (climb; fb mode), run_n5.sh (sweep, committed CSV
  with sha1), check_sol2.py (Oink zlk + verify.py, 4 GB cap), summarize_n5.py / plot_n5.py, dlm_gen.py (DLM Tables 1-2),
  gen_deeptrap.sh / gen_padsae.sh / pad_prio.py, anneal_c / n3grid / anneal_dbg (N1 family tools).
- Open debts: VJ00 (Vöge-Jurdziński 2000) not opened by L-NEW (cited for Engine.evaluate's cost); the deeptrap oscillation of N5
  (iterations 26 at N = 6, 15 at N = 7, 33 at N = 8; plain switchallexp is a smooth 2N): CAUSE UNKNOWN, not investigated;
  hypothesis: the best-reward start is "all traps" (P is the top reward) and N5's trap release order depends on tie-breaks that
  vary with N; check with a per-iteration trace (which edges each step switches).

## Sources opened
- arXiv 1008.0530 v1 (Hansen-Miltersen-Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based
  stochastic games with a constant discount factor"), opened 2026-10-18 09:2xZ (pdf, 13 pp). Thm 6.5: Strategy-Iteration
  from any start terminates within (m+1)(1 + log_{1/γ}(n²/(1−γ))) = O(m/(1−γ) · log(n²/(1−γ))) iterations (the n² is
  n²/(1-γ) inside the log). Proof via Lemma 6.4 (every L̄ iterations a new action is never used again). §7: SI is
  "exponential for non-discounted 2TBSG, or when the discount factor is part of the input" (citing Friedmann).
- arXiv 0909.5653 v1 (Fearnley-Jurdziński-Savani, Lemke / Cottle-Dantzig for discounted games), opened 2026-10-18.
  Lemke as a homotopy in the covering parameter z at fixed discount (text near l.250: "how much further z can be decreased
  before σi ceases to be optimal"); Thm 18: Lemke 2^(n+1) - 2 iterations on G_n; Thm 19 Cottle-Dantzig; p. near l.557:
  "standard reductions [16, 21, 13] convert this parity game into average-reward ... discount factor ... very close to 1".
- NOT yet opened (needed for N1's termination bound only): Zwick-Paterson TCS 158 (1996) discount threshold; Puri thesis.
  Used instead, as restated in 2610.22149: Prop. 7.11 = [ZP96, Thm 5.2] ‖λ(γ) − λ‖∞ ≤ 2n(1 − γ)‖r‖∞ (normalised values).
- arXiv 1106.0778 (Friedmann, LMCS 7(3:19)), opened 10:30Z, §9: reward r_Ω(v) = (−|V|)^Ω(v); β_G := 1 − 1/(4·|V|³·max|r(v)|) [p. 35; CORRECTED per L-LIT T19, box 3; earlier text had |V|];
  Thm 9.2 (Puri), Thm 9.5 (Vöge: every parity improving switch is a discounted improving switch), Lemma 9.6 (1-sink games:
  Odd's discounted best response reaches the sink), so the lower bound transfers to discounted payoff games.
- arXiv 2610.22149 v1 (Loff-Skomra, "Smoothed analysis of policy iteration and value iteration for deterministic discounted
  and mean-payoff games played on any graph", 15 Oct 2026), opened 10:35Z. §7.4, Figure 7.2 IncreasingDiscountPI:
  "γ ← (1 + γ)/2; (σ, τ) ← DiscountedPI(σ, τ, γ) until (σ, τ) are optimal in the mean payoff game" = N1. Thm 7.9 (1 − γ <
  1/(4n²Δ(r)) => unique optimal pair), Thm 7.14 (O(m² + m²n⁴Δ(r)² log³(nΔ⁺)) Howard switches), Thm 1.2 (smoothed poly), §9
  open problems. Cites [LS24] = Loff-Skomra, ICALP 2024, LIPIcs 147:1-147:16 (NOT opened).
- arXiv 2402.03975 v1 (Loff-Skomra, "Smoothed analysis of deterministic discounted and mean-payoff games", 6 Feb 2024 =
  [LS24], ICALP 2024 version restricted to ergodic graphs per its HAL listing), opened 11:45Z. Thm 1.10: "The greedy-all
  switches policy iteration rule combined with increasing discount factor solves random instances of deterministic discounted
  or mean-payoff games in polynomial smoothed complexity." Thm 6.6 (Figure 12, IncreasingDiscountPI: halts on every input,
  smoothed polynomial). WORST CASE, verbatim (p. 5, l. 199-201 of the text dump): "Otherwise, for mean-payoff games, or for
  discount factors γ exponentially close to 1, no upper-bound is known on the number of iterations, significantly better
  than the number of policies, which is exponential in √ the number n of states." (same sentence in 2610.22149 §1.2).
  Example 3.5 / §3.2: a deterministic two-player game whose value, as ONE payoff varies in [−1, 1], has 2^Ω(n) break points
  (from [BNRC08] / [ABGJ18]); this is a parametric-PAYOFF statement, not a lower bound for IncreasingDiscountPI. No
  worst-case lower bound for IncreasingDiscountPI is stated in either paper (searched: worst, exponential, lower bound, open).
- arXiv 1208.5083 v2 (Post-Ye), opened 10:38Z: Thm 3.7, the highest-gain simplex rule takes O(n³m²log²n) iterations on
  deterministic MDPs with uniform discount, any discount (Thm 4.8: O(n⁵m³log²n) for distinct discounts).
- Search (WebSearch, 10:30Z) also listed: Madani-Thorup-Zwick, ACM TALG 6(2) 2010, O(mn) for deterministic discounted MDPs
  (abstract page only, NOT opened); Karczmarz arXiv 2110.15070 (NOT opened).

- arXiv 1309.5925 v2 (Allamigeon-Benchimol-Gaubert-Joswig, "Combinatorial simplex algorithms can solve mean payoff games",
  SIAM J. Optim. 24(4) 2014), abstract page opened 2026-10-18 ~18:39Z (box 3): any combinatorial simplex algorithm has a
  tropical analogue solving MPGs (Hahn series + symbolic perturbation); strongly polynomial combinatorial simplex "is open".
  Body NOT opened.
- arXiv 2309.02223 (van Dijk-Loho-Maat, "The worst-case complexity of symmetric strategy improvement", CSL 2024), pdf opened
  ~18:40Z (sha256 10e6794d82aba465..): Theorem 1 p. 2 (exponential for SSI independently of the improvement rule; any
  valuation), Algorithm 2 (SSI, f applied to I), Algorithm 3 (generalized SSI with J-sets), Lemma 5, p. 3 "more than only
  local information".

- Jurdziński & Vöge, "A Discrete Strategy Improvement Algorithm for Solving Parity Games", BRICS RS-00-48 (Dec 2000; full
  version of the CAV 2000 paper, LNCS 1855), https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, opened 2026-10-18 ~21:17Z
  (sha256 485a12de432a2a8c..):
  - §6 shortest-paths procedure, lines 1-10;
  - Theorem 6.2 (p. 25): an improvement step in O(n·m);
  - §1: Bellman-Ford O(n²·m);
  - §5 Lemmas 5.2-5.9: Improve(σ) = σ iff σ is optimal (Lemma 5.8);
  - §7: number of steps open (2000).
  Box 4 used it to correct N5's cost statement.

## Dead ends
- N2 (PRIO-ANNEAL), KILLED ON DATA 18:05Z UTC (box 3; first implementation n2.py). Padded switchallexp
  (gen_padsae.sh; dummies block compression): largest stage 6, 15, 34, 72, 148, 300, 604 (N = 1..7). Instance
  experiments/new/instances/killer/padsae_N7.pg (sha1 9ee0385509ac81f2dd9eb111df2ecbdabdfa87b1, n = 230): stage of 604.
- N1 (LS24 IncreasingDiscountPI on parity rewards), KILLED ON DATA 2026-10-18 17:54Z UTC (box 3; unrefereed; docs/new/N1-KILL.md).
  Obstruction: deep traps (trap priority gap P - q > max priority + 2) hold Even in all traps with positive values until a phase
  after the parity-like horizon; that single phase runs Howard from the best-reward start = Friedmann's counter. Instance:
  experiments/new/instances/killer/deeptrap_sae_N7.pg (sha1 835ce1326ca36e318bd59d54aead26eee6d36b24, n = 239): 1244 Even
  switches in one phase; N = 1..7: 11, 31, 71, 151, 311, 631, 1244.
- X1 SCALE-VI (2026-10-18, screened out by argument before code; Lead 10:00Z: record as dead end by argument). Bit-scaled
  energy value iteration: phase k solves the energy game with weights ceil(w / 2^k), warm-started from 2 f_{k+1} (valid
  lower bound since ceil-weights at k+1 doubled dominate weights at k). Obstruction: vertices whose winner flips to Odd in
  phase k must be lifted to the top value, about n·W_k lifts, and nothing bounds the flips per phase. That is small-progress-
  measure behaviour (pseudo-polynomial per phase). Instance: none run. Any game where a low priority decides an Odd win
  late (a single Odd self-loop of priority 1 reached through high even priorities) forces the climb in the last phase.

## Things only I know
- N5 Odd output strategy is σ̄ (Odd's optimal counter to the final σ), not τ. n5.py mode ssi reproduces DLM Prop. 7 exactly:
  use it as the engine check after any change. The Lead's clock stamps were ahead earlier; always date -u.
- N5 fallback: on non-sink games N5's selection AND SSI's I can both be empty (random n = 11 game r00008); the fallback is one
  classical switch-all step. Waiters: never `pgrep -f <script name>` in a loop whose own command line contains that name; wait on a PID.
- Run date -u for EVERY timestamp, including message first lines; in box 3 I estimated two stamps (18:22Z, 19:05Z) that were
  20-55 min ahead of the clock. Commit times (TZ=UTC git log --date=format-local) are the reliable record.
- out/ does not survive a container: cite only committed CSVs. Python Zielonka is exponential on counter_rr/counter_m (b ~1.6):
  never use check_sol.py as the sweep checker there; check_sol2.py (Oink zlk, tl fallback) is the sweep checker.
- Never edit a running bash script in place with an editor that keeps the inode (bash reads it lazily); sed -i is safe (new inode).
- N1 stop test: "sigma has no VJ improving switch" is WRONG as a stop test (a region-correct sigma need not be VJ-optimal;
  tc 4 stalled at j = 102 forever). The certificate (sign of values + harness/verify.py on both restricted strategies) is right.
- Merging equal-parity neighbouring priorities alone kills Friedmann's switchallexp for plain VJ switch-all (10, 7, 9, 11, 13 for
  N = 2..6): the counter depends on strict priority order; merged ties are ranked by index. Any test of an SI-type method must
  say whether it merges. Adversary can block merging by dummies.
- N1 on switchallexp is invariant under priority spreading p -> K p (K = 3, 9: identical even/odd iteration counts; phases
  scale by K). Reveal order of decisions, not their absolute horizon, determines the run.
- N1 ablation (straight at the final gamma) = Friedmann's counts exactly, matching 1106.0778 Thm 9.5 / Lemma 9.6.
- The exact integer-scaled evaluation (Q = b^n * prod over cycles (b^L - a^L)) is only ~25% faster than Fractions; the cost is
  the number of phases (~(d+3) log2 n without merging) times big-number comparisons.
- Index dependence in L-SI's engine: the vertex numbering enters (a) the injective priority rank (ties of equal priority by
  index), (b) the best-reward start (ties), (c) the zadeh tie-break / the cunningham cyclic order. A renumbering changes all three.
- N1 counts on switchallexp are insensitive to every delay/trap transform tried (key-edge delays up to 100(i+1): EXACTLY
  25, 42, 64, 90); the largest phase is always the final one (2N + 5). Friedmann's games: Odd wins every vertex.
- In 1-sink games the region certificate needs Odd's discounted best response to be globally winning; certificate-stopped
  VJ Howard reaches that after 2^(N-1) + O(1) iterations (vjcert --certstop); N1 after ~2.6 N².
- The dual transform (owners swapped, priorities +1: dual.py) makes Friedmann's families trivial for Howard (N + O(1)).
- renum's best numberings have no readable class structure (as L-RED R7 found); lift.py transfers numbering by labels and
  keeps most of the count (Cunningham switchbestexp N = 2 -> 3: lifted start 688 vs best 939).
- Big-d random games (n ~ 350, d ~ 350) take minutes in anneal_c: ~3,000 phases of ~1M-bit numbers.
- (succ. 2) n5_lock.step / n5_trace copy n5.py's loop for logging and assert equality with n5.run; never cite them without that assert.
- (succ. 2) VJ "improving" at a cycle node: a switch that closes a cycle through its own cycle node can change the strategy with
  Ξ unchanged (Odd 1→3 instance in N5-killer-box4.md §3). Every one-switch argument must exclude cycle-closing switches and cycle nodes.
- (succ. 2) Engine.evaluate's tie-break is static (index order). Any design that makes candidates TIE against τ turns N5's step
  into an index rule, not a stall.
- (succ. 2) The container's clock runs differently from your sense of time: always date -u.
