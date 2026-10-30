# N5-TAU (box 96): the proof side of box 95's reading. The reading is CORRECTED: moving τ is NOT what kills H_n. N5 started with τ already Odd-optimal (τ never moves; the whole run is ONE W-run) takes 6N + 1 iterations on switchbestexp N = 3..7 (19 … 43), fewer than from the default start. What kills H_n is S4a's FIXED-Odd frame (a W-run), in which a withheld W-better closure must be Ξ-blocked (R140 DECEL-RED) and is charged to R*_F; on H_n R*_F ≤ 5. Lemma STUB-RED (lane, a restatement of landed FW-R*): inside a W-run, stubborn triples cost at most (n − 1)(R*_F + 1) transitions. The triple shape that can survive: a Ξ-blocked, W-better closure (Odd deviation on its target's play), i.e. R*_F itself. No general O(1) lemma; P(τ) as posed is DEAD
L-NEW successor 39 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 19:21Z: «BOX 96 = the proof side of your reading. Formulate the
property P(τ) exactly and try to prove: if τ_t is moved only by Odd's own improvement step (S4b), then the S4a W-optimum against τ_t resolves
every «stubborn triple» … within O(1) steps of its creation … If it fails, give the exact obstruction: which triple shape survives.» Written
2026-10-30 19:22Z-19:23Z (date -u). Working note, unrefereed. Labels: PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim.
G-N5-TIME OPEN.

## 0. Sources, setting
- docs/new/N5-HN-box95.md (box 95: N5 = I^glo for 13 iterations, split after the first τ-change); L-LIT T59 §3.2 (stubborn cycles: «Three Even
  nodes; two leave to the lane and one enters per iteration … The closure is never inside the arena»); L-RED R140 Corollary DECEL-RED; landed
  RESULTS R88 FW-R*, R89 GP*-RUN; P-N5-WRUN GAP-DEV.
- switchbestexp N (PGSolver port, experiments/hard-families/pgsolver_port.py), as read from the file (N = 3): bit i has the Even triple
  e_i → f_i → g_i and the Odd exit h_i with successors {e_i, m_i} (e_i, f_i, g_i, h_i have priorities 27, 29, 31, 32 for i = 0; m_i a single-
  successor Odd vertex of high even priority, 90 for i = 0). The cycle e_i f_i g_i h_i is the stubborn cycle; h_i is the only Odd choice on it.
- Tools: experiments/new/box96/taustart.py (N5 from four Odd starts: BEST = best-reward, OPT = τ_end everywhere, BR = σ̄(σ_0), OPTH = τ_end
  only at the h_i), box85/xirise.py (R*_F, FL_F, returns per W-run).

