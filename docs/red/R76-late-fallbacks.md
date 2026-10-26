# R76: N5's late fallback regime on the frontier (P-N5-FBRED, ACCEL, EPOCH, FB-2T): no kill; the BGHM gadget collapses; no phase reaches f ≥ n (L-RED successor 19, box 45b; Lead 03:07Z, 03:26Z, 03:39Z, 04:05Z, date -u)
Targets:
- P-N5-FBRED (docs/new/P-N5-FBRED-box44.md, sha1 11b15455): Theorem FB-RED and its late form.
- L-NEW's working doc docs/new/N5-FBF-box44.md, all lane-PROVED and unrefereed:
  - §7 (l-new bca23df8): VI-LB and the BGHM obstruction;
  - §8 (6800a4b7): Lemma ACCEL;
  - §9 (916aa2b3): Lemma EPOCH;
  - §10 (a77693d1): Lemma ALT. Not checked here.
- L-SI's docs/si/N5-2O-box16.md (l-si 67fd31d9): Theorem FB-2T, with ROUTE-2, DIR, SAT-2.
Labels per L40: DATA / READING. Nothing here proves a bound. Every game class, unless a row says otherwise.

## 0. Result
- **No kill. No phase reaches f ≥ n**, so the late regime stays vacuous: N_late = 0 and no fallback g_j with j ≥ n, in every run.
  Best f − n = −2 (library, n3all_maxph_0, a start pair), the same as the Lead's figure.
- 0 FAIL on every check, in every run:
  - FB-RED and its late form;
  - CN-ONLY_D;
  - ACCEL (a) (honest values are simple-path values in U_c) and (SG) (strict gain at every switch of an Even z with λ(z) ≠ z);
  - EPOCH (c), and (a)/(b) where applicable. They never applied: no epoch reaches n − 1 fallbacks;
  - ROUTE-2, terminal-routing acyclicity (|Q_c| ≥ 3), and DIR (exercised 11 times);
  - output correctness against Oink (zlk regions plus strategy verification) on every pinned instance.
- (1) The BGHM Fig. 2(a) gadget, built as N5 games, **collapses**: ≤ 1 iteration and 0 fallbacks from EVERY start pair (§2). The
  mechanism is in §2: Ξ is an exact policy evaluation against Odd's optimal counter-strategy σ̄. A fallback is a policy-improvement
  step, not a value-iteration round, and the "+1 per loop" accumulation does not exist. This is ACCEL's READING, confirmed on
  instances.
