# Box 91: expulsions at SPLIT-COUNT's route vertices; gate races; the waiting-High trigger (L-SI successor 48; Lead «go» 23:10Z 2026-11-08)
Written 2026-11-08/09 (date -u in the commit). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD /
READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). No counterexample candidate.
Setting: L-NEW 66 box 199 (claude/l-new 91ed2f3f, docs/new/N5-SPLIT-box199.md Add. 2): (v, I), tops, split pairs (u, b), J_b, U_y,
H_s := E_s(b) ∩ U_y on J_b, Dhi_y(b, J_b) = #distinct H_s; SPLIT-COUNT c_y(v, I) ≤ Σ_(u,b) Dhi_y(b, J_b). L-RED 62 R228 Add. A-C (claude/l-red
4b309716). Box 90 §7 (Lemma SUPERSET, WC).
Premises used (all as box 199 states them): P-N5-CHAIN (frozen l-new 93531b03; landing as R125, pending) §2 [OPT], (E-DOM), (Core); §4 F1,
F2, F3, F4′, F5, F6, STRICT; §5 CN2-3, LOC-GATE3, NO-TIE3; §7 E-MON3; box 199's Lemma SPLIT (TRANSFER). No [E-LEV], no landed R-id beyond those.
Tools: experiments/si/box91/ (mult91.py census, run91.sh, check91.sh wired; pins.txt; inst/ + SHA1SUMS; out/own91.out, g391.out, ctrl91.out).
Engines (two on every number): own = L-RED R221 own.py (IDEAL-CYC Howard, pad-free Γ, the genome's start; claude/l-red 4b309716);
g3 = L-NEW's padded Γ3 N5′-xi run from S3 (gamma3 / n5v / n5x / eg195, claude/l-new fcba92fc = box 90's pin). mult91.py is my code
on both (no L-NEW / L-RED census code).

## 0. Answer
- PART 1 (proof side). Three PROVED (lane) statements, all elementary, all with 0 failures on two engines (§1-§3):
  - Lemma PARALLEL (the general form of SUPERSET): at any change of b's high part H inside J_b, every EXPELLED letter z lies on b's OLD play
    strictly after b's split u′ and not on the new play, and the top x (x ≻ z) lies on the NEW play after u′ and not on the old one. So a
    letter is lost only to a strictly higher letter that enters on a parallel divergent segment.
  - Lemma PAIR-EXPEL (the expulsion twin of PAIR-SPLIT): two expulsions of the same z at (b, J) through the same split pair (u′, b′) of b's
    plays have E(b′) ∩ U_z strictly lex-larger at the later one. Corollary EXPEL-COUNT: a_z(b, J) ≤ 1 + Σ_(u′,b′) Dhi_z(b′, J_b′), where
    a_z := the number of maximal presence runs of z in H on J.
  - Lemma GATE-RACE: an Odd gate whose two faces p, q have ch_p, ch_q value changes flips at most 2·min(ch_p, ch_q) + 1 times, and every
    flip is paid by a change of the face Odd LEAVES. Corollary TRIGGER: that change is a Λ-change (at most n − 1 per face over the whole run,
    F2) or the entry of a letter onto that face's play.
- WHAT IT GIVES (exactly): NOTHING polynomial by itself. With PARALLEL and E-MON3, Dhi_y(b, J) ≤ 1 + Σ_z a_z ≤ 1 + L·A*, L ≤ M letters,
  A* := max a_z(b, J). So (Corollary A*-EQUIV, PROVED given C-EQUIV and SPLIT-COUNT) C ≤ 3M·(1 + M·A*), and C ≤ A* (take b = v):
  T3 polynomial ⟺ C polynomial ⟺ A* polynomial. A* is the cleanest form of the open core I have: how often ONE letter can leave and
  re-enter ONE vertex's play inside one Λ-interval. EXPEL-COUNT bounds A* by the recursion A*(z) ≤ 1 + 3M·D(z), D(z) := max Dhi_z, which
  unrolls to (1 + 3M)^O(M): exponential, the same shape as PAIR-HIGH / SPLIT-COUNT. Where it differs from L-NEW 67's TIME charge (BOX 200,
  Dhi_y(b) = 1 + Σ_(z ≻ y) c_z(b)): it counts PRESENCES and EXPULSIONS (a_z ≥ c_z), charges each expulsion to its split pair, and adds the
  geometric fact (PARALLEL) that expeller and expelled sit on parallel segments; it does not use time.
