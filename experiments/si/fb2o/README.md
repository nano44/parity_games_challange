# fb2o: DATA for docs/si/N5-2O-box16.md (L-SI successor 11, box 16)
- fb2o.py: per-phase checks of PFZ-q, ROUTE-2, DIR, SAT-2 and the FB-2T pair count, in arithmetic κ (κopt by brute force over simple paths;
  small n only). MUT=1 is a mutation control that must fail.
- climb2o.py: hill-climb on games with exactly two Odd choice vertices (OBJ=f: fallbacks in one phase; OBJ=hyp: DIR + SAT hypothesis hits).
- lib2o.txt: the 43 repository .pg files with exactly two Odd choice vertices and n ≤ 40 (found 2026-10-26 by a scan of experiments/ and docs/).
- logs/: lib2o.txt (PASS), climb_rand.txt, climb_fts.txt, climb_hyp.txt.
- tcsw.py: terminal changes per fallback-free run, (h_D), (h3_D), W-frame ROUTE-2 (DATA for docs/si/N5-2O-T-box16.md §3); logs tcsw_*.txt.
- tcdir.py: direction of terminal changes against the gates' W / Ξ order (TC-W test; DEAD box 16 in docs/si/DEAD.md); --one GAME START.json.
- climbtc.py: climb for two-gate terminal changes (found none against W; random start pairs did).
- instances/: tcw_against_n12.pg (first-gate form), tcwult2_against_n8.pg + .start.json (all three forms). inst4344.txt, tcw.txt: input lists.
- gdnc.py: Lemma G_D-NC (b′), (c2′) and Corollary FRZ-U_D (docs/si/N5-2O-T-box16.md §6); MUT=1 control; logs gdnc_*.txt.
- hcyc.py: cycle configurations of the two gates per frame; whether they share the honest class (N5-2O-T §7). gdnc.py H3ONLY=1: Lemma C2-H3; MUTL=1 control.
- km2.py: set-form FRZ-U freeze test on two-gate same-class ¬(h3_D) runs (vacuous). twin.py: Δ-RT levels of twin gates against m* (N5-2O-T §8). tcdir.py also reports TC-CN (twinW / diffW / TCCN_V).
