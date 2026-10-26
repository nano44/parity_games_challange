# Addendum 2 P-N5-OFFMONO-add2 (box 49): the κ-changes of a class that touch the path-free values F number at most 2(n − 1)(|U_c| − 1) per phase (Lemma FT-COUNT); outside them κ is constant on the path-free vertices, so on c's cycle every offset is constant (Remark FT-CONST); hence CHAIN-COUNT′ holds with the cut CYC_c ∩ ZCH_c ∩ FT_c, of size at most 2(n − 1)(|U_c| − 1), with no TIE or ODDC term (Corollary CHAIN-COUNT″) — every game; plus a code-level lemma on S1's tie-breaks (PF-CHOICE, TIE-CHARGE)
L-NEW successor 29 (Opus 5.5), D14 / D18, Lead reading L40. Lead's word of 18:08Z (message to L-NEW): "KPOLY §11: freeze it as add2,
docs/new/P-N5-OFFMONO-add2-box49.md. The referees should review the strongest form together with OFFMONO." Written 2026-10-26 from 18:17Z (date -u).
FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-KPOLY-box49.md §11 (l-new d60dcc86). This addendum governs. It extends docs/new/P-N5-OFFMONO-box49.md (sha1
d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4) and docs/new/P-N5-OFFMONO-add-box49.md (sha1 5911aba8fc4e968187523c27b4f48cdc55433b3f), neither edited.
Tools: experiments/new/box48/ft.py, tie.py, tieclimb.py; outputs experiments/new/box48/out/ft_*.txt, tie_*.txt, tie2_*.txt, tieclimb/.
Labels: PROVED (L-NEW 29, unrefereed) / PROVED, CODE-LEVEL (against si.py; §4) / OPEN / DATA / READING. Not a TARGET.md claim; no running-time
bound; G-N5-TIME stays open.
What this is and is not, plainly:
- With add1, the cut set of CHAIN-COUNT had a polynomial bound only up to TIE_c + ODDC_c. Here the cut set is bounded unconditionally, by an
  elementary count (§1-§3); no tie-break of SPEC S1 is used there. TIE_c is also bounded (§4, code-level); ODDC_c is not, and is not needed.
