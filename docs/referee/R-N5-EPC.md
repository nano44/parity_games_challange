# R-N5-EPC: REFEREE report on packet P-N5-EPC (L-NEW box 48: FB-RISE_C and SAT_C restated, Lemma RET-FB, Corollary VIS, Theorem EP-C, Lemma SAT-FB, Corollary SAT-FB1, Theorem FB-C′, Corollary EP-ASM, the D-change remark; every game)
Referee: REFEREE (successor 15), Opus 5.5 (owner ruling D15). FIRST referee (Lead brief 15:08Z, Lead stamp). REFEREE-2 successor 17 reviews in parallel.
- Object and pin: docs/new/P-N5-EPC-box48.md, sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700, 185 lines, author L-NEW successor 27. Pin
  check: the same sha1 on my tree, at the l-new freeze 81ab0b72 (the commit that adds the file), and at every trunk commit from the l-new
  merge da109c4d to cf372dec (the trunk head at my fetch; all ancestors of HEAD). The packet's quote base, trunk f4562054, is an ancestor of
  the freeze 81ab0b72, and my FBC report 0addfc5f (quoted in §3 and §7) is an ancestor of f4562054.
- Written 2026-10-26T15:12Z-15:52Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: no docs/referee-2/ file on EPC on my tree, on trunk or on origin/claude/referee-2 at any of my fetches
  (re-listed in the same turns; 0 / 0 / 0 at 15:52Z). No lane code run (experiments/new/box48/*.py neither executed nor imported; lane start files read as
  data). D1.
- Premises read against their text: SPEC S2, S4a ("Else σ_new = σ."), S4b, S4c, S5, FIX 3 (docs/new/N5-ssi-global.md); RESULTS R15 (a), (d);
  R17 (a) (V1)/(V2), box 10 §2 Case A; R38 (a); R57 (a) (VJ) and 1E-N3; R60 (c); R64 / R63 (epoch); R68 (X_dir, X_big, T*_Q := max_u
  T*(G^u), R51 (a)'s bound, (Στ), HON-FB (iv)); P-N5-HONFF (signed by both, no gap): FB-RISE (a) items 2-3, Q-A, HON-0-FF (b), REC-1-FF (c);
  P-N5-FBC (both referees' §Cs: all signed, no gap) for §1.
- Quotes and pins: all 24 curly-quoted passages (22 in §7 and the 2 of §5, which repeat §7's) verbatim (whitespace normalised) at
  f4562054, each ending at the cited line (my scratch/fbc_quotes.py). Pins: P-N5-HONFF 98101d1f, P-N5-HONFF-fixes ccc520dd, P-N5-FBC
  32d3776c (at f4562054 and 81ab0b72); long121_n40.pg c667c085, .start d750664a (at 81ab0b72): all match.
- Tool: scratch/epc_probe.py (own engine rl_engine; exact LEV_C for every configuration C visited in the phase, by simple-path enumeration in
  H_C with a budget; checks in §6). Logs scratch/epc_logs/.

## Verdicts (sign-off line per item)
| § | statement | verdict (Opus 5.5, D15) |
| --- | --- | --- |
| §1 | Lemma FB-RISE_C (restated with proof) | SIGNED (identical to P-N5-FBC's, signed by both referees) |
| §1 | Lemma SAT_C (1), (2) (restated with proof; the 4n(n − 1) window left to VIS (a) with R15 (d), R57 (a)) | SIGNED |
| §2 | Lemma RET-FB | SIGNED |
| §2 | Corollary VIS: V_C ≤ 2n² − n + R⁰_C | SIGNED |
| §2 | Theorem EP-C: N_ep ≤ NCONF·(2n² − n) + R⁰, and R⁰ ≤ Σ_S REV(S) | SIGNED |
| §3 | Lemma SAT-FB | SIGNED |
| §3 | Corollary SAT-FB1 | SIGNED |
| §3 | Theorem FB-C′: f ≤ n·\|𝒞_f(P)\| | SIGNED; EPC's own proof stands WITHOUT my FBC-N3 route (no R15 (b), no R38 (f) CN-LAST); §3 below |
| §3 | Consequences bullet (f ≤ n·N_ep implies R60 (c); n·Δ^k on 𝒞^kO; n(1 + m) if all \|D_k\| ≤ 1) | SIGNED (with P-N5-FBC (b), (c)'s counts) |
| §4 | Corollary EP-ASM | SIGNED as an assembly; its second term SIGNED AS AN IMPLICATION from (Στ); which terms are bounded: §4 below |
| §5 | remark: (D changes) + 1 ≤ N_ep | SIGNED |
| §5 | DEAD "a fallback from a saturated C-state is flat and ends the phase" | CONFIRMED DEAD (data item, reproduced on rho3_253_n32 at L-RED's start file) |
| §6 | data, open items, READINGs | not signed (as briefed) |
No gap. Notes EPC-N1..N4. Nothing here bounds N_ep or N5's running time on general games (EP-ASM leaves four quantities open, §4); not a
TARGET.md claim; G-N5-TIME stays OPEN.

## 1. §1, restated lemmas
FB-RISE_C's text and proof are P-N5-FBC's (both referees signed it, joint gap map empty; REFEREE-2's N-FBC-1 / N-FBC-2 apply here too: LEV_C ≥ 0
at every state, and the Even case needs no C-state). SAT_C (1), (2) as restated drop the window bound; (2) uses only (1)'s first half at t′
and (MON) ✓. The window t′ − t ≤ 4n(n − 1) is used only in VIS (a), with R15 (d) and R57 (a) named as its premises ✓ (this answers my FBC-N2
for this packet).

## 2. RET-FB, VIS, EP-C, re-derived (parentheticals checked one by one)
- RET-FB ✓. L := min(LEV_C(t) + 1, n − 1); induction on |r| for simple H_C-paths r from y to a cycle node u of λ, |r| ≤ L, at the C-state s.
  - |r| = 0 ✓ (λ fixed on P, Ξ_s(u) = (u, ∅, 0)).
  - y Even ✓: |r′| ≤ L − 1 ≤ LEV_C(t), so Ξ_t(z) ⪰ value(r′) "(LEV_C(t) ranges over all vertices, at every state)" ✓. Items 2 and 3 of FB-RISE
    (a), in H_C, give Ξ_{t+1}(y) ⪰ value(r) "(They do not need t to be a C-state …)" ✓ (they read only G's edge (y, z), the bound on Ξ_t(z),
    S4c's maximum, Case A with Ω := Ξ_t, (MON), (V1)/(V2) at t + 1 and λ_{t+1} = λ; REFEREE-2's N-FBC-2 on P-N5-FBC). Then (MON) to s ✓
    ("t + 1 ≤ s, both in P").
  - y Odd ✓: s is a C-state, so σ̄_s(y) = σ̄_C(y) = z, the only H_C-edge at y; the induction hypothesis at s for r′ (|r′| < |r|) gives
    Ξ_s(z) ⪰ value(r′); the Odd case of §1 at s ((V1), (V2); or the own-cycle-node comparison) gives Ξ_s(y) ⪰ value(r) ✓. The induction is
    on |r| at the fixed state s, and the Even branch does not call it (it bounds Ξ_s directly), so it is well-founded ✓.
  - "At a non-C state an Odd vertex with σ̄ ≠ C can sit below its H_C-paths" ✓ (my MUT=2, RET read at every later state, fails 251 times).
- VIS ✓. Returns of C split into (a) LEV_C(s_i) = n − 1: all i ≥ i₀ (LEV_C non-decreasing); SAT_C (2) + R15 (d) put every later C-state within
  4n(n − 1) of s_{i₀}; two C-epochs are separated by a non-C epoch, so s_{j+1} ≥ s_j + 2 and V_C − i₀ ≤ 2n(n − 1) ✓. (b) LEV_C(s_i) ≤ n − 2 with
  a fallback source t ∈ [s_i, s_{i+1}): RET-FB at s_{i+1} ≥ t + 1 and LEV_C(t) ≥ LEV_C(s_i) (MON) give a rise of LEV_C(s_·) by ≥ 1, from values
  in {0, …, n − 2}: ≤ n − 1 ✓. (c) the rest, R⁰_C ✓. 1 + 2n(n − 1) + (n − 1) = 2n² − n ✓.
- EP-C ✓. Epochs are partitioned by their configuration, N_ep = Σ_C V_C ✓. A return in R⁰_C has no fallback source in [s_i, s_{i+1}), so the
  states s_i, …, s_{i+1} lie in one maximal fallback-free run S; per S and configuration with V′ epoch starts in S, ≤ V′ − 1 such returns; sum:
  REV(S) ✓; fallback-free runs number ≤ f + 1 ✓.

## 3. SAT-FB, SAT-FB1, FB-C′ (and the Lead's question)
- SAT-FB ✓. With a C-state t′ > t: SAT_C (2) gives Ξ_{t+1} = Ξ_t ✓. Iσ_{t+1} = ∅ ✓: an Even x with Iσ_t(x) = ∅ keeps σ_t(x) and, Ξ being equal,
  Iσ_{t+1}(x) = Iσ_t(x) = ∅; a switched x has σ_{t+1}(x) = z*(x), and any w with Ξ_t(w) ≻ Ξ_t(z*) ≻ Ξ_t(σ_t x) would be in Iσ_t(x) (w ≠ σ_t(x),
  strictly better than it) with a larger value than the maximum z* — impossible ✓. At t + 1: if Iτ = ∅ too, N5 stops (S5); else S4a keeps σ
  ("Else σ_new = σ."), and S4b changes τ or, if S4b returns τ, S4c fires for Odd (FIX 3: "Odd falls back only if Iσ = ∅") and switches some
  Odd vertex to an improving edge, changing τ ✓ — HON-FB (iv)'s argument (R68 (c)) ✓. τ is constant on P, so t + 1 is P's last state ✓.
- SAT-FB1 ✓ and FB-C′ ✓ (unsaturated ≤ n − 1 by FB-RISE_C and monotone LEV_C ≥ 0; saturated ≤ 1; N ≤ n per C).
- The Lead's question: EPC's proof of FB-C′ stands on its own. It uses SAT_C (2) (which uses only (MON) and SAT_C (1)), S2, S4c's maximum,
  S4a's else-branch, S4b, S4c / FIX 3 for Odd, S5 and FB-RISE_C. It uses neither RESULTS R15 (b) nor R38 (f) CN-LAST, i.e. not my FBC-N3
  route. The two proofs differ exactly at the last-state step: mine derives it through "Ξ-flat ⇒ every gate is a length-only switch at a
  cycle node ⇒ CN-LAST"; EPC's shows directly that no improving edge survives an S4c step that leaves Ξ unchanged. EPC's is shorter and
  needs fewer premises. The packet's §3 remark describes my route correctly (its two quotes are verbatim at f4562054). The statement is the
  same: SAT-FB1 = FBC-N3's claim.
- SAT-FB's disjunction is needed (DEAD item, §5 of the packet): reproduced at L-RED's start file of experiments/red/fbr/instances/rho3_253_n32.pg
  (rho3_253_n32.start.json's n5py_start, read as data): phase [5, 33] has saturated fallbacks at t = 19, 20, 24, 25 that are neither Ξ-flat nor
  last, each leaving its configuration for good. With MUT=3 (SAT-FB read as the DEAD guess, no disjunction) my check fails 7 times there.
  This does not touch FBC-N3 / SAT-FB1: two saturated fallbacks of ONE configuration still cannot occur (0 SATFB1 failures).

## 4. EP-ASM: what is bounded and what is open (the Lead's question)
EP-ASM: N_ep(P) ≤ (4n² − 3n) + (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2) + NCONF_{≥2}(P)·(2n² − n) + R⁰_{≥2}(P). The split N_ep = N_0 + N_1 + N_{≥2}
by |D_E| is a partition of the epochs (D_E is a function of the epoch's configuration, τ fixed on P) ✓.
| term | what it bounds | status |
| --- | --- | --- |
| 4n² − 3n | N_0, the epochs with D_E = ∅ | BOUNDED, unconditionally: HON-0-FF (b) (P-N5-HONFF, signed by both, no gap) |
| (1 + 4n² − 3n + X_dir + X_big)·(T*_Q + 2) | N_1, the epochs with \|D_E\| = 1 | IMPLICATION from (Στ) (REC-1-FF (c), signed as such; holds at R65's audit strength). Inside it: 4n² − 3n bounded; T*_Q = max_u T*(G^u), R51 (a)'s bound, polynomial but very large (R68 limit (i)); X_dir and X_big OPEN (R68's open terms) |
| NCONF_{≥2}(P)·(2n² − n) | the epochs of configurations with \|D_C\| ≥ 2, except R⁰ returns | the factor 2n² − n is PROVED (VIS); NCONF_{≥2}(P) is OPEN (no bound here; the packet says so, §6) |
| R⁰_{≥2}(P) | fallback-free returns to configurations with \|D_C\| ≥ 2 at LEV_C ≤ n − 2 | OPEN (EP-C bounds R⁰ by Σ_S REV(S) over ≤ f + 1 fallback-free runs, itself not bounded) |
So EP-ASM is a REDUCTION of N_ep to four open quantities, X_dir, X_big, NCONF_{≥2}, R⁰_{≥2}, plus premise (Στ) for N_1 and R51 (a)'s large
polynomial T*_Q. It bounds N_ep on no class by itself; for phases with every |D_k| ≤ 1 it reduces to R68 / REC-1-FF's form (NCONF_{≥2} =
R⁰_{≥2} = 0, X_big = 0). The READING in §4 ("RESULTS R61 (f)'s ρ count is not used") is accurate.

## 5. §5 remark
(D changes) + 1 ≤ N_ep ✓: τ is fixed on P, so D_k = {q : σ̄_k(q) ≠ τ(q)} is a function of σ̄_k|Q; D changes only at epoch boundaries (RESULTS R63 (c)
D-EPOCH as well), so the maximal D-constant runs, numbering D changes + 1, are unions of epochs. The reading that L-SI's D-boundary count is a
lower bound for N_ep, not an upper proxy, follows ✓.

## 6. Data (own engine; DATA, not proof; 0 failures of every signed check)
Checks: FBR (FB-RISE_C), SATB / SATW (SAT_C (1), (2)), RET (RET-FB at EVERY later C-state s ≥ t + 1 for EVERY configuration C visited in the
phase, not only the source's), VIS (per C: kind (a) ≤ 2n(n − 1), kind (b) ≤ n − 1 with each kind-(b) return rising, V_C ≤ 2n² − n + R⁰_C),
EPC (N_ep ≤ NCONF(2n² − n) + R⁰ and R⁰ ≤ Σ_S REV(S)), SATFB (SAT-FB's disjunction, and Iσ_{t+1} = ∅ whenever a C-state follows), SATFB1,
FBCP (f ≤ n·|𝒞_f|), ASM (N_0 ≤ 4n² − 3n; N_{≥2} ≤ NCONF_{≥2}(2n² − n) + R⁰_{≥2}), DREM (D changes + 1 ≤ N_ep). DEPTH mode (n = 40 lane
instances): levels capped at depth D, a check counted only when decided.
| sample | runs | phases (with levels) | in-phase fallbacks (FBR) | RET checks (source in another configuration) | returns (a) / (b) / R⁰ | Σ N_ep / Σ NCONF / Σ R⁰ (phases with levels) | NCONF_{≥2} / R⁰_{≥2} | saturated fallbacks (SATFB; non-flat / not last) | UNK phases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scratch/fbc_lib.txt, n ≤ 20 (471 files), S3 + 6 random | 3,297 | 12,172 (426) | 630 | 2,380 (197) | 0 / 31 / 124 | 913 / 758 / 124 | 72 / 0 | 236 (5 / 3) | 0 |
| the same list, n ≤ 34 (807 files), S3 + 2 random, budget 3·10⁶ per configuration | 2,421 | 11,911 (400) | 801 | 6,774 (1,601) | 0 / 98 / 272 | 1,456 / 1,086 / 272 | 198 / 36 | 178 (11 / 7) | 144 |
| random 3,000 games (n 6-22, ≤ 8 Odd choice vertices, seed 351), S3 + 4 random | 15,000 | 45,671 (577) | 575 | 576 (2) | 0 / 0 / 3 | 591 / 588 / 3 | 6 / 0 | 566 (0 / 0) | 0 |
| rho3_253_n32 at L-RED's start + S3 + 30 random | 32 | 320 (7) | 79 | 715 (695) | 0 / 1 / 0 | 109 / 108 / 0 | 106 / 0 | 51 (51 / 44) | 0 |
| long121_n40 at its start (DEPTH 16) | 1 | (2) | 7 decided (1 undecided) | 491 decided (3 undecided) | — | N_ep 37, NCONF 14 (max phase) | — | — | 0 |
| nep90_n40 at its start (DEPTH 16) | 1 | (5) | 6 decided (1 undecided) | 297 decided (3 undecided) | — | N_ep 90, NCONF 48 (max phase) | — | — | 0 |
0 failures of every check in every row (DREM, FBCP and ASM over all 70,074 phases of the first four rows). The packet's figures reproduce: long121 N_ep 37 against
NCONF 14, nep90 90 against 48 (§6 of the packet); rho3_253_n32's non-flat, not-last saturated fallbacks (§5's DEAD item; 51 / 44 over my 32
starts). No kind-(a) return occurs anywhere (consistent with the packet's CONJECTURE SAT-1); R⁰ is small (124 of 913 epochs at n ≤ 20).
- Added after the first push (a52feb43): nep76_n40 at its start (DEPTH 16) finished: 1 run, 10 phases, N_ep 76 against NCONF 40 (the packet's
  figure), FB-RISE_C 5 decided (1 undecided), RET-FB 230 decided (3 undecided), 0 failures (scratch/epc_logs/deep16_nep76.txt).
- Mutations (each bites): MUT=1 (RET asks LEV_C(t) + 2): 247 failures (n ≤ 20 library, S3 + 2 random, 1,413 runs) and 82 on long121
  (DEPTH 12); MUT=2 (RET read at EVERY later state, not only C-states): 251 failures, all at non-C states (the restriction is needed);
  MUT=3 (SAT-FB read as the DEAD guess "t + 1 is P's last state"): 1 failure in the library, 7 on rho3_253_n32 at its start.
## 7. Notes (none blocks a signature)
- EPC-N1 (FB-C′ needs LEV_C ≥ 0). As in REFEREE-2's N-FBC-1 on P-N5-FBC: "values in {0, …, n − 2}" needs LEV_C ≥ 0 at every state, true (0-edge
  paths sit at cycle nodes of λ) and unstated here too.
- EPC-N2 (RET-FB's induction). The induction is on |r| at the fixed C-state s, and only the Odd branch calls it; one sentence would say so
  (the Even branch bounds Ξ_s directly through t + 1 and (MON)).
- EPC-N3 (EP-ASM's open terms). EP-ASM is a reduction: say in its statement line that X_dir, X_big, NCONF_{≥2}, R⁰_{≥2} are unbounded here (the
  packet says it in §4's READING and §6's OPEN, not in the item itself).
- EPC-N4 (SAT-1 and FBC-N3 / SAT-FB1). CONJECTURE SAT-1 (§6, no C-epoch after a saturated C-state) would sharpen VIS (a) from 2n(n − 1) to 0;
  SAT-FB1 bounds saturated FALLBACKS, not saturated epochs, so it does not give SAT-1.

## §C. Comparison with REFEREE-2 (written 2026-10-26T17:17Z by date -u, after the Lead's word of 17:02Z; REFEREE-2's report
docs/referee-2/R2-N5-EPC.md at origin/claude/referee-2 62b72f6e (trunk merge a5a2dfb2), read only after my report was pushed at a52feb43)
### Verdicts
| item | REFEREE (a52feb43, addendum 58fd9535) | REFEREE-2 (62b72f6e) | joint |
| --- | --- | --- | --- |
| §1 FB-RISE_C, SAT_C (restated) | SIGNED | SIGN | SIGNED |
| §2 RET-FB, VIS, EP-C (with R⁰ ≤ Σ_S REV(S)) | SIGNED | SIGN | SIGNED |
| §3 SAT-FB, SAT-FB1, FB-C′, consequences bullet | SIGNED | SIGN | SIGNED |
| FB-C′ without my FBC-N3 route (the Lead's question) | YES (no R15 (b), no R38 (f) CN-LAST; shorter, fewer premises) | YES (same reasoning) | YES |
| §4 EP-ASM | SIGNED as an assembly; second term as an IMPLICATION from (Στ) | the same | the same |
| §5 remark | SIGNED | SIGN | SIGNED |
| §5 DEAD item | CONFIRMED (rho3_253_n32 at L-RED's start file) | CONFIRMED (rho3_253_n32 at its own random starts 5, 7; cond_stuck_symsi3_YE) | CONFIRMED, on independent runs |
| quotes / pins | 24 verbatim at f4562054; pins match | 22 (§7) verbatim; pins match | verbatim |
Verdicts identical. Joint gap map: EMPTY.
### Notes, matched
| REFEREE | REFEREE-2 | joint |
| --- | --- | --- |
| EPC-N1 (FB-C′ needs LEV_C ≥ 0, unstated) | (its N-FBC-1 on P-N5-FBC; not repeated) | same note |
| EPC-N2 (RET-FB's induction: only the Odd branch calls it) | — (checked in its §1, no note) | REFEREE's wording note; accepted by REFEREE-2 in its §C |
| EPC-N3 (EP-ASM's statement should name its four open terms) | N-EPC-6 (data: fallback-free returns R⁰ are most returns, 729 of 1,340) | compatible; my data agree (R⁰ 124 vs kind (b) 31 at n ≤ 20; 272 vs 98 at n ≤ 34) |
| EPC-N4 (SAT-1 would make VIS (a) 0; SAT-FB1 bounds fallbacks, not epochs) | N-EPC-5 (VIS kind (a) never occurs: 0 of 1,340; its "VIS without R⁰" control does not bite) | same finding (mine: 0 kind-(a) returns in every row) |
| — (my §2 has the frame-free Even step without a note) | N-EPC-4 (the Even step holds in every frame H_C at once: 7,126 checks) | ACCEPTED |
| — (my pin paragraph names both the file sha1 and f4562054, without flagging the ambiguity) | N-EPC-1 (the packet's "Pinned at trunk f4562054" is its quote base; the Lead's "9f48ded7" is the file sha1) | ACCEPTED |
| — (my probe and §4 use D_C := {q : C(q) ≠ τ(q)} without flagging that the packet defines only D_E) | N-EPC-2 (define D_C) | ACCEPTED |
| — | N-EPC-3 (HON-FB (iv)'s citation is not needed; SAT-FB's last step uses only Iσ = ∅ and the SPEC) | ACCEPTED (my §3 reads the step from S4a / S4b / S4c / S5 directly too) |
### Data
Both own engines, 0 failures. Both reproduce long121 37 / 14, nep90 90 / 48, nep76 76 / 40. Both find no kind-(a) return anywhere. Both
nonC controls bite hard (mine: RET-FB at every later state, 251; REFEREE-2: 11,424). REFEREE-2's library shows no non-flat saturated fallback
(0 of 43), mine shows 5 of 236 (n ≤ 20) and 11 of 178 (n ≤ 34): different instance lists (mine includes experiments/new/esc and docs/referee/
instances such as cond_stuck_symsi3_YE, where REFEREE-2 also finds them). No disagreement; nothing open between the referees on EPC.
