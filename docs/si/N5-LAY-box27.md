# N5-LAY (box 27): frame-wise sinks; SEG-LAST reduces to SINK-GROW (a frame-wise settled set grows at every step); W-GROW and H-GROW DEAD
L-SI successor 23 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 08:10Z, STEP 1: «the layered K-REDUCTION (queue item 1):
prove CONJECTURE SEG-LAST without (H4′_rel) (GEN_W may stay), or find a SEG-LAST failure inside a REL segment. ... If a proof needs a new
hypothesis, state it and measure how often it holds on the library and on the kill instances.» Working note, unrefereed, not frozen. Not a
TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN /
DATA / READING / DEAD. Counts are TRANSITIONS. Tools: experiments/si/lay/ (wsink.py, wclimb.py, anat.py); outputs lay/*.txt, lay/out/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | frame-wise settled sets S^W_t, S^H_t and frame-wise SINKS (W-sink: W-unsettled, its next Even non-T vertex on its b-W-play W-settled) | definitions |
| §2 | Lemmas W-STICK, H-STICK, READY, SINK-OFF; Theorem SINK-STEP: an arena-ready W-sink, and an H-sink that switches to its target, switch at t for the LAST time; W-GROW(t) ⇔ some W-sink is arena-ready at t | PROVED (lane) |
| §2 | Corollary: SEG-LAST without (H4′_rel) on every REL segment where W-GROW or H-GROW holds at each step (GEN_W kept); contains LAST-STEP (box 26 §7) and K-REDUCTION (box 26 §8) | PROVED (lane) |
| §3 | W-GROW and H-GROW at every step of the library (14,103 steps, 3,134 segments) and of the three box-26 kill pins, including the 4 steps with no frontier vertex; the box-26 N_t-version (MUT) fails there | DATA |
| §4 | W-GROW DEAD (lay/instances/wgrow_kill_n90, t = 1) and H-GROW DEAD (lay/instances/hgrow_kill_n89, 6 of 7 steps), both two engines; dual obstructions (a W-sink waits for its target's honest value; an H-sink waits for its W-chain); CONJECTURE SINK-GROW (W-GROW ∨ H-GROW at each step) survives both; kill searches on SINK-GROW | DEAD; CONJECTURE; DATA |
| §5 | where a proof of W-GROW stands; the remaining obstruction (a zig-zag of unready W-sinks) | READING, OPEN |

## 0. Setting and premises
As N5-LWP-box26 §0, §7, §8 (GRUN §4 notation). A maximal REL-admissible segment [a, b] of one fallback-free run, GEN_W assumed, NO (H4′_rel).
Premises (as in box 26 §7-§8): RESULTS R82 (STATIC-DEPTH′) and R83 (STATIC-DEPTH-REL) as LANDED and their proof steps (signed there):
(W-MONO) W_{t+1} ⊵ W_t; (Ξ-SUCC) Ξ_t(σ_t v) non-decreasing in t; (SW) every Even switch of N5 is to an edge of Iσ_t; S4a's pointwise
W-optimality over strategies that use arena edges of state t; R15 (a) Ξ_t ⊴ Ξ_{t+1}; R80 (a) EVERY-SWITCH. τ is constant on the run; on
RO_b, σ̄_t = σ̄_b on [a, b] (REL); every cycle of CW_b (CH_b) is a W-cycle (honest cycle) at every state of [a, b] (REL).

## 1. Definitions
- E_b := (Even ∩ X_b) ∖ T, T = T_W ∪ T_H. For v ∈ E_b: y_v := σ_b(v); A(t, v) := {σ_t(v)} ∪ {w : (v, w) ∈ Iσ_t}; v is ARENA-READY at t if
  y_v ∈ A(t, v) (in particular if σ_t(v) = y_v).
- S^W_t (S^H_t): the vertices whose W-play (honest play) is the same at every state of [t, b]. Monotone in t (box 26 §5). U^W_t := E_b ∖ S^W_t,
  U^H_t := E_b ∖ S^H_t. (Box 26's N_t is U^W_t ∪ U^H_t.)
- jW(v) (jH(v)): the first Even vertex outside T after v on v's W-play (honest play) at b, or ⊥. The map jW follows v's simple b-W-play, so
  jW-chains have no repeats; likewise jH.
- W-SINK at t: v ∈ U^W_t with jW(v) ∉ U^W_t (⊥ allowed). H-SINK at t: v ∈ U^H_t with jH(v) ∉ U^H_t.
- W-GROW(t): S^W_{t+1} ∩ E_b ⊋ S^W_t ∩ E_b. H-GROW(t): the same with S^H.

## 2. PROVED (lane)
- Lemma CHAIN. If v ∈ E_b and jW(v) ∉ U^W_t then y_v ∈ S^W_t; if jH(v) ∉ U^H_t then y_v ∈ S^H_t.
  Proof. The b-W-play from y_v reaches jW(v) (or, if jW(v) = ⊥, the first vertex of T_W) through Odd vertices off T_W and Even vertices of
  T_H ∖ T_W only; (F1), (F2) of box 26 §7 backwards from that vertex put y_v in S^W_t. Honest: the same with T_H, σ̄ (constant on RO_b). □
- Lemma W-STICK. If v ∈ E_b, y_v ∈ S^W_t and v is arena-ready at t, then σ_s(v) = y_v for every s ∈ [t + 1, b], and v ∈ S^W_{t+1}.
  Proof. Step (B) and the GEN_W step of R82 (N5-PIECE-box25 §2) at the single vertex v: σ′ := σ_{t+1} with v ↦ y_v uses arena edges of
  state t; y_v's W-play under σ_{t+1} is its W-play at b (y_v ∈ S^W_t), which avoids v (v ∉ T_W), so it is also its play under σ′ and
  W_σ′(v) = v ⊕ W_b(y_v) = W_b(v). S4a's optimality gives W_{t+1}(v) ⊵ W_b(v), W-MONO gives ⊴, so they are equal; the cycle node of W_b(v)
  is on a cycle of CW_b, a W-cycle at t + 1 (REL), so v's W-play at t + 1 ends in the same cycle as at b, and GEN_W makes the plays equal:
  σ_{t+1}(v) = y_v. Induction on s ∈ [t + 1, b − 1]: σ_s(v) = y_v makes v arena-ready at s and y_v ∈ S^W_t ⊆ S^W_s, so σ_{s+1}(v) = y_v.
  v's W-play on [t + 1, b] is v followed by y_v's, constant: v ∈ S^W_{t+1}. □
- Lemma H-STICK. If v ∈ E_b, y_v ∈ S^H_t and σ_s(v) = y_v for some s ∈ [t, b], then σ = y_v at v on [s, b], and v ∈ S^H_s.
  Proof. Otherwise v leaves y_v at some s1 ≥ s (σ_{s1+1}(v) = w ≠ y_v) and returns at some s2 > s1 (σ_b(v) = y_v). By (SW) at s2 and at s1,
  Ξ-SUCC and R15 (a): Ξ_{s2}(y_v) ▷ Ξ_{s2}(σ_{s2} v) ⊵ Ξ_{s1+1}(w) ⊵ Ξ_{s1}(w) ▷ Ξ_{s1}(σ_{s1} v) = Ξ_{s1}(y_v) = Ξ_{s2}(y_v), the last equality
  because y_v's honest play is the same at s1 and s2 and a valuation is a function of the play. Contradiction. Then v's honest play on
  [s, b] is v followed by y_v's honest play at b (it avoids v: v ∉ T_H). □
- Lemma READY (step (A) of R82 at an arbitrary state). If v ∈ E_b, y_v ∈ S^H_t, then v is arena-ready at t.
  Proof. If σ_t(v) ≠ y_v, v switches to y_v at some t′ ∈ [t, b); by (SW), Ξ-SUCC: Ξ_{t′}(y_v) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v); y_v ∈ S^H_t gives
  Ξ_t(y_v) = Ξ_{t′}(y_v) ▷ Ξ_t(σ_t v), i.e. (v, y_v) ∈ Iσ_t. □
- Corollary SINK-OFF. Every W-sink and every H-sink at t is off target (σ_t(v) ≠ y_v); every H-sink is arena-ready.
  Proof. W-sink v with σ_t(v) = y_v: ready, so W-STICK (with CHAIN) gives σ = y_v on [t, b] and v's W-play on [t, b] is v followed by y_v's
  (constant, avoids v): v ∈ S^W_t, against v ∈ U^W_t. H-sink: H-STICK with s = t gives v ∈ S^H_t, against v ∈ U^H_t. Readiness: CHAIN + READY. □
- Theorem SINK-STEP. Let t ∈ [a, b) and v ∈ E_b with σ_t(v) ≠ y_v = σ_{t+1}(v) (v switches at t to its target). If jW(v) ∉ U^W_t or
  jH(v) ∉ U^H_t, this is v's last switch in [a, b]. Every arena-ready W-sink at t switches at t to its target. Moreover
  W-GROW(t) ⇔ some W-sink at t is arena-ready ⇔ some W-sink at t switches at t; and H-GROW(t) ⇔ some H-sink at t switches at t.
  Proof. Last switch: by CHAIN, y_v ∈ S^W_t (resp. S^H_t); v is arena-ready at t + 1 (σ_{t+1}(v) = y_v), so W-STICK at t + 1 (resp.
  H-STICK with s = t + 1) gives σ = y_v on [t + 1, b]. Ready W-sinks: W-STICK and SINK-OFF. W-GROW(t) ⇒ ready W-sink: take x ∈ E_b ∩
  S^W_{t+1} ∖ S^W_t and walk x, jW(x), jW(jW(x)), … while the vertex is in U^W_t; each such vertex is in S^W_{t+1} (a suffix of a play
  constant on [t + 1, b]); the walk has no repeats, so it stops at a W-sink x′ ∈ S^W_{t+1} ∖ S^W_t. Then σ_{t+1}(x′) = y_{x′} (first step of
  its W-play) ≠ σ_t(x′) (SINK-OFF), and (SW) puts y_{x′} in A(t, x′). Conversely a ready W-sink is in S^W_{t+1} ∖ S^W_t (W-STICK). H: the
  same walk along jH; the H-sink found switches at t to its target; conversely an H-sink switching at t to its target is in S^H_{t+1}
  (H-STICK). □
- Corollary (SEG-LAST without (H4′_rel), conditional). If at every t ∈ [a, b) W-GROW(t) or H-GROW(t) holds, then every transition of [a, b]
  is some Even vertex's last switch in [a, b] (CONJECTURE SEG-LAST holds on [a, b]), and b − a ≤ the number of vertices of E_b that switch
  in [a, b] ≤ |E_b| ≤ n − 1. If W-GROW holds at every t, also b − a ≤ |U^W_a|.
- Containment. (i) Under (H4′_rel), box 26 §7 finds at every t a FRONTIER vertex v (off target, y_v ∈ S^W_t ∩ S^H_t); it is a W-sink
  (v ∈ U^W_t as σ_t(v) ≠ y_v; jW(v) lies on y_v's W-play, so in S^W_t) and arena-ready (READY): W-GROW(t). So the Corollary contains
  Theorem LAST-STEP. In fact a frontier vertex is exactly a vertex that is both a W-sink and an H-sink. (ii) If K-ARENA holds at t (box 26
  §8), K-REDUCTION gives K ⊆ S_{t+1} and some v ∈ K off target, so v ∈ (S^W_{t+1} ∖ S^W_t) ∩ E_b: W-GROW(t). So the Corollary contains
  Theorem K-REDUCTION. (iii) W-GROW is strictly weaker than both: on karena_kill_n71 at t = 0 (K-ARENA and (H4′_rel) fail, no frontier
  vertex) vertex 35 is a ready W-sink (σ_0(35) = 46, y = 50; jW(35) = 50 is W-settled from 0 but H-settled only from 1, which is why
  box 26's WX-ARENA, phrased on N_t, missed it); 35 switches at 0 for the last time.
- So: SEG-LAST without (H4′_rel) is REDUCED to CONJECTURE SINK-GROW («in a REL-admissible segment with GEN_W, at every transition the
  W-settled part or the H-settled part of E_b grows»). GEN_W is still used (W-STICK). W-GROW alone and H-GROW alone are DEAD (§4).
  SINK-GROW also gives b − a ≤ |U^W_a| + |U^H_a| ≤ 2|E_b|, and (with SINK-STEP) SEG-LAST, so b − a ≤ |E_b| ≤ n − 1.

## 3. DATA (lay/wsink.py; WSOFF/HSOFF = SINK-OFF, HSR = READY at H-sinks, WSL = W-STICK, WSR = W-GROW, SS = neither W-GROW nor H-GROW
## by a sink switching to target; MUT=1 takes the sinks of box 26's N_t instead of U^W_t and must bite)
| corpus | segments | steps | sink-lemma failures (WSOFF, HSOFF, HSR, WSL) | W-GROW fails (WSR_V) | H-GROW fails | steps with a frontier vertex (both-sink) | W-sinks / ready |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all default starts (lay/wsink_alt.txt) | 907 | 4,478 | 0 | 0 | 0 | 4,478 | 7,006 / 6,811 |
| alt_all pinned starts (lay/wsink_alt_start.txt) | 1,249 | 5,384 | 0 | 0 | 0 | 5,384 | 8,622 / 8,208 |
| lib41 (lay/wsink_lib41.txt) | 978 | 4,241 | 0 | 0 | 0 | 4,241 | 6,245 / 6,018 |
| karena_kill_n71 | 2 | 5 | 0 | 0 | 0 | 4 | 6 / 6 |
| cycset_kill_n60 | 1 | 4 | 0 | 0 | 0 | 3 | 5 / 5 |
| setstep_kill_n71 | 1 | 3 | 0 | 0 | 0 | 1 | 3 / 3 |
| grun/out/lwp_a (start pinned) | 3 | 23 | 0 | 0 | 0 | 23 | 31 / 31 |
- MUT=1 bites on all three kill pins (WSR FAIL: 1, 1, 2 steps): exactly the steps with no frontier vertex.
- In the library a frontier vertex exists at every step (box 26 FR_V = 0), so W-GROW is new only on the climb instances; ~3-5 % of W-sinks
  are not ready, but never all of them at one step.
- How often the new hypothesis holds: at 100 % of the 14,103 library steps and of the 12 kill-pin steps; (H4′_rel) fails in 10 library
  segments and on all three pins' first segments.

## 4. Kill searches (lay/wclimb.py; mutations as lwp/xclimb.py)
- W-GROW is DEAD (DEAD.md box 27): from karena_kill_n71 (score: steps with no frontier vertex + unready W-sinks), step 10,666, found
  lay/instances/wgrow_kill_n90.pg (n 90, sha1 f9a7ef09…; .start = S3 start written out, sha1 a4ead4de…). Segment [0, 3], t = 1: W-sinks 37
  and 57, both σ_1 = 1 with target 5; 5 is W-settled from 0, H-settled from 2; (37, 5), (57, 5) not improving at 1, improving at 2, where
  both switch for the last time. Two engines (n5b SPEC state sequence identical; improving sets identical at t = 0, 1, 2); W-plays
  recomputed from (σ_t, τ). At t = 1 the H-sink 55 switches 40 → 48 = its target (H-GROW holds), 43 switches 37 → 70 (last); SEG-LAST holds.
- So the W-frame alone does not carry SEG-LAST: an unready W-sink waits for its target's HONEST value, exactly the case of §5 first bullet.
- H-GROW is DEAD (DEAD.md box 27): OBJ=H (kill = H-GROW failure) from cycset_kill_n60, step 1,208: lay/instances/hgrow_kill_n89.pg (n 89,
  sha1 998a4a5e…; .start sha1 5895810a…). Segment [1, 8], 7 steps, H-GROW fails at t = 1..6, a frontier vertex at NO step:
  | t | ready W-sinks (all switch, last) | H-sinks (σ, target, jW) | other switchers |
  | --- | --- | --- | --- |
  | 1 | 38, 66, 70 | 1, 46, 73 (27, 23, 34): stay | none |
  | 2-6 | 49; 64; 77, 78; 22; 28, 33 | the same three: stay | none |
  | 7 | 4, 34, 62, 80 | 1, 46, 73 switch to 23 (last) | 55 (last) |
  A W-frame snake settles one W-sink per step; the H-sinks' W-chains end at 34, which settles only at t = 7. Two engines (n5b state
  sequence identical; σ̄ maps and improving sets equal n5b's at all 14 states).
- The two kills are dual: a W-sink can wait for its target's HONEST value (wgrow_kill_n90), an H-sink can wait for its W-chain
  (hgrow_kill_n89). CONJECTURE SINK-GROW says the frames never wait on each other at the same step. SINK-GROW climbs (OBJ=S: kill = SINK-GROW,
  SEG-LAST or sink-lemma failure; shaping: W-/H-GROW failures and 100 // (1 + support), support = ready W-sinks + H-sinks switching to
  target) from hgrow_kill_n89 (two seeds), wgrow_kill_n90, karena_kill_n71: results below.

## 5. Where a proof of W-GROW stands (READING; OPEN)
- An unready W-sink w at t: y_w ∈ S^W_t, and by READY y_w ∉ S^H_t, so jH(w) ∈ U^H_t; and (SW) at w's final switch t_w > t forces
  Ξ_{t_w}(y_w) ▷ Ξ_t(y_w): y_w's honest value must still rise strictly, which goes through its H-chain (Odd vertices of RO_b and Even
  vertices of T are fixed, so Ξ_s(y_w) is a strictly monotone function of Ξ_s(jH(w))).
- The H-chain from jH(w) ends at an H-sink h (H-chains have no repeats), which is off target and ready (SINK-OFF). If h is also a W-sink, it
  is a frontier vertex and W-GROW holds. Otherwise jW(h) ∈ U^W_t and the W-chain from h ends at another W-sink. So W-GROW fails at t only
  if this zig-zag (W-sink → H-chain → H-sink → W-chain → W-sink → …) closes into a cycle on which every W-sink is unready and every
  H-sink is passed over by S4a in favour of a W-better arena edge. That is box 26's J_b-cycle obstruction in its sharpest form; nothing proved
  here excludes it.
- A time-only argument cannot close it: with L(x) the last switch of x, the lemmas give L(x) ≤ max(f^W(jW x), f^H(jH x)) and
  f^W(x) = max(L(x) + 1, f^W(jW x)) (f^W, f^H the first settled states), the recursion of R82's depth; a step t with no last switch then
  forces a jW/jH-cycle of vertices with L > t, and the recursion allows it.
