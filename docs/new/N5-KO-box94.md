# N5-KO (box 94): N5 on 𝒞^kO (k fixed). Theorem kO-RED (lane; a composition of landed R54 (e), R61 (d), R89): every run has polynomially many W-runs, so N5 is polynomial on 𝒞^kO iff its W-runs are (iff XI-CH-POLY there, by P-N5-WRUN E1). The per-W-run residual is NOT closed. CONJECTURE NO-REPEAT-kO (σ̄ on the k choice vertices never repeats inside a W-run, SB_F < ∏ deg) is DEAD: gate_K64_n581 ∈ 𝒞^5O has 64 σ̄-changes in one W-run with ∏ deg = 32
L-NEW successor 39 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 18:14Z: «BOX 94 … The target: N5 polynomial on 𝒞^2O, or
𝒞^kO for fixed k, via RUN-SETTLE / HEAD-RED plus landed R61 … Bound σ̄-flips and head Ξ-changes per W-run when only k Odd vertices choose.
Also bound the number of W-runs. Check what landed R47/R61 already give per phase. If it closes, it is a packet: a subclass result,
polynomial by other means, explicitly NOT M4.» Written 2026-10-30 18:25Z-18:27Z (date -u). Working note, unrefereed. Labels: PROVED (lane) /
CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim; it did NOT close, so no packet. G-N5-TIME OPEN.

## 0. Sources and setting
- 𝒞^kO: games with at most k Odd CHOICE vertices o_1, …, o_k (out-degree ≥ 2); every other Odd vertex has one successor. P := ∏_i deg(o_i)
  (≤ n^k). Δ, m_E, n_E as usual.
- Landed (docs/RESULTS.md), quoted:
  - R54 (e) Corollary Φ-kO: «along any N5 run the number of distinct τ's is at most ∏ over the Odd choice vertices o_i of deg(o_i), and the
    run has at most n(n − 1) + ∏_i deg(o_i) phases».
  - R61 (d) Corollary FB-kO (signed conditional on R56 and R58, both landed): «on 𝒞^kO every phase of every N5 run from every start pair has
    N_late ≤ 1 + k·(2n)·k·(2(k − 1)n)^{k−1} and f ≤ 1 + (n − 1)(1 + N_late) = O(k^{k+1}·2^k·n^{k+1})», f = in-phase fallbacks of the phase.
  - R89: «a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of consecutive states of one
    τ-stretch none of whose transitions is an S4c fallback or changes λ_W»; (Lemma FRAME-τ) «no τ repeats in a run»; (Theorem STRETCH-RED)
    «Q := the transitions of S that are an S4c fallback or change λ_W, and Q ≤ fb_S + n(n − 1)(fb_S + 1)», fb_S its S4c fallbacks.
  - SPEC FIX 3 (docs/new/N5-ssi-global.md): «In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ) … Odd falls back only if Iσ = ∅.»
- Lane-level, other lanes (not landed): L-SI successor 34 box 52 (l-si 71d1d0ac, docs/si/N5-HEADS-box52.md §1-§2): Theorem RUN-SETTLE /
  Corollary RUN-COUNT «|F| ≤ E_F + (E_F + 1)(n − 1) = n(E_F + 1) − 1» and Theorem HEAD-RED «E_F ≤ Σ_o SB_F(o) + Σ_c CN_F(c) + Σ_u HXU_F(u)»,
  with events (i) σ̄ changes, (ii) CN switches (Even W-cycle nodes switching), (iii) Ξ changes at upward heads U_k = {σ̄_k(g) : g Odd,
  σ̄_k(g) ≠ τ(g)} ∪ {Ξ-successor of c : λ_W(c) = c}. Its Case 3a uses Claim RG′ and L-LIT T54's LEX-BFS / IDX-MONO (lane).

## 1. Theorem kO-RED (PROVED, lane; a composition of R54 (e), R61 (d), R89 and FIX 3)
- Statement. On 𝒞^kO, every N5 run from every start pair has at most
  NW := P + FB + n(n − 1)(FB + P) W-runs, where FB := (n(n − 1) + P)·(f_k + 1) and f_k := 1 + (n − 1)(1 + N_k),
  N_k := 1 + k·(2n)·k·(2(k − 1)n)^{k−1}; and its number of transitions T satisfies T ≤ (P − 1) + FB + n(n − 1)(FB + P) + NW·L, L := the
  largest |F| of a W-run of the run. For fixed k: NW = O(n^{2k+3}) (k ≥ 2), so N5 is polynomial on 𝒞^kO ⇔ L ≤ p(n) on 𝒞^kO.
