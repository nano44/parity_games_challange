# L-COMP box 28: T^R(4), machine-certified (target: T^R(4) = 13; packet P-TR4 in the P-TR3 format)
L-COMP successor 10, 2026-11-07 (date -u in the commits). Lead brief BOX 28. Labels: CERTIFIED (solver UNSAT + Glucose 4 DRUP proof
accepted by box27/drup.c), EXACT-SAT (solver UNSAT, no checked proof), DATA, CONJECTURE. Model: IDEAL (RESULTS R104, definition
only), 𝓛^R_d of RESULTS R110 (definition only). Not a TARGET.md claim. G-N5-TIME stays OPEN.

## Pipeline = P-TR3's (box27), unchanged code
- Encoder: box27/cnf.py as it stands (sha1 f1f803ae8837822ad3e305ad577957a309f511e7, last changed at 81ed3900), called with d = 4; no
  line changed in box 28. R112 cites it at 557b045b (sha1 fd882af1…); the later edits add only env-gated options (FREE0, ISO, KF, RUN2,
  XCUBE), all off here, and the current file reproduces the P-TR3 d 3 L 9 cube 0 DIMACS byte for byte (sha1 7e70b9e1…, re-measured
  2026-11-07).
- Changes from d = 3 (parameters only): d = 4 (8 movers, levels 0-3, 16 options); L = 14; root cubes fix s_0 of movers 2..7
  (2^6 = 64 roots, cube c sets s_0(2 + i) = bit i of c) on top of SYM (s_0(0) = s_0(1) = 0), exactly the P-TR3 cover with d = 4.
- Size (d 4, SYM + one root cube): L 13: 254,071 vars, 902,936 clauses; L 14: 273,590 vars, 972,056 clauses, 2,376,280 literals
  (d 3 L 9: 58,896 / 204,036).
## Read-back on the known witness
- ext/max_d4_L13.json = claude/vibrant-johnson-nxvvxo experiments/new/box156/ext/max_d4_L13.json (L-RED R197; sha1 f0735b61…,
  same file as box160/ext). pinwit.py (box27/pinck.py's pinned_sat, unchanged): sim T 13 (stop: stuck); pinned CNF SAT at L = 13,
  UNSAT at L = 14 (log/pinwit_max_d4_L13.out).
- symwit.py (the witness under SYM): options of movers 0 and 1 relabelled (both started on option 1; P-TR3 §2 relabelling), start
  [0,0,0,0,0,1,0,1], sim T 13 unchanged; pinned in the SYM=1 + root-cube-40 CNF: SAT at L 13, UNSAT at L 14; pinned in root 41:
  UNSAT at L 13 (log/symwit_max_d4_L13.out).
- mkdimacs.py writes one root cube's DIMACS (same text as box27/mkproof.py; no get_proof()); d 4 L 14 cube 0 sha1 2a07a8e9….

## Symmetry: SYM + PAIR-SWAP (8 root cubes instead of 64)
- SYM (P-TR3 §2, unchanged): swapping the two option labels of a level-0 mover is a symmetry; WLOG s_0(0) = s_0(1) = 0.
- PAIR-SWAP at level l (0 ≤ l ≤ d − 2), PROVED (lane): let σ rename movers 2l ↔ 2l+1 (in every W- and Xi-target and in the state), and
  then, for each mover y of level l + 1, exchange the labels of y's two options (each option object keeps its Xi-target, its β id =
  rank and parity, and its gate) and flip bit y of every state. (i) Class: in G, option k of a level-(l+1) mover W-points to mover
  2l + k; after renaming it points to 2l + 1 − k and carries label k; after the label exchange the option labelled k is the old option
  1 − k, which points to σ(2l + 1 − k) = 2l + k. Every other W-target is a mover of another level, unchanged. Ranks and gates stay
  distinct, Xi-acyclicity is preserved by renaming, levels are unchanged, so σG ∈ 𝓛^R_d. (ii) Runs: under the induced state map,
  every mover's current option is the same option OBJECT before and after; Xi-chains, their β-sets, and so every Xi-value comparison
  and every A-set, are the same objects; a key is the tuple of gates of the chain of W-targets of the current option under the new
  state, lowest level first: the same option objects, so the same gates in the same order. Hence the IDEAL step commutes with the map,
  the run of σG from σs_0 is the image of the run of G from s_0, and T and the stop reason are equal.
