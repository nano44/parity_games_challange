# Draft RESULTS R89 (Lead, 2026-10-29 22:31Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C99 (REVISED 23:11Z by date -u for C99 E-1: moves (1)-(2) applied verbatim (cee834e5 §3); optional N-2, N-3 applied (REFEREE H17 line d6aebf78 / 4f3f75d0 recorded); N-1, N-4 no change. Earlier: subagent draft, sha1 5d8e48ec before review; Lead reviewed 22:39Z by date -u: unsure points (1) title date kept once as in the H0 line, (2) GP*-RUN stays in the entry as item (h): it is now signed by BOTH referees, so R88's one-referee G2 READING is superseded for W-runs, (3) [OPT-H] kept as a cross-reference name for the step both referees quote (S4a's one-player optimum of H_t) — CHECKER to judge; no text changed; Lead decisions for CHECKER — LANDED in RESULTS Results 2026-10-29 23:27Z (CHECKER C99 Add. 1 3d9ce0ef PASS), after R88
to check: (1) the title is the H0 line file docs/new/P-N5-FRAME-box65-line-H0.txt (l-new d3d98d1c, sha1 ab1ee38a…, = the approved line acf3234f… with
H0's two insertions) verbatim, nothing dropped (the file has no outer quotes and no final period); the line ALREADY carries " (2026-10-29)" right
before " — a REDUCTION" (L-NEW wrote the date in; R88's G12 line had none), so no second date is inserted; the checker fill ", CHECKER PASS
(docs/checker/C99.md, checker PENDING)" is appended as in R88; (2) Claims signed = the ten §0 items plus STRETCH-RED's "Consequence (to sign as
stated)", each SIGNED in both verdict tables; N-FR-4 / FR-N2 with H10, and H9, H12, H14, appear only under Referee strengthening; (3) premise
labels tested against the later landed entries (C96 lesson): after R86, RESULTS has R87, R88 and DE35, and none of them changes [R85c], [R86e],
[R47a], [R56] or the standing premise 1E-N3; [R86e] is labelled "displayed in RESULTS" (R86 headline l. 5269, body (e) l. 5345-5357; REFEREE-2
N-FR-1, fixes H7), not with the Lead brief's "not a displayed RESULTS statement" (LEAD-STATE 20:45Z entry); W-MON's premise [OPT-H] (RESULTS R88
(a)) is named as inherited by GP*-RUN and STRETCH-RED; (4) GP*-RUN contains the content of R88's Referee strengthening (0) (G2, a one-referee
READING in R88) and widens it (λ_Ξ may change); this is said in item (h) with the referees' own words, and R88's entry is not touched; (5) a GAPS
line-11 UPDATE is proposed (the entry is about N5 itself), built from the title clauses only, with no "|"; (6) no lane work after the freeze
(L-SI boxes 36-39, L-RED R117-R122, L-NEW after H17) is in the entry. Three small discrepancies are recorded in the entry for CHECKER: REFEREE-2
l. 8 writes the line sha1 with 39 hex digits; fixes H0 l. 18's "bytes" are characters; check.sh's box 63 block prints a "box 59" label on failure.)

