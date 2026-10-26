# P-N5-HON fixes (box 46 packet): the referees' notes, written out (no gap)
L-NEW successor 26 (Opus 5.5, D14 / D18, L40), for the parked author (successor 25). Written 2026-10-26 11:49Z onward by date -u, on the Lead's word of
11:37Z (Lead's stamp): "the P-N5-HON notes collection. Both §Cs are in. FILE: docs/new/P-N5-HON-fixes-box46.md, repairs only. Packet sha1
07f8e767 FROZEN; do not touch it." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-HON-box46.md, sha1 07f8e767cfca12d29c8f6f2e3f03358326abbef1 (l-new 67a7b54d; re-measured on this tree). The packet
  is NOT edited; this file is its correction layer, a record of the reports, not refereed text.
- Sources (read on trunk fb3302f5; the line numbers below are of these files there; every quote below, set in curly double quotes, was checked by script against
  that tree: whitespace normalised, then substring test; the script is §5):
  - REFEREE: docs/referee/R-N5-HON.md (report e7f9bc31, independence-line correction 59121877, §C a00a15c0; successor 14).
  - REFEREE-2: docs/referee-2/R2-N5-HON.md (report 1566b439, §C 7f8bafdc; successor 16). The Lead notes that REFEREE-2's DATA total corrections
    of 10:31Z are in its message only, not in its file; they are not recorded here (I have not seen that message).
- Nothing here changes a signed statement.

## 1. Verdicts (both referees, Opus 5.5, D15)
- REFEREE (R-N5-HON.md l. 27-38): Lemma HON, SAT0, HON-FB (i)-(iv), HON′, HON-0 (a)-(c), RESTRICT_u / REPRO_u and REC-1 (a) SIGNED; EP-1u
  “SIGNED as an IMPLICATION from (Στ)” (l. 35) and REC-1 (b)-(d) “SIGNED as IMPLICATIONS from (Στ)” (l. 37). l. 40: “No gap. Notes HON-N1..N4
  (wording / citation).”
- REFEREE-2 (R2-N5-HON.md l. 128-131): “Lemma HON, Lemma SAT0, Lemma HON-FB (i)-(iv), Corollary HON′, Corollary HON-0 (a)-(c), Lemma
  RESTRICT_u (i)-(iv), Corollary REPRO_u (with EPR-1), Theorem REC-1 (a): SIGN, on every game, under the standing SPEC premise 1E-N3 (P1, P2).
  Corollary EP-1u and Theorem REC-1 (b)-(d): SIGN as IMPLICATIONS from (Στ) (which holds at R65's audit strength).” l. 27: “No gap. Notes
  N-HON-1..5 (§3).”
- R65's audit strength, both: REFEREE l. 40-41: “With RESULTS R65 ((Στ) at audit strength) EP-1u and REC-1 (b)-(d) hold at that same
  strength”; REFEREE-2 l. 96 (N-HON-4): “at R65's audit strength EP-1u and REC-1 (b)-(d) hold without the "(Στ)" hypothesis; signed here as
  implications.” RESULTS R65 has landed (docs/RESULTS.md l. 3324).
- The packet's §2 claims (1: HON-0 implies the signed REC-0, difference f·n + 2; 2: the proofs are independent): REFEREE l. 32: “CHECKED: TRUE
  (strictly; difference f·n + 2)”; l. 33: “CHECKED: TRUE in the sense "neither proof uses the other, nor SN-PREFIX_D or EP-0"”; REFEREE-2 l. 20:
  “CONFIRMED (both claims)”.
- Q-R17: YES from both. REFEREE l. 125: “HON uses R17 three ways; in each, nothing beyond the listed items enters.” (the list, l. 126-134);
  REFEREE-2 l. 89 (N-HON-2): “YES.” and §C l. 141: “REFEREE's three-use list is the more complete statement, ACCEPTED”. Read Q-R17's answer as
  REFEREE's three uses: §1 step 1 (the full induction step, items (1)-(7) of R-N5-HON.md l. 126-131); SAT0 (Case A at a single state, without
  (F2), l. 132); HON-FB (i) (Theorem PH's case split with "the phase ends" replaced, l. 133-134).
- Joint gap map EMPTY: REFEREE §C l. 188: “No verdict disagreement. Both referees: no gap.”, l. 210: “EMPTY.”; REFEREE-2 §C l. 149: “No
  disagreement on any verdict. Joint gap map: EMPTY.”

## 2. Notes (wording and citation; no statement changes)
- N-HON-1 (SAT0's Odd case; REFEREE-2; SETTLED as a NOTE). Packet l. 86: “(r′ and z's play avoid x)”. REFEREE-2 raised it (l. 85-86: “the
  parenthesis "(r′ and z's play avoid x)" is false when x lies on its own W-cycle without being its cycle node”) and, after REFEREE's reading,
  settled it in its §C (l. 142): “SETTLED as a NOTE, not a gap” … “I WITHDRAW the word "false" and keep N-HON-1 as a wording note ("z's path
  to its cycle node avoids x")”. REFEREE §C l. 192: “ACCEPTED.” … “equivalent: "r′ and z's path to its cycle node avoid x"”. Read the packet's
  parenthesis at l. 86 as: (r′ and z's path to its cycle node avoid x).
- HON-N1 (REFEREE; ACCEPTED by REFEREE-2). Packet l. 121: “HON-FB adds XW and the Theorem PH case split”. REFEREE l. 162-163: “REC-0's chain
  also contains XW: it is in P-N5-REC0's premise list (l. 25) and in the proof of SN-PREFIX_D (a), which REC-0 step 3 uses”; l. 163-164: “What
  HON adds over REC-0's premises is R17 (c)'s case split (HON-FB (i)), SAT0 and HON-FB (ii)-(iii); what it drops is SN-PREFIX_D and EP-0.”
  REFEREE-2 §C l. 140: “ACCEPT HON-N1: the packet's "HON-FB adds XW" is inexact”. Read the packet's sentence at l. 120-121 as: both proofs use
  the same Lemma P step (Q-R17), WM, XW, R15 (a), (d) and Lemma S (c); HON adds R17 (c)'s case split (HON-FB (i)), SAT0 and HON-FB (ii)-(iii),
  and drops SN-PREFIX_D and EP-0. The independence claim is unaffected (REFEREE l. 164: “The independence claim ("neither proof uses the other")
  is unaffected.”).
- HON-N2 (REFEREE; ACCEPTED by REFEREE-2, §C l. 143). Packet l. 37: “in the referee queue” and l. 115: “it is in the referee queue and is expected
  to land as signed”. REFEREE l. 165-166: “"P-N5-REC0 … is in the referee queue and is expected to land as signed" is stale at the pin: both
  referees signed REC-0”. Since then REC-0 has LANDED as RESULTS R66 (docs/RESULTS.md l. 3396). Read both context lines as: packet
  P-N5-REC0-box45 (Lemma REC-0) is signed by both referees and landed as RESULTS R66. So, as REFEREE l. 166-167 says, “the packet's "HON-0 is the
  stronger form of the signed REC-0" is now literally true.”
- HON-N3 (REFEREE; ACCEPTED by REFEREE-2, §C l. 144: “ACCEPTED (my §2 uses both but did not flag it for HON-FF)”). REFEREE l. 168-170: “The
  fallback-free hypothesis is used twice: for the rise (Lemma P's step needs h → h + 1 to be an S4a step) and for the sandwich that keeps W's
  cycle-node map at h + 1 (WM at every transition of the gap).” … “so a proof of HON-FF has to replace both, not only the first.” A remark on
  the packet's OPEN §5, not a fix. (Context, not part of the fixes: the lane's working doc docs/new/N5-HONFF-box47.md, l-new 385a5534, proves
  HON-FF by a route that does not use step 1 on gaps with a fallback; it is unrefereed and outside this packet.)
- N-HON-2 (REFEREE-2; Q-R17 in step 1). R2-N5-HON.md l. 89-92, the list for step 1: the hypothesis W_h ⪰ value(r′) for |r′| ≤ LEV(h); σ_{h+1} an
  optimum of the switch-best arena of G_τ at σ_h (P2); (F1)/(F2) including (MON); (V1) and strict (V2); “"no vertex changes its W-cycle node
  from h to h + 1", which HON proves by the sandwich, not from a phase start. Nothing else”. Contained in REFEREE's three-use list (§1 above).
- N-HON-3 (REFEREE-2; ACCEPTED by REFEREE). R2-N5-HON.md l. 93-94: “The packet's list is complete; P1 enters through R15 (a), (d)” … “and XW; P2
  through WM and S (c).” REFEREE §C l. 194: “ACCEPTED: my signatures are under the same standing premise (as every N5 entry since R57); I add
  it here”. So both signatures are under the standing SPEC premise 1E-N3 (RESULTS R57) in its two forms P1, P2 (REFEREE-2 l. 28-30); the
  packet names 1E-N3 in its premise list (packet l. 22: “Standing premise 1E-N3 (RESULTS R57).”). The landing line should name 1E-N3 next to
  the signatures.
- N-HON-5 / HON-N4 (data; no statement change). REFEREE-2 l. 97: “In-gap fallbacks (f_in) occur in 9 phases (16 fallbacks) of my library runs
  and in none of my random runs”; l. 99: “mutation hon (bound f_in + n − 1, the saturated tail dropped) does NOT bite.” REFEREE l. 171-172:
  “My lib41 run (different random starts) agrees with the packet on the maximum of 57 W-honest states in a phase; my f_in total is 9 against
  the packet's 4 (3 gaps), which is expected with other random starts.” REFEREE-2 §C l. 146: “REFEREE's LEVMAX-20 run thins my N-HON-5 point
  less than I stated (1 inside-gap case with exact LEV exists)”.

## 3. Data (recorded, not signed)
- Both referees: 0 failures of every signed check on their own engines (REFEREE l. 137: “All runs: own engine, 0 failures of every signed
  check in every sample.”; REFEREE-2 l. 109: “Sets (0 violations in every set)”). Both see a maximum of 57 W-honest states in a phase on lib41,
  as the packet does; the HON bound is far from attained. Mutation controls bite on both sides (REFEREE l. 148-153; REFEREE-2 l. 123-125),
  except REFEREE-2's "hon" mutation (N-HON-5).
- HON-FF (packet §5, not signed): REFEREE l. 156-157: “none failed to rise.”

## 4. Context (not part of the fixes)
- RESULTS R66 (REC-0, docs/RESULTS.md l. 3396) has landed; HON-0's N_0 bound f_in + 4n² − 3n implies REC-0's for every f ≥ 0, n ≥ 1 (difference
  at least f·n + 2), as both referees confirmed (§1). That does not affect REC-0's signatures.

## 5. Quote check (script; run from the repository root on trunk fb3302f5)
`python3 experiments/new/box47/quotecheck.py docs/new/P-N5-HON-fixes-box46.md fb3302f5 docs/referee/R-N5-HON.md docs/referee-2/R2-N5-HON.md
docs/new/P-N5-HON-box46.md docs/RESULTS.md` prints, for every quote, the file and line(s) where it occurs, and exits 1 if any quote occurs in
none. Result at the freeze: its last line is `46 quotes, 46 found, 0 missing` (exit 0); each reported location equals the one cited above.
Output: experiments/new/box47/out/quotecheck_hon_fixes.txt.
