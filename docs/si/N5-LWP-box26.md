# N5-LWP (box 26): CONJECTURE L-WAVE′ survives four new kill searches; candidate settling invariants killed; CONJECTURE SEG-LAST
L-SI successor 22 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 06:38Z, STEP 1: «CONJECTURE L-WAVE′ (GRUN §5) ... Aim: a proof
(the READING obstruction: gate competitors are off the end-state plays; Even P-changes are not events), or a kill with an instance. Try one
structurally different kill search (not more of the same climb from lwp_a) before committing to the proof route». Working note, unrefereed,
not frozen. Not a TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) /
CONJECTURE / OPEN / DATA / READING / DEAD. Counts are TRANSITIONS. Tools: experiments/si/lwp/ (gaps.py, rsamp.py, dagclimb.py, xclimb.py,
gaptrace.py, vstep.py, gapdepth.py, lastsw.py, seglast.py); outputs lwp/*.txt, lwp/out/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | four structurally different kill searches for L-WAVE′ (random start pairs on library games; independent small random games; the pure-length regime; a climb on the gap's excess over the end-state depth): no kill; best gap = n − 1 again (xk_k, n 26) | DATA |
| §2 | anatomy of the n − 1 gaps: a few multi-switch steps, then one "snake" (one Even switch per transition, each to the vertex that switched just before), driven by P-level waves at Even vertices | DATA, READING |
| §3 | candidate settling invariants that would prove L-WAVE′ (VS-STEP, PS-STEP, PV-STEP, GAP-DEPTH, LAST-SWITCH per gap): all DEAD, killers named | DEAD |
| §4 | surviving stronger forms: gap ≤ \|Even\| (NEVEN); gap ≤ switching Even vertices + L-cuts (SWL); CONJECTURE SEG-LAST (every transition of a REL segment is some Even vertex's last switch in it), which would drop (H4′_rel) and GEN_W from STATIC-DEPTH-REL | CONJECTURE, DATA |
| §5 | Lemma P-ARENA (the (c, P)-level form of STATIC-DEPTH′ step (A)) and the monotonicity of settled sets | PROVED (lane), elementary |
| §6 | where the proof route stands | READING, OPEN |
| §7 | Theorem LAST-STEP: SEG-LAST holds under STATIC-DEPTH-REL's hypotheses ((H4′_rel), GEN_W), by a frontier argument; the frontier exists at every step of all 3,134 library segments; CONJECTURE CYC-SET (which would remove (H4′_rel)) DEAD; CONJECTURE SET-STEP open | PROVED (lane); DATA; DEAD; CONJECTURE |
| §8 | Theorem K-REDUCTION: a terminal part of J_b on the unsettled vertices whose targets are in the arena settles in one step (contains LAST-STEP); its hypothesis K-ARENA DEAD (karena_kill_n71); in the library every step is covered by the singleton case | PROVED (lane); DATA; DEAD |

## 0. Setting
As N5-GRUN-box25 §0, §4, §5. A run S: a maximal fallback-free stretch of one phase. REL segments, RO_b, X_b, CW_b, CH_b, L-cuts as in GRUN
§4-§5 (grun/relseg.py, grun/lwave.py). L-WAVE′ EVENTS (grun/lwave.py PMODE=1): the non-L REL cuts and every transition at which the path
set P of Ξ changes at an Odd choice vertex of RO_b (b the end of the segment holding the transition). A GAP [x, y]: consecutive points of
{run start, events, run end}; its length y − x (as in lwave.py). CONJECTURE L-WAVE′: every gap has ≤ n − 1 transitions.
lwp/gaps.py reproduces lwave.py's cutting (same counts on lwp_a, lwkill_n31) and also returns the event and L-cut states. In §3-§4 a gap
closing at an event y is examined on [x, y − 1] (the closing transition is the event itself; REFERENCE state b := y − 1), else on [x, y].

## 1. Kill searches for L-WAVE′ (DATA; score = max gap − (n − 1), > 0 is a kill)
| search | what is different from box 25's climbs | size | best score |
| --- | --- | --- | --- |
| lwp/rsamp.py MODE=lib (lwp/out/rl1.log, rl2.log) | no game mutation: alt_all games (n ≤ 60) with uniformly random start pairs (σ0, τ0) | ≥ 66,187 + 42,511 trials (stopped by me) | 0, only at n 4-6 (trivial gaps n − 1) |
| lwp/rsamp.py MODE=rand (rs1.log) | independent random games n 4-7, out-degree ≤ 3, random starts | ≥ 64,212 trials (stopped by me) | 0 at n 5 |
| lwp/dagclimb.py TAUOPT=1 (dag20.log, dag32.log) | the PURE-LENGTH REGIME: a DAG plus one top even sink g, all other priorities 0, so c = g and P = ∅ at every vertex and state; then no P-event can occur and a run is one gap up to ties; τ0 = Odd's optimal distance strategy, so the whole game is one phase | 2 × 40,000 steps, n 20 fixed and n ≤ 32 | −14 (n 20, run 5), −9 (n 15, run 5): runs ≤ 0.33n |
| lwp/xclimb.py (OBJ=GD; xa, xr, xk logs) | objective = 2 × (gap − end-state REL depth) + (gap − (n − 1)): grows the time L-cuts add beyond STATIC-DEPTH-REL's depth instead of the raw gap; seeds lwp_a, run49_n32 (default start), lwkill_n31 | 3 × 20,000 steps | 0: xk_k (n 26, gap 25 = n − 1); xa −4 (n 22); xr −4 |
- CORRECTION (written before the push): the climbs scored the depth excess with an earlier reference rule (a gap closing at an event AT
  the run end was measured on [x, y], after the event), which inflated it (xk 22, xa 15). Under §0's rule (reference y − 1 whenever y is an
  event) the excess is 1 on xk_k / xk and 0 on xa (lwp/gapdepth.py). So the GD climb was partly mis-aimed; it still found a second gap of
  n − 1, and no kill.
- READING (pure-length regime): a one-switch-per-step wave a_1 ← a_2 ← ... ← a_k needs every edge a_j → a_(j−1) to be non-improving until
  a_(j−1) switches, i.e. the a_j's initial targets must be longer than the wave's route: a shared slow path of length ≥ k, so a wave uses
  ≤ about n/2 transitions. The long waves of §2 are P-level waves; lengths alone do not make them.
- Pins (lwp/out/; sha1sum; frozen copies of xk_k as lwp/instances/lwp_gap_n26.*): xk_k.pg 1ad8d0036d3d1503b8f672199110d3f41c65030a, xk_k.start a2e00ea7c3383b9cd35d21f306c77c8fc3f57684 (gap n − 1,
  one Odd choice vertex 4); xa.pg d18575db040f26b4bc02c98a15b21550ed4004bf, xa.start 5a951ab112a2896e38a987eaafedca102b559948 (gap n − 5). grun/out/lwp_a.pg 19d105416929800709707a2489b335a6a936e883, .start ebe3da481098f568ee171b061ab70e2d0f786bbd.

## 2. Anatomy of an n − 1 gap (lwp/gaptrace.py on grun/out/lwp_a, n 26, gap [1, 26], one gate u = 4, L-cuts at 5 and 16)
- Transitions 1-4: several Even vertices switch at once (10, 5, 8, 7 switches), vertex 6 switches 14 > 24 > 14 > 24 and vertex 11 four times.
- Transitions 5-25: ONE Even switch per transition, each vertex to the one that switched just before (25 → 8, 13 → 25, 24 → 13, ..., 3 → 12):
  a snake through 21 distinct vertices. Only the switching vertex changes its path set; at the L-cut 15 → 16 the gate's σ̄ moves 0 → 5 and 13
  vertices change length only.
- The path sets go through three levels (weights −2^25 → −2^24 → −2^23 in E.weight: plays first avoid vertex 16 (priority 63, odd), then 5
  (63, odd)); a vertex can pass through an intermediate level before its final one, which is why the settling potentials of §3 fail.
- A kill needs some Even vertex to switch twice inside one gap on the snake's route; xk_k (n 26) has the same shape.

## 3. Candidate invariants that would prove L-WAVE′: DEAD
Each would bound a gap by a monotone count (Ξ is monotone, RESULTS R15 (a), and S1's order is lexicographic in (c, P, ℓ), so the sets
below only grow; §5).
| candidate | statement (on [x, b], b the reference state) | killer | corpus (alt_all default / pinned starts) |
| --- | --- | --- | --- |
| VS-STEP | every transition makes some vertex VALUE-settled (Ξ_(t+1)(v) = Ξ_b(v) ≠ Ξ_t(v)) | lwp_a: 13 of 25 transitions settle nothing (the late L-cut moves every length) | (KEY=V; not re-run) |
| PS-STEP | ... some vertex (c, P)-settled | lwp_a t = 2; lend27_n24 [5, 7] t = 6 | 109 / 144 failing transitions (lwp/vstep_alt*.txt) |
| PV-STEP | ... some vertex (c, P)- or value-settled (would give gap ≤ 2n) | lwp_a t = 2 | 0 / 0 (PVSTEP PASS); dead by lwp_a only |
| GAP-DEPTH | gap ≤ max_Q d at b (STATIC-DEPTH-REL with L-cuts allowed) | lwp_a 25 > 23; xk_k 24 > 23 | 8 / 5 gaps fail (gci2_n12: gap 6, depth 0) (lwp/gapdepth_alt*.txt) |
| LAST-SWITCH (gap) | every transition is the last switch in the gap of some Even vertex (would give gap ≤ \|Even\|) | lwp_a t = 2, 3; xk_k one transition | 0 / 0 (lwp/lastsw_alt*.txt); lib41 0 |
- Controls: MODE=run (the same tests on whole runs) fails as it must (VS/PV on lwkill_n31 [2, 40]: 36 transitions; LAST-SWITCH 17).

## 4. Surviving stronger forms (CONJECTURE; DATA)
- NEVEN: every gap [x, b] has b − x ≤ |Even|. DATA: max (b − x) − |Even| = −1 (alt_all default), 0 (pinned starts, lib41; lwp_a; xk_k −1).
- SWL: b − x ≤ (Even vertices that switch in [x, b]) + (L-cuts in the gap). 0 violations: alt_all 974 + 1,332 gaps, lib41 1,125 gaps,
  lwp_a (25 = 23 + 2), xk_k (lwp/lastsw*.txt).
- CONJECTURE SEG-LAST: in every maximal REL-admissible segment [a, b] (GRUN §4), every transition t → t + 1 (a ≤ t < b) is the last switch in
  [a, b] of some Even vertex. DATA (lwp/seglast.py): 0 failures on alt_all (907 segments, 4,478 transitions; pinned starts 1,249 / 5,384),
  lib41 (978 / 4,241), lwp_a, xk_k, lwkill_n31. Controls: on whole runs it fails (144 failing transitions on alt_all), and on σ̄-constant
  PIECES it fails at 4 transitions (cw11_n24 [0, 3] twice: one vertex switching 3 times, the piece crosses a cycle appearance (N5-PIECE-box25
  §1); cw11_n24 [12, 14]; cone_n69 [2, 20]): the persistence of the end-state cycles matters. D_t := {v : σ_t(v) ≠ σ_b(v)} is NOT monotone (161 lib41 segments).
  Kill search (lwp/xclimb.py OBJ=SL, score 10 × failures + max(length − switchers)): from cw11_n24 and pftheta34_n32 (20,000 steps each;
  lwp/out/sl_*.log): best 0, no failure.
- What SEG-LAST would give (READING, a REDUCTION): Even vertices on the end-state cycles of a REL segment never switch in it (proof of
  STATIC-DEPTH′, first item) and out-degree-1 vertices never switch, so SEG-LAST bounds the segment by |Q ∖ (T_W ∪ T_H)| ≤ n − 1 WITHOUT
  (H4′_rel) and GEN_W: it would cover the 45 + 49 segments where (H4′_rel) fails (GRUN §4) and CONJECTURE STATIC-DEPTH′-TIE for pieces
  inside one segment.

## 5. PROVED (lane), elementary
- Monotone settled sets. On states [x, b] of one run (in-phase S4a transitions only), let VS_t := {v : Ξ_t(v) = Ξ_b(v)} and PS_t := {v :
  (c, P) of Ξ_t(v) = (c, P) of Ξ_b(v)}. Then VS_t ⊆ VS_(t+1) and PS_t ⊆ PS_(t+1). Proof: R15 (a) gives Ξ_t ⊴ Ξ_(t+1) ⊴ Ξ_b pointwise. S1's
  order compares c (by reward), then P (by weight), then ℓ: so the (c, P) projection is monotone (x ⊴ x′ implies (c, P)(x) ≤ (c, P)(x′)
  lexicographically), and a value sandwiched between two equal values (or two equal projections) equals them. □
- Lemma P-ARENA. Let t ≤ b be states of one run, v Even, y := σ_b(v) ≠ σ_t(v) =: z, v not the cycle node of Ξ_t(v) nor of Ξ_b(v), with
  Ξ_b(v) = v ⊕ Ξ_b(y) and Ξ_t(v) = v ⊕ Ξ_t(z), and y ∈ PS_t. If v ∉ PS_t, then (v, y) ∈ Iσ_t (so y is in v's S4a arena at t).
  Proof. Otherwise Ξ_t(y) ⊴ Ξ_t(z) (S1's order is total; S2). Write π for the (c, P) projection. The map x ↦ v ⊕ x keeps the cycle node,
  adds v to P or not according to p′(v) > p′(c) alone, and adds 1 to ℓ (S1; the argument in GATE-RISE, GRUN §2), so π(v ⊕ x) is a function of
  π(x) and is monotone in it. Then π(v ⊕ Ξ_t(y)) ≤ π(v ⊕ Ξ_t(z)) = π(Ξ_t(v)) ≤ π(Ξ_b(v)) = π(v ⊕ Ξ_b(y)) = π(v ⊕ Ξ_t(y)) (the last step:
  y ∈ PS_t). So π(Ξ_t(v)) = π(Ξ_b(v)), i.e. v ∈ PS_t: contradiction. □
- Use: P-ARENA is step (A) of STATIC-DEPTH′ at the (c, P) level (no play-settling of y needed). Step (B) has no (c, P) analogue in hand:
  S4a chooses in the W-frame, so v may take another arena edge with the same W-value.

## 6. Where the proof route stands (READING; OPEN)
- The two obstructions of GRUN §5 are both present in the data: (i) GAP-DEPTH fails (13 corpus gaps; gci2_n12: gap 6 at depth 0; lwp_a by 2):
  L-cuts make gaps outlast the end-state depth, so no induction along the end-state plays alone can work; the competitors' rise (off the end-state plays) is what costs the
  time. (ii) Even P-changes inside gaps are the snakes of §2.
- Every successful bound in the data is a COUNT of vertices (NEVEN, SWL, SEG-LAST), not a depth. A proof of L-WAVE′ along these lines would
  show that each transition of a gap "uses up" one Even vertex for good, up to one extra transition per L-cut (SWL). SWL gives only
  gap ≤ |Even| + L-cuts, and L-cuts per gap are ≤ Σ_gates (n − 1) (ℓ moves one way inside a P-block, GRUN §5): an O(n·#gates) gap bound, which
  is weaker than L-WAVE′ but polynomial; it is CONJECTURE (SWL is not proved).
- Next proof target: SEG-LAST under STATIC-DEPTH′'s hypotheses (one piece, end-state cycles persistent). Its contrapositive: if no vertex has
  its last switch at t, every switcher of t switches again later; the (c, P)-level tools above do not exclude this.

## 7. Theorem LAST-STEP (PROVED, lane): SEG-LAST under STATIC-DEPTH-REL's hypotheses (STEP 2, box 26)
Premises: RESULTS R82 (STATIC-DEPTH′) and R83 (STATIC-DEPTH-REL) as LANDED, their proof steps (signed there) used locally, and RESULTS R80 (a)
EVERY-SWITCH. Notation of GRUN §4 at the segment end b: X_b, RO_b, CW_b, CH_b, T_W, T_H, T := T_W ∪ T_H, J_b (restricted to X_b, (H4′_rel)).
S^W_s (S^H_s): the vertices whose W-play (honest play) at every state of [s, b] equals the one at b; S_s := S^W_s ∩ S^H_s. These grow with s.
Statement. Let [a, b] be REL-admissible, with (H4′_rel) and GEN_W. Then for every t ∈ [a, b) some Even v ∈ X_b ∖ T switches at t → t + 1 and
never again in [a, b] (CONJECTURE SEG-LAST holds on [a, b]). Hence b − a ≤ the number of Even vertices of X_b ∖ T that switch in [a, b].
Local facts (each is a step of the STATIC-DEPTH′ / STATIC-DEPTH-REL proof, used with an arbitrary start s instead of a + d):
- (F1) T_W ⊆ S^W_a, T_H ⊆ S^H_a, and an Even vertex of T has σ_t = σ_b on [a, b].
- (F2) Odd v ∉ T_W on the W-play of a member of X_b: τ(v) ∈ S^W_s implies v ∈ S^W_s; Odd v ∉ T_H in RO_b: σ̄(v) ∈ S^H_s implies v ∈ S^H_s.
  Even v ∈ T_H ∖ T_W: σ_b(v) ∈ S^W_s implies v ∈ S^W_s; Even v ∈ T_W ∖ T_H: likewise for H.
- (F3) Even v ∈ X_b ∖ T, y := σ_b(v) ∈ S_s (s ≤ b): σ_u(v) = y for every u ∈ [s + 1, b], and if also σ_s(v) = y then v ∈ S_s.
  (Steps (A), (B) and the GEN_W step of STATIC-DEPTH′ for t ∈ [s, b − 1]; the second part: v's plays at u ∈ [s, b] are v followed by y's,
  which are y's plays at b and avoid v since v ∉ T.)
Proof. Fix t < b. Call v a FRONTIER vertex if v is Even in X_b ∖ T, σ_t(v) ≠ σ_b(v) and σ_b(v) ∈ S_t. By (F3) with s = t a frontier vertex
has σ_(t+1)(v) = σ_b(v) ≠ σ_t(v) and σ constant on [t + 1, b]: it switches at t for the last time. So it suffices that a frontier vertex
exists. Suppose not, and let N := (X_b ∩ Even) ∖ (T ∪ S_t).
- N ≠ ∅: otherwise every Even vertex of X_b ∖ T is in S_t, so its σ is σ_b on [t, b] (the first step of its W-play); Even vertices of T keep
  σ_b (F1); Even vertices outside X_b are not in Q (X_b ⊇ Q) and have out-degree 1. So σ_t = σ_(t+1), against EVERY-SWITCH.
- Every v ∈ N has σ_b(v) ∉ S_t: if σ_b(v) ∈ S_t then σ_t(v) = σ_b(v) (v is not a frontier vertex) and (F3) gives v ∈ S_t.
- Every v ∈ N has a J_b-successor in N. Let y := σ_b(v); say y ∉ S^W_t (the case y ∉ S^H_t is the same with honest plays, σ̄ and T_H).
  Walk along v's W-play at b from y. If it reached T_W passing only Odd vertices and Even vertices of T_H ∖ T_W, then (F1) and (F2), applied
  backwards from the first vertex of T_W, would put y in S^W_t. So it meets an Even vertex v′ ∉ T first, which is v's J_b-successor; and
  v′ ∉ S^W_t (else (F2) backwards puts y in S^W_t again). v′ is on the W-play of a member of X_b, hence v′ ∈ X_b; so v′ ∈ N.
- So J_b restricted to N has no sink, and N is finite and non-empty: J_b has a cycle, against (H4′_rel). □
- Remarks. (o) This strengthens the conclusion of STATIC-DEPTH-REL (b − a ≤ max d) to one per-transition statement; it uses the same
  hypotheses, so it removes nothing yet. (i) The bound "b − a ≤ switchers" is a count, not a depth; both are ≤ |Q ∖ T| ≤ n − 1. (ii) The proof uses (H4′_rel) ONLY in
  the last line: a J_b-cycle whose vertices are all unsettled at t. So SEG-LAST without (H4′_rel) reduces to: (H4″) no J_b-cycle lies in
  N_t at any t < b. A J_b-cycle mixes the frames (an all-W cycle would be a W-cycle at b, in T_W), so it contains Odd vertices o, o′ with
  τ(o) ≠ σ̄(o) on its W-legs and on its honest legs; nothing proved here excludes that it stays unsettled.
DATA (lwp/laststep.py; FR_V = steps without a frontier vertex, FRL_V = frontier vertices whose last switch is not at t; MUT=1 asks for
σ_b(v) ∈ S_(t−1) and must bite: it does on lwp_a and dl_6_8):
| corpus | segments | transitions | (H4′_rel) fails | FR_V | FRL_V | J_b-cycle vertices not settled from a (CYCSET_V) |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all, default starts (lwp/laststep_alt.txt) | 907 | 4,478 | 5 | 0 | 0 | 0 (77 cycle vertices) |
| alt_all, pinned starts (lwp/laststep_alt_start.txt) | 1,249 | 5,384 | 3 | 0 | 0 | 1 (run34_n40 [11, 14]; frontier still present) |
| lib41 (lwp/laststep_lib41.txt) | 978 | 4,241 | 2 | 0 | 0 | 0 (39) |
- So in the library a frontier vertex exists at EVERY step, also in the 10 segments where (H4′_rel) fails (dl_6_8 [1, 7]: 28 J_b-cycle vertices,
  all settled from a). CONJECTURE CYC-SET («every J_b-cycle vertex of a REL segment is settled from its start»; with it the proof above needs
  no (H4′_rel)) is DEAD, already in the library (run34_n40 with its pinned start, segment [11, 14]: 14 cycle vertices settled only from
  12-14, while a frontier vertex exists at every step), and with no frontier vertex by lwp/xclimb.py OBJ=H4 (score: long (H4′_rel)-failing segments; kill = SEG-LAST or frontier failure) from dl_4_4 found
  lwp/out/h4a_k.pg (n 60, sha1 957c7c9e2ce5a6d57890e42b0e8ca0a0911ecefd, default start; frozen copy lwp/instances/cycset_kill_n60.pg; segment [0, 4], J_b-cycle vertices 1, 3, 34, 37, 48, 58, 59
  settled only from 1, no frontier vertex at t = 0) and h4b_k.pg (n 48, e97f88d5ea74f45822aeec7dd5e146cb40d91ce3; segment [1, 4], cycle
  vertices 31, 33, 34, 35 settled from 2). SEG-LAST still holds on both.
- What happens there (DATA, h4a_k t = 0): the unsettled J_b-cycle vertices 1 and 37 switch TOGETHER at t = 0 (1: 28 → 59, 37: 6 → 58), both for
  the last time, and the whole cycle is settled from t + 1. CONJECTURE SET-STEP («at every t of a REL segment some switcher of t is in
  S_(t+1)»; it implies SEG-LAST): 0 failures in the 3,134 segments (lwp/seglast.py SS_V) and on h4a_k, h4b_k. The proof route: a terminal
  strongly connected part K of J_b on N_t settles in one transition; step (A) (arena membership) is what is missing, since the targets'
  honest values are not final before K settles.

## 8. Theorem K-REDUCTION (PROVED, lane): SEG-LAST without (H4′_rel), given K-ARENA
Setting and premises as §7 (R82, R83 proof steps; R80 (a) EVERY-SWITCH; S4a's pointwise W-optimality over strategies using arena edges, as
listed in R82). A(t, v) := {σ_t(v)} ∪ {w : (v, w) ∈ Iσ_t} (v's S4a arena at t). N_t := (X_b ∩ Even) ∖ (T ∪ S_t). A TERMINAL PART of J_b on N_t
is a strongly connected set K ⊆ N_t such that every J_b-successor of a vertex of K lies in K or outside N_t.
- K-ARENA at t: some terminal part K of J_b on N_t has σ_b(v) ∈ A(t, v) for every v ∈ K.
Statement. Let [a, b] be REL-admissible with GEN_W (no (H4′_rel)). If K-ARENA holds at t ∈ [a, b) for the part K, then σ_s = σ_b on K for every
s ∈ [t + 1, b], K ⊆ S_(t+1), and some v ∈ K has σ_t(v) ≠ σ_b(v): v switches at t for the last time in [a, b]. So if K-ARENA holds at every
t < b, SEG-LAST (and SET-STEP) hold on [a, b] and b − a ≤ the number of Even vertices of X_b ∖ T that switch in [a, b] ≤ n − 1.
Proof. N_t ≠ ∅ for t < b (§7, first bullet), so terminal parts exist (a sink component of the condensation).
- (1) Off-K vertices on K's plays are settled. Let v ∈ K. On v's W-play at b, the first Even vertex outside T after v is a J_b-successor: in
  K, or in S_t, and then every vertex after it on its W-play is W-settled from t (suffixes of a play that is constant on [t, b]). The same
  holds for honest plays. Odd vertices on these plays use τ (W) or σ̄, constant on RO_b (honest); Even vertices of T keep σ_b (F1). So for
  any state s ∈ [t, b] and any σ* with σ* = σ_b on K and σ* = σ_s off K, the W-play (honest play) of v ∈ K under σ* (with τ, resp. σ̄)
  equals its W-play (honest play) at b: at every vertex the successor is the b-successor (W-settled Even vertices have σ_s = σ_b), and the
  play ends in a cycle of CW_b (CH_b), which is a cycle of its frame at s (REL-admissible).
- (2) s = t + 1. Let σ′ := σ_(t+1) with σ′ := σ_b on K. By K-ARENA, σ′ uses arena edges of state t. By (1) (with σ_(t+1) off K, s = t + 1),
  W_σ′(v) = W_b(v) for v ∈ K. S4a's pointwise optimality gives W_(t+1)(v) ⊵ W_b(v), W-MONO gives ⊴, so they are equal. The cycle node of W_b(v)
  is on a cycle of CW_b, a W-cycle at t + 1, so v's W-play at t + 1 ends in it; GEN_W gives v's W-play at t + 1 = its W-play at b, hence
  σ_(t+1)(v) = σ_b(v), for every v ∈ K.
- (3) Induction. If σ_s = σ_b on K for some s ∈ [t + 1, b − 1], K-ARENA at s holds trivially (σ_b(v) = σ_s(v)), and (2) at state s (off-K
  vertices are settled from t ≤ s) gives σ_(s+1) = σ_b on K. So σ = σ_b on K on [t + 1, b], and (1) gives K ⊆ S_(t+1).
- (4) If σ_t = σ_b on K, (3) runs from s = t and (1) gives K ⊆ S_t, against K ⊆ N_t. So some v ∈ K has σ_t(v) ≠ σ_b(v) = σ_(t+1)(v). □
Corollary (contains Theorem LAST-STEP). K-ARENA holds automatically for a terminal part that is a single vertex {v}: v ∉ T is not its own
J_b-successor, so all J_b-successors of v are in S_t, then (F1), (F2) backwards put y := σ_b(v) in S_t, and step (A) of STATIC-DEPTH′ puts y
in A(t, v). Under (H4′_rel) every terminal part is a single vertex. So K-ARENA can fail only when EVERY terminal part of J_b on N_t is a
J_b-cycle (size ≥ 2), and SEG-LAST without (H4′_rel) is reduced to: CONJECTURE K-ARENA for terminal J_b-cycles of unsettled vertices.
GEN_W is still used (step (2)); CONJECTURE STATIC-DEPTH′-TIE stays open.
DATA (lwp/laststep.py KARENA_V: steps with no arena-complete terminal part; KSET_V / KLAST_V: an arena-complete part that is not settled
from t + 1 / has no last switch at t, which the theorem excludes under GEN_W; lwp/laststep_*.txt, the same runs as the §7 table):
- alt_all (4,478 steps; pinned starts 5,384) and lib41 (4,241): KARENA_V = KSET_V = KLAST_V = 0, and NO step has a nontrivial terminal part
  (kar_nontrivial = 0): in the library every step is covered by the singleton case, i.e. by the Corollary, even in the 10 (H4′_rel)-failing
  segments (their J_b-cycles are not terminal among the unsettled vertices, or are settled).
- cycset_kill_n60 (the climb instance of §7): one step (t = 0) with a nontrivial terminal part K ⊇ {1, 37}; K-ARENA holds there and K
  settles from t + 1, as the theorem says.
- READING (where K-ARENA can fail). Inside a terminal part K the honest J_b-edges form an acyclic graph (an honest J_b-cycle would be an honest
  cycle at b, in T_H), so K has H-EXIT vertices, whose honest J_b-successor lies outside K (in S_t). For an H-exit v, y := σ_b(v) is
  H-settled from t and step (A) gives y ∈ A(t, v). So K-ARENA can fail only at a vertex v ∈ K with σ_t(v) ≠ σ_b(v) whose honest
  J_b-successor u is in K and whose target's honest value Ξ_t(σ_b v) still rises before v's last switch, i.e. u is not yet at its b-value at t.
- CONJECTURE K-ARENA is DEAD (DEAD.md box 26): lwp/xclimb.py OBJ=KA (score: steps with a nontrivial terminal part; kill = K-ARENA / KSET /
  KLAST / SEG-LAST failure; lwp/out/ka*.log) from cycset_kill_n60 found lwp/instances/karena_kill_n71.pg (n 71, sha1
  8b659497688c47075235957ae1e636b5564ec235) in 511 steps: at t = 0 the only terminal part K = {1, 3, 35, 41, 46, 50, 64} has 41 with
  σ_0(41) = 50 ≠ 35 = σ_b(41) and (41, 35) not improving at 0, exactly the case of the READING above (41's honest J_b-successor 35 is in K and
  switches 46 → 50 at 0). K settles in two layers (from states 1 and 2). SEG-LAST holds: 1 and 35 switch at 0 for the last time.
- So SEG-LAST without (H4′_rel) needs a LAYERED form of the theorem: vertices of K whose targets are in the arena take them for good, the
  next honest layer follows. The partial strategy σ′ (σ_b on the arena-ready vertices only) breaks step (2), because their W-plays pass
  vertices of K that are still off target. OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/lwp/ tools and logs; pins in §1, §7 (lwp/instances/); DEAD entries in docs/si/DEAD.md (box 26);
  check.sh blocks "box 26".
- FINDINGS: (1) L-WAVE′ survives four structurally different kill searches (random starts, random games, pure-length regime, depth-excess
  climb); gap = n − 1 is reached again (xk_k) and never beaten. (2) DEAD: VS-STEP, PS-STEP, PV-STEP, GAP-DEPTH, per-gap LAST-SWITCH (lwp_a,
  xk_k), CYC-SET (run34_n40, cycset_kill_n60), K-ARENA (karena_kill_n71). (3) CONJECTURE SEG-LAST (0 failures in 3,134 segments; it fails on pieces and runs, which serve as controls)
  would remove (H4′_rel) and GEN_W from STATIC-DEPTH-REL; SWL, NEVEN and SET-STEP hold in the data. (4) PROVED (lane): monotone settled sets;
  Lemma P-ARENA; Theorem LAST-STEP (SEG-LAST under (H4′_rel) + GEN_W, by a frontier argument that uses (H4′_rel) only to exclude an
  unsettled J_b-cycle); Theorem K-REDUCTION (§8: a terminal part of J_b on the unsettled set whose targets are all in the arena settles
  in one step; contains LAST-STEP). L-WAVE′, SEG-LAST without (H4′_rel), STATIC-DEPTH′-TIE stay OPEN.
- NEEDS: none from the owner.
