# rund: DATA for docs/si/N5-RUND-box17.md (L-SI successor 12, box 17)
- rund.py: twin terminal changes along fallback-free in-phase runs (D-change, W unchanged, length-only, levels); LENONLY lists the DEAD
  strict-raise cases (D constant, W(v) changes only in length).
- rel.py: Lemma CR-REL (edge order transfer level L_rel vs M_D; freeze check from state k_0 + n − 1 on runs of ≥ n + 1 states; "content"
  of the freeze). MUT=2 control (freeze from k_0 + 1) must fail; MUT=1 (L_rel − 1) does not bite on available data.
- le.py: twin pairs and their relative disagreement level L_e per run.
- gap.py: Lemma OFFSET (MONO, FAC), Theorem TWIN-GAP (JUMP, POST, BOUND), CONJECTURE OFFSET-ONCE (RETURN inside a stretch_D with (h3_D)).
  MUT=1 (doubled jump) must fail.
- climbtw.py, climboff.py: climbs (twin changes per run; offset changes per vertex per stretch_D). dumprand.py: rewrite game #I of a
  --rand stream.
- instances/: lenonly_n8.pg (DEAD box 17, sha1 725c2766…); climb outputs tw_*, off_* (best games, not counterexamples).
- below.py: per-transition trace of the long runs (note §9); pv.py: per-vertex changes per run (note §9).
- mkret.py, mkalt.py: OFFSET-ONCE counterexamples (note §10; instances offret_n23, offalt_K10); mkalt2.py: the failed linear-size variant;
  trace.py: one-vertex N5 trace (logs/trace_offret_n23.txt).
- okfrz.py: Lemma P^c_ok / Corollary FRZ-OK (note §13); MUT=1 must fail.
- lvl.py: CONJECTURE LEVEL-COUNT and its strong form INC (note §12); mkinc.py: the INC counterexample (incdown_n23).
- piece.py: Lemma PIECE_D / Corollary SPLIT-RED (aligned / split / forbidden states; note §11). MUT=1 must fail.
- logs/: the runs quoted in the note. Reproduce: `python3 -I gap.py --list ../../new/box41/lib41.txt 2` with RS=2, etc. (see the note §7).
- sched.py (successor 13): Lemma P^c_sch / Corollary FRZ-SCH / Corollary CHARGE (note §14): per-edge forbidden states (first, last,
  persistent), the GEN freeze check over all s ≤ t, and the charging of every change. MUT=1 (schedule shifted) and MUT=2 must fail.
- lvl2.py (successor 13): LC2, PAIR-OC, OC_NORISE, PAIR_ALL after LEVEL-COUNT's count form died (note §15); MUT=1 (W only) must fail
  on lcount_n23 / lcount2_n23 (L-RED's instances in experiments/red/h3/instances/).
- sched.py also (note §16): FS_SPAN_V / FS_DUR_V (CONJECTURE FS), FZ_EQ_V (Fact FZ), UNF_V (Lemma UNF), U and UF_ONCE_V (CONJECTURE UF-ONCE),
  gate classes of forbidden pairs; NOGEN=1 skips the quadratic GEN check; --rand like lvl.py. Logs fs_*.txt.
- sched.py USTRUCT=1 (note §17): per-U-event structure, OFFUP_V (Lemma OFFUP), U-SPLIT classes (U_OTHER is a violation); logs/ustruct.txt.
- bnd.py (note §19): (R4) stretch_D boundaries per run by cause (DCH / XI / WG), gate Ξ / W changes, Lemma GATE-XI attribution; V=1 per run.
