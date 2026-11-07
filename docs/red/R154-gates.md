# R154: two (or k) independently scheduled Ξ supplies ADD, they do not multiply, through Odd min-gates. PROVED (lane), Lemma GATE-r: an Even selector h whose options ℓ_j are Odd gates ℓ_j → {λ_j, S_a(j)} with STATIC branches (Ξ(λ_j), W(ℓ_j) constant) switches at most r times in a τ-stretch, r = the number of distinct gate signals S_a, however often the signals rise. Hence R148 §3's gated shared ladder (one ladder top T gating every engine step, condition G2) runs ONE climb step, not K·m. DATA: on the real quadratic supply obs_K12_m24 (observer Ξ rising 301 times in one 324-transition W-run) an 8-level selector gated by the observer jumps l1 → l8 in ONE switch (sgate_K8); the abstract selector with adversarial signals has max switches exactly r (exhaustive, K ≤ 6, r ≤ 3). The multiplication must come from DYNAMIC branches (Ξ or W changing at the λ_j), i.e. from more Ξ-changes or W-changes, which is the R95 / R* residual again. No super-quadratic W-run
L-RED successor 36 (Opus 5.5; D1/D18). Lead 2026-10-31 03:04Z: «R154 … build two (then k) INDEPENDENTLY scheduled leapfrog Ξ supplies, two
observer-like vertices with coprime or nested periods, feeding gates of one even-c tie DAG. Score XICH at one vertex in ONE W-run against n,
and the W-run length; this is R*/XI-CH-POLY directly. Two supplies whose rounds multiply (not add) would be the first super-quadratic W-run.
If they only add, give the exact obstruction (e.g. Lemma ADD for shared vs disjoint supplies) with the instance that blocks it.» Written
2026-10-31 from 04:10Z (date -u).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - docs/red/R148-hxs.md §2-§3 (the gated shared ladder design, conditions G1-G4);
  - red/span/mkrw.py and red/mix/obs2.py docstrings (the observer supply);
  - this lane's R152 / R153 (XI-PAY, SW-XI).

## 1. Where the multiplication has to happen (READING)
- R148 §3: a cubic W-run needs about K·m engine steps, each followed by an L-long ladder wave. The ladder is shared, so the engine's
  next step must WAIT for the ladder top T: «each reactor step r_j → r_(j+1) must ALSO read the ladder top T, through an Odd
  q_(j+1) → {T, r_j} whose minimum caps the improvement of r_(j+1) until T has risen» (G2).
- With two supplies (the brief), the engine step is a selector driven by two signals with different periods. Either way the core
  object is an Even vertex h climbing through options whose improvement is capped by a shared signal through Odd minima. §2 shows that
  object climbs at most r steps for r signals.
- The ladder bottom has the same shape. S4a picks by W (ARENA-MAX), so a wave runs up the ladder only when the two rails' bottoms
  leapfrog in W. wlev/wch.py: the max number of W-order flips between two successors of one Even vertex in one W-run is 16 (sbq2_K8_m16,
  latew_K8_m32), 24 (obs_K12_m24), 6 (cedge_n32) and 4 (tie_n32), all linear. A single vertex's W changes up to 301 times (obs_K12_m24,
  Even 247), but that is one vertex rising, not two alternating.

## 2. Lemma GATE-r (PROVED, lane; L-RED successor 36)
- Setting: a τ-stretch of an N5 run. Even h has successors ℓ_1, …, ℓ_K. Each ℓ_j is Odd with exactly two successors, λ_j (= τ(ℓ_j)) and
  a gate signal S_(a(j)), a(j) ∈ {1, …, r}.
- Hypotheses:
  - (H1) Λ_j := Ξ(λ_j) is constant on the stretch;
  - (H2) W(ℓ_j) =: Ω_j is constant and the Ω_j are pairwise distinct;
  - (H3) no Ξ- or W-play from ℓ_j, λ_j or S_a passes h or ℓ_j again.
  - Then Ξ_k(ℓ_j) = ℓ_j ⊕ min(Λ_j, Ξ_k(S_(a(j)))): Odd's S1 choice is the minimum, ⊕ is monotone, and (H3) excludes cycles through ℓ_j.
    h's step-2 choice is the Ω-maximum of its arena {σ(h)} ∪ Iσ(h) (ARENA-MAX with (H2), (H3)).
