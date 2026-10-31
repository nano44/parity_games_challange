# N5-TIE (box 106): the TIE face inside a W-constant interval reduces to a monotone lexicographic potential. Lemma ODD-NORET (PROVED, lane): when X's W-cycle node is odd, X never re-enters a target inside a W-constant interval (IDX-MONO makes index(σ(X)) non-increasing). Lemma KEY-MON (PROVED, lane): when it is even, every T54 key is lexicographically non-increasing through the interval and strictly decreases at each switch (LEX-BFS, induction on W-length). So tie returns inside an interval are ≤ the key decreases of X (TIE-RED). The remaining statement is KEYCH-POLY (CONJECTURE): key decreases per vertex per W-constant interval are polynomial
L-NEW successor 40 (Opus 5.5), D14 / D18, Lead reading L40. Lead 01:31Z: «BOX 106 = the TIE face, proof side … bound TRET_F(X), or the
Iσ-toggles at fixed W, per W-constant interval … Look for a potential that the tie-break moves monotonically while W stays fixed: e.g. a
lexicographic key over the W-tight subgraph … Outcome: PROVED (lane) …; or DEAD …; or a reduction of the TIE face to a named smaller
statement.» Written 2026-10-31 01:32Z-01:4xZ (date -u). Working note, unrefereed. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Premises (quoted as P-N5-SETTLE §2 quotes them; L-LIT T54 §4.1-§4.2, «PROVED, L-LIT, elementary, modulo Claim RG»)
- Claim RG′ is signed in P-N5-SETTLE. Everything below inherits the SETTLE reading that IDX-MONO and LEX-BFS hold at every S4a step of a
  W-run with «W-tight» = W_(k+1)-tight.
- IDX-MONO: «If Even v ≠ c := λ_W(v) and Ω(c) is odd, then σ_{k+1}(v) = the smallest-index W-tight edge of {σ_k(v)} ∪ Iσ_k(v).»
- LEX-BFS: «If Ω(c) is even and v ≠ c is Even, then σ_{k+1}(v) = argmin over the W-tight arena edges y of key_{σ_{k+1}}(y).»
  - key_σ(x) := (x_{ℓ−1}, …, x_1, x_0), where x = x_0 → … → x_ℓ = c is the (σ, τ)-path. Keys are compared lexicographically.
- A W-CONSTANT INTERVAL I of a W-run F is a maximal run of states of F with W unchanged (R95). In I, W, λ_W and the W-lengths ℓ(x) are
  fixed, and so is the W-tight edge set.
- Tools: experiments/new/box105/keymon.py (+ runkey.sh → keymon_corpus.txt) and o1.py's TIECLASS line (+ runo1.sh → o1_corpus.txt).
  Pin: new/check.sh «box 106 TIE».

## 1. Lemma ODD-NORET (PROVED, lane; premise IDX-MONO)
- Statement. Let I be a W-constant interval and X an Even vertex with λ_W(X) = c ≠ X, c odd. Along I, index(σ_t(X)) is non-increasing
  and strictly decreases at each switch of X. So X switches at most deg(X) − 1 times in I, and never re-enters a target inside I.
- Proof.
  - W_t is the valuation of σ_t's own play, so W_t(X) = X ⊕ W_t(σ_t(X)): σ_t(X) is W_t-tight.
  - In I, W_(t+1) = W_t, so σ_t(X) is W_(t+1)-tight and lies in the arena {σ_t(X)} ∪ Iσ_t(X).
  - IDX-MONO picks the least-index tight arena edge, so index(σ_(t+1)(X)) ≤ index(σ_t(X)), with equality iff no switch. □
- DATA: ODDUP 0 on the corpus. Of the 88 tie returns classified by o1.py (TIECLASS), 0 have an odd W-cycle node.
  - The o1.py re-run of this box counts 10,190 returns and 88 tie returns, against box 105's 10,261 / 82. Coverage depends on which large
    runs finish under the 300 s cap. O1W = LEAVE_TIE = BOTH_TIE holds in both runs.

## 2. Lemma KEY-MON (PROVED, lane; premise LEX-BFS)
- Statement. Let I be a W-constant interval and x any vertex with λ_W(x) = c ≠ x, c even. Along I, key_t(x) is lexicographically
  non-increasing. If x is Even and switches at t → t + 1, then key_(t+1)(x) < key_t(x).
