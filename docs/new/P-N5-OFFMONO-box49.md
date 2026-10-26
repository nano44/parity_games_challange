# Packet P-N5-OFFMONO (box 49): inside a phase, the κ-offset of an Odd choice vertex to its next routing vertex never falls (Lemma OFFSET-MONO), so a change of κ(q) is a sum of non-negative level rises along q's chain (Corollary CHAIN-SUM), and per class the κ-changes of one vertex are at most Σ over the class's Odd choice vertices of (offset values) × (exit changes + cycle transitions + 1), plus the cycle transitions (Corollary CHAIN-COUNT) — every game
L-NEW successor 28 (Opus 5.5), D14 / D18, Lead reading L40; Lead's routing of 16:41Z (Lead's stamp): "(a) Prove that an ENTRY cannot occur inside
a phase, under the hypotheses where OFFSET-MONO applies. … If (a) closes, OFFSET-MONO plus NO-ENTRY becomes a packet." Written 2026-10-26 16:48Z
onward (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-KPOLY-box49.md §2 (first form, with hypotheses (E1), (E2)) and §7 (this form). This packet governs.
Tools: experiments/new/box48/offmono2.py (this form), reset.py (the first form); outputs in experiments/new/box48/out/.
Labels: PROVED (L-NEW 28, unrefereed) / OPEN / DATA / READING. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
What this is and is not, plainly:
- (a) closes in a stronger way than asked: the ENTRY hypotheses (E1), (E2) of KPOLY §2 are NOT needed. The lemma holds at every in-phase
  transition, for every Odd choice vertex q ≠ c on no honest cycle at t, with the offset taken to q's routing vertex at t + 1. So R61's "odometer
  reset" (a lower offset falls while a higher level rises) cannot happen at any level whose vertex is on no honest cycle.
- It does NOT bound the exit changes (a vertex's routing vertex changing), and it does not bound how many values an offset takes. Corollary
  CHAIN-COUNT turns R61's PRODUCT over chain levels into a SUM over the class's Odd choice vertices, at the price of the exit-change count.
  Whether that is polynomial in n and k depends on the exit changes per phase (L-SI successor 17's quantity), which are OPEN.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma OFFSET-MONO | PROVED (to sign) |
| §2 | Corollary CHAIN-SUM | PROVED (to sign) |
| §2 | Corollary CHAIN-COUNT | PROVED (to sign) |
| §3 | comparison with RESULTS R61 (c) and R72 | READING (not to sign) |
| §4 | data | DATA (not to sign) |
| §5 | open | OPEN (not to sign) |
- Premises (LANDED):
  - SPEC docs/new/N5-ssi-global.md (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) S1's order (l. 30-31) and S4c (l. 56-57); standing premise
    1E-N3 (RESULTS R57).
  - RESULTS R38 (a) KEY (λ is constant on a phase).
  - RESULTS R56: the setting line (κ, κwt_c, s_c; docs/RESULTS.md l. 2840) and (a) the facts (Aκ), (A0κ), (M1κ), (M2κ) (l. 2851), stated in
    P-N5-FBRED-box44 §1.1 (l. 49-50; sha1 11b15455…) and P-N5-FBPOLY-box41 §0.3 (l. 93-97; sha1 de244dcd…); (d) κ-Y-FORM_D (l. 2858-2860).
  - RESULTS R18 (d) Lemma S (a) (l. 803-804), on every game by RESULTS R57 (a) (VJ).
  - (SW) "every Even switch of N5 is to an edge of Iσ", as listed among R72's landed premises (docs/RESULTS.md l. 3768-3769): S4a's arena
    restricts Even v to {σ_t(v)} ∪ Iσ_t(v), S4c switches to an edge of Iσ_t.
  - For Corollary CHAIN-COUNT's reading only (§3): RESULTS R61 (b) SAT-k, (c) FB-kT; RESULTS R72.

## 0. Setting (every game)
A phase P of N5 (τ and λ constant; RESULTS R38 (a)); a cycle node c of P; U := U_c := λ^{-1}(c), constant on P; Q := the Odd vertices of out-degree
≥ 2. κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) ∈ ℤ² for z ∈ U, s_c := +1 if Ω(c) is odd, −1 if even, ordered lexicographically (RESULTS
R56's setting line); κwt_c(v) := (wt_c(v), s_c), wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0; κwt_c of a vertex set or path is the sum.
The lexicographic order on ℤ² is compatible with addition, so differences of κ-values are compared in ℤ². next_t(z) := σ_t(z) for Even z,
σ̄_t(z) for Odd z (the honest successor).
- For q ∈ Q ∩ U, q ≠ c: par_t(q) := the first vertex of Q ∖ {q} on q's honest play at t strictly before c, and par_t(q) := c if there is none.
- OFFSET: for s ∈ {t, t + 1} and p ∈ U, off_s(q; p) := κ_s(q) − κ_s(p) ∈ ℤ².
- Facts used, for z ∈ U and in-phase transitions:
  - (Aκ) for z ∈ U ∖ {c}: next_t(z) ∈ U and κ_t(z) = κwt_c(z) + κ_t(next_t z). (A0κ) κ_t(c) = (0, 0).
  - (M1κ) for valuations x, x′ with cycle node c: x ⊴ x′ ⇔ κ(x) ≤ κ(x′).
  - κ-Y-FORM_D: for q ∈ Q ∩ U, q ≠ c, on no honest cycle at t: κ_t(q) = κwt_c(q) + min over Y^q_t := {y ∈ succ(q) ∩ U : y's honest play at t
    avoids q} of κ_t(y); the minimum is attained at σ̄_t(q) (Odd's choice; RESULTS R56 (d) with (Aκ)).
  - (SW): σ_{t+1}(x) ∈ {σ_t(x)} ∪ Iσ_t(x) for every Even x at an in-phase transition.

## 1. Lemma OFFSET-MONO (PROVED, every game)
Statement. Let t → t + 1 be an in-phase transition of P, q ∈ Q ∩ U with q ≠ c and q on no honest cycle at t, and p := par_{t+1}(q). Then
off_{t+1}(q; p) ⪰ off_t(q; p).
Proof. Let y1 := σ̄_t(q), y2 := σ̄_{t+1}(q), and let π := (y2 = x_1, x_2, …, x_r, p) be q's honest play at t + 1 from y2 up to its first visit of p
(π = (p) if y2 = p). All vertices of π lie in U (they lie on q's play, λ_{t+1} = λ_t), and none of x_1, …, x_r is in Q (p is the first vertex of
Q ∖ {q} on the play, and x_i ≠ q because the play is simple before c by (Aκ) iterated and q ≠ c).
- Step 1 (the path π). For every vertex x of π: off_{t+1}(x; p) ⪰ off_t(x; p). Induction backwards along π. At p both sides are (0, 0). Let x = x_i,
  x′ := x_{i+1} (or p) = next_{t+1}(x), with off_{t+1}(x′; p) ⪰ off_t(x′; p). By (Aκ) at t + 1: off_{t+1}(x; p) = κwt_c(x) + off_{t+1}(x′; p) ⪰
  κwt_c(x) + off_t(x′; p) = κwt_c(x) + κ_t(x′) − κ_t(p). It remains to show κwt_c(x) + κ_t(x′) ⪰ κ_t(x), since κ_t(x) − κ_t(p) = off_t(x; p).
  - x Odd: x ∉ Q, so x has one successor: next_t(x) = x′, and (Aκ) at t gives κ_t(x) = κwt_c(x) + κ_t(x′).
  - x Even with σ_{t+1}(x) = σ_t(x): the same.
  - x Even with σ_{t+1}(x) = x′ ≠ σ_t(x): by (SW), (x, x′) ∈ Iσ_t, i.e. Ξ_t(x′) ▷ Ξ_t(σ_t x). Both x′ and σ_t(x) = next_t(x) lie in U ((Aκ); x′ on
    q's play), so both values have cycle node c and (M1κ) gives κ_t(x′) ⪰ κ_t(σ_t x). With (Aκ) at t: κ_t(x) = κwt_c(x) + κ_t(σ_t x) ⪯
    κwt_c(x) + κ_t(x′).
  No step uses where x's play went at t: it need not meet p (this removes KPOLY §2's hypothesis (E2)).
- Step 2 (q). By (Aκ) at t + 1 and Step 1 at y2: off_{t+1}(q; p) = κwt_c(q) + off_{t+1}(y2; p) ⪰ κwt_c(q) + κ_t(y2) − κ_t(p). And off_t(q; p) =
  κwt_c(q) + κ_t(y1) − κ_t(p) by (Aκ) at t. It remains to show κ_t(y2) ⪰ κ_t(y1) or to absorb the difference. y2 ∈ U (it lies on q's play).
  - Case N (y2's honest play at t avoids q): y2 ∈ Y^q_t, and q is on no honest cycle at t, so κ-Y-FORM_D gives κ_t(y1) ⪯ κ_t(y2). Done.
  - Case L (y2's honest play at t passes q; it does so before c, since q ≠ c and the play is simple before c): let ζ be that play from y2 up to
    its first visit of q, and Z := the cycle q → ζ → q. By (Aκ) iterated along ζ, κ_t(y2) = κwt_c(ζ) + κ_t(q) = κwt_c(ζ) + κwt_c(q) + κ_t(y1) =
    κwt_c(Z) + κ_t(y1). So it suffices that κwt_c(Z) ⪰ (0, 0).
    - Let τ″ := σ̄_t with q's choice replaced by y2. ζ is a play under (σ_t, σ̄_t) that avoids q until its end, so under (σ_t, τ″) the play from q
      is the cycle Z, and V_{σ_t,τ″}(q) has as cycle node the vertex u* of largest rank on Z; c ∉ Z (ζ ends at q before c), so u* ≠ c.
    - Lemma S (a) (RESULTS R18 (d); every game by R57 (a)), with Ξ_t = L_{σ_t} (S1's counterstrategy is optimal: standing premise 1E-N3):
      Ξ_t(q) ⊴ V_{σ_t,τ″}(q). SPEC S1's order compares the reward of the cycle node first
      (reward(v) = p′(v) if v is even, −p′(v) if odd), and rewards are injective, so reward(u*) > reward(c).
    - If some vertex of Z has rank > rank(c): then rank(u*) > rank(c), wt_c(Z) has the sign of u* (the largest power of 2 dominates the signed
      sum), and u* odd would give reward(u*) = −p′(u*) < min(p′(c), −p′(c)) ≤ reward(c), a contradiction. So u* is even and wt_c(Z) > 0, hence
      κwt_c(Z) ≻ (0, 0).
    - Otherwise wt_c(Z) = 0 and rank(u*) < rank(c). If c is even, reward(c) = p′(c) exceeds the reward of every vertex of lower rank (even:
      smaller p′; odd: negative), against reward(u*) > reward(c). So c is odd, s_c = +1, and κwt_c(Z) = (0, |Z|) ≻ (0, 0).
  In both cases off_{t+1}(q; p) ⪰ κwt_c(q) + κ_t(y1) − κ_t(p) = off_t(q; p). □
- Remarks. (i) Step 1 is the Bellman-Ford monotonicity of RESULTS-landed BF-type arguments (an Even vertex moves only along Iσ, and in one
  class Ξ-improving means κ-larger), read with p as a moving reference: it holds for ANY reference vertex p whose t+1-path from x contains no
  Odd choice vertex. (ii) Case L is the mirror of the cycle argument in L-SI's BF-F_D (ii) (docs/si/N5-ROOT-box20.md §2): there an Even cycle with
  positive weight is excluded by Even's optimum; here an Odd cycle with negative weight is excluded by Odd's optimum (Lemma S (a)). (iii) Only
  "q on no honest cycle at t" is assumed; q may be on an honest cycle at t + 1 (Step 2 uses (Aκ) at t + 1, valid for every z ∈ U ∖ {c}).

## 2. Corollaries CHAIN-SUM and CHAIN-COUNT (PROVED, every game)
For an in-phase transition t → t + 1 and q ∈ Q ∩ U, q ≠ c, the (t+1)-CHAIN of q is x_0 := q, x_{i+1} := par_{t+1}(x_i), until x_{h+1} = c. (Each x_i
lies on q's play at t + 1, which is simple before c, so the chain has h + 1 ≤ |Q ∩ U| terms besides c.)
- Corollary CHAIN-SUM. κ_{t+1}(q) − κ_t(q) = Σ_{i=0}^{h} [off_{t+1}(x_i; x_{i+1}) − off_t(x_i; x_{i+1})], and every term with x_i on no honest cycle at
  t is ⪰ (0, 0). Proof: the sum telescopes to κ_{t+1}(q) − κ_{t+1}(c) − κ_t(q) + κ_t(c), and κ(c) = (0, 0) at both times (A0κ); for i ≥ 1,
  par_{t+1}(x_i) = x_{i+1} because x_i's play at t + 1 is a suffix of q's; each term is OFFSET-MONO at x_i. □
  So κ(q) changes at t → t + 1 only if some level x_i of its (t+1)-chain has a strict offset rise to x_{i+1}, or some x_i is on an honest cycle at t.
- Corollary CHAIN-COUNT. Fix a run J of consecutive in-phase transitions of P and the class c. For x ∈ Q ∩ U ∖ {c}: EXIT_x := the transitions of J
  with par_t(x) ≠ par_{t+1}(x); CYC_c := the transitions of J at which some x ∈ Q ∩ U ∖ {c} is on an honest cycle at t. An x-PIECE is a maximal
  run of consecutive transitions of J, none in EXIT_x ∪ CYC_c (so par(x) = p is constant on its states). Suppose that on the states of every
  x-piece, off(x; p) takes at most D values. Then for every q ∈ Q ∩ U ∖ {c} the number of transitions of J that change κ(q) is at most
  |CYC_c| + Σ_{x ∈ Q ∩ U ∖ {c}} D·(|EXIT_x| + |CYC_c| + 1).
  Proof. Let t → t + 1 change κ(q). If it is in CYC_c, count it there (≤ |CYC_c|). Otherwise, by CHAIN-SUM some level x of q's (t+1)-chain has
  off_{t+1}(x; p) ≻ off_t(x; p), p := par_{t+1}(x). If par_t(x) ≠ p, the transition is in EXIT_x (≤ |EXIT_x|). Otherwise it lies in an x-piece, where
  OFFSET-MONO applies at every transition (par(x) = p at both ends, x on no honest cycle at the source), so off(x; p) is non-decreasing on the
  piece and rises strictly at most D − 1 times there. The x-pieces number ≤ |EXIT_x| + |CYC_c| + 1. Summing over x: ≤ |CYC_c| + Σ_x (|EXIT_x| +
  (D − 1)(|EXIT_x| + |CYC_c| + 1)) ≤ |CYC_c| + Σ_x D·(|EXIT_x| + |CYC_c| + 1). □

## 3. READING (not to sign): what this gives for the 𝒞^kO count, and against R61 and R72
- R61 (c) FB-kT bounds V_q (distinct κ(q) values at late fallbacks) by Σ_{h=0}^{m_c−1} D_c·((m_c − 1)·D_c)^h, a product over chain levels: R61 (b)
  SAT-k gives κ_t(q) ∈ S_{q,p} + κ_t(p), |S_{q,p}| ≤ d_q, and the product counts the possible sums because a lower offset might fall while an upper
  one rises (R61 §5's "model obstruction"). OFFSET-MONO says that cannot happen at a level on no honest cycle. In the window where SAT-k holds at
  every level (its hypotheses as in R61 (b); I have not matched them to "every x-piece" line by line), D := D_c, and CHAIN-COUNT gives
  V_q ≤ 1 + |CYC_c| + Σ_{x} D_c(|EXIT_x| + |CYC_c| + 1): LINEAR in m_c = |Q ∩ U ∖ {c}| instead of exponential, plus the EXIT and CYC counts.
- So the answer to "does it remove the exponent in k, or only one factor": it removes the whole product over chain levels, but only by
  introducing the exit-change counts EXIT_x, which R61's value count does not need. The two bounds are min-combined: R61's is exponential in k
  and independent of exits; CHAIN-COUNT is linear in k and linear in the exits. A bound polynomial in n and k follows exactly when the exit
  changes and the CYC transitions per phase (or per late window) are polynomial. That is OPEN.
- Against RESULTS R72 (RELAY-CHAIN (b): Σ_{q ∈ Q_c} ρ_q ≤ |Q_c|·(ROUTE_c + CYC_c + TOG_c)): R72 charges every κ change of a relay to a ROUTE, CYC or
  TOG event of its class. CHAIN-COUNT splits ROUTE-type activity further: a level that keeps its routing vertex can only RAISE its offset, so
  same-exit route changes are monotone and bounded by the number of offset values; what is left is EXIT. I have not checked term by term that
  R72's ROUTE events equal EXIT ∪ same-exit offset rises; the comparison is a reading.

## 4. DATA (not to sign; experiments/new/box48/offmono2.py; outputs in experiments/new/box48/out/)
offmono2.py checks OFFSET-MONO at every in-phase transition and every q ∈ Q, q ≠ c, on no honest cycle at t, with p := par_{t+1}(q): V_Kc =
off_{t+1}(q; p) ≺ off_t(q; p) in κ with the class sign s_c (must be 0); V_M = the same on the first component only (must be 0); V_Kx = with the
OPPOSITE length sign (a control for the sign; expected to fail in Case L-type ties); LOOP = Case L occurs; MUT=1 = p replaced by a vertex of U
not on q's (t+1)-play (must bite).
| sample | checks | Case L | parent changed at t → t+1 | V_Kc | V_M | V_Kx | MUT=1: V_Kc / V_M |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (experiments/new/box41/lib41.txt), n ≤ 34, S3 + 2 random, seed 7 | 7,218 | 7 | 82 | 0 | 0 | 700 | 1,094 / 1,040 |
| nep90_n40 (start ../si/rund) | 455 | 0 | 28 | 0 | 0 | 8 | 150 / 136 |
| nep76_n40 | 390 | 0 | 42 | 0 | 0 | 11 | 186 / 156 |
| long121_n40 | 363 | 2 | 26 | 0 | 0 | 1 | 71 / 71 |
| N5-NCONF §12 climbed games (n 48): nep90 / nep76 / long121 descendants | 1,311 / 1,134 / 1,270 | 6 / 0 / 1 | 110 / 57 / 68 | 0 | 0 | 9 / 5 / 0 | 536 / 398 / 182 (V_Kc) |
| KPOLY §0 climbed n = 80 game (out/qpcclimb/scale/snap_n80_s62.pg, sha1 06dd25e2) | 3,600 | 9 | 177 | 0 | 0 | 7 | 1,771 / 1,576 |
Files: out/offmono2_lib41_n34_k2.txt, out/offmono2_lib41_n34_MUT.txt, out/offmono2_long7.txt. Case L occurs (25 checks in all) and the lemma held
there; checks with a changed parent (590) are covered, which KPOLY §2's first form excluded. reset.py (KPOLY §2) found 0 ENTRY events; the
present form makes ENTRY irrelevant.

## 5. OPEN (not to sign)
- The exit changes EXIT_x per phase (L-SI successor 17's bound side) and the CYC transitions per phase.
- The number of values D of an offset over a sub-run with fixed routing vertex outside R61's late window.
- Whether CHAIN-COUNT and R61's SAT-k window can be matched exactly, so that FB-kT's V_q has a signed linear-in-k form with EXIT as the only
  new term.

## 6. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the file and line named (trunk 7d87f9be merged into l-new at 58061d91).
- SPEC docs/new/N5-ssi-global.md l. 30: “compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight”; l. 31: “if c is odd,
  longer is better for Even; if c even, shorter is better.”; l. 56-57: “for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ
  maximising (Ξσ(w), w)”.
- RESULTS R56 setting, docs/RESULTS.md l. 2840: “s_c := +1 if Ω(c) is odd, −1 if even”; (a) l. 2851: “Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per
  honest class”; (d) l. 2858: “κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y)”.
- P-N5-FBRED-box44 l. 49-50: “κ_t(z) = κwt_c(z) + κ_t(next_t z)”. P-N5-FBPOLY-box41 l. 95: “For valuations x, x′ with cycle node c_θ: x ⊴ x′ ⇔ κ(x) ≤
  κ(x′)”; l. 93: “(A0κ) κ_t(c_θ) = (0, 0)”.
- RESULTS R18 (d), l. 803-804: “(a) L_σ is the pointwise minimum of V_{σ,τ'} over Odd's strategies τ'”.
- RESULTS R72 premises, l. 3768-3769: “(SW): every Even switch of N5 is to an edge of Iσ”.
- RESULTS R61 (c), l. 3123: “V_q ≤ Σ_{h=0}^{m_c−1} D_c·((m_c − 1)·D_c)^h”.
- Pins: N5-ssi-global.md 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e; P-N5-FBRED-box44.md 11b15455f70d439c93a48d7e82fcdc14ef73854d; P-N5-FBPOLY-box41.md
  de244dcd3592b04eca2080a0efe10a7c0b2e5301; offmono2.py and the outputs: sha1 in the push message.
- Script: `python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-OFFMONO-box49.md 58061d91:docs/new/N5-ssi-global.md 58061d91:docs/RESULTS.md
  58061d91:docs/new/P-N5-FBRED-box44.md 58061d91:docs/new/P-N5-FBPOLY-box41.md` (output experiments/new/box48/out/quotecheck_offmono.txt).