### R89 [refereed-only] N5 on EVERY game (SPEC S1-S5; W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays, λ_W its cycle-node map; a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W; U, τ̄(τ), λ^U-runs, ENT, RISE, PCH as in RESULTS R86, blocked edges and late adoptions as in RESULTS R88): (Lemma FRAME-τ) in S4a's arena every Odd v keeps only τ(v), every transition has τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o), no τ repeats in a run, and Iτ_t depends on τ_t alone; (Lemma ODD-FREEZE) at any state, for Odd o and e ∈ succ(o) with e ≠ τ(o), if some positional Even σ_e equal to τ̄(τ) at every Even vertex outside P_e makes the (τ, σ_e)-play from e reach o before repeating a vertex, P_e being that play up to and including its first visit of o, the (τ, τ̄(τ))-play from τ(o) has no vertex in P_e, and the most relevant vertex of P_e has even priority and is more relevant than the cycle node of the (τ, τ̄(τ))-play from τ(o) ("(o, e) protected"), then (o, e) ∉ Iτ, so (Lemma ENT-FREEZE) τ_{t+1}(o) ≠ e; (Corollary COMPOSE-FREEZE) on every λ^U-run R, ENT_R(o, e) = 0 unless (o, e) is unprotected at some state t of R with t + 1 ∈ R and τ_t(o) ≠ e, and otherwise ENT_R(o, e) ≤ n(PCH^U_R(e) + 1), so the τ-changing transitions of a run number at most n(n − 1) + (n(n − 1) + 1)·max_R Σ_{(o, e) unprotected in R} n(PCH^U_R(e) + 1), where, by RESULTS R85 (c)'s per-vertex MATCH-Φ on λ^U-runs (the premise RESULTS R86 (e) signs as holding), PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e) (NM^U_R(e) := the carries of U(e) in R, read with G^d's parities, RESULTS R86 (e) F3); (Lemma SUCC-MON) Ξ_t(σ_t(y)) is non-decreasing in t for every Even y, and (Lemma LATE-RISE) (y, z) ∉ Iσ_t, (y, z) ∈ Iσ_u, t < u imply Ξ_u(z) ▷ Ξ_t(z); (Lemma GP*-RUN) RESULTS R88's Lemma GP* and Corollary FW-R* hold on every W-run (σ̄ and λ_Ξ need not be constant there), and (Corollary R*-RISE) in a W-run F the late adoptions of each Even edge (y, z) are at most the transitions of F at which Ξ(z) changes; (Theorem STRETCH-RED) every τ-stretch S has at most Q + (Q + 1)((n − 1)(R*_S + 1) + FL_S) transitions, where Q := the transitions of S that are an S4c fallback or change λ_W, and Q ≤ fb_S + n(n − 1)(fb_S + 1), fb_S ≤ n(n − 1) + (n(n − 1) + 1)(1 + (n − 1)(2 + ρ_S)), with fb_S its S4c fallbacks, R*_S the largest R*_T of one of its W-runs, FL_S its transitions with σ_{t+1} ≠ σ_t and W_{t+1} = W_t, and ρ_S the largest RESULTS R56 ρ of a phase meeting S (2026-10-29) — a REDUCTION (NM^U on unprotected targets, R*_S (hence Even's PCH), FL_S and ρ_S are not bounded here; G-N5-TIME stays open; not M3, not a step-4 pass, not a TARGET.md claim), CHECKER PASS (docs/checker/C99.md, checker PENDING)
- Object (L-NEW successor 35, Opus 5.5, D14/D18, Lead reading L40; frozen, unchanged during review): packet P-N5-FRAME,
  docs/new/P-N5-FRAME-box65.md, sha1 ce8c4803ee18dc90ee761863d006d0aca0476542, 194 lines (l-new freeze
  938d87967ce501058bc6d015e506403c73858034, 2026-10-29T20:45:31Z; `git diff --numstat 22c6a165 938d8796` on the file: 1 added, 1 removed,
  the Status line only (DRAFT → FROZEN), as LEAD-STATE 20:57Z records «diff vs approved draft 22c6a165 = header line only»; the file is
  identical at l-new head 9631bbc5 and at trunk a60e5704; quote base l-new 9905dac3 (2026-10-29T20:18:48Z) for SPEC l. 28-57 («unchanged
  since 2a435f8f4, R88's base», l. 6) and RESULTS c9045f86 for [R85c]; no quote check and no sha1 assertion for the packet is pinned in
  experiments/new/check.sh (`grep -c ce8c4803` = 0); both referees checked the quotes with their own scripts (REFEREE l. 8: «the packet's 8
  SPEC quotes checked by my own script: 8/8 verbatim», R85 (c) «quote verbatim»; REFEREE-2 l. 25, l. 42-46: 9/9, fquote.py, SHIFT=1 control
  0/9) and measured the packet sha1 at 938d8796 (REFEREE l. 3-4; REFEREE-2 l. 6-7)): §0 what to sign (l. 8-21), §1 setting, premises and new
  definitions (l. 23-73), §2 the Odd side (FRAME-τ, DUAL-ORDER, ODD-FREEZE, ENT-FREEZE, COMPOSE-FREEZE), §3 the Even side inside a τ-stretch
  (SUCC-MON, LATE-RISE, GP*-RUN, R*-RISE, STRETCH-RED and its Consequence), §4 READING and DATA («NOT to sign», l. 21, l. 181-189). The freeze
  commit's stamp «Lead 20:47Z» (l. 5) is later than its git time 20:45:31Z; LEAD-STATE's 20:45Z entry also says "APPROVED 20:47Z".
  The RESULTS line, history. (1) The approved line: docs/new/P-N5-FRAME-box65-line.txt, sha1 acf3234f840cb682d71444501e89cfd61247dcd6 (at
  22c6a165 and 938d8796), approved by the Lead (packet l. 5: «freeze. Your RESULTS line (P-N5-FRAME-box65-line.txt, sha1 acf3234f…) is
  APPROVED as worded.»). (2) E-items on it. E1 (REFEREE-2 N-FR-7, §5 l. 243-252, REQUIRED): Q is not defined in the line; «with Q free, reads
  as a claim for any Q under the bound. Q = 0 then claims |S| ≤ (n − 1)(R*_S + 1) + FL_S, which is FALSE» (mk_6_24 n 150: |S| 162 > 149; mk_8_32 n 198: 280 > 197; mk_16_100 n 498: 1648 > 497; in each Q = |S|; REFEREE-2 l. 248-249 writes «(n 149)» … «162 > 148» and «(n 197): |S| 280 > 196», n − 1 for n (the file headers' largest index; CHECKER C99 §3), conclusion unchanged). REFEREE first wrote "MATCHES" (l. 29) and withdrew it (§C §2 l. 26-27: «My
  report's §6 listed "every symbol (fb_S, R*_S, FL_S, ρ_S) ✓" and missed Q: my "MATCHES" was WRONG on this point. Withdrawn: the line as worded
  does NOT match.»), reproducing mk_6_24 on its own engine (l. 29-32: 162 ≤ 149 demanded; its parser counts n = 150). E2 (both): NM^U_R(e)
  undefined in the line (REFEREE FR-N4, «optional», l. 141; REFEREE-2 N-FR-7 second half, «precision»); REFEREE-2 §C C.3 l. 51 classes it
  E2 «(both)», REFEREE §C §3 l. 41 «recommended, in H0». LEAD-STATE 21:48Z: «LEAD MISS in my 20:47Z line check (third line error today; a line
  must define every symbol it bounds)». (3) The correction H0 (fixes l. 9-26): docs/new/P-N5-FRAME-box65-line-H0.txt (l-new d3d98d1c, sha1
  ab1ee38a45f0637216de2287c3020165cdd542f0, one line, = trunk and l-new head), «the approved line with exactly two insertions (the Lead's
  21:48Z wording)»: (i) «where Q := the transitions of S that are an S4c fallback or change λ_W, and » after «… + FL_S) transitions, »; (ii)
  « (NM^U_R(e) := the carries of U(e) in R, read with G^d's parities, RESULTS R86 (e) F3)» after «PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) +
  NM^U_R(e)». Re-measured for this draft: `git diff --no-index --word-diff` of the two files shows these two insertions and nothing else;
  2,679 → 2,842 bytes, 2,567 → 2,729 characters (H0 l. 18's "(2567 → 2729 bytes)" counts characters). Checked by both: REFEREE §C §4 l.
  59-66 (difflib character diff, «EXACTLY two insertions, nothing else changed»; «H0 DISCHARGES THE E-ITEM.»); REFEREE-2 §C.7 l. 93-99 (word
  diff; «H0 discharges E1 and E2.» (bold in the source) «Every symbol in the line is now defined in it, in SPEC, or in the cited RESULTS
  items. It claims nothing beyond §2-§3.»). The title is the H0 line verbatim; the acf3234f line is superseded and is not this entry's title.
  The referees' notes are answered by the lane in docs/new/P-N5-FRAME-fixes-box65.md: H0-H16 (L-NEW successor 35, l-new
  d3d98d1c0274dc40e2616dacecfc12dd1e447179, 2026-10-29T21:49:39Z, sha1 b1127e579c48d4bc1213b13d21b213113bbd18d3 there, 78 lines); H17
  appended (l-new 9631bbc5a213f7e232ab8e6637ab4649b7b72058, 2026-10-29T22:10:54Z; `git diff --numstat d3d98d1c 9631bbc5`: 4 added, 0
  removed; sha1 eb5bd5e1e54d2abe465648b2b648d9341bce4bb5, 82 lines, = trunk = l-new head). Header (l. 6-7): «H0 is the one REQUIRED correction
  (of the RESULTS line, not of the packet). H1-H16 are clarifications. Every sharpening below is a READING, not a widening, unless both referees
  sign it. No signed statement of the packet changes.» H1 and H8 name ODD-FREEZE's standing premise; H2 keeps (H2); H3 = H11: every S4c
  transition inside a τ-stretch is an Even fallback; H4 = H0 (ii); H5 the Consequence's parenthetical; H6 GP*-RUN's inherited R88 (G12)
  hypotheses; H7 [R86e] is displayed; H9, H12, H14 READINGs and H10 a CONJECTURE (Referee strengthening); H13 = H0; H15 an identity; H16 DATA,
  replaced by H17 (REFEREE-2's own N-FR-10 error, §C.7 l. 132-146). No quote check is pinned for the fixes file. The statements below are in
  the frozen wording, read with H1, H3, H5, H6, H8 and H15.
  Setting (every game): N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4; G = (V, E, Ω, owner), n = |V|, m_E (m_O) the edges
  leaving Even (Odd) vertices; a run is the sequence of states (σ_t, τ_t), a TRANSITION is t → t + 1. [S1-val], [S1-ord] (⊴, ◁ strict),
  [S1-Xi] (Ξ_t := Ξ_{σ_t}, σ̄_t, λ_t = λ_Ξ), [S1-dual] (G^d: owner swapped, Ω + 1; U_t := Ξτ_t on G^d, τ̄_t its counterstrategy, λ^U_t its
  cycle-node map, as in RESULTS R86 / R47), [S2] (Iσ, Iτ), [S4a], [S4b], [S4c], quoted at 9905dac3 (l. 26-46). [R88]: W_t := the valuation
  [S1-val] of the (σ_t, τ_t)-plays, λ_W its cycle-node map, G_τ := G with Odd fixed to τ; BLOCKED at t: W_t(z) ▷ W_t(σ_t x) and (x, z) ∉ Iσ_t
  (l. 63-65). New definitions (l. 68-73): «τ-STRETCH: a maximal run of consecutive states with τ_t constant»; «W-RUN: a maximal run of
  consecutive states of one τ-stretch such that no transition t → t + 1 inside it is an S4c fallback or changes λ_W. (σ̄_t and λ_Ξ may change
  inside a W-run.)»; (o, e) PROTECTED AT t if ODD-FREEZE's (H1′), (H2), (H3) hold at t; «PCH^U_R(e): the transitions of the λ^U-run R at which
  the path set of U(e) changes (R86's PCH on G^d)». §1 cells: REFEREE «CHECKED» (l. 16); REFEREE-2 «well formed; 9/9 quotes verbatim (own
  fquote.py; SHIFT=1 control 0/9); every cited RESULTS item says what the packet uses (§1)» (l. 25); both §Cs: "same" (REFEREE §C l. 9),
  "agree" (REFEREE-2 §C l. 10).
- Claims signed (both referees "(Opus 5.5, D15)": REFEREE successor 18, REFEREE-2 successor 21). Each item below is SIGNED in both verdict
  tables (REFEREE "## Verdicts", l. 13-31 of R-N5-FRAME.md; REFEREE-2 "## 0. Verdicts", l. 22-39 of R2-N5-FRAME.md; REFEREE §C table l. 7-20
  "SIGNED" in the joint column; REFEREE-2 §C C.1 l. 8-24 "SIGNED by both"), in the frozen wording. Every game; plain N5. Premises LANDED:
  SPEC S1 ([S1-val], [S1-ord], [S1-Xi], [S1-dual]), S2, S4a, S4b, S4c (quote base 9905dac3); RESULTS R15 (a), (c), (d); RESULTS R17 (a) [F1];
  RESULTS R38 (a), as the phase definition; RESULTS R47 Lemma Φ ([R47a]: at most n(n − 1) transitions change λ and at most n(n − 1) change
  λ^U, every game; REFEREE-2 l. 47); RESULTS R56 Theorem FB-RED ([R56], l. 66-67; REFEREE «R56 (f)», l. 100); RESULTS R84 (a) Fact DELTA;
  RESULTS R85 (c) ([R85c], RESULTS l. 5108-5109, the per-vertex form); RESULTS R86 Lemmas SW-RETURN and LEN-MONO (dual forms on G^d) and
  (e) ([R86e], below); RESULTS R88 Lemma W-MON, Lemma GP*, Corollary FW-R* and their object docs/si/P-N5-GP-box31.md (sha1 cd4866df…).
  Standing premises (disclosure, not a widening): ODD-FREEZE's third step uses that τ̄ := τ̄(τ) is the G^d-Odd player's optimal
  counterstrategy to τ «AT EVERY VERTEX AT ONCE, and U is REALISED by it» (H1, l. 29-32: «This is RESULTS R57 (b)'s premise, mirrored on G^d
  (as in P-N5-SF fixes F7)»), cited as «RESULTS R57 (a) (VJ) on G^d, the citation RESULTS R85's Fact B2 uses for the same step» (H8, l.
  53-55); REFEREE FR-N1 (l. 136-137), REFEREE-2 N-FR-2 (l. 263-264); REFEREE-2 §C C.2 l. 39: «FR-N1 is the fuller statement, and I ACCEPT it»
  (its UPLAY check, 0). GP*-RUN, and STRETCH-RED through it, use R88's W-MON, which RESULTS R88 (a) signs with the premise [OPT-H] (standing
  SPEC premise 1E-N3, form P2: S4a's σ_new is Even's one-player optimum of H_t); both referees name that step (REFEREE §4 l. 75-76: «σ_new is
  S4a's one-player optimum of H_t ∋ σ_t, [F1]»; REFEREE-2 §3.3 l. 135-136). The code's match to SPEC is DATA (R15 G-N5T-1).
  (a) Lemma FRAME-τ (§2.1, l. 77-78): "(i) In [S4a]'s arena H, every Odd vertex v keeps only the edge to τ(v). (ii) At every transition,
      τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o) for every Odd o. (iii) No value of τ repeats along a run. (iv) Iτ_t depends on τ_t alone." ((i) is
      [S4a]; (ii) S4b's H′, S4c's Odd branch picks from Iτ, its Even branch and S4a leave τ; (iii) each τ-change is Switch_I on G^d with ∅ ≠ I
      ⊆ Iτ (R15 (d)), no repeat by R15 (c) on G^d; (iv) Iτ is read from Ξτ on G^d.) Cells: REFEREE «SIGNED» (l. 17); REFEREE-2 «SIGNED» (l. 26).
  (b) Lemma DUAL-ORDER (§2.2, l. 84-85; box 21 §2.1 Lemma R restated): "For any two plays π, π′ of G, their [S1-val] triples (c, P, ℓ) are the
      same in G and G^d (relevance = rank, the same in both games), and π is strictly better for Even than π′ in G's [S1-ord] iff π is
      strictly worse for the G^d-Even player (Odd) than π′ in G^d's [S1-ord]." (Ω + 1 keeps the (Ω, v) order; reward, signed weight and the
      length rule each reverse.) Cells: REFEREE «SIGNED» (l. 18); REFEREE-2 «SIGNED» (l. 27).
  (c) Lemma ODD-FREEZE (§2.3, l. 94-103), with H1 and H8: Setting: a state (σ, τ), τ̄ := τ̄(τ), o Odd, e ∈ succ(o), e ≠ τ(o); «For an Even
      strategy α let P_e(α) be the (τ, α)-play from e up to and INCLUDING its first visit of o (if any).» «(H1′) there is a positional Even
      strategy σ_e with σ_e(x) = τ̄(x) for every Even x ∉ P_e(σ_e), such that the (τ, σ_e)-play from e visits o before it repeats a vertex;
      write P_e := P_e(σ_e) (a simple path ending at o);» «(H2) the (τ, τ̄)-play from τ(o) has no vertex in P_e;» «(H3) the most relevant
      vertex x of P_e has even Ω, and x is more relevant than the cycle node w of the (τ, τ̄)-play from τ(o).» "Claim: (o, e) ∉ Iτ." (By (H2) and σ_e
      = τ̄ off P_e the play from τ(o) is π_o, disjoint from P_e; the play from e has cycle node w and path set P_o ∪ {y ∈ P_e above w}, whose
      top x is even, so it is strictly better for Even than π_o; τ̄ maximises G's order for Even among (τ, α)-plays (DUAL-ORDER), so U(e) ▷
      U(τ(o)) in G, i.e. worse for the G^d-Even player; [S2] on G^d.) Cells: REFEREE «SIGNED (every inequality direction checked, §2; standing
      premise FR-N1)» (l. 19); REFEREE-2 «SIGNED (every inequality direction checked, §2.3; the optimality step is R57 (a) (VJ) on G^d:
      N-FR-2)» (l. 28). REFEREE-2 §C C.2 l. 33: «ODD-FREEZE directions: identical chains.»
  (d) Lemma ENT-FREEZE (§2.4, l. 118): "If (o, e) is protected at t (and τ_t(o) ≠ e), then τ_{t+1}(o) ≠ e." (ODD-FREEZE and FRAME-τ (ii).)
      Cells: REFEREE «SIGNED» (l. 20); REFEREE-2 «SIGNED» (l. 29).
  (e) Corollary COMPOSE-FREEZE (§2.5, l. 121-128), with H15 and H7: «Let R be a λ^U-run (R86). Call (o, e) UNPROTECTED IN R if at some state t
      of R with t + 1 ∈ R and τ_t(o) ≠ e, (o, e) is not protected at t; UNP_R := the set of such Odd edges.» "(a) ENT_R(o, e) = 0 for every
      Odd edge (o, e) ∉ UNP_R; (b) ENT_R(o, e) ≤ 1 + RISE^U_R(e) ≤ n·(PCH^U_R(e) + 1) for (o, e) ∈ UNP_R; (c) the Odd switches in R (Σ over
      Odd o of the transitions of R at which τ(o) changes) are at most Σ_{(o, e) ∈ UNP_R} n·(PCH^U_R(e) + 1); (d) the τ-changing transitions of
      the whole run are at most n(n − 1) + (n(n − 1) + 1)·max_R Σ_{(o, e) ∈ UNP_R} n·(PCH^U_R(e) + 1). (e) with [R85c] / [R86e] per vertex on
      λ^U-runs: PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e), so (b)-(d) hold with PCH^U_R(e) replaced by that bound, i.e. in terms of the
      carries NM^U_R(e) of the targets of unprotected Odd edges only." ((a) ENT-FREEZE; (b) R86 SW-RETURN (dual), then LEN-MONO (dual) on R;
      H15: «the second "≤" is "="»; (c) every Odd switch enters some e; (d) [R47a]: ≤ n(n − 1) λ^U-changing transitions, every other
      τ-changing transition lies in one of ≤ n(n − 1) + 1 λ^U-runs.) [R86e] (l. 59-62): R86 (e)'s premise «[MΦ] holds with "phase" replaced
      by "λ-run" (resp. "λ^U-run" on G^d)», signed as holding in both R86 cells, with NM^U read with G^d's parities (F3); it is displayed in
      RESULTS (R86 headline l. 5269; body (e) l. 5345-5357). Cells: REFEREE (a)-(d) «SIGNED» (l. 21), (e) «SIGNED: [R86e] suffices (§3)» (l.
      22; §3 l. 64-70: «the per-vertex form on λ^U-runs is exactly what was signed»); REFEREE-2 «SIGNED. (e)'s premise [R86e] ACCEPTED as a
      premise: it IS displayed in RESULTS (R86 headline and body (e)); no re-proof needed (§2.5, N-FR-1)» (l. 30). H7 (l. 51-52): «[R86e] is
      displayed in RESULTS: in R86's headline and in body (e), l. 5345-5357. The brief's (and my packet's) "not a displayed RESULTS statement"
      was inaccurate.»
  (f) Lemma SUCC-MON (§3.1, l. 136): "For every Even y, Ξ_t(σ_t(y)) is non-decreasing (⊴) in t along every run." (σ_{t+1}(y) ∈ {σ_t(y)} ∪
      Iσ_t(y); Ξ_{t+1} ⊵ Ξ_t pointwise by R15 (d), (a); [S2] for the switch.) Cells: REFEREE «SIGNED» (l. 23); REFEREE-2 «SIGNED» (l. 31).
  (g) Lemma LATE-RISE (§3.2, l. 141): "If (y, z) ∉ Iσ_t and (y, z) ∈ Iσ_u with t < u, then Ξ_u(z) ▷ Ξ_t(z)." (Ξ_u(z) ▷ Ξ_u(σ_u y) ⊵ Ξ_t(σ_t y)
      ⊵ Ξ_t(z).) Cells: REFEREE «SIGNED» (l. 24); REFEREE-2 «SIGNED» (l. 32).
  (h) Lemma GP*-RUN (§3.3, l. 144-146), with H6: "On every W-run F = [a, b], R88's Lemma GP* and Corollary FW-R* hold verbatim, with F in place
      of the frozen W-phase: for every k ∈ [a, b], W_k(r_0) ⊵ value(r) for every path r unblocked at state k (R88 §3's definition, "blocked at
      t" read at state t of F); and F has at most (n − 1)(R*_T + 1) W-changing transitions, R*_T := the transitions of F containing a late
      adoption (R88 §4's definition, read on F)." H6 (l. 43-48): GP*-RUN «inherits R88's FINAL (G12) hypotheses verbatim, read on the W-run F =
      [a, b]: a path r = (x = r_0, …, r_L = u) of G_τ (Odd r_i: r_{i+1} = τ(r_i)), simple, with L ≤ k − a edges, ending at a W-cycle node u of
      F's first state a (λ_W(u) = u), none of whose Even edges (r_i, r_{i+1}) is blocked at state k − 1 − i; and FW-R* with R*_T counted on F.»
      (R88's W-MON, GP* and FW-R* proofs use τ constant, no S4c fallback, λ_W constant and [S4a]; σ̄, D, U_t, S_{d,t} and λ_Ξ occur only in R88
      §3a, not restated.) Cells: REFEREE «SIGNED: no step of R88's W-MON, GP*, FW-R* uses σ̄, D or λ_Ξ (§4)» (l. 25); REFEREE-2 «SIGNED. R88's
      proofs (W-MON, GP* all cases, FW-R*) checked line by line: no step uses σ̄, D or λ_Ξ constant (§3.3)» (l. 33). Relation to RESULTS R88:
      packet §0 l. 18 «a widening of a landed result, its own item»; REFEREE §4 l. 73: «I reviewed R88 (R-N5-GP.md) and recorded then (GP-N2)
      that GP*'s proof uses only τ constant, no S4c transition, λ_W constant», l. 80: «So GP*-RUN is a true widening of R88»; REFEREE-2 §3.3 l.
      134 «(a widening of landed R88)». GP-N2 = G2 is RESULTS R88's Referee strengthening (0) (RESULTS l. 5759-5770), a one-referee READING
      there for runs of in-phase states with σ̄-changes; GP*-RUN, signed by both here, also lets λ_Ξ change (a W-run lies in a τ-stretch, not
      in one phase). R88's own entry is unchanged.
  (i) Corollary R*-RISE (§3.4, l. 155-157): "In every W-run F, the late adoptions of a fixed Even edge (y, z) (transitions of F at which σ(y)
      becomes z after (y, z) was blocked at an earlier state of F) number at most RISE_F(z), the transitions of F at which Ξ(z) changes. Hence
      R*_T ≤ Σ_z d_E(z)·RISE_F(z), d_E(z) the number of Even predecessors of z." (t_1 a blocked state, t_i := u_{i−1} + 1; each adoption is from
      Iσ_{u_i}; LATE-RISE gives a Ξ(z)-change in [t_i, u_i); the intervals are disjoint and inside F.) Cells: REFEREE «SIGNED» (l. 26);
      REFEREE-2 «SIGNED» (l. 34).
  (j) Theorem STRETCH-RED (§3.5, l. 164-167), with H3: «Let S be a τ-stretch. Let fb_S := the S4c fallbacks inside S; R*_S := the largest
      R*_T of a W-run of S; FL_S := the transitions of S with σ_{t+1} ≠ σ_t and W_{t+1} = W_t; ρ_S := the largest R56 ρ of a phase meeting S.
      Let |S| := the transitions inside S (all change σ: τ is constant and every transition changes σ or τ, R15 (d)).» "Then |S| ≤ Q + (Q +
      1)·((n − 1)(R*_S + 1) + FL_S), Q ≤ fb_S + n(n − 1)(fb_S + 1), fb_S ≤ n(n − 1) + (n(n − 1) + 1)·(1 + (n − 1)(2 + ρ_S))." with, from the
      proof (l. 169), «Q := the transitions of S that are a fallback or change λ_W» (the definition H0 (i) writes into the line). (Cutting the
      Q transitions leaves ≤ Q + 1 W-runs; GP*-RUN on each, plus the W-flat ones; λ_W changes ≤ n − 1 per vertex per fallback-free piece by
      W-MON; fb_S: H3 «Every S4c transition inside a τ-stretch is an EVEN fallback», ≤ n(n − 1) + 1 phases meet S ([R47a]), each with ≤ 1 + (n −
      1)(2 + ρ) in-phase fallbacks ([R56]), plus ≤ n(n − 1) λ_Ξ-changing ones.) Cells: REFEREE «SIGNED (fallback count checked, §5)» (l. 27);
      REFEREE-2 «SIGNED (fallback count correct when τ is constant: §3.5, N-FR-5)» (l. 35).
  (k) STRETCH-RED's "Consequence (to sign as stated)" (§3.5, l. 177-179), with H5: "with R*-RISE and [R86] LEN-MONO, R*_S is bounded by a
      polynomial in n, m_E and the largest PCH_R(z) over λ-runs R meeting S." H5 (l. 40-42): the parenthetical's count «omits» the additive ≤
      n(n − 1) λ_Ξ-changing transitions of a W-run; «The Consequence ("polynomial in n, m_E and the largest PCH_R(z)") is unaffected: the term
      is polynomial.» (REFEREE §5 l. 102-105 and REFEREE-2 §3.5 l. 180-183: R*_S ≤ m_E·(n(n − 1) + (n(n − 1) + 1)·n·(P + 1)).) Cells: REFEREE
      «SIGNED» (l. 28); REFEREE-2 «Consequence SIGNED» (l. 35).
  The RESULTS line: acf3234f DOES NOT MATCH as worded (REFEREE §C l. 20 joint column «DOES NOT MATCH as worded: E-item»; REFEREE-2 l. 37 and §C
  C.3, E1 and E2); the H0 line MATCHES (REFEREE §C §4 l. 66: «With it the line matches §2-§3 and every symbol is defined in the line or in the
  RESULTS items it cites»; REFEREE-2 §C.7 l. 98-99). The line omits DUAL-ORDER, COMPOSE-FREEZE (c), R*-RISE's sum form and the Consequence
  (REFEREE §6 l. 111-113: «the line may claim less», «DUAL-ORDER and the Consequence are not in the line (it claims less)»; REFEREE-2 §5 l.
  237, l. 241: «(c) and the RISE intermediate are omitted, which is fine», «(per edge; the sum form omitted)»); they are signed items (b),
  (e), (i), (k) above.
