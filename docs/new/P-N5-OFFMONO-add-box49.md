# Addendum P-N5-OFFMONO-add (box 49): an unchanged cycle of c changes no κ-value or routing vertex on it (Remark Z-CONST); P-N5-OFFMONO's Corollary CHAIN-COUNT holds with its cut set CYC_c replaced by ZC_c := ZCH_c ∩ CYC_c, the cycle changes of c at which an Odd choice vertex sits on c's cycle (Corollary CHAIN-COUNT′); and the cycle changes per phase and class are at most (n − 1)·|U_c| + TIE_c + ODDC_c (Lemma ZCH-COUNT) — every game
L-NEW successor 29 (Opus 5.5), D14 / D18, Lead reading L40. Lead's GO of 17:24Z (message to L-NEW): item 2, "the OFFMONO addendum freeze", to be
reviewed together with P-N5-OFFMONO-box49. Written 2026-10-26 from 17:28Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-KPOLY-box49.md §8 (successor 28, l-new 331f0337). This addendum governs where it differs from KPOLY §8; the differences are
listed in §5. The packet it extends, docs/new/P-N5-OFFMONO-box49.md (sha1 d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4), is not edited.
Tool: experiments/new/box48/zch.py; outputs experiments/new/box48/out/zch_*.txt.
Labels: PROVED (L-NEW 29, unrefereed) / OPEN / DATA / READING. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.
What this is and is not, plainly:
- It removes from P-N5-OFFMONO's count every transition at which some Odd choice vertex is on c's cycle but the cycle does not change (on
  kw25_n32 that is a whole phase: old-sense CYC 25 = phase length, cycle changes 0). It bounds the remaining cycle changes polynomially EXCEPT for
  two kinds, TIE_c (Odd vertices on c's new cycle re-route with unchanged κ) and ODDC_c (the cycle node c is an Odd choice vertex and only its
  own choice changes). Those two are OPEN.
