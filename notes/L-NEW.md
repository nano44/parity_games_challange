# L-NEW notebook ((c) design lane under D14; Lead reading L35)
Overwrite the top sections; append to "Sources opened" and "Dead ends". Box 1 started 2026-10-18 09:10Z (date -u).

## Box 32 in progress (successor 12, session_01SqmdU7H8WiFZUGTRjZi1C3; GO 2026-10-24 23:50Z)
- DONE (pushed): handover 9cd52937; milestone 4f2e8e34; NO-WAKE FALSE ee763e68; P-N5-U23 fixes 0274bd53 (sha1 870c63a3…; R26 LANDED eb8e22e);
  P-N5-LP 04845d18 (sha1 d2c8121a…, pinned bc42f2c; both referees: all signed except DF FALSE → DF′); P-N5-LP fixes 459660c3 (sha1 af17cce0…);
  P-N5-SO dacf9506 (sha1 deb5ee44…, pinned 1ef02bb, to referees' successors); P-N5-OE db35220e (sha1 adeccd89…, sent for pinning).
- Write-up docs/new/N5-L-box32.md (§0-§6, 4b, 4c). Tools experiments/new/box32 (lcheck.py = LP lemmas; socheck.py = TH/SO/J;
  oddlev.py = Lemma OE; orise.py; dormant.py, rrdorm.py, wgap.py, kwlev.py, wakeinfo.py; climbs rrclimb.py (wakes), lemclimb.py, nwclimb.py,
  mblockclimb.py; out/ is gitignored by experiments/new/box32/.gitignore).
- State (per phase, o-cyclic 𝒞^1O): T = O(m n⁵ (1 + X + K)) (P-N5-OE Corollary OX, unrefereed). Only X (≡ Z) and K (wakes) remain.
  K: 0 in library; climbs (~7·10⁵ candidates) max 2 per run; every wake is U3, length-only regime (c_w top), W(y) unchanged (W-tie switch).
- Expect: §C items on P-N5-LP; referee items on P-N5-SO / P-N5-OE → NEW fixes files, never edit packets.
- Pitfalls hit: `pgrep -f X` in a Monitor matches the waiter (use ps + awk on argv); reach_o omits o; Lead relays queue unseen while I work
  (ReadNotifications after each push); my P-N5-LP §0 overstated VJ00 Lemma 5.8 2 ⇒ 3 (false at cycle nodes: R15 side finding) — check
  R15's side findings before citing VJ00 directions.

## Resume point (overwritten at handover, LANE-RESTART step 1; successor 11 PARKED after box 31, 2026-10-24 23:21Z by date -u)
Successor 11 (Opus 5.5, D15/D18), session_01JjUBLJnxF38h9cjDCyZeZf. Box 31 (Oct 24, 19:53Z-23:21Z). Nothing running at park. Context ~400k;
parked early at the Lead's request ("freeze P-N5-U23, then park").

### DONE (all pushed with scripts/push.sh)
- Handover check a4db2c08 (5/5).
- P-N5-NH fixes: docs/new/P-N5-NH-fixes-box30.md (b4fc3a4f). Landed as R22.
- Box 31 (a): docs/new/N5-U1T-box31.md.
  - U1-T FALSE (L-RED's u1t_cex_n32; mine u1t_cex2_n32).
  - Packet docs/new/P-N5-U1-box31.md (d8d6e1d0, sha1 eb90788d…), LANDED as RESULTS R24 with both signatures: Lemma R, TB, CASC,
    Theorem U1, Lemma WC.
  - Fixes: docs/new/P-N5-U1-fixes-box31.md. REFEREE in §1-§5, REFEREE-2 in §7. It includes the EQ-fallback claim §7.5, PROVED (L-NEW)
    and unrefereed.
- Box 31 (b): docs/new/N5-U23-box31.md.
  - Packet docs/new/P-N5-U23-box31.md, frozen at the park commit: CASC-U2 and CASC-U3 with their corollaries. NEVER edit it; repairs go
    in a new fixes file.
  - §5 of the doc: every (E) and (K_W) transition seen is TAME in L-SI's sense, so they cannot be charged to J.

### IN FLIGHT (others)
- P-N5-U23: waiting for the Lead to pin it and route it to the referees.
- L-COMP box 7 tabulates (E) at small n from N5-U23-box31.md's definitions.
- L-SI: R25 (Theorem FB) at CHECKER. L-RED: (X).

### NEEDS / next
- Successor 12, first: answer the referees on P-N5-U23 in docs/new/P-N5-U23-fixes-box31.md (a new file).
- Then the open cores, as the Lead routes:
  - (E): events in U3 (kind crossings, c_w's own switches);
  - (K_W): W-changes on R outside route form.
  - Idea (READING, N5-U23 §5): a coarse freeze at L-SI's gate level M (constant on tame blocks, non-increasing along tame runs)
    instead of at c_w.
- Also open: NFB-O; (X).

## Things only I know (successor 11)
- The tie-break is the lever. S4a's choice among W-optimal arena edges is NOT arbitrary: odd c_w → min index (longest-path
  recursion, first strict max), even c_w → lexmin root-first index sequence (BFS over preds in index order). The current edge is
  always optimal when W stands still, so the choice can only move "down" (Lemma TB). Combined with the arena rule (only
  honest-improving edges join) and route-additivity, a Howard-style layer induction gives CASC.
- CASC needs ONE dependence order for both frames. Route form gives it (both values are π ⊕ terminal at o). Outside route form the
  W root is c_w and the honest root is o or C_Ξ: the conflict sits exactly on the frame cycles through o (CASC-C).
- Under ¬H2, w = (c_w, ∅, d): o is on its own W-cycle, so nothing before c_w beats it. That one line kills W-CYC (Lemma WC).
- Tools, experiments/new/box31: tbcheck.py (TB on N5 runs; layered generator), tbarena.py (TB on random arenas: the fast test),
  casccheck.py, runinfo.py (W-flat runs per piece), p3long.py (P3′ pieces), nrcheck.py (U2/U3, CASC-C, W-CYC), cascade.py (abstract
  model), climbs cascclimb.py (modes thw / flat), nrclimb.py. out/ holds climb bests (not gitignored at this depth: copy finals to
  instances/).
- U2/U3 (box 31 b): in U2 honest values are route functions with constant terminals at the first of {c_θ, o}, so CASC holds there
  unchanged. In U3 split R by kind (c_w on the route or not); only kind crossings and c_w's own DFS choice break the layer
  induction. Tools: u23check.py, u23climb.py (modes U2 / U3), tamecheck.py (L-SI tameness; reads experiments/si/coarse/mono.py).
  U2 W-flat switches have never been seen.
- The lane helper reach_o (box28/fbre.py) returns R minus o: count |R| with o in every statement.
- Pitfalls: my first message stamp (20:22Z) was 3 min ahead of date -u (20:19Z): stamp only from the command output, not a guess.
  Random o-cyclic runs almost never reach W-flat runs or U2/U3; seed climbs from u1_n32 / b5_os_n14.

## Things only I know (successor 10)
- The structure that carries everything:
  - Ξ ⊴ W always (XW).
  - Off R, Ξ = W with no (h) (Lemma G (a)), so all F-dynamics is R17 on 𝓕 per crossing-free interval (F1°), whatever the state type.
  - H1 ⟺ λ_Ξ(o) ∈ F and H2 ⟺ τ(o) ∈ F. Both are constant on crossing-free intervals (TC), so the "type" of a whole interval is
    nearly fixed.
- O-counts decompose exactly: OTHER-touching = crossings + F-changes + R-only. Every big O seen (26 at n 16, O/n = 2.04 on b5_os) is
  mostly crossings + F-changes. R-only ≤ |R| in all data.
- "Route form" (H1 or λ_Ξ(o) = o; H2 or λ_W(o) = o): values on R are π ⊕ terminal in that frame. In general each frame is "path to
  its cycle node in the graph with o fixed to its exit" (a two-target route game). P3′ = the honest target higher.
- U1 mechanism (wf0_cex_n16, iterations 16 and 20): Engine.evaluate's tie-break (first max in DFS / BFS, experiments/si/si.py
  evaluate) is not "keep current". So S4a moves an R-vertex to a W-tied successor with a better V_mid set. The Lead confirmed this is
  N5 as specified; a keep-on-ties variant would be a different algorithm (do not adopt).
- Tools, experiments/new/box28: nhprof, fbre, xcount, eqcheck, fbclimb (FIT=p/v), xclimb, wclimb. experiments/new/box29: otherx,
  rsplit, ivsplit (per-interval split), tccheck, oblock, dstat, throttle, odep, p3check, rfcheck, wflat, u1vertex, and climbs opclimb,
  orclimb, u1climb, nfbclimb. Seed climbs from named instances: random C^1O almost never gives throttled or route-form pieces.
- Pitfalls:
  - The container clock (date -u) runs slowly. Stamp only from date -u.
  - pkill -f kills my own shell: kill by pid from ps.
  - push.sh takes several minutes while climbs load the CPU. Do not commit while it is running (verify reads the working tree).
  - Check "freeze" indices with the right bound: a route path has ≤ |R| edges (box 29 off-by-one).

## Things only I know (successor 9)
- Box 26/27 picture (READING; assumes (h)). Inside a joint λ-phase with τ fixed:
  - UNTHROTTLED states (θ = w) are pure one-player G_τ (Lemma UT: ≤ n − 1 value changes per maximal unthrottled run, even as θ = w
    moves).
  - THROTTLED (θ ◁ w) (θ, w)-stretches are O(n³) via C / FBL / FBF / XA / CR / PIECE.
  - So everything rests on how often θ or w changes, plus the non-(h) states.
- The two-frame band (box 26 §7.3): F→R needs the honest test, R→F needs the W test, and in between a vertex keeps its side.
  "Withheld" and "trust" are its two faces. Reweighting (Johnson / T29 Lemma B) cannot remove it. Coarsening above u* does.
- (NH) start points:
  - All box-25 W-drop instances at fallbacks off (h) have τ(o) closing a cycle at o (wdrop_cyc n 4, wd16_s2).
  - In every long phase (fts_best16, tp32, rt48, ph64, sc32, elim24_p52), non-(h) transitions = 0 (phaseprofile.py). So (NH) may be
    a boundary effect at phase starts.
  - A first check: count non-(h) states per phase across climbs.
- (CYC') start points:
  - sc32.pg (n 32) has θ changing at every one of 43 transitions in one phase, with no w-change.
  - Lemma UD: u* only descends when θ changes AT u*. In sc32, check how many θ-changes are at u* versus below it. That is (CYC-u*).
  - Box 27 §8c sketches a recursion below u*: after the coarse freeze every vertex is one-sided.
- Tools (experiments/new/box25/; all import common.py; random generator rand_c1o):
  - reentry.py (ROUTE / WRISE / THETA classes), routemono.py, piececheck.py, crossings.py (throttled by default; --all);
  - coarsecheck.py (C1 / C2 / C3, --withfb), fbedges.py, fbfcheck.py, phaseprofile.py;
  - climbs: xingclimb.py (throttled), fbreclimb.py, stretchclimb.py, routeclimb.py, thetareclimb.py, shrink_theta.py.
- Pitfalls:
  - `cd dir && nohup cmd &` backgrounds the cd too, so later relative paths break. cd first, then nohup on its own line.
  - pkill -f kills my own shell (hit again in box 27). Kill by `ps -eo pid,args | awk '$3=="script"'`.
  - Measure THROTTLED quantities explicitly. Unthrottled regimes are already bounded and inflate the counts (box 26's mistake).
  - Header timestamps only from date -u.
- From box 25: the o-cyclic core (box 25 §5) holds. Inside a (τ, λ)-phase under (h), θ = o ⊕ min over exits ∉ R of their o-free
  value. W-drops happen off (h) and at throttled (h)-fallbacks (fbh_drop9). A fallback's refused edge can be a W-tie (fbh_thr).
- TRAPS THAT BIT ME:
  - (box 25) I announced (WF) as new, although box 22 had it. Check: grep docs/new/ and this notebook before calling anything new.
  - (box 26) My crossing climbs measured the unthrottled regime. Check: restrict to θ ◁ w.

## Things only I know (successor 8)
- o-cyclic state, precisely:
  - Lemma 1 of P-N5-1OA (X has G[X]-optimal values at pure transitions) holds on ALL of 𝒞^1O. REFEREE-2 notes the same,
    including fts_best16 (there X = ∅).
  - Lemma 2 (θ = w at pure steps) is the break. It fails first at cyc4 (n 4; box22/instances/cyc4.pg, sha1 bff7a8c2…).
  - Lemma 2' (PROVED under (H): the (σ, τ)-play from o does not return to o): a throttle surviving a pure step needs an
    INCOMPLETE exit a = σ̄(o) ∈ Y, with Ξ(a) ◁ U_τ(a). DATA: 0 exceptions in 196 states.
  - Mechanism (the self-throttling exit):
    - a's best route against τ runs through o, while a currently avoids R (24 of 24 throttled states of fts_best16);
    - θ rises only through o-free exit improvements;
    - all 5 exits of fts_best16 are incomplete at states 2-25 and complete together at state 26.
  - Ring reading (L-RED R58 §10): fts_best16's exits lie on one σ-path back to o, and σ̄(o) walks along it. A super-linear θ-count
    would need nested rings, which nobody has built. θ-change climbs stay below n (13 at n 16, 16 at n 24).
  - cycclimb (pure run in one λ-phase − (n−1)) at n 8 / 10 / 12 / 14: best −1 / 0 / −2 / −5. The smallest pure block beating
    R17's per-phase bound is fts_best16 (n 16).
- Tools:
  - box21/n5x.py: trace equal to n5.run. box21/climb_fix.py: modes tstar, tstarph, bestph, oneodd, seg1o, laps1o, segfz, tany.
  - box22/statcheck.py: P-N5-1OA lemmas L1-L3. It now has a main-guard (d68ded65); its CLI is unchanged from the referees' pin.
  - box22/shrinkP.py: violation() for I1-I4, with env HREQ / NOFB.
  - box22/incomplete.py: Lemma 2'.
  - box22/climbPure.py: the pure-transition climb.
  - n11/n5ht.py: N5-HT, dead.
- Pitfalls:
  - pkill -f matches my own shell. Kill by argv fields.
  - Scripts imported by others need a __main__ guard.
  - Count stretches with λ held constant.
  - In 𝒞^1O checks, R must follow forced Odd vertices.
  - check_sol2 needs Oink built (scripts/setup_oink.sh).
- Process: Lead rulings this run were the stop rules (03:20Z, 04:45Z, 05:00Z), "freeze before any run" (box 23), and the frozen
  packet rule (corrections only in new dated sections).

## Sources opened
- (succ. 12, box 32) VJ00 = Jurdziński & Vöge, BRICS RS-00-48 (www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, sha256 485a12de432a2a8c…, opened
  2026-10-25 00:35Z, pdftotext): p. 14-15 σ̄ definition and Prog (P1)-(P3); p. 15 Lemma 5.2; p. 16 (11); §4.4 p. 11 improvement (2) and Switch_I;
  p. 19-21 Lemma 5.8 (2 ⇒ 3 ⇒ 1 proved via Lemma 5.7, 5.2; 1 ⇒ 2 via Lemma 5.9 'proved similarly'). Used in P-N5-LP (DF uses 2 ⇒ 3 ⇒ 1 only).
- (succ. 7, box 18) arXiv 1405.0945 v1 (4c6956dc2f1db3ee): §1 l.95-119 (SA level n exact). arXiv 1506.04184 Bodirsky-Mamino
  (e0e0e34de549a4d8): abstract, §1 l.103-104, Thm 5.1 (NP ∩ co-NP; no bounded-width statement). C. Fritz PhD thesis Kiel 2006
  (macau.uni-kiel.de d1644.pdf, fa1253460e9058c3): ch. 3 intro, §3.5 remark (simplify-then-solve slower than lifting).
- (succ. 6, box 17) arXiv 2108.13338v5 e-print (sha256 7189eb2f…, LaTeX): §1 intro l.13 (determinacy, citing Martin 75 / EJ91, not opened), §2 all
  (Def 2.1-2.2, Thm 2.3, Lemma 2.4, Prop 2.5, operators), §3 Algorithm 1, Thm 3.1 + proof, Def 3.3, Thm 3.4; §4 Alg 2-3, Lemma 4.2, Thm 4.3,
  Cor 4.4, Thm 4.5, Rem 4.6; lmcs.cls l.685-699 (one counter per section). Kelner-Spielman STOC 2006 author PDF (sha256 3b5f68fe88c9cd46…):
  abstract, §1-2, Thm 3.2, Thm 6.3.
- (succ. 5, box 13) arXiv 2108.13338 Koh-Loho (21ee0e4336252f7e): §1 p.2-3, Thm 2.3, 3.1, 4.5. Schewe MFCS 2009 author PDF (d27bbc79ab6b162b):
  §1 p.2, Cor. 6-8. arXiv 1305.3944 Avis-Friedmann (d1fafb8b5d0b822c): abstract, Thm 4. arXiv 1210.2459 CGR (02fca6a45515f2ec): abstract.
  arXiv 2509.16075 Maat (69706649fed1fac9): related work p.2. arXiv 1405.0945 (4c6956dc2f1db3ee): §1 p.2. arXiv 1605.03019 (cb6029755abff8a9): §1.
- (succ. 5) arXiv 2007.06558 v5 Cen et al. (sha256 23fddbc3f493d02e): Thm 1. arXiv 2105.15186 v3 Cen-Wei (a2da0da3164be410): Thm 3.
- (succ. 5, 2026-10-22) arXiv 1304.1888 v2 HIJ (sha256 01e4cde9b47f90cb): §2.3 Def. 16, Thm 18; §3 Thm 19, Thm 21 (family G_n); §4 Thm 22-25;
  §1.1. arXiv 1708.01544 ABGJ (9608058cb6fa98a3): Thm A/B, Cor. 31, Remark 32, p.2-3 (bitlength of t exponential). de Klerk-Nagy,
  optimization-online 2010/02/2555 (726c92b99e80dae6): abstract, Def. 1. arXiv 1106.0778 Friedmann (46c96f44775aa2b0): §9 beta_G, Thm 9.3.
  arXiv 1008.0530 v1 HMZ (f53a6b5127d95078): Thm 6.5. arXiv 0909.5653 v1 FJS (9fbd86643615f000): B13 context only.
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

- (succ. 2, box 7) VJ00 RS-00-48 §7 p. 26-27 re-read: Prop. 7.4 (O(n³) improvement steps, one-player parity games; NO proof), Prop. 7.5,
  Prop. 7.6, "at most O(n²) substantial steps". Asadi-Chatterjee-de Raaij arXiv 2506.12254 (UAI 2025), abstract page opened
  2026-10-18 between 23:42Z and 23:47Z (date -u bounds): Howard on deterministic mean-payoff MDPs Ω̃(I) lower bound; "best known upper bound is exponential".
  Hansen-Zwick ISAAC 2010 and Hansen-Kaplan-Zwick SODA 2014: records only (WebSearch), NOT opened.

- (succ. 3, box 8) Fearnley arXiv 1705.02313 v1 (sha256 a49296a2…), §4 "One-player strategy improvement", Lemma 3: O(|V||E|) for the
  ALL-SWITCHES (greedy) one-player rule only, citing Cochet-Terrasson-Gaubert [3]; it does not cover adaptive subsets.
- (succ. 3, box 8) Zadeh, "What is the worst case behavior of the simplex algorithm?", CRM Proc. Lecture Notes (2008), §1 p. 1:
  "An example due to Edmonds for shortest path computations is also known [16]". Edmonds' example itself NOT opened.
- (succ. 3, box 8) REFEREE R-N5K9 (claude/referee 160db1d) §(2)-(3): (P*), (P_strict), switch-all insufficient.
- (succ. 4, box 10) VJ00 BRICS RS-00-48 re-opened 2026-10-21 23:31Z (pdf sha256 485a12de432a2a8c…, pdftotext): §5.1 pp. 12-14 (shortest-path
  characterisation of Π_σ, equations (6)-(10)), §5.2 Prop. 5.1 + Lemma 5.2 => Ω_σ = Θ_{σσ̄} and σ̄ is a best counter-strategy (eq. (11), p. 16: the
  (F1) fact of N5-phase-bound-box10.md, used on the dual game), §5.4 Improve, Lemma 5.7 (not used), Lemma 5.8 (not used), §3 postulates P1-P2,
  I1-I2 (not used), Prop. 7.4 p. 36 (statement only, no proof).
## Dead ends
- (succ. 12, box 32) Coarse freeze at R25's gate level M for (E) / (K_W): VACUOUS. M_k = ∞ at 52 of 69 U2/U3 KW transitions and at both
  U3 events (220-file 𝒞^1O library, mblock.py). (KW-M) "≤ |R| KW per M-block" FALSE: experiments/new/box32/instances/kwm_cex_n24.pg
  (sha1 c2723e08…; 15 KW at |R| 3).
- (succ. 12, box 32) (NO-WAKE) "no used-level rise without fallback, crossing or σ̄(o)": FALSE. Obstruction: W-blind band; with c_w the
  top-rank vertex W compares lengths only, and an S4a step shortens z's route to a W-tie, the tie-break takes z while Ξ sees level 30.
  Instance experiments/new/box32/instances/nowake_cex_n32.pg (sha1 3a56e3fb…, U3, transition 1: y 11, 22 → 9, level 30 > L_0 = 26).
- (succ. 11, box 31) CONJECTURE (U1-T), "after the κ_w-freeze each R-vertex has ≤ 2 Ξ-changes per W-length value": FALSE.
  - Instance: experiments/new/box31/instances/u1t_cex2_n32.pg (n 32, sha1 6162a26f…, n5.py 9 it / 1 fb, Oink zlk OK, strategies
    verified). U1 piece 0..5 is one W-flat run; vertex 23 (level 9) switches at all 5 steps.
  - Obstruction: the BFS tie-break (even c_w) lets lower-level improvements re-open tied honest-improving edges each step. Bounded
    by CASC (≤ ℓ − 1 per run), so not superpolynomial.
- (succ. 10, box 29) CONJECTURE (WF0), "no S4a step is W-flat and honest-strict": FALSE, wf0_cex_n16.pg (n 16, sha1 1de2ff5b…, Oink
  verified). It is N5 as specified (S1 tie-breaks; the Lead confirms the spec is faithful).
- (succ. 10, box 28) CONJECTURE (FBRE-F), "in a (w, u*)-run, no vertex evicted by a fallback after the coarse freeze re-enters R":
  FALSE.
  - Instance: experiments/new/box28/instances/fbref_n48.pg (n 48, sha1 414231a27ba3…, Oink zlk OK, strategies verified).
  - 10 post-freeze evictees (run index 48 ≥ 47) re-enter at index 54, after a θ-change at 53.
  - Obstruction: an eviction decided below u* is undone by a θ-change below u*.
  - Lemma C, CR and FB-W hold on that run.
- (succ. 8, box 23) N11 = N5-HT (honest override at trust conflicts), frozen at e003f7e6: DEAD on B8.
  - switchbestexp needs exactly 20·2^N − 19 iterations (N = 2..8), the same as Even switch-all.
  - switchallexp needs 10·2^N − 10 (N = 2..6), then 1243 / 2486. All verified.
  - Obstruction: the conflict set is large, so the override replays switch-all.
  - Data: experiments/new/n11/results/.
- (succ. 8, box 21) Route "R17's Lemma P / Theorem PH for N5 against a frozen opponent" (Lemma PT): dead.
  - Obstruction: H1 is false. Edges improving in G_τ* are withheld by the honest gate while their head is exploitable.
  - Instances: experiments/new/box21/instances/h1_hand.pg (n 9), fts_ph16.pg (sha1 55a21ee5…; 22 > 15 in one λ-phase),
    fts_best16.pg (sha1 5534245f…; canonical, 27 > 15).
- (succ. 8, box 21) Route "bound N5 via (R-a) ∧ (R-b) incompatible" (R57 O4): insufficient by itself.
  - Obstruction: Theorem B. (FO) is also needed, and fts_best16 has C_τ = 0 with a long phase.
- (succ. 7, box 19) N10a ACYC + ESC1 (N10-screen.md §1): 15 gaps in 800 random two-player queries (results/rand300.txt); one-player exact.
- (succ. 7, box 19) N10b ACYC + ESC1 + ESC-tau (§2): gap on experiments/new/esc/instances/esc_gap_r1794_Q1.pg (n = 8, sha1
  ab859e3f4acf4ca223bc7af905010d59db758d66; Even wins only vertex 5); no cut ever violated (cuts = 0).
- (succ. 7, box 19) N10c conditioning on N10b (§3): STUCK on the yes-instance instances/cond_stuck_r1569_YE.pg (n = 14, sha1
  c7715537ff454341b3309ea058796c1f759c1ba6) and cond_stuck_symsi3_YE.pg (counter_symsi N = 3 restricted to W_E, n = 32, sha1
  4483eb7c813989cb79edf76c6e604367d39db75a). Obstruction: an N10b gap on a restriction (r1569: v 7 -> 10 accepted, lost everywhere).
- (succ. 7, box 18) N9a SA+_k of ACYC (docs/new/N9-screen.md §1): levels 1, 2 wrong ("Even wins all") on one-player all-odd
  circ(4,1,2), circ(7,1,2) (experiments/new/sa/instances/circ12_n7.pg sha1 4a1973a88a1311966ef5d2f5382221aef3d09c3e); k* grows
  (1,2,2,2,3,3,3 at n 3..9). Obstruction: functional-graph acyclicity (every sigma closes a cycle) needs high-degree refutations.
- (succ. 7, box 18) N9b certified LP peeling (§2): STUCK at round 1 on peel_r1147.pg (n = 5, sha1
  68a8c41b926e2fd324b196c99c4c61ea6d2a91ed; Odd wins all): argmax rounding of the level-1 REGION optimum wins nowhere; also
  r26 (n 6) where the LP value is exact (6.0) yet no rounded strategy wins: the optimum is a mixture.
- (succ. 6, box 17) PROOF ROUTES for R2's expected pivots (not algorithm dead ends; N8d-R2 stays alive), docs/new/N8d-proofs.md §3:
  rank-gap potential (best candidate removes 6.8e-16 of the gap at switchallexp N=4 dual seed 1); Lemma M (lock-in prefixes) FALSE at
  switchallexp N=2 (sha1 ca6e0b7d4745…) dual seed 1 state 1 (9 candidates, none raises M); "switches about once" false off G_zeta (max 19 at
  switchallexp N=10, 27-28 at switchbestexp N=6-8); Kelner-Spielman / Random-Edge: no polytope, no cube walk.
- N8a (Koh-Loho strategy iteration with tree labels, arXiv 2108.13338, PERFECT (n, d/2)-universal tree; pivot rules switch-all and global),
  DEAD END 2026-10-23 (box 14; docs/new/N8a-kohloho.md §6). Passed the hard bench and 10,000 random games (all verified); killed by family
  L_k = 15-node crawl core + k isolated Even self-loops of new high even priorities: pivots 3·n^{k+1} (global), 4·n^{k+1} (switch-all),
  n = 15 + k; instances experiments/new/instances/n8a/levels_2.pg (sha1 3c0092c4c3b5163675b483d4235fb947a17cb130, 14,740 / 19,652 pivots)
  and levels_3.pg (sha1 9ce17076951c96e3cfac2e0703a47253d81bbb6b, 314,929 / 419,904), Oink zlk + verify.py OK. Obstruction: Tighten at an
  odd priority = prefix successor with carries; recurring strategies (Koh-Loho §3) turn each Odd toggle into +1 on an L-digit base-n counter.
- N7 (entropic temperature homotopy: soft Bellman operator at gamma = beta_G, Newton path following in tau), DEAD END 2026-10-22 (box 12;
  docs/new/N7-entropic.md). Proof route dead at the screen: known entropy-regularised rates are poly(1/(1-gamma), 1/tau) (Cen et al.
  2007.06558 Thm 1; Cen-Wei 2105.15186 Thm 3), both exponential for parity; HMZ principle. Bench: stalls on counter_ortl-3 (sha1 c8bc3499...)
  at tau ~ 2.8e-7 and on tc+ N = 2; start-phase failures on tc 4, counter_symsi 1-2, counter_rob 2. All produced answers correct.
  SCREENING PRINCIPLE (N6, N7): any method on the parity -> discounted reduction analysed polynomially in 1/(1-gamma) is no better than SI
  (HMZ 1008.0530 Thm 6.5); require a gamma-free argument before benching such a candidate.
- N6 (IPM on the Jurdzinski-Savani P-matrix LCP of the parity-induced discounted game), DEAD END 2026-10-22 (box 12, successor 5;
  docs/new/N6-ipm.md). Proof route dead at the screen: HIJ arXiv 1304.1888 Thm 19/21 kappa = Theta(n/(1-gamma)^2) (cost-independent,
  extremal arena G_n), parity needs 1/(1-gamma) = n^Theta(d) (Friedmann 1106.0778 sec. 9 beta_G), and HMZ 1008.0530 Thm 6.5 makes SI
  polynomial whenever the kappa bound is polynomial. Gauntlet step 2 failed: the implemented path-following IPMs give no answer on
  counter_ortl N = 3 (n = 16; experiments/new/instances/n6/counter_ortl-3.pg sha1 c8bc349942b32305edee56ba8fb7d6504ed86622), tc N = 4,
  tc+ N = 2, counter_symsi, counter_rob, counter_core N = 4 (central) and every random game with n >= 23. Obstruction: the iterate keeps
  every product w_i z_i within 50% (or 1%) of mu yet leaves the path in coordinate space (state 7: z_7 ~ 0.05 vs 2.5e5 on the path);
  Newton direction arb-certified, M certified P (262,143 minors), stall mu independent of precision, neighbourhood and step factor.
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

- (succ. 3, box 8) K9's route through a policy-free one-player premise ((P*), (P_strict), VJ00 Prop. 7.4 "every policy" reading),
  and box 7's K8 constant-case closure. Obstruction: CDAG_n has 2^n - n - 1 Ω-strict single VJ00 improvements (one-player, all ⊕).
  Instance: experiments/new/instances/cdag/cdag_N12.pg (sha1 41f780ede48ae00d4e4f15251abf2583f9094aa0), chain 4083 by cdag.py.
- (succ. 9, box 25) Three candidate lemmas for o-cyclic 𝒞^1O, all FALSE (instances verified with Oink zlk and strategy check).
  (a) "While only the above part A = V \ (X ∪ Reach(o)) moves, θ = w": zfrozen_thr.pg (n 13, sha1 93c6030c54d5…, random start).
  (b) (WF) "Even fallbacks with τ fixed are W-flat": first refuted in box 22 §3 (i1h_fts_best16, n 11). Smaller instances here:
      wdrop_cyc.pg (n 4, sha1 d2684b7b752d…, random start), wdrop_canon.pg (n 8, sha1 a5007dfe1ac7…, canonical).
  (c) (WF) under hypothesis (h): i1h_fts_best16 already; smaller: fbh_drop9.pg (n 9, sha1 f25c999053aa…, throttled state).
  Also dead as a potential: the count of complete vertices (Ξ = U_τ) on fts_best16 is constant for 23 transitions.
  Obstruction for all: trust routing (docs/new/N5-1Ocyc-box25.md §5).
## Things only I know (earlier successors)
- (succ. 8) Pitfalls in box 21:
  - `pkill -f "climb_fix.py ..."` killed my own shell (exit 144). Kill by `ps -eo pid,args | awk '$2=="python3" && $3==...'`.
  - Stretch counts on 𝒞^1O must hold the joint λ-map constant too: seg1o_20 first showed a 21-step "(θ, w, τ)-stretch" that
    spanned 6 λ/w changes.
- (succ. 7) The pkill self-kill trap bit AGAIN (box 18, exit 144): `pkill -f "twoout.py circ 9 9"` matched my own bash -c line.
  Use `ps -eo pid,args | awk '$2=="python3" && $4=="twoout.py"'` then kill the PID.
- (succ. 7) Plain SA does not multiply the choice equality by continuous variables: (1 - s_a) f != s_b f as monomials. Pruning
  multipliers by that identity WEAKENED the LP (K_3 at k = 1 turned feasible) until SA+ added sum_u q_{A+vu,x} = q_{A,x}.
- (succ. 7) peel.py bug found and fixed before any result: a dict literal {r_u: 1, r_v: -1} with u = v (Odd self-loop) keeps only
  -1, giving r_v <= 0. Any LP builder keyed by dicts needs the u != v guard; sanity = LP value >= |W| on every game.
- (succ. 7) Rotation-orbit reduction (sa_feasible group=) cut circ(8) k = 3 from 1,541 s to 1 s with identical k*; it is exact
  because the LP is convex and invariant (orbit-average of a feasible point is feasible).
- (succ. 6) kl.py compresses priorities (Game.__init__ l.25-32); L-COMP's kl2.py uses p+2. Do not tell anyone "both use p+2". Counts agree on all
  data so far; a difference needs a Tighten carry out of a digit n-1 (N8d-single.md §0b).
- (succ. 6) The container again started on a stale local branch (6b3dcd53, 349 behind origin/claude/l-new): fetch + compare before work.
- (succ. 5, traps hit in boxes 12-16; read these first)
  - Notifications: read ReadNotifications at EVERY milestone push. In box 14, six Lead messages sat unread for 1h14m; I kept climbing after
    the Lead had handed climbs to L-RED (process slip, recorded in N8a §7).
  - Self-kill: `awk '/bench.sh/'` or `pkill -f <name>` matches your own bash -c line (exit 144, bit again). Match argv fields:
    `ps -eo pid,args | awk '$2=="python3" && $3 ~ /kl\.py$/'`. Background subshells relaunch the next job: kill the parent too.
  - `cmd1 && (cmd2 &)` in a for loop: `for s in 1 2 3; do L=$(...); echo ... >> f & done` runs the $(...) SEQUENTIALLY; only the echo is
    backgrounded. Wrap the whole body in ( ... ) &.
  - bench.sh re-reads kl.py / n6.py per instance: never edit the solver while a bench runs (N6 mixed code versions once).
  - Shared output paths race between parallel lanes (two modes wrote the same .sol; fixed by per-mode names).
  - `rm -rf $VAR/$X` is blocked by the safety check; use fresh directories or "${VAR:?}"/"${X:?}".
  - Foreground `sleep N; cmd` is blocked: use an until-loop with run_in_background, or a blocking until-loop under 600 s.
  - Waiter shells hit their background time limit and are reported as "killed": harmless if they only watched files.
  - IPM work (N6): a "jam" is first a step-rule bug (Armijo on max-norm proximity, infeasible/big-M starts, log-coordinate Newton all
    jammed); certify the Newton direction (arb ball) and the matrix property before blaming kappa.
  - Koh-Loho: the hard bench is NOT adversarial for tree labels; climbs found the crawl within an hour (Tighten's prefix successor +
    recurring strategies = a base-n counter per tree level; padding with isolated vertices widens the perfect tree, extra high
    priorities add levels).
  - `date -u` was reliable; my sense of elapsed time was not (it ran far ahead of the clock).
  - The Lead's trunk SHA in a brief may be newer than your fetch (612686b case): re-fetch before saying it does not exist.
- (succ. 5) Kill processes by matching argv fields (`ps -eo pid,args | awk '$3 ~ /bench\.sh$/'`), never by a pattern that also appears in
  your own bash -c line: `awk '/bench.sh/'` killed my own shell (exit 144) again on 2026-10-22. Background subshells re-launch the next
  job: kill the parent subshell too.
- (succ. 5) bench.sh re-reads n6.py per instance: do not edit n6.py while a bench runs; two modes sharing one .sol path raced (fixed).
- (succ. 5) For IPM work: a "jam" is first a step-rule bug (Armijo on max-norm proximity, infeasible starts, big-M all jammed); only after
  certifying the Newton direction (arb ball) and the P-property did the counter_ortl-3 stall count as the method's.
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
- (succ. 3) The pgrep waiter trap bit AGAIN (01:03Z): `until ! pgrep -f "n5_adv_ch.py 96"` matched its own bash -c line and never ended.
  Wait on a PID (`wait`/`kill -0 PID`), or check the log's final "best" line.
- (succ. 3) Exhaustive longest-chain DP over all strategies (dagchain.cpp) found CDAG at n = 5..7 in minutes; random-game sampling
  (box 7's 21 at n ≤ 9) and even REFEREE-2's climb (183 at n = 10) understated the truth (1013 at n = 10). Anneal the GAME, not
  only the start.
- (succ. 3) Seeded climbs (start from a hand-built family) beat random climbs: random one-player climbs never exceeded n, while
  seeded ones refuted SB1 within minutes (11 at n = 10). Seed from structure whenever a "≤ f(n)" conjecture rests on climbs.
- (succ. 3) Lemma NR (σ and τ never return; R15 (c)+(d)) kills every N5-following argument that needs a reply to come back.
- (succ. 3) A worker restart can kill push.sh mid-run (exit 137): check `git rev-parse HEAD origin/claude/l-new` and re-run push.sh.