- It does not bound EXIT_x or the offset value count D (L-SI successor 18's side). A phase count polynomial in n and k on this route still
  needs both (P-N5-OFFMONO §5).

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma FT-COUNT | PROVED (to sign) |
| §2 | Remark FT-CONST | PROVED (to sign) |
| §3 | Corollary CHAIN-COUNT″ (sum form and D form) | PROVED (to sign) |
| §4 | Lemma PF-CHOICE, Corollary TIE-CHARGE | PROVED, CODE-LEVEL (to sign against si.py; separate from §1-§3, which do not use it) |
| §5 | what supersedes what in add1 | READING (not to sign) |
| §6 | data | DATA (not to sign) |
| §7 | open | OPEN (not to sign) |
- Premises (LANDED unless marked):
  - RESULTS R38 (a) Remark KEY (λ constant on a phase; docs/RESULTS.md l. 1825).
  - RESULTS R56: the setting line (κ, κwt_c, s_c; l. 2840) and (a) the facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ) (l. 2851), stated with proofs in
    P-N5-FBPOLY-box41 §0.3 (l. 88-100; sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301). (INJ): the signed weight is injective on vertex sets.
  - (SW), as listed among RESULTS R72's landed premises (l. 3768-3769) (§4 only).
  - UNREFEREED, under review with this addendum: P-N5-OFFMONO-box49 §0-§2 (setting; Lemma OFFSET-MONO; Corollary CHAIN-SUM; EXIT_x, CYC_c);
    P-N5-OFFMONO-add-box49 §0-§3 ((CYC-ID), (CYC-SHAPE); Remark Z-CONST; Corollary CHAIN-COUNT′ and its Step A; ZCH_c; the Even-switch step of
    Lemma ZCH-COUNT's proof, used in §4).
  - §4 only: SPEC docs/new/N5-ssi-global.md S1 (sha1 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e; l. 33-44) and its reference implementation
    experiments/si/si.py Engine.evaluate (sha1 e688b96327b7fd2770126e20bb00e459c1f18869; l. 78-205), which SPEC S1 names as exact.

## 0. Setting (every game)
As P-N5-OFFMONO §0 and add1 §0: a phase P, a cycle node c, U_c, Q, κ, s_c, next_t, par_t, off_s, Z_t(c), ZCH_c, CYC_c; in-phase transitions only.
- F := {(0, s_c·ℓ) : 1 ≤ ℓ ≤ n − 1}. A_t := {z ∈ U_c ∖ {c} : P(Ξ_t z) = ∅}, the PATH-FREE vertices of the class at t.
- Fact (A-F) (PROVED, elementary). For z ∈ U_c ∖ {c}: z ∈ A_t ⇔ κ_t(z) ∈ F. Proof: by (INJ), the first component M_t(z) is 0 iff P(Ξ_t z) = ∅;
  then κ_t(z) = (0, s_c·ℓ) with ℓ the length to c, ℓ ≥ 1 since z ≠ c, ℓ ≤ n − 1 since the play to c is simple. □
- FT_c := the in-phase transitions t → t + 1 of P at which some z ∈ U_c ∖ {c} has κ_t(z) ≠ κ_{t+1}(z) with κ_t(z) ∈ F or κ_{t+1}(z) ∈ F (an
  F-TOUCHING change).

## 1. Lemma FT-COUNT (PROVED, every game)
Statement. |FT_c| ≤ 2(n − 1)(|U_c| − 1) for every phase P and class c.
Proof. Charge each transition of FT_c to one z ∈ U_c ∖ {c} with an F-touching change there. For fixed z, κ(z) is non-decreasing over the states
of P ((M2κ)). So every value v ∈ F is the source of at most one change of κ(z) (after it leaves v, κ(z) ≻ v forever) and the target of at most
one (after it reaches v from below, it is never below v again). Hence z takes at most 2|F| = 2(n − 1) charges; there are |U_c| − 1 choices
of z. □

## 2. Remark FT-CONST (PROVED, every game)
Statement. At an in-phase transition t → t + 1 not in FT_c: A_t = A_{t+1}; κ_t(z) = κ_{t+1}(z) for every z ∈ A_t ∪ {c}; and for every x ∈ Z_t(c),
x ≠ c, and p := par_{t+1}(x): off_{t+1}(x; p) = off_t(x; p).
Proof. If z ∈ A_t, then κ_t(z) ∈ F (A-F), so, the transition not being F-touching at z, κ_{t+1}(z) = κ_t(z) ∈ F and z ∈ A_{t+1}; the converse
in the same way. κ(c) = (0, 0) at both states ((A0κ)). For x ∈ Z_t(c), x ≠ c: x ∈ A_t (add1 (CYC-SHAPE)), so x ∈ A_{t+1}. p lies on x's honest
play at t + 1 before c, or p = c; every vertex of that play before c is path-free (P of a vertex on the play is the part of P(Ξ_{t+1} x) after
it, which is empty), so p ∈ A_{t+1} ∪ {c} = A_t ∪ {c}. Both κ(x) and κ(p) are unchanged, so is their difference. □
No tie-break of SPEC S1 is used: the remark does not say that next is unchanged on A_t (that is §4's code-level corollary).

## 3. Corollary CHAIN-COUNT″ (PROVED, every game)
Fix a run J of consecutive in-phase transitions of P and the class c. ZC″_c(J) := CYC_c(J) ∩ ZCH_c(J) ∩ FT_c. An x-PIECE″ is a maximal run of
consecutive transitions of J, none in EXIT_x ∪ ZC″_c(J); v_x(π) := the number of distinct values of off(x; p) on the states of π.
- Step A″. At a transition of J not in ZC″_c, for every x ∈ Q ∩ U_c ∖ {c} and p := par_{t+1}(x): off_{t+1}(x; p) ⪰ off_t(x; p). Proof: if x is
  on no honest cycle at t, Lemma OFFSET-MONO. Otherwise x ∈ Z_t(c) (add1 (CYC-ID)), so the transition is in CYC_c; not being in ZC″_c, it is
  not in ZCH_c (then add1's Remark Z-CONST gives equality) or not in FT_c (then Remark FT-CONST gives equality). □
- Statement (sum form). For every q ∈ Q ∩ U_c ∖ {c}, the transitions of J that change κ(q) number at most
  |ZC″_c(J)| + Σ_{x ∈ Q ∩ U_c ∖ {c}} (|EXIT_x| + Σ_{x-pieces″ π} (v_x(π) − 1)).
- Statement (D form). If v_x(π) ≤ D for every x and π: at most |ZC″_c(J)| + Σ_x D·(|EXIT_x| + |ZC″_c(J)| + 1).
- And |ZC″_c(J)| ≤ min(|CYC_c ∩ ZCH_c|, |FT_c|) ≤ 2(n − 1)(|U_c| − 1) (Lemma FT-COUNT).
Proof. add1 §2's proof word for word, with ZC_c replaced by ZC″_c and Step A by Step A″. □
So per phase and class, for every q ∈ Q ∩ U_c ∖ {c}: κ(q)-changes ≤ 2(n − 1)(|U_c| − 1) + Σ_x D·(|EXIT_x| + 2(n − 1)(|U_c| − 1) + 1).

## 4. Code-level: Lemma PF-CHOICE and Corollary TIE-CHARGE (PROVED against si.py; §1-§3 do not use this section)
SPEC S1 defines σ̄ as “Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate (lines 78-205)” (SPEC l. 33). The proof reads that code
(si.py at sha1 e688b963…; line numbers of that file). v denotes the cycle node being processed (our c), R the alive vertices reaching it (l. 110).
- Lemma PF-CHOICE. Let t be a state of P and x ∈ A_t an Odd vertex. Then σ̄_t(x) is the minimiser, over y ∈ succ(x) ∩ (A_t ∪ {c}), of
  (κ_t(y), tb_t(y)) in lexicographic order, where tb_t(y) := (y) (y's index) if Ω(c) is even, and tb_t(y) := the sequence of indices of the
  vertices of y's honest play at t from c's side (empty for y = c) if Ω(c) is odd.
  Proof.
  - (a) R = U_c: every x ∈ R receives the valuation (v, path[x], dist[x]) (l. 197), so R ⊆ U_c, and U_c ⊆ R since a vertex's cycle node is set
    only there. path[x] is P(Ξ_t x) as a bit set, dist[x] is ℓ. A path-free x has rank(x) < rank(c): a vertex u of larger rank receives its
    own bit (Even-liked u: reach(v, u) (l. 137) excludes u, so u ∉ M and path[u] |= bit(u), l. 140; Odd-liked u: u ∈ M = reach(u, v), l. 145-147).
  - (b) After the restriction loop (l. 135-150), the successors hs[x] of a path-free x are exactly succ(x) ∩ (A_t ∪ {c}) ∩ R, in increasing index
    order (hs[x] is filtered from gs[x] = succ[x], l. 116; restrict (l. 129-134) deletes entries, keeping the order).
    - Even-liked u (l. 136-143): x is path-free, so x ∈ M (else path[x] gets bit u). restrict(x, M) deletes exactly the edges to vertices outside
      M, and those vertices get bit u (l. 138-140). A path-free y is in M, so its edge is kept. restrict(u, M) touches u ≠ x only.
    - Odd-liked u (l. 144-149): x ∉ M (else path[x] gets bit u). restrict is applied to q ∈ M ∖ {u} only, so x's edges are untouched. An edge
      x → y with y ∈ M still present at this step would put x into M, because reach(u, v) (l. 120-128) runs over predecessors and excludes only v
      (and x ≠ v). So every edge from x to a vertex that gets bit u here is already deleted.
    - So every edge from x to a vertex with a non-empty path set is deleted by the end, and no edge to a path-free vertex or to c is.
  - (c) Ω(c) even (l. 152-171): longest(x) scans hs[x] in order and keeps the first strict maximum (l. 165); dist = ℓ. So σ̄(x) is the least-index
    y ∈ hs[x] maximising ℓ(y), i.e. minimising κ(y) = (0, −ℓ(y)) (s_c = −1), ties by index.
  - (d) Ω(c) odd (l. 172-181): BFS from v over hp in layers; a vertex is discovered by the first vertex of the current layer, in layer order,
    that it points to (l. 177-179, "if y not in dist"), and that vertex becomes its choice. hp[·] is in increasing index order (built at l. 90
    over increasing v, filtered and restricted keeping the order). A path-free vertex points only to path-free vertices or c in the
    restricted graph ((b)), so path-free vertices are discovered only from path-free vertices or c, and within a layer they are ordered by
    (position of the discovering vertex, index). By induction on the layer, that order among path-free vertices is the lexicographic order
    of tb. The discovering vertex of x is the earliest-ordered y ∈ hs[x] with dist(y) = dist(x) − 1, i.e. the minimiser of (κ(y), tb(y))
    (κ(y) = (0, ℓ(y)), s_c = +1). □
- Corollary TIE-CHARGE. At an in-phase transition not in FT_c, next_{t+1}(z) = next_t(z) for every z ∈ A_t. Hence every STRICT and every TIE
  transition of add1 §3 lies in FT_c, and STRICT_c + TIE_c ≤ 2(n − 1)(|U_c| − 1).
  Proof. By FT-CONST, A_t = A_{t+1} and κ is unchanged on A_t ∪ {c}. An Even z ∈ A_t that switches has κ_{t+1}(z) ≻ κ_t(z) (add1 §3, the Even
  case: (SW), (M1κ), (Aκ), (M2κ)), an F-touching change; so Even vertices of A_t keep next. For Odd z ∈ A_t, induction on ℓ(z): the κ-minimal
  options of z have ℓ = ℓ(z) − 1 (c odd) or are the maximal-ℓ options (c even, where tb is the index); for c odd their tb is fixed by next on
  vertices of smaller ℓ (induction hypothesis), and for c even tb does not depend on the state. PF-CHOICE then gives the same minimiser at t
  and t + 1. A STRICT or TIE transition changes next at some vertex of Z_{t+1}(c) ∖ {c} ⊆ A_{t+1}, or (STRICT) changes κ there, so it is in FT_c. □
- ODDC_c is not covered: the cycle node's own Odd choice (S1 (v), si.py l. 182-195) is the first cycle found by a stack search over ALL alive
  vertices of rank < rank(c), including vertices of U_c with non-empty path sets, whose Even switches are not F-touching. ODDC_c stays OPEN;
  §3 does not need it.

## 5. What supersedes what (READING)
- add1's Remark Z-CONST and Corollary CHAIN-COUNT′ STAY (Z-CONST is used in Step A″; CHAIN-COUNT′ is a corollary of CHAIN-COUNT″, since
  ZC″_c ⊆ ZC_c).
- add1's Lemma ZCH-COUNT stays true, but its TIE_c and ODDC_c terms are no longer needed on this route: §3 bounds the cut ZC″_c by
  2(n − 1)(|U_c| − 1) directly (Lemma FT-COUNT). §4 bounds STRICT_c + TIE_c; ODDC_c is not bounded anywhere.
- N5-KPOLY §11 is superseded by this addendum.

## 6. DATA (not to sign; experiments/new/box48/)
- ft.py (FT-COUNT: FTB_V; FT-CONST: OC_V; CHAIN-COUNT″: PM_V, CC_V, CCD_V). lib41 (experiments/new/box41/lib41.txt) n ≤ 34, S3 + 2 random,
  seed 7, 746 phases, 6,752 transitions: FT 1,102 (largest per phase and class 29); CYC 432; cut CYC ∩ ZCH ∩ FT (MUT=5, the stated ZC″) 42
  transitions, cut CYC ∩ FT (MUT=0, a larger cut) 270, against add1's ZC 59; every check 0 in both (out/ft_lib41_n34_MUT5.txt, _MUT0.txt). The
  seven long instances of add1 §4 (MUT=0 and MUT=5): FT ≤ 6, ZC″ 0, all checks 0 (out/ft_long7_MUT5.txt, out/ft_long7.txt).
- Controls for the cut: MUT=1 (no cut) and MUT=4 (the first cut transition of each phase and class dropped) do NOT bite on this corpus
  (out/ft_lib41_n34_MUT1.txt, _MUT4.txt), as add1's MUT=1. The cut is needed by the proof; the data do not show it necessary.
- tie.py (PF-CHOICE: CHAR_V; TIE-CHARGE: FT_V; FT-COUNT: FTB_V). lib41 as above: 2,523 characterisation checks, CHAR_V 0; 1,102 transitions with a
  change of A or of next on A, all F-touching (FT_V 0); FTB_V 0 (out/tie2_lib41_n34_k2.txt). The tie-break controls bite: MUT=1 (index tie-break
  for both parities) CHAR_V 1, MUT=2 (path-sequence tie-break for both) 55, MUT=3 (reversed index) 182 (out/tie2_lib41_MUT{1,2,3}.txt). The TIE
  and ODDC events (out/tie_lib41_n34_k2.txt): 3 TIEs (klcount_n16, n18_base, n18_lvl; c odd, the old option's κ strictly up, the new option
  tied at t) and 1 ODDC (u3ev_n16; the old option's M rises to 8192).
- tieclimb.py: 4 climbs × 3,000 steps from u3ev_n16 (objective ODDC_c) and klcount_n16 (TIE_c), n ≤ 24: best ODDC_c 1 and TIE_c 1 per phase and
  class; 292,764 characterisation checks on climbed games, CHAR_V, FT_V, FTB_V 0 (out/tieclimb/).

## 7. OPEN (not to sign)
- EXIT_x per phase and the offset value count D on x-pieces″ (L-SI successor 18's side; P-N5-OFFMONO §5).
- ODDC_c per phase (not needed by §3).

## 8. Quotes and pins (checked by script)
Every quote below, set in curly double quotes, is verbatim from the file and line named, at l-new 278616c6.
- SPEC docs/new/N5-ssi-global.md l. 33: “σ̄ is computed by Vöge-Jurdziński's procedure exactly as si.py Engine.evaluate”; l. 41: “first strict
  maximum wins”; l. 42: “first discovery sets Odd's choice”; l. 44: “Successor and predecessor lists are in increasing index order.”
- si.py l. 136: “if self.par[u] == 0:                 # Even likes u: Odd avoids it where it can”; l. 137: “M = reach(v, u)”; l. 145: “M = reach(u, v)”;
  l. 165: “if d > best:”; l. 172: “else:                                    # odd cycle: shortest path (BFS over preds from v)”; l. 178: “if y not in dist:”;
  l. 197: “val[x] = (v, path[x], dist[x])”.
- RESULTS l. 1825: “λ_U is a function of τ alone, so on every run of states with τ constant it is constant”; l. 2840: “s_c := +1 if Ω(c) is odd,
  −1 if even”; l. 2851: “Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class”; l. 3768-3769: “(SW): every Even switch of N5 is to an edge
  of Iσ”.
- P-N5-FBPOLY-box41 l. 97: “(M2κ) For z ∈ U and every in-phase transition t → t+1: κ_t(z) ≤ κ_{t+1}(z).”; l. 98: “The signed weight is injective
  on vertex sets”.
- P-N5-OFFMONO-add-box49: “Remark Z-CONST (PROVED, every game)”; “Corollary CHAIN-COUNT′ (PROVED, every game)”; “Lemma ZCH-COUNT (PROVED, every
  game)”; “Fact (CYC-ID) (PROVED, elementary)”; “Fact (CYC-SHAPE) (PROVED, elementary)”.
- Pins: N5-ssi-global.md 66fde9ef1726602fc0a52ca8d6d6fe8cbbcf110e; si.py e688b96327b7fd2770126e20bb00e459c1f18869; P-N5-OFFMONO-box49.md
  d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4; P-N5-OFFMONO-add-box49.md 5911aba8fc4e968187523c27b4f48cdc55433b3f; P-N5-FBPOLY-box41.md
  de244dcd3592b04eca2080a0efe10a7c0b2e5301; scripts and outputs: sha1 in the push message.
- Script: `python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-OFFMONO-add2-box49.md 278616c6:docs/new/N5-ssi-global.md
  278616c6:experiments/si/si.py 278616c6:docs/RESULTS.md 278616c6:docs/new/P-N5-FBPOLY-box41.md 278616c6:docs/new/P-N5-OFFMONO-add-box49.md`
  (output experiments/new/box48/out/quotecheck_offmono_add2.txt).
