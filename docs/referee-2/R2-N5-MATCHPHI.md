# R2-N5-MATCHPHI: REFEREE-2 report on packet P-N5-MATCHPHI (L-LIT): definitions, Fact 1, Lemma MATCH-Φ, Corollary (PCH ≤ (K(K+1)/2)(NM + 1) + NM)
Referee: REFEREE-2 successor 19 (session_01V5yGRZzoAVpZvqB1LedCVF), Opus 5.5 (D15, L37). Written 2026-10-29 from 11:03Z (date -u).
Object: docs/lit/P-N5-MATCHPHI.md, sha1 544705b74312e49ee31fd93ede1952396ebd12f1 (measured with `git show 12b7d12a:<path> | sha1sum`; equal to the Lead's),
133 lines, l-lit freeze 12b7d12a4bb2839ed1997276b54f83d11a70dd1d. Pinned scripts measured at the same commit:
- docs/lit/T33-match-phi-check.py 6853179b;
- docs/lit/P-N5-MATCHPHI-quotecheck.py 0ac586a4.
Both equal the Lead's figures.
INDEPENDENCE:
- I have not opened any file under docs/referee/ on MATCHPHI and have not run `git log` on origin/claude/referee.
- Name count `git ls-tree --name-only -r origin/claude/referee docs/referee/ | grep -ic matchphi`: 0 at 2026-10-29 11:02:53Z; 0 at 2026-10-29 11:09:42Z (push turn, after `git fetch origin claude/referee`). Names only.
- The lane's two scripts were READ, then RUN as the pinned re-runs the Lead asked for. They ran in a detached worktree at 12b7d12a (scratchpad),
  with `python3 -I`. Their output is in logs/pinned_check.txt. They were never imported.
- My checks use my own code: docs/referee-2/R2-N5-MATCHPHI/mphi_check.py, with its own MATCHED matcher (Mendelsohn-Dulmage + augmenting paths),
  cross-checked against brute force. Quotes with my ../R2-N5-CORE/qcheck.py.
Scope (D1): a REDUCTION of the P-changes of one vertex in one phase to its carries NM, which are not bounded (OPEN). Not a TARGET.md claim. No running
time. G-N5-TIME stays OPEN.

## 0. Verdicts (all "(Opus 5.5, D15)")
| § | item | verdict |
| --- | --- | --- |
| §1 | definitions pos, w, Φ, MATCHED (M1)-(M3), CARRY, NM | SIGNED (well formed; deciding MATCHED is polynomial, as stated) |
| §2 | Fact 1 (w(i) > w(o) ⇔ weight({i}) > weight({o}); even additions and odd removals raise the weight; MATCHED = decomposition into individually weight-raising one-for-one exchanges, even additions, odd removals) | SIGNED |
| §2 | Lemma MATCH-Φ (Φ rises by ≥ 1 at every MATCHED P-change) | SIGNED |
| §2 | Corollary PCH_𝒫(v) ≤ (K(K+1)/2)(NM + 1) + NM ≤ (n²/2)(NM + 1) + NM, per vertex per phase, every game | SIGNED. The first term is SHARP at NM = 0 (N-MP-2) |
| §2 | Remark: the Corollary uses only distinct ranks and P_t ⊆ R_c with c = λ(v) fixed on the phase, not (MON), not TOP-SHAPE | CORRECT against the proof. Checked on 25,000 arbitrary (non-monotone) subset sequences. One premise sentence misattributes (MON) to Fact 1 (N-MP-1) |
| — | pinned re-runs | REPRODUCED exactly (§2) |
| — | quotes | 5/5 VERBATIM (lane quotecheck "quotes=5 bad=0"; my qcheck 5/5, SHIFT=1 control 0/5; a mutated quote makes the lane checker report bad=1) |
| §3, §4 | DATA, READING | not signed. One DATA figure differs from mine (N-MP-4) |
No gap. Notes N-MP-1..5.

## 1. Proof check
- Definitions.
  - pos and w are defined on R_c, which needs c fixed. c = λ(v) is constant on a phase (R84's setting, quoted).
  - P_t ⊆ R_c by S1: P holds the vertices with p′ > p′(c), i.e. rank > rank(c).
  - MATCHED is a bipartite cover problem: the even outgoing and the odd incoming ranks must be covered by (M1)-edges. By Mendelsohn-Dulmage
    it is decidable as two one-sided cover tests. ✓
- Fact 1.
  - The four cases (i ≷ o, the parity of the larger) are each right. ✓ (F1: every o ≠ i, every parity pattern, K ≤ 7; 0 failures.)
  - "Individually weight-raising" holds in every context, since weight is additive: weight(S − o + i) − weight(S) = weight({i}) − weight({o})
    (F1add: 0 failures).
  - Hence a MATCHED change always raises the weight (F1b: 0 failures on all 2,374,900 ordered pairs, K ≤ 7). Fact 1 uses Fact DELTA only, not
    (MON) (N-MP-1).
- Lemma MATCH-Φ.
  - A ∖ B and B ∖ A split into M's pairs, the uncovered incoming ranks and the uncovered outgoing ranks.
  - Each pair contributes w(i) − w(o), an integer ≥ 1 by (M1) (the w values are distinct integers). Each uncovered incoming rank contributes
    pos(i) ≥ 1 by (M2), and each uncovered outgoing rank contributes pos(o) ≥ 1 by (M3).
  - The terms are non-empty because A ≠ B. ✓
  - MP: checked on every ordered pair of distinct subsets, improving or not, for K ≤ 7 and every parity pattern (2,374,900 pairs, the K = 7 run includes every K ≤ 6;
    661,892 MATCHED), and at all 23,330 + 31,014 + 3,763 + 872 MATCHED N5 P-changes. 0 failures.
- Corollary.
  - Φ ∈ [−Σ_odd pos, Σ_even pos], an interval of width W = Σ_{k ≤ K} k = K(K+1)/2.
  - Σ over MATCHED changes of ΔΦ equals (Φ_end − Φ_start) − Σ over carries of ΔΦ, which is ≤ W + NM·W. Each MATCHED change contributes ≥ 1.
  - PCH = #MATCHED + NM. K ≤ n − 1 gives W ≤ n²/2. ✓
  - COR / CORn: 0 failures on 12,734 + 23,111 + 709 + 1,201 (vertex, phase) pairs and on 25,000 random subset sequences.
- The Remark. The proof never compares P_t with P_{t+1} beyond the definitions: no (MON), no TOP-SHAPE, no strict rise. My random sequences are
  arbitrary walks on subsets (local flips and random jumps, mostly non-monotone), and the bound held on all 25,000. ✓

## 2. Pinned re-runs (as the Lead asked) and own data
- `python3 -I docs/lit/T33-match-phi-check.py` at 12b7d12a, exit 0:
  - "A: improving pairs 80640 | matched with phi rise < 1: 0 | carries: 32534";
  - Part B NM = 0, 0, 1, 3, 7, 15, 31, 63 for k = 1..8, strict-rise=True, fixed-top=True.
  - Exactly the expected output.
- `python3 -I docs/lit/P-N5-MATCHPHI-quotecheck.py`: "quotes=5 bad=0".
  - My control: one character of the R84 quote changed in a scratch copy → "quotes=5 bad=1". The file was restored, and the worktree is clean.
- Own combinatorics (mphi_check.py comb).
  - K ≤ 7, all 2^K parity patterns, all ordered pairs.
  - My matcher equals brute force on 2,358,516 pairs with |A Δ B| ≤ 6 (K ≤ 7) and on all 294,132 pairs with |A Δ B| ≤ 8 (K ≤ 6).
  - Controls bite:
    - CTL_noM2 (an odd incoming rank left uncovered): 375,337 pairs with ΔΦ < 1 (K = 7);
    - CTL_noM1 (pairs not required to satisfy (M1)): 547,514;
    - CTL_carry_rise (carries that raise the weight; carries are not just falls): 525,558.
- TIGHTNESS (N-MP-2). The longest chain of MATCHED changes (the graph of MATCHED moves is a DAG, since Φ rises) has length exactly W = K(K+1)/2
  for every K = 1..7, attained by the all-odd parity pattern. So at NM = 0 the bound is attained, and W cannot be lowered to, say, K.
- N5 data (mphi_check.py n5; own engine; 0 violations):
| corpus | runs | P-changes | MATCHED / carries | max NM (n) | max NM / n | max PCH per (v, phase) |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all (413; given start else S3) | 413 | 53,549 | 23,330 / 30,219 | 62 (gate_K64_n581, n 581) | 0.90 (ret22_n40) | 67 (snap_n80_s62) |
| lib41_noref × 3 | 1,230 | 70,808 | 31,014 / 39,794 | 18 (xsn91_n48) | 0.469 (b6_xw_n32) | 37 |
| named (box49 dressings, si/root, nep90, long121, pl130_n40 + its .start) | 19 | 13,282 | 3,763 / 9,519 | 47 (pl130_n40, n 40) | 1.175 (pl130_n40) | 72 (l121_d29) |
| random kO n 8-20 (3,000 × 3) | 9,000 | 1,221 | 872 / 349 | 1 | 0.125 | 2 |
- These reproduce §3's L-COMP figures: 62 at n 581, 0.90 on pinned starts, 1.18 (= 47/40) on pl130_n40.
- Carries are 56 % (alt_all), 56 % (lib41) and 72 % (named) of the P-changes, consistent with §3's "60-75 % on the long pins".

## 3. Notes (not gaps)
- N-MP-1 (premise wording). The premise list says "(MON) and Fact DELTA are used only by Fact 1". Fact 1 uses Fact DELTA only.
  - (MON) / R84's strict rise enters only the READING: in N5 every P-change raises the weight, so a carry is an improving change that does not
    decompose.
  - Say "Fact DELTA is used only by Fact 1; (MON) only by the reading".
- N-MP-2 (sharpness). The Corollary's first term is attained at NM = 0. The longest MATCHED-only chain over subsets of K ranks is exactly
  K(K+1)/2 (all-odd parities, K ≤ 7, exhaustive). Worth recording beside the Corollary: any improvement must come from bounding NM, not from W.
- N-MP-3 (Fact 1 in context). Fact 1 is stated for singletons. The packet's reading, that the decomposition consists of steps each raising the
  weight of the CURRENT set, needs additivity: weight(S − o + i) − weight(S) = weight({i}) − weight({o}). That is immediate from the definition.
  One line.
- N-MP-4 (§3 DATA line, not to sign). §3 says "Max NM per (vertex, phase): 31 on alt_all (0.775n); 62 at n 581".
  - root/logs/alt_all.lst contains red/usplit/instances/gate_K64_n581, whose run gives NM 62 (vertex 578, phase [0, 71]). So my alt_all maximum is
    62, not 31.
  - 31 may be the maximum over alt_all without the n = 581 game, or over another start set. The "0.775n" fits n = 40 (31/40).
  - Also, "pl130: 157 = 41 matched + 116 carries" has no stated unit: my largest single (vertex, phase) on pl130_n40 has PCH 62 = 15 + 47. Say
    whether 157 sums over vertices.
- N-MP-5 (thin spot / reading). In random games NM ≤ 1 per (vertex, phase): the carries come from the long library and lane instances. The
  N5-specific content (S4a's rule) is not used anywhere in the signed items, as §4 says.

## 4. DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-MATCHPHI/{mphi_check.py, named.lst, run_all.sh, logs/ (including pinned_check.txt)}.
- FINDINGS:
  - Definitions, Fact 1, MATCH-Φ and the Corollary all SIGNED, no gap. The Remark is correct.
  - The bound's first term is sharp at NM = 0 (N-MP-2).
  - The pinned checks reproduce exactly.
  - One premise sentence misattributes (MON) (N-MP-1). One §3 DATA figure differs from my alt_all run (N-MP-4).
- NEEDS: Lead: the §C word; route N-MP-1..5 to L-LIT.
