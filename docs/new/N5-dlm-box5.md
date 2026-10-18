# N5 vs DLM's distraction (box 5, L-NEW successor 2; GO 22:47Z, written 22:51Z by date -u; DATA and arguments, unrefereed)
Lead brief: build a DLM-distraction module (L-LIT T20 caveat 1; van Dijk-Loho-Maat 2309.02223 p. 15, "distracted by their opponent's
(bad) strategy") from the condition "N5 ≈ SSI iff τ̄ ⊆ A_σ", so that N5 follows an SSI-like path on DLM's own exponential construction.
Measure both tie-break modes.

Implementations used:
- n5.py, SPEC mode, UNMODIFIED;
- L-COMP's n5b.py from claude/l-comp 29a6ed17, run read-only from a scratchpad copy, in its modes spec and orig (its own A5 tie-break).
Solutions are checked by zielonka.py + verify.py (dlm_module.py, every row) and by Oink zlk + verify.py (check_sol2.py,
n5/box5/oink_check.txt). Outputs: experiments/new/n5/box5/. Instances: experiments/new/instances/dlmmodule/ (sha1 in module_sha1.txt).

## Result: NOT KILLED. The module cannot be built from DLM's mechanism; obstruction K6 below.

## 1. The condition, exactly
τ̄ = Even's best reply to τ; A_σ(v) = {σ(v)} ∪ Iσ(v).
- If τ̄(v) ∈ A_σ(v) for every Even v, then τ̄ is a strategy of N5's arena H_σ and is optimal there (it is optimal in the larger
  arena G_τ). So N5's σ' is valuation-equivalent to τ̄.
- SSI's new σ is also τ̄: SSI switches exactly where (v, τ̄(v)) ∈ Iσ and keeps σ(v) elsewhere, and there τ̄(v) = σ(v).
- So under the condition the two Even steps coincide up to optimal ties, and dually for Odd with σ̄ ⊆ A_τ.
On DLM's SSI paths the condition fails almost everywhere (dlm_diag.py; n5/box5/diag_*):
- dlm1, n = 3: Even fails 11 times and Odd 10 times in 13 SSI iterations; only 3 iterations are clean (7, 11, 13).
- dlm2, n = 3: Even 87, Odd 75 in 23 iterations; none clean.
The distraction IS the failure: τ̄(v) is a non-improving edge, so SSI keeps σ(v).

## 2. Where N5 leaves SSI's path (dlm_agree.py: N5's step applied to EVERY state of SSI's run; ssi_agreement.txt)
| family | n = 2..5: SSI iterations | states where N5's step = SSI's | disagreeing vertices (Even / Odd), by kind |
| --- | --- | --- | --- |
| dlm1 | 5, 13, 29, 61 (108) | 3, 5, 7, 9 (24) | 118 / 144, ALL "SSI keeps, N5 switches" |
| dlm2 | 9, 23, 51, 107 (190) | 6, 8, 10, 12 (36) | 224 / 255, ALL "SSI keeps, N5 switches" |
- N5's step never omits a vertex that SSI switches, and never switches a vertex differently. It only adds switches, exactly at the
  vertices where the distraction makes SSI keep σ(v) although Iσ(v) ≠ ∅.
- The number of states where the steps agree grows linearly (2n − 1 for dlm1, 2n + 2 for dlm2).
- NOT a theorem: on random games "N5 ⊇ SSI" FAILS (n5_superset.py, 1,500 games, every state of both N5's and SSI's runs,
  44,366 states).
  - SSI switches that N5 does not make: Even 69 times keeps, 49 times switches elsewhere; Odd 50 / 22 (n5/box5/superset_random.txt,
    first witness saved there).
  - N5 can skip a best-reply switch when τ̄'s downstream choices are not available in A_σ.
  - So K6(i) is a statement about DLM's mechanism, not about N5 in general.
- Observation on DLM's families only: N5 ⊇ SSI. N5's joint restricted optimum takes every switch SSI takes, plus the
  improving switches that the distraction withholds.

## 3. Module attempt (dlm_module.py): Odd blunder dummies on DLM's games
- Every edge (x, y) of an Even vertex with ≥ 2 successors becomes x → D → {y, g}. D is an Odd dummy of the lowest priority; g is a
  shared gift (Even self-loop, top-even or 0).
- Start: DLM's (σ0, τ0) mapped onto the dummies, and τ(D) = g (the blunder that should make N5's restricted optimum keep σ, as
  SSI does).
- The FULL effective start pair is written to a .start file, so n5.py and n5b start identically.
| family, gift | n = 1..6: N5 n5.py SPEC | n5b spec | n5b orig | SSI (n5.py mode ssi) on the same games |
| --- | --- | --- | --- | --- |
| dlm1, top | 2, 2, 2, 2, 2, 2 | same | same | 2, 6, 14, 30, 62, 126 (= 2^(n+1) − 2) |
| dlm1, low | 1, 2, 3, 4, 5, 6 | same | same | 1, 3, 4, 7, 14, 25 |
| dlm2, top | 3, 5, 7, 9, 11, 12 | same | same | 2, 10, 18, 33, 64, 123 |
| dlm2, low | 3, 7, 9, 11, 13, 15 | same | same | 3, 10, 23, 39, 74, 148 |
All N5 runs: 0 fallbacks, all checks OK (module.txt; Oink zlk on dlm2_top n = 3, 6). The three implementations agree on EVERY row.
Unmodified DLM families, n = 1..8, n5.py / n5b spec / n5b orig (controls.txt):
- dlm1: 1, 2, 4, 4, 6, 7, 8, 8;
- dlm2: 2, 4, 7, 8, 11, 12, 13, 15;
- identical in all three.
Reading: the blunders keep SSI exponential (DLM's distraction survives and even sharpens, SSI ≈ 2^(n+1) on dlm1_top), but N5 gets
FASTER (2 to 15). Against the blunder τ, N5's joint optimum sees the gift on every candidate route and moves at once.

## 4. K6, the obstruction (next to K1-K5 in N5-killer-box4.md §6)
K6 (DLM distraction). For N5 to follow an SSI path, a module must make σ(v) restricted-optimal against τ at EVERY vertex where SSI keeps
σ(v) although Iσ(v) ≠ ∅: a local stall, so N5 adds none of its extra switches. When σ' agrees with σ on the plays from σ(v) and from the improving w, the stall lemma's
chain applies locally: an Odd blunder (τ worse for Odd than σ̄) on the play from σ(v), persistent like K2. But:
- (i) DLM's mechanism is itself the opposite situation. SSI keeps because τ̄(v) is NON-improving, while N5's arena keeps all
  improving edges and takes them. That happened at 100% of these vertices (§2: 342 Even and 399 Odd vertex-events,
  n = 2..5, both families).
- (ii) Adding Odd blunders to supply the local stall changes τ̄ (Even's best reply exploits the blunder), so it changes SSI's own
  path, and N5's joint optimum exploits the blunder too (§3: faster).
- (iii) The local stall must persist through SSI's whole path, so the K2/K3 requirements (all of Odd frozen; preferences that read
  the counter) apply locally at every distracted vertex.
In short: DLM's distraction works by withholding improving switches from a LOCAL rule. N5's step is the joint optimum over all
improving switches, and it takes every withheld switch unless an opponent blunder makes staying at least as good. That would need
the K1-K3 structure at every distracted vertex at once.

## 5. Not done
- "N5 ⊇ SSI" is false in general (§2). On DLM's families it holds on the data. An attack that uses the states where N5 skips an
  SSI switch has not been tried.
- No module family that gives N5 super-linear growth in either tie-break mode.
