# Addendum 3 P-N5-OFFMONO-add3 (box 49): Lemma OFFSET-MONO holds with no honest-cycle hypothesis (OFFSET-MONO⁺), so a change of κ(q) is always a sum of non-negative level rises and the κ-changes of a class are counted with x-pieces cut at the exit changes only (Corollary CHAIN-COUNT‴) — every game
L-NEW successor 29 (Opus 5.5), D14 / D18, Lead reading L40. Lead's word of 18:52Z (message): "Freeze it now as docs/new/P-N5-OFFMONO-add3-box49.md:
OFFSET-MONO⁺ and CHAIN-COUNT‴, with the data and exact premises, saying which add/add2 cuts become unnecessary while their lemmas stay true."
Written 2026-10-26 from 18:58Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-KPOLY-box49.md §14 (l-new bb92d772, cf57ad0a); this addendum governs. It answers REFEREE 15's OFFADD-N2
(docs/referee/R-N5-OFFMONO-add.md at c2a97189, l. 40-44, 58-60: a CONJECTURE candidate there). It extends P-N5-OFFMONO-box49 (sha1
d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4), P-N5-OFFMONO-add-box49 (sha1 5911aba8fc4e968187523c27b4f48cdc55433b3f) and P-N5-OFFMONO-add2-box49 (sha1
f2d123ef6ebbb71408dc25b503b78edc085cbf9a); none is edited.
Tool: experiments/new/box48/offmono3.py; outputs experiments/new/box48/out/offmono3_*.txt.
Labels: PROVED (L-NEW 29, unrefereed) / DATA / READING. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
What this is and is not, plainly: the cycle cuts of add1 / add2 were needed by their proofs, not by N5; with OFFSET-MONO⁺ they disappear and the
count of P-N5-OFFMONO reduces to the exit changes EXIT_x and the offset value count D, both OPEN (L-SI's side; ALTERNATION).

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma OFFSET-MONO⁺ | PROVED (to sign) |
| §2 | Corollary CHAIN-COUNT‴ (sum form and D form) | PROVED (to sign) |
| §3 | what becomes unnecessary in add1 / add2 | READING (not to sign) |
| §4 | data | DATA (not to sign) |
- Premises (LANDED unless marked):
  - SPEC docs/new/N5-ssi-global.md (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) S1's order; standing premise 1E-N3 (RESULTS R57).
  - RESULTS R38 (a) Remark KEY (λ constant on a phase; l. 1825).
  - RESULTS R56: setting line (l. 2840) and (a) (Aκ), (A0κ), (M1κ), (M2κ), (INJ) (l. 2851), stated with proofs in P-N5-FBPOLY-box41 §0.3
    (sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301) and P-N5-FBRED-box44 §1.1 (sha1 11b15455f70d439c93a48d7e82fcdc14ef73854d).
  - RESULTS R18 (d) Lemma S (a) (l. 803-804), every game by RESULTS R57 (a) (VJ).
  - (SW), as listed among RESULTS R72's landed premises (l. 3768-3769).
  - UNREFEREED, under review with this addendum: P-N5-OFFMONO-box49 §0 (setting), §1 (Lemma OFFSET-MONO and its proof: Step 1, Case L), §2
    (Corollary CHAIN-SUM; EXIT_x; x-pieces); P-N5-OFFMONO-add-box49 §0 ((CYC-ID), (CYC-SHAPE)) and §2 (the charging proof of CHAIN-COUNT′).

## 1. Lemma OFFSET-MONO⁺ (PROVED, every game)
Statement. Let t → t + 1 be an in-phase transition of P, q ∈ Q ∩ U_c with q ≠ c, and p := par_{t+1}(q). Then off_{t+1}(q; p) ⪰ off_t(q; p).
Proof. If q is on no honest cycle at t, this is Lemma OFFSET-MONO. Let q be on an honest cycle at t; by add1 (CYC-ID), q ∈ Z_t(c), and q is
path-free at t with κ_t(q) = (0, s_c·ℓ) (add1 (CYC-SHAPE)). Let y1 := σ̄_t(q), y2 := σ̄_{t+1}(q).
- Step 1 of OFFSET-MONO's proof (the path π from y2 to p along q's honest play at t + 1; backwards induction with (Aκ) at t + 1, (SW) and
  (M1κ)) does not use where q is at t. So off_{t+1}(q; p) ⪰ κwt_c(q) + κ_t(y2) − κ_t(p). By (Aκ) at t (q ≠ c), off_t(q; p) = κwt_c(q) + κ_t(y1)
  − κ_t(p). It remains to show κ_t(y2) ⪰ κ_t(y1).