- (2) Friedmann's switchallexp / switchbestexp from Odd-optimal start pairs (τ_0 = τ*): 0 fallbacks, one phase, 8-25 iterations. With
  τ fixed and optimal, S4a (Even's restricted best response to τ) does all the work, so N5 escapes the VJ switch-all lower bound
  through S4a (§3).
- Frontier records (pinned, Oink-verified):
  - 39 in-phase fallbacks in one phase at n 48 with |Q| = 4 (fr39_q4_n48). L-NEW's previous frontier max was 17 at n 32;
  - ρ = 144 in one phase at n 32, all 10 Odd choice vertices in one class, with only f = 19 (rho144_n32);
  - 74 κ-levels of one vertex in one phase at n 40 (lev74_n40; the previous best was 52);
  - in-flight climbs at report time: ρ3 = 194 at n 32 (|Q| 12); N_ep = 72 epochs in one phase at n 40 (ρ3 210) (§5).
  Large ρ does not turn into fallbacks.

## 1. Tools (experiments/red/fbr/; engine si.py read-only; trace = experiments/red/o1/o1_19.trace, own copy of n5.py's loop)
- fbr19.py (sha1 0d649319): exact checker, written from the packet definitions (not from L-NEW's fbf.py / epoch.py or L-SI's fb2o).
  Per phase (maximal run with (λ, τ) constant):
  - f, ρ, Q-runs, N_late, late fallbacks;
  - FB-RED f ≤ 1 + (n − 1)(2 + ρ) and its late form f ≤ 1 + (n − 1) + (n − 1)·N_late;
  - CN-ONLY_D: at most one in-phase fallback with S = ∅, and it is the phase's last transition;
  - ACCEL (a): the honest play from z to λ(z) is simple, stays in U_c, and folding SPEC's extend along it reproduces Ξ_t(z) exactly;
  - (SG): for every in-phase switch of an Even z with λ(z) ≠ z, key(Ξ_{t+1}(z)) > key(Ξ_t(z));
  - levels: the max over z of the number of distinct Ξ(z) values in the phase;
  - EPOCH:
    - epochs = maximal runs with σ̄|Q constant, and σ̄|Q repeats;
    - (c) f ≤ 1 + n·N_ep;
    - after the epoch's (n − 1)-th fallback: Ξ frozen (a), no Even switch with λ(z) ≠ z, and ≤ 4n(n − 1) + 1 transitions remain (b);
    - fallbacks per epoch, and the longest S4a run in an epoch (before the freeze);
  - FB-2T:
    - ROUTE-2 at every state of classes with |Q_c| = 2;
    - routing acyclicity (q → first terminal) when |Q_c| ≥ 3;
    - DIR: κ_t(q) ∈ A_q for direct q at t > g_{|U_c|−1};
    - SAT-2: κ_t(q′) ∈ V_{q′}(κ_Θ(q)) at its hypothesis;
    - κopt in DIR and SAT-2 is computed by brute-force simple-path DFS in G_c / G_c^q (Odd vertices forced);
  - ρ3: ρ restricted to classes with ≥ 3 terminals; f − n;
  - output: harness/verify.py on every run; Oink (`--zlk`, then `oink --no -v --sol`) with --oink.
  - Calibration: it reproduces L-NEW's figures:
    - fb17_n32 (sha1 398e23e2): f 17;
    - lap_n6_s1_110421 (4f4fe69c): 3 epochs, 1 σ̄|Q repeat;
    - lev_l_x (n 32): 50 epochs, 36 repeats, 52 levels;
    - longest S4a run in an epoch 55 (x32_rand64).
- libfr19.py (5f24f7f3): library sweep, any class, n ≤ 80, S3 + 5 random start pairs per file.
- climbfr19.py (4d4f2125): hill climb on (game, start pair), with constraints |Q| ≥ QMIN and ≥ 2 Even choice vertices. The objective
  is an expression over fbr19's fields. Bookkeeping caveat: in one run (cl_rise_81) the printed BEST line and the saved best json
  disagree on |Q| and ITER (both have 74 levels). Pinned numbers are from independent re-runs (n5.py --start, check_sol2.py,
  fbr19 --oink), never from the log.
- bghm19.py (b72dc219): the BGHM gadget family (§2). fried19.py (661c3efd): Friedmann families from τ* starts (§3).
  shrinkep19.py (3691a94a): greedy vertex deletion toward an epoch with n − 1 fallbacks.

## 2. The BGHM Fig. 2(a) gadget as N5 games (Lead 03:07Z (1); ACCEL READING check, 03:26Z)
- Construction (bghm19.build(k, gap, variant)), inside one class with cycle node c (Even, self-loop, top even priority). Gadget i:
  - v1 (Odd choice) → {v2, h}, with h even rank R and h → c;
  - v2 (Even) → {l, x} (variant A, x odd rank → c) or → {l, c} (variant B);
  - l has even rank r < R, and l → v1.
  - Chaining (k ≥ 2): gadget i exits into v1 of gadget i + 1.
  - Ω(h) − Ω(l) = 2(gap + 1); one isolated filler vertex per unused priority makes the rank gap the same.
- Runs, EVERY start pair (all products of choice-vertex successors):
  - k = 1, gap 0-6, variants A and B (n 9-21): 4 starts each;
  - k = 3, gap 0-4, variant A (n 21-45): 64 starts each.
  Every run has ≤ 1 iteration, 0 fallbacks, ρ 0, 0 FAIL.
  Pinned: bghm_k1_gap6_A.pg (sha1 08733fd1648a7a14218cd96606204664b1625fe0, n 21) and bghm_k3_gap4_A.pg
  (fd8629f7ae16dd52b81fdd2e38ec8811173cdb18, n 45); n5.py from S3: 1 iteration, 0 fallbacks; check_sol2: zlk OK, strategies verified.
- Mechanism (READING, consistent with ACCEL (a) and the data):
  - In Γ_c, Odd at v1 "earns" one cycle increment per loop and VI needs about 2^{R+1−r} rounds.
  - In G the loop v1 → v2 → l → v1 is a cycle with its own top (l, even). Odd's exact best reply σ̄ never takes it: an even cycle is
    worse for Odd. So σ̄(v1) = h at once, and Ξ(v2) is a simple-path value immediately.
  - Γ_c's −∞ for a loop has no counterpart in N5 inside a phase: a loop would be a λ-change.
  - A fallback switches Even to argmax Ξ, with Ξ exact; it does not take a horizon step. So VI-LB is a valid but loose lower bound:
    the gadget's VI rounds have no N5 transitions to land on.
- Hence f per phase cannot grow by cycle accumulation on this gadget. Any growth must come from monotone climbs through distinct
  simple-path values (ACCEL (a)).

## 3. Friedmann's families from Odd-optimal starts (a test of "τ fixed ⇒ N5 = switch-all PI")
- Hypothesis tested. If τ_0 = τ* (Odd optimal; Oink zlk strategy on W_O), then I_τ = ∅ forever (ENDGAME), and N5 would be S4a plus
  switch-all fallbacks, i.e. possibly VJ switch-all PI, which Friedmann's families defeat.
- Data (pgsolver_port.py; fbr19 with Oink):
  | family | N | n | ITER from S3 / τ* / (σ*, τ*) | phases (τ*) | in-phase fallbacks |
  | --- | --- | --- | --- | --- | --- |
  | switchallexp | 1..5 | 21-77 | 5-10 / 5-10 / 5-10 | 1 | 0 |
  | switchbestexp | 1..4 | 35-110 | 20, 32, 41, 47 / 13, 13, 19, 25 / same | 1 | 0 |
- Refuted for these families: S4a (Even's best response to τ in the improving-edge arena) finishes without one fallback. A fallback
  needs S4a to be stuck, i.e. a τ that hides σ̄-improvements, as in the f39 wave (§4). By the same token τ must not move, which needs
  S4b stuck too.

## 4. What a long fallback phase looks like (DATA)
- f39_n48 (R75 §5, 𝒞^1O, start pair): its 39-fallback phase is a Bellman-Ford wave.
  - Each fallback switches exactly one Even vertex onto the vertex switched at the previous fallback: a path grows from vertex 16 over
    37 vertices.
  - S4a takes none of these steps: they improve against σ̄ but not against τ (o = c_θ).
  - It is one epoch with 39 fallbacks. EPOCH (a)'s freeze needs n − 1 = 47; vertex deletion gets to n 46 (gap −6), and further
    deletions break the wave (shrinkep19).
- Frontier versions keep one wave per class: fr39_q4_n48 (|Q| 4, f 39, ρ 35).
- The restart proxy f − |U| (a second wave would make it positive) reached −2 at n 32 (f 20, |U| 22), and −9 at n 48 (f 39).
- No climb produced two waves in one phase.
- READING: by FB-RED and EPOCH, late fallbacks need Q-runs or epochs that each restart a wave of ≥ |U_c| − 1 rounds in one class.
  A wave needs a long honest path whose vertices switch one at a time. The data never show a second wave over the same vertices
  inside one phase.

## 5. Records and runs
| item | value | where (start) | pinned sha1 | n5.py --start (ITER, fallback) | check_sol2 |
| --- | --- | --- | --- | --- | --- |
| f per phase, frontier | 39 (n 48, \|Q\| 4, ρ 35) | fr39_q4_n48 (start pair) | 8d7e883a98ea19eaf7ebdfd0df4cb2ef8a78762d | 49, 39 | zlk OK, strategies verified |
| ρ per phase | 144 (n 32, 10 Odd choice vertices in one class; f 19) | rho144_n32 (start pair) | 232b9581f027e6dab6ad995d13738784f26deb78 | 32, 20 | OK, verified |
| levels of one vertex in one phase | 74 (n 40; ρ 141, f 7) | lev74_n40 (start pair) | 6f13c0b0ee52d78cf66486ca7fe8e624344986f8 | 97, 8 | OK, verified |
| levels | 56 (n 48, \|Q\| 3; switching transitions 97) | lev56_n48 (start pair) | fb3a61f12c783a0b7af79a45c3dcfd645764b42f | 99, 9 | OK, verified |
- Start files: experiments/red/fbr/instances/<name>.start.json. Field "start" is the per-vertex vector; "n5py_start" holds n5.py's
  --start strings.
- Library (665 files, any class, n ≤ 80, S3 + 5 starts; 3,990 runs; 0 FAIL):
  - checks: 57,825 (SG), 1,646,958 ACCEL (a), 1,946 ROUTE-2, 7,535 routing-acyclicity, 11 DIR (11 hits), 0 SAT-2 (0 hits);
  - maxima: f 38 (dirty_a_best), f/n 0.85, ρ 60, ρ3 36, levels 61, switching transitions 112, N_ep 53 (rise_thin51_n40),
    σ̄|Q repeats 38, S4a run in an epoch 55, f − n = −2; epochs reaching n − 1 fallbacks: 0.
- Climbs (0 FAIL in every evaluated candidate). Completed:
  - fmax + ρ from f39 + q and fb17: best 39 at n 48, |Q| 4;
  - wave restart f − |U|: best −2;
  - levels: best 74 at n 40, 56 at n 48.
  Running at report time, until about 04:49Z; I report their ends when they finish:
  - ρ3 (194 at n 32, |Q| 12, f 16);
  - f − n with ≥ 3 terminals per class (no gain over −9 at n 48);
  - N_late (0);
  - N_ep (72 epochs in one phase at n 40, |Q| 5, ρ3 210; objective N_ep·1000 + ρ3 = 72,210).

## 6. FB-2T's lemmas (L-SI, l-si 67fd31d9): exercised where possible
- ROUTE-2: 1,946 library states plus every climb candidate, 0 violations.
  The general form (routing acyclic for |Q_c| ≥ 3): 7,535 library states plus climbs, 0 violations. This is automatic for positional
  plays, as ROUTE-2's proof says.
- DIR: hypothesis met 11 times in the library (L-SI's data: 1); κ_t(q) ∈ A_q in all 11 (brute-force κopt).
- SAT-2: hypothesis never met (0). It needs a class with exactly 2 terminals and |U_c| − 1 fallbacks inside one q-run after
  g_{|U_c|−1}. Not exercised; it rests on its proof.

## 7. Not done / next
- Lemma ALT (l-new a77693d1, §10) is not checked.
- SAT-2 is not exercised. Next: a climb on its hypothesis count, seeded from the DIR-hit file best_pfz_9504.
- A deliberate two-wave construction is not attempted. It needs two anchors at opposite ends of one honest chain whose values rise
  alternately with λ and τ fixed, plus S4a stuck for every step: a τ hiding σ̄-improvements at each wave.
- One-phase counter: no instance. Levels per vertex per phase stay ≤ 1.9·n in all data (74 at n 40).