- Proof.
  - (a) τ-stretches. τ is determined by its values at o_1, …, o_k, so there are at most P distinct τ; none repeats in a run (FRAME-τ). So the
    run has at most P τ-stretches and at most P − 1 τ-changing transitions.
  - (b) Even fallbacks. A transition that is an S4c fallback with Iσ ≠ ∅ keeps τ (FIX 3). It is either in-phase (both states in one phase) or
    a phase boundary. By R54 (e) there are at most n(n − 1) + P phases, hence at most that many boundaries, and by R61 (d) at most f_k
    in-phase fallbacks per phase. So the run has at most FB such fallbacks. An S4c fallback with Iσ = ∅ changes τ (FIX 3: only Odd moves)
    and is counted in (a).
  - (c) Within a τ-stretch S, every transition is a Q-transition (an S4c fallback, necessarily with Iσ ≠ ∅, or a λ_W change) or lies inside
    one W-run, and the W-runs of S are separated by Q-transitions, so S has at most Q_S + 1 W-runs. STRETCH-RED: Q_S ≤ fb_S + n(n − 1)(fb_S + 1).
    Summing over the ≤ P stretches with Σ_S fb_S ≤ FB: Σ_S Q_S ≤ FB + n(n − 1)(FB + P), and the W-runs number at most P + Σ_S Q_S = NW.
  - (d) T = τ-changing transitions + Σ_S Q_S + Σ_F |F| ≤ (P − 1) + FB + n(n − 1)(FB + P) + NW·L.
  - (e) Orders: P ≤ n^k, f_k = O(n^{k+1}), FB = O(n^{k+1}(n² + n^k)) = O(n^{2k+1}) for k ≥ 2 (O(n⁴) for k = 1), NW = O(n^{2k+3}). □
- Consequences.
  - With P-N5-WRUN (signed by both referees; line L-3): on 𝒞^kO, N5 polynomial ⇔ WRUN-POLY restricted to 𝒞^kO ⇔ XI-CH-POLY on 𝒞^kO ⇔ … (all
    rows E1-E8 read on 𝒞^kO games; their proofs never use the class).
  - With L-SI's RUN-SETTLE / HEAD-RED (lane): N5 polynomial on 𝒞^kO ⇐ per W-run polynomial counts of: σ̄-changes at the k choice vertices
    (only they can change σ̄), CN switches, and Ξ-changes at the heads; the D-heads number at most k at any state (|D_t| ≤ k), the C-heads at
    most |C| ≤ n.
  - k = 1 is consistent with landed R51 (𝒞^1O polynomial): there L ≤ T is polynomial, and kO-RED gives nothing new.
- Status: a REDUCTION of N5 on 𝒞^kO to per-W-run lengths on 𝒞^kO. The packet the Lead asked for needs L ≤ p(n) on 𝒞^kO, which is NOT proved.