- DATA (§4; two engines; identical on every row and counter): A* ≤ 6 on the climb bests and RWX / C6G8 (DHIB26_2804: Dhib 26 from A* 6
  over many letters), A* = n + 1 on MW(n) (linear), A* 0-1 on FW / WC. The expulsion DAG is DEEP on MW (depth n, the chain h_1 ← h_2 ← …),
  so path-count bounds (Corollary EXP-PATHS, §1) are loose; the per-pair expulsion multiplicity is ≤ 3.
- PART 2 (design side, box 90 §7 (5)). The second half is NOT an obstruction: by PARALLEL an Even route to h_k that avoids h_(k−1) wins as
  soon as h_k ITSELF sits on the divergent segment (h_k ≻ h_(k−1)); MW realizes it (expulsion chain of depth n). Box 90 §7's reading
  («needs a letter above h_(k−1) that the old route lacks … PAIR-HIGH's recursion again») is corrected: h_k is that letter. The first half
  IS the obstruction, as a lemma (§5, Corollary WAIT-TRIGGER, PROVED (lane) for the design class of §5): an unlock of h_k is a flip of
  qh_k's gate paid by its β-face (GATE-RACE), and that payment is a Λ-change of the β-face (≤ n − 1 over the run, no replay) or the entry of
  a letter on the β-face's play. The low race's state at u reaches the β-face's value only through letters on the β-face's play; so a
  trigger keyed to «u's lane is at h_(k−1)» puts h_(k−1) on the β-face's play, i.e. it is ON a route carrying h_(k−1). No working waiting
  High built; C, T3 linear on every family here. No instance to send.

## 1. Lemma PARALLEL (PROVED, lane; premises [OPT], F3, E-MON3, Lemma SPLIT (i) at b)
Let s − 1, s ∈ J (a Λ-interval of b, Λ = w), H_(s−1) ≠ H_s, x := the top (most relevant e-vertex of H_(s−1) Δ H_s), Z := H_(s−1) \ H_s.
P_r := b's play at r (simple path then one cycle), u′ := the first vertex of P_s whose successor differs at s − 1 (b's split).
(i) x ∈ P_s \ P_(s−1); every z ∈ Z lies in P_(s−1) \ P_s. (ii) z ≺ x for every z ∈ Z. (iii) every z ∈ Z lies strictly after u′ on P_(s−1);
x lies strictly after u′ on P_s.
Proof. E_r(b) is the set of e-vertices of P_r more relevant than w ([OPT], F3), and y ≻ w for the letters of U_y here (y is a top of a
Λ-interval with Λ = w). E-MON3: H is lex-nondecreasing on J, so the top enters: x ∈ H_s \ H_(s−1); being an e-vertex above w, x is on P_s
and not on P_(s−1); likewise z ∈ H_(s−1) \ H_s is on P_(s−1) and not on P_s. (ii): x is the most relevant element of the difference. (iii):
P_(s−1) and P_s agree up to u′ (definition of the split, positional strategies), so a vertex of that common prefix is on both plays. ∎
- SUPERSET (box 90 §7) is the special case where both plays share the suffix from qh_k: then neither h_k nor anything after it can be the
  expeller of h_(k−1); the expeller must enter on the divergent part, and in WC nothing above h_(k−1) does.
- Corollary EXP-PATHS (PROVED). X(z) := the letters that expel z in J. a_z ≤ 1 + #expulsions of z (each run but the last ends with one),
  each expulsion of z is an entry of some x ∈ X(z), and an entry expels z at most once: a_z ≤ 1 + Σ_(x ∈ X(z)) a_x. Every change of H is
  an entry of its top: Dhi_y(b, J) − 1 ≤ Σ_z a_z. Hence Dhi_y(b, J) ≤ 1 + Σ_z P_X(z), P_X(z) := 1 + Σ_(x ∈ X(z)) P_X(x) (paths in the
  expulsion DAG). Exponential in the DAG's depth; tight for a binary counter, loose on MW (§4).
- DATA (mult91.py; unit: one change of H with Z ≠ ∅ for par1-3; tuple (b, J, y) for afail, pxfail, dhifail; set: the 11 frozen instances of
  §4; scope: own engine to the end of the run, cap 3000; g3 to the first fallback, cap 20000): par1 = par2 = par3 = lexfail = afail =
  pxfail = dhifail = 0 (TOTALS) on both engines. Controls on MW8_2 / C6G8_n54 (own): CTRL=pre (par3 counted on the whole old play) par3
  58 / 80; CTRL=a0 (the 1 dropped from afail's bound) afail 14 / 96. seg2 (DATA only: expelled letters not all on the FIRST divergent
  segment of the old play, multi-switch steps): 0-20, so «first segment» would be false as a lemma (DWT20_2803: 20).