- y2 lies on q's honest play at t + 1, so y2 ∈ U_c (λ constant, R38 (a)); y2's honest play at t ends in c's honest cycle Z_t(c), which
  contains q. So that play meets q, either before c (Case L1) or after reaching c (Case L2).
- Case L1. This is OFFSET-MONO's Case L verbatim: ζ := y2's t-play up to its first visit of q, Z := q → ζ → q avoids c, κ_t(y2) = κwt_c(Z) +
  κ_t(y1), and κwt_c(Z) ⪰ (0, 0) by Lemma S (a) with S1's reward order. That argument does not use q's position at t.
- Case L2. Let τ″ := σ̄_t with q's choice replaced by y2, and V″ := V_{σ_t,τ″}. Under (σ_t, τ″) the play from q is q, then y2's honest t-play up
  to c (it avoids q), then Z_t(c) from c up to q (all those vertices keep their choices), and back to q. Its cycle is q, y2's t-path to c, and
  the arc of Z_t(c) from c to q; that arc has ranks below rank(c) except c itself (c is the top of Z_t(c)). By Lemma S (a), Ξ_t(q) ⊴ V″(q).
  - If P(Ξ_t y2) ≠ ∅: the top u* of the new cycle is the top of P(Ξ_t y2), with rank(u*) > rank(c). S1's order compares the rewards of the
    cycle nodes first, rewards are injective, so reward(u*) > reward(c). An odd u* of rank > rank(c) has reward −p′(u*) < min(p′(c), −p′(c)) ≤
    reward(c); so u* is even, and the signed weight M_t(y2) > 0 (the top power dominates). y1 is c or lies on Z_t(c), so M_t(y1) = 0 (add1
    (CYC-SHAPE), (A0κ)). Hence κ_t(y2) ≻ κ_t(y1).
  - If P(Ξ_t y2) = ∅: the new cycle's top is c, and V″(q) = (c, ∅, 1 + ℓ(Ξ_t y2)), which is q ⊕ Ξ_t(y2) (rank(q) < rank(c)). Ξ_t(q) ⊴ V″(q)
    with equal cycle nodes gives, by (M1κ), κ_t(q) ⪯ κwt_c(q) + κ_t(y2), and with (Aκ) at t, κ_t(y1) ⪯ κ_t(y2). □

## 2. Corollary CHAIN-COUNT‴ (PROVED, every game)
Fix a run J of consecutive in-phase transitions of P and the class c. An x-PIECE‴ is a maximal run of consecutive transitions of J, none in
EXIT_x (so par(x) = p is constant on its states); v_x(π) := the number of distinct values of off(x; p) on the states of π.
- Statement (sum form). For every q ∈ Q ∩ U_c ∖ {c}, the transitions of J that change κ(q) number at most
  Σ_{x ∈ Q ∩ U_c ∖ {c}} (|EXIT_x| + Σ_{x-pieces‴ π} (v_x(π) − 1)).
