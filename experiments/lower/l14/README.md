# L-LOWER BOX L14 tools (successor 13; prep before «go», nothing run at scale)
- rsolve.py GENOME TARGET OUT: writes gsolve ranks/signs (the «_solved» form of L10 §3d); reproduces
  ../l10/rec/L10_C11_osc2_final_solved.txt bit for bit (sha1 c2e925f7) from L10_C11_osc2_final.txt.
- ann3.c: copy of ../l10/ann.c with a third order constraint (10th argument, same form as the 9th). Build: gcc -O2 -o ann3 ann3.c -lm.
  C12 call: ann3 C11 core8 OUT SEED SECS 0.8 "8+11+13+14+15:0,1,2,3,4,5,6,7" - "11+13+14+15:8,9" "13+14+15:10,11".
- mincut.py GENOME X: helper vertex cut kappa(y) from each core mover y to the sink X.
- cause.py GENOME: checks Lemma CAUSE / KEY-DELAY on a free run (0 violations on HIT7_lift_d32, PG_C10_X11_k2_t16, PG_C4_X13_k2_t10).
