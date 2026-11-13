# L-LOWER BOX L18: f6's full-horizon correctness inside the search (tools; product docs/lower/L18-horizon.md)
- enc32c.py: copy of ../l12/enc32_lcomp.py (sha1 a8c4f5e3) + CLAMP_FROM / CLAMP_KEEP: transitions t >= CLAMP_FROM keep only the
  CLAMP_KEEP core movers' constraints (core forced to the target = the clamped run of l16/f6check.py). CLAMP_FROM None = original.
- pgad6.py: l16/pgad5.py on enc32c with env F6R = R (horizon): free run rows 0..PREFIX, clamped f6 constraints on transitions PREFIX..R-1.
- ccheck.py: checker mode (genome fully fixed). Validation: A3x5_P15 (f6check first mismatch at pre-state row 18) prefix 15: SAT at R 17,
  18, UNSAT at R 19, 20; A2_solved (f6 correct on rows 0..510) prefix 6: SAT at R 64 and R 510 (34M clauses, 35 s, 651 MB).
- Sizes (pgad6 build, frame below, P 13): R 32 6.3M clauses / 0.85 GB; R 64 11.5M / 1.6 GB; ~163k clauses per clamped row, so R 510
  (~85M) does not fit. Horizon refinement: ask at R < 510, check SAT decodes with f6check 0..510, raise R past a mismatch. UNSAT at R
  implies UNSAT at 510 (the full question only adds constraints).
- q.sh: ONE pgad6 question per task in the BOX L18 frame (XS 8,11,12,14,15, XORD 8,11,12,15,14, XALL, FIXC 16,17, G empty), with
  replay (sim6 = fenc) and f6check 0..510 on SAT.
- pgad6 env PHASESTATES (default 1 with PHASE): also phases the helper states from the hint genome's clamped run (l7/clamp.py).
  FINDING: CaDiCaL (pysat cadical195) does not follow these phases: P 6 R 32 with A2_solved (a model) phased: 524 s (unphased 584 s);
  the same design as ASSUMPTIONS (env ASSUMEHINT=1, diagnostic): SAT in 0.2 s.
- pgad6 env LNS=movers [LNSFREE=gates,starts] (with PHASE): large-neighbourhood question: the hint's design literals are ASSUMED except
  those of the listed movers' options (wiring, signs, ranks) and the listed categories. SAT = a real solution (decoded, CHECKed, replayed);
  UNSAT = «this neighbourhood only», never a frame verdict.
- drift.py: f6's two chains, decisive option and helper states at given rows of a genome's clamped run (run/drift_P7R64.txt).
- FRAME L18b (Lead 19:57Z, named frame change) = L18 + q5 (mover 10) free: XS 8,10,11,12,14,15, XORD 8 < 11 < 10 < 12 < 15 < 14 (reach order
  of A2_solved's wiring; also consistent with the C8 and H7 decodes). lnsb.sh with env XSL=8,10,11,12,14,15 XORDL=8,11,10,12,15,14.
  Results under L18b are tagged «L18b» in logs and docs, never mixed with L18 rows.
- inframe.py: checks a genome lies in a pgad5/6 frame on a base (run/inframe.txt: every decode vs A2_solved under L18b).
- mono.py (successor 16): horizon monotonicity check (run/mono.txt): builds one question's CNF at Ra < Rb with variables named by
  allocation site and row, and checks Ra's clauses (minus the unused row-(Ra+1) gate definitions, checked extendable) occur in Rb.
  INCLUDED on two instances ⇒ «UNSAT at R 64 implies UNSAT at R 510» for R-ladder screens (Lead ruling 02:22Z). First attempts without
  renaming (literal inclusion) fail: state variables of all rows are allocated before the transitions, so numbers shift with R.
- KNOWN LIMIT (successor 16): all six L18b clients free (XS 8,10,11,12,14,15, XORD 8,11,10,12,15,14) → RecursionError. Two recursions
  need an acyclic candidate graph: enc32c.ro (static reach) and the chain-membership encoding q / inopt (enc32c l. 250, 257). An
  iterative ro (regression: CNF sha1 identical, ec7e1941 for XS 8,10,11 and a7e0e854 for XS 8,10,11,12, R 16, base L18b_N13a) only moves
  the crash to q / inopt, whose recursion IS the encoding (it assumes no cycle). Not a small fix: change reverted, limit recorded.