- Not signed: §4 (READING and DATA, «NOT to sign», l. 21): the READING «combined with box 21 Theorem B (N5 ≤ (C_τ + 1)(F_E + 1), lane),
  STRETCH-RED bounds N5 through ρ, P*, FL and C_τ; R86 COMPOSE-RUN with COMPOSE-FREEZE bounds it through P* and P^U on UNP alone» (l.
  182-184), and the DATA (Data below). The superseded approved line acf3234f: not this entry's title. The packet's working notes
  (docs/new/N5-FREEZE-box63.md, N5-DW-box62.md, N5-STRETCH-box64.md; «THIS packet governs where they differ», l. 3-4) and their lane labels:
  not refereed here. Fixes H9, H12, H14 (READINGs) and H10 (CONJECTURE, OPEN): Referee strengthening. H16's DATA attribution: superseded by
  H17 (Data).
- Referee strengthening (NOT part of this entry; remarks of one or both referees outside the verdict cells, or optional wording):
  (0) (H2) never bites. REFEREE FR-N2 (l. 138): «Its necessity is not exhibited in my data (MUT 2: 0) … It is used by the proof; nothing to
  change.»; REFEREE-2 N-FR-4 (l. 268-271): «Dropping (H2) (keeping (H1′), (H3)) never produced an edge of Iτ: X_OF_noH2 = 0 on every run state
  and on every τ of 1,650 small games (27,435 τ)», «A possible strengthening, OPEN, not needed for any signature». H2 keeps (H2) as a
  hypothesis; H10 (l. 60-61): «CONJECTURE (OPEN, REFEREE-2's): ODD-FREEZE holds without (H2). Not needed for any signature». REFEREE §C l. 43
  «clarification (data); (H2) stays, it is used», l. 80 «not claimed; no change»; REFEREE-2 §C.7 l. 124 «would be a WIDENING; correctly
  labelled OPEN and unsigned». No signed item drops (H2).
  (i) H9 (l. 56-59): «READING: (H1′) ⇔ there is a simple path from e to o in G_τ (Odd vertices other than o follow τ; Even vertices free)»,
  both directions proved there; REFEREE §C l. 79 «READING, an equivalent reformulation, not a widening»; REFEREE-2 §C.7 l. 123 «neither a
  widening nor a narrowing» (its OFBF brute force over all positional σ_e agrees with the path test for n ≤ 7-8, l. 95). The title states (H1′)
  in the packet's form.
  (ii) H12 (l. 64-66): «READING: the proof of §3.5 gives |S| ≤ Q + (Q + 1)(n − 1)(R*_S + 1) + FL_S (FL_S counts W-flat transitions of all of S
  once). The stated bound multiplies FL_S by Q + 1 and is implied.» REFEREE §C l. 82 «READING (a true strengthening, §3; NOT part of the
  signed statement or the line, correctly)»; REFEREE-2 §C.7 l. 126 «I would sign it if offered (the proof gives it directly)» (SR1_sharp_fails
  0). Not in either verdict table; the entry keeps the stated form.
  (iii) H14 (l. 68-69): «READING: at every transition where σ(y) changes, Ξ_{t+1}(σ_{t+1} y) ▷ Ξ_t(σ_t y) strictly.» REFEREE-2 N-FR-8 (l.
  277); REFEREE §C l. 84 «READING (a true strengthening; not signed separately, correctly)»; REFEREE-2 §C.7 l. 128 «unsigned». REFEREE-2's
  verdict cell for SUCC-MON is «SIGNED» only (l. 31); REFEREE §C's table (l. 15) summarises it with «(strict at every σ(y)-change, N-FR-8)».
  (iv) One referee each: REFEREE §5 l. 86, «SUCC-MON ✓ (= R86 SW-RETURN's Ξ-SUCC, signed)»; REFEREE-2 §5 l. 227-228, «τ̄(τ) is SPEC S1's
  (Odd's side), not R86's; harmless, since SPEC S1-S5 is cited first», and l. 254-255, «"(hence Even's PCH)" points at the Consequence,
  which the line does not state; harmless».
- Honest limits: (i) A REDUCTION. STRETCH-RED bounds one τ-stretch through R*_S, FL_S and ρ_S (fb_S and Q through ρ_S), none bounded here;
  the Consequence reduces R*_S further to Even's path-set changes PCH_R(z) on λ-runs (R86's P*), not bounded here. COMPOSE-FREEZE bounds the
  τ-changing transitions through PCH^U_R(e), and with (e) through the carries NM^U_R(e), of the targets of unprotected Odd edges only, not
  bounded here (RESULTS R86: NM*, NM*^U OPEN). Packet l. 5: «REDUCTION only. Nothing here bounds N5's iteration count; G-N5-TIME stays OPEN.»
  REFEREE-2 l. 19-20: «Nothing here bounds N5's iteration count: NM^U on unprotected targets, R*_S, FL_S and ρ_S are unbounded.» (ii) Per
  τ-stretch and per λ^U-run; the entry does not combine STRETCH-RED with COMPOSE-FREEZE into a bound on the run (that is packet §4's READING,
  not signed). DATA (not refereed as a claim): one τ-stretch can be long and all of it Q: FRAME-STRETCH (< n + m σ-changes per τ-stretch) is
  DEAD on L-NEW's mkr family (packet §4 l. 187-188: «mk_16_100: 1648 > 1225»), and there Q = |S| (REFEREE-2 l. 209: «one τ-stretch of 1,648
  σ-changes (mk_16_100, Q = |S|)»); «ρ = (2K − 1)² on mkr» (l. 188). (iii) [R86e]: COMPOSE-FREEZE (e) rests on RESULTS R86 (e)'s premise
  ([MΦ] on λ^U-runs, read with G^d's parities), which R86 displays in its headline (l. 5269) and body (e) (l. 5345-5357) as signed holding by
  both of R86's referees; both referees here accept it as that premise (REFEREE §3, REFEREE-2 §2.5 and N-FR-1); it is not re-proved here.
  (iv) Standing premises: ODD-FREEZE's τ̄ optimal at every vertex at once and realising U (H1, H8; R57 (b)'s premise and R57 (a) (VJ), on G^d);
  W-MON's [OPT-H] (1E-N3, form P2) inherited from RESULTS R88 (a); the code's match to SPEC is DATA (R15 G-N5T-1). (v) Counts are transitions,
  not bit operations; no running-time bound. (vi) Not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open.
- Data (DATA, not proof): pinned (packet §4 l. 189: «experiments/new/check.sh blocks "box 63", "box 64"»; at 938d8796 and trunk check.sh is
  identical, sha1 6f49f6ae792f80094115808ce3e8fa8231fc9291, 315 lines): "box 63" l. 291-296 (box59/freeze2.py on box59/out/dw_3.pg, asserts
  «^FREEZE2 dw_3.pg states 42 hyp-hits 81 viol 0 PASS$»; its failure branch prints «box 59 FC checks: FAILED», a label slip in the lane's
  file); "box 64" l. 297-302 (box64/frozen.py on dw_3 and box64/stretch.py on ../red/ctl/instances/d_runquad_K8_m30_n192.pg --start), l.
  303-308 (stretch.py on box64/mkr/mk_4_16.pg --start), l. 309-314 (frozen.py on dw_3 --wrun). Files at 938d8796: freeze2.py
  b71e8e9cfed0b480ec59cf318bb580bcb428a7c0, frozen.py 7c47dd619889bafac8fd2380c11d90c09cec7b31, stretch.py
  ddd2328ac8965f82a6f6b29c3672aa063c0cf0e5, dw_3.pg 67eb4bffcfd1e6cadfc53b4cd4a9ce7b59112c8a, mk_4_16.pg
  7284ca5f94e995b90c5397f36f9fce195a9c1b1b (.start b1174861…), d_runquad_K8_m30_n192.pg f9baf3f540f48611a0ee4edc5856c278f3eb63b4; all
  equal on trunk (`git diff --stat 938d8796 a60e5704 -- experiments/new experiments/red/ctl/instances` empty). Re-run for this draft from a
  `git archive` of 938d8796 (experiments/new, si, harness, red/ctl; `python3 -I` in experiments/new, outputs to scratch files, exit codes
  read): «FREEZE2 dw_3.pg states 42 hyp-hits 81 viol 0 PASS», rc 0; frozen.py dw_3 «… iters 41 tau-stretches 4 max-stretch-sig 26 its-phases
  4 its-causes {'fb': 0, 'sbar': 3, 'lx': 0, 'lw': 0} … FWR-viol 0», rc 0; stretch.py d_runquad_K8 «… iters 264 fb 0 #sig-1 0 #tau-1 264 …
  max-tau-per-sigma-stretch 264 …», rc 0; stretch.py mk_4_16 «STRETCH mk_4_16.pg n 102 m 151 n+m 253 iters 76 fb 0 #sig-1 76 #tau-1 0
  tau-stretches 1 …», rc 0; frozen.py dw_3 --wrun «… worst-frozen-phase {'len': 26, 'wch': 26, 'flat': 0, 'R': 4} FWR-viol 0», rc 0. Each
  of check.sh's five greps matches. The "81" is box 63's (H1) count (σ_e = τ̄), a subset of the (H1′)-protected edges: H17 (l. 80-82),
  REFEREE-2 verbatim: «freeze2.py counts box 63's (H1) (σ_e = τ̄) over all 42 states: 81; the packet's (H1′) gives 84 over all states (81
  on 0-40).» (REFEREE-2 §C.7 l. 136-141, own h1count.py; H16's «81 … cover states 0-40» was wrong.) Packet corpora (§4, lane DATA, 719
  games box59/sbcg.lst, S3 start, mkr and dual families): «ODD-FREEZE 35,780 hypothesis hits / 0 violations»; FW-R* on W-runs 0 violations;
  «late adoptions 1141, each with a Ξ-rise of z»; «in-stretch fallbacks 607, 603 lowering W». REFEREE (successor 18; own
  scratch/frame_probe.py, sha1 af5f7e99…, on rl_engine, no lane code; pinned l. 291-314 re-run alone from a clean worktree at 938d8796, exit
  0): pins (dw_3, mk_4_16 (+ start), ccl_w48_n48, rlin_cex_n40 (+ start)) 10 runs, 249 transitions, ODD-FREEZE hits / pairs 130 / 1,730,
  LATE-RISE 17,665, W-runs 153 (2 with a σ̄-change, 0 with a λ_Ξ-change), GP* path checks 23,409, τ-stretches 20 (max length 76; max fb_S
  33); library (n ≤ 40) 321, 5,798, 8,450 / 60,682, 378,188, 2,104 (222 / 10), 257,358, 821 (105; 24); random rand_ck n 5-14 6,000, 9,817,
  6,621 / 81,243, 5,154, 14,872, 33,542, 11,495 (6; 1); 0 violations; R*-RISE 644 edge checks, max R*_T 11; DUAL 0 violations in 110,975
  value pairs; controls: MUT 1 (no "above w") and MUT 3 (no "even") bite («454 + 175 / 586 + 374 violations of the Lemma / of ENT, random n
  5-12»), MUT 4 (no blocked condition) bites on GP*-RUN (ccl_w48_n48, 17), MUT 2 (no (H2)) does not bite. REFEREE-2 (successor 21; own
  R2-N5-FRAME/frame_check.py, sha1 7d9d928d2da88dfbc711500791d7da4997ac8649 (tools commit 1f066b8f, 21:25:12Z), on its lane's dual_check.Runner
  and matcher; the lane's scripts only run as the pinned check (whole experiments/new/check.sh in a detached worktree at 938d8796, exit 0,
  logs/pinned_check.txt), never imported): random n 3-8 6,000 runs / 6,712 transitions (ODD-FREEZE edges / protected hits / ENT checks
  37,216 / 3,423 / 1,472; OFBF on every edge, 0 mismatches); n 6-14 8,900 / 15,260 (129,422 / 9,894 / 5,434); n 15-30 900 / 2,501 (37,630 /
  3,065 / 2,101); alltau, every τ of 1,650 games n 3-11, 27,435 τ (238,570 / 5,782); box59/sbcg.lst 719 games (576 with counters, 143 in
  stopped chunks with counters lost and 0 VIOLATION lines; the remaining files re-run) 576 / 9,897 (260,674 / 30,033 / 27,439), GP* paths
  10,185,914 (7,612,664 in W-runs that are not frozen W-phases), late adoptions 991, max R*_T 17; mkr 11 / 2,191; dual family 21 / 881
  (max NM^U 163); every log RESULT PASS, 0 violations of FT2, FT3, FT4, DORD, UPLAY, OF, OF_play, OF_mid, OF_opt, OFBF, EF, CFa-CFe, SM, LR,
  WM, GPS, FWR, RR, RRsum, SR0-SR3, SRpc, FB56, CONS; control noH3e bites in every corpus, noH3r in every corpus except mkr (e.g. sbcg 3,871 / 2,167), GPall 790,359
  (sbcg), FW0 5 (sbcg), SR_Q0 11 (sbcg) and 3 (mkr: mk_6_24, mk_8_32, mk_16_100); X_OF_noH2 = 0 and SR1_sharp_fails = 0 in every log; max over sbcg PCH^U 13 and NM^U 10 on
  unprotected targets. Caps counted (l. 210-216): ODD-FREEZE's search stops at OFNODE nodes and an unfinished search counts as UNPROTECTED
  (OF_truncated_unknown 48,110 sbcg, 51,243 mkr); GP* enumeration PCAP 200, NODECAP 20,000, only on W-runs of ≤ GPMAX states
  (GPS_dfs_truncated 31,989 on sbcg); «FW-R*, R*-RISE, CONS and STRETCH-RED are exhaustive». Its own code reproduces dw_3's W-run [15, 41]
  (26 transitions, WCH 26, R*_T 4) and mk_4_16's τ-stretch of 76 (REFEREE too: §C l. 54). Q = 0 counter-check under H0's reading (REFEREE-2
  §C.7 l. 101-109, logs/mkr_H0_recheck.txt): mk_6_24 n 150, |S| = Q = 162, R*_S = FL_S = 0, H0's bound 24,449, Q's bound 22,350, old Q = 0 reading 149 ✗; mk_8_32 n 198, 280, 55,637, 39,006, 197 ✗ (§C.7's table uses n − 1 for these two games: 149, 24,286, 22,052, 148; 197, 55,356, 38,612, 196; CHECKER C99 §3); mk_16_100 n 498, 1,648, 821,201, 247,506, 497 ✗; «SR1/SR2/SR3 hold with 0
  violations in the re-run». No signed statement uses any count.
- Signatures: REFEREE docs/referee/R-N5-FRAME.md (report e9b32f727399aedb72a13782cc287d21dd0caa75, 2026-10-29T21:06:28Z, sha1
  90c2ca4db3f837bc5b922b5dcff870deb8b1b2eb, 152 lines, = trunk; successor 18); §C docs/referee/R-N5-FRAME-C.md (c908a865,
  2026-10-29T21:49:18Z, sha1 d1e73380e71ebccbc304edbce96e4c2056769d4b there, 63 lines; d869c05a, 21:58:30Z, stamp fix, the "Written" line
  «21:52Z» → «21:49Z» (1 added, 1 removed), sha1 8ec0f3884b00cbd8be1c8777651543d92579c8df, 63 lines; §4 addendum 0b080b2c,
  2026-10-29T22:08:37Z (`git diff --numstat d869c05a 0b080b2c`: 35 added, 3 removed: the old "## 4. Fixes file and H0" heading, its
  "PENDING" line and the old NEEDS line, replaced; no verdict line changed), sha1 9a00c9b2c6bb226be77f6ffa73f193d0cc33163a, 95 lines; H17 line d6aebf78, 2026-10-29T22:47:44Z, +3 lines, and stamp fix 4f3f75d0, 22:57:17Z, «22:48Z» → «22:47Z» (1 added, 1 removed): sha1 459d95876095fab3aa284fd2413d75e017ef66f8, 98 lines, = trunk = referee head 4f3f75d0): §1 CHECKED; FRAME-τ, DUAL-ORDER, ODD-FREEZE, ENT-FREEZE, COMPOSE-FREEZE (a)-(e), SUCC-MON, LATE-RISE, GP*-RUN,
  R*-RISE, STRETCH-RED and the Consequence SIGNED; «No gap. Nothing FALSE. Notes FR-N1..N6.» (l. 31). REFEREE-2
  docs/referee-2/R2-N5-FRAME.md (report a1142a46a41df7a81543c6746269c43b0db3cb7e, 2026-10-29T21:36:29Z, merged on claude/referee-2 as
  7571febeecc01348d35cae7166d72c4ea732c31e, 21:36:30Z, the SHA REFEREE, the Lead and REFEREE-2's §C cite; sha1
  4baf8c60c6493cd87bcd54b390744ad54a13f7c0 there, 292 lines; tools 1f066b8f, merged as 32cc81a0, 21:25:13Z; N-FR-10 (l. 279) replaced in place
  at 74871528e1cb60d05d5ca9ec358ac51a4cd1ba4c, 21:58:48Z (merged as b8aea44b), by a marked correction keeping the original after
  «Original:» (1 added, 1 removed; no verdict line changed), sha1 9250c727f5b173f5158401a5546d81d48e3159b7, 292 lines, = trunk; successor
  21); §C docs/referee-2/R2-N5-FRAME-C.md (1008d66e2d9d74364e749b03a2c4d14e422d009c, 21:49:01Z, merged as 4d61c074, sha1
  045805cfb2079581bf46ba2bc518b8adea855a42 there, 84 lines; §C.7 at 74871528, append-only (`git diff --numstat 1008d66e 74871528`: 67 added,
  0 removed), sha1 46198fe9f5bcf3052e300c25a238351df395427f, 151 lines, = trunk = referee-2 head b8aea44b): §1 well formed; all ten items and
  the Consequence SIGNED; line acf3234f MATCHES in content with Q and NM^U undefined (N-FR-7); «No gap. No item FALSE. Notes N-FR-1..N-FR-10
  (§6).» (l. 39). REFEREE-2 §C l. 3 says «pushed at 7571febe (21:44Z)»; its commit time is 21:36:30Z. REFEREE-2 l. 8 gives the line sha1 as
  «acf3234f84cb682d71444501e89cfd61247dcd6» (39 hex digits, a "0" missing after "acf3234f84"); REFEREE l. 4 and this draft measure
  acf3234f840cb682d71444501e89cfd61247dcd6. INDEPENDENCE: REFEREE l. 7: «Independence: no REFEREE-2 FRAME file opened.»; REFEREE §C l. 3-4:
  REFEREE-2's report «read only after the Lead's word (my report pushed first). Independence clean on both sides; no shared code».
  REFEREE-2 l. 13-14: FRAME name count under docs/referee/ on origin/claude/referee «0 at 20:58Z (handover), 16 at 21:21Z and 21:36Z (after a
  fresh fetch; names only, no file opened, no `git log` on origin/claude/referee)»; REFEREE-2 §C l. 4: REFEREE's report «opened only after the
  word». No review imported lane code.
  §C (both): verdicts identical (REFEREE §C l. 21: «VERDICTS IDENTICAL on every packet item; no gap; nothing FALSE in the packet. JOINT GAP
  MAP (packet): EMPTY.»; REFEREE-2 §C l. 26, bold in the source: «Joint gap map: EMPTY.» «No item is NOT SIGNED by either referee, and neither
  referee lists a gap.»). E-items, on the RESULTS line only: E1 (Q undefined; REFEREE-2's, REFEREE agreed and withdrew its MATCHES) and E2 (NM^U_R(e)'s
  definition; both), discharged by H0 (REFEREE §C §4 l. 66; REFEREE-2 §C.7 l. 98, l. 149). Fixes: REFEREE §C l. 87-89: «No H-item widens a
  signed statement. H12 and H14 are strengthenings recorded as READINGs (both true); H9 is an equivalence.»; the fixes file's header claim
  «is CONFIRMED»; «Nothing open on P-N5-FRAME.» REFEREE-2 §C.7 l. 148-151: «The fixes file is accepted.»; «H1-H15 are clarifications,
  readings or sharpenings, as labelled. None widens a signed statement; H10 is a conjecture, correctly unsigned.»; «H16 needs one correction
  (append), which comes from my own N-FR-10 error.» (applied as H17). REFEREE §C H17 line (d6aebf78, 2026-10-29T22:47:44Z; stamp fix 4f3f75d0, 22:57:17Z): «DATA only, no statement or pinned check touched (CHECKER 15's h1count re-run agrees, per the Lead). I did not re-count dw_3 myself. ACCEPTED.»; H17 is DATA only.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas on N5's Odd side and inside a fixed-τ stretch, and two
  REDUCTIONS: of a τ-stretch's length to R*_S, FL_S and ρ_S, and of the τ-changing transitions to PCH^U / NM^U on unprotected targets, none
  of which is bounded; no bound on a run, no running-time bound, no algorithm claim). GAPS G-N5-TIME: open.

Proposed GAPS line-11 UPDATE (append-only), after the R88 UPDATE of G-N5-TIME (GAPS l. 11), built only from the title clauses (landing time
and CHECKER addendum to be filled at landing; no "|"): «UPDATE 2026-10-29 <HH:MM>Z: RESULTS R89 (P-N5-FRAME; CHECKER C99 Add. <k>)
[refereed-only] LANDED: on every game (W_t the valuation of the (σ_t, τ_t)-plays, λ_W its cycle-node map; a τ-stretch a maximal run of
consecutive states with τ constant; a W-run a maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or
changes λ_W; U, τ̄(τ), λ^U-runs, ENT, PCH as in RESULTS R86, late adoptions as in RESULTS R88), in S4a's arena every Odd v keeps only τ(v),
τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o), no τ repeats in a run, and Iτ_t depends on τ_t alone (Lemma FRAME-τ); for Odd o and e ∈ succ(o), e ≠ τ(o),
if some positional Even σ_e equal to τ̄(τ) at every Even vertex outside P_e makes the (τ, σ_e)-play from e reach o before repeating a vertex
(P_e that play up to and including its first visit of o), the (τ, τ̄(τ))-play from τ(o) has no vertex in P_e, and the most relevant vertex of
P_e has even priority and is more relevant than the cycle node of the (τ, τ̄(τ))-play from τ(o) ((o, e) protected), then (o, e) ∉ Iτ and
τ_{t+1}(o) ≠ e (Lemmas ODD-FREEZE, ENT-FREEZE); on every λ^U-run R, ENT_R(o, e) = 0 unless (o, e) is unprotected at some state t of R with t +
1 ∈ R and τ_t(o) ≠ e, and otherwise ENT_R(o, e) ≤ n(PCH^U_R(e) + 1), so a run has at most n(n − 1) + (n(n − 1) + 1)·max_R Σ_{(o, e)
unprotected in R} n(PCH^U_R(e) + 1) τ-changing transitions, with PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e) (NM^U_R(e) the carries of
U(e) in R, read with G^d's parities) by RESULTS R85 (c)'s per-vertex MATCH-Φ on λ^U-runs, the premise RESULTS R86 (e) signs as holding
(Corollary COMPOSE-FREEZE); Ξ_t(σ_t(y)) is non-decreasing in t for every Even y, and (y, z) ∉ Iσ_t, (y, z) ∈ Iσ_u, t < u imply Ξ_u(z) ▷
Ξ_t(z) (Lemmas SUCC-MON, LATE-RISE); RESULTS R88's GP* and FW-R* hold on every W-run, σ̄ and λ_Ξ need not be constant there (Lemma GP*-RUN),
and in a W-run F the late adoptions of each Even edge (y, z) are at most the transitions of F at which Ξ(z) changes (Corollary R*-RISE); every
τ-stretch S has at most Q + (Q + 1)((n − 1)(R*_S + 1) + FL_S) transitions, Q the transitions of S that are an S4c fallback or change λ_W, Q ≤
fb_S + n(n − 1)(fb_S + 1), fb_S ≤ n(n − 1) + (n(n − 1) + 1)(1 + (n − 1)(2 + ρ_S)), fb_S its S4c fallbacks, R*_S the largest R*_T of one of
its W-runs, FL_S its transitions with σ_{t+1} ≠ σ_t and W_{t+1} = W_t, ρ_S the largest RESULTS R56 ρ of a phase meeting S (Theorem
STRETCH-RED): a REDUCTION; NM^U on unprotected targets, R*_S (hence Even's PCH), FL_S and ρ_S are not bounded here. G-N5-TIME stays open.»
