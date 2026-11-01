# Box 127 N5-PARAM: XI-CH inside a W-run vs breakpoints of parametric shortest paths (D18 bridge)
L-NEW successor 45, 2026-11-01 06:2x-06:4xZ (date -u). Lead box 127. Code: experiments/new/box127/ (expir.py, runcorp.sh, pincheck.sh).
Labels: PROVED (lane) = proved here, not refereed; DATA; READING; DEAD (with instance); CONJECTURE.

## 0. Question
Inside a W-run (RESULTS R89: one τ-stretch, no S4c fallback, λ_W constant) σ only improves and Ξ_k = Odd's one-player optimum in G_σk.
Can XI-CH (changes of Ξ_k(x)) be cast as a breakpoint count of a monotone parametric one-player problem, and what does the theory give?

## 1. Sources opened (nothing else is cited)
- [GR] K. Gajjar, J. Radhakrishnan, «Parametric Shortest Paths in Planar Graphs», arXiv 1811.05115 (pdf sha256 79208b4f5fe9aa56…).
  Used: §1 Theorem 1 (planar n^Ω(log n)) and its paragraph: Carstensen ϕ(n, ∞) = n^Ω(log n); Mulmuley-Shah ϕ(n, O((log n)^3)) =
  n^Ω(log n); Gusfield's matching upper bound n^(log n + O(1)) (as presented in Carstensen's thesis p. 100, per [GR]);
  Proposition 5 (alternation-free = expiration property, Nikolova); Theorem 6 (alternation-free sequences, f(n, 2^k) ≥ n^k) and the
  recursion f(n, 2^k − 1) ≤ 2n·f(n, 2^(k−1) − 1) (p. 5-6); proof of Theorem 2 (§4: middle-vertex split + Davenport-Schinzel).
- [CFLY] Chakraborty, Fischer, Lachish, Yuster, «Two-phase algorithms for the parametric shortest path problem», STACS 2010,
  arXiv 1001.3749 (pdf sha256 45398534db333c8b…), §1 (l. 208-219 of the text dump): Carstensen's n^Ω(log n) for a_e + x b_e, a_e,
  b_e > 0; the n^O(log n) upper bound; the simpler proof of Nikolova-Kelner-Brand-Mitzenmacher.
- NOT OPENED (paywalled / not found; cited only through [GR], [CFLY]): Carstensen, Math. Programming 26 (1983) 64-75,
  doi 10.1007/BF02591893 (Springer 429) and her 1983 Michigan thesis; Mulmuley-Shah, JCSS 63 (2001), doi 10.1006/jcss.2001.1766
  (landing page only); Gusfield 1980 thesis / JACM 1983; Nikolova 2009 thesis.

## 2. What drives the known upper bound (READING of [GR], made exact in §3)
[GR] p. 5-6: the n^O(log n) bound uses ONE combinatorial fact about the sequence p_1, …, p_T of envelope paths: alternation-free
(Prop. 5): if u, v lie on p_i, p_j, p_k (i < j < k) and p_i[u:v] = p_k[u:v] = q, then p_j[u:v] = q. Costs, λ and linearity enter only
through this fact. So the bridge to test is not «is the family affine» but «is the Ξ-play sequence alternation-free».

