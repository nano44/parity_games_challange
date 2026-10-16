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

## READING + DATA: -1 return-set changes at CUT pieces are phantoms (10:49Z by date -u)
In search_rec (dtl.cpp 834-994), a -1 result goes on with the threshold scan "lowest priority t at which a vertex of R
attracts into X", and makes a cut if that scan finds something. The return set V is used only in the other branch
(Dom(V) when the scan is empty). So at a CUT piece, V influences nothing: not the cut's attractor, not its recursion, not
any later context. A change of V there changes no later piece. It is a symptom of new tangles, not a carrier of state.
DATA: in phi_flat_alive_n32 (Even searches 4 -> 5), piece 1's cut is identical (seed 2, attracted {2}) and only V
changes ({17,27} -> {7,12,17,27}). The search's real progress is the growth of piece 2's cut attractor ({10,15,19,24,26}
-> 25 vertices, same V = {14}) and the new recursion below it (`show.py ... --search 4` and `--search 5`).
Consequences (READING): (1) the transition counting of GAP-A-M section 6 (first piece whose (R, result, V) differs) also
counts such phantom V changes at cut pieces. For cuts, the state that matters is the attractor (the removed set), and that
can grow at an unchanged (R, result, V), which is L-ALG's "cut pieces not covered" case. (2) Phi_idx at cut pieces also
counts phantoms. A counter digit cannot live in a cut piece's V, only in its attractor (R10's 2CE class) or in a
domfirst piece's V (R10 MIRROR / R12).

## DATA: alive-top drivers at Dom(prevV) pieces versus MIRROR (M1) (11:00Z by date -u; produced on Opus 5.5)
phi_full.py now logs every driver that is alive at r0 (top not dead before the first changed round) together with the
earlier search's piece kind, and, at domfirst pieces, whether the driver's top h lies in that piece's -1 return set M_s.
Corpus: 134 files (dtl_mviol_n20, L-ALG experiments/alg/instances/*.pg and climbs_1016/*.pg, this lane's instances).
- 699 changes at equal context; 277 cap-only, all 277 raise a record: 0 Phi_idx COUNTEREXAMPLES.
- 18 flat (record-neutral) changes that are not cap-only: 17 at CUT pieces (phantoms, previous section), 1 at a domfirst
  piece (nest_nest_s84.pg, search 12->13, index 1), and it has NO driver born in the earlier search (the undo test
  finds none), so it is not a carry by a new tangle at all.
- 175 alive-at-r0 drivers at domfirst pieces: in 0 of 175 is the top h in M_s. Every one dies inside the earlier
  search's pruning (death rounds 2..9 of 4..12). That matches MIRROR (M1): h in M_s would mean Dom(M_s) removes h in
  piece 0 of s, so C could not be learned later in s.
READING: (H2a) narrows to that single driverless domfirst flat change, plus whatever the alive-top drivers do through
pruning (the (M2) self-reinforcing shape). The 17 cut-piece flats carry no state.

## NOTE: the equal-context counts are Lemma F instances; the cross-context data (11:28Z by date -u; produced on Opus 5.5)
Per L-ALG's correction (l-alg 155362c, GAP-A-M section 11c.1, via the Lead 11:16Z): L-ALG's Lemma F (proved under C6)
says that at an EQUAL context every vertex a new driver rescues beats its same-context record at that index. My
131/131 and 277/277 "cap-only changes raise a record" counts are all equal-context changes. So they are Lemma F
instances, not evidence for Phi_idx's real content (the CROSS-context record). The ALL-cap-only count of the data
section above is withdrawn as evidence for Phi_idx in the same way.
Cross-context split (phi_full.py now keeps per-context records at each index within a phase; same corpus of 134 files):
- In 50 of the 277 cap-only changes, index j already held a -1 record from a DIFFERENT context in the phase.
- In 50 of those 50, some RESCUED vertex beats the cross-context record (the merge over the other contexts) at j.
- 0 cap-only changes fail when the test is restricted to rescued vertices (rs_resc 277/277).
So the cross-context content of Phi_idx holds on these 50 cases. That is DATA on a small corpus, not a proof.
Climbs: dtl_search.py --fitness phicap reloads phi_full.py at every evaluation, and its record self.rec spans all
contexts of the phase. A hit is therefore a real cross-context counterexample. Its old test ("no vertex raises a
record") was stricter than Phi_idx ("no rescued vertex raises one"); new runs use the rescued-only test. Seeds 111-117
ran with an alive-top logging bug between about 10:50Z and 10:55Z, when phi_full.py raised and the fitness returned -1,
so candidates with alive-top drivers were rejected in that window.