- Proof, by induction on ℓ(x), the W-length (fixed in I).
  - A W-tight edge x → y has ℓ(y) = ℓ(x) − 1. Paths to c inside the tight subgraph are layered, and key(x) = key(next(x)) followed by x,
    all of length ℓ(x).
  - ℓ = 0: x = c, the key is empty.
  - Odd x: next(x) = τ(x), fixed in a W-run, so key_(t+1)(x) = key_(t+1)(τ x)·x ≤ key_t(τ x)·x = key_t(x) by induction.
  - Even x: σ_t(x) is W-tight (as in §1) and in the arena. By LEX-BFS, key_(t+1)(x) = min over tight arena y of key_(t+1)(y)·x
    ≤ key_(t+1)(σ_t x)·x ≤ key_t(σ_t x)·x = key_t(x).
    - Distinct y give keys that differ in their last entry, so the minimiser is unique.
    - If x switches, the minimiser is not σ_t(x), and the first inequality is strict. □
- Lexicographic order of equal-length tuples is decided by the first differing entry, which justifies «·x preserves ≤ and <».
- DATA (keymon.py): KEYUP 0 (no key ever rises inside an interval) and SWNOTDOWN 0 (every switch strictly lowers the key).
  - Scope: 1,111 of the 1,137 runs (box 50b's corpus + 5 pins); 26 large runs hit the 300 s cap and are NOT checked. 35 W-constant
    intervals with switches.
  - u23sw64_n32: one interval of length 8, 31 tie returns, the max key changes of one vertex 8, the max switches of one Even vertex 6.

## 3. Corollary TIE-RED (PROVED, lane) and the remaining statement
- For a W-constant interval I and Even X, let KEYCH_I(X) be the number of strict decreases of key(X) in I.
  - If λ_W(X) is odd: tie returns inside I = 0 (ODD-NORET).
  - If λ_W(X) is even: tie returns of X inside I ≤ switches of X in I ≤ KEYCH_I(X) (KEY-MON).
  - Summing over the ≤ WCH_F + 1 W-constant intervals of F: in-interval tie returns of X ≤ Σ_I KEYCH_I(X).
- CONJECTURE KEYCH-POLY: KEYCH_I(x) ≤ p(n) for every vertex x and every W-constant interval I.
  - DATA: max 8 (u23sw64_n32, = the interval length).
  - Why it is not proved: key(x) lives in the set of lexicographically ordered paths of the layered tight DAG, which can be exponentially
    large. A key decrease at x needs a decrease below it or an arena INSERTION (an Iσ gain) that lowers the min. Each insertion is a
    Ξ-overtake, so a bound on insertions is again a Ξ-count at fixed W.
  - The potential is monotone. The open part is its LENGTH.
- Not covered: tie returns whose window crosses a W-change elsewhere (W(X) fixed at the leave and re-entry, W changing somewhere in
  between): 10 of 88 corpus tie returns (TIECLASS «Wchanges»; 4 of them with X its own W-cycle node).
- So the TIE face is reduced to KEYCH-POLY inside intervals plus these cross-interval tie returns. This is a named smaller statement: it
  is monotone, and lexicographic over a fixed layered DAG. It is not a bound.
- READING (D18): KEY-MON says the (σ, τ)-tree inside a W-constant interval with even cycle node evolves as a lexicographic BFS tree under
  monotone edge insertions. The question «how many times can a lex-BFS tree change under insertions» is a dynamic-graph-algorithms question
  (incremental lex-BFS / lex-min path trees). No source opened, no claim imported.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box105/keymon.py, runkey.sh, keymon_corpus.txt; o1.py TIECLASS line (o1_corpus.txt re-run);
  new/check.sh «box 106 TIE». SHA: see the commit.
- FINDINGS:
  - PROVED (lane): ODD-NORET (odd W-cycle node: no return inside a W-constant interval).
  - PROVED (lane): KEY-MON (even: T54 keys non-increasing, strictly at switches).
  - PROVED (lane): TIE-RED (in-interval tie returns ≤ key decreases).
  - DATA: KEYUP 0, SWNOTDOWN 0, ODDUP 0; all 88 tie returns have an even cycle node; 78 lie inside one interval.
  - CONJECTURE: KEYCH-POLY. Cross-interval tie returns (10 / 88) are open.
- NEEDS: Lead: L-RED target «many key decreases of one vertex in one W-constant interval» (KEYCH super-linear), e.g. u23sw64_n32's interval
  scaled.
