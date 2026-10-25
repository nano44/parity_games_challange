# R71: post-freeze regimes of P-FREEZE / HAT-FREEZE / NHN are unreached; CONJECTURE FB-CAP; CONJECTURE INTO attacked (L-RED successor 17, box 41; GO 2026-10-25 16:53Z, date -u)
Targets (Lead 16:53Z, 17:25Z):
- (1) P-FREEZE (c), LEN-TAIL, NO-CROSS-A (docs/new/P-N5-PFZ-box39.md, sha1 3c617e06) and HAT-FREEZE (c), RHO-TAIL
  (docs/new/P-N5-RHO-box40.md, sha1 cd5df65c) after the freeze, at |U| ≥ 3.
- (2) NHN (docs/new/N5-NHN-box40.md, sha1 81302f57): T0-PIN, NHN-BOUND, EV2 ends after the hat freeze.
- (3) CONJECTURE INTO and case (ii) (docs/si/N5-RISE-box13.md, sha1 3b8fea13). (4) LV-NONE / SCOPE-FB: not started.
𝒞^1O only: exactly one Odd vertex with out-degree > 1, asserted in every checker. Labels per L40: PROVED / CONJECTURE / OPEN / DATA.
Nothing here is a running-time bound. G-N5-TIME stays OPEN.

## 0. Result
- **No kill.** All checks pass: 0 FAIL of P-FREEZE (a)-(c), LEN-TAIL, NO-CROSS-A, Y-FORM, HAT-FREEZE (a)-(c), RHO-TAIL, T0U, EV2-FB,
  SG-EV, T0-PIN, NHN-BOUND, INTO, case (i), case (ii) on every run of §2-§4.
- **(1), (2): the post-freeze regimes at |U| ≥ 3 were NOT reached**, nontrivially or at all, beyond the boundary case below.
  - P-FREEZE's hypothesis t > f_{|U|−1} needs ≥ |U| − 1 fallbacks inside one θ-run. The largest value of f − (|U| − 1) at |U| ≥ 3 is −1,
    and it is attained only at |U| = 3 with f = 1. This holds over the library, random games, n = 3 and partial n = 4 exhaustive
    (every start pair), and all climbs and shrinks (§2).
  - HAT-FREEZE (c) / RHO-TAIL: reached only at g = |U| − 2 exactly, with |U| = 3 and g = 1.
  - Every such phase is TRIVIAL: no F ∩ U vertex is below MoptÛ at the phase start, so the freeze converges nothing. This includes
    L-NEW's 5 box-40 climb phases.
  - NHN: T0-PIN's hypothesis (an EV2 end at g_j with j ≥ |U| − 1) never occurs.
- **CONJECTURE FB-CAP (L-RED succ. 17, DATA only):** in every phase, the in-phase Even S4c fallbacks number ≤ max(1, |U| − 2).
  - It holds in every run of §2, from any start pair tried, up to 37 fallbacks in one phase at |U| = 48 (rise_fb38_n48).
  - If true, then:
    - P-FREEZE (c), LEN-TAIL and NO-CROSS-A are vacuous for |U| ≥ 3;
    - BRK-POLY's branch j ≥ |U| is vacuous;
    - T0-PIN and NHN's post-freeze branch are vacuous;
    - in-phase fallbacks per phase are ≤ n − 2, far below BRK-POLY / HN-POLY.
  - It is a target for L-NEW (a proof), and for me (a kill; §2.4 says why the obvious argument fails).
- **(3) INTO: no failure.** Library, S3 + 2 random start pairs: 67 / 67 post-rise states with r > L have a gate into R̄; no fallback after
  a rise in case (i) or (ii). Climbs (§4) reach min #gates into R̄ = 1, never 0.

