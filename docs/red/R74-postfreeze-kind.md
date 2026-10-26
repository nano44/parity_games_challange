# R74: hunting a post-freeze kind change (KIND-MONO content): not found; a reading of why it is hard (L-RED successor 18, box 44 item (1b); Lead 22:56Z / 23:07Z, date -u)
Target: P-N5-KW (docs/si/P-N5-KW-box15.md, sha1 c0b0111f + addendum 8d6bfb3c, pinned trunk d9291be0), Lemma KIND-MONO. Wanted: a
post-freeze kind change, i.e. a vertex of R ∖ {o} whose kind (c_w ∈ π_v) changes at a state ≥ k0 + |R| − 1 of a fallback-free run.
The run must lie in a U3 / U23 stretch with c_w ≻ c_θ. Such an instance exercises KIND-MONO without breaking it (the change must go B → A).
𝒞^1O only. Labels per L40. Nothing here is a running-time bound.

## 0. Result
- **Not found.** The post-freeze kind-change regime stays VACUOUS in my data. No climb, random run or start pair entered it:
  - R73 §2-§3 and §7: lib41, lib41 × 3 start pairs, 7.1 M random runs, 5 climbs from S3;
  - this box: 4 start-pair climbs (genome = game + start pair; 1,856,999 evaluations in all).
- The climbs got close to it:
  - post-freeze parts of U3 / U23 c_w ≻ c_θ runs up to 19 transitions;
  - up to 16 kind-change transitions in a run, all before the freeze.
- §2 is a READING of why the regime is hard to enter (§2.1 uses only FRZ-U). Its conclusion: a post-freeze B → A change needs a W-length cascade on kind-A
  routes that starts late. That is only possible through BAND gates (rank strictly between c_θ and c_w) whose Ξ-improvement arrives
  after the freeze. This is a design target for a construction. It is not a proof that the regime is empty.

## 1. Tools and data
- kmpst18.py (experiments/red/kw/): hill-climb on (#FAIL, post-freeze kind changes, longest post-freeze U3x run part, kind-change
  transitions). Each mutation changes either the game or the start pair (σ_0, τ_0). Trace: ex16.trace. Checker: kw18.analyse (R73 §1).
- Runs (2,700 s each):
  | seed | start game | best (post-freeze kind changes, post-freeze length, kind-change transitions) |
  | --- | --- | --- |
  | 61 | kc18_n24 (R73) | (0, 19, 0); 352,519 evaluations |
  | 62 | kc18_n24 | (0, 19, 0); 459,853 evaluations |
  | 63 | kc18_n24 | (0, 18, 16); 273,933 evaluations |
  | 64 | cascb_witness (REFEREE 11) | (0, 11, 0); 770,694 evaluations |
- 0 FAIL of every R73 check in every evaluated game.

## 2. READING: what a post-freeze B → A change needs
Setting: a run of a U3 / U23 stretch with c_w ≻ c_θ; c_w is even (PAR), so P = A. Post-freeze means a state ≥ k0 + |R| − 1.
1. After the freeze, κ(π_x) = π_x ∩ V_{>c_w} is constant for every x ∈ R (FRZ-U). Take a B → A change of v: v switches from a kind-B a
   to a kind-A z. κ(π_v) is ({v} ∩ V_{>c_w}) ∪ κ(π_a) before the switch and the same with κ(π_z) after it. FRZ-U keeps it constant,
   so κ(π_z) = κ(π_a).
2. With κ(π_z) = κ(π_a):
   - Ξ decides at c_w (in z's honest path set, not in a's). So (v, z) is a gate whenever z is kind A and a is kind B.
   - W ties above c_w and decides by length. c_w is even, so the shorter path to c_w wins.
   - So v switches as soon as W(z)'s length drops below W(a)'s, or z becomes kind A. For the switch to be post-freeze, this must first
     happen at a state ≥ k0 + |R| − 1.
   - "z becomes kind A late" is the same event one step down. So the first post-freeze kind change in a run needs a kind-A vertex z
     whose W-length to c_w SHORTENS at a state ≥ k0 + |R| − 1 (or at the last pre-freeze state).
3. Shortening kind-A routes after the freeze:
   - LEN allows ≤ r − 2 length changes per vertex, so it is not excluded. But a shortening x: b → b′ (both kind A, same κ) must be a
     Ξ-gate.
   - Ξ sees, below c_w, the band vertices (rank in (c_θ, c_w)) on the path before c_w, and then the length to c_θ.
   - If no band vertex differs, the Ξ length order is s_θ·ℓ. If c_θ is even, Ξ and W both prefer shorter. Then the arena contains every
     shortening, each S4a step is one Bellman-Ford round, and the lengths settle within r − 1 rounds of their last trigger.
   - If c_θ is odd, Ξ prefers longer. Then a pure shortening is never a gate.
4. So a late shortening needs a late trigger: a band vertex entering or leaving a kind-A route that makes the shorter edge a Ξ-gate
   only after the freeze. This is the BAND / wake mechanism of R27 (e) and the K-chain.
   - Note: the K-chain itself has c_θ = c_w (its top T is on both cycles), so it is not a U3x stretch, and it cannot be used as is.
5. Construction target (OPEN; for successor 19 or a lane):
   - a U3 / U23 stretch with c_w ≻ c_θ;
   - a kind-A chain whose band vertices make one shorter edge a Ξ-gate only at run index ≥ |R| − 1, e.g. a K-chain-like cascade of
     length ≥ |R| inside the kind-A part;
   - and a kind-B vertex v with an edge to the chain's head, whose W-length the cascade beats only at its end.
   - The difficulty is that the cascade must be longer than |R| − 1 while all its vertices lie in R.

## 3. Dead ends
- Start-pair climbs toward the regime: plateau at a long post-freeze part with 0 kind changes. The obstruction is §2.1-§2.3: without
  a late band trigger, every kind-relevant comparison is settled by the freeze or by the first post-freeze arena optimum.
  Instances: experiments/red/kw/out/kmpst*.pg (scratch, not pinned).

## 4. Not started this box
- (2) DUAL / MIRROR (docs/new/P-N5-DUAL-box43.md, sha1 a51f7c30): Lemma DUAL on my engine; a 𝒞^1O phase from a non-S3 start, or under
  the Odd-first tie rule, exceeding the landed per-phase bounds. Queued for successor 19 (context limit).
