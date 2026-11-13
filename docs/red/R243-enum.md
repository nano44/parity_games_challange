# R243 (interim): full key enumeration past level 7 — a value-side SIGNAL obstruction, a k = 6 construction at d = 20, and exact signal screens (DATA; no kill, no cap lemma)
L-RED successor 69 (session_01V5yGRZMU6zgaX7o1n7CQzP, Opus 5.5 high), D1 / D18 / D21. Lead RE-TARGET 09:08Z (owner: «So put everything into trying solving it today»),
sharpened 09:15Z / 09:21Z (box 217 A2, A5, A6 ENUM-LOG, A7 / A7′). Written 2026-11-13T10:52Z (date -u). Labels: DATA, READING (mine, not proved),
CONSTRUCTION (an instance with a checked run). Nothing here is a RESULTS entry or a TARGET.md claim. **G-N5-TIME stays OPEN; ENUM-LOG (A6) stays OPEN.**

## 0. Answer so far
- **No k = 8 construction; no cap lemma.** The question «k ≥ 8 at linear fuel?» is open after this session.
- **Where HIT7 stops (DATA, diag243.py on HIT7_d28_F254):** level-7 movers 14 / 15 have KF 254 = flips(12, 13), exactly the 2^8 − 2 their full
  enumeration needs (the KEY side is ready), but switch only 32 / 33 times: on 122 / 142 steps their key-least option is NOT Ξ-improving
  (blocked by the VALUE side). Level-6 mover 13 is never blocked; its option-0 Ξ-target is the level-5 full mover 11 (its chain reads the
  lower block's state). out/diag243_HIT7.out.
- **READING (forced timing):** a full mover x (sw = |K(x)| − 1) has μ(x) change ONLY at its own switches (KEY-TAU (ii): μ falls at every switch
  and |K(x)| − 1 falls are all there are). Hence at every step where its key-least option changes, that option must be Ξ-better at the
  current state: the Ξ-comparison of x's two option chains (top differing β) must PREDICT at state t the key order of the level-(L − 1) pair
  at t + 1. Counting supply (A7) is not the issue at level 7 of HIT7; this prediction (a SIGNAL) is.
- **CONSTRUCTION, k = 6 at d = 20:** H5PLUS_L5 = H5 + one level-5 mover (W-targets the level-4 pair, Ξ-targets the existing level-5 movers 11, 10,
  own β's at the two lowest ranks): experiments/red/r243/inst/H5PLUS_L5.json, sha1 251b12617a7cf5ecca7eee8c4c4ce0a213bca832, 41 movers, Ξ-acyclic.
  N5 (n5s237 spec, S3, Γ3 = box 189): T 136, maxsw 63 = 2^6 − 1, levels 0..5 full; every KEY-TAU counter 0; n5v xdiff 0 (kt241). H6 needs d 24 / 48
  movers for k = 6. The useful Ξ-targets (10, 11) are «shadows»: level-5 movers switching at the level-4 rate (sw 31 = 2^5 − 1).
- **Exact signal screens** (an added mover y is exact: nothing points to it, the rest of the run is unchanged; checked by re-run every time):
  | genome | target level | one added mover (signal243) | + one Ξ-MUX z (screen2_243) | iterated (2 z's) | full |
  | --- | --- | --- | --- | --- | --- |
  | DBL4 | 4 | 15 | — | — | 15 |
  | H5 | 5 | **63** | — | — | 63 |
  | H6 | 6 | 65 | 96 (z at level 5, swz 32) | 98 | 127 |
  | HIT7 | 7 | 144 (Ξ-targets 13, 12: the level-6 full pair) | 191 (z at level 7, swz 127) | running at handover | 255 |
  | H5PLUS_L5 | 6 | 64 (W-targets 40, 10: a half-rate shadow) | — | greedy adds clones (64) | 127 |
- **Climbs** (enum243.py, k-score): from random ladders k stalls at 2 (d = 4, 6, 8; 100k evals each); from HIT7 lifted to d 40 / 56, level 7 rises
  33 -> 64 (general) and stays 33 with mutations restricted to levels ≥ 7. out/jobF_*.log, out/jobE.log.

## 1. Tools (experiments/red/r243)
enum243.py (k(G) via r187 ideal.traj, which equals N5's T_key on the five towers: 30 / 136 / 209 / 299 / 67, checked; climb, lift); diag243.py; signal243.py;
greedy243.py (PAIR env: chosen W-targets); screen2_243.py (Ξ-MUX z + target y, numpy; ADDZ iterates). Every construction is re-checked on n5s237 + n5v.

## 2. Next (for a successor)
- A JOINT screen for two shadows (s1, s2) at the target level + the full mover F with Ξ-targets (s1, s2), as H5's 10 / 11 / new 40 (the greedy
  cannot find it: one shadow alone does not raise sw(F), so the greedy adds clones). If F_6 on H5PLUS_L5 becomes full, recurse (shadows at
  level 7, ...): the size per level then measures the fuel law A6 asks for.
- The forced-timing READING above as a lane lemma: «x full ⇒ at each KP change of x the KP option is Ξ-better»; then whether a Ξ-comparison of
  two chains can predict the level-(L − 1) key order at depth L with O(1) added movers per level (the open step).