## 1. Tools (experiments/red/frz/; written from the frozen texts, own traces)
- pfz17.py: exact checker for P-N5-PFZ §2-§4, P-N5-RHO §1-§3 and N5-NHN §1-§5.
  - Simple-path maxima are computed by DFS with a budget; over-budget runs are counted as skipped.
  - Trace: sox.trace (= n5.run, SPEC S3), or ex16.trace from a start pair.
  - Regime counters PF_post_U*, HF_post_U*, HF_postH1_U*, and their NONTRIVIAL forms (*_nontriv_*: some vertex below Mopt at the
    run / phase start).
  - Cross-check: on experiments/new/box40/out/*.pg it reproduces L-NEW's P-N5-RHO §8 (C) counts exactly (Y-FORM 25, HAT-FREEZE (a) 22,
    HFc 10).
- climb17.py / shrink17.py: climbs on the excess f − (|U| − 1) (θ-run) or g − (|U| − 2) (phase).
  - shrink17 scores from the trace only and greedily deletes vertices and edges; then it mutates.
- rs17.py, rsu17.py: random canonical games; per-|U| maxima. rstart17.py: random games × random start pairs (FB-CAP).
- exfz17.py: exhaustive (ex16.games, every start pair), full pfz17 checks on every run with an Even fallback.
- fu17.py: per-|U| fallback counts per θ-run / phase. rep17.py: vertices switched by ≥ 2 fallbacks of one phase. fbwho.py: who switches
  at a fallback.
- into17.py: INTO / case (i) / case (ii) from N5-RISE §0, §2, with the scope-run machinery of rx16.py (box 39).
  - It splits INTO_FAIL (gates exist, all into F) from INTO_FAIL_NOGATE (Iσ_t = ∅; see §4).
  - It agrees with L-SI's §3 numbers on rise_thin51_n40 (t = 76) and tevlast7_n32 (states 18-40).
- intoclimb17.py (optional start-pair genome); intolib17.py.

## 2. (1)-(2): the post-freeze regimes (DATA)
### 2.1 Tables
| space | runs | max f − (|U|−1) per θ-run, |U| = 2 / 3 / 4 / 5 | max g − (|U|−2) per phase, |U| = 3 / 4 / 5 | nontrivial post-freeze at |U| ≥ 3 | FAIL |
| --- | --- | --- | --- | --- | --- |
| library (431 files, 𝒞^1O ones, S3; survey parts 0-2 with DFS checks; fu17 on all) | – | – / −1 / −2 / −3 | 0 / −1 / −2 | 0 | 0 |
| random n 6-16, S3 (rsu17, 2 × 600 s) | 1,543,851 | 0 / −1 / −2 / −3 (= 2 − |U| at every |U| ≤ 14) | 0 / −1 / −2 (= 3 − |U|) | – | – |
| random n 4-9 × 4 random start pairs (rstart17, 1,800 s) | 4,463,540 | – | g − max(1, |U|−2): 0 / −1 / −2 | – | – |
| n 3, every start pair, full space (exfz17) | 48,600 (1,756 with an Even fallback) | 0 / −1 / – / – | 0 / – / – | 0 | 0 |
| n 4, every start pair, full space (exfz17; PARTIAL at R71 time) | 14,370,048 of 83,607,552 (581,660 with an Even fallback) | 0 / −1 / −2 / – | 0 / −1 / – | 0 | 0 |
- In random canonical runs, EVERY phase has at most one in-phase Even fallback.
- Library maxima: 25 fallbacks in one θ-run at |U| = 48 (njb_reabs65_n48); 34 in one θ-run and 37 in one phase at |U| = 48
  (rise_fb38_n48).
- Survey part 3 (35 large files) hit its 1,800 s timeout with buffered output: NOT RUN for the DFS checks. fu17 (trace only) covered all
  431 files.

### 2.2 Climbs and shrinks (excess objectives)
| seed | objective | n start → end | best excess reached |
| --- | --- | --- | --- |
| random n 10, 12 (climb17 pf) | f − (|U|−1), nontrivial | 10, 12 | −1 (|U| = 3) |
| njb_reabs65_n48 (shrink17 pf, UMIN 4 / 3) | f − (|U|−1) | 48 → 16 / 35 | −2 (|U| = 4) / −1 (|U| = 3) |
| nleq_cex_n48 (shrink17 pf, UMIN 3) | f − (|U|−1) | 48 → 7 | −1 |
| njb_reabs65_n48 (shrink17 hat, UMIN 4) | g − (|U|−2) | 48 → 16 | −1 |
| rise_fb38_n48, rhc_pure_22_6, b5_os_n40 (shrink17 hat, UMIN 3: FB-CAP attack) | g − (|U|−2) | → 39, 9, 11 | 0 (|U| = 3, g = 1) |
- Every climb collapses to the boundary case: one fallback at |U| = 3.

### 2.3 Mechanisms (READING, from traces)
- Fallback at a cycle node outside U ("pump"; rhc_block_bk20_3, vertex 8, state 2).
  - An improving edge of a cycle node that only changes its own cycle's length is W-neutral, so S4a keeps σ and S4c switches it.
  - It is decoupled from U: such a switch changes no valuation. So it fires at the first fallback after it becomes ready and adds no
    separate fallback, unless U is already quiescent (Iσ on U empty).
- Eviction chain (njb_reabs65_n48, fallbacks 43-67, one vertex each).
  - Values: R values (c, {o, 10}, ·) < F values (c, ∅, ·) < W values (c, {o}, ·); o's priority is even and vertex 10's priority is odd
    with higher rank.
  - Each fallback evicts the R vertex whose Even edge onto the growing F path has just become improving. S4a never takes it (W-worse).
  - The chain's F anchor, o and c_θ are never evicted, so f ≤ |U| − 2 along the chain.
  - τ(o) = 11 stays Odd-optimal (Iτ = ∅ from state 10). In Odd's frame, Even's best reply from σ̄(o) = 43 closes a long cycle with top
    45 (same priority as c_θ = 21, higher rank). SI does not see it: no single switch reaches it.

### 2.4 Why FB-CAP is not obvious (attack notes)
- "Each U vertex is switched by at most one fallback per phase" is FALSE (rep17 on the library, 765 fallbacks):
  - 54 phases have a vertex switched by 2 fallbacks of one phase (b5_os_n12 … b5_os_n40; up to 8 such vertices at n 40, with g = 9 at
    |U| = 40);
  - 26 fallbacks switch only c_θ (a W-neutral cycle-node switch inside U).
  - FB-CAP still holds in all of them.
- So a proof needs a potential that is not a per-vertex count. In the data, FB-CAP is tight only at |U| ≤ 3.

## 3. Instances (DATA)
- experiments/red/frz/out/ is gitignored scratch. The boundary instances are library files:
  - rhc_block_bk20_3.pg (L-NEW box 40, sha1 cc459f93…): a θ-run with |U| = 3 and 1 fallback (the pump at vertex 8);
  - n4all_maxph_0.pg (L-COMP): a phase with |U| = 4 and 1 fallback.
- None is a counterexample.

## 4. (3) CONJECTURE INTO and case (ii)
- Setting as in N5-RISE §0, from the text: k0 an in-scope Even fallback with L = M_k0 ≥ 0; j the first S4a COARSE_L(θ) change; post-rise
  states t with every transition of (k0, t) an in-scope S4a step with r > L.
- Seeds (S3), sha1 re-measured:
  | seed | sha1 | rises | post-rise states with r > L |
  | --- | --- | --- | --- |
  | rise_thin51_n40 | 47aaf46e | 1 | 1 |
  | tevlast11_n40 | 8421ab30 | 1 | 27 |
  | farrise25_n32 | 8941d1c9 | 1 | 0 |
  | tevlast7_n32 | d905038c | 1 | 23 |
  INTO holds at all 51 post-rise states.
- Library (intolib17, 816 runs = S3 + 2 random start pairs per 𝒞^1O file, seed 7):
  - 59 rises, 67 post-rise states with r > L, INTO 67 / 67, min #gates into R̄ = 1;
  - fallbacks after a rise in the same scope run: 0 (case (i) and case (ii));
  - INTO_FAIL_NOGATE: 0.
- Climbs (intoclimb17; fitness (INTO fails + case (i) + case (ii), gate-free states, −min #gates into R̄, post-rise states), 3,000 s each):
  - from rise_thin51_n40 and tevlast11_n40 (S3), and from tevlast7_n32 with the start pair in the genome;
  - min #gates into R̄ reached 1, never 0; no HIT.
- Statement note (not a kill). As written, INTO quantifies over every post-rise state with r_t > L, including the LAST state of the
  stretch. If Iσ_t = ∅ there (Odd moves next), INTO fails for lack of any gate, although the reduction only needs INTO at fallback states.
  Not seen in data (0 states). Suggest "at every post-rise state with r_t > L and Iσ_t ≠ ∅", or restrict INTO to fallback states,
  which is all the reduction uses.

## 5. Dead ends of this box (each with its obstruction and instance)
- Padding fallbacks with a pump outside U. The obstruction: a pump's switch is W-neutral and changes no valuation, so S4c takes it
  together with the first U fallback after it becomes ready (rhc_block_bk20_3: the pump is the only fallback, at the end).
- "Each U vertex is evicted at most once per phase" as a route to FB-CAP: false on b5_os_n40 (8 vertices switched twice, §2.4).
- Excess objectives on hill climbs: every climb collapses to |U| = 3, f = 1. The excess rewards small |U|, not long fallback runs.

## 6. Open (for the Lead to route)
- FB-CAP: a proof (L-NEW), or an n ≥ 5 exhaustive or start-pair search (L-RED).
- The INTO wording at gate-free states (§4).
- (4) LV-NONE / SCOPE-FB: not started this box.
