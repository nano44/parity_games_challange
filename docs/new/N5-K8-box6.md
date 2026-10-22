# K8: when can N5 follow a switch-best run? (box 6, L-NEW successor 2; GO 23:31Z, written 23:34Z by date -u; DATA and arguments)
Lead brief (1): build a switch-best-type family whose arena-reply changes N5's Odd step reproduces one step back (sb_tauvar.py misses
= 0), or write the exact obstruction. Result: NOT built. The obstruction is K8.

## 1. The exact requirement
Notation: (σ_k) is switch-best's run (σ_{k+1} = optimum of the improvement arena H_{σ_k}, Odd free). b_k = Odd's VJ best reply to σ_k
in G. τ_sb(k) = Odd's optimal strategy in H_{σ_k}.
- (a) Saddle identification: τ_sb(k) = b_{k+1}. Measured EXACTLY on switchbestexp: 20/20, 58/58, 134/134, 286/286 steps (N = 1..4;
  sb_flipback.py). Reason: in H_{σ_k}, Odd's optimal strategy is its best reply to the arena optimum σ_{k+1}, and on the plays
  that matter Odd's options in H_{σ_k} are those of G.
- (b) By the coincidence lemma (N5-dlm-box5.md §7), N5's σ-sequence equals switch-best's for L steps if τ_k = τ_sb(k) = b_{k+1}
  for k < L. This needs τ_0 = b_1 at the start, and at every step
      OddStep(σ_k, b_{k+1}) = b_{k+2}            (*)
  because N5's Odd step answers the OLD σ_k.
- (c) If Odd's restricted step returns its full best reply (OddStep(σ_k, ·) = b_k, the usual case), (*) reads b_k = b_{k+2} for
  all k. So along the whole followed run, Odd's best replies are CONSTANT or ALTERNATE between exactly two strategies.
  Otherwise (*) needs Odd's restricted step to land exactly on a future best reply.
K8. (*) for every k < L (and τ_0 = b_1) is SUFFICIENT for N5 to follow a switch-best run of length L (coincidence lemma).
- It is not necessary: N5's step can match switch-best's while τ ≠ τ_sb (the "S." steps in sb_traj.txt).
- On the data, N5 LEAVES switch-best's path only at steps where (*) has failed (every "-" in sb_traj.txt follows a ".").
- The route via the lemma therefore needs (*). When OddStep(σ_k, ·) is Odd's best reply to σ_k, (*) means b_k = b_{k+2}: the run's
  Odd best replies take at most 2 values, with period ≤ 2.
- A killer that follows switch-best WITHOUT (*) would need N5's step to coincide with switch-best's by other means at every step.
  That happened only on short runs (§2).

## 2. Data
- switchbestexp (sb_flipback.txt):
  - Odd's best replies take 2, 4, 8, 16 values (N = 1..4) and change 1, 4, 10, 24 times.
  - The flip-back b_k = b_{k+2} holds at 0 of 39 changes, and (*) fails at every change (sb_tauvar.txt: misses 1, 4, 10, 24).
  - Friedmann's counter needs Odd's punishments to encode the counter, which is exactly what K8 forbids.
- Random games (sb_flip_rand.py, 2,000 games; sb_flip_rand.txt):
  - Flip-backs exist: 6 of 82 changes. So K8 is a condition, not an impossibility.
  - N5 follows switch-best fully in 1,635 of 2,000 runs, but those runs are short (≤ 4 steps).
- Constant case (Odd's reply fixed = a one-player game for Even): switch-best is then the optimum of a one-player improvement arena.
  - Climb for long runs (sb_oneplayer.py): best 10 steps (n = 16, 3,000 steps) and 16 (n = 40, 2,000 steps), i.e. ≤ n/2
    (sb1p_*.txt).
  - Consistent with box 4: N5 against a fixed optimal τ* on switchallexp takes 2N iterations.
- Two-strategy alternating case: not tested by a dedicated construction. Friedmann's switch-best lower bound (1106.0778 §8) uses
  Odd replies that change with the counter, so it does not fall into this case.

## 3. What a killer along this route must have
A family where switch-best is super-polynomial while Odd's best reply along its run is constant or 2-periodic, and N5's restricted
Odd step reproduces it.
- The constant case is a one-player switch-best question. Data: linear.
- The 2-periodic case would need an exponential switch-best run driven by Even alone, with Odd toggling between two punishments.
- No such family is known to the lane, and none was found.
