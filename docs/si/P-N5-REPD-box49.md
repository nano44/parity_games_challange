# P-N5-REPD (box 49): repeat late adoptions per W-run reduced to window depth and exceptional repeats (GP*-SUB, LOC-R*, WIN, Theorem REP-DEPTH)
L-SI successor 31 (Opus 5.5; D15 / D18, Lead reading L40). Packet for the two referees, FROZEN at its push; the sha1 goes to the Lead;
repairs go in a NEW file docs/si/P-N5-REPD-fixes-box49.md, never into this file. The RESULTS-line proposal is the separate file
docs/si/P-N5-REPD-line.txt. Lead 2026-10-30 03:13Z: «GO: freeze P-N5-REPD in the P-N5-CUT style. Content: GP*-SUB, LOC-R*, WIN, Theorem
REP-DEPTH, written as a REDUCTION of [P-REP] to [P-WD] ∧ [P-X]. Every symbol defined, including window, t*, X_F, SELF, depth and D_F. Every
hypothesis carried. The definitions of "late adoption" / "W-run" cited from the landed RESULTS R88/R89. The pins added.» Working notes with
data: docs/si/N5-SUB-box46.md, N5-WDEPTH-box48.md. Labels (D18 / L40): PROVED (lane, unrefereed) / DATA / READING.
SCOPE (D1): a REDUCTION of one count (REPEAT late adoptions per W-run) to two counts NOT bounded here. Not a TARGET.md claim, not an
algorithm claim, no running-time bound; G-N5-TIME stays OPEN. Every [Q path@commit:lines] «…» is verbatim, checked by
experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh «box 49» with the shifted-line control that must fail).

## 0. What to sign, and what not
| § | statement | label |
| --- | --- | --- |
| §2 | Lemma GP*-SUB (R88's GP* and FW-R* on every sub-interval of a W-run, lateness read relative to it) | PROVED (to sign) |
| §3 | Corollary LOC-R* (W-changing transitions ≤ (n − 1)(RLOC + 1), RLOC = transitions with a LOCAL late adoption) | PROVED (to sign) |
| §4 | Lemma WIN (a window has ≤ n W-changing transitions; INIT ≤ n − 1) | PROVED (to sign) |
| §5 | Theorem REP-DEPTH (REP_F ≤ X_F + (1 + m_E + X_F)·Σ_{d=1}^{D_F} (n·m_E)^d) and Corollary REPD-POLY (the conditional) | PROVED (to sign) |
| §6 | readings, data, pinned checks | READING / DATA (NOT to sign) |

## 1. Setting, symbols, premises
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4 as in RESULTS), under the standing SPEC premise of RESULTS R57 (S1's procedure
  realises the optimal counterstrategy); any parity game G = (V, E, Ω, owner), n = |V|, m_E = the number of edges leaving Even vertices.
  A run (any start pair) is the sequence of states (σ_t, τ_t); a TRANSITION is t → t + 1, indexed by t.
- [R89] RESULTS R89 (landed): [Q docs/RESULTS.md@59cf1f1f4:5854] «W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays, λ_W its cycle-node
  map; a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of consecutive states of one τ-stretch none
  of whose transitions is an S4c fallback or changes λ_W … (Lemma GP*-RUN) RESULTS R88's Lemma GP* and Corollary FW-R* hold on every W-run».
- [R88] RESULTS R88 (landed): [Q docs/RESULTS.md@59cf1f1f4:5630] «BLOCKED at state k−1−i (W-better than σ's choice at r_i but not a
  VJ00-improving edge of Ξ) … (Corollary FW-R*) F has at most (n−1)(R*_T+1) W-changing transitions, R*_T := the transitions of F at which
  some Even vertex adopts an edge blocked at an earlier state of F». The proofs are those of R88's object docs/si/P-N5-GP-box31.md §3 (GP*)
  and §4 (FW-R*), read on W-runs by R89 GP*-RUN.
