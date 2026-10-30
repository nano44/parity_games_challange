# R-N5-LATEP-C: §C cross-map for P-N5-LATEP (REFEREE 19 vs REFEREE-2 22)
Referee: REFEREE (successor 19), Opus 5.5 (D15). Lead brief 2026-10-30 06:49Z; written 06:49Z-06:55Z by date -u. Every verdict "(Opus 5.5, D15)".
- My report: docs/referee/R-N5-LATEP.md at claude/referee 5bdd5d6d, pushed BEFORE I opened REFEREE-2's.
- REFEREE-2's report: docs/referee-2/R2-N5-LATEP.md at claude/referee-2 e7b538a9 (sha1 00ca428a…, 178 lines), opened 06:49Z after the Lead's word.
- Fixes and corrected line: not yet pushed (Lead: SHA to follow); the word-diff goes in a later section.

## 1. Joint gap map
| item | REFEREE 19 | REFEREE-2 22 | joint |
| --- | --- | --- | --- |
| §2 LATE′ and its diff against R88 §4 | CHECKED, exact | CHECKED, exact | agreed |
| §3 FW-R*′ | SIGNED | SIGNED | SIGNED by both |
| §4 LATE-SPLIT′ (i), (ii) | SIGNED | SIGNED | SIGNED by both |
| §4 CIRCLE′ | SIGNED | SIGNED | SIGNED by both |
| §5 GAP-CLIMB | SIGNED | SIGNED | SIGNED by both |
| §6 CHAIN | SIGNED | SIGNED | SIGNED by both |
| §7 TXC-DESCENT | SIGNED | SIGNED | SIGNED by both |
| §7 TXC-RED, Σ LCT ≤ n(n − 1), composed bound | SIGNED | SIGNED | SIGNED by both |
| §8 READING, §10 DATA | not signed | not signed | — |
| line 4a68934d | MATCHES after LATEP-L1 (GXC source), L2, L3 | MATCHES after L-1 (REQUIRED: t range), L-2..L-4 | MATCHES after L-1 + LATEP-L1 (see §2) |
Verdicts identical. The gap map is EMPTY: neither referee lists a gap in any proof, and nothing in §2-§7 is false.
- Proof-level agreements: both derive FW-R*′ with τ := the first adoption after t (R2 N-1); both note that the leave k in (p, u) is UNIQUE (my
  §4, R2 N-2); both spell out TXC-DESCENT's termination on the simple prefix up to the lasso's cycle node (my §7, R2 N-5).
- Data: two engines agree where the sets coincide. so_th_n32 (S3): TXC 73 and gate terminals 16, both of us, against the pinned 63 / 15. Both
  reproduce the lane's latep.py pins exactly (wdepth_K4_m16 LP 37, REPP 21; tiedmut LP 6, REPP 1). Both find T4-terminated descents and CNW > 0
  (mine: n ≤ 120 with both starts, T4 36, CNW 110; REFEREE-2: S3 on all 719, T4 5, CNW 71, instance b5_o11). Both: the T4 control never bites.
  REPEAT′ is rare for both (mine 2 at n ≤ 120; REFEREE-2 4 on all 719, max 3 per W-run).