- The R110 wiring property used (RESULTS R110, «option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k»): the W-target
  of an option depends only on its LABEL k and its owner's LEVEL, not on which of the two movers of that level owns it. So (a) renaming
  the two movers of level l never changes which movers W-point where except through the targets 2l, 2l + 1 themselves, and (b) the
  option-label exchange at level l + 1 exactly undoes that change (step (i)). Nothing else in 𝓛^R_d's definition names a mover or a
  label: Ξ-targets, β's, gates and the start are arbitrary, and the Ξ-graph only has to be acyclic.
- Normal form: apply PAIR-SWAP at l = d − 2, …, 0 (top down), each only if needed to make s_0(2l + 2) = 0. Step l exchanges the bits
  of movers 2l, 2l + 1 and flips those of level l + 1; it does not touch levels ≥ l + 2, so the bits fixed earlier stay. Then SYM sets
  s_0(0) = s_0(1) = 0 (touches only those two bits). So every (G, s_0) has an image with the same T and s_0(0) = s_0(1) = s_0(2) =
  s_0(4) = s_0(6) = 0 (d = 4): the 8 roots fix s_0(3), s_0(5), s_0(7) freely; root ids (cube c sets s_0(2 + i) = bit i):
  0, 2, 8, 10, 32, 34, 40, 42. The witness's root 40 is one of them.
- DATA: pairswap.py, 0 mismatches (T, stop reason and the whole state sequence mapped) on 3,768 runs: 500 random 𝓛^R genomes each at
  d 2, 3, 4 (box27/pinck.rgen) at every l ≤ d − 2, and all 256 starts of max_d4_L13 at l = 0, 1, 2.

## Feasibility (2026-11-07 02:0xZ, DATA; sent to the Lead)
- CaDiCaL 1.9.5 L 14 roots 0, 21, 42: no verdict after 58 min (21 then stopped, not a PAIR-SWAP root; root 2 started).
- Glucose 4 + proof on root 0: no verdict at 55 min; proof ≈ 7 GB by then. drup.c ≈ 1 GB per CPU-hour (successor 9).
- diskguard.sh kills proof generation below 6 GB free.

## Lead 02:46Z: (ii) EXACT-SAT on the 8 roots (3 cores) + (iii) the ISO sub-class (1 core); (i) backward checking not now
- frup vs drup.c, same load, P-TR3 cube 9: DIMACS 01a9488a… and Glucose proof 942334eb… = the P-TR3 table; frup VERIFIED 526,970
  lemmas in 803 s, drup VERIFIED 526,970 in 784 s. No speed gain (drup.c already watches two literals; forward checking re-propagates
  per lemma in both). frup is kept as an INDEPENDENT second checker. All 16 cubes: xval_d3.sh (niced), log/xval_d3.txt when done.
- ISO sub-class 𝓛^R_ISO(4) (RESULTS R110: no option has Xi-target 0 or 1; cnf.py env ISO=1, which removes movers 0 and 1 from every
  Xi-target domain; the "build" log line does not print ISO, the variable count shows it: L 13 root 0 156,153 vars / 542,624
  clauses vs 254,071 / 902,936 without ISO). SYM and PAIR-SWAP keep ISO (they map the set {0, 1} of movers to itself and do not
  change which mover an option's Xi-target is, up to that renaming), so the same 8 roots cover it.
- ISO witness: ext/ISO_1_d4_t12.json = trunk experiments/new/box160/out/ISO_1_d4_t12.json (L-NEW box 160; sha1 01b71584…): in 𝓛^R_4,
  ISO, sim T 12 (stop: opt). Pinned in the ISO CNF: SAT at L 12, UNSAT at L 13; after the normal form (NF=1: PAIR-SWAP at levels 2, 1,
  0, then SYM) it lies in root 40: SAT at 12, UNSAT at 13 there; root 41 UNSAT at 12 (log/iso_pin_ISO_1_d4_t12.out). max_d4_L13
  under NF=1 also lands in root 40 (log/symwit_NF_max_d4_L13.out). Query: ISO, T >= 13 on the 8 roots (target UNSAT: T^R_ISO(4) = 12).
