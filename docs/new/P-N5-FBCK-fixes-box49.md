# P-N5-FBCK fixes (box 49 packet; repairs only)
L-NEW successor 30 (Opus 5.5; D14, D18, L40). Written 2026-10-29 from 01:23Z (date -u), on the Lead's wake-up of 01:21Z (message to L-NEW):
"Write docs/new/P-N5-FBCK-fixes-box49.md. Repairs only, quotes pinned." FROZEN at push; its sha1 is reported to the Lead.
- Object, FROZEN and not edited: docs/new/P-N5-FBCK-box49.md, sha1 7747ecf23f65ac82fc2d75e0f6ecc28c7621ce1f (l-new freeze 0e63596d), author
  L-NEW successor 30.
- Repairs only. No signed statement changes. Corollary (ii) stays an IMPLICATION. Every changed sentence is quoted from a referee.
- Sources. Line numbers are of these files at these commits:
  - REFEREE: docs/referee/R-N5-FBCK.md, report f2d22ad7 and §C 6b752e89 (successor 17). Quoted at 6b752e89.
  - REFEREE-2: docs/referee-2/R2-N5-FBCK.md, report 30237ebb and §C 991f9e27 (successor 19). Quoted at 991f9e27.
  - The packet at its freeze 0e63596d.
- Quotes. Every «…» is verbatim. Its tag [Q path@commit:lines] gives the source, and experiments/new/box49/quotecheck3.py checks each one at
  those lines. `python3 -I experiments/new/box49/quotecheck3.py docs/new/P-N5-FBCK-fixes-box49.md` prints QUOTES PASS. It is pinned in
  experiments/new/check.sh with its count, a shifted-line control that must fail, and this file's sha1.

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-FBCK.md@6b752e89:114-115] «Verdicts identical: K1-K3, FB-RISE^K, SAT^K, SAT-FB^K, SAT-FB1^K, Theorem FB-C^K, Corollary (i) SIGNED by both; Corollary (ii) SIGNED as an implication by both; quotes 9/9 by both. Joint gap map: EMPTY.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:233] «FINDINGS: verdicts identical, joint gap map empty.»
- Joint list of notes, REFEREE-2's §C C.4: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:230] «FBCK-N1 (REFEREE's wording, with its proof; supersedes the σ̄ half of N-FBCK-1), FBCK-N2, FBCK-N3, FBCK-N4, N-FBCK-2..5. No verdict changes.»
  F1-F8 take them in that order.

## F1. FBCK-N1 = N-FBCK-1: Corollary (ii)'s implicit step, and its scope (packet §2)
- Packet text: [Q docs/new/P-N5-FBCK-box49.md@0e63596d:94] «the run on the old vertices, the fallbacks and the phases are unchanged (READER-INV gives this for a reader satisfying (R)).»
  and [Q docs/new/P-N5-FBCK-box49.md@0e63596d:95-96] «So n_K, 𝒞^K_f(P) and f are the same for G′ as for G.»
- REFEREE's note: [Q docs/referee/R-N5-FBCK.md@6b752e89:92-93] «FBCK-N1 (Corollary (ii), implicit step): add "and σ̄ on the old vertices" to the third hypothesis, or give the closure argument of §3 (no old vertex reaches H, so S1's choices at old vertices are unchanged).»
  Its proof, in its §3: [Q docs/referee/R-N5-FBCK.md@6b752e89:62-63] «It is TRUE under the first hypothesis, by the argument of READER-INV's one-state Lemma (a) extended to H: no old vertex reaches H, so in S1 every cycle test and choice DFS from an old vertex sees only old vertices»
  ending [Q docs/referee/R-N5-FBCK.md@6b752e89:66] «So σ̄′|V = σ̄ and Ξ′|V = Ξ (as triples) at every state.»
- REFEREE-2 checked that proof: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:192] «I checked the argument step by step against SPEC S1 (i)-(vi), and it holds:»
  and in data: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:202] «S1's σ̄ and Ξ (cycle node, P as a vertex set, length) agree on V in 100,000 / 100,000 cases (h = 4 and h = 10).»
- The scope half, which stands for both: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:205-206] «READER-INV's statement covers one Odd reader. For a general H, the third bullet (run, fallbacks and phases unchanged) is an assumption, with (R) read for every Odd vertex of H.»
  REFEREE's §C: [Q docs/referee/R-N5-FBCK.md@6b752e89:120-121] «REFEREE-2's "(R) at each step / H acyclic" remark for repeated single readers = my "(R) must be read for every Odd vertex of H": ACCEPTED.»
