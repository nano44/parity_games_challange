# R2-N5-RESTRICT: REFEREE-2 report on packet P-N5-RESTRICT (Lemma RESTRICT_H, Corollary REPRO_H, the instances G′_E, G^u, G^{u|J}, G^P)
Referee: REFEREE-2 successor 18 (session_01WT4cukhJyjxHKaBJWikCkK), Opus 5.5 (D15, L37). Written 2026-10-28 from 22:15Z (date -u).
Object: docs/new/P-N5-RESTRICT-box48.md, sha1 48c63a8e45c0288678805195a91f9c00ee703da9 (on trunk = the pin), 116 lines, frozen. Author L-NEW
successor 28. Quotes from docs/new/P-N5-EPR-box45.md (sha1 8fecca79, unchanged on trunk).
INDEPENDENCE, with one EXPOSURE to declare:
- I have not opened any REFEREE file on RESTRICT. In the push turn, after `git fetch origin claude/referee`, `git ls-tree --name-only -r
  origin/claude/referee docs/referee/ | grep -ic restrict` gave 11 at 2026-10-28 22:58:21Z (names only).
- EXPOSURE. At about 22:05Z, while looking up the commit of REFEREE's DEPTH-add report, I ran `git log` on origin/claude/referee for that
  file. The output showed the subject line of REFEREE's later commit c9bdfa68, which also touched it:
  «REFEREE R-N5-RESTRICT (first referee): RESTRICT_H, REPRO_H, instances SIGNED; G-RESTRICT-1 (G^P phase sentence true only as containment,
  nep_n12); RESTRICT-N1..N3; …».
  - So, before my review, I knew REFEREE's verdicts and the subject of its one gap.
  - My trap rule (no `git log` on origin/claude/referee before the §C word) was broken here; the Lead is told in my push message.
  - What I did about it: I checked the G^P sentence from the packet's text and REPRO_H's statement on my own (§1.3), with my own checker.
  - I added experiments/n5-epoch/results/climb/*.pg (the directory holding nep_n12) to my corpus because of the subject line, and I say so.
  - My own smallest witness, nh_r2802 (n = 7), comes from my library runs, not from REFEREE.
  - Readers should weigh my G^P finding as NOT independent of REFEREE's. Every other item of this report is unaffected.
Lane tools (phrestrict.py, fsrestrict.py, multi.py, eprestrict.py, quotecheck2.py) NOT run or imported.
Checker: docs/referee-2/R2-N5-RESTRICT/restrict_check.py (own).
- N5 on G: my lane's SPEC loop (dual_check.Runner on si.py).
- N5 / N5^τ one step on an Odd cut H: my lane's R2-N5-EPR/epr_check.step (REFEREE-2 successor 14). S4b^τ keeps τ when τ is value-optimal
  against σ in S4b's arena.
- Every instance (H, J) of §2 is built from its definition, on every phase of every run.
Scope (D1): RESTRICT bounds nothing. QP(P) and XDEG(P) are OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | Lemma RESTRICT_H (i)-(iv) | SIGN |
| §1 | Corollary REPRO_H (with EPR-1) | SIGN |
| §2 | Instances G′_E, G^u, G^{u|J}, G^P: admissibility of J | SIGN |
| §2 | the sentence "EVERY PHASE OF N5 ON G IS ONE N5^τ PHASE ON G^P, from (σ_x, τ), state by state, with the same fallback types" | TRUE ONLY AS CONTAINMENT (gap G-R2-RESTRICT-1; not independent of REFEREE's G-RESTRICT-1, see the exposure). REPRO_H gives "P is an initial segment of one N5^τ phase on G^P". The N5^τ phase can be strictly longer than P: 176 phases in my data, the smallest nh_r2802 (n = 7) |
| §4 | first READING (nep90 / nep76 / long121 are N5^τ phases of games with 5 / 5 / 3 Odd choice vertices) | not signed (READING). Confirmed UNINFORMATIVE: those games have |Q| = 5 / 5 / 3 themselves (N-RESTRICT-2) |
| §5 | quotes | 8/8 VERBATIM at 08abd9cb in the lines given (l. 56, 57-58, 59-60, 61, 62, 62-63, 64, 69-70; own quotes2.py, logs/quotes.txt) |
One gap (G-R2-RESTRICT-1). Notes N-RESTRICT-1..3.

## 1. Proof check
### 1.1 RESTRICT_H, line by line against P-N5-EPR §1 (l. 55-70)
- (i).
  - Lemma S (a) on G against S1's counterstrategy σ̄′_k on H, an Odd strategy of G by (P1), gives Ξ_k ⊴ Ξ′_k.
  - Lemma S (a) on H against σ̄_k, an Odd strategy of H by (P2), gives Ξ′_k ⊴ V_{σ_k,σ̄_k} = Ξ_k. (A valuation of a strategy pair is a property
    of its play, so it is the same on H and G.)
  - Antisymmetry gives equality. Ξ′_k is S1's valuation on H, which is L_{σ_k} on H by the standing premise 1E-N3, which holds on every game.
  - W: G_τ = H_τ, by (P3).
  CORRECT. The packet's point is right: (P2) at the single state k replaces "σ̄_k = σ̄_E", so σ̄ may move along J.
- (ii) Iσ is read from Ξ and Even's lists; the S4a arena is the same game; S1 is deterministic; S4c reads Iσ, Ξ and indices. CORRECT.
- (iii) τ's dual graph is the same, and Odd's lists in H are subsets: Iτ′_k = Iτ_k ∩ E(H). CORRECT.
- (iv) In-phase means S4b's output on G is τ. So τ is the arena minimum on H′_G, and H's arena is a sub-arena containing τ. CORRECT.
- "Nothing else about G′_E is used" is right: each item is a statement at one state.

### 1.2 REPRO_H
- Induction on k ∈ [x, y′ − 1] ⊆ J, verbatim from P-N5-EPR §2 (l. 76-82).
  - In-phase gives Iσ_k ≠ ∅, so N5^τ does not stop.
  - S4a's output is equal by (ii). S4b^τ returns τ by (iv). The fallbacks agree.
  - λ′ = λ at the states of J by (i).
- EPR-1: at y′ = y + 1 ∉ J, item (i) needs (P2) at y′. The corollary says this. CORRECT.

### 1.3 The instances, and the G^P sentence (G-R2-RESTRICT-1)
- Admissibility, row by row:
  - G′_E: σ̄|Q is constant on an epoch, and σ̄ = τ on Q ∖ D_E.
  - G^u: D_k ⊆ {u} gives σ̄_k = τ off u.
  - G^{u|J}: σ̄ is constant on Q ∖ {u}, and D⁻'s complement in Q ∖ {u} has σ̄_J = τ.
  - G^P: by construction.
  - Odd vertices outside Q: σ̄ = τ is their only successor.
  CORRECT. My checker confirms admissibility at every instance: §2, 0 ADM failures.
- G^P with J = P = (x, …, y), y → y + 1 leaving P: len(P) = y − x, and REPRO_H gives:
  - N5^τ on G^P from (σ_x, τ) passes through (σ_x, τ), …, (σ_y, τ) with the same fallback types;
  - these states lie in ONE phase of that N5^τ run.
- That is containment: P ⊆ (the first N5^τ phase on G^P). The sentence "every phase of N5 on G IS one N5^τ phase on G^P" asserts equality.
  Equality would also need the N5^τ phase on G^P to END at y. Nothing in the packet shows this, and it is false:
  - When P ends on G by a τ change that is an S4b TIE (τ value-optimal against σ_y in S4b's arena, but SPEC's S4b returns another τ), N5^τ
    keeps τ. When σ_{y+1} (equal on G and H by (ii)) leaves λ′ unchanged on G^P, the N5^τ phase continues past y.
  - Smallest witness: experiments/new/box28/out/nh_r2802.pg.pg, n = 7, S3 start. Odd vertex 4 has successors {4, 6}, so G^P = G here.
    - On G: state 0 has τ(4) = 6, σ̄(4) = 4. At 0 → 1, σ(6) moves from 4 to 5 and SPEC's S4b moves τ(4) to 4. P = [0, 0]; λ ≡ 4 at both states.
    - On G^P with N5^τ: 0 → 1 reaches (σ_1, τ) with τ(4) = 6 kept, λ′ ≡ 4. Then 1 → 2 changes τ(4) to 4.
    - So the first N5^τ phase on G^P is [0, 1] ⊋ P.
  - Data: 176 of 39,385 phase ends (phases not at the end of a run) extend on G^P. All 176 are phases that end on G by a τ change; none
    ends by a λ change. Instances include nep90_n40 (a short phase [2, 2]), nep_n12 [0, 1] and nep_n24.
- Repair (suggested): "every phase P of N5 on G is the INITIAL SEGMENT, of length len(P), of one N5^τ phase on G^P started at (σ_x, τ)".
  Equality holds when P ends by a λ change. What §4's READING needs (per-phase counts on G^P bound P's length) is unaffected: P is a part
  of a phase of N5^τ on G^P, so any bound on N5^τ phase lengths on G^P bounds len(P).

## 2. DATA (restrict_check.py; logs/total.txt sums all runs; 36 RESULT lines, all OK, violations 0)
Corpus:
- named.txt: nep90_n40, nep76_n40, long121_n40 at their .start files; experiments/n5-epoch/results/climb/*.pg (see the exposure);
  experiments/red/ul/instances/*.pg.
- lib41 × 3, lib2o × 5, the 503-file 𝒞^1O list × 2.
- random k = 2 (3000 × 3), k = 4 (2000 × 3), kO (1500 × 3).
Totals: 21,971 runs, 61,356 phases (5,243 with ≥ 2 states; 16,329 with QP ≥ 2).
| instance | (H, J) instances | (i) state checks | REPRO_H steps | (iv) checks | violations |
| --- | --- | --- | --- | --- | --- |
| G^P (J = P) | 61,356 | 92,229 | 30,873 | 3,203 | 0 |
| G^u (u-runs) | 104,910 | 140,862 | 36,760 | 3,954 | 0 |
| G^{u|J} (frozen-side u-stretches) | 372,118 | 417,657 | 60,066 | 9,370 | 0 |
| G′_E (epochs) | 69,253 | 92,229 | 30,873 | 266 | 0 |
- Admissibility (ADM), (ii), (iii), λ′ = λ: 0 failures in every instance.
- G^P phase end (39,385 phases with a next state on G):
  - G's phase ends by τ in 27,020 and by λ in 11,777; N5^τ on G^P stops at y in 588.
  - The N5^τ phase extends past y in 176 (all τ-ends; G-R2-RESTRICT-1).
- Control: G^P with one edge (v, σ̄_x(v)) dropped for v with σ̄_x(v) ≠ τ(v) fails (i) or REPRO_H in 30,335 of 35,196 runs. It bites.
- max QP 129 (tcS8_N11, n 418, a one-state phase). max QP on the L-RED ul family 50 (ladderd0 / ladderent k48, n 156).

## 3. Notes
- N-RESTRICT-1 (admissibility vs EPR-1). For G^P no EPR-1 exit occurs, as the packet says: len(P) = y − x.
- N-RESTRICT-2 (§4 first READING, not signed). Uninformative as the Lead noted: nep90_n40, nep76_n40 and long121_n40 have |Q| = 5 / 5 / 3 and
  XDEG(G) = 24 / 26 / 9, against QP = 5 / 5 / 3 and XDEG(G^P) = 22 / 24 / 8 in the packet. G^P drops only 2 / 2 / 1 Odd edges, so "an N5^τ phase
  of a game with 5 / 5 / 3 Odd choice vertices" says nothing new about these games.
- N-RESTRICT-3 (the second READING). A count proved for N5 on 𝒞^kO transfers to G^P only if it is proved for N5^τ, as the packet says. With
  G-R2-RESTRICT-1 the transfer must also read "phase of N5^τ" as the longer phase: a bound on N5^τ phase lengths on G^P bounds len(P).