- Definitions used throughout (as in R88 / R89). F = [a, b] a W-run (states a..b; transitions a..b − 1). (y, z) (y Even) is BLOCKED at state
  t ∈ F if W_t(z) ▷ W_t(σ_t y) and (y, z) ∉ Iσ_t. A LATE ADOPTION in F is a transition u of F at which some Even y switches to z (σ_{u+1}(y) = z ≠
  σ_u(y)) while (y, z) was blocked at some state of F earlier than u. A LATE TRANSITION is a transition of F containing at least one late
  adoption. R*_T(F) := the number of late transitions of F. W-CHANGING transition: W_{t+1} ≠ W_t.
- [CUT6] P-N5-CUT §6 (docs/si/P-N5-CUT-box43.md, frozen 2678f6c6, sha1 d6519d3d…; SIGNED by both referees, REFEREE 19 ff5a6f81 + §C
  1a4e7571, REFEREE-2 21 7fd2aea8 + §C 4d6a69d1; its RESULTS line is in landing). Quoted: [Q docs/si/P-N5-CUT-box43.md@2678f6c6:154-156] «(i)
  #FIRST in F ≤ m_E. (ii) Let u₁ < u₂ be consecutive late adoptions of (y, z) in F (transitions u₁ → u₁ + 1, u₂ → u₂ + 1). Then y leaves z
  at a transition k → k + 1 with u₁ < k < u₂, and, if y is off-cycle (for F's τ) at every state of [k + 1, u₂ + 1], either W(z) changes on
  [k + 1, u₂ + 1] or the adoption is W-SILENT: W_{u₂+1}(σ_{u₂} y) = W_{u₂+1}(z).» FIRST: the first late adoption of an edge in F; REPEAT: any
  later one; REP_F := the number of REPEATs in F. OFF-CYCLE: y is not the cycle node of its own W-valuation.

## 2. Lemma GP*-SUB (PROVED)
Let F = [a, b] be a W-run and F′ = [a′, b′] with a ≤ a′ ≤ b′ ≤ b. Read BLOCKED at states of F′ and call an adoption at u ∈ [a′, b′) LATE IN F′
if its edge was blocked at a state of [a′, u). Then R88's Lemma GP* holds on F′ with "cycle node of state a′" and paths of ≤ k − a′ edges, and
F′ has at most (n − 1)(R*_T(F′) + 1) W-changing transitions, R*_T(F′) := the transitions of F′ containing an adoption late in F′.
Proof. R88's proofs (P-N5-GP §3, §4, as R89 GP*-RUN reads them on W-runs) use exactly these properties of the interval:
(1) every transition inside it is an S4a step with τ constant and no fallback (W-MON at each k → k + 1; Case B's ρ̂ ∈ H_k);
(2) λ_W is constant on it (the base case L = 0: W_{a′}(u) = (u, ∅, 0) for a cycle node u; B1′ (ii), B2a, B2b (i), (iii); and in FW-R*,
    "u = λ_W(x) is a cycle node of the first state");
(3) BLOCKED and Iσ are read at states of the interval (Case A; FW-R*'s blocked state t = k − 1 − i ≥ k − n + 1 is required to lie in the
    interval, which FW-R* ensures by taking k ≥ first state + n − 1);
(4) nothing about states outside it (maximality is never used).
(1), (2) hold on F′ because they hold on F ⊇ F′; (3), (4) are read on F′ by definition. So the two proofs go through verbatim on F′. □

## 3. Corollary LOC-R* (PROVED)
Call a late adoption of F at u LOCAL if its edge was blocked at some state t of F with u − n + 1 ≤ t < u, and let RLOC(F) := the transitions
of F containing a local late adoption. Then F has at most (n − 1)(RLOC(F) + 1) W-changing transitions.
Proof. FW-R*'s proof (P-N5-GP §4): every W-changing transition k with k ≥ a + n − 1 has, on the (σ_{k+1}, τ)-play from a vertex x whose W
changes, an Even y_i whose edge (y_i, y_{i+1}) was blocked at t = k − 1 − i ≥ k − n + 1 (i ≤ n − 2) and adopted at some u with t < u ≤ k. So
u − t ≤ k − t ≤ i + 1 ≤ n − 1: the adoption is local, and k is charged to the local late transition u with k − u ≤ n − 2. Each u is charged by
at most n − 1 values of k; the k < a + n − 1 are at most n − 1. □

## 4. Lemma WIN (PROVED)
Windows. Let L₁ < L₂ < … < L_r be the late transitions of F. The INIT window is the set of transitions [a, L₁) (all of F if r = 0); the
WINDOW of L_i is [L_i, L_{i+1}) (with L_{r+1} := b). Every transition of F lies in exactly one window. For a transition t, L(t) := the late
transition opening t's window (INIT if none).
Statement. The INIT window has at most n − 1 W-changing transitions; every other window at most n.
Proof. Window of L = L_i: the sub-interval F′ = [L + 1, L_{i+1}] has transitions L + 1, …, L_{i+1} − 1, none of which is a late transition of F.
An adoption at u in this range that is late in F′ has its edge blocked at a state of [L + 1, u) ⊆ F, so it is late in F, and u is a late
transition of F: impossible. So R*_T(F′) = 0 and GP*-SUB gives ≤ n − 1 W-changing transitions among L + 1, …, L_{i+1} − 1; the transition L
adds at most one. INIT: F′ = [a, L₁] has R*_T(F′) = 0 in the same way, ≤ n − 1. □

## 5. Theorem REP-DEPTH and Corollary REPD-POLY (PROVED)
The charge. Let ρ be a REPEAT of the Even edge (y, z) at transition u₂ of F, u₁ < u₂ the previous late adoption of (y, z) in F. Between u₁ and
u₂ there is no adoption of (y, z) (any adoption of (y, z) after u₁ is late: (y, z) was blocked before u₁), so y leaves z exactly once, at a
transition k with u₁ < k < u₂ ([CUT6] (ii)). Classes:
- ρ is CHAINED if W(z) changes at some transition of [k + 1, u₂ − 1]; then t*(ρ) := the last such transition;
- ρ is SELF if W(z) changes at no transition of [k + 1, u₂ − 1] but changes at u₂;
- ρ is SILENT / OWN-CYCLE otherwise: by [CUT6] (ii), if W(z) changes at no transition of [k + 1, u₂], then either y is its own W-cycle
  node at some state of [k + 1, u₂ + 1] (OWN-CYCLE) or the adoption is W-silent (SILENT).
X_F := the number of SELF, SILENT and OWN-CYCLE REPEATs in F (the EXCEPTIONAL ones).
Depth. For a late transition L of F let lwd(L) := the largest depth of a chained REPEAT at L (0 if L contains none), and lwd(INIT) := 0.
For a chained ρ, depth(ρ) := 1 + lwd(L(t*(ρ))). This is well-founded: L(t*(ρ)) ≤ t*(ρ) < u₂, so it refers only to REPEATs at earlier
transitions. D_F := the largest depth of a chained REPEAT of F (0 if there is none); R_d := the number of chained REPEATs of depth d.
Theorem REP-DEPTH. For every W-run F of every run on every game:
  R₁ ≤ (1 + m_E + X_F)·n·m_E,   R_{d+1} ≤ R_d·n·m_E (d ≥ 1),   hence   REP_F = X_F + Σ_{d=1}^{D_F} R_d ≤ X_F + (1 + m_E + X_F)·Σ_{d=1}^{D_F} (n·m_E)^d.
Proof.
- (a) Each window is charged at most n·m_E chained REPEATs (ρ is charged to the window of t*(ρ)). For a fixed edge (y, z), consecutive
  REPEATs ρ, ρ′ have the intervals [k + 1, u₂ − 1] and [k′ + 1, u₂′ − 1] with k′ > u₂, so distinct REPEATs of one edge have distinct t*. At a
  W-changing transition t, t*(ρ) = t requires W(z) to change at t, so at most |{Even edges (y, z) : W_{t+1}(z) ≠ W_t(z)}| ≤ m_E REPEATs have
  t* = t. A window has at most n W-changing transitions (Lemma WIN).
- (b) The windows with lwd = 0 are INIT and the windows of late transitions L that contain no chained REPEAT; such an L contains a late
  adoption that is FIRST or exceptional, and distinct L contain distinct adoptions, so there are at most 1 + m_E + X_F of them ([CUT6] (i)).
  Every chained REPEAT of depth 1 is charged to one of them; with (a), R₁ ≤ (1 + m_E + X_F)·n·m_E.
- (c) A chained REPEAT of depth d + 1 is charged to a window with lwd = d, opened by a late transition containing a chained REPEAT of depth d;
  distinct windows have distinct opening transitions, so there are at most R_d such windows; with (a), R_{d+1} ≤ R_d·n·m_E.
- REP_F counts every REPEAT once: chained ones by depth, the rest in X_F. □
Corollary REPD-POLY (the conditional). If for a constant D and a polynomial p every W-run F of every run on every game has [P-WD] D_F ≤ D and
[P-X] X_F ≤ p(n), then REP_F ≤ p(n) + (1 + m_E + p(n))·D·(n·m_E)^D ≤ q(n) for a polynomial q (m_E ≤ n²): P-N5-CUT's premise [P-REP] holds.
So, with P-N5-CUT's Theorem CUT-RED, G-N5-TIME's iteration half follows from [P-B] ∧ [P-SC] ∧ [P-ODD] ∧ [P-WD] ∧ [P-X]. □

## 6. READING and DATA (NOT to sign); pinned checks
- DATA (experiments/si/odd/repchain.py; corpus odd/out/repchain_corpus.txt, 719 games of odd/sbcg.lst, S3 start):
  - REPEATs 41: chained 41, exceptional 0 (SILENT 0, SELF 0, OWN-CYCLE 0); windows of t*: INIT 0, FIRST-only 40, REPEAT-opened 1 (so_th_n32);
    D ≤ 2; at most 6 REPEATs per window; LOC-R* violations 0; Lemma WIN violations 0 (≤ n − 1 W-changing transitions per window observed).
  - L-RED's latew_K20_m32 (sha1 063d173c2de7, with .start; one W-run): REP 570, all chained, all in FIRST-only windows, D = 1, ≤ 30 per window,
    R*_T 640 = RLOC; WCH 700.
- READING: CONJECTURE WD-BOUNDED (D_F ≤ 2) is open; a repeat-opened window has the same n·m_E capacity as a FIRST window, so no argument here
  stops a chain of windows. L-RED is attacking it. CONJECTURE REP-LIN is DEAD (L-RED R128; latew 570 > 538).
- Pinned (experiments/si/check.sh «box 45», «box 46», «box 48», «box 49»): repchain.py on latew_K20_m32 (REP 570, windows, D 1, X 0), on
  runfam_K40 (LOC-R*: WCHW 159, RLOC 8), on so_th_n32 (depth 2, WINR 1); this file's quotes (quotecheck.py, --mut must fail).

## DONE / FINDINGS / NEEDS
- DONE: this packet, frozen at its push; the RESULTS-line proposal docs/si/P-N5-REPD-line.txt.
- FINDINGS: Theorem REP-DEPTH: REP_F ≤ X_F + (1 + m_E + X_F)Σ_{d≤D_F}(n m_E)^d; [P-REP] ⇐ [P-WD] ∧ [P-X] (Corollary REPD-POLY, an implication).
- NEEDS: none from the owner.