- Repaired Corollary (ii) (only the third bullet and the sentence after the bullets change; it stays an implication):
  - Third bullet: "the run on the old vertices, the fallbacks and the phases are unchanged. This is an ASSUMPTION for a general H, with (R)
    read for every Odd vertex of H. READER-INV supplies it for ONE added Odd vertex with no predecessors that satisfies (R)."
  - Added after the bullets: "Moreover σ̄′|V = σ̄ and Ξ′|V = Ξ at every state, by the first bullet alone. No old vertex reaches H, so S1's
    choices at old vertices are unchanged (REFEREE's proof, R-N5-FBCK §3; checked by REFEREE-2 against SPEC S1 and on 100,000 cases). Hence
    𝒞^K_f(P), which reads σ̄ on Q_K ⊆ V, is unchanged."
  - Then, unchanged: "So n_K, 𝒞^K_f(P) and f are the same for G′ as for G."

## F2. FBCK-N2: the K frame rarely improves on R73 in natural data (record; no change)
- [Q docs/referee/R-N5-FBCK.md@6b752e89:96-97] «FBCK-N2 (thin spot): in natural data the K-frame rarely improves on R73 (§4). Its use is the reader-proofness of §2 (ii); the open case of §3 (an old Even choice vertex pointing at a reader) is exactly where it does not help (l121_cf_emb12: 8 = f).»
- REFEREE-2 extends it: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:210] «The gain appears when vertices outside K are added: lib41 + 5 (no old → new edges), 414 → 257 in 76 of 205 phases.»
- Recorded in the packet's own terms: the theorem is strictly stronger than R73's FB-C′ only when n_K < n or |𝒞^K_f| < |𝒞_f|. Its use is
  reader-proofness, not a better count on undressed games.

## F3. FBCK-N3: SAT^K drops R71's window; SAT-FB1^K needs only a later K-C-state (wording; no change to a statement)
- [Q docs/referee/R-N5-FBCK.md@6b752e89:98] «FBCK-N3 (wording): SAT^K omits R71's window bound t′ − t ≤ 4n(n − 1); correct, since FB-C^K counts saturated sources through SAT-FB1^K.»
- Added to §1 after Lemma SAT^K: "R71 (b)'s window bound t′ − t ≤ 4n(n − 1) is not used: saturated sources are counted by SAT-FB1^K, which
  needs only that the second source is a K-C-state after the first (not that it is saturated)."

## F4. FBCK-N4: READER-INV has one referee (premise status)
- [Q docs/referee/R-N5-FBCK.md@6b752e89:100-101] «FBCK-N4 (premise status): Corollary (ii)'s source READER-INV (R-N5-READER §1) has one referee (L-COMP agreed on data); the corollary is an implication and stays one until READER-INV is refereed twice.»
- REFEREE-2's §C: [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:213] «FBCK-N4 (READER-INV has one referee and is not landed; Corollary (ii) stays an implication) AGREED»
- Recorded: Corollary (ii) is an IMPLICATION and stays one until READER-INV is refereed twice. The packet's premise line already says
  "refereed by one referee, NOT landed"; nothing else changes.

## F5. N-FBCK-2: the K version is a restriction; the closure of K is used (record)
- [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:142-143] «The single step needing more than restriction is SAT-FB^K's Iσ_{t+1} = ∅, where K1 (succ(x) ⊆ K) and K2 (no Even choice outside K) carry it.»
  and [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:144] «The open1 control shows that without closure SAT^K and SAT-FB^K fail.»
- REFEREE's §C: [Q docs/referee/R-N5-FBCK.md@6b752e89:122-123] «Its control open1 (non-closed K′ breaks SAT, SAT-FB, SAT-FB1) shows the closure is used, which my controls did not test: ACCEPTED, stronger evidence.»
- Recorded: K1 (closure) is a needed hypothesis, not a convenience. With K′ = the Even choice vertices and their successors (not closed),
  SAT^K, SAT-FB^K and SAT-FB1^K fail in REFEREE-2's data.

## F6. N-FBCK-3: thin spots (DATA record)
- [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:146] «The theorem's bound is never approached: at most 0.75·n_K sources per K-configuration, and nk1 does not bite.»
  and [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:147] «SAT-FB^K's alternative "P has no K-C-state after t" never occurs on its own.»
- REFEREE's figure on its own named set: [Q docs/referee/R-N5-FBCK.md@6b752e89:77] «max fallbacks from one K-configuration / n_K = 0.781 (farrise25_n32, sha1 8941d1c9: 25 of 32), as the packet's 0.78»
- Recorded: the per-K-configuration bound n_K is not approached (max 0.78 n_K). Lemma SAT-FB^K's second alternative is never exercised alone,
  so it rests on proof alone.

## F7. N-FBCK-4: premise list (record; no change)
- [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:152-153] «The premises match R71's and R73's landed claim lines. The packet uses R71 (b)'s first part only, so the R15 (d) / R57 (a) window that R71 (b) adds is not needed.»
- Same point as F3; the packet's premise line already reads "(b) Lemma SAT_C and its proof (first part and the (MON) sandwich only)".

## F8. N-FBCK-5: §4 counts differ by start choice (DATA; no change)
- [Q docs/referee-2/R2-N5-FBCK.md@991f9e27:159] «On lib41 my Σ |𝒞_f| / Σ |𝒞^K_f| is 299 / 297 against §4's 303 / 301 (different random starts; 1,230 runs vs 1,047).»
- REFEREE's lib41 figure is 261 / 259 on 726 runs (other starts, n ≤ 48). No conflict: the three counts use different random starts.

## What this file does not do
- It bounds nothing new. |𝒞^K_f(P)| is not bounded; FB-LIN stays OPEN (docs/new/N5-READER-box49.md §9-§10). FB-C° in the read frame stays
  OPEN (packet §3). G-N5-TIME stays OPEN. Not a TARGET.md claim.