## 1. P(τ) as posed, and why it is DEAD
- P(τ) (the Lead's form, made exact): «τ_t changes only by S4b steps (no S4c Odd fallback)». Claim to test: under P(τ) every stubborn triple
  of H_n is resolved within O(1) steps of its creation, AND this is what kills H_n in N5.
- DATA (taustart.py):

  | N | n | BEST (default) | OPT (τ_0 = τ_end: τ never moves) | BR (τ_0 = σ̄(σ_0)) | OPTH (τ_end only at the h_i) |
  | --- | --- | --- | --- | --- | --- |
  | 3 | 85 | 41 (3 τ-changes, max W-run 26) | 19 (0, one W-run) | 41 | 19 |
  | 4 | 110 | 47 (4, 31) | 25 (0) | 47 | 25 |
  | 5 | 135 | 55 (5, 38) | 31 (0) | 55 | 31 |
  | 6 | 160 | 62 (6, 44) | 37 (0) | 62 | 37 |
  | 7 | 185 | 68 (7, 49) | 43 (0) | 68 | 43 |

- So N5 with τ NEVER moving (one W-run against the Odd-optimal τ*) is linear, 6N + 1, and shorter than the default run. Fixing τ only at the
  h_i (OPTH) gives the same counts. The τ-moves of box 95 are where N5 first departs from I^glo on the default start, but they are not
  needed to kill H_n.
- DEAD: box 95's READING «the first killer is the τ frame, i.e. Odd's own S4b step moving τ_t» (as an explanation of WHY H_n dies). Instance:
  switchbestexp N = 3..7 from the OPT start (τ constant, 6N + 1 iterations). Corrected reading: the killer is that S4a optimises against a
  FIXED Odd strategy (the W-run frame), whatever that strategy is and whether it moves later.
- Consequently P(τ) («moved only by S4b») is the wrong property: a property of how τ MOVES cannot be what matters when τ need not move.

## 2. Lemma STUB-RED (PROVED, lane; a restatement of landed R88 FW-R* with R140 DECEL-RED): what a stubborn triple costs inside a W-run
- Definition. In a W-run F, a WITHHELD CLOSURE at state t is an Even edge (y, z) with W_t(z) ▷ W_t(σ_t y) (W-better than y's choice) that is
  not adopted at t → t + 1. It is OFFERED if (y, z) ∈ Iσ_t, BLOCKED otherwise (R88's sense).
- Statement. Every W-run F has at most (n − 1)(R*_F + 1) W-changing transitions (R88 FW-R*, R89 GP*-RUN), and FL_F flat ones. A withheld
  closure delays W only while it is BLOCKED: if from state t on no edge is blocked-then-adopted, W reaches the arena optimum within n − 1
  transitions (GP*). An offered withheld closure is withheld only because S4a's one-player optimum prefers another edge at y with at least
  the same W-value (R140 NO-LOCAL-DELAY: a strictly W-best edge in H_t is taken at once).
- Proof. FW-R* and GP* as landed; NO-LOCAL-DELAY is ARENA-MAX (S4a's step, R57 premise) restated. □
- So, inside a W-run, the stubborn-triple mechanism («one cycle edge is never inside the arena») costs at most n − 1 transitions per release of
  a blocked edge: it is R*_F, nothing else.
- DATA (xirise.py on switchbestexp, default start, 2 W-runs each): R*_F = 5, 4, 3 at N = 3, 5, 7 (not growing); FL_F = 0; returns ≤ 1 per
  edge per W-run; |F| = 26, 38, 49. FW-R* gives |F| ≤ (n − 1)(R*_F + 1): 504, 670, 736 — far from tight, and R*_F does not grow with N.

## 3. The exact obstruction: which triple shape survives
- In N5 a stubborn closure survives a W-run only as a BLOCKED, W-better edge (y, z): W_t(z) ▷ W_t(σ_t y) but Ξ_t(z) ⊴ Ξ_t(σ_t y). By GAP-DEV the
  (σ_t, σ̄_t)-play from z then contains an Odd vertex o with σ̄_t(o) ≠ τ(o). For an H_n-type triple this o is the exit h_i (the only Odd choice on
  the cycle): READING (not traced instance by instance here), the closure survives while Odd's best response leaves the cycle at h_i
  (σ̄(h_i) = m_i) but the frame's τ(h_i) = e_i keeps it closed.
- So the surviving triple shape is: «a cycle closure whose W-value (exit closed by τ) beats the current choice while its Ξ-value (exit opened by
  σ̄) does not». Its count per W-run is R*_F, and it can be released many times only if σ̄ at the exit flips back and forth inside one W-run
  (mechanism O of box 88) or the poison is lifted by Even climbs below the deviation (mechanism B). Both are the open per-W-run residuals of
  P-N5-WRUN (rows E4, E8). On H_n neither happens more than 5 times.
- No O(1) lemma for general triples: gate_K64_n581 (𝒞^5O, box 94) has R*_F = 64 in one W-run, i.e. 64 releases of blocked, W-better edges
  through 5 Odd exits. Whether those are "triples" in Friedmann's sense is a naming question; they are exactly the surviving shape above.

## DONE / FINDINGS / NEEDS
- DONE: experiments/new/box96/taustart.py; check.sh section "box 96"; this note.
- FINDINGS:
  1. DEAD (box 95's READING, corrected): moving τ is not what kills H_n. Instance: switchbestexp N = 3..7 from τ_0 = τ_end (τ never moves, one
     W-run): 19, 25, 31, 37, 43 = 6N + 1 iterations, fewer than from the default start. P(τ) «τ moved only by S4b» is the wrong property (DEAD).
  2. Corrected READING: the killer is S4a's fixed-Odd frame (W-run). Inside a W-run a withheld W-better closure costs time only while it is
     Ξ-blocked (Lemma STUB-RED, PROVED lane = R88 FW-R* + GP* + R140 NO-LOCAL-DELAY). On H_n: R*_F ≤ 5, FL_F = 0, not growing with N.
  3. Obstruction: the surviving triple shape is a W-better, Ξ-blocked closure whose exit is closed by τ and opened by σ̄ (GAP-DEV). Its
     number per W-run is R*_F, the open residual of P-N5-WRUN. gate_K64_n581 has 64 such releases in one W-run with 5 Odd exits.
- NEEDS: none from the owner. L-RED's adversarial form should be restated: make the h_i-type exits flip σ̄ repeatedly inside ONE W-run (τ fixed),
  so that the same closure is blocked and released many times (R*_F super-linear). Moving τ is irrelevant.