## 2. Notes map
| mine | REFEREE-2 | content |
| --- | --- | --- |
| LATEP-D1 | N-7 | txcd.py reads W with the OLD τ after a τ-change (l. 58); so_th 73, not 63; the «box 52» pins encode the undercount. REFEREE-2 also has a patched scratch copy reproducing the true counts |
| LATEP-D2, LATEP-N5 | N-8 | txcd.py has no T4 test; «0 T4» / «CNW 0» false; T4's necessity is not exhibited |
| LATEP-L1 | L-2 | GXC is defined by citing L-NEW box 70, which is not landed and not pinned. I mark it REQUIRED under the every-symbol rule, REFEREE-2 marks it a precision. Joint position: inline the definition or pin @170e5316. I keep REQUIRED (an unpinned, unrefereed source cannot bind a symbol of a landed line; the packet's §9 calls it "landed", which is false) |
| LATEP-L2, LATEP-N2 | L-4, N-9 | X′_F's blocked state t: state "some" (R2) / fix the choice (mine). R2 N-9 adds that λ_W is constant on F, so "y own cycle node somewhere on [k + 1, t]" is just λ_W(y) = y and the choice of t does not matter. I accept that: it makes L-4 / my L2 a wording point only |
| LATEP-L3, LATEP-N3 | L-3 | the line files CIRCLE′'s inequalities under «Lemma LATE-SPLIT′» |
| LATEP-L3 (premises) | — | mine only: name the landed premises in the line |
| LATEP-N1 | — | mine only: standing premise inherited from R90 K2 |
| LATEP-N4 | — | mine only: §8's «REP′* ≤ REP* ≤ T» should be ≤ n·T |
| — | L-1 (REQUIRED) | REFEREE-2 only: the line's «(any t of F if none)» drops t < u. Read literally, an adoption of an edge blocked only at states ≥ u would be LATE′; then «LATE′ ⊆ R88-late» and REP′ ≤ REP fail. I MISSED this in my symbol test (my §9 listed "LATE′ (t, p)" as bound in the line). I CONFIRM L-1: the packet's §2 keeps t < u in every case; the fix «(a ≤ t < u if there is none)» is right |
| — | N-1, N-2, N-3, N-4, N-5, N-6 | REFEREE-2 only, all clarifications: N-4 (l. 111 «§8 DATA» → «§10 DATA») and N-6 (box-40 remark needs j − 2 in the same W-run) are correct; I add them to the routed list |

## 3. Joint position on the line (pending the corrected line)
REQUIRED before landing: L-1 (t < u in the no-previous-adoption case) and LATEP-L1 = L-2 (GXC inlined or pinned; I hold REQUIRED).
Precisions: L-3 / LATEP-N3 (CIRCLE′ label); L-4 / LATEP-L2 ("some t"); LATEP-L3 (landed premises named). I will word-diff the corrected line
against 4a68934d and re-run my strict symbol test when the Lead sends the SHA.

## 4. Addendum (Lead 07:00Z): fixes F0-F15 + F-SYM (l-si 17a3ecec, sha1 a690dc2504ed8c11c554d83bc0dc45a3051973de) and line F1 (sha1 a85759a26b38b8bb6e3958bb19745d2aa9fd397c); written 07:01Z by date -u
- Hashes re-measured: both match. The frozen packet at 17a3ecec still has sha1 b15223e5.
- (1) My own word diff (`--word-diff=porcelain`) of the frozen line 4a68934d against F1 shows exactly F0's five changes:
  - «F = [a, b]»;
  - the premises «with RESULTS R15, R17 (a), R47 (a), R88 (…), R89 (…) and R90 (…)»;
  - «(a ≤ t < u if there is none)»;
  - «t the earliest blocked state»;
  - GXC_F inlined;
  - «(Lemma LATE-SPLIT′, Corollary CIRCLE′)».
  Nothing else changes.
  - GXC is inlined as I gave it. It stays inside the scope «over the transitions s → s + 1 of F (s, s + 1 in F)», so «s, s + 1 in F» is kept;
    the τ-clause of box 70 is automatic on F. ✓
- Strict symbol test of the whole F1 line (mine): a and b are now bound; t is bound in both cases of LATE′ (t < u always, which closes L-1);
  X′_F's t is fixed (the earliest; [k + 1, t] is non-empty by F10); GXC_F is self-contained; every other symbol is as in my §9 of
  R-N5-LATEP. No free symbol, and no unlanded source. The F-SYM table agrees.
- (2) F0-F15 are corrections or clarifications only; nothing widens. In detail:
  - F1-F4 are the line changes;
  - F5 and F6 are DATA;
  - F7 and F14 correct the §8 READING (not signed);
  - F8-F13 and F15 are clarifications.
  - F3 omits SUCC-MON because no proof of §3-§7 uses it. I checked this: W-SUCC (R90) carries the W chains, and SUCC-MON is Ξ-based.
  - F4 (earliest t) changes no signed statement (CIRCLE′ holds for every fixed choice).
- (3) F5 / F6 against my D1 / D2:
  - The fixed txcd.py gives so_th_n32 TXC 73 / gates 16 and tiedmut_so_th_n32_11 TXC 77. These equal my engine (73; 77) and REFEREE-2's.
  - The re-derived «box 52» block at 17a3ecec, run alone in a clean worktree, PASSES (so_th TXC 73 / T4 0 / GATE 16 / CNW 0; wdepth unchanged;
    b5_o11 CNW 1). Exit 0.
  - F6's corpus figures (T4 5, CNW 71) are REFEREE-2's S3-on-719 set. My 36 / 110 come from a different set (n ≤ 120, given starts plus S3),
    as F6 says. D1 and D2 are closed.
- Verdict (Opus 5.5, D15): F1 MATCHES §3-§7 with F0-F15, has no free symbol, and claims nothing more. P-N5-LATEP is landable as far as REFEREE
  is concerned, with F1 as the line.

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: verdicts identical, gap map EMPTY, every PROVED item SIGNED by both; D1 = N-7 and D2 = N-8 confirmed by two engines (so_th TXC 73);
  REFEREE-2's L-1 (line drops t < u) is a REQUIRED fix that I missed, and I confirm it; GXC source REQUIRED (my L1 = R2's L-2).
- NEEDS: none (§4: F1 MATCHES, no free symbol; F0-F15 clean; D1/D2 closed).
- F16 check (Lead 08:06Z; l-si baa8a48a, docs/si/P-N5-LATEP-line-F16.txt sha1 65277addc8be558922dcdcc7d035426ba3062b8e and fixes sha1 66c85a168022bf08af630ddcd0df494b09a5733c, re-measured; fixes append-only vs 17a3ecec; my own word diff F1 → F16, written 08:07Z by date -u): exactly the five changes «R15» → «R15 (a), (d),», «+R57 (a) (premise (VJ)),», «−W-MON,» (R88's list), «+W-MON′,» (R90's list), «a REPEAT′ if {+it is LATE′ and+} …». Use-by-use claim checked at b63f2554: §5 l. 99 and §6 l. 109 use W monotonicity on F, which is R90 W-MON′ with τ kept (R88's W-MON is stated for a frozen W-phase; R89 GP*-RUN carries it to W-runs, so either citation works, and W-MON′ is the direct one); §3 goes via R89 GP*-RUN; §4's chain uses only OPT-OFF (ii) and W-SUCC (R90); §7 uses [V1]/[V2], λ_W constant on F, and R15, with no W monotonicity. ✓ The REPEAT′ restriction matches packet §2 («A LATE′ adoption is FIRST′ … REPEAT′ otherwise»). I MISSED both defects in my F1 test; the drafter caught them. Strict symbol test of the whole F16 line: no free symbol, no unlanded source. MATCHES (Opus 5.5, D15).