- Statement. h switches at most r times in the stretch.
- Proof.
  - Write ξ_k(j) := min(Λ_j, Ξ_k(S_(a(j)))), so Ξ_k(ℓ_j) = ℓ_j ⊕ ξ_k(j). All ℓ_j have the same irrelevant priority, so
    Ξ_k(ℓ_j) ▷ Ξ_k(ℓ_i) ⟺ ξ_k(j) ▷ ξ_k(i). Put X_k := ξ_k(cur_k), cur_k the index of σ_k(h).
  - Landings. Let h switch at k to j1 and later at k′ to j2. Then Ω_(j2) ▷ Ω_(j1): W(h) = h ⊕ Ω(σ(h)) never decreases (the
    Ω-maximum is taken over an arena containing σ(h)), and the Ω are distinct.
  - The landing values ξ at the switch times strictly increase, and ξ is monotone in time because Ξ is ([R15]; R153 SW-XI's chain).
    So X_(k′) ⊵ ξ_k(j1).
  - Suppose a(j1) = a(j2) = a, and put s := Ξ_k(S_a).
  - At k: j1 is improving, so ξ_k(j1) = min(Λ_(j1), s) ▷ X_k; in particular s ▷ X_k.
  - j2 is not in h's arena at k, since otherwise the Ω-maximum would not be j1. So min(Λ_(j2), s) ⊴ X_k ◁ s, hence Λ_(j2) ⊴ X_k.
  - At k′: j2 is improving, so Λ_(j2) ⊵ ξ_(k′)(j2) ▷ X_(k′) ⊵ ξ_k(j1) ▷ X_k ⊵ Λ_(j2). That is a contradiction.
  - So the landings of h lie in pairwise distinct signal groups, and there are at most r of them. □
- Corollary ONE-JUMP (r = 1). With one shared gate signal, h switches at most once, however often the signal rises.
- What the lemma does NOT cover: dynamic branches (Λ_j or Ω_j changing in the stretch). Each branch change is a Ξ- or W-change at λ_j or
  on ℓ_j's τ-path, so the climbs are paid by those changes (SW-XI). That is the residual XI-CH-POLY (R95), or R* if the branch W
  changes.

## 3. DATA
- Abstract model (wlev/gates_abs.py, exhaustive over the branch order Λ, the signal map and the start, signals raised adversarially by DP):
  | K | r = 1 | r = 2 | r = 3 |
  | --- | --- | --- | --- |
  | 3 | 1 | 2 | — |
  | 4 | 1 | 2 | 3 |
  | 5 | 1 | 2 | 3 |
  | 6 | 1 | 2 | — |
  The max is exactly r, so GATE-r is tight.
- N5 instance, one signal: wlev/instances/sgate_K8 (wlev/mkgate1.py on red/xich/instances/obs_K12_m24, priorities rescaled
  p → 4p + (p mod 2); OBS = the Even observer 247, MV = the fixed marker M (vertex 1, Ξ = W = (z, {M}, 1) constant); 8 levels with odd
  markers just above 701, 695, …, 659, the range of the observer's second-most-relevant vertex):
  - «SGATE sgate_K8.pg n 297 iters 324 fallbacks 0 wruns 1 maxL 324 XICH(OBS) 301 signals [247] tau-changes 0»;
  - «switch at 3: l1 -> l8; improving at k: [2, 3, 4, 5, 6, 7, 8]»; «h switches 1 levels 8».
  - The original run is untouched: still one 324-transition W-run, no τ change. The observer rises 301 times, and h climbs ONCE: every
    level opens at the same transition and ARENA-MAX takes the top.
  - xeng: state sequences identical. Oink 8fbf0a7 --zlk + verify: OK.
- N5 instance, two signals: wlev/instances/sgate2_K12 (OBS = 247 and Odd 46 (24 Ξ-changes), round robin; 12 levels): «h switches 1
  levels 12», «switch at 0: l1 -> l12». So it is ≤ 2, as GATE-r says. xeng identical, Oink OK.

## 4. Consequences (READING)
- Two observer-like supplies with coprime or nested periods feeding Odd min-gates give at most r climbs. Their rises are not reusable,
  because every gate on one signal opens together and S4a's W-optimum skips to the best open option (ARENA-MAX, G3). So the supplies
  ADD. This is the exact obstruction asked for. Instance: sgate_K8 (one signal, 301 rises, 1 climb).
- R148 §3's design needs a fresh gate vertex per engine step (n ≥ K·m gate vertices for K·m steps, so the ladder reuse buys nothing), or
  dynamic branches. Dynamic branches mean Ξ- or W-changes at the λ_j, which is again the R95 residual. The multiplication cannot be
  bought with gates alone.
- This sharpens the earlier walls (R140 ARENA-MAX look-ahead; R144 Lemma ADD for one closure) into a lemma about the GATING mechanism
  itself. A super-quadratic W-run needs a selector whose options' own values move (a nested counter in Λ or Ω), not more signals.

## 5. Pins (experiments/red/check.sh «R154»)
- wlev/pins.sha1 (sgate_K8, sgate2_K12); sgtrace on sgate_K8; xeng and Oink on both; gates_abs.py 4 1 (1) and 4 2 (2).

## DONE / FINDINGS / NEEDS
- DONE: this note; red/wlev/ (wch.py, mkgate1.py, sgtrace.py, gates_abs.py, instances); check.sh «R154». SHA: see the commit.
- FINDINGS:
  - PROVED (lane): GATE-r. A selector with r gate signals and static branches climbs ≤ r times; supplies add.
  - DATA: sgate_K8 (1 climb against 301 signal rises, xeng / Oink OK); abstract max = r exactly.
  - READING: the multiplication needs dynamic branches (a counter in the options' own values), not more signals.
- NEEDS: none.
