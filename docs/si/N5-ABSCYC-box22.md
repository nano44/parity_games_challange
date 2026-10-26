# N5-ABSCYC (box 22): gap (i) closes in the cyclic abstract model. Each vertex's play is final from step d*(v), its depth in the FINAL forest, so the run is fixed within n steps (under genericity)
L-SI successor 18 (Opus 5.5; D18, Lead reading L40). Lead's GO 17:19Z, queue item 2: «Prove CONJECTURE FINAL-EACH (gap (i), cycles in the
abstract model), or record the obstruction with its instance». Working note, unrefereed; not frozen. Not a TARGET.md claim; G-N5-TIME OPEN.
Labels: PROVED (lane, unrefereed; in the MODEL only) / CONJECTURE / OPEN / DATA / READING.
Tools: experiments/si/root/absdepth.py (uses abscyc.py's model code unchanged). Logs: experiments/si/root/logs/absdepth_*.txt.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | the model (P-N5-GCX-box21 §4, frozen 5a91bebb; GCX note §8), and GEN | definitions |
| §2 | Facts MONO, MONO-SUCC (model, already in the packet), N-MONO (new, one line) | PROVED (model) |
| §2 | Theorem ABS-DEPTH: under GEN, every v has its final play at every state t ≥ d*(v); the run is fixed after ≤ max_v d*(v) ≤ n steps | PROVED (model, cyclic, GEN) |
| §3 | without GEN the per-vertex statement is false (instance, n = 3); the step bound held in all data | DATA + CONJECTURE ABS-DEPTH-TIE |
| §4 | what it gives for N5 (the lift) and what it does not | READING |
| §5 | FINAL-EACH: no longer needed for the bound; still unproved | CONJECTURE (kept) |

## 1. The model (as P-N5-GCX-box21 §4 and N5-GCX-box21.md §8; restated, nothing changed)
Non-terminals V (|V| = n), terminals t with constants h(t) ≤ T(t); weights w(v); successors succ(v) ≠ ∅ among V ∪ terminals, any digraph
(cycles allowed). A strategy s picks s(v) ∈ succ(v). It is VALID if every play reaches a terminal; then M_s(v) := Σ_{u on v's play} w(u) + h(end)
and N_s(v) := the same with T. Values lie in a totally ordered abelian group. A STEP from a valid s: arena Al_s(v) := {s(v)} ∪ {y ∈ succ(v) :
M_s(y) > M_s(s(v))} (M_s(t) := h(t), N_s(t) := T(t)). s′ := a valid strategy using arena edges only, whose N is pointwise maximal among such
strategies. The model ASSUMES one exists; abscyc.py skips games where it does not (NOPT). Among several, a deterministic rule picks one
(abscyc.py: most agreement with s). The run s_0, s_1, … starts from a valid s_0. play_t(v) := v's play under s_t (its non-terminals and its
terminal), s* := the fixed point (§2), d*(v) := the number of non-terminals on v's play under s*.
- GEN (genericity): for every v, distinct plays from v (simple paths from v to a terminal) have distinct N-values.
  In the random games of abscyc.py (weights ±2^i, terminal values up to 2^{2n}) GEN failed in 0 of 9,635 runs (§3). In N5 the analogue
  fails exactly at κ / W ties (N5 has ties; RESULTS R61 (f)'s tie_q and L-NEW's TIE_c).

## 2. Facts and Theorem ABS-DEPTH (PROVED, in the model)
- (MONO) M_{t+1} ⪰ M_t pointwise. For every u, M_t(u) ≤ w(u) + M_t(s_{t+1}(u)): equality if s_{t+1}(u) = s_t(u), and strict otherwise by the
  arena. Sum along u's s_{t+1}-play, which is finite (valid), to its terminal. (Packet §4 remark.)
- (TERM) The run reaches a fixed point s*. At a switched vertex u, M_{t+1}(u) = w(u) + M_{t+1}(s_{t+1}u) ≥ w(u) + M_t(s_{t+1}u) > M_t(u). So Σ_v M_t(v)
  strictly increases while the strategy changes, and there are finitely many strategies.
- (MONO-SUCC) M_t(s_t v) is non-decreasing in t. (Packet §4 remark: kept, M_{t+1}(s_t v) ≥ M_t(s_t v); switched, M_{t+1}(y) ≥ M_t(y) > M_t(s_t v).)
- (N-MONO, new) N_{t+1} ⪰ N_t pointwise, for every t ≥ 0; hence N_t ⪯ N* := N_{s*} for every t. Proof: s_t is valid and uses only arena
  edges of Al_{s_t} (its own choices), so it is a candidate in the step from s_t, and s_{t+1}'s N is pointwise maximal among the candidates. □
Theorem ABS-DEPTH (PROVED in the cyclic model, under GEN). For every v and every t ≥ d*(v): play_t(v) = play*(v). Hence s_t = s* for t ≥ max_v
d*(v), and the run takes at most max_v d*(v) ≤ n steps.
Proof. Induction on d := d*(v). Let y* := s*(v). Either y* is a terminal (d = 1), or y* ∈ V with d*(y*) = d − 1 and, by induction, play_t(y*) =
play*(y*) for every t ≥ d − 1. In both cases M_t(y*) = M*(y*) and N_t(y*) = N*(y*) for every t ≥ d − 1 (for a terminal, for every t).
- (A) y* ∈ Al_{s_t}(v) for every t ≥ d − 1. If s_t(v) = y*, it is the current choice. Otherwise suppose M_t(y*) ≤ M_t(s_t v). v takes y* at some
  later transition t′ → t′ + 1 with t′ ≥ t (s*(v) = y*). That needs M_{t′}(y*) > M_{t′}(s_{t′} v). But M_{t′}(y*) = M*(y*) = M_t(y*) ≤ M_t(s_t v) ≤
  M_{t′}(s_{t′} v) by MONO-SUCC, a contradiction.
- (B) Let t ≥ d − 1 and s′ := s_{t+1} with v's choice replaced by y*. y*'s play under s_{t+1} is play*(y*) (t + 1 ≥ d − 1), and it does not contain v,
  because play*(v) = v · play*(y*) is a simple play. So s′ is valid: plays not through v are unchanged, and plays through v continue along
  play*(y*). s′ uses only edges of Al_{s_t}: its choices off v are s_{t+1}'s, and its choice at v is y*, by (A). By pointwise maximality,
  N_{t+1}(v) ≥ N_{s′}(v) = w(v) + N_{s′}(y*) = w(v) + N*(y*) = N*(v).
- With N-MONO, N_{t+1}(v) = N*(v) for every t ≥ d − 1, i.e. N_t(v) = N*(v) for every t ≥ d. play_t(v) and play*(v) are plays from v with equal N, so
  by GEN they are equal. □
- Remarks. (i) The induction runs on the FINAL forest of s*, not on the graph. So it needs no acyclicity, and it never looks at a vertex's
  current successors. That is how it avoids the DEAD box 21b obstruction (changes on the plays of non-chosen, not-yet-viable successors).
  (ii) It reproves P-N5-GCX's ABS-HEIGHT (acyclic) under GEN with the sharper bound max d* ≤ height. The bound is sharp: N5-GCX-box21.md §8's
  climbs reach exactly n steps for n = 5, 6, 7 (so max d* = n there). (iii) Only (A) uses M; (B) and the conclusion use N. The roles match
  S4a: M = the honest frame Ξ (the arena), N = the W-frame (the optimum).
- DATA (absdepth.py; logs/absdepth_gen_n456_s1.txt, absdepth_gen_n78_s2.txt): 9,635 runs (n = 4-8, abscyc.py's random games), 50,906
  vertices, DEPTH_V = NDEPTH_V = N_DROP = M_DROP = 0, GEN held in every run. Control MUT=1 (d* − 1 in place of d*): DEPTH_V 1,938 of 14,217
  vertices (n = 4-6, seed 1).
- Extremal runs: abscyc.py --climb 20000 N 1 (N = 5, 6) reaches 5 and 6 steps. The final forests are single paths, d* = (2, 4, 5, 1, 3) and
  (6, 5, 1, 3, 2, 4), GEN holds, 0 violations: the bound max d* is attained exactly.

## 3. Without GEN (DATA; CONJECTURE ABS-DEPTH-TIE)
- The per-vertex statement is FALSE without GEN. Instance (absdepth.py --tie, pinned): non-terminals 0, 1, 2; terminals t3, t4, t5
  (indices 3, 4, 5) with h = (−1, 1, −1), T = (0, 1, 1); w = (−1, 1, 1); succ(0) = {1, t3}, succ(1) = {0, 2, t5}, succ(2) = {0, t4, t5}; start
  (t3, t5, 0); run (t3, t5, 0) → (1, t5, 0) → (1, 2, t4). Vertex 2 has d*(2) = 1 (final play 2 → t4, N = 2). At state 1 it holds 2 → 0 → 1 → t5,
  also N = 2. So N settled at step 1 (as (B) shows, given its premise), but the play did not. GEN fails.
- The step bound survived: with values in {−2..2} (SMALL=1; logs/absdepth_small_n4567_s3.txt), 11,326 runs (n = 4-7), 46 non-GEN runs,
  7 per-vertex failures (all in non-GEN runs), and 0 runs longer than max d* (steps_gt_maxfinaldepth = 0).
- CONJECTURE ABS-DEPTH-TIE: under abscyc.py's tie rule (most agreement with the current strategy), the run is fixed within max_v d*(v) steps
  without GEN. Not attempted. The acyclic tie lemma ABS-TIE (packet §4) gives Σ deg along paths for any rule.

## 4. READING: what this gives for N5, and what it does not
- In the packet's reading (P-N5-GCX-box21 §5, not claimed): inside a PURE global C-interval, once A has frozen (≤ |A_a| − 1 steps, FREEZE-A
  (b), P-N5-ROOT, in review), S4a acts on U_c as the model's step. The gates are terminals with h_u = M(σ̄ u) + wt(u) and T_u = h_u + Δ(u),
  M = Ξ's (M, ℓ), N = W's. Under that reading and GEN (no κ / W ties among plays), ABS-DEPTH bounds the rest of a pure C-interval by
  max d* ≤ |U_c| steps after A freezes. So a pure C-interval [a, b] holds no switch in U_c at index ≥ (|A_a| − 1) + |U_c| < 2n. That is
  WEAKER than UL_C (index ≥ |U_c| − 1) but polynomial. Used as UL-RED's premise it gives packet §3's bounds with n − 1 replaced by 2n, for runs
  whose C-intervals are all pure. L-RED 22's R91 kill (reader_L) is in an IMPURE interval, which this does not touch.
- Gaps left for the lift, each named: (L1) the identification itself (READING, packet §5: the arena is Iσ; Even's optimum over all
  strategies equals the optimum over valid ones for in-phase steps, because an optimum closing another cycle would change λ and end the
  phase; W's play beyond a gate follows τ; each to be written as a lemma). (L2) GEN versus N5's tie rules (§3; CONJECTURE ABS-DEPTH-TIE).
  (L3) impure intervals (gap (iv); R91's reader_L shows UL_C fails there). (L4) the number of C-cuts K(S) (P-N5-GCX §3), unbounded.

## 5. FINAL-EACH
CONJECTURE FINAL-EACH (every transition with a change holds some vertex's final change) is not implied by ABS-DEPTH and is not needed for
the bound any more. ABS-DEPTH gives ABS-CYC (≤ n steps) under GEN. FINAL-EACH stays a CONJECTURE with its data (P-N5-GCX §5); I did not
pursue it.
