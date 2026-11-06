# Draft RESULTS Note E-3 (Lead; first fill 2026-11-06T11:26:35Z by date -u (subagent); for REFEREE and REFEREE-2 sign-off and CHECKER C126) — RESULTS R110's CONDITIONAL DEAD SC-ISO: its machine premise T^R(3) ≤ 8 is now RESULTS R112 — NOT LANDED; goes after Erratum E-2, before Dead ends

Placement: directly after «**Erratum E-2**»'s block and before «## Dead ends» in docs/RESULTS.md (at local trunk 7302bc7c: Erratum
E-2 l. 12165-12191, blank l. 12192, «## Dead ends (kept;» l. 12193). Note block = the lines between the two markers below (not landed:
this header, the sources, the checks and the markers). If R113 (docs/agents/R113-draft.md) lands first, every line number below l.
12151 moves down by 211; the insertion point is fixed by the two markers, not by number.
Sources (re-measured at local trunk 7302bc7c = origin trunk 1393ebbc plus the l-new merge; RESULTS sha1
70407ce74b93fb77fae28452e9ccd6b3ea2b01e8, 12,730 lines; GAPS sha1 f204d0a12bd3d5eb1160c64a96260e88f073dbbd, 23 lines; neither changed
by the merge):
- RESULTS R110, docs/RESULTS.md l. 11323-11596 (landed 2026-11-05 20:08Z, d056db87; CHECKER C122 32f65fe0): title l. 11323 (the
  definitions of 𝓦_d, 𝓛^R_d and T^R(d); SC-ISO; «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine)»; «together with the machine premise
  T^R(3) ≤ 8 (CaDiCaL UNSAT on L-RED's encoding, not Lean, not refereed; without it the instance shows that SC-ISO at d = 4 forces T^R(3)
  ≥ 9)»); body Claims (g) l. 11415-11433 («SIGNED UNCONDITIONALLY: the instance computation and the implication «SC-ISO at d = 4 ⇒
  T^R(3) ≥ 9»», l. 11425-11426; the premise's source «L-RED's xcnf.py encoding», l. 11430); Honest limits (iii) l. 11505-11509 («a
  CaDiCaL UNSAT on L-RED's encoding, not Lean and not landed»; «and the label changes only through a separately landed item»).
- RESULTS R112, docs/RESULTS.md l. 11909-12150 (landed 2026-11-06 10:37Z, 1393ebbc; CHECKER C123 89764538): title l. 11909 («T^R(3) ≤
  8, hence T^R(3) = 8»); Claims frame l. 11948-11951; Premise l. 12018-12022 (R110's definitions quoted verbatim); Claims (e) l.
  11991-11994 (the encoding audits); Honest limits (i), (iii) l. 12069-12075.
- The referees of R110 on the premise: REFEREE successor 23, docs/referee/R-P-IDEAL-FLIP.md (last changed 5c02d44d): l. 76 «So «SC-ISO
  at d = 4 ⇒ T^R(3) ≥ 9» is PROVED (by the instance alone). That part I SIGN.», l. 158-159 «Dropping «CONDITIONAL» needs that plus a
  faithfulness check of the encodings and a landed premise. The Lead or CHECKER decides the route.»; REFEREE-2 successor 27,
  docs/referee-2/R2-P-IDEAL-FLIP.md (dc622d03): l. 82 «G-FLIP-1 (open): MP «T^R(3) ≤ 8» is a single-encoding SAT result (L-RED's
  xcnf.py, CaDiCaL UNSAT), not Lean, not refereed, not landed.», l. 85 «RESULTS must keep that wording. The item must not be cited as an
  unconditional DEAD.».
- Form: RESULTS «**Erratum E-1**» (l. 12152) and «**Erratum E-2**» (l. 12165), and docs/agents/R105-erratum-E2-draft.md.
- Precedents: DECISIONS Lead reading L42 («A packet claim that needs an uncovered premise is not signed: it is moved to "not to sign"
  (or stated with the premise as an explicit hypothesis, labelled CONDITIONAL).»), L45 (a lift of an L42 restriction once a signed item
  covers the premise, with both referees «stating that 1E-N3 covers S4b and that the lift is consistent with their signatures»).
THE DECISIVE CHECK (diffE3.py, by script on RESULTS at 7302bc7c; full output diffE3.out in the scratch directory): is R110's T^R(d) /
𝓛^R_d EXACTLY the quantity R112 bounds?
- RESULTS sha1 70407ce74b93fb77fae28452e9ccd6b3ea2b01e8 lines 12730
- (1) R110 definition, from R110 title l. 11323: 446 chars; frame of R110 title before it: "In the IDEAL model of RESULTS R104 (premise:
  R104's definition of the model only, no theorem of R104 used; and RESULTS R109's SEG-ONCE at l = −1 only), on acyclic Ξ-graphs, with
  𝓦_d"
- (2) R112 body Premise quote of R110 (F1): 446 chars; == R110 definition (whitespace-normalised): True
- (3) R112 statement (title up to the date): In the IDEAL model of RESULTS R104 (definition only, no theorem of R104 used), on 𝓛^R_3
  (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem of R110 used: the 2-wide degree-2 ladders with levels 0, 1, 2 in
  L-RED's R197 W-convention, all acyclic Ξ-data, β's, gates and starts, ISO not assumed; T^R(d) the largest number of steps over 𝓛^R_d
  and all starts): T^R(3) ≤ 8, hence T^R(3) = 8
- R112 gloss after the citation: "the 2-wide degree-2 ladders with levels 0, 1, 2 in L-RED's R197 W-convention, all acyclic Ξ-data, β's,
  gates and starts, ISO not assumed; T^R(d) the largest number of steps over 𝓛^R_d and all starts"
- model: True; both «In the IDEAL model of RESULTS R104»; R112 «(definition only, no theorem of R104 used)», R110 «(premise: R104's
  definition of the model only, …»
- definition by citation: True; R112 cites R110's definitions of both 𝓛^R_d and T^R(d)
- T^R(d) text: True; the same 60 characters in R110 and in R112's gloss
- d: True; R112 is at d = 3; R110's premise is «T^R(3) ≤ 8»
- levels: True; R110 «levels 0, …, d − 1» at d = 3 = R112 «levels 0, 1, 2»
- acyclicity: True; R110 defines 𝓛^R_d and T^R(d) inside «on acyclic Ξ-graphs»; R112 «all acyclic Ξ-data» and body «on acyclic Ξ-graphs»
- wiring (R112 body): True; R112 Claims frame restates R110's parenthesis («no other movers» via «2-wide»)
- starts: True; all starts in both; R112 «β's, gates and starts» free
- ISO not assumed: True; R110's T^R(d) carries no ISO; ISO is a separate R110 property; R112 «ISO not assumed»
- steps = R104 L(G): True; R112 body; R110 «number of steps» of R104's run
- SC-ISO uses this T^R: True; R110's SC-ISO quote ends «… is at most T^R(d − 1)», after the definition, same symbol
- premise = R112 claim: True; R110 premise «T^R(3) ≤ 8»; R112 «T^R(3) ≤ 8, hence T^R(3) = 8»
- ALL ASPECTS EQUAL: True 12
- word diff R110 definition -> R112 gloss (difflib, whitespace tokens):
- delete: R110 has "on acyclic Ξ-graphs, with 𝓦_d the genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers named
  0 and 1, 𝓛^R_d ⊆ 𝓦_d"; R112's gloss has "-"
- insert: R110 has "-"; R112's gloss has "with levels 0, 1, 2"
- replace: R110 has "convention (movers 2l"; R112's gloss has "W-convention, all acyclic Ξ-data, β's, gates"
- replace: R110 has "2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l −
  1) + k),"; R112's gloss has "starts, ISO not assumed;"