## 2. Lemma PAIR-EXPEL and Corollary EXPEL-COUNT (PROVED, lane; premises as §1 plus F1, F2, F4′, STRICT, CN2-3, LOC-GATE3, NO-TIE3, (E-DOM), (Core))
Let s < s′ in J be two expulsions of the same z at b (z ∈ H_(r−1) \ H_r for r = s, s′) whose splits (§1) are the same pair (u′, b′):
u′ is b's split at both, and b′ its new successor at both. Let a′ := u′'s successor at s′ − 1 (a′ ≠ b′). Then E_s′(b′) ∩ U_z >lex E_s(b′) ∩ U_z.
Proof.
- Λ: b′ lies on b's play at s and at s′ (after u′), so Λ_s(b′) = Λ_s′(b′) = w, and Λ(b′) = w on [s, s′] (F1, F2: Λ monotone, distinct cycle
  rewards). The same holds for u′ and for a′ at s′ − 1 (on b's old play at s′).
- Step 1: Ω_(s′−1)(a′) ▷ Ω_s(b′). Mover u′: σ_s(u′) = b′ ≠ σ_(s′−1)(u′) = a′, so u′ leaves b′ at a first s″ ∈ (s, s′ − 1]; then, verbatim
  box 199 §2 (a) (F1, STRICT, F4′, CN2-3): Ω_(s′−1)(u′) ⊵ Ω_s″(u′) ▷ ext(u′, Ω_(s″−1)(b′)) ⊵ ext(u′, Ω_s(b′)), and F4′ gives the claim.
  Gate u′: its successors are its two faces, a′ is the other face; at s Odd plays b′, so Ω_s(b′) ◁ Ω_s(a′) (LOC-GATE3, NO-TIE3); F1 on a′.
- Step 2: E_(s′−1)(a′) ∩ U_z ⊵lex E_s(b′) ∩ U_z. Both values have Λ = w, so [VJ] compares their plays by the most relevant vertex d of the
  symmetric difference. If d ≻ z, d is an e-vertex (E-DOM; c_W is in no play's set, K0 / K3 lie on both or neither by (Core)), even, so
  d ∈ E_(s′−1)(a′): strict lex on U_z. If d ≼ z, the two sets agree on U_z.
- Step 3: E_s′(b′) ∩ U_z >lex E_(s′−1)(a′) ∩ U_z. b's plays at s′ − 1 and s′ agree up to u′; u′ is not an e-vertex (e-vertices have one
  successor, F6), so E_(s′−1)(b) = A ⊔ E_(s′−1)(a′) and E_s′(b) = A ⊔ E_s′(b′) with the same A. The change of E(b) at s′ has top x′ ≻ z
  (§1 (ii)), x′ ∈ E_s′(b), and the two sets agree above x′. So on U_z the top of the difference is x′, on b′'s side.
- Steps 2 and 3 and transitivity of lex order on subsets of U_z give the claim. ∎
- Corollary EXPEL-COUNT (PROVED). For each pair (u′, b′) the values E(b′) ∩ U_z at z's expulsions through it are pairwise distinct and lie in
  one Λ-interval J_b′ of b′ (above). So #expulsions of z through (u′, b′) ≤ Dhi_z(b′, J_b′), and a_z(b, J) ≤ 1 + Σ_(u′,b′) Dhi_z(b′, J_b′)
  ≤ 1 + 3M·max Dhi_z (the pairs are edges out of movers and gates: ≤ 3M on standard states, R228 §2).
- Note: unlike PAIR-SPLIT, z itself is NOT on b′'s side at s (it was just expelled), so no «rise above z at b′» follows from z alone; the rise
  comes from the second expulsion's top x′ (Step 3). Step 2 is the only place where Odd's / Howard's choice at u′ is used.
- DATA (unit: couple s < s′ of same-pair expulsions; TOTALS): pefail 0 on 28 (MW8_2), 496 (MW32_2), 10 (C6G8_n54), 121 (DWT20_2803),
  103 (DHIB26_2804), 74 (DHIB18_2805) couples, both engines; ecfail 0 (unit (b, J, y, z)); pelam 0. Control CTRL=uz (U_z := ∅): pefail
  fires on every couple (28 / 28 on MW8_2). nexpl (max #expulsion split pairs of one z; maximum) ≤ 3 except MW(n): n.

## 3. Lemma GATE-RACE and Corollary TRIGGER (PROVED, lane; premises F1, F2, LOC-GATE3, NO-TIE3, E-MON3)
Let o be an Odd vertex with two successors p, q (a gate and its two faces), over any time window. Let ch_p := #t with Ω_t(p) ≠ Ω_(t−1)(p).
(a) A flip at t from p to q implies Ω_t(p) ≠ Ω_(t−1)(p): Ω_(t−1)(p) ◁ Ω_(t−1)(q) ⊴ Ω_t(q) ◁ Ω_t(p) (LOC-GATE3, NO-TIE3, F1).
(b) Flips alternate p→q, q→p; by (a) #(p→q) ≤ ch_p and #(q→p) ≤ ch_q; so #flips ≤ min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1). ∎
- Corollary TRIGGER (PROVED). In (a), the change of the left face p at t is (α) a change of Λ(p), at most n − 1 times over the whole run
  (F1, F2: Λ only rises and never returns), or (β) inside a Λ-interval of p, a change of E(p) whose top x enters E_t(p), i.e. x lies on p's
  play at t (E-MON3, [OPT]), or (γ) a change of p's value below every e-letter (play length / low vertices).
- Reading (order theory): o merges two monotone chains (the face values) and switches each time the merge alternates; a gate that flips f
  times needs ≈ f/2 rises on EACH face. A High that unlocks and re-locks k times therefore needs its FIXED W-continuation (e-face) to rise
  ≈ k times (the lock is paid by the e-face), not only its trigger.
- DATA (unit: Odd vertex with two successors, whole run; TOTALS): grfail = gr2fail = grwhy = trfail = 0, both engines. maxflip (maximum)
  = 4n + 2 on MW(n) (34 at n = 8, 130 at n = 32), ≤ 15 elsewhere. Kinds: fl_lam / fl_e / fl_len =
  8 / 34 / 0 (MW8_2), 32 / 130 / 0 (MW32_2), 8 / 0 / 0 (FW8_2: every FW letter arrives by a Λ-change, the clock), 16 / 0 / 0 (FW16_2),
  0 / 3 / 0 and 0 / 15 / 0 (WC4_2, WC16_2: one e-entry cascade). maxlamfl (max Λ-flips at one gate) ≤ 2. Control CTRL=gr (bound
  lowered by 1) fires (8 on MW8_2).

## 4. DATA table (mult91.py; both engines give IDENTICAL rows on every column; per-tuple MAXIMA unless said; out/own91.out, out/g391.out)
Units: C per (v, I, y); Dhib, maxa (= A* over route vertices b), Xdep (longest expulsion chain), Xfan (max |X(z)|), maxPX, mexp (max
expulsions of one z by one x), nexp (max expulsions at one tuple) per tuple (b, J, y); sumD per (v, I, y); seg2, tuples are TOTALS.
Scope: own to the end (cap 3000), g3 to the first fallback (cap 20000). Every must-be-0 counter of §1-§3 is 0 on every row.
| instance (sha1, inst/SHA1SUMS) | N + M | T3 | C | Dhib | sumD | maxa | Xdep | Xfan | maxPX | mexp | nexp | maxflip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WC4_2 (e7569f92) | 60 | 4 | 1 | 2 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| WC16_2 (995e7132) | 216 | 4 | 1 | 2 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| FW8_2 (108a63cf) | 371 | 29 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| FW16_2 (94df42b7) | 787 | 53 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| MW8_2 (66b84dcb) | 261 | 55 | 17 | 18 | 18 | 9 | 8 | 8 | 37 | 1 | 15 | 34 |
| MW32_2 (445031d1) | 957 | 199 | 65 | 66 | 66 | 33 | 32 | 32 | 529 | 1 | 63 | 130 |
| C6G8_n54 (52067442) | 204 | 17 | 6 | 8 | 16 | 3 | 2 | 2 | 4 | 2 | 6 | 11 |
| RWX_n95 (da8b3a30) | 328 | 12 | 2 | 7 | 8 | 2 | 3 | 1 | 4 | 1 | 5 | 3 |
| DWT20_2803 (ca731061) | 364 | 22 | 3 | 20 | 21 | 2 | 9 | 2 | 12 | 2 | 18 | 6 |
| DHIB26_2804 (2c49fd10) | 400 | 28 | 4 | 26 | 45 | 6 | 9 | 4 | 32 | 3 | 31 | 15 |
| DHIB18_2805 (9e8c2e3c) | 400 | 19 | 4 | 18 | 30 | 5 | 7 | 3 | 21 | 2 | 19 | 10 |
- Cross-check: Dhib / sumD equal L-RED R228's on DHIB26_2804 (26 / 45), DHIB18_2805 (18 / 30) and MW8_2 (18 / 18), from my code.
- Frozen copies: RWX_n95, C6G8_n54, DWT20_2803 from claude/l-red 4b309716 experiments/red/r228/inst (= its SHA1SUMS); DHIB26_2804,
  DHIB18_2805 the same (Addendum C bests); MW / FW / WC from claude/l-si experiments/si/box90/inst (= its SHA1SUMS).
- READING:
  - On the climb bests Dhib is large because MANY letters each enter a few times (maxa ≤ 6): the «L·A*» regime, polynomial by itself.
    A super-polynomial Dhi needs A* super-polynomial, i.e. one letter replaying at one vertex.
  - MW is the only family where A* grows (= n + 1, the race letter z under each h_k), and there the expulsion DAG is a chain of depth n with
    mexp 1: each h_k expels h_(k−1) once and h_(k−1) never comes back (a_(h_k) = 1). That is a unary counter: the High letters do not replay.
  - A binary counter at one vertex needs a_(h_(k−1)) ≥ 2 under h_k, i.e. by EXPEL-COUNT a rise of E(b′) above h_(k−1) between two
    expulsions through one pair: a higher letter entering at b′. Nothing here does that (mexp ≤ 3, nexpl ≤ 3 off MW).

## 5. Part 2: the waiting-High trigger (box 90 §7 (5)) — obstruction (PROVED for the design class; READING beyond)
Design class (box 90 §7): high letters h_1 ≺ … ≺ h_n at gates qh_k with fixed W-targets D_k; a low race at a mover u (lane options into the
qh_j); h_k should UNLOCK (Odd at qh_k forced from the β-face to the e-face) only when the race at u has reached h_(k−1), and the unlock must
not lie on any route carrying h_(k−1). Then:
- Corollary WAIT-TRIGGER (PROVED, from GATE-RACE (a) and TRIGGER). The unlock of h_k at t is paid by a change at t of the β-face pβ_k: (α)
  a Λ-change, at most n − 1 for pβ_k over the whole run and never undone, so a Λ-keyed High unlocks, and re-unlocks, at most n − 1 times;
  or (β) the entry at t of a letter x onto pβ_k's play; or (γ) a change below all e-letters. In case (β), let u″ be the split of pβ_k's change at t (Lemma SPLIT at pβ_k). If
  u″ = u and u's change is the race «reaching h_(k−1)» (u switches to its lane into qh_(k−1), top h_(k−1)), then by TRANSFER (box 199 §1 (iv))
  pβ_k's change has the same symmetric difference: h_(k−1) enters pβ_k's play, so pβ_k's play carries h_(k−1) at t. ∎
- Consequence for the design: the trigger «u's lane is at h_(k−1)» puts h_(k−1) on the β-route of qh_k, i.e. the trigger IS on a route
  carrying h_(k−1) — the case box 90 §7 excludes. The alternatives are (α) (Λ-keyed: the clock designs FW / MW, which unlock each gate
  once) and (β) with a letter x ≠ h_(k−1) whose entry onto pβ_k's play coincides with the race's arrival; by TRANSFER that x enters at a
  vertex of pβ_k's play that switches at t, i.e. a SECOND vertex reading the race (a copy), which is box 85's TWO COPIES (DEAD there as a
  counter) or a clock.
- The other half is fine (PARALLEL, §0): a route to h_k avoiding h_(k−1) wins once h_k is on the divergent segment; MW does it.
- What would still give a counter (READING, open, not built): a letter whose gate unlock is keyed (β) to a copy of the race that itself
  has a waiting High: the recursion of box 85 / 89, one level up. I did not find a finite design that closes it; no instance.
- Labels: WAIT-TRIGGER is PROVED for the design class (a gate unlock keyed to a change at u that reaches the β-face through u's own play);
  «no waiting High exists» in general is NOT claimed (a design keyed to a different vertex's value is not covered).

## 6. Where this differs from L-NEW 67 (BOX 200, TIME charge for Dhi_y(b) = 1 + Σ_(z ≻ y) c_z(b))
- L-NEW 67 charges the ENTRIES (tops) at b to time. Box 91 charges the EXPULSIONS to split pairs (PAIR-EXPEL) and isolates the replay count
  A* (presences of one letter at one vertex), with the parallel-segment geometry (PARALLEL) and the gate race (GATE-RACE). The two meet
  in Dhi_y(b) − 1 = Σ_(z ≻ y) c_z(b) ≤ Σ_z a_z(b): a bound on A* is a bound on every c_z(b), not conversely.

## Correction 1 (appended 2026-11-09, date -u in the commit; L-RED 62 R228-box91, claude/l-red f3903cb8, relayed by the Lead 00:25Z: box 91 SURVIVES; findings F1, F2)
Pushed text above is not rewritten; this correction governs where they differ.
- Verdict relayed: PARALLEL, PAIR-EXPEL, EXPEL-COUNT, GATE-RACE, TRIGGER, A*-EQUIV all SURVIVE on L-RED's own census (expel228.py, 19,436
  same-pair couples, 0 fails, control fires). I have not re-run L-RED's tool; its numbers are relayed as such.
- (F1) A* LABELLING. Corollary A*-EQUIV's A* is the maximum of a_z(b, J) over ALL vertices b, all Λ-intervals J of b and all letters z
  (needed for «C ≤ A*, take b = v»). The DATA column «maxa» of §4 and the counts quoted in §0, §4 («A* ≤ 6 off MW», «A* = n + 1 on MW(n)»,
  «A* 0-1 on FW / WC») are a different, smaller quantity: the maximum over the ROUTE vertices b (successors b of split pairs (u, b), at
  the tuples (b, J_b, y) that SPLIT-COUNT sums over), restricted to letters above y. Rename it A*_route. Restated DATA, with the
  corollary's quantity A*_all (experiments/si/box92/astar92.py; unit (v, I, z), per-tuple MAXIMUM over all vertices; both engines, see
  box 92 §5):
  | instance | C | A*_route (box 91 «maxa») | A*_all |
  | --- | --- | --- | --- |
  | WC4_2 / WC16_2 | 1 / 1 | 1 / 1 | 1 / 1 |
  | FW8_2 / FW16_2 | 3 / 3 | 0 / 0 | 8 / 16 |
  | MW8_2 / MW32_2 | 17 / 65 | 9 / 33 | 18 / 66 |
  | C6G8_n54 | 6 | 3 | 6 |
  | RWX_n95 | 2 | 2 | 2 |
  | DWT20_2803 | 3 | 2 | 5 |
  | DHIB26_2804 | 4 | 6 | 9 |
  | DHIB18_2805 | 4 | 5 | 6 |
  - So A*_all = 2n + 2 on MW(n) (= C + 1) and A*_all = d on FW(d, 2) with C = 3: A*_all can be large while C stays bounded, as A*-EQUIV
    allows (C ≤ A*_all, not conversely). cfail (a tuple with c_y > a_y; must be 0) = 0. Corrected statements: «A*_all ≤ 9 on the climb
    bests and RWX / C6G8», «A*_all = 2n + 2 on MW(n)», «A*_all = d on FW(d, 2)». The READING of §4 («Dhib large from many letters each
    entering a few times») holds with A*_route; the claim that MW is the only family where the count grows is FALSE for A*_all (FW grows).
  - The bound Dhi_y(b) ≤ 1 + M·A* in A*-EQUIV may use A*_route for the route vertices b (that is where SPLIT-COUNT evaluates Dhi), so
    C ≤ 3M·(1 + M·A*_route) also holds; C ≤ A*_all needs A*_all. Both directions of the equivalence stand with A* := A*_all.
- (F2) WAIT-TRIGGER and TRIGGER's case (γ). §5's Consequence paragraph dropped case (γ) of Corollary TRIGGER (the β-face's value changes
  below every e-letter: play length / low vertices only). Inside the stated design class (a trigger keyed to u's switch reaching the
  β-face through u's own play) (γ) via u is impossible, since u's switch into qh_(k−1) changes the β-face's e-set (case (β)), so the
  corollary stands as stated. But «the waiting-High class is obstructed» covers only that class. A LENGTH-ONLY trigger at a SECOND vertex
  is not excluded by any box 91 lemma. Box 92 takes it first: on PRIV steps with e_h above Λ it is excluded by box 92's Lemma
  GATE-LOW-NULL (b) (a length-only change leaves both projections unchanged, so the gate cannot flip); the remaining room is the
  non-PRIV gate (box 92 class K7).