- It does not bound the exit changes EXIT_x (L-SI successor 18's quantity) or the number D of offset values on a piece. A phase count
  polynomial in n and k on this route still needs EXIT_x, TIE_c, ODDC_c per phase and D (P-N5-OFFMONO §5).

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Remark Z-CONST | PROVED (to sign) |
| §2 | Corollary CHAIN-COUNT′ (stated form and sum form) | PROVED (to sign) |
| §3 | Lemma ZCH-COUNT | PROVED (to sign) |
| §4 | data | DATA (not to sign) |
| §5 | differences from KPOLY §8 | READING (not to sign) |
| §6 | open | OPEN (not to sign) |
| §7 | what the addendum gives, against RESULTS R61 and R72 | READING (not to sign) |
- Premises (LANDED, the same entries P-N5-OFFMONO §"Premises" lists, plus (M2κ)):
  - SPEC docs/new/N5-ssi-global.md (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e) S1's order and S4c; standing premise 1E-N3 (RESULTS R57).
  - RESULTS R38 (a) Remark KEY (λ is constant on a phase; docs/RESULTS.md l. 1825).
  - RESULTS R56: the setting line (κ, κwt_c, s_c; l. 2840) and (a) the facts (Aκ), (A0κ), (M1κ), (M2κ) (l. 2851), stated with proofs in
    P-N5-FBPOLY-box41 §0.3 (l. 88-97; sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301) and P-N5-FBRED-box44 §1.1 (l. 49-50; sha1
    11b15455f70d439c93a48d7e82fcdc14ef73854d). (M2κ) rests on RESULTS R15 (a) (Lemma A).
  - (SW) "every Even switch of N5 is to an edge of Iσ", as listed among RESULTS R72's landed premises (l. 3768-3769).
  - From P-N5-OFFMONO-box49 (UNREFEREED, under review with this addendum; nothing here is signed before it is): §0's setting and notation
    (U, Q, κ, κwt_c, next_t, par_t, off_s), Lemma OFFSET-MONO (§1), Corollary CHAIN-SUM and Corollary CHAIN-COUNT with its definitions of EXIT_x,
    CYC_c and x-piece (§2).
  - For §7's reading only: RESULTS R61 (b), (c), (f) and RESULTS R72.

## 0. Setting (every game)
As P-N5-OFFMONO §0: a phase P of N5 (τ and λ constant, RESULTS R38 (a)); a cycle node c of P; U := U_c := λ^{-1}(c), constant on P; Q := the Odd
vertices of out-degree ≥ 2; κ_t(z) = (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U, in the lexicographic order; next_t(z) := σ_t(z) for Even
z, σ̄_t(z) for Odd z; par_t and off_s as there. All transitions below are in-phase transitions t → t + 1 of P.
- Z_t(c) := c's honest cycle at t, as a sequence from c: (c, next_t(c), next_t²(c), …) up to the last vertex before the return to c.
- ZCH_c(J) := the transitions of a run J with Z_t(c) ≠ Z_{t+1}(c). CYC_c(J) as in P-N5-OFFMONO §2 (some x ∈ Q ∩ U ∖ {c} on an honest cycle at t).
  ZC_c(J) := ZCH_c(J) ∩ CYC_c(J).
- Fact (CYC-ID) (PROVED, elementary). For x ∈ U and a state t: x is on an honest cycle at t ⇔ x ∈ Z_t(c). Proof: the honest play from x follows
  next_t, a function, so x lies on at most one next_t-cycle, and if it lies on one, that cycle is the end of its play; the play's cycle node is
  λ_t(x) = c, which lies on that cycle; the next_t-cycle through c is Z_t(c). Conversely every vertex of Z_t(c) is on that cycle. □
- Fact (CYC-SHAPE) (PROVED, elementary). For v ∈ Z_t(c), v ≠ c: κ_t(v) = (0, s_c·ℓ) with 1 ≤ ℓ ≤ n − 1, ℓ the distance from v to c along Z_t(c).
  Proof: the honest play from v runs along Z_t(c) to c; c is the vertex of largest rank on its honest cycle (it is the cycle node; P-N5-FBPOLY
  §0.3's (A0κ) proof: c's own cycle "whose top is" c), so every vertex on the way has rank < rank(c) and wt_c = 0 there; by (Aκ) iterated and
  (A0κ), κ_t(v) = (0, s_c·ℓ). |Z_t(c)| ≤ n gives ℓ ≤ n − 1. □

## 1. Remark Z-CONST (PROVED, every game)
Statement. If Z_t(c) = Z_{t+1}(c) (as sequences), then for every x on it: κ_t(x) = κ_{t+1}(x); and for x ∈ Q on it, x ≠ c: par_t(x) = par_{t+1}(x),
and off_t(x; par(x)) = off_{t+1}(x; par(x)).
Proof. For x on the cycle, the honest play from x at t and at t + 1 is the same walk along the common cycle (next_t and next_{t+1} agree on its
vertices, because the sequence lists each vertex followed by its successor). κ_s(x) is a function of that walk at both times (c is the cycle node
at both, by R38 (a); (CYC-SHAPE) gives the value), so it is unchanged. par_s(x) is the first vertex of Q ∖ {x} on the walk before c, the same at
both times; call it p. p lies on the cycle or p = c, so κ_t(p) = κ_{t+1}(p) (first part, or (A0κ)), and the offset is unchanged. □

## 2. Corollary CHAIN-COUNT′ (PROVED, every game)
Fix a run J of consecutive in-phase transitions of P and the class c. EXIT_x as in P-N5-OFFMONO §2. An x-PIECE′ is a maximal run of consecutive
transitions of J, none in EXIT_x ∪ ZC_c(J) (so par(x) = p is constant on its states).
- Step A (non-negativity outside ZC_c). At a transition of J not in ZC_c, for every x ∈ Q ∩ U ∖ {c} and p := par_{t+1}(x): off_{t+1}(x; p) ⪰
  off_t(x; p). Proof: if x is on no honest cycle at t, Lemma OFFSET-MONO. Otherwise x ∈ Z_t(c) by (CYC-ID), so the transition is in CYC_c, hence
  (not in ZC_c) not in ZCH_c: Z_t(c) = Z_{t+1}(c), and Remark Z-CONST gives equality (par_t(x) = par_{t+1}(x) = p there). □
- Statement (sum form). For every q ∈ Q ∩ U ∖ {c}, the number of transitions of J that change κ(q) is at most
  |ZC_c(J)| + Σ_{x ∈ Q ∩ U ∖ {c}} (|EXIT_x| + Σ_{x-pieces′ π} (v_x(π) − 1)), v_x(π) := the number of distinct values of off(x; p) on the states of π.
- Statement (stated form). If v_x(π) ≤ D for every x and every x-piece′ π, that number is at most |ZC_c(J)| + Σ_x D·(|EXIT_x| + |ZC_c(J)| + 1).
Proof. Let t → t + 1 change κ(q) and not be in ZC_c (those are at most |ZC_c|). By Corollary CHAIN-SUM, κ_{t+1}(q) − κ_t(q) is the sum over the
levels x_i of q's (t+1)-chain of off_{t+1}(x_i; x_{i+1}) − off_t(x_i; x_{i+1}), with x_{i+1} = par_{t+1}(x_i); by Step A every term is ⪰ (0, 0) (here
used at every level, including levels on an honest cycle at t, which CHAIN-SUM alone leaves unsigned). The sum is not (0, 0), so some term is
≻ (0, 0): a level x with off_{t+1}(x; p) ≻ off_t(x; p), p := par_{t+1}(x). Charge the transition to (x, t). If par_t(x) ≠ p, t is in EXIT_x. Otherwise t
is in J ∖ (EXIT_x ∪ ZC_c), hence a transition of an x-piece′ π, and off(x; p) rises strictly from state t to state t + 1 of π. On π, off(x; p) is
non-decreasing (Step A at each of its transitions, p fixed), so it rises strictly at most v_x(π) − 1 times. Distinct transitions get distinct
charges, which gives the sum form. The x-pieces′ number at most |EXIT_x ∪ ZC_c| + 1 ≤ |EXIT_x| + |ZC_c| + 1; with v_x(π) ≤ D:
Σ_π (v_x(π) − 1) ≤ (D − 1)(|EXIT_x| + |ZC_c| + 1), and |EXIT_x| + (D − 1)(|EXIT_x| + |ZC_c| + 1) ≤ D·(|EXIT_x| + |ZC_c| + 1). □
- Remarks. (i) ZC_c ⊆ CYC_c, so CHAIN-COUNT′ implies P-N5-OFFMONO's CHAIN-COUNT, with x-pieces′ at least as long as x-pieces; the hypothesis "≤ D
  values on every piece" is then asked on longer pieces. (ii) ZC_c ⊆ ZCH_c, so KPOLY §8's form (cut at EXIT_x ∪ ZCH_c, count |ZCH_c|) also follows.
  (iii) The cut is needed only where c's cycle changes WITH an Odd choice vertex on it at t: a cycle change with no such vertex leaves every
  level of every chain off any honest cycle at t, so OFFSET-MONO applies at all of them.

## 3. Lemma ZCH-COUNT (PROVED, every game)
Definitions, for a transition t → t + 1 in ZCH_c: N := {v ∈ Z_{t+1}(c), v ≠ c : next_{t+1}(v) ≠ next_t(v)}. The transition is
- STRICT if some v ∈ N has κ_{t+1}(v) ≻ κ_t(v);
- TIE if it is not STRICT and N ≠ ∅;
- CEVEN if N = ∅ and c is Even; ODDC if N = ∅ and c is Odd.
TIE_c, ODDC_c := the numbers of TIE, ODDC transitions of P for the class c.
Statement. In a phase P, for the class c: |ZCH_c(P)| ≤ (n − 1)·|U_c| + TIE_c + ODDC_c. More finely: STRICT ≤ (n − 1)(|U_c| − 1), CEVEN ≤ n − 1;
at a TIE transition every vertex of N is Odd with κ_{t+1}(v) = κ_t(v); at an ODDC transition c ∈ Q and σ̄(c) changes.
Proof. The four kinds partition ZCH_c. If N = ∅, then next(c) changed (otherwise next_{t+1} = next_t on every vertex of Z_{t+1}(c), and tracing
from c gives Z_t(c) = Z_{t+1}(c)); so at an ODDC transition c is Odd with out-degree ≥ 2, c ∈ Q, and σ̄(c) changed.
- STRICT. Charge the transition to the first v ∈ N (in Z_{t+1}(c)'s order) with κ_{t+1}(v) ≻ κ_t(v). v ∈ Z_{t+1}(c), so κ_{t+1}(v) = (0, s_c·ℓ),
  1 ≤ ℓ ≤ n − 1 (CYC-SHAPE). By (M2κ), κ(v) is non-decreasing over the states of P, so each of these n − 1 values is the target of at most one strict
  rise of κ(v): v takes at most n − 1 charges. v ∈ U_c ∖ {c} (the cycle lies in U_c). Total ≤ (n − 1)(|U_c| − 1).
- Every Even v ∈ N is STRICT-qualifying. x′ := next_{t+1}(v) = σ_{t+1}(v) ≠ σ_t(v), so by (SW) (v, x′) ∈ Iσ_t: Ξ_t(x′) ▷ Ξ_t(σ_t v). x′ ∈ U_c (on
  Z_{t+1}(c); λ constant) and σ_t(v) = next_t(v) ∈ U_c ((Aκ), v ≠ c), so (M1κ) gives κ_t(x′) ≻ κ_t(σ_t v) (⊴ is total and (M1κ) is an equivalence, so
  strict ▷ is strict >). Then κ_{t+1}(v) = κwt_c(v) + κ_{t+1}(x′) ⪰ κwt_c(v) + κ_t(x′) ≻ κwt_c(v) + κ_t(σ_t v) = κ_t(v) ((Aκ) at t + 1 and t, (M2κ) at x′).
  Hence at a TIE transition N consists of Odd vertices, and each has κ_{t+1}(v) ⪯ κ_t(v) (not STRICT) and κ_{t+1}(v) ⪰ κ_t(v) ((M2κ)): equality.
- CEVEN. Let ψ_s := κ_s(next_s c) for the states s of P. next_s(c) lies on Z_s(c) or equals c, so ψ_s = (0, s_c·ℓ), 0 ≤ ℓ ≤ n − 1 (CYC-SHAPE; (A0κ)
  for ℓ = 0): ψ takes at most n values. ψ is non-decreasing on P: if next(c) is unchanged, by (M2κ) at next(c) ∈ U_c; if c (Even) switches to x′
  := σ_{t+1}(c), then (c, x′) ∈ Iσ_t by (SW), x′ ∈ U_c and σ_t(c) ∈ U_c (both on c's cycle at their times, or c), so (M1κ) gives κ_t(x′) ≻ ψ_t and
  ψ_{t+1} = κ_{t+1}(x′) ⪰ κ_t(x′) ≻ ψ_t ((M2κ)). At a CEVEN transition next(c) changes, so ψ rises strictly; a non-decreasing sequence with at most
  n values rises strictly at most n − 1 times. So CEVEN ≤ n − 1.
Summing: |ZCH_c| ≤ (n − 1)(|U_c| − 1) + TIE_c + (n − 1) + ODDC_c = (n − 1)|U_c| + TIE_c + ODDC_c. □
- Corollary (PROVED, from §2 and §3). In CHAIN-COUNT′ with J = the in-phase transitions of P: |ZC_c| ≤ |ZCH_c| ≤ (n − 1)|U_c| + TIE_c + ODDC_c. So
  the cut set costs a polynomial amount apart from TIE_c and ODDC_c.

## 4. DATA (not to sign; experiments/new/box48/zch.py; outputs experiments/new/box48/out/zch_*.txt)
zch.py runs N5 per phase and class and checks, each must be 0: ZC_V (Remark Z-CONST: κ or par changes on an unchanged cycle), PSI_V (ψ falls,
c Even), CEVEN_V (> n − 1 CEVEN transitions), STRICT_V (a vertex with > n − 1 STRICT charges), ZB_V (|ZCH_c| > (n − 1)|U_c| + TIE_c + ODDC_c), PM_V
(off(x; p) falls inside an x-piece′), CC_V (CHAIN-COUNT′ sum form), CCD_V (stated form, D := the largest v_x(π)), OTHER (a transition outside the
four kinds, or a TIE vertex that is Even or changes κ). Controls: MUT=1 (pieces not cut at ZC_c), MUT=2 (the opposite length sign −s_c), MUT=3
(pieces not cut at EXIT_x, offset taken to the current parent).
| sample | phases / transitions | ZCH (STRICT, TIE, CEVEN, ODDC) | CYC (at t) / ZC | κ(q)-changes | all checks | MUT=1 / MUT=2 / MUT=3 |
| --- | --- | --- | --- | --- | --- | --- |
| lib41 (experiments/new/box41/lib41.txt), n ≤ 34, S3 + 2 random, seed 7 (`2 7 --list ../box41/lib41.txt --nmax 34`) | 746 / 6,752 | 133 (50, 3, 79, 1); max per phase and class 6; max TIE 1, max ODDC 1 | 432 / 59 | 2,574 (max 51) | 0 | 0 / PM_V 688, PSI_V 124, OTHER 50 / PM_V 44 |
| nep90_n40, nep76_n40, long121_n40 (their starts), the three N5-NCONF §12 climbed games (n 40) and snap_n80_s62 (KPOLY §0) | 8 / 799 | 0 | 2 (on best_qpc_nep90_n40_s51) / 0 | 2,936 (max 72) | 0 | not run |
Files: out/zch_lib41_n34_MUT0.txt (the run), out/zch_lib41_n34_MUT1.txt, _MUT2.txt, _MUT3.txt (controls), out/zch_long7.txt (the seven long instances;
command list in experiments/new/box48/README.md). Reading of the data: MUT=1 does not bite on this corpus (no in-piece offset fall at a level on a
changing cycle occurs when ZC_c is not cut), so the ZC_c cut is not shown NECESSARY by the data; it is needed by the proof. MUT=2 confirms the
class sign matters (as for P-N5-OFFMONO's V_Kx); MUT=3 confirms the EXIT_x cut matters. The cycle part is small next to CYC_c: ZC 59 against
CYC 432 on lib41; on kw25_n32, CYC_c covers the whole 25-transition phase and ZCH_c = 0 (out/cyc_lib41_n34_k2.txt, KPOLY §8). TIE and ODDC are
rare here (3 and 1 in 6,752 transitions); the long instances have no cycle change at all, so they do not test §3.

## 5. Differences from N5-KPOLY §8 (READING; KPOLY §8 is a working document and is superseded by this addendum where they differ)
- KPOLY §8 cuts the pieces at EXIT_x ∪ ZCH_c and counts |ZCH_c|; this addendum cuts at EXIT_x ∪ ZC_c with ZC_c = ZCH_c ∩ CYC_c (§2 Remark (ii):
  KPOLY's form follows). KPOLY's statement “P-N5-OFFMONO's CHAIN-COUNT holds with CYC_c replaced by ZCH_c” is true but not implied by the
  original CHAIN-COUNT (ZCH_c ⊄ CYC_c in general: a cycle change with no Odd choice vertex on c's cycle is in ZCH_c and not in CYC_c); §2 holds both.
- KPOLY §8 defines TIE_c as the changes “at which every vertex v ≠ c of Z_{t+1}(c) with next_{t+1}(v) ≠ next_t(v) is Odd with κ_{t+1}(v) = κ_t(v)”,
  which read literally also holds when no such vertex exists; §3 requires N ≠ ∅ for TIE, so TIE, CEVEN and ODDC are disjoint.
- KPOLY §8's bound reads “ZCH_c ≤ (n − 1)·(|U_c| − 1) + n + TIE_c + ODDC_c”; §3's (n − 1)|U_c| + TIE_c + ODDC_c is one smaller (CEVEN ≤ n − 1, the
  bound KPOLY's proof already gives: “such transitions number ≤ n − 1 ≤ n”).
- KPOLY §8 proves Z-CONST's κ part in one line; §1 adds the routing-vertex and offset parts with their proof, and §0 states (CYC-ID) and
  (CYC-SHAPE), which KPOLY uses without statement.

## 6. OPEN (not to sign)
- TIE_c and ODDC_c per phase (successor 29's queue item 3 (a)). These are the cycle-change cases of RESULTS R61 (f)'s tie / cyc kinds (KPOLY §8's
  reading; not matched line by line here).
- EXIT_x per phase (L-SI successor 18) and the offset value count D on x-pieces′ (P-N5-OFFMONO §5; KPOLY §9 (a)).

## 7. READING (not to sign)
- With this addendum the cycle part of P-N5-OFFMONO's count is |ZC_c| ≤ (n − 1)|U_c| + TIE_c + ODDC_c instead of |CYC_c|, which on 𝒞^1O phases can
  be the whole phase (kw25_n32, §4). The route "phase count polynomial in n and k" now needs exactly: EXIT_x, D, TIE_c, ODDC_c, per phase.
- Against RESULTS R72 (RELAY-CHAIN (b), Σ_q ρ_q ≤ |Q_c|·(ROUTE_c + CYC_c + TOG_c)): R72's CYC_c is its own event kind; I have not matched it to ZC_c.
  If R72's CYC events at an unchanged cycle are empty by the same Z-CONST argument, R72 (b) would sharpen the same way; that is a reading only.

## 8. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the file and line named, at l-new 366fd235 (trunk a5bc809f merged at e77d3c79).
- RESULTS R38 (a), docs/RESULTS.md l. 1825: “λ_U is a function of τ alone, so on every run of states with τ constant it is constant”.
- RESULTS R56 setting, l. 2840: “s_c := +1 if Ω(c) is odd, −1 if even”; (a) l. 2851: “Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class”.
- RESULTS R72 premises, l. 3768-3769: “(SW): every Even switch of N5 is to an edge of Iσ”.
- P-N5-FBPOLY-box41 l. 93-94: “next_t(c_θ) lies on c_θ's own cycle (λ_t(c_θ) = c_θ, so c_θ is on its honest cycle), whose top is c_θ”; l. 95: “For
  valuations x, x′ with cycle node c_θ: x ⊴ x′ ⇔ κ(x) ≤ κ(x′)”; l. 97: “(M2κ) For z ∈ U and every in-phase transition t → t+1: κ_t(z) ≤ κ_{t+1}(z).
  Proof: R15 (a) and (M1κ)”.
- P-N5-FBRED-box44 l. 49-50: “κ_t(z) = κwt_c(z) + κ_t(next_t z)”.
- P-N5-OFFMONO-box49 §1: “Then off_{t+1}(q; p) ⪰ off_t(q; p).”; §2: “CYC_c := the transitions of J at which some x ∈ Q ∩ U ∖ {c} is on an honest cycle
  at t”; “EXIT_x := the transitions of J with par_t(x) ≠ par_{t+1}(x)”.
- N5-KPOLY-box49 §8 (l-new 331f0337): the three quotes in §5, and “Corollary CHAIN-COUNT′ (PROVED). P-N5-OFFMONO's CHAIN-COUNT holds with CYC_c
  replaced by ZCH_c”.
- Pins: N5-ssi-global.md 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e; P-N5-OFFMONO-box49.md d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4; P-N5-FBPOLY-box41.md
  de244dcd3592b04eca2080a0efe10a7c0b2e5301; P-N5-FBRED-box44.md 11b15455f70d439c93a48d7e82fcdc14ef73854d; zch.py and its outputs: sha1 in the push message.
- Script: `python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-OFFMONO-add-box49.md 366fd235:docs/RESULTS.md 366fd235:docs/new/P-N5-FBPOLY-box41.md
  366fd235:docs/new/P-N5-FBRED-box44.md 366fd235:docs/new/P-N5-OFFMONO-box49.md 331f0337:docs/new/N5-KPOLY-box49.md` (output
  experiments/new/box48/out/quotecheck_offmono_add.txt).
