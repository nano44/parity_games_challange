# R92: QP_c grows linearly on long phases, in ONE class (the LADDER family, D0 and ENT forms)
L-RED successor 22 (Opus 5.5; D14/D15/D18, Lead 16:34Z target (2), 17:31Z order). Written 2026-10-26 ~17:5xZ (date -u). Labels (D18 / L40):
DATA / READING / OPEN.
Target: docs/new/N5-NCONF-box48.md §11-§12 (l-new b9a6568f / 0cc8839a), QP_c := max over cycle nodes c of |⋃_{k ∈ P} D_k ∩ λ^{-1}(c)|.
§12 OPEN (1): "Scaling of max QP_c on long phases with n". The Lead's brief adds: "Look for a long-phase family in which QP_c grows with n.
Disjoint copies do not count; they raise QP, not QP_c."

## 1. Result (DATA, verified; counted with L-NEW's own qp.py, unmodified, trunk = l-new)
Family ladder (experiments/red/ul/mkladder.py k [ent]), n = 3k + 12, L = k.
The phase is the whole run, one phase with no fallback, and it contains an all-gated class.

| instance (experiments/red/ul/instances/) | sha1 game | sha1 start | n | phase len | QP | QP_c (classes) | D0 | ENT | N_ep | NCONF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ladderd0_k12_n48 | c654bf9e… | 674f6eeb… | 48 | 13 | 14 | 14 (1) | 14 | 0 | 1 | 1 |
| ladderd0_k24_n84 | 3ee730b9… | 5522cce1… | 84 | 25 | 26 | 26 (1) | 26 | 0 | 1 | 1 |
| ladderd0_k48_n156 | 2f544269… | 812a3df1… | 156 | 49 | 50 | 50 (1) | 50 | 0 | 1 | 1 |
| ladderent_k12_n48 | 56986308… | 674f6eeb… | 48 | 12 | 14 | 12 (2) | 3 | 11 | 12 | 12 |
| ladderent_k24_n84 | 4423259c… | 5522cce1… | 84 | 24 | 26 | 24 (2) | 3 | 23 | 24 | 24 |
| ladderent_k48_n156 | 8101c924… | 812a3df1… | 156 | 48 | 50 | 48 (2) | 3 | 47 | 48 | 48 |

- So QP_c = k + O(1) ≈ n/3 on a phase of length ≈ n/3: linear in n, within ONE class. These are not disjoint copies: one Bellman-Ford clock
  is read by every gate.
- In the ENT form the gates ENTER D one per tick: D0 = 3, ENT = k − 1. The phase also has N_ep = NCONF = k: σ̄|_Q changes at every
  transition, and every configuration is new.
- Evidence, on all six instances:
  - experiments/red/ul/vrun.sh: n5.py (SPEC) = n5b.py --mode spec iterations, 0 fallbacks.
  - check_sol2 prints "zielonka(oink zlk) OK strategies verified" for both solutions.
  - L-NEW's phrestrict.py (RESTRICT_H on the used-edge game G^P) on k = 12 (both forms) and ent k = 24: XI_V 0, REP_V 0. With MUT=1
    (drop one σ̄-edge) XI_V = 1. The gates' σ̄-edges are USED: the phase is not reproduced without them.

## 2. The construction
- Clock (class B, cycle node b, an Even self-loop): mkreader's Bellman-Ford chain v_0 … v_L. The wave reaches v_L, v_{L−1}, …, v_1 at
  ticks 1, 2, …, L.
- D0 form:
  - Class S (cycle node c_s, the cycle c_s ↔ u1, as in R91 §2) holds x and k + 1 Odd rungs g_0, g_1 … g_k. Each g_j has σ̄ = c_s
    (Odd prefers S's class, which is worse for Even than b) and τ(g_j) = v_{L+1−j}.
  - The gates' even ranks rise with j, above b and below G, so Ξ(x via g_j) rises with j.
  - W(x via g_j) = g_j ⊕ W(v_{L+1−j}): a rung that has received the wave carries G, and the highest such rung wins.
  - So x climbs one rung per tick. Every gate is in D for the whole phase (D0 = k + 2) and each drives one switch of x.
- ENT form: g_j → {q, v_{L+1−j}}, τ = v_{L+1−j}.
  - Before the wave reaches v_{L+1−j}, Odd's best reply is τ itself (the o-level is below q-level), so g_j ∉ D.
  - After it, σ̄(g_j) = q (q is below G), and g_j enters D at tick j. The gates sit in class b with the clock.
- τ is Odd-OPTIMAL in both forms (I_τ = ∅ for the whole phase), because Even's best reply to τ runs q → v_0 → … → G.

## 3. Scope (READING / OPEN)
- What it settles: QP_c is not a bounded parameter on long phases, even per class and even counting only gates that are used. Long-phase
  structure therefore cannot be charged to a constant number of disagreeing Odd vertices per class. §12's data point (10-14 at n = 48)
  scales linearly.
- What it does not settle:
  - These phases are linear (≈ n/3), not super-linear. Long121-type phases (≈ 3n) with QP_c = Θ(n) at the same time are not built here.
    Grafting a ladder onto long121 is the natural next step if the Lead wants it.
  - Nothing here is a lower bound on N5's iterations. The run has n/3 iterations.
- For L-NEW (EPC / NCONF): the ENT form has N_ep = NCONF = k inside ONE fallback-free phase (DATA). Any count of epochs or configurations
  per phase must be at least linear in n.

## Sources opened
- docs/new/N5-NCONF-box48.md (l-new b2a78eb1): §10 (RESTRICT_H, G^P), §11 (QP, Remark QP-D, DUNION, QP_c), §12 (qpcclimb data, OPEN (1)).
- experiments/new/box48/qp.py and phrestrict.py (identical on trunk and l-new; run unmodified).