- delete: R110 has "(kept apart from R109's T*(d) over 𝓛_d; T^R(d) ≤ T*(d))"; R112's gloss has "-"
RESULT: the definitions are IDENTICAL. R112 adopts R110's definitions by citation and quotes them verbatim (446 characters, equal to
R110's title text); its statement is at d = 3, over all acyclic Ξ-data, β's, gates and starts, ISO not assumed, with R104's number of
steps; R110's premise is exactly R112's first clause. The only textual differences are in R112's gloss after the citation, which
abbreviates R110's text: it leaves out the auxiliary class 𝓦_d and the level-0 naming (implied by the R197 wiring, movers 0 and 1 on
level 0), the wiring parenthesis (restated in R112's Claims frame, l. 11949-11951) and R110's remark on T*(d) (not part of the
definition of T^R(d)), it writes R110's frame «on acyclic Ξ-graphs» as «all acyclic Ξ-data», and it says «R197 W-convention» where R110 says «R197
convention» (CHECKER C123 and both referees of R112 diffed
the class: R112 Object, «TR-L1 MET: R110's definitions are cited, «acyclic» is added, and T^R(d) is defined verbatim from R110.»). No
difference in the class, the starts, acyclicity, ISO or the quantity, so the lift is drafted (if a referee finds one, the note does not
land).
---BEGIN NOTE BLOCK---
**Note E-3** (not a result; <DATE> <HH:MM>Z by date -u; Lead; RESULTS R110's CONDITIONAL DEAD SC-ISO, its premise now RESULTS R112):
- What changes: RESULTS R110's title line (l. 11323) lists «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine)» of the lane conjecture
  SC-ISO, false by the ISO genome iso_d4_st9 of 𝓛^R_4 «together with the machine premise T^R(3) ≤ 8 (CaDiCaL UNSAT on L-RED's encoding,
  not Lean, not refereed; without it the instance shows that SC-ISO at d = 4 forces T^R(3) ≥ 9)». Its body signs, by both referees,
  «SIGNED UNCONDITIONALLY: the instance computation and the implication «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9»» (Claims (g)), and its Honest
  limits (iii) call the premise «a CaDiCaL UNSAT on L-RED's encoding, not Lean and not landed» and say «the label changes only through
  a separately landed item». RESULTS R112 (landed 2026-11-06 10:37Z, CHECKER C123 89764538) is a separately landed item stating «T^R(3)
  ≤ 8, hence T^R(3) = 8».
- Same quantity: R112 bounds R110's own T^R(3). Its title is «on 𝓛^R_3 (RESULTS R110's definitions of 𝓛^R_d and T^R(d) only, no theorem
  of R110 used: …; T^R(d) the largest number of steps over 𝓛^R_d and all starts)», and its body quotes R110's definitions verbatim;
  scope (d = 3), acyclicity (R110 defines T^R(d) inside «on acyclic Ξ-graphs»; R112 «all acyclic Ξ-data»), starts (all), ISO (not in
  R110's T^R(d); R112 «ISO not assumed») and the quantity (R104's number of steps) agree. SC-ISO's bound «… is at most T^R(d − 1)» uses
  the same T^R.
- Effect: with RESULTS R112, R110's premise T^R(3) ≤ 8 holds, so R110's signed implication «SC-ISO at d = 4 ⇒ T^R(3) ≥ 9» gives: SC-ISO
  at d = 4 is false, by R110's instance experiments/new/box160/out/iso_d4_st9.json (sha1 7ca1e68c…; an ISO genome of 𝓛^R_4, «T 11 from
  its stored start, mover 1 moving at step 7 and mover 0 at step 8, 6 + 3 = 9 steps outside» in R110's words, against T^R(3) = 8). So the lane conjecture SC-ISO («for every d ≥ 3,
  …») is false. Read R110's «CONDITIONAL DEAD (premise T^R(3) ≤ 8, machine)» as DEAD, resting on R110 (g)'s signed instance and
  implication and on RESULTS R112.
- What it rests on: R112 is a machine-certified, refereed-only statement («(i) A MACHINE STATEMENT: the upper bound T^R(3) ≤ 8 rests on
  the UNSAT of 16 recorded DIMACS formulas», certified by DRUP proofs checked with the lane's own checker drup.c, on an audited, not
  proved, encoding; R112 Honest limits (i)), and, for all 16 cubes, regenerated byte-identically and accepted by REFEREE's independent RUP checker (R-P-TR3 Addendum 1, 365f22e1). The DEAD needs no premise outside RESULTS and is exactly as strong as R112's machine statement; it is cited as «DEAD (with RESULTS R112's machine trust base)», not as a hand-proved DEAD. The premise is
  discharged by R112's statement, not by any particular encoding: R110 named «L-RED's xcnf.py encoding» as its source, while R112 rests
  on L-COMP's «experiments/comp/box27/cnf.py, mapped clause by clause to R104 in ENCODING.md» with its certificate; nothing here uses
  xcnf.py.
- Unaffected: R110's items (a)-(f), its DATA and its instance; R112. R110's heading text and its UPDATE on GAPS l. 11 (which repeats the
  CONDITIONAL clause) stay as landed (the heading equals the MATCHED line L-3); this note governs their reading, as Erratum E-2 does for
  R105. No title, GAPS line or Dead-ends row changes (SC-ISO is a lane conjecture killed inside a landed line, CHECKER C118 §5, applied
  to SC-ISO by C122). G-N5-TIME stays open.
- Sign-off: REFEREE 5e4def16 and REFEREE-2 8db8eb95 (each: R110 (g)'s implication with RESULTS R112 gives the DEAD, and R112's
  T^R(3) is R110's), CHECKER C126 <checker>.
---END NOTE BLOCK---
FLAGS FOR THE REFEREES AND CHECKER (not part of the note):
- F-1, THE REFEREE-2 RULING ON R110 (for both referees). REFEREE-2 27 wrote «RESULTS must keep that wording. The item must not be cited as
  an unconditional DEAD.» (R2-P-IDEAL-FLIP.md l. 85), when the premise was a single-encoding, unlanded SAT result (l. 82). The note keeps
  R110's wording (heading and GAPS UPDATE unchanged) and records the change of reading through a landed item, as R110's Honest limits
  (iii) allow. REFEREE 23's conditions for dropping «CONDITIONAL» (l. 158-159: L-COMP 9's independent result, «a faithfulness check of
  the encodings and a landed premise») read as met: R112 is L-COMP 9's result on cnf.py, both R112 referees found the encoding faithful
  (REFEREE R-T3R-audit «FAITHFUL WITH GAPS (T3-G1, T3-G2; neither is an error)», T3-G2 closed; REFEREE-2 27 «The encoding is faithful to
  R104's definition on every clause»; RESULTS R112 Claims (e)), and R112 is landed (Lead reading, not a referee's words; both referees
  to confirm in their sign-off). L-RED's xcnf.py encoding was not audited by REFEREE (R112 draft (12)); the note does not need it.
- F-2, THE LABEL. "Note E-3" continues the E-numbering of the two errata; nothing in R110 is wrong, so it is not called an erratum.
  CHECKER may prefer "Erratum E-3" or another label; nothing else depends on it. E-3 as a RESULTS label occurs 0 times ("Note E-3",
  "Erratum E-3": 0 times; «E-3» occurs only inside other labels such as «N-OE-3»).
- F-3, NO GAPS UPDATE (E-2 precedent: «No title, GAPS line or Dead-ends row changes. R105's heading text and its UPDATE on GAPS l. 11
  (which repeats both clauses) stay as landed (the heading equals the MATCHED line L-2); this erratum governs their reading.»). GAPS
  mentions SC-ISO 3 times, all inside R110's UPDATE on l. 11; no GAPS row depends on SC-ISO. If the Lead prefers a GAPS record, an
  UPDATE head "UPDATE <DATE> <HH:MM>Z: RESULTS Note E-3 (CHECKER C126 <checker>)" could be appended to l. 11; not drafted.
- F-4, NO DEAD-ENDS ROW. CHECKER C122 l. 60 «No Dead-ends row (C118 §5; here the kill is also conditional): agreed.»: the first
  ground (a lane conjecture killed inside a landed line) still holds; the next free Dead-ends number stays DE37 («DE37» 0 times in
  RESULTS). CHECKER to confirm.
- F-5, WHAT THE DEAD RESTS ON. The DEAD now carries R112's trust base (machine certificate, own RUP checker, audited encoding); the note
  says so instead of calling it a hand proof.
- F-6, PLACEHOLDERS: <DATE>, <HH:MM>, <checker> (as E-2's draft), plus <referee> and <referee-2>, the two sign-off commits, filled when
  the referees' files exist. If the Lead prefers the E-2 form (no sign-off line), the last bullet can be dropped by the same script.
CHECKS (by script, chkE3 = chk113.py in its E3 mode, simE3.py):
- Quote sweep (chk113.py in its E3 mode, the R113 rule: outermost guillemet quotes, whitespace joined, split at the ellipsis, parts of
  6+ characters; sources as for R113 plus docs/referee/R-P-IDEAL-FLIP.md at 5c02d44d, docs/referee-2/R2-P-IDEAL-FLIP.md at dc622d03 and
  docs/checker/C118.md): whole file 67 outermost quotes, 67 parts, 0 not found; the note block alone 17 quotes, 18 parts, 0 not found.
  Line-precise: 25 of 25 (source, cited line range, quote) triples found verbatim, whitespace-normalised, inside the cited lines
  (lpE3.py).
- "|": 0 in the note block; outside it only inside double quotes in this CHECKS list. The block is 30 lines, 3,483 bytes.
- Placeholders in the block: <DATE> 1, <HH:MM> 1, <checker> 1 (the CHECKER C126 commit), <referee> 1, <referee-2> 1 (the two sign-off
  commits); all filled at landing.
- Definition diff (diffE3.py): R112's quote of R110's definitions equals R110's title text (446 characters): True; all 12 aspects equal:
  True.
- LANDING SIMULATION (simE3.py, on an in-memory copy of RESULTS at the local trunk): RESULTS 12,730 -> 12,761 lines (wc -l), a pure
  insertion of 31 lines (the note block, placeholders filled with simulation values, plus one blank line) directly after Erratum E-2's
  block (E-2 l. 12,165, its blank line l. 12,192, byte-unchanged: True) and before the Dead ends heading, which moves from l. 12,193 to
  l. 12,224: True; order E-1, E-2, Note E-3, Dead ends: True; every other line byte-unchanged (common prefix and suffix: True); "|" in
  the note block: 0. GAPS: not changed (no UPDATE; l. 11 keeps 76 "|" and 47 UPDATE 2026- heads; 23 lines). Placeholders in the block:
  <DATE> 1, <HH:MM> 1, <checker> 1, <referee> 1, <referee-2> 1.
- GAPS consequence: none (E-2 precedent; F-3). G-N5-TIME stays open.
- NOT RUN: scripts/verify.sh; no referee or CHECKER file for this note exists yet.

LEAD EDIT after sign-off (2026-11-06 13:02Z by date -u): applied to the block, verbatim from the referees' files:
- REFEREE-2 E3-W1 (required; R2-NOTE-E3.md, 8db8eb95): «The DEAD is unconditional within RESULTS and exactly as strong as R112.» replaced by
  REFEREE-2's sentence «The DEAD needs no premise outside RESULTS and is exactly as strong as R112's machine statement; it is cited as «DEAD
  (with RESULTS R112's machine trust base)», not as a hand-proved DEAD.»
- REFEREE E3-1 (optional; R-P-IDEAL-FLIP.md §D, 5e4def16): the instance clause now quotes R110's own words «T 11 from its stored start,
  mover 1 moving at step 7 and mover 0 at step 8, 6 + 3 = 9 steps outside».
- REFEREE E3-2 (optional): «, and, for all 16 cubes, regenerated byte-identically and accepted by REFEREE's independent RUP checker
  (R-P-TR3 Addendum 1, 365f22e1)» added after «R112 Honest limits (i))».
- Sign-off placeholders filled: REFEREE 5e4def16, REFEREE-2 8db8eb95. Remaining placeholders: <DATE>, <HH:MM>, <checker>.
