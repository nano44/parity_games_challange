# Box 93: the two open rows of WAIT-CLOSED, K7 (non-PRIV gate) and K6 (lagging merged copy) (L-SI successor 49; Lead «go» 03:36Z 2026-11-09)
Written 2026-11-09 (date -u in the commit). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD /
READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). No counterexample candidate.
Setting: box 92 (docs/si/box92-closed.md: GATE-LOW-NULL, CONJECTURE WAIT-CLOSED, table K1-K9), box 91 (GATE-RACE, TRIGGER), box 86 (LAG
TOWER, SAME-E-MERGE, ACCESS-LATCH, LEAPFROG). New input: L-NEW 67 BOX 202 (claude/l-new fa17fdf6, docs/new/N5-XIFVS-box202.md: K1-FLIP
DEAD on k1fail_202.json, CONJECTURE K1-FLIP(2) «flips(g) ≤ 2(lamch(g) + 1)» at Ξ-feedback number k = 1).
Premises: as box 91 / 92 (P-N5-CHAIN facts [OPT], F1, F2, F3, F6, CYC, LOC-GATE3, NO-TIE3, E-MON3, (E-DOM), (Core); Γ3's gate structure).
Tools: experiments/si/box93/ (np93.py on box 91's two engines; genk93.py K7 probe; run93.sh; k6/ (h = 4, 5 lag towers, run_k6.sh);
check93.sh, wired). Engines: own = L-RED R221 own.py (claude/l-red 4b309716); g3 = L-NEW's Γ3 N5′-xi from S3 (claude/l-new fcba92fc).

## 0. Answer
- K7 (non-PRIV gate): CLOSED as a waiting mechanism by two PROVED (lane) statements; NOT closed as a counter question, which it reduces to
  the core at the High's e-face continuation:
  - **Lemma NP-SHAPE** (§1): a non-PRIV state of gate o has Odd on the e-face p_e, and p_b's play = A · o · (p_e's play). So no flip has
    non-PRIV on both sides; a flip with non-PRIV before it is a RELOCK (p_e → p_b), one with non-PRIV after it is an UNLOCK (p_b → p_e).
    What replaces «e_o above Λ»: at a non-PRIV state the β-face's value is the e-face's value extended by the returning prefix A · o, so
    the β-face FOLLOWS the e-face; the trigger side costs nothing and limits nothing.
  - **Corollary E-FACE-PAYS** (§2; GATE-RACE (a), which never used PRIV): relocks(o) ≤ ch(p_e), unlocks(o) ≤ 1 + ch(p_e), and
    ch(p_e) = ch(D) for the e-face continuation D (W-target of e_o) whenever D's play does not pass e_o. So a High h_k, PRIV or not,
    UNLOCKS AT MOST 1 + ch(D_k) TIMES. A waiting High with a quiet continuation (ch(D_k) ≤ K) unlocks ≤ K + 1 times; a High that
    unlocks often has a continuation whose value changes often, i.e. the counter lives in D_k's play (letters entering it: c_y(D_k), the
    core itself), not in the waiting.
  - DATA (§3; both engines IDENTICAL on 15 instances): every must-be-0 counter 0. MW's race gate: 4n + 2 flips = 2n + 1 relocks, each paid
    by an e-set change of its e-face (ch(p_e) = ch(D) = 2n + 1, tight), and 2n + 1 UNLOCKS, ALL non-PRIV (the β-face follows). No relock
    on any instance is paid by a below-e-letter change of the e-face (relG 0).
  - Design side (§4): the obvious K7 design (move the High's continuation onto the race so that ch(D_k) grows) is DEAD: C = 2 at n = 4, 8,
    16 (Ku_n, Kprev_8; both engines). The continuation's richness makes Odd avoid the e-face.
- K1-FLIP(2) (BOX 202 asked): E-FACE-PAYS gives, on every genome (any k), flips(g) ≤ 2·min_f ch_f + 1 ≤ 2·lamch(g) + 2·min_f nl_f + 1,
  nl_f := the non-Λ value changes of face f. So K1-FLIP(2) holds at every gate with a face whose value changes only at Λ-changes, and a
  K1-FLIP(2) failure needs non-Λ changes on BOTH faces (DATA: k1both = k1c2 on every row). At k = 1 the open step is exactly a bound
  on min_f nl_f per gate (§2 (d)). This does not prove K1-FLIP(2).
- K6 (lagging merged copy) at h = 4 and 5: DEAD on DATA (§5): CNT 2 on all 4 + 4 towers, re-arms ≤ 1; the latch holds (ACCESS-LATCH,
  0 violations); SAME-E-MERGE and ACCESS-LATCH are height-free PROVED statements (box 86), so the h ≤ 3 obstruction is general wherever
  ACCESS-LATCH's hypothesis holds; the residue is LEAPFROG with shared e's (POOL-ALT's open case, box 86 §4), unchanged.
- WAIT-CLOSED (§6): restated with K7 and K6 rows updated. It is still a CONJECTURE for C; the per-gate part is a lemma.

## 1. Lemma NP-SHAPE (PROVED, lane; premises: Γ3's gate structure (SAME-E-MERGE's facts, box 86 §1), plays follow σ_t, σ̄_t)
Gate o with faces p_e (play starts at e_o: p_e = e_o, or the pad pe_o → e_o) and p_b. NP_t := e_o ∈ E_t(p_b).
(a) If NP_t then σ̄_t(o) = p_e, p_b's play at t is A_t · o · (p_e's play at t) for a path A_t from p_b to o, and E_t(p_e) ⊆ E_t(p_b).
(b) If o flips at t (σ̄_(t−1)(o) ≠ σ̄_t(o)) then not both NP_(t−1) and NP_t; NP_(t−1) implies the flip is a relock (p_e → p_b); NP_t
    implies it is an unlock (p_b → p_e).
Proof. (a) e_o's only in-edge comes from o's e-face side (from o, or from the pad whose only in-edge is from o), so a play passing e_o
passes o and leaves o by p_e: σ̄_t(o) = p_e. A play is a simple path then a cycle, and from o on it follows the same edges as p_e's play
at t; the part before o is A_t. With equal Λ, E_t(p_b) = E(A_t) ⊔ E_t(p_e) (an e-set is the set of e-vertices on the play more relevant
than Λ, [OPT], F3); with unequal Λ the play of p_b still contains p_e's play and Λ is the same cycle, so the same holds. (b) By (a), NP_s
forces σ̄_s(o) = p_e; a flip changes σ̄(o), so at most one of s = t − 1, t has NP, and on that side o plays p_e. ∎
- Reading (the «what replaces e_o above Λ» question): on a non-PRIV state Odd stays on p_e because Ω(p_b) = ext(A · o, Ω(p_e)) ▷ Ω(p_e)
  (LOC-GATE3, NO-TIE3: Odd plays the ◁-smaller face). The decision is made inside A · o and can be low (box 92 §2), but whatever A is,
  p_b's value is p_e's value plus a prefix. So an UNLOCK at a non-PRIV state is free for the β-side: once p_b's route returns through o
  with an Even-favoured prefix, p_b beats p_e by construction, at every value p_e has. GATE-LOW-NULL needs PRIV because there the two
  faces are independent; here they are not, and the binding face is p_e.

## 2. Corollary E-FACE-PAYS (PROVED, lane; GATE-RACE (a) of box 91 §3, premises F1, F2, LOC-GATE3, NO-TIE3; no PRIV hypothesis)
Over the whole run, let ch_f := #t with Ω_t(f) ≠ Ω_(t−1)(f).
(a) Every relock of o at t has Ω_t(p_e) ≠ Ω_(t−1)(p_e); every unlock has Ω_t(p_b) ≠ Ω_(t−1)(p_b). So relocks(o) ≤ ch(p_e) and
    unlocks(o) ≤ 1 + relocks(o) ≤ 1 + ch(p_e) (flips alternate). [GATE-RACE (a), verbatim; it uses only F1 and Odd's ◁-choice.]
(b) Let D := e_o's successor (e-vertices have one successor, F6). At every t at which D's play does not pass e_o, p_e's play is the fixed
    prefix (pad,) e_o followed by D's play, so Ω_t(p_e) = ext(prefix, Ω_t(D)) and ext by a fixed prefix is injective on values with the
    same Λ. Hence on any window where D's play avoids e_o, the value changes of p_e are exactly those of D: ch(p_e) = ch(D) there.
(c) Corollary for the waiting-High class: a High h_k at gate qh_k with W-target D_k unlocks at most 1 + ch(D_k) times over the run, PRIV
    or not (when D_k's play avoids e_(h_k); otherwise ch(p_e) in place of ch(D_k)). With CYC (Λ takes ≤ 2M + 3 values per vertex, only
    upward): ch(D_k) ≤ (2M + 2) + Σ_J #changes of E(D_k) in J + gam(D_k), and #changes of E(D_k) in J = Σ_y c_y(D_k, J) ≤ M·C. So
    unlocks(h_k) ≤ 1 + (2M + 2) + (2M + 3)·M·C + gam(D_k): a High that re-unlocks super-polynomially often needs C super-polynomial AT
    ITS OWN CONTINUATION (or super-polynomially many value changes of D_k below every e-letter, gam). The waiting cannot amplify a
    quiet continuation.
(d) For any gate g (any genome, any k): flips(g) ≤ 2·min(ch(p_e), ch(p_b)) + 1 (GATE-RACE (b)), and ch_f = lam_f + nl_f with lam_f ≤
    lamch(g) (lamch(g) := #t with Λ changed at p_e or p_b, BOX 202's counter). So flips(g) ≤ 2·lamch(g) + 2·min_f nl_f + 1. If some face
    has nl_f = 0, then flips(g) ≤ 2·lamch(g) + 1, i.e. K1-FLIP and K1-FLIP(2) hold at g. A gate violating K1-FLIP(2) has nl_f ≥ 1 on
    BOTH faces. ∎ (DATA: on k1fail_202.json the own / g3 max-flip gate has flips 2, lamch 0 and nl ≥ 1 on both faces.)
- What (c) does NOT give: a bound on C. The right side contains C (at D_k). It closes K7 as a NEW MECHANISM: whatever a non-PRIV trigger
  does, the number of unlocks is paid by the e-face continuation; the waiting-High class with continuation changes ≤ K is bounded by
  K + 1 unlocks per High (PROVED).
- Relock payment by kind (DATA, relL / relE / relG): on LAM ∧ PRIV relock steps a γ-only (below every e-letter) change of p_e cannot pay
  (PROVED, with e_o more relevant than Λ at t − 1 and t (GATE-LOW-NULL's premise): by GATE-LOW-NULL (a) Odd's choice there is a function of π(E(p_e)), π(E(p_b)); π(E(p_b)) does not fall (E-MON3: lex rise of
  E(p_b) inside a Λ-interval cannot lower its projection above e_o: the top of the difference is either at least as relevant as e_o, and then it is the top of the
  projections' difference, or below e_o, and then the projections are equal); so π(E(p_e)) must rise, and a γ-only change leaves it fixed). On non-PRIV-before relocks (NP-SHAPE (b))
  I have no proof; relG = 0 on every row.

## 3. DATA (np93.py; unit: gate o (Odd vertex with an e-face) over the whole run; set: box 91's 11 frozen instances + L-NEW's
## k1fail_202.json (sha1 99bba752, claude/l-new fa17fdf6) + the K7 probes Ku_8, Ku_16, Kprev_8 (inst/SHA1SUMS); scope: own to the end
## (cap 3000), g3 to the first fallback (cap 20000); TOTALS unless «mx_» (the max-flip gate's row); out/own93.out, out/g393.out)
Must-be-0 (TOTALS, both engines, all 15 rows): npside 0, npsub 0, npboth 0, npkind 0 (NP-SHAPE); relfail 0, unlfail 0 (E-FACE-PAYS (a));
dfail 0 (E-FACE-PAYS (b), proxy); k1both = k1c2 on every row (E-FACE-PAYS (d)).
| instance | N + M | gates | flips | np_rel | np_unl | k1c2 | relL / relE / relG | mx: flips, ch_pe, ch_pb, ch_D | mx: lam / ech / gam of p_e |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ROWS93
- Both engines give IDENTICAL rows on every column (own93.out, g393.out).
- Controls (own; out/ctrl93.out): CTRL=swap (faces exchanged in relfail) relfail 4 on C6G8_n54 (0 on MW8_2: there the β-face changes more);
  CTRL=tight (bound lowered by 1) relfail 176 / 92, unlfail 8 / 5 on MW8_2 / C6G8_n54 (it also counts every gate with 0 relocks).
- READING:
  - MW's race gate (MW8_2: 34 flips; MW32_2: 130): relocks 17 / 65 = ch(p_e) = ch(D) (D = the race mover u), every one paid by an e-set
    change of u's play (relE); unlocks 17 / 65, all non-PRIV (np_unl). The β-face follows; u pays. Its 2n + 1 changes are the n High
    entries and the race letters, each once per High (box 91: a_(h_k) = 1). That is the linear unary count.
  - The k > 2 climbed genomes have K1-FLIP(2) failures (k1c2 up to 22 on DHIB26_2804); BOX 202's conjecture is only for k = 1; on
    k1fail_202 (k = 1) k1c2 = 0 on both engines.

## 4. K7 design probe (DEAD; genk93.py = genm90.py with the Highs' W-target moved: WT=u (the race mover) or WT=prev (qh_(k−1)'s mover))
- Idea: by E-FACE-PAYS a re-unlocking High needs its continuation D_k to change often; MW's race mover u changes 2n + 1 times. So point
  the High's e-face at u (or at the previous High) and let the non-PRIV β-route follow.
- DATA (mult91 C / T3, both engines; unit (v, I, y) for C, per-tuple maximum): C = 2 at n = 4, 8, 16 for WT=u (T3 28 / 52 / 100) and at
  n = 8 for WT=prev (T3 52); max gate flips 4 (np93). WT=D reproduces MW8_2 byte for byte (cmp).
- Why (READING): with e_(h_k) → u, the e-face's play carries the race's best letters, so Ω(p_e) is large and Odd (who plays the ◁-smaller
  face) stays on the β-face; the High never waits for anything. A continuation rich enough to change often is also rich enough to be
  avoided. Frozen: inst/Ku_4, Ku_8, Ku_16, Kprev_8.

## 5. K6 at h = 4, 5 (lag86.py cfg extended; k6/cfg L = [1, 3, 6, 10] (h = 4), [1, 3, 6, 10, 15] (h = 5); a 2, b 2, c 1, merge 1,
## cexit C; cpos ±1, wreal 0/1; measured with box 84-86's tools on box 81's IDEAL-CYC reference; k6/out)
| instance | cfg (h; cpos; wreal) | T | R | tog (B1..Bh) | CNT (of 2^h) | REARM | premature | hubH | OFF / on real / latch-viol. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ROWSK6
- Lemma checks (k6/out; TOTALS over the 8 towers): FLIP-U / FLIP (flipu85) EXCU, LOWER-BLIND keep (lb84) EXCLB, PRIV-FLIP (priv84)
  EXCPF, POOL-ALT (pool85) EXCPA, ACCESS-LATCH at OFF steps (latch86) EXCAL.
- Second engine (mult91 own / g3 on the same genomes; C per (v, I, y), T3): TWOENG
- DEAD at h = 4, 5 (DATA): the count does not grow with h (CNT 2 at h = 2..5); with wreal = 1 bit 1 latches as at h ≤ 3.
- General part (PROVED, box 86, no height in the statements): SAME-E-MERGE (a merged copy shares the real chain's e's from the merge
  mover on) and ACCESS-LATCH (a merged waiting hub keeps its SET option while no other option is lex-above w). So at every h a merged
  lagging copy latches unless another option of B_l overtakes w strictly (LEAPFROG). That residue is box 86 §4's open case (leapfrogs
  decided by shared e's in different positions over time); h = 4, 5 do not exhibit it.

## 6. WAIT-CLOSED after box 93
| class | box 92 status | box 93 |
| --- | --- | --- |
| K6 lagging merged copy | DEAD h = 2, 3 (DATA); open h ≥ 4 | DEAD h = 2..5 (DATA); latch PROVED at every h under ACCESS-LATCH's hypothesis; residue = LEAPFROG with shared e's (open) |
| K7 non-PRIV gate | DATA only | NP-SHAPE + E-FACE-PAYS PROVED: unlocks(h_k) ≤ 1 + ch(D_k) PRIV-free; the trigger side is free and irrelevant; open part = ch(D_k) itself (the core at the continuation) |
- **Lemma WAIT-QUIET (PROVED, lane; = E-FACE-PAYS (c))**: in any genome, a High at gate qh_k whose e-face continuation D_k changes value at
  most K times while its play avoids e_(h_k) unlocks at most K + 1 times and flips at most 2K + 1 times, whatever its trigger (PRIV,
  non-PRIV, Λ-keyed, length-only, copy). This is the per-gate form of WAIT-CLOSED for the class «waiting Highs with quiet continuations».
- CONJECTURE WAIT-CLOSED (C-level) stays a CONJECTURE: bounding C needs more than gate flips (letters re-enter plays by route changes
  too), and the class «continuation changes often» is the core itself (c_y at D_k), not a waiting design. No family with C super-linear
  in N + M was found; nothing to freeze as a counterexample candidate.