## 3. PROVED (lane)
- Lemma AF-QP. Let p_1, …, p_T be simple s-t paths in an n-vertex digraph, consecutive entries distinct, each with ≤ ℓ edges, and
  alternation-free in the sense of §2 (all pairs u, v). Then T ≤ (2n)^⌈log2 ℓ⌉.
  Proof. Taking (u, v) = (s, t): no path recurs after it is left, so T = the number of distinct paths. Let F(ℓ) be the maximum T. F(1)
  = 1 (one s-t edge). For ℓ ≥ 2 give each p_i its middle vertex m(p_i) at position ⌈|p_i|/2⌉ (prefix and suffix ≤ ⌈ℓ/2⌉ edges). Fix a
  vertex w and the subsequence of paths with m = w. Its prefixes s..w, with consecutive repeats merged, are simple s-w paths with ≤
  ⌈ℓ/2⌉ edges and inherit alternation-freeness (a triple of them is a triple of the p's with both u, v on the prefix part), so they
  take ≤ F(⌈ℓ/2⌉) distinct values with no recurrence, hence change ≤ F(⌈ℓ/2⌉) − 1 times along the subsequence; the same for suffixes.
  Consecutive members of the subsequence are distinct paths, so each step changes the prefix or the suffix: the subsequence has ≤
  2F(⌈ℓ/2⌉) − 1 members. Summing over w: F(ℓ) ≤ 2n·F(⌈ℓ/2⌉), and F(ℓ) ≤ (2n)^⌈log2 ℓ⌉. ∎ ([GR]'s sketch, completed.)
- Corollary AF-XI. Let PI_k(x) := the path part of the (σ_k, σ̄_k)-play from x up to the first visit of the cycle node of Ξ_k(x),
  followed by a virtual terminal T (so ℓ ≤ n). Ξ_k(x) = (c, P, ℓ) is a function of PI_k(x) (c its last real vertex, P and ℓ read
  off it; asserted by expir.py at every state). If, inside a W-run F, the sequence (PI_k(x))_k were alternation-free for every x,
  then ΞCH_F(x) ≤ (2n)^⌈log2(n+1)⌉ for every x: a quasi-polynomial XI-CH bound per W-run.
- Fact VAL-NORET (standard SI monotonicity, SPEC «Termination»: Ξ_{σ'} ⊵ Ξ_σ when σ' applies improving switches). Inside any run
  segment where σ moves by improving switches, Ξ_k(x) never returns to a value it has left. So the (u, v) = (x, T) case of
  alternation-freeness holds up to Odd's tie-breaking among equal-valued plays (DATA: no path part ever returned, RET 0 below).

## 4. DEAD: the expiration route (instance nep92_n40, sha1 ce224ec31e56, start sha1 10fdf3a3c76c)
- W-run [6, 20], source x = 0 (Odd), blocks 0 < 8 < 9 at (u, v) = (0, 19):
  PI_0 = (0, 19, 24, 20, 4, 30, 16, 37, 11, T); PI_8 = (0, 24, 19, 22, 14, 27, 38, 13, 2, 3, 15, 29, 5, 11, T);
  PI_9 = (0, 19, 22, 14, 27, 38, 13, 2, 3, 15, 29, 5, 11, T). The segment 0→19 is used, left for 0→24→19, and used again.
- Obstruction (exact): the middle segment uses the Even edge 24→19. σ_k(24) = 20 at states 6-9, 19 at 10-16, 20 at 17-20: Even's
  vertex 24 switches 20 → 19 and back 19 → 20 inside ONE W-run, and the alternation is paid by that edge appearing and disappearing. In a fixed-graph parametric family edge availability does not change; here it
  is the whole dynamics. Pin: 50 violations, 27 of 360 (W-run, source) pairs, all Q2OFF (middle segment not followable at i or k).
- Corpus DATA (box 125's corpus: box59 sbcg.lst 719 + si/root alt_all.lst 413 = 1,132 runs; c_sbcg.txt, c_alt.txt): 1,692 W-runs,
  80,401 (W-run, source) pairs, ΣXCH 104,383, Σ(blocks − 1) 105,060; RET 0; alternation violations 16,500 in 158 games (1,802 pairs);
  every violation has q unfollowable at j (QOFF 9,913) or the middle segment unfollowable at i or k (Q2OFF 13,980); NEITHER 0.
  Max ΞCH_F(x) 63 (gate_K64_n581, n = 581).
- So Corollary AF-XI's premise is false; Gusfield's argument does not transfer. The quasi-polynomial W-run bound is NOT obtained.

## 5. Decision on (2): can XI-CH be cast as a parametric breakpoint count? (READING)
- No, not with the known theory. Three obstacles, the first decisive:
  (a) availability: G_σk differs from G_σ(k−1) by Even edges entering and leaving; segments come back (§4). No fixed graph with
      one-parameter weights reproduces this without the expiration property, which the envelope sequences in [GR] have.
  (b) the lexicographic order is NOT the obstacle for a fixed cycle node c: P and ℓ are additive along the path, and (P, ℓ) is one
      scalar Σ_{u above c} ±2^rank(u)·2n ∓ ℓ of O(n) bits (bit cost polynomial). The c-dependent threshold «above c» is the real
      lexicographic issue; within a W-run λ_W is constant but the cycle nodes of Ξ may move (not measured here).
  (c) circularity: a breakpoint count bounds Ξ-changes by the number of parameter pieces; here the «parameter» is σ itself, whose
      changes are the W-run length. Any transfer must bound availability toggles independently, which is XI-CH again (relocation).
- What survives: AF-QP is a clean sufficient condition. A weaker, availability-aware version (alternations of a segment pair (q, q')
  at (u, v) charged to switches of Even vertices on q') gives a Davenport-Schinzel order equal to the switch count: useless.

## 6. (3) What the known theory gives (READING; nothing PROVED about N5)
- Upper bound n^O(log n): NOT available (premise dead, §4).
- Lower-bound template for L-RED: an envelope sequence of lines min_i(a_i + λ b_i) has, as λ increases, slopes strictly decreasing
  and intercepts strictly increasing (elementary). So Carstensen / Mulmuley-Shah sequences are monotone in a FIXED cost order, which
  is compatible with Ξ-monotonicity (VAL-NORET). But each Ξ-change costs a transition of the W-run, so a super-polynomial XI-CH family
  IS a super-polynomial W-run: the template supplies the order of the plays, not the S4a dynamics that would delete the current optimum
  at each step. Not handed to L-RED as a construction; offered as an idea only (Lead decides).

## DONE / FINDINGS / NEEDS: in the Lead message and notes/L-NEW.md.
