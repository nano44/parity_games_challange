# Box 12: epoch census for N5 (L-COMP successor 5, Opus 5.5; Lead GO 2026-10-26 07:57Z)
D18 / L40. Every number here is DATA (not proof). Labels: DATA / READING. Nothing here is a TARGET.md claim; G-N5-TIME stays open.

## Code (L-COMP's own; no other lane's code imported)
- `census.py`: runs N5 with `experiments/n5-second/n5b.py` in SPEC mode (L-COMP's independent implementation, equal to n5.py state by state
  on 22,810 runs, box 9; `fbtrace` hook added 2026-10-26, no effect on the run) and measures, per phase (R38 (a): (λ_Ξ, τ) constant) and per
  epoch (maximal run with σ̄|Q constant): N_ep, ρ = Σ_q ρ_q, the ALT classes (clean strict / tie / non-clean / cycle-node), |D_E|, len(E),
  crossings X_D and X_SN^pre(E). Definitions and the line each comes from are in the script header (RESULTS R60, R61, R63, R64 on trunk e1eabcd0).
- Falsification tests of LANDED statements, every phase: EP0 (R64 (c)), ALT (R61 (e)), NEP (R61 (f), disjoint-class reading = strongest),
  XEP (R63 (d) with the sharpening XEP-N1), SPLIT-RD / SPLIT-STICK (R63 sharpening via R55 (a)), EPOCH (R60 (c)), MONO (R15 (a)),
  D-EPOCH (R63 (c)). A hit prints `VIOLATION`.
- `exhk.py`: exhaustive canonical families (1O = exh.py's C^1O family; 2O = two Odd choice vertices of out-degree 2, Even out-degree 1-2),
  S3 or all start pairs, multiprocessing.
- `climb.py`: hill climbs on (game, start pair) with census.analyse as the scorer (fitness `nep` or `lend2`), sideways moves accepted.
- `named.txt`: the named instance set (lane instances with their start files). `instances/lcount_n23.*`: copies of L-RED's pinned files
  (origin/claude/l-red, experiments/red/h3/instances/; sha1 f86125a0 / 098fca21 / c25786c5 equal to L-RED's), added at the Lead's request.

## Reading choices (READING)
- κ in ALT is read through Ξ: a clean change is STRICT iff Ξ_{t+1}(q) is strictly better than Ξ_t(q) in the VJ order (SI.nvo); TIE as in
  R61 (e) with Ξ-equality. ALT classes are made disjoint in the order cyc (λ(q) = q), nc, tie, strict, so the NEP test is the strongest reading.
- len(E) counts the in-phase transitions whose source lies in E, so it includes an exit transition that stays in the phase (R64). L-NEW's
  P-N5-EPR §5 table reports y − x (both ends in E): its maxima 91 (|D| = 1) and 56 (|D| = 0) on lib41 correspond to my 92 and 56.
- S3 = SPEC's start (n5b default); random start pairs: every vertex of its owner a uniform successor.

RESULTS_TABLES
