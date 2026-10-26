# N5 box 11, part 2 (L-SI successor 6): the straddling interval, its exact obstruction, and the reduction NJB ⇐ (P) ∧ NL=
L-SI successor 6 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~13:10Z (date -u). Lane write-up, unrefereed.
- Labels: PROVED (L-SI succ. 6); READING (lane; a proof sketch whose cited steps were checked against the source text, not a full
  proof); CONJECTURE; OPEN; DATA.
- Everything is on 𝒞^1O; the script asserts it. Not a running-time bound, not a TARGET.md claim, not a step-4 pass. G-N5-TIME stays OPEN.
- Context: packet P-N5-ENT (docs/si/P-N5-ENT-box11.md, sha1 4fd22be7) proves D_M ≤ 1 for every block, CONDITIONAL on (P). The only
  interval it leaves is the STRADDLING interval (f_i, f_{i+1}) of a block: r > M at f_i + 1, and r ≤ M at some later state of it.

## 1. The straddling interval, made exact (PROVED, L-SI succ. 6)
- Let (k0, k) := (f_i, f_{i+1}) be straddling, with L := M, and suppose it is dirty. Then:
  - (a) its first change j is a rise with r_j > L (R31 PL (b), R35 RDROP);
  - (b) with t1 := the first state of (k0+1, k] with r_{t1} ≤ L: j < t1, and r = L on [t1, k];
  - (c) every state of [k0+1, k] has r ≥ L.
- Proof.
  - (a) is PL (b) with RDROP.
  - (b) r_j > L forces j < t1. By FBW-S at the fallback k, r_k ≥ M_k = L. Fact R (r non-increasing along S) then gives r = L on [t1, k].
  - (c) follows from Fact R and r_k ≥ L. □
- So the straddle differs from P-N5-ENT's setting (Σ) only at the S4a steps s ∈ [t1, k) with r_s = L exactly.

## 2. The exact obstruction (PROVED, L-SI succ. 6, by reading the proof of R29 NL)
- R29 (e) Lemma NL (P-N5-CLS §5) assumes r_j > L. Its proof uses that hypothesis in ONE place, the key step (K*): for q ∈ R_j ∖ R̄_{j+1},
  "lev(Ξ_j q, W_j q) = r_j > L, so COARSE_L(Ξ_j q) ◁_L COARSE_L(W_j q)", which WM and (i) at q then contradict.
  - (i) reduces to (K*) through its minimal-failure argument. (ii) is (i) + (K*). (iii) is (i) + (ii) + TRANSFER + (A_j).
- At r_j = L, lev(Ξ_j q, W_j q) = L, so COARSE_L(Ξ_j q) = COARSE_L(W_j q), and (K*) gives nothing.
  - What is left open is a vertex q that leaves R at an S4a step with r_j = L while keeping its COARSE_L value, possibly carrying along
    a free vertex v that switched to q along a gate of level > L.
- Every other ingredient of P-N5-ENT uses r > L ONLY through NL (i)-(iii).
  - Checked against the texts: P-N5-ENT §0 (Σ2)-(Σ3), Lemma FZ, and through EV+ the R35 items NO-RF-OLD and ENT-SHAPE (1)-(4).
    Their proofs (P-N5-NJB §3-§4) cite r > L only to invoke OFFGATE + NL (iii) for (A_s) and NL (i)-(ii).
  - P-N5-RL EV and EV+ use NL (i)-(ii) and FLAT-ALL; FREE-FREEZE holds for every later state of the phase.
  - RB, WALK, CYC-EV and TEV-FB use only M_k ≤ L (CLS2), Lemma G and R15 (a) beyond FZ.

## 3. CONJECTURE NL= and the reduction
**CONJECTURE NL= (L-SI succ. 6, DATA).** R29 NL (i)-(iii) hold with "r_j > L" weakened to "r_j ≥ L".
- (NL= concerns only the case r_j = L; r_j > L is NL.)
**Reduction (READING, L-SI succ. 6).** (P) ∧ NL= ⇒ NJB in full (D_M = 0 for every block of every scope run). Hence, with (P) and NL=, every
scope run has ≤ n·n_E fallbacks of level ≥ 0.
- Sketch.
  - In a dirty straddling interval, §1 (c) gives r ≥ L on [k0+1, k]. With NL= in place of NL, the facts (Σ1)-(Σ6) of P-N5-ENT §0 hold
    verbatim.
    - (A_s) follows by OFFGATE at k0+1, then NL= (iii).
    - No leave follows from NL= (ii). M_k ≤ L is CLS2. B ≠ A follows from the rise at j.
  - Lemmas FZ, BF, RB, WALK, CYC-EV and Proposition TEV-FB then hold as proved there (§2: they use r > L only through NL).
  - EV+ needs NO-RF-OLD, ENT-SHAPE (1)-(4), EV and MERGE in the same setting with NL= in place of NL (§2). Then EV+ against TEV-FB is a
    contradiction, as in Theorem ENT-X.
  - So no straddling interval is dirty, and with P-N5-ENT's NJB-A and RDROP every interval is clean.
- Why a READING and not PROVED: the step "R35's NO-RF-OLD and ENT-SHAPE use r > L only via NL" was checked by reading P-N5-NJB §3-§4,
  not re-proved line by line under r ≥ L. A packet would restate those proofs under NL=.
- The gain over P-N5-ENT's D1 is a factor 2 in PL-S″ (n·n_E instead of 2·n·n_E). The polynomial bound for fallbacks of level ≥ 0 per scope
  run already holds without NL= (CONDITIONAL on (P)). So NL= is NOT on the critical path of G-N5-TIME.

## 4. DATA (DATA, not proof; experiments/si/tev/nleq.py, straddle.py; logs experiments/si/tev/logs/)
- nleq.py checks every in-scope S4a step s that follows a fallback k0 of the same scope run (the last one before s) with L := M_{k0} ≥ 0
  and r_s ≤ L, i.e. a step where NL is NOT available. At each it tests NL's three conclusions: (i) COARSE_L(Ξ) unchanged off R̄_{s+1};
  (ii) no leave; (A) gates into F_s of level ≤ L.

| set | steps | of which r = L | of which r < L | (i) fails | (ii) fails | (A) fails |
| --- | --- | --- | --- | --- | --- | --- |
| NAMED + experiments/red/so/instances/*.pg | 856 | 358 | 498 | 0 | 4 (all r < L) | 0 |
| LIB | 1,348 | 385 | 963 | 0 | 4 (all r < L; same 4) | 0 |

  - The 4 leaves: zcl_fb2_n32 at s = 28, 29 (L = 29, r = 27) and zcl_tp_n32 at s = 25, 26 (L = 31, r = 29). These are r < L, outside NL=.
  - At r = L: 743 steps, 0 failures of (i), (ii), (A). NL= survives on this data.
- Straddling intervals themselves: 0 (straddle.py: NAMED 290 block intervals, LIB 357; tev_cex_n40 15). So the reduction's hypothesis is
  vacuous in data, as with ENT-X.
- Target for L-RED: an S4a step with r_s = L (L the last fallback level of the scope run) at which a vertex leaves R. By §2 it must keep
  its COARSE_L value. This kills NL=. It does not kill NJB.
