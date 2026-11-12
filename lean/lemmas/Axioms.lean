/-
Axiom audit.  Run from lean/lemmas:  lake env lean Axioms.lean
Every line must list only axioms among: propext, Classical.choice, Quot.sound.
-/
import PGLemmas

#print axioms PG.lam_gap_sharp
#print axioms PG.lam_gap_oneplayer
#print axioms PG.brseg
#print axioms PG.brsegG
#print axioms PG.brsegG_noH0
#print axioms PG.one_cross
#print axioms PG.one_cross_vj
#print axioms PG.Example.window_example
#print axioms PG.vj00Le_iff
#print axioms PG.val_proper
#print axioms PG.two_cross
#print axioms PG.lam_count
#print axioms PG.howard_run
