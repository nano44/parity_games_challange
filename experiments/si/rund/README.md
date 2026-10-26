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
- lvl.py: CONJECTURE LEVEL-COUNT and its strong form INC (note §12); mkinc.py: the INC counterexample (incdown_n23).
- piece.py: Lemma PIECE_D / Corollary SPLIT-RED (aligned / split / forbidden states; note §11). MUT=1 must fail.
- logs/: the runs quoted in the note. Reproduce: `python3 -I gap.py --list ../../new/box41/lib41.txt 2` with RS=2, etc. (see the note §7).
