# R13: attack on L-ALG's Phi_idx (per-piece-index death-round record) on the pinned A_DTL (L-RED, 10:45Z by date -u; produced on Opus 5.5)
Target (Lead 10:37Z): Phi_idx says that every dead-top cap carry at depth-0 piece index i raises R_i(u) for some rescued
u. Here R_i(u) is the maximum death round of u at piece index i over the phase's -1 results there, with a stable result
counting as infinity. That gives <= n^2(n+2) such carries per phase. L-ALG's data are on C6 (ideal pruning). This file
tests the claim on A_DTL itself (actual pruning, deficits included) with this lane's tracer (exact against Oink).
Status words: DATA / READING.

## DATA
- Tools (experiments/red/carry/):
  * phi_idx.py: changes at a -1 piece at an equal context that raise no record ("flat"), regardless of driver type;
  * phi_drivers.py GAME SEARCH PIECE: L-ALG-style driver classification of one change (undo test at the first changed
    round r0; top alive or dead; rescued vertices above or below the top);
  * phi_full.py: the exact claim. A change is CAP-ONLY if every driver is dead before r0 and rescues only vertices above
    its top. A cap-only change that raises no record is a counterexample.
- phi_full.py on the 109 files of L-ALG's instances plus dtl_mviol_n20: 324 changes, 131 cap-only, ALL 131 raise a record
  (0 counterexamples); 4 non-cap flat changes.
- phi_idx.py on 147 files (instances and climbed games): 0 flat changes once records are taken from -1 results only.
  3,000 random games with n <= 20 (`--random 3000 20 31`): 0 flat changes of any driver type.
- Near miss, not a counterexample: experiments/red/carry/instances/phi_flat_alive_n32.pg (a climb from L-ALG's
  dtl_replay4_n32; Oink: 3 dominions, 43 tangles, 14 iterations, solution verified). Even searches 4 -> 5, depth-0 piece
  index 1 (a cut piece, -1 both times, same context): the return set grows from {17, 27} to {7, 12, 17, 27}. Vertices 7
  and 12 go from round 4 back to round 5, which only EQUALS their record from search 3 (a different context at that
  index), so no record is raised. Its only driver is t16 (top 7, priority 22). It is ALIVE at r0 = 1 and rescues vertex 6
  (priority 20, below its top): an alive-top carry, which Phi_idx does not claim to cover (L-ALG: alive-top carries fail
  it at cut pieces). The shape (same index, new context, rescue to the SAME death round as before) is exactly what a
  cap-carry counterexample would need.
- Climbs on fitness `phicap` (1000 x counterexamples + 10 x cap-only changes) from dtl_replay4_n32 (110.16 at the
  start: 11 cap-only changes), dtl_replay2deep_n32 and dtl_mviol_n20 are running at the time of writing.
