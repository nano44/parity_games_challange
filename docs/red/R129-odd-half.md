# R129: the Odd half of P-N5-CUT (O* and B*'s τ-part). Super-linear: the dual of R124's bidirectional chain gives O* = 2K(m − 1) τ-changes inside one λ^U-run and 2K(m + 1) inside one Ξ λ-run, 1128 / 1176 at n = 294 (≈ n²/77), fallback-free. ≥ n² is not reached. By R111's exact mirror, O* ≥ n² on G IS a λ-run with > n² σ-changes on G^d, so R124 §2 and R125 §3 (mirrored: σ-stability of a reused Odd gate) are the exact obstruction. DATA (two engines, Oink) + READING
L-RED successor 31 (Opus 5.5; D1/D18). Lead 2026-10-30 01:01Z: "Next box, R129: the Odd half. Try to make τ-changing transitions per
λ-run (inside B*) or per λ^U-run (O*) super-linear, and if possible ≥ n², on a growing family ... Use R125's τ-tick gate obstruction
(τ-stability) as the starting point: either it blocks this too, so state why exactly, or it can be circumvented. Two engines; check
faithfulness against the packet's definitions." Packet: l-si 2678f6c6, docs/si/P-N5-CUT-box43.md §8 (read only). Written 2026-10-30
from 01:05Z (date -u). Labels: DATA / READING / OPEN. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. Counter (span/ostar.py, sha1 shown in the commit), from P-N5-CUT §8's definitions
- O* := max over λ^U-runs R′ of the transitions t -> t + 1 with t, t + 1 ∈ R′ at which τ changes. λ^U = the cycle-node map of Odd's
  valuation on G^d.
- TB* := max over λ-runs R (Ξ's cycle-node map) of the τ-changing transitions inside R: the τ part of B*. FB* := Even fallbacks
  inside R: B*'s other part.
- Engine 1: L-COMP's n5b SPEC trace with n5b's SpecSI on G and on G^d.
- Engine 2: L-NEW n5x trace (L-SI si.py valuations), O* and TB* recomputed independently (inline script, same definitions).

## 2. DATA
| instance | n | iterations | τ-changes | Ξ λ-runs | λ^U-runs | O* | TB* | FB* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ctl/instances/d_runquad_K8_m30_n192 (R111: dual of R106's mkr) | 192 | 264 | 264 | 1 | 2 | 263 | 264 | 0 |
| dual of span/instances/bidir_K8_m32 (ctl/dualize.py) | 198 | 528 | 528 | 1 | 33 | 496 | 528 | 0 |
| span/instances/dbidir_K12_m48 (dual of mkrb.py 12 48) | 294 | 1176 | 1176 | 1 | 49 | 1128 | 1176 | 0 |
| control: seg/instances/runquad_K8_m30_n192 (Even side) | 192 | 264 | 0 | 2 | 1 | 0 | 0 | 0 |
- Fits:
  - O* = 2K(m − 1) (the longest λ^U-run, as R124's longest λ-run);
  - TB* = 2K(m + 1) (σ never changes, so the whole run is ONE Ξ λ-run and every transition is a τ-change).
- With m = 4K: O* ≈ n²/77. Super-linear in n; not ≥ n².
- Engine 2 on dbidir_K12_m48: iterations 1176, τ-changes 1176, O* 1128, TB* 1176 (= engine 1).
- Pin experiments/red/span/instances/dbidir_K12_m48.pg (sha1 547280177c9e0946d0b25acbbfdfa9f8928ed69b), .start
  (3b7bb166f7a088cd20bfe2bd4843582a194e4446). vrun_dbidir_K12_m48.txt: n5b SPEC 1176 iterations, 0 fallbacks; n5.py 1176, 0; state
  sequences identical (xeng.py); both solutions Oink zlk OK, strategies verified.

## 3. READING: why ≥ n² is the Even problem again (the exact obstruction)
- R111 (DATA + mirror checked): on G^d, N5's run is the mirror of its run on G, state by state. σ and τ swap, and λ and λ^U swap.
- So O*(G) = max over λ-runs of G^d of the σ-changing transitions, and TB*(G) = max over λ^U-runs of G^d of the σ-changing ones.
- An O* ≥ n² family is therefore exactly an Even-side λ-run with ≥ n² σ-changing transitions on G^d, i.e. RUN-QUAD's problem (R123
  §3, R124). Its obstruction is the one already found, mirrored:
  - two-factor clocks give ≤ w·n²/(4ab) (R124 §2; here w = 2, a ≈ 12, b = 3: n²/72, measured n²/77);
  - a third factor needs a REUSED waiting gate. On the Odd side that is a gate at an Even vertex of G whose τ-side signal must read the
    previous Odd hop. By R125 §3 mirrored, Odd's best reply from the signal route reaches the honest route's continuation plus the
    reader's marker, so the gate is never σ-STABLE: Even's S4a takes the honest option at once (mirror of mk3f's collapse at
    transitions 0-1).
- R125's τ-tick obstruction does not block super-LINEAR O*: a dual clock needs no gate that the other side must hold. The τ-changes
  are Odd's own improving moves.
- Mixing sides does not add. Uncoupled Even and Odd clocks run in PARALLEL (R111 §1, union.py: runquad_K3 ⊎ d_runquad_K8 = max, not
  sum). A coupled clock is R112/R113's problem; R113 §2 shows a leapfrog chain cannot follow cross-released sources.

## 4. For the packet (one line each)
- [P-ODD] O* and B*'s τ part are Θ(n²) on dbidir (≈ n²/77); polynomial; the reduction's O* term is not the weak point on known
  families.
- A super-polynomial O* is a super-polynomial N5 run (O* ≤ T), so, as for every premise, only the exponent is extra content.

## DONE / FINDINGS / NEEDS
- DONE: span/ostar.py; engine-2 recount; pin dbidir_K12_m48 + vrun (two engines, Oink); this note; R128 sanity line.
- FINDINGS:
  1. DATA: O* = 2K(m − 1), TB* = 2K(m + 1) on dual bidir (1128 / 1176 at n 294), fallback-free; super-linear, ≈ n²/77.
  2. READING: O* ≥ n² on G ⇔ an Even λ-run with ≥ n² σ-changes on G^d (R111 mirror). The obstruction is R124/R125 mirrored (σ-stability
     of a reused Odd-side gate).
  3. READING: R125's τ-stability does not block super-linear O*: dual clocks need no cross-held gate.
- NEEDS: none from the owner.
