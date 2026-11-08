# Box 84: HUB PAIR «MIRROR», milestone 1 (L-SI successor 44; Lead GO 01:54Z 2026-11-08, design (c) of box83-ladder.md §0)
Written 2026-11-08T02:26Z (date -u). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box84/ (pair84.py builder; gen83.py is a byte copy of box 83's DSL; check84.sh, wired). Measured with box 83's
meas83 / lock83 and the pinned box 81 / 82 tools (census81, anal82, real81, xchk81).

## 0. Answer (milestone 1)
- Design MIRROR (§1). It breaks LOCK-UP's hypothesis «every option of B other than S has its Ξ-target in Y ∪ {X} ∪ Z ∪ {u}».
  - SET_l's continuation goes into the mirror M_(l+1); B_l's UP and lanes go into the real B_(l+1).
  - M_(l+1)'s play never passes B_(l+1), so the alternatives reach e's the continuation does not have. lock83 (which takes X = B_(l+1)) finds HYP in 0 states, as it must: the
    continuation never reaches B_(l+1).
- Result (DATA, §2), with mirror UP into the next mirror (MUP = 1):
  - Bit 1 now resets TWICE inside one Λ-interval (box 83: once).
  - At h = 3 the hub's e-set walks through 8 = 2^3 values, all lex-increasing.
  - But growth stays LINEAR: hubH 4 / 8 / 11 / 15 and R 4 / 9 / 13 / 17 for h = 2 / 3 / 4 / 5. RF(1) = 5 at every h ≥ 3.
  - Max adoptions per bit per Λ-interval 3 and max resets 2 (h = 3, 4, 5).
- NOT a counter. The obstruction (READING from the traces, not proved):
  - Bit l's SET condition is {e_l} ∪ m_(l+1) ▷ r_(l+1), where r_(l+1) := E(B_(l+1)) and m_(l+1) := E(M_(l+1)) are the real and mirror
    e-sets one level up.
  - That condition reads only the bits ABOVE l. So a carry starts ONE ripple wave down the bits: each B_l re-sets as soon as the
    mirror catches up, without waiting for the lower bits to count.
  - B_l's re-set does reset and re-set B_(l−1) (2 toggles), but B_l's reset triggers nothing below. Doubling would need both.
- The deeper reason: by R218 PLAY-BLIND, B_l's value can react to a lower bit only if B_l's play passes a mover that switches. The
  MIRROR plays only go up, so a bit is blind to the lower counter. Making a bit wait for the lower bits needs a route from B_l DOWN into
  them. That is [F09]'s s-hub (H1), which leaks with access (LEAK-ARCH) and was DEAD without access in R218 §6 (t4).
  So the next question is a downward route without H1's leak. OPEN.

## 1. The build (pair84.py; R104 IDEAL format)
- Real bits B_1..B_h (B_l at level l); mirrors M_2..M_h (M_l at level l); top T = B_(h+1) = M_(h+1); dummies D_l as in box 83.
- Every bit and mirror x of level l has:
  - UP (β → B_(l+1); with MUP = 1, a mirror's UP goes to M_(l+1));
  - an RS2 delay lane of length L_l (B) or LM_l (M), with exits → B_(l+1);
  - SET (W-target w at level l − 1 with one option β → M_(l+1); Ξ-target x; even β).
- The mirror's e lies above the real e at the same level (gate key (9, 1, l) > (9, 0, l)).
- H (level 0): β → B_1. Start: every bit on UP; lanes on EXIT.
- Intended mechanism: after a carry into l + 1, r_(l+1) holds e_(l+1) while m_(l+1) lags, so B_l's alternatives win and B_l resets.
  Once M_(l+1) sets, its mirror e outranks e_(l+1), so B_l re-sets.

| instance | args (h; L; LM; MUP) | sha1 (.json) |
| --- | --- | --- |
| HP2_mup | 2; 1,4; 8; 1 | b7964d561d92c316261d145b52bce66026ea00af |
| HP3_mup | 3; 1,3,6; 6,12; 1 | 3766033c28302e00db5427d74b7f7a06d8f5adee |
| HP3_mup0 | 3; 1,3,6; 6,12; 0 | e99c9ef6ea31da8638f85cce01daf3ab463c87f1 |
| HP4_mup | 4; 1,3,9,19; 7,10,30; 1 | d7ebbea0c3f21ce76b4304756387f6c067090737 |
| HP5_mup | 5; 2,4,12,17,22; 5,17,20,34; 1 | 39bce9f76d5ad06830d225c66e3835cde55fb9ef |
(sha1 of the working-tree files at the commit that adds them; re-take with `git show <that commit>:path | sha1sum`.)

## 2. DATA (outputs in experiments/si/box84/out/)
Unit: one Howard run per frozen instance (IDEAL-CYC, stored start). Set: the 5 instances above. Scope: box81/ref idealcyc. Counters as
in box83-ladder.md §3 (RF, hubH, SumD = Σ_v D^tot_E(v), bits, premature resets); lock83: adoptions and resets per bit per Λ-interval.

| instance | N | n | T | R | C | RF (levels 0..h) | hubH | SumD | adoptions / resets per bit (max) | N5′-xi on Γ3 (iters / fb / T3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HP2_mup | 40 | 253 | 11 | 4 | 0 | 0 3 2 | 4 | 291 | 2 / 1 | 14 / 1 / 11 |
| HP3_mup | 77 | 497 | 17 | 9 | 0 | 0 5 4 2 | 8 | 710 | 3 / 2 | 20 / 1 / 17 |
| HP3_mup0 | 77 | 497 | 15 | 6 | 0 | 0 3 4 2 | 5 | 685 | 2 / 1 | not run |
| HP4_mup | 186 | 1,245 | 37 | 13 | 0 | 0 5 7 4 2 | 11 | 1,991 | 3 / 2 | 40 / 1 / 37 |
| HP5_mup | 301 | 2,035 | 43 | 17 | 0 | 0 5 7 7 4 2 | 15 | 4,349 | 3 / 2 | not run |
- Premature resets 0 everywhere. N5′-xi = T + 3 with one fallback and mover phase = Howard (real81) on HP2-HP4. xchk81: game, states,
  values and labels SAME on HP2-HP4.
- Hub walk at h = 3 (HP3_mup, meas83 -v), 8 values: ∅ < {e_B1} < {e_B1, e_M2} < {e_B3} < {e_B1, e_B3} < {e_B1, e_M3} < {e_B2, e_M3}
  < {e_B1, e_M2, e_M3}. At h = 4 there are 11 values; the first lane phase sets several bits at once (0001 → 0111), so the low part is
  skipped.
- MUP = 0 (a mirror's UP goes to the real B_(l+1)): an unset mirror then shows r_(l+2)'s real e's, so a carry two levels up never
  resets B_l. h = 3: hubH 5, RF(1) 3, the box 83 picture.
- Lane scan (scratch, 25 random lane-length draws per h, seeded): best hubH 8 / 11 / 15 and R 9 / 13 / 17 at h = 3 / 4 / 5; RF(1) = 5 in
  every best run. So the linear growth is not a tuning artefact of the frozen choices.
- Trace of HP5_mup (meas83 bits, steps 24-43): the carry into bit 5 at t 24 gives one wave, B4 ↓ (25); B3 ↓↑ (26, 27); B2 ↓↑ (28, 29);
  B1 ↓↑ (30, 31). M5 sets at t 36 and gives a second wave, B4 ↑ (37), B3 ↓↑, B2 ↓↑, B1 ↓↑. Each bit toggles twice per wave, but the
  waves do not nest.

## 2b. Where MIRROR sits against L-RED's Lemma PRIV-FLIP (R222 §3, claude/l-red 3d9e788d; Lead 02:30Z)
- PRIV-FLIP (PROVED lane, L-RED): on a Λ-interval with Λ(B) ∈ {K1, K2}, if no play from SET's W-target or from B's other gates passes
  B (PRIV), then #changes of [σ(B) = S] ≤ 1 + (D_E,I(w) − 1) + Σ_(o ≠ S) (D_E,I(g_o) − 1). With HUB-ASC-G / UP-B this is polynomial
  for bounded U(G).
- Which of the three ways out MIRROR takes:
  - PRIV holds: every play from B_l's options goes up and never returns to B_l.
  - Λ is constant: C = 0 in every run.
  - U(G) grows with h. Every UP, carry and lane exit is an upward Ξ-edge, so U(G) = Θ(N); census81 gives U 20 / 39 / 94 / 152 for
    HP2 / HP3 / HP4 / HP5.
  So PRIV-FLIP does not forbid MIRROR. But it explains the DATA quantitatively.
- B_1's flips are at most 1 + Σ(D_E − 1) over w_1 (whose play is M_2's) and B_1's other gates (whose plays are B_2's).
  - A counter needs B_1 to flip about 2^h times. So E(M_2) or E(B_2) must take about 2^(h−1) values: the same hub-pair question one
    level up.
  - MIRROR's hub e-set heights grow linearly (maxD 4 / 8 / 11 / 15), so B_1's flips stay bounded (RF(1) = 5).
- FINDING (READING with PRIV-FLIP): a PRIV SET counter is a recursion on e-set heights, D(l) ≳ 2·D(l + 1) for the hubs that a level-l
  bit reads. Nothing in MIRROR makes a level-(l + 1) hub's height double. The way out is not U(G) alone.
  - Under PRIV, one needs higher hubs that themselves count (heights 2^(h−l)).
  - Without PRIV, a play from the bit's own options must return to the bit (the R218 §4 branch (c) cycle).

## 3. Next (proposal)
- A bit must WAIT for the lower counter before re-setting: its SET (or its lane) must be beaten until the bits below are full. By
  PLAY-BLIND that needs a route from B_l down into the lower bits, without H1's access leak. Candidate: the downward route enters only
  the lower MIRRORS (which lag), never a real bit's gate. LEAK-ARCH's H1 is about the real hub route, so this may avoid its proof; R218
  §4's branch (c) cycle must be checked first. Not built.

## 4. Milestone 2 (ii): PRIV broken by an EVEN-top cycle (Lead 03:04Z; written 2026-11-08T03:07Z, date -u)
Tools: experiments/si/box84/m2/ (cyc84.py adds a CYC option to a bit; priv84.py = my own count of L-RED's PRIV-FLIP quantities;
climb84.py adversarial climb; check_m2.sh, called by check84.sh).
- Design (cyc84.py): bit B gets an option CYC.
  - Its β is even and above every other β (TOP). It goes to a level-0 helper c whose one option leads back to B. So when Odd keeps
    β, the play from CYC's gate returns to B through an even-top route, and PRIV fails by construction.
  - Its e-face goes to a new mover y one level down, with β → B_(l+1) (live: Odd CAN break the cycle).
  - The gate index is below or above every level-l gate.
- **Lemma LIVE-BREAK (PROVED, lane; one line, the argument of LOCK-UP (i)).** On an interval with every cycle node constant and
  Λ(B) ∈ {K1, K2}: if σ_t(B) = o and the β-route of o's gate returns to B, then Odd takes the e-face at some gate of that route at t.
  Otherwise B's play is the returning cycle, whose cycle node is its most relevant vertex; that vertex is a β, not K1 or K2.
  So a returning route is never on a current play of B, and PRIV fails only in the HIDDEN value of o (its gate's β-face while B sits
  elsewhere).
- DATA (unit: one Howard run; scope: idealcyc; counters as §2 plus priv84: per (B, SET option, Λ-interval) flips of [σ(B) = S] minus
  PRIV-FLIP's bound, «excess»):

| instance | base + CYC on | T | R | RF (levels 0..h) | hubH | excess max (PRIV units / non-PRIV units) |
| --- | --- | --- | --- | --- | --- | --- |
| CY2_lr | LR2_exitup; B1 | 9 | 6 | 0 6 1 | 6 | 0 / −5 |
| CY2_hp | HP2_mup; B1 | 11 | 6 | 0 6 2 | 6 | 0 / −5 |
| CY3_hp | HP3_mup; B1, B2 | 17 | 12 | 0 7 8 2 | 8 | 0 / −7 |
| CY4_hp | HP4_mup; B1, B2, B3 | 37 | 17 | 0 7 9 8 2 | 11 | 0 / −13 |
- At h = 2, CY2_lr meets the box 83 §5.3 criterion formally: RF(1) = 6 ≥ 2·1 + 2, hubH 6 ≥ 4, no premature reset. But the mechanism
  is not a re-arm.
  - CYC is a second e at level 1, below e_SET, so bit 1 becomes a 3-valued digit. The hub walks ∅ < {CYC} < {SET} < {e_B2} <
    {CYC, e_B2} < {SET, e_B2}, i.e. 3 × 2 values.
  - At h = 3 and 4, hubH stays 8 and 11, exactly MIRROR's. CYC adds R (12 vs 9, 17 vs 13) but no recursion.
- PRIV-FLIP's bound is attained (excess 0) on every PRIV unit of LR3_exitup and HP3-HP5_mup. It is never exceeded on non-PRIV units:
  max excess −5 … −13 on the CYC gadgets.
- Adversarial climbs (climb84.py, seeds 11-14, 1,500 iterations each; rand191 genomes, d × w = 2×2, 3×2, 2×3, 3×3, every mover given
  a SET-type option; score = (max excess over non-PRIV units, their max flips, T); out/climb_s*.log): best excess −1, −1, 0, −1, and
  max flips of a non-PRIV unit ≤ 1. Weak evidence: random cyclic genomes rarely flip a SET option at all.
- **(ii) is DEAD at h = 2 (as a recursion).** Exact obstruction: LIVE-BREAK. A returning even-top route is never Λ while Λ(B) ∈ {K1, K2},
  so it acts only as one more hidden value (one more digit value per CYC option), not as a re-arm. A dead CYC gate (no live e-face)
  would make the cycle Λ(B) when adopted: a C-step (READING: F1 then keeps B at that even cycle).
  Instance: CY2_lr (and CY3_hp, CY4_hp for the h-growth).
- Not proved: a version of PRIV-FLIP for non-PRIV units. CONJECTURE (DATA above: 0 exceedances in 4 gadgets + 4 climbs): its bound
  holds for every SET-type option when Λ(B) ∈ {K1, K2}.

## 5. Milestone 3 (i): can a bit WAIT for the lower count? (Lead 03:39Z; written 2026-11-08T03:41Z, date -u)
Tools: experiments/si/box84/m3/ (low84.py smallest test; lb84.py machine check of LOWER-BLIND; check_m3.sh, called by check84.sh).
### 5.1 On paper (the Lead's key question first)
- E-MON (P-N5-ASC §3) applied to a lower-reading hub v: on a Λ-interval, if E_t(v) loses e's at t + 1 (lower bits reset at a carry),
  then E_(t+1)(v) gains an e more relevant than every e it lost (lex order = numeric order of the 0/1 word, R221 NO-REFLECT).
  - So a hub that reads the lower count must also read, at every carry that clears it, a more relevant «carry» e.
  - For the hub through which bit l waits, that is an e of level ≥ l (or of level l above every cleared one): bit l's own e (PRIV
    fails), the e of a copy of bit l, or a higher e.
  - E-MON does NOT forbid both heights doubling. The lower hub can be a full bottom-up counter view, as ASC-EXP is. But it forces the
    lower hub to carry bit l's state. Under PRIV that state must come from a copy.
- **Lemma LOWER-BLIND (KEEP form) (PROVED, lane).** Let S = (w, Ξ-target B, even β) be a SET-type option of B, on an interval where every
  cycle node is constant and Λ(B) ∈ {K1, K2}. Assume PRIV at t and σ_t(B) = S. Then σ_(t+1)(B) = S iff U(S) >lex U(g_o) for every other
  option o whose gate has cycle node Λ(B). Here U(·) := the e-vertices of the play that are at least as relevant as e_S, and
  U(S) = {e_S} ∪ U(w). Under [E-LEV] these are e's of level ≥ lev(B). So a SET bit's RESET is never decided by lower-level e's.
  Proof.
  - Odd takes e at g_S (LOCK-UP (i) / PRIV-FLIP (a)), so S's value has e-set {e_S} ∪ E(w).
  - e_S is private (PRIV), so for each o the symmetric difference of the e-sets contains e_S. Its most relevant element z is therefore
    at least as relevant as e_S, and it is the most relevant element of U(S) Δ U(g_o).
  - With equal cycle nodes, z decides (PRIV-FLIP's facts: only e's, c_W, K0, K3 lie above an e, and those agree), and ties are
    impossible. Howard keeps S iff S ▷ every option. Options with another cycle node cannot be chosen inside the interval. ∎
  - The ADOPTION form is FALSE. A hidden S shows its β-face (HIDE-BUSY), so adopting S also needs B's current option to beat the
    others, and lower e's can decide that. lb84 run on adoption steps too (scratch): 67 / 259 (HP4_mup), 58 / 250 (CY4_hp), 9 / 51
    (RS2_L8M6) and 5 / 49 (RSG_K4) mispredictions.
- Consequence for a counter (READING): resets come only from above, which a binary counter needs anyway. The WAITING has to happen
  at adoption, and the waiting hub must carry a level-l «carry» e (E-MON).
### 5.2 Smallest test (low84.py): B2 waits on bit 1 through a lower mirror
- Base HP2_mup (§1). A level-1 mirror M1 copies B1's rule: UP and SET continuation → M2; an RS2 lane exiting to M2 (PRIV kept) or to
  B2 (PRIV broken); its mirror e lies above e_B1. B2 gets an option LOW (β → M1, dead e-face).

| instance | M1 lane exits | T | R | C | bits (B2 B1) | premature resets | sha1 (.json) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LO2_priv | M2 (PRIV) | 12 | 4 | 0 | 00 01 10 … 10 01 00 | 1 (t 11) | 6f3c27f813233782ad760b821677c9bc8c968c65 |
| LO2_nopriv | B2 (PRIV fails) | 10 | 3 | 1 | 00 01 10 10 00 … | 1 (t 5) | 2ad3c7e3f782fed8afdafa4c9bca4a8fd53f09ef |
- LO2_priv: B2 does NOT wait for B1. LOW's play climbs M1 → M2, and M2's mirror e lies above e_B2. So when M2 sets, LOW ▷ SET_B2 and
  B2 resets with no carry. The run ends at 00. This is a premature reset by B2's OWN mirror.
- LO2_nopriv: the LOW route returns to B2, and the bits die at 00 with a C-step. This is R218's H1-CYCLE picture.
- Exact obstruction (SELF-MIRROR DICHOTOMY; READING from LOWER-BLIND plus the test). The carry e that E-MON forces into B_l's waiting
  hub is either
  - more relevant than e_SET_l: then by LOWER-BLIND it decides B_l's KEEP, and B_l resets whenever its copy sets (LO2_priv); or
  - B_l's own e: PRIV fails, and the route is hidden-only (LIVE-BREAK) or a cycle (LO2_nopriv).
- Not tested, and not excluded by anything proved: the third option, a copy of bit l whose e lies at level l but BELOW e_SET_l. It is
  invisible to B_l's KEEP (LOWER-BLIND) yet still more relevant than every lower e, so it can serve as E-MON's carry. That needs TWO
  copies per level: one above e_l for the lower bit's continuation (MIRROR), one below e_l for B_l's own waiting hub.
- DATA, LOWER-BLIND (keep form), lb84.py:
  - Unit: steps t → t + 1 inside a constant-cycle-node interval with σ_t(B) = S, PRIV at t, Λ(B) ∈ {K1, K2}.
  - Set: LR3_exitup, LR6_exitup, HP3-HP5_mup, CY3_hp, CY4_hp, RS2, RS2_L8M6, RSG_K4, LO2_priv, LO2_nopriv. Scope: idealcyc.
  - 825 steps, 0 mispredictions; on 102 of them lower e's are present (out/lb84.out).
### 5.3 Where the counter question stands after box 84 (READING; the Lead's requested reduction, with its one open case)
- Under PRIV and constant Λ, a SET bit resets only on changes of the upper parts of its options' plays (LOWER-BLIND). Its flips are
  bounded by the e-set heights of those plays (PRIV-FLIP).
- Breaking PRIV with a returning route gives hidden values only (LIVE-BREAK) or Even-won cycles (E-CYCLE / H1-CYCLE).
- So a counter needs Λ changes, or hubs with unboundedly many ascents whose heights double per level. The one construction not yet
  excluded is the two-copies-per-level design of §5.2 (the low copy). That is the next build, for my successor.