- Statement (D form). If v_x(π) ≤ D for every x and π: at most Σ_x D·(|EXIT_x| + 1).
Proof. Let t → t + 1 change κ(q). By Corollary CHAIN-SUM, κ_{t+1}(q) − κ_t(q) = Σ_i [off_{t+1}(x_i; x_{i+1}) − off_t(x_i; x_{i+1})] over q's (t+1)-chain,
x_{i+1} = par_{t+1}(x_i); every term is ⪰ (0, 0) by OFFSET-MONO⁺. The sum is not (0, 0), so some term is ≻ (0, 0): a level x with off_{t+1}(x; p) ≻
off_t(x; p), p := par_{t+1}(x). Charge the transition to (x, t). If par_t(x) ≠ p, t ∈ EXIT_x. Otherwise t is a transition of an x-piece‴ π, on
which off(x; p) is non-decreasing (OFFSET-MONO⁺ at each transition, p fixed), so it rises strictly at most v_x(π) − 1 times there. Distinct
transitions get distinct charges. The x-pieces‴ number at most |EXIT_x| + 1, so Σ_π (v_x(π) − 1) ≤ (D − 1)(|EXIT_x| + 1). □
- In words: per phase and class, κ-changes ≤ Σ_x D·(|EXIT_x| + 1). The route needs only EXIT_x and D (L-SI's ALTERNATION, docs/si/N5-EXIT-box22.md §9).

## 3. What becomes unnecessary in add1 / add2 (READING)
- The CUTS become unnecessary for the count: P-N5-OFFMONO's CHAIN-COUNT (cut CYC_c), add1's CHAIN-COUNT′ (cut ZC_c = ZCH_c ∩ CYC_c) and add2's
  CHAIN-COUNT″ (cut ZC″_c = CYC_c ∩ ZCH_c ∩ FT_c) all follow from CHAIN-COUNT‴ (their cut sets only add pieces and a non-negative term).
- Their LEMMAS stay true, and none of them is withdrawn: add1's Remark Z-CONST, (CYC-ID), (CYC-SHAPE), Lemma ZCH-COUNT; add2's Lemma
  FT-COUNT, Remark FT-CONST, and the code-level Lemma PF-CHOICE and Corollary TIE-CHARGE. (CYC-ID) and (CYC-SHAPE) are used in §1.
- Step A of add1 and Step A″ of add2 are special cases of OFFSET-MONO⁺.
- This explains the controls of add1 (MUT=1) and add2 (MUT=1, MUT=4) that removed the cut and never bit.

## 4. DATA (not to sign; experiments/new/box48/offmono3.py = offmono2.py with the honest-cycle filter removed)
| sample | checks | q on an honest cycle at t (Case L1 / L2) | V_Kc | V_M | controls: V_Kx (opposite sign), MUT=1 V_Kc (p off q's play), at on-cycle checks |
| --- | --- | --- | --- | --- | --- |
| lib41 (experiments/new/box41/lib41.txt) n ≤ 34, S3 + 2 random, seed 7 | 7,689 | 471 (0 / 471) | 0 | 0 | 25; 51 |
| the seven long instances of add1 §4 (nep90, nep76, long121 at their starts; three N5-NCONF §12 climbed n-40 games; snap_n80_s62) | 8,525 | 2 (0 / 2) | 0 | 0 | — |
Files: out/offmono3_lib41_n34_k2.txt, out/offmono3_lib41_n34_MUT.txt, out/offmono3_long7.txt. Case L1 never occurs in these data; Case L2
does (473 checks). REFEREE 15 found 0 failures at 4,006 + 1,371 on-cycle levels with its own engine (R-N5-OFFMONO-add.md l. 58-59, quoted in §5).

## 5. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the file and line named, at the revision named.
- P-N5-OFFMONO-box49 (l-new 3e03271f): “Then off_{t+1}(q; p) ⪰ off_t(q; p).”; “Case L (y2's honest play at t passes q; it does so before c, since q ≠ c
  and the play is simple before c)”; “No step uses where x's play went at t”.
- REFEREE R-N5-OFFMONO-add.md (c2a97189): “this suggests a CONJECTURE that OFFSET-MONO holds for every q ∈ Q ∩ U ∖ {c}, which would make the cut,
  and the CYC term, unnecessary. Not proved (OFFADD-N2).”; “OFFSET-MONO for q on an honest cycle at t: 0 failures in 4,006 + 1,371 checks”.
- RESULTS (3e03271f) l. 803-804: “(a) L_σ is the pointwise minimum of V_{σ,τ'} over Odd's strategies τ'”; l. 1825: “λ_U is a function of τ alone, so on
  every run of states with τ constant it is constant”; l. 3768-3769: “(SW): every Even switch of N5 is to an edge of Iσ”.
- SPEC (3e03271f) l. 30: “compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight”.
- Pins: as in the header and Premises; offmono3.py and outputs: sha1 in the push message.
- Script: `python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-OFFMONO-add3-box49.md 3e03271f:docs/new/P-N5-OFFMONO-box49.md
  c2a97189:docs/referee/R-N5-OFFMONO-add.md 3e03271f:docs/RESULTS.md 3e03271f:docs/new/N5-ssi-global.md` (output experiments/new/box48/out/quotecheck_offmono_add3.txt).
