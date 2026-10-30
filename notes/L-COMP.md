# L-COMP notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point -- ACTIVE: successor 8 (session_01V5yGRWL1xbdLiUMMLuy7vR, Opus 5.5), started 2026-10-30 13:10Z by date -u. BOX 23.
- Lead brief 13:09Z (D18): true maxima of R*_F and FL_F per W-run (box 85 FREE-RED). Everything in experiments/n5-box23/README.md.
- Lead reading 13:22Z: "earlier" = strictly earlier (q < t); report incl (q <= t) too. (incl = strict PROVED, mine: S4a/S4c adopt only
  improving edges.) Do not retry the PGSolver OCaml build (box 21 diff stays unrouted).
- BOX 23 DONE (README has every table): (a) rstar.py = xirise.py on 1,132/1,132; (b) C(4) exhaustive all starts: R*_F <= 1, FL_F <= 1,
  random n 5 / 6: R*_F 1, FL_F 1 / 2; (c) climbs R*_F ~0.7-1.0n (42 at n 60); (d) latew: R*_F = K·m = Theta(n^2) per W-run, 1,344 at n 778.
  15 witnesses pinned (pin23.py ALL OK). IN FLIGHT: nothing. NEEDS: next box from the Lead.
### Things only I know (successor 8)
- red/n3/instances/n3cov_lean.start is invalid (R99); start files must be overlaid on S3 dropping invalid entries (rstar.overlay).
- pkill -f / pgrep -f with a pattern that occurs in your own command line kills / matches your own shell (bit me 14:45Z).
- climbs/*.log and *.out are in .git/info/exclude; results/climbs_end.txt collects the END lines for commits.
- R*_F <= |F| and FL_F <= |F| trivially, so R*-POLY and FL-POLY together = W-run length POLY (FREE-RED makes it an equivalence).

## Resume point -- PARKED: successor 7 (session_01V5yGRZrRdwiCSQqHfS2zGE, Opus 5.5), 2026-10-29 19:2xZ by date -u. Lead 17:49Z: box 22 last, then park; no successor for now.
- Handover check 76a57b40 (successor 7's answers in docs/agents/handover-checks/L-COMP.md). Boxes this session: 17-22, all under experiments/n5-box17..22/
  (one README per box: definitions, cross-checks, every table, every pinned sha1). Every push via scripts/push.sh, verify PASS each time.
### DONE (all DATA unless labelled)
- BOX 17 (exhaustive small-n tables of L-SI's quantities): box17.py = my implementation on n5b of REL cutting / SEG-COUNT EXC / SEG(S) /
  L-WAVE' gap / f per phase / DL-RUN deadlocks; xcheck.py = field-by-field equality with L-SI's own tools (seglast.segs, segsw, relseg,
  lwave PMODE=1, chg/dlock.py) on all L-SI/L-RED pins + 4,000 random games: 0 mismatches. Model C(n) (all owners, parity patterns, successor
  sets; ids in rank order; privar.py: priorities matter only by rank+parity). EXHAUSTIVE n <= 4 with ALL start pairs (C(4): 12,960,000 games,
  268,435,456 pairs), L(3) all rank orders; random n 5-8. 0 violations; max EXC 0, SEG 3, L-WAVE' gap 3 = n - 1 (tight on 384 trajectories),
  f 1, no deadlock step at all (least n with DL-RUN in [5, 20]; segcount_kill_n20 is 1-minimal under vertex/edge deletion, dlshrink.py).
- BOX 18 (T32): nm.py carries (= T32 and T33 brute force on all K=6 pairs, all parities; = L-RED gatep.py counts). NM <= 1.18n (pl130_n40);
  LIP DEAD (ladderd0_k12_n48 [0,13] v 14); HAM-MONO DEAD in all forms; NEST-FACE (ii) PROVED (mine, unrefereed) from R84 monotonicity.
- BOX 19: CUT-Φ DEAD (b4_n5_other_0, n 5: cycle-appearance cut with no path-set change; wk1_n32 σ̄-type).
- BOX 20: N5-SF SBC tables (sf20.py on L-NEW's n5sf.py verbatim copy, n5-box20/lnew_box54 @ l-new 56a42d4f): n <= 3 exhaustive, C(4) every
  16th game, random n 5-8: 0 cycle/region/opt violations, max SBC/n 1.17.
- BOX 21: PGSolver friedmannsubexp / fearnleysubexp ported (hard-families/pgsolver_port.py); byte-identical to L-LIT's T47 generator on 36
  (family, N) pairs N 1..12 (+ friedmann N 13..20); NOT diffed vs the PGSolver binary (build refused by the permission classifier).
  N5 linear (friedmann 4N+3 S3 / 4N+13 lastedge, N <= 16); N5-SF SBC ~ 0.08n on friedmannsubexp N <= 20 (DSB = SBC + 1, no cycle-centre
  counter). check.sh gate n5-box21/check.sh.
- BOX 22: fcN (L-RED R115) rebuilt from my own switchbestexp port (fc3/6/10 sha1 = L-RED's); sfb.py = N5-SF on n5b (= n5sf.py on fc3-6, fc8
  and 1,000 random games). N = 3..16, S3: L-RED's iteration counts reproduced exactly; SBC_σ = N² for N <= 14, then 227 (N²+2) at 15 and
  257 (N²+1) at 16; SBC_τ = N. N5 itself on fcN is linear (41..129, ≈ 6.3N + 22, 0 fallbacks).
### IN FLIGHT: nothing. No background jobs. Parked on the Lead's 17:49Z order (no successor for now).
### NEEDS: none from the owner. Open (not routed): a PGSolver binary diff of friedmannsubexp/fearnleysubexp if an OCaml build is ever allowed.
### Things only I know (successor 7)
- An experiments/n5-box17/enum.py name shadowed stdlib `enum` (any `import re` broke): never name a module after a stdlib module (renamed exh17.py).
- pgrep -f in an until-loop matches its own command line (bit me again 10:3xZ): wait on files/line counts, not process names.
- run_parts.sh N P: resumable parts (skips existing JSON); merge.py merges; parts' .log files are in .git/info/exclude locally only.
- n5x (L-SI/L-NEW engine) is ~2x faster than n5b for N5-SF; sf20.py caches each state's step per game, so all-start tables cost ~ #states.
- Building PGSolver (ocaml/dune) is refused by the auto-mode classifier ("Code from External"); apt install of ocaml was allowed.
- Oink must be rebuilt per container (scripts/setup_oink.sh, ~5 min); verify.sh needs it.
- L-SI's rows() uses n5x; its "fb" is the flag of the transition LEAVING a state; runs() splits at k with fb; phases need j > i.

## Resume point -- PARKED: successor 6 (session_01JPReGnoQGuUgg6d59WzGYS), 2026-10-28 22:1xZ by date -u. Lead 22:06Z: BOX 16 CLOSED, park.
- Last pushes: aeff7b04 (box 16 §4/§5), eabb3018 (XR-LIN repro), d9197efe, 973520df. Both 973520df and aeff7b04 merged by the Lead.
- No background jobs. Oink was built in this container (gitignored; rebuild with scripts/setup_oink.sh).
- Open (not routed): an H_n variant whose Odd gate must re-open many times (Odd's S4b as a counter). That is L-RED / L-NEW design work;
  a future L-COMP successor measures it with experiments/friedmann-hn/randstarts2.py --var (add the variant to hn_var.VARS).
- Trap this session: a Lead message claimed 973520df was on trunk when it was not. Check with `git merge-base --is-ancestor`
  before relying on such a claim.

### Box 16 history (successor 6), 2026-10-26 by date -u
Handover check 9c5bd6e2 (Lead: 5/5). GO 19:18Z. Everything: experiments/friedmann-hn/README.md.
### DONE (DATA)
- hn.py: H_n from [F] §8.4 Table 7 (arXiv 1106.0778, sha256 46c96f44...); Fact 8.1 asserted; mode fig (gate priorities 8i-5.., Fig. 8-10;
  Table 7 as printed collides with the lane: not injective) and mode table. M1's switchbestexp is NOT H_n (25N+10 vertices).
- iglo.py: I^glo (PGSolver switch_globally_best port) from ι: 16*2^n - 21 steps (n 1..6), Lemma 8.3 holds: H_n faithful.
- box16.py on n 3..8, 10, 12, 16 (F = (ι, σ̄(ι)) = Fs3, S3, G<k> mid-counter): 45 runs OK (n5 = n5b = L-SI rows; Oink zlk; verify), 0
  violations. N5 LINEAR: S3 it 6n+4, longest 5n+1 exact; F it 8.06n+9.4, longest 7.06n+3.4. Shape: n tau changes (e_i -> h_i, one gate
  per iteration, empty phases), then one final phase (lane walk + ~1 sigma-bar flip per gate, ALT ~ n+2). f = 0, lambda_Xi const.
### DONE after RESTART (2026-10-28)
- XR-LIN reproduction (eabb3018): experiments/xr-lin, n5b only: Xi(o) changes 86 > 2n = 82 on l121reader_n41, run on 0..39 = long121_n40.
- §4 randstarts2.py (XR, ALT, TF per run): 1,612 H_n runs, 0 FAIL, all linear; τ re-flips at a gate at most twice.
- §5 hn_var.py dual / ex: linear in n; gate flips ≤ 2 / ≤ 1; dual phases = it + 1; ex F phases 3n + 3.
### IN FLIGHT: nothing.
### Things only I know (successor 6)
- exh.py imports L-NEW's experiments/new/box25 'common'; L-SI's gcx needs experiments/si/root 'common': box16.py pops sys.modules['common'].
- n5b.read_start with no TAU0 line leaves tau all -1 (truthy list, S3 not used): always write both lines.
- [F]'s start σ̄(ι) equals S3's τ on H_n (same start sha1).

## Resume point -- HANDOVER of successor 5 (session_017XFY64b42Hkc6fmeUEzwek, Opus 5.5), parked 2026-10-26 ~19:0xZ at ~515k context
Boxes this session: handover check 1a8a4628; box 12 epoch census cf441de1; HON-FF add-on 15bcfa06; box 13 growth law + rho_q table 73e72e55;
box 14 NCONF 6f782d57 + EP-ASM dda29260; box 15 UL_G / GCI-LEN (this push). Everything: experiments/n5-epoch/README.md (one section per box,
every command, every sha1). No background jobs. NEEDS: next box from the Lead (successor 6).
### DONE (all DATA; 0 violations of any landed or lane statement tested)
- census.py (EP0/ALT/NEP/XEP/SPLIT/EPOCH/MONO), honff.py (HON-FF; IMM/IMM' dead confirmed), rhotab.py (= L-SI relay.py exactly), nconf.py
  (= L-NEW nep90 exactly), epc.py (EP-ASM in the Lead's form), ulg.py (UL_G, GCI-LEN; = L-RED on b6_xs_n24).
- Records pinned in experiments/n5-epoch/instances/ (pin.py: n5.py = n5b states, Oink zlk, verify.py): nep94_n48 (N_ep 94, NCONF_{>=2} 93),
  nep92_n40 (92), lend107_n32 (|D| 3 epoch len 107 = 3.34 n), lend82_n32, ret14_n48 / ret14_n64 (R0_{>=2} 14), ffin12_n32 (12 fallbacks in one
  honest gap), gci2_n12 / gci3_n24 (gated global C-intervals n - 3 / n - 4).
- Growth law: not separable (fresh climbs b <= 0.5; seeded b ~1.2-1.3 seed-dominated; fixed k = 5 all b <= 0); only the |D| >= 2 epoch
  length still rises with budget at n 32 (58, 63, 62, 82, 107/95 for 240 ... 7,680 s).
### Open items for successor 6
- L-SI's FREEZE-G per-gate reset count (Lead 15:04Z (5); docs/si/N5-ROOT-box20.md §9): NOT RUN.
- Longer lend doubling at n 32 (15,000 s+), several seeds (seed variance is large: 107 vs 95).
### Things only I know (successor 5)
- TRAP that bit me: Lead messages queue while a long tool loop runs; four arrived during box 14 and I read them only at its end (C-ONCE and
  UL_C were already dead by then). Check: call ReadNotifications between every wait step of a long box, not only at the end.
- Engine: n5b.N5(g, mode="spec").run(..., trace=, fbtrace=); census.state_info gives Xi, sbar, lam, lamW, W, D, RD, H per state.
- honff.lev(g, SG, Xi, lam, oddmap, budget): LEV in G_tau (oddmap = tau) or H_C (oddmap = sigma-bar); optimistic-completion prune verified by
  levcheck.py (0 mismatches vs brute force).
- climb.py fitnesses nep, lend2, nconf2, ret02, gdl, ulg; --fixk keeps |Q|; seeds padded with Even self-loops; replay any best with
  census.py FILE.pg:FILE.start. Wall-clock budgets: steps fall with n (n 64 seeded ~1-2k steps); always report steps.
- runjobs.sh JOBFILE (env P parallelism) runs climb job lists; fit.py DIR fits END lines.
- Stop-hook: untracked climb logs trigger "uncommitted changes"; wait in-turn (10-min steps) or commit partial logs.
- epc.py's "runs" in box-14 outputs mixed game and fallback-free runs (fixed to ff_runs later).


## Resume point (successor 5, session_017XFY64b42Hkc6fmeUEzwek, Opus 5.5) -- box 12 (epoch census) DONE 2026-10-26
Handover check 1a8a4628 (Lead: 5/5). Box 12 GO 07:57Z. Code + tables: experiments/n5-epoch/ (README.md has every command and number).
### DONE
- census.py (n5b SPEC engine, own definitions pinned to RESULTS R60/R61/R63/R64): N_ep, ρ, ALT classes, |D_E|, len(E), X_SN^pre; falsification
  tests EP0/ALT/NEP/XEP/SPLIT/EPOCH/MONO/D-EPOCH with mutation controls. 0 violations on named (60 runs), lib41 (1,236), random C^kO (100,000),
  exhaustive C^2O n 4 all starts (3,538,944), C^2O n 5 every 10th (10.8M).
- Climbs (climbs.sh): N_ep 76 at n 40 (nep76_n40, seeded rise_thin51), 56 at n 32; |D| >= 2 epoch len 55 at n 32 (lend55_n32, |D| 4), 47 (|D| 2).
  All pinned with pin.py (n5.py = n5b states, Oink zlk, verify.py).
### Box 12 add-on HON-FF DONE (15bcfa06). Box 13 DONE (growth law; rho_q table): see experiments/n5-epoch/README.md "Box 13".
- Scaling climbs: fresh exponents <= 0.5, seeded ~1.2-1.3 (seed-dominated; steps fall with n); budget doubling at n 32: lend still rising (82).
- rhotab.py = L-SI relay.py counts exactly on lib41; N_ep records have acyclic star relay graphs (root q = 0 ROUTE-only).
### Box 14 (NCONF add-on 6f782d57; EP-ASM box GO 15:04Z) DONE: README "Box 14" (both sections). Item (5) FREEZE-G NOT RUN.
### IN FLIGHT: nothing (no background jobs). NEEDS: next box from the Lead. HANDOVER: this session parks at ~480k (Lead: handover ~600k).
### Things only I know (successor 5, box 13-14)
- climb.py fitnesses: nep, lend2, nconf2, ret02, gdl; --fixk keeps |Q|; seeds padded with Even self-loops. runjobs.sh JOBS (env P = parallelism).
- Wall-clock budgets: steps per climb fall with n (n 64 seeded ~1,000-2,000 steps); compare steps before reading a trend.
- fit.py parses END lines of *.log in a dir; family = <fit>_<fresh|seed|seed90|k5>_n<N>_r<R>.
- epc.py's "runs" counter in b14 outputs mixed game runs and fallback-free runs (fixed to ff_runs afterwards; ff runs = phases + f).
- honff.lev(g, SG, Xi, lam, oddmap): oddmap = tau gives LEV in G_tau, = sigma-bar gives LEV_C in H_C.
- rhotab.py reproduces L-SI relay.py exactly with --lsi-starts 4 --nmax 48 --kmin 1 (random.Random(path) starts).
### Things only I know (successor 5)
- n5b.run has an fbtrace hook (fallback flag per transition), no effect on the run.
- lib41.txt contains games up to n 492 (not n <= 64).
- climb.py mutates the start pair too; replay with census.py FILE.pg:FILE.start (the .start is SIGMA0/TAU0).
- check_instance.py's analyse assumes C^1O; use experiments/n5-epoch/pin.py for k >= 2.
- Background watchers using `until ... ; do sleep` hit the 10-min foreground limit; run them with run_in_background.


## Resume point (successor 4, session_01AiLCefKYn3CkbJsYJtY5aR, Opus 5.5) -- HANDOVER after box 11 (2026-10-26 07:3xZ by date -u)
Handover check cd3b5ff7 (5/5). Boxes run: 7 completion, 8, 9, 9b, 10, 11 + N5 step-2 diff. Last push: see git log (box 11 1d2f29d7 + this).
### DONE (all pushed on claude/l-comp; every number is DATA unless labelled)
- Box 7 complete (4633d132): box7.py + box7w.py on the whole n 5 subset (68,764,800 runs), 0 violations; J <= 1, Z <= 1, K = 0, S_o <= 1.
- Box 8 complete (758d02ef): box8.py = REFEREE-2 oe/cls/sn/h1_check (start pair) + REFEREE probes (canonical) on n 4 / n 4 all starts /
  n 5 subset: 0 violations; max J 1, K 0, X <= 3, X_SN <= 2, REL <= 3; VACUOUS: CLS1/FBL/CLU, WK, ABS-L.
- N5 gauntlet step 2 closed (45def408, a47b3fa3): experiments/n5-second/seqdiff.py; n5b SPEC = n5.py state by state on 22,810 runs +
  box 43/44 frontier 459 runs.
- Box 9 (52e326aa..589dc66c): climb9.py; WK non-vacuous (9,020 checks pass; wk1_n32, wk2_n32); CLS1 small-n climbs n 6-12 vacuous;
  ABS-L climbs: 0 theta-changes above L.
- Box 9b (86193e62..589dc66c): gdnc_check.py (G_D-NC b'/c1'/c2', C2-H3, FRZ-U_H3), frz_climb.py; FRZ instances frz1/frz3_n24 test FRZ-U_H3
  as proved, frz2_n24 only the stronger 1-based form (author: 0-based); not-(NC) case of FRZ-U_H3 VACUOUS (tau changes after 80% of
  not-(NC) states).
- Box 10 (95f35638, 16c960b5): instances/notnc/ (8 pinned (h3_D) and not-(NC) in-phase states); n5tau.py + tau_check.py: N5^tau on 26,573
  runs, 0 violations of R48 (i), R50 (h), R51 (a) via REFEREE-2 fbpoly_check / kw_check unmodified; N5^tau != SPEC on 497 runs.
- Box 11 (c4fef4b0, 1d2f29d7): citeclosure.py: RESULTS closure of R48, R50 = L-NEW's §9.2 list exactly; rund_check.py: OFFSET (a)-(c),
  TWIN-GAP (i)-(iii) 0 violations on 322,065 runs, TWIN-GAP (ii) vacuous.
### IN FLIGHT: nothing (no background jobs). NEEDS: none open from the Lead; next box to be routed.
### Things only I know (successor 4)
- Runners live in the scratchpad (lost with the container); every command is in the README sections / script headers.
- gdnc_check.state_info is the shared state machinery for gdnc_check, frz_climb, rund_check (D_k, u(v), pi_v, NC, h3, M_D, h_D).
- REFEREE-2 checkers expect FULL strategy lists with the non-own entries CONSTANT along a run (out_check compares whole tau lists);
  tau_check.full() fills them with succ(v)[0]. My first version used one combined list and produced 3 fake "fallback changes tau" FAILs.
- .start formats differ by lane: SIGMA0/TAU0 v:w (mine, L-NEW), bare v:w pairs (L-SI si/instances), 'sigma [list]' / 'tau [list]'
  (L-NEW box45). seqdiff.readstart handles the first two.
- L-NEW's DIV is measured on the restricted game G'_E of an epoch, not on G: div_n8 diverges only on its G'_E (results/tau/divE_n8.pg).
- citeclosure.py: lane report numbers collide with RESULTS numbers (L-RED R73, docs/red/R72-, OUT-R1, NEB-R1, P-N5-NH (R1)); filters
  are in TOK / LANE; R1/R2 hits left are DATA/SIG-only labels.
- climb best files are overwritten on equal fitness; the logged seed is the last STRICT improvement: replay with score(g, seed) may not
  reproduce; search many random starts on the best instead (done for frz3/frz4).
- Never `pkill -f` (killed my own shell twice); kill by pid. scripts/push.sh can take 10+ min under full CPU load.

## Resume point (successor 3, box 7, 2026-10-25 by date -u) -- HANDOVER
### DONE box 7 (Lead GO 23:2xZ; amended 00:28Z: (c) via L-RED u23x.py; 00:33Z: NO-WAKE false, table K and S_o instead)
- box7.py (R23 WM/LV', R24 CASC/TB/U1, R25 FB/MONO, J): n 4 canonical, n 4 all starts, n 5 quarters 1-2: 0 violations, max J 1.
- box7w.py (K, S_o, rise causes, u23x P-N5-U23, E, K_W): n 4 canonical, all starts, n 5 quarter 1: 0 violations; max K 0, S_o 2, E 1, K_W 2.
- README "Box 7" (rows Q234ROW / W5ROW to fill).
### IN FLIGHT (resumable; rerun the same command, finished tasks are reused from results/box7/<tag>.tasks/, gitignored)
- At park (04:3xZ): box7.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only --every 4 --offset 2 (then --offset 3)
  --jobs 4 --out results/box7, ~2 h each, running unattended in this container (scratchpad run7x.sh). A successor reruns the same
  commands; finished tasks are reused from results/box7/<tag>.tasks/ if the container survives, else they restart from zero.
- Not started: box7w on n 5 quarters 2-4 (same command with box7w.py and --offset 1/2/3).
### Things only I know (box 7)
- nowake.py / mblock.rows_w and u23x.rows_x hard-code start_pair(..., None); box7w rebinds the module-level name start_pair.
- u23x.rows_x caps runs at 400 states (fine for n <= 5).
- A container restart loses the .tasks caches only if the directory is lost; they are gitignored, so a new container restarts the
  n 5 quarters from zero.

## Resume point (successor 3, box 6 end, 2026-10-24 23:0xZ by date -u)
### DONE box 6 (Lead GO 20:0xZ)
- box6.py: exhaustive checks of P-N5-NH (c7981ee) F1°, TC (i)-(iv) and CONJECTURE (OB_R) per crossing-free interval; --every/--offset
  sampling, resume. 0 violations on n 4 canonical, n 4 all starts and the WHOLE n 5 subset (4 quarters = 68,764,800 runs, 100,587,132
  intervals, 3,432 OTHER blocks); F1° and (OB_R) attained (slack 0), never exceeded. n 4 canonical: (OB_R) vacuous.
- X chains: one-wave ~0.8-0.9n; wave chain from L-RED x32_waves32; long climbs at n 32: X 67 / 75 / 77 at 360 / 1,500 / 2,400 s
  (b6_xl2_n32, 2.41n); n 40: 79, n 48: 84. X rises with budget at fixed n: maxima are lower bounds. README "Box 6".
### IN FLIGHT: nothing. Queue: longer X climbs (budget is the limit); a k-digit wave design is L-RED's target, not mine.

## Resume point (successor 3, session_01BmytANWGKiHZhXK9QC2rB2, Opus 5.5; box 5 = X / O per joint lambda-phase; 2026-10-24 by date -u)
Handover check 0ef77018 (5/5, Lead GO 17:5xZ). Box 5 started 17:52Z.

### DONE (pushed on claude/l-comp)
- box4.py: X (crossing transitions), O (OTHER-touching), Xmn (X - n), Xplen/Oplen; --slices + resume (OUT/TAG.tasks/<i>.json);
  --no-reentry. xo_validate.py: equal to L-NEW box28 xcount.py on 33 instances (4 pinned ones included). shrink.py --prop X/O/canonX/
  canonO --thr T. climb5.py (X/O hill climb, optional SEED.pg padded to n). xo_split.py (box 29 split per crossing-free interval).
- Tables: n 4 canonical (X 2, O 1), n 4 all starts (X 3, O 2), random n 6-16 (X <= 4, O <= 3), climbs n 6-16, seeded O chain
  n 10-40 (b5_o11, b5_os_n12..n40: O = phase length, 11 .. 77, O/n peaks 2.14 at n 28). README "Box 5".
- Reported to the Lead at once: O > n (18:27Z), O/n rising (19:00Z), O split (19:13Z: F1° and (OB_R) hold; growth = F-changes).

### IN FLIGHT
- n 5 canonical subset: DONE 19:56Z (68,764,800 games, all 160 slices; results/box5/box4_n5_ed2_od2_nf_cyc.json).

### Things only I know (box 5)
- L-NEW's |R| (reach_o) excludes o; thtrace.Rset (mine, xo_split) includes o. X is the same either way; for (OB_R) compare with
  |R| without o.
- box29 scripts live on claude/l-new only; run them from a git-archive copy with PYTHONPATH=experiments/new:experiments/si:
  experiments/harness and symlinks box25/box28 next to box29 (python -I breaks their sibling imports).
- Climbs are very seed-dependent (O at n 10: 11 once, 6 twice at 300 s); seeding from the previous best is what made the O chain.
- Every O-chain phase is pattern 23 throughout, tau constant: the long phases are Even-only improvement runs at fixed tau.

## Previous resume point (successor 2, kept for its "Things only I know"; LANE-RESTART step 1; successor 2 parks after box 4, 2026-10-24 ~17:40Z by date -u)
Session session_01TpuThMoeBcLB2T5KKeJpAa (Opus 5.5), boxes this session: N8d step 2 + switchbestexp + box 2b (2026-10-23),
box 3 and box 4 (2026-10-24). Lead asked to park at ~587k context after box 4.

### DONE (all pushed on claude/l-comp; merged by the Lead up to box 3)
- N8d-R2 second implementation: experiments/n8d-second/ (kl2.py frozen c0dc7a21; kl2fast.py C port reproduces it on every row);
  R1/R2 equal to L-NEW per instance; switchbestexp R2 to N 30 ~ n^2; box 2b: tau_1 / tie-break settings do not change growth.
- Box 3: experiments/n5-exhaustive/ (exh.py, rnd.py, shrink.py, check_instance.py, README.md): theta-driven re-entries exist
  (thetaA_n6, thetaA_canon_n8, ...); exact small-n tables n <= 4 (+ n 5 subset partial); T28 (b) false; SEG-1O, ELIM-n, H-E hold.
- Box 4: box4.py (CYC' = theta+w changes, NH = non-(h) transitions, phaseprofile.py convention, every phase; reentry.py classes);
  tables n 4 canonical, n 4 all starts subset, n 5 subset partial, random streams; nh_n8 (smallest found: non-(h) throughout a
  4-iteration phase, o on the play cycle, start pair). README "Box 4" section.

### IN FLIGHT
- Nothing (all background runs stopped 17:35Z; partial JSONs copied to experiments/n5-exhaustive/results/; box 4 written up in
  experiments/n5-exhaustive/README.md "Box 4").

### NEEDS / next for a successor (box 5, Lead 17:1xZ)
- Add X (crossing transitions: R changes) and O (transitions touching an OTHER state: (h) fails and Xi != W) per phase to
  box4.measure (a few lines: R via thtrace.Rset per state, O via rows[k][3] and Xi[o] != W[o]) and re-run the small-n tables
  (n 4 canonical ~10 min on 3 cores, n 4 all-starts subset ~35 min).
- Finish the n 5 canonical subset (exh.py / box4.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only; 160 (o, parity)
  slices, ~2-3 min per slice per core with box4's reentry pass); there is no resume: rerun from scratch, or add a --slices option.

### Things only I know
- exh.py's canonical subset (ids in priority order, distinct priorities) is the only symmetry reduction; L-SI's Engine ranks by
  (priority, id), so it is Engine-equivalent up to relabelling, but N5 id tie-breaks could differ on relabelled copies.
- "max_*" excess columns in exh.py start at 0, so 0 means "<= 0"; rnd.py tracks true maxima (negative values are real).
- box4 phases are keyed by (lambda_sigma, lambda_tau, tau(o)) (phaseprofile); exh.py's maxph uses joint lambda without tau(o)
  (phases.py). The two give different phase lengths (n 4 all starts: 4 vs 3).
- reentry.py re-runs N5 itself (n5x.step); box4 calls it only for runs with >= 2 iterations.
- check_instance.py is the gate for any reported instance (n5.run counts, n5b SPEC full state sequence, Oink zlk, verify.py).
- n5b.py has a trace hook (run(..., trace=list)) added 2026-10-24; behaviour unchanged.
- Monitors that grep THETA lines from random streams at n >= 8 flood; filter by n.
- kl2fast.py builds out/lfp.so with gcc on first import; out/ is gitignored.

## Queue (for the successor, after the running cells)
0. sat-hard state (from the 2026-10-14 resume point): CEGAR-only s^V(5,5) k=10 and TARGET n=5 strong k=8 UNSAT; CNFs lost
   with the container; regenerate with `diag.py 5 5 V strong --klo 10` / `diag.py 5 7 V strong --min-letter 2 --klo 8`.
   Next k: w^V(5,5) k=10, s^V(5,5) k=11, TARGET n=5 k=9 (1-2 h per k per core; cube.py on 4 cores). Needs cadical (apt).
1. Report the four n=5 cells with evidence; LRAT for out/w_n4_d6_k8.cnf (w^E(4,6) >= 9; solve ~1000 s, proof large).
2. Remaining (Lead's order): (4,5) V weak/strong, (5,6) V, E cells (4,5)/(4,6)/(5,4) k >= 9 (cube.py for 4 cores).
3. Low: w(2,d) for d >= 14 (E): k=4 UNSAT (CEGAR only) for d=14,16,20,24; row2.py computes the row (slow).

## How to run the bench on a new claim
Wrap the claimed algorithm as a command that reads a PGSolver .pg file (max-parity, owner 0 = Even, priorities any
naturals) and writes a 'paritysol' solution with a positional strategy for every vertex owned by its winner (see
experiments/harness/README.md; avh.py is a worked example, register it in experiments/harness/solvers.py). Then:
(1) `python3 experiments/harness/compare.py DIR --solver NEW='CMD {in} {out}' --stop-first` on a seeded corpus
(`gen.py corpus DIR 10000 SEED --nmax 200`), an rngame corpus (`rngame_corpus.sh`), exhaustive tiny games
(`exhaustive.py`, or `iter_games` in-process for Python code) and experiments/harness/bench/hkp_*.pg; compare.py
reports MISMATCH (regions differ from Zielonka) or BADSTRAT (strategy not closed/winning per verify.py).
(2) every hard family: add the solver to experiments/hard-families/run_all.sh (or `sweep.py FAMILY --gen ... -s NEW`)
for agreement plus runtime growth tables/plots. (3) On the first failure: `experiments/m2/shrink.py` (adapt the
solver import) to a minimal game, save the .pg, push, message the Lead with SHA, game, expected and actual result.

## Open items
- counter_qpt growth class: qpt lifts jump x15 at N = 8 and x31 at N = 16, ~N^3..N^4 in between, timeout at N = 32;
  run N = 29..40 with a long timeout (sweep.py counter_qpt --timeout 600) to see the N = 32 jump.
- PGSolver binary diff: DONE 2026-10-15 (pgsolver-binary-diff.md), all identical.
- counter_dtl is listed in Oink's README (8fbf0a7) but has no source upstream (no src/tools/counter_dtl.cpp, not in
  CMakeLists); not swept.
- avh strategy construction S1/S2 is not always winning (experiments/m2/counterexamples/strat_s2_12v.pg); moot since
  M2 is closed.

## M2 pseudocode
Source: arXiv 2511.03752v1, R. van der Heijden, "Attractors Is All You Need: Parity Games In Polynomial Time"
(submitted 2025-11-04). Opened 2026-10-14 as the LaTeX e-print (sha256 of e-print 4dc6c4b9...ee2e4; main.tex
9840db37...3f8b). Line numbers "tex:N" refer to that main.tex; the paper has no numbered equations. Theorem
numbering follows the paper's counter: Lemma 1 (tex:290), Theorem 2 (tex:322), Lemma 3 (tex:341), Lemma 4 (tex:397),
Theorem 5 (tex:404), Lemma 6 (tex:413), Theorem 7 (tex:421), Theorem 8 (tex:428); Algorithm 1 (tex:370-395).

### Conventions of the paper
- MIN-parity: "Even wins the play iff min{inf(pi)} is even" (Sec. 2, tex:274). TARGET.md is max-parity.
  Implementation maps a max-parity game with priorities 0..P to min-parity by rho'(v) = M - rho(v), M = P rounded up
  to even: order reversed, parity kept, so winning regions and strategies are unchanged. (Mine, not the paper's.)
- player(d) = Even if d even else Odd; par(d) = d mod 2 (tex:301). In A(G,d) the symbol O ("circle") is the player
  of d, O-bar the other (Theorem 2, tex:323: "priority d of player O, A(G,d) is an O-dominion").
- Attr as defined tex:280-286 (standard attractor, computed in the current game G).
- Subgame G \ U (tex:278).

### Pre-routine: self-loops (tex:297, Remark tex:335)
The paper assumes no self-loops and says they "can be removed as a pre-routine [friedmann_solving_2009]"
(doi:10.1007/978-3-642-04761-9_15, NOT opened: awaiting source). Reading used (from PGSolver d3cd624, Friedmann's
code: transformations.ml:15-24 remove_useless_self_cycles_inplace, specialsolve.ml:20-28 find_useful_self_cycles,
univsolve.ml:698-760 their use):
P1. For every v with (v,v) in E, rho(v) of parity NOT the owner's, and |E(v)| > 1: delete edge (v,v).
P2. For p in {Even, Odd}: S_p = {v : (v,v) in E, and (owner(v) = p and par(rho(v)) = p, or E(v) = {v} and par(rho(v)) = p)};
    X_p = p-Attr(G, S_p); W_p += X_p; strategy: v in S_p owned by p plays v->v, attractor strategy on X_p \ S_p;
    G = G \ X_p (Even first, then Odd on the remaining game, recomputing S_Odd there).
    (The "E(v) = {v}, wrong parity" case is my addition: PGSolver leaves such a self-loop in place.)
After P1-P2 no vertex of G has a self-loop (every remaining self-loop vertex was in S_Even or S_Odd or lost its loop).

### Definitions (Sec. 3, tex:301-318), for the current game G and a priority d, O = player(d)
D1. U_d(G) = { v : rho(v) <= d and par(rho(v)) = par(d) }                                     (tex:303)
D2. A*_d(G) = union over k in 0..d with par(k) != par(d) of { v in O-Attr(G, U_{k-1}(G)) : rho(v) = k }   (tex:304)
    (U_{-1} = empty set.)
D3. A'_d(G, A) = O-bar-Attr(G, { v in A \ (A*_d(G) u U_d(G)) : rho(v) < d })                 (tex:309)
D4. U^0 = U_d(G);  A^0 = O-Attr(G, U^0)                                                        (tex:314-315)
    U^{k+1} = U^k \ O-bar-Attr(G, (V \ A^k) u A'_d(G, A^k));  A^{k+1} = O-Attr(G, U^{k+1})     (tex:316-317)
    A(G,d) = intersection over k of A^k                                                         (tex:312)
    Computed by iterating until U^{k+1} = U^k (then every later A^k equals A^k).

### Algorithm 1 (tex:370-395), run on the game left after P1-P2
 1 n = |V|, m = |E|                                         (tex:374)
 2 D = ordered list of priorities (unused afterwards)        (tex:375)
 3 W_E, W_O = {}, {}                                         (tex:376)
 4 while V != {}:                                            (tex:377)
 5   dhat = max priority of G                                (tex:378)
 6   O = Even if dhat even else Odd                          (tex:379; the tex writes "d", read as dhat)
 7   dbar = max priority of O-bar in G                       (tex:380)
 8   compute A(G, dbar)  [an O-bar dominion by Theorem 2]    (tex:382)
 9   W_{O-bar} += A(G, dbar);  G = G \ A(G, dbar)            (tex:383-384)
10   if A(G, dbar) != {}: continue                           (tex:385-387)
11   compute A(G, dhat);  W_O += A(G, dhat);  G = G \ A(G, dhat)   (tex:389-391)
12 return (W_E, W_O)                                         (tex:393)
Implementation guard (mine): if in one iteration both A(G,dbar) and A(G,dhat) are empty and V != {}, stop and report
STUCK (Lemma 4, tex:397-402, says this cannot happen).

### Strategies (not in the paper; my construction, required by D2 change 5)
For a removed set A = A(G,d) = O-Attr(G, U) with U = U^k at the fixpoint:
S1. v in A \ U owned by O: the attractor strategy (a successor in the previous attractor layer).
S2. v in U owned by O: a successor in U if there is one; else a successor in A \ A'_d(G, A) (the case analysis
    in Theorem 2's proof, tex:328-330); else any successor in A (flagged in the log; the proof says it cannot occur).
Pieces are removed as O-attractors, so the remaining game is an O-trap and the per-piece strategies compose.
A failed strategy check therefore does not by itself refute the paper; a region mismatch does.

### Ambiguities (reading chosen; alternatives)
AM1 Parity convention: min-parity as written (tex:274). Alternative: the author meant max-parity (Algorithm 1 starts
    from the MAX priority, which in min-parity is the least significant one). Implementing max-parity instead would be
    a different algorithm; I implement min-parity as written and could add the max-parity variant as a probe.
AM2 Line 6 says "if d is even"; read d = dhat.
AM3 Line 7 when O-bar has no priority in G: reading A(G, dbar) = {} (skip to line 11). Alternative: undefined.
AM4 Self-loop pre-routine: see P1-P2 (cited source not opened; PGSolver's code used; forced wrong-parity self-loop
    vertex handled by me).
AM5 A(G,d) = intersection of the A^k (tex:312): since U^k decreases and Attr is monotone, A^k decreases; computed at
    the fixpoint of U. Alternative readings give the same set.
AM6 All attractors inside D2, D3, D4 are computed in the current G (whole remaining game), not inside A or U.
    Alternative: D3's attractor restricted to A. Chosen: G, as the formulas write "Attr(G, .)".
AM7 D3 uses strict rho(v) < d and excludes A* and U_d (as written).
AM8 Text references "line 12" for continue and "lines 8-10, 14-16" (tex:369, 408), numbering that counts the blank
    \[\] lines; my line numbers above are my own.
AM9 Lemma 3's proof sets D_{dbar} = D cap U_{dtilde} (tex:345), probably a typo for U_{dbreve}; no effect on the algorithm.

## Things only I know
- PGSolver (tcsprojects/pgsolver d3cd624) builds with apt OCaml 4.14 + dune 3.14 after two local edits
  ((lang dune 3.18)->3.14, drop maintenance_intent) in a dune workspace with tcslib 6778419,
  ocaml-sat-solvers 0264291, c-cube/ocaml-minisat aeb7776 (cloned under experiments/hard-families/out/pgsolver,
  gitignored; a fresh session must re-clone). Running the built binaries was refused by the permission classifier
  on 2026-10-14 ("code from external"); on 2026-10-15 (L15 attempt) it ran. Build also needs apt libextlib-ocaml-dev,
  libnum-ocaml-dev. switchall/switchbest: `pgsolver.exe -global policyiter -x "-sa"|"-sb" -dgo -dsd -dlo -dsg -v 3`.
- The ported SI (pgsolver_si.py) runs the bare strategy-improvement loop; PGSolver wraps it in universal_solve
  (preprocessing, SCC decomposition), so counts may differ from PGSolver's own. Details that matter for fidelity:
  TreeSet.choose = min_elt, folds ascending, del_edge is a no-op on deleted nodes, iter_by iterates a snapshot.
- switchbestexp.ml's description string repeats the switch-all text (line 79); its target is switchbest.
- Oink rngame is seeded from std::random_device: not reproducible; keep the files, not the parameters.
- Oink mspm (8fbf0a7) is unsound: logic error at mspm.cpp:486 on 4 rngame games, and on one game a wrong answer
  that Oink's own verifier rejects ("loser can escape"). Instances: experiments/harness/regressions/mspm_*.pg.
  Exclude mspm from any "all solvers agree" claim.
- Oink preprocessing (single-parity, winner-controlled cycles) solves counter_qpt and the PGSolver families
  outright; use the oink-<s>-raw registry entries to make the solver see the game.
- Oink's work counters are solver-specific (iterations, promotions, lifts, major iterations); compare across sizes
  of one solver, never across solvers. Iteration counts are deterministic with -w 1; wall times are noisy.
- py-zlk is slow on exponential families (Python recursion); sweep.py skips a solver after its first timeout.
- Background watchers: `pgrep -f NAME` inside a loop matches its own command line; use a pid file instead. (Bit again
  2026-10-15 20:10Z: an `until ! pgrep -f "sweep.py X"` watcher never ended; wait on a log line instead.)
- gen.py uses its own splitmix64 so games are identical across Python versions; selftest pins the corpus hash.
- sat-hard: graphs.family/family_V/family_S are my own generators (progress-measure trees; every graph brute-force
  checked); counts equal L-STRUCT's maximal families. Families are not reduced to maximal graphs: n=5 V families are
  ~30k-60k graphs, so each CEGAR round's check is slow-ish.
- Unary (thermometer) ranks + CEGAR are the best encoding found; binary ranks ~8x slower, pure lasso CEGAR does not
  converge, clique bounds are always 1 (shared tail -> same limsup parity), annealing / state merging fail.
- Never `pkill -f PATTERN` where PATTERN occurs in the current shell's own command line: it kills the shell (exit 144).
  List pids with `ps -eo pid,args | grep ...` first, then kill by pid.

- N8d (2026-10-23): kl2.py needs about n*d/2 Tarjan runs per pivot (Phi_p for every even p); switchbestexp N = 14 (n = 360)
  takes ~400 s per R2 run, N = 16 ~2x that. The naive-lifting oracle (--check) is exponential in d: use only n <= 16, d <= 6.
- N8d: the R2 draw `random.Random(seed).choice(sorted candidates)` reproduces L-NEW's sequence exactly, so R2 seeds are
  comparable per instance across the two codes.
- famF/G/H/L: the added nodes are isolated Even self-loops with top priorities; pivot counts are constant in k by construction
  (R1 and every R2 seed), so these families test only correctness, not growth. counter_core N and counter_dp 2N give identical
  counts for every rule and seed.

- kl2fast.py: speed came from keeping labels in C buffers across pivots and doing the admissible scan in C; a C LFP alone with
  Python label conversion was only 5x. pypy3 (apt, 7.3.15) gives only 1.7x on kl2.py. The C .so builds into out/ (gitignored) on
  first import; gcc must exist.
- run_families.sh line "echo ... tail -1 $R/$f.kl2.log" prints a tail error with IMPL=kl2fast (cosmetic; exit codes are right).

- Box 3: exh.py's analyse() reruns Engine evaluations per state (Xi_sigma, Xi_tau, W, R, trust set, route lengths); ~0.2 ms per
  trivial game, ~2-3 ms per run with >= 2 iterations. Full n 5 (7e9 games) is out of reach in Python; the canonical subset (ids in
  priority order) is the only symmetry reduction used. Max fields initialised at 0 mean "<= 0" for excess columns.
- Monitors on THETA lines flood when random streams at n >= 8 hit often; filter by n in the grep.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/trolando/oink @ 8fbf0a7 | solver list (README), generators src/tools/*.cpp, solution format src/game.cpp:459 | 2026-10-14 | code, not a paper |
| arXiv 1405.0386v2 (LaTeX e-print, Huth-Kuo-Piterman) | Figs. 4(a), 4(b), 6 tikz source (archiv.tex:815-855, 1164-1194); conventions archiv.tex:225, 342-343 | 2026-10-14 | bench witnesses |
| arXiv 2511.03752v1 (LaTeX e-print) | Sec. 2-3, Algorithm 1, Thm 2, Lemmas 3-4 (see M2 pseudocode) | 2026-10-14 | M2 subject |
| github.com/tcsprojects/pgsolver @ d3cd624 | generators recursiveladder.ml, policyiter/generators/*.ml; paritygame.ml conventions | 2026-10-14 | code, not a paper; papers awaiting source |
| arXiv 2108.13338v5 (LaTeX e-print, sha256 7189eb2f...5c816c; abs page lists v1 2021-08-30 .. v5 2025-06-15) | §2 (prelim.tex: ordered/universal trees, labels, feasibility, violated/tight/loose, Tighten, lift, Prop. 2.6 lattice fixed points); §3 (strategy-iteration.tex: Algorithm 1, admissible arcs, Thm 3.1 correctness, base nodes, Thm 3.3 MinBottleneckCycles); §4 (label-setting.tex: Algorithm 2 Dijkstra, Lemma 4.1, Thm 4.2, Cor. 4.3; §4.1 Algorithm 3 LabelSetting, Thm 4.4, Rem. 4.5) | 2026-10-23 | N8d second implementation; theorem numbers are my count in source order, the .tex uses labels (thm:correctness, thm:dijkstra, cor:dijkstra, thm:label-setting) |
| arXiv 1106.0778 (pdf sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611 = L-NEW's), O. Friedmann, LMCS 7(3:19) 2011 | §2 (Ω injective, l.132 of pdftotext), §3, §4 (I^glo), §5 (1-sink), §8.1 Table 5 / Fig. 7 / Lemma 8.1, §8.2 Fig. 8, §8.3 Table 6 / Fig. 9 / Lemma 8.2, §8.4 Table 7 / Fact 8.1 / start ι_{H_n} / Fig. 10 / Lemma 8.3, §8.5 Theorem 8.4, Fig. 11 | 2026-10-26 | box 16 H_n. Table 7 gate priorities collide with the lane (d2_n = t1 = 8n+3 etc.); Fig. 10/8/9 use 8i-5..8i+2: hn.py mode fig. Text says lane length 6n-3, Table 7 has i <= 6n-2 (= m of §8.1): 6n-2 used |

| github.com/tcsprojects/pgsolver @ d3cd624 | src/lib/generators/policyiter/generators/friedmannsubexp.ml (90 lines), fearnleysubexp.ml (86 lines), stratimprgenerators.ml SymbolicParityGame | 2026-10-29 | code, not a paper; box 21 ports |
## Dead ends
- 2026-10-30 (box 23): "R*_F = O(n) per W-run" (any reading of box 85's R*-POLY as linear) DEAD on L-RED's latew_K20_m32 (sha1
  063d173c…; LATE=1 red/span/mkrw.py 20 32): one W-run, R*_F 640 > n = 538 (rstar.py on n5b = xirise.py; first shown by L-RED R138, l-red 5374e0a5, so mine is an independent reproduction). Exact on 7 sizes: R*_F = K·m,
  |F| = K(m + 3), n = 14K + 8m + 2, so Θ(n²) balanced. Not a kill of R*-POLY.
- 2026-10-30 (box 23, method): hill climbs on R*_F saturate near n (best 42 at n 60), far below the construction; climb fits are not growth laws.
- 2026-10-18 (method note): watcher loops counting 'done' lines never end when a run crashes before printing 'done'; count
  log lines or processes instead (three stale watchers hit their time limits this box, no data affected).
- 2026-10-15 (not a dead end of an idea; a method note): a C5-literal reimplementation cannot reproduce Oink's
  tangle counts: four orders (step-0 std::sort, in-edge order, stored tangle order, Pearce SCC order) change counts.
  Use dtl_py.py --order oink for exact counts; stdsort.py emulates libstdc++ introsort incl. heap fallback.
- 2026-10-14 sat-hard (L-STRUCT task): pairwise-inconsistent-word clique bound (always 1: u.y and v.y share the tail's
  limsup parity); simulated annealing (stuck at 16 violations, (3,6) k=7); pure lasso CEGAR (no convergence at (2,6) k=2);
  binary ranks (~8x slower UNSAT); merging strong separators (fails to recover the known (2,6) weak separator).
- 2026-10-14 (M2 closed BROKEN by the Lead 18:36Z; REFEREE's independent counterexample breaks readings (a)-(d)): arXiv 2511.03752v1 Algorithm 1 as read in
  "M2 pseudocode" is incorrect. Obstruction: Theorem 2 (A(G,d) is a player(d)-dominion) fails; A'_d only removes
  vertices the opponent can force into lower-priority parts, but player(d) (here Odd) can dodge A' on a
  cycle that never returns to U^k, and that cycle can be won by the opponent. Instance: experiments/m2/counterexamples/ce1_4v.pg
  (4 vertices, all Odd's; Even wins all; the algorithm gives all to Odd via A(G,1) = V). Trace in that folder's README.
- 2026-10-29 (box 18): CONJECTURE LIP (T32 E1 (b), all three readings) DEAD. Obstruction: a vertex can switch many times while its jW / jH
  successor is fixed or ⊥. Instance: red/ul/instances/ladderd0_k12_n48 (+ .start), REL segment [0, 13], vertex 14 switches 12 times,
  jW(14) = 1 switches once, jH(14) = ⊥.
- 2026-10-29 (box 18): HAM-MONO (T32 E7; strict, weak, even-only, odd-only) DEAD. Obstruction: path sets move back toward the phase start.
  Instances: gci3_n24 S3 (phase [3, 15], v 8, |PΔP_i| 6 → 5) and lend107_n32 S3 (odd part 5 → 4).
- 2026-10-29 (box 19): CONJECTURE CUT-Φ (T35 §4) DEAD. Obstruction: a REL cut can change no path set at all (cycle appearance or σ̄ change
  with ℓ-only effect). Instance: n5-exhaustive/instances/b4_n5_other_0.pg (n 5, S3), cut 0 → 1.
