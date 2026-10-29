# R2-N5-FBCK: REFEREE-2 report on packet P-N5-FBCK (box 49): Facts K1-K3, FB-RISE^K, SAT^K, SAT-FB^K, SAT-FB1^K, Theorem FB-C^K, Corollaries (i), (ii)
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-29 from 00:15Z (date -u).
Object: docs/new/P-N5-FBCK-box49.md, sha1 7747ecf23f65ac82fc2d75e0f6ecc28c7621ce1f (measured with `git show <ref>:<path> | sha1sum` at l-new 0e63596d,
origin/claude/l-new and trunk: all equal the pin), 131 lines, frozen. Author L-NEW successor 30.
INDEPENDENCE:
- I have not opened docs/referee/R-N5-FBCK.md and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic fbck`: 14 at 2026-10-29 00:13:33Z; 14 at 2026-10-29 00:42:38Z (push turn, after `git fetch origin claude/referee`). Names only.
- Declared read: the packet quotes REFEREE's READER report as the premise of Corollary (ii). I read its verdict table and §1 setting and
  Lemma (a) (docs/referee/R-N5-READER.md @ e83fd19d, l. 1-30) to check that implication. That file is on another packet (READER), not on FBCK.
Lane tools (experiments/new/box49/fbconf.py, quotecheck3.py, the rest of box49/*.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-FBCK/fbck_check.py, percase.py; quotes with ../R2-N5-CORE/qcheck.py; run_all.sh; logs/.
- N5 on G: my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py = SPEC S1, read-only).
- Ξ: my own play value of (σ, σ̄), with the ENGXI cross-check against the engine.
- K, n_K, Q_K, K-configurations, H^K_C and LEV^K_C are computed from §0's definitions. LEV^K_C is EXACT by enumeration of simple H^K_C-paths.
  Over budget, iterative deepening gives min(LEV^K_C, D) exactly, and only the checks that this decides are run.
Scope (D1): a REDUCTION of f to |𝒞^K_f(P)|. The count |𝒞^K_f(P)| is not bounded (FB-LIN OPEN). FB-C° in the read frame stays OPEN. Not a TARGET.md
claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §0 | Facts K1-K3 | SIGN |
| §0 | LEV^K_C ≥ 0 and non-decreasing on P (setting sentences) | SIGN |
| §1 | Lemma FB-RISE^K | SIGN |
| §1 | Lemma SAT^K | SIGN |
| §1 | Lemma SAT-FB^K | SIGN |
| §1 | Corollary SAT-FB1^K | SIGN |
| §2 | Theorem FB-C^K | SIGN |
| §2 | Corollary (i) | SIGN |
| §2 | Corollary (ii) | SIGN AS AN IMPLICATION from its three bullets, with "the run on the old vertices" read to include σ̄ on the old vertices. READER-INV supplies the third bullet only for ONE added Odd vertex with no predecessors, not for a general set H (N-FBCK-1) |
| §5 | quotes | 9/9 VERBATIM in the tagged lines (own qcheck.py; SHIFT=1 control 0/9) |
| §3, §4 | READING / OPEN / DATA | not signed. §2 (ii)'s and §3's instance numbers reproduced (§2 below) |
No gap. Notes N-FBCK-1..5.

## 1. Proof check against RESULTS R71 and R73 (landed text on trunk) and their source proofs
### 1.1 Setting, K1-K3
- K1: a successor of a vertex reachable from an Even choice vertex is reachable from it. The honest play from x ∈ K and λ(x) stay in K. ✓
- K2: an Even vertex of out-degree ≥ 2 is in K by the 0-edge path, so an Even x ∉ K has one successor and Iσ(x) = ∅ by S2. ✓
- K3: an in-phase fallback is Even's (FIX 3) and needs Iσ ≠ ∅, so K ≠ ∅. ✓
- Data, 0 failures:
  - K1: closure, plays staying in K and λ(x) ∈ K, at every state of every run.
  - K2: no improving edge outside K at every state.
  - K3: 409 + 267 + 6,434 phases with K = ∅, none holding a fallback.
- H^K_C vs R71's H_C. By K1 a path of H_C from x ∈ K never leaves K, so the H^K_C-paths from x are exactly the H_C-paths from x.
  - So LEV^K_C is R71's condition restricted to x ∈ K, with the cap n_K − 1 instead of n − 1.
  - The cap is right: a simple path in G[K] has ≤ n_K − 1 edges.
  - Only C on Q_K is ever read.
- LEV^K_C ≥ 0: a 0-edge path is x = u with λ(u) = u, and Ξ_k(u) = (u, ∅, 0) on the phase. Non-decreasing: (MON) with H^K_C and λ fixed. ✓
  (Checks LEV0, MONO.)

### 1.2 FB-RISE^K (against R71 (a) and P-N5-FBC-box47 §1 l. 47-56; HONFF §1 items 2-3)
- Every vertex the proof names lies in K by K1:
  - x and z, and r′;
  - in the Odd case, σ̄_t(x) = C(x) for x ∈ Q_K, or the unique successor;
  - in the Even case, σ_t(x), z*(x) and z.
- So R71's argument applies verbatim with x restricted to K.
- The Odd case uses the configuration only at x ∈ Q_K, which is exactly what "K-C-state" fixes.
- The Even case is R71 (a)'s Even case. R71 (a)'s landed text says it "holds at any source state". Items 2 (Case A with Ω := Ξ_t, ρ := σ_t; Q-A
  YES by both referees of R70 / R71) and 3 (3a by (V1)/(V2) at t + 1; 3b different cycle nodes) read only Ξ_t / Ξ_{t+1} at x, σ_t(x), z*(x),
  z and value(r′).
- ✓ Data:
  - RISE exact at 276 (lib41) + 213 (lib41 dressed) + 6 (named) + 6,249 (random sets) sources; in deep mode at 401 + 352 + 98 more;
    426 + 322 + 13 undecided (LEV at the source reached the cap D).
  - Odd case ODDC at every K-C-state: 1,253 + 1,019 + 39 + 13,258 exact, and 2,310 + 2,042 + 785 in deep mode.

### 1.3 SAT^K (against R71 (b), first part only)
- At a K-C-state the honest play from x ∈ K follows a simple H^K_C-path to λ(x), so Ξ_t(x) = value(r_x) ⪯ B^K_C(x).
- LEV^K_C = n_K − 1 gives ⪰ on K.
- At a later K-C-state t′: Ξ_t = B^K_C ⪰ Ξ_{t′} ⪰ Ξ_t on K. By (MON), Ξ is constant on K on [t, t′].
- ✓ The 4n(n − 1) window of R71 (b) is not used, and the packet does not claim it.
- Data: SAT (Ξ = B^K_C on K) and SAT_const at every saturated K-C-state, 0 failures; XIB at every K-C-state.

### 1.4 SAT-FB^K (against R73 (d) and P-N5-EPC-box48 §3 l. 97-107)
- Assume a K-C-state t′ > t. SAT^K gives Ξ_{t+1} = Ξ_t on K.
- Iσ_{t+1} = ∅:
  - Even x ∉ K by K2.
  - Even x ∈ K: succ(x) ⊆ K, so S2 at t + 1 reads only Ξ_{t+1} = Ξ_t on succ(x). R73's two cases then hold. In the second, a w ∈ succ(x)
    with Ξ_t(w) ≻ Ξ_t(z*) would lie in Iσ_t(x), against z* being the maximum.
- The last step reads S4a / S4b / S4c / S5 and FIX 3 directly, as R73's landed text has it after fixes R6. The packet does not cite HON-FB
  here. ✓
- This is the one place where restricting to K needs care: R73 had Ξ_{t+1} = Ξ_t on ALL of V. Here equality holds on K only, and K1 and K2
  are exactly what make it enough.
  - Control open1 (K replaced by the non-closed K′ = Even choice vertices + their successors) breaks SAT, SAT-FB and SAT-FB1: 795 + 418
    SAT, 1 + 1 SATFB, 1 SATFB1 failures.
  - So the closure of K is used, and it is not cosmetic.
- SAT-FB1^K: as R73's SAT-FB1. ✓
- Theorem FB-C^K: as R73's FB-C′, per C at most n_K − 1 unsaturated sources (strictly rising LEV^K_C in {0, …, n_K − 2}) and 1 saturated. Each
  source has exactly one K-configuration, so summing over C gives f. ✓
- Corollary (i): n_K ≤ n, and restriction to Q_K maps 𝒞_f(P) onto 𝒞^K_f(P). ✓ (COR1 checked in every fallback phase.)

### 1.5 Corollary (ii)
- From its three bullets the conclusion follows:
  - K(G′) = K(G): no new Even choice vertex, and no old vertex reaches H.
  - n_K is unchanged, and so is Q_K.
  - f and the phases are unchanged by hypothesis.
  - 𝒞^K_f(P) is unchanged IF σ̄′ = σ̄ on Q_K at every fallback source.
- That last condition is part of "the run on the old vertices unchanged" only when the run is taken to include σ̄. I sign it with that reading
  (N-FBCK-1).
- READER-INV (REFEREE, at e83fd19d l. 14 and §1) is stated for G′ = G plus ONE Odd vertex o with no predecessors. Its one-state Lemma (a) gives
  Ξ′ = Ξ and σ̄′|V = σ̄ on V, and under (R) the run, fallbacks and phases are unchanged. So for H = {o} the third bullet, σ̄ included, is
  supplied, and Corollary (ii) holds for that case.
- For a general H (several readers, forced Even vertices in H, edges inside H) READER-INV does not state the third bullet. The corollary is
  then a pure implication. It is not an application of READER-INV.

## 2. Data (own checker; every non-mutation run 0 violations)
| corpus | runs | fallback phases (with n_K < n) | f | Σ \|𝒞_f\| / Σ \|𝒞^K_f\| | sources checked exactly / deep / undecided | saturated sources |
| --- | --- | --- | --- | --- | --- | --- |
| named (9 box49/inst dressings, si/root/instances 7, nep90_n40, long121_n40; BUDGET 3e6) | 18 | 15 (7) | 117 | 78 / 75 | 6 / 98 / 13 | 0 |
| lib41_noref × 3 starts | 1,230 | 240 (25) | 1,103 | 299 / 297 | 276 / 401 / 426 | 36 |
| lib41 dressed: +5 new vertices (70 % Odd, out-deg 2-3; Even out-deg 1; no old → new edge) × 2 starts | 820 | 205 (205) | 887 | 414 / 257 | 213 / 352 / 322 | 20 |
| random dressed k4, n 8-18, +6 (20,000 × 3) | 60,000 | 1,743 (1,743) | 1,745 | 1,743 / 1,743 | 1,745 / 0 / 0 | 1,729 |
| random dressed kO, n 8-18, +6 (20,000 × 3) | 60,000 | 1,944 (1,944) | 1,944 | 1,944 / 1,944 | 1,944 / 0 / 0 | 1,926 |
| random k2, n 6-16 (20,000 × 3) | 60,000 | 1,712 (1,155) | 1,712 | 1,712 / 1,712 | 1,712 / 0 / 0 | 1,702 |
| random kO, n 8-20 (10,000 × 3) | 30,000 | 847 (610) | 848 | 848 / 848 | 848 / 0 / 0 | 831 |
- THM (f ≤ n_K·|𝒞^K_f|) and CNT (≤ n_K sources per K-configuration) are decided in every fallback phase. They do not need LEV.
- Largest ratios:
  - sources per K-configuration over n_K: 0.75 (wd16_s2: 12 of 16; ccl_fbx_n32+5: 24 of 32);
  - max |𝒞^K_f|: 4 (zcl_rx_n32), 8 (l121_cf_emb12).
- §2 (ii) / §3 instance claims reproduced (percase.py, own engine, given starts; phase [1, 122], f = 8 in each):
  - l121_cf35_39: n 41, n_K 40, |𝒞_f| 8, |𝒞^K_f| 5;
  - l121_cf_emb12: n_K 41, |𝒞^K_f| 8 = f;
  - long121_n40, l121reader_n41, l121_a / _b / _e100: |𝒞^K_f| 5;
  - swlin_kill_n26: 6 fallbacks, |𝒞^K_f| 3.
- Dressing works as intended: on lib41 + 5, 76 fallback phases have |𝒞^K_f| < |𝒞_f| (Σ 414 → 257), and the theorem holds on all 205.
- Controls (FBCK_MUT, on the dressed k4 and the kO random sets):
  - plus2 (FB-RISE^K with + 2) bites 4 + 6 (RISE);
  - tau (Odd vertices of Q_K cut to τ instead of C) bites 263 + 264 (ODDC 18 + 24, RISE 9 + 12, SAT 6, XIB);
  - open1 (non-closed K′) bites 2,528 + 1,281 (SAT, SATFB, SATFB1, XIB);
  - nk1 ((n_K − 1) per configuration) does NOT bite (N-FBCK-3).

## 3. Notes (not gaps)
- N-FBCK-1 (Corollary (ii)'s scope).
  - The packet's parenthetical "READER-INV gives this for a reader satisfying (R)" is right for ONE Odd reader o with no predecessors
    (READER-INV's setting). It is not right for the corollary's general H.
  - Two points should be said in the corollary:
    - "the run on the old vertices" must include σ̄|V (READER-INV's Lemma (a) has it), since 𝒞^K_f reads σ̄ on Q_K;
    - for |H| ≥ 2, or Even vertices in H, the third bullet is an assumption, not a consequence of READER-INV.
  - Repeated single-reader additions would need each new vertex to have no predecessors when it is added (H acyclic, added sinks first), and
    (R) at each step. That is not proved here.
- N-FBCK-2 (the K version is a restriction, so the proofs transfer).
  - Every R71 / R73 step reads Ξ and the frame only at x, its successors and the vertices of r′, all in K by K1.
  - The single step needing more than restriction is SAT-FB^K's Iσ_{t+1} = ∅, where K1 (succ(x) ⊆ K) and K2 (no Even choice outside K) carry
    it.
  - The open1 control shows that without closure SAT^K and SAT-FB^K fail.
- N-FBCK-3 (thin spots).
  - The theorem's bound is never approached: at most 0.75·n_K sources per K-configuration, and nk1 does not bite.
  - SAT-FB^K's alternative "P has no K-C-state after t" never occurs on its own. In every saturated case (36 + 20 + 6,188), a later K-C-state
    exists and t + 1 is the last state of P.
  - Random games give mostly one saturated fallback per phase. The unsaturated sources come from the library sets (240 + 193 exact, more in
    deep mode).
- N-FBCK-4 (premise list).
  - The premises match R71's and R73's landed claim lines. The packet uses R71 (b)'s first part only, so the R15 (d) / R57 (a) window that R71
    (b) adds is not needed.
  - R73's SAT-FB last step is cited in its post-fix (R6) form, without HON-FB.
  - The standing premise 1E-N3 (P1) and Q-A are named.
  - The quote base 6d863a4d is older than trunk. The quoted R71 (a), (b) sentences are unchanged in RESULTS at trunk 908e4333 (l. 3712 then,
    a later line now).
- N-FBCK-5 (§4 vs mine, not to sign).
  - On lib41 my Σ |𝒞_f| / Σ |𝒞^K_f| is 299 / 297 against §4's 303 / 301 (different random starts; 1,230 runs vs 1,047).
  - Max fallbacks per K-configuration: 0.75 n_K on wd16_s2 in both.

## 4. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-FBCK/{fbck_check.py (modes files / pairs / random / dress / dressfiles / start; deep mode; MUT plus2, tau,
  open1, nk1), percase.py, named.lst, run_all.sh, logs/}.
- FINDINGS:
  - K1-K3, FB-RISE^K, SAT^K, SAT-FB^K, SAT-FB1^K, FB-C^K and Corollary (i): all SIGN, no gap.
  - Corollary (ii) SIGN as an implication, with σ̄|V in "the run unchanged". READER-INV covers only a single Odd reader (N-FBCK-1).
  - The closure of K is needed (open1 control); FB-RISE^K's +1 is the right step (plus2 bites).
- NEEDS: Lead: the §C word (REFEREE's R-N5-FBCK.md exists; not opened); route N-FBCK-1..5 to L-NEW.