## 2. Per W-run on 𝒞^kO: what does not close, with an instance
- The natural finite-alphabet handle: σ̄ restricted to {o_1, …, o_k} takes at most P values. If it never repeated inside a W-run, SB_F ≤ P − 1.
- CONJECTURE NO-REPEAT-kO: inside every W-run of N5 on 𝒞^kO, σ̄|{o_1..o_k} never takes a value twice. DEAD.
  - Instance: experiments/red/usplit/instances/gate_K64_n581.pg with its .start (L-RED, R134 family; box 86's R*_F record). It is in 𝒞^5O
    (choice vertices 4, 79, 154, 230, 573, each of out-degree 2; P = 32; box94/kcount.py). One W-run, |F| = 71, SB_F = 64 > P − 1 = 31;
    vertex 573 changes σ̄ 62 times, 61 of them returns (box90/sbv.py). gate_K16_n197 is also in 𝒞^5O (P = 32): SB_F = 16, vertex 189 14 times.
  - So in 𝒞^5O the σ̄-changes per W-run grow linearly in n (K = 16 → 16, K = 64 → 64, n ≈ 9K) with k and P fixed. Not a kill of polynomiality.
- Obstruction (exact). A σ̄-flip-flop at one choice vertex o between a, b is driven by the order of Ξ(a), Ξ(b) changing back and forth (box 90
  §2 READING; L-SI's FLIP-EV, lane CONJECTURE). With k fixed the alphabet is finite, but the flips are paid by Ξ-changes of o's successors,
  i.e. by per-vertex Ξ-changes again. On gate_K the Ξ-changes at the poisoned targets form a K-step counter (box 86 §4, PCH = K − 1). So
  fixing k bounds the NUMBER of heads (≤ k D-heads) but not how often one head's Ξ changes. The 𝒞^kO restriction removes no part of
  the XI-CH-POLY core; it only removes the W-run count (§1).
- D-heads vs C-heads (DATA, box94/kodata.py on random 𝒞^2O / 𝒞^3O games: n 12-24, 2,200 games, seeds 1-5): runs are short (max |F| 5,
  max iterations 6, max σ̄-changes of one vertex per W-run 2); no information beyond "nothing grows". Recorded only to say random 𝒞^kO games are not informative.

## 3. DATA: W-run lengths in the corpus by k (box94/kcount.py joined with box92/xirun_*.txt; kcount_corpus.txt)
| k (Odd choice vertices) | games | largest |F|/n | instance |
| --- | --- | --- | --- |
| 0 | 18 | 0.26 | new/box51/out/dlc_d2 (n 27, |F| 7) |
| 1 | 176 | 2.01 | si/runlin/instances/runfam_K40 (n 79, |F| 159; 𝒞^1O, polynomial by R51) |
| 2 | 20 | 1.00 | n5-exhaustive/instances/frz1_n24 (|F| 24) |
| 3 | 28 | 1.00 | n5-exhaustive/instances/frz3_n24 (|F| 24) |
| 4 | 23 | 0.67 | red/fbr/instances/fr39_q4_n48 |
| 5 | 27 | 0.48 | red/n3/instances/ret22_n40 (gate_K64_n581, not in this list: 71 / 581) |
| ≥ 6 | 427 | 0.80 | red/n3/instances/run34_n40 |
(719 distinct game files over both lists; |F| maxima from box 92's xirun outputs for both start sets.) The quadratic one-W-run families have many Odd choice vertices: latew_K16_m32
k = 95, fx_K8_m32 k = 32; pftheta34_n32, runfam_K40 and rel2_R2_n82 have k = 1.
- READING. The longest W-runs per n in the corpus are on 𝒞^1O, where N5 is polynomial (R51). On 𝒞^kO, k ≥ 2, no W-run longer than n is known.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box94/kcount.py, kcount_corpus.txt, kodata.py; check.sh section "box 94"; this note.
- FINDINGS:
  1. PROVED (lane; composition of landed R54 (e), R61 (d), R89 STRETCH-RED and SPEC FIX 3) Theorem kO-RED: on 𝒞^kO every run has at most
     NW = P + FB + n(n − 1)(FB + P) = O(n^{2k+3}) W-runs, and T ≤ (P − 1) + FB + n(n − 1)(FB + P) + NW·L. So N5 is polynomial on 𝒞^kO
     (k fixed) iff its W-runs are, iff XI-CH-POLY holds on 𝒞^kO (P-N5-WRUN E1).
  2. NOT closed: per-W-run length on 𝒞^2O / 𝒞^kO. No packet.
  3. DEAD: CONJECTURE NO-REPEAT-kO. gate_K64_n581 ∈ 𝒞^5O, P = 32, has SB_F = 64 in one W-run (one vertex flips 62 times). σ̄-changes per W-run
     grow linearly with k fixed.
  4. Obstruction: fixing k bounds the number of D-heads (≤ k) but not the Ξ-changes of one head; the gate_K heads carry a K-step path-set
     counter. The XI-CH-POLY core is untouched by the class restriction.
  5. DATA: longest W-runs per n are on 𝒞^1O (runfam_K40, 2.01n). For k ≥ 2, max |F|/n ≤ 1.00 in the corpus.
- NEEDS: none from the owner. Lead: if a 𝒞^2O packet is still wanted, the missing lemma is a per-W-run bound on Ξ-changes of the ≤ 2 D-heads
  and the C-heads (HEAD-RED's (iii)) plus σ̄-changes at 2 vertices. L-RED could aim a gate_K-type family at k = 2 (it uses k = 5).
