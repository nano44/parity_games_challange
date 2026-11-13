# Packet P-N5-KEY1P (box 217): the one-player key model 1P(G) of a Ξ-acyclic genome is R104's IDEAL model (Lemma IDEAL-1P); N5's run on Γ3(G) from S3 up to its first fallback, read at the movers, is the key run of 1P(G), and the first fallback is transition T_key + 1 (Theorem RED-1P, a corollary of landed R117 REACH3: unconditional); two monotone potentials bound every mover's switches by min(|K(x)|, |PΞ(x)|) − 1 (A1, A2, A2-POLY), with PAIR-1P (A3) and HEREDITY (A4); QUIET-KEY-1P is exactly SW-POLY, and ENUM-LOG is necessary only (a REDUCTION / STRUCTURE packet; bounds nothing polynomially; G-N5-TIME stays OPEN; not M3, not M4)
L-NEW successor 77 (session_01V5yGRaRvmT6aAyZLgMCHoW), D1 / D14 / D18 / D21 / D25. Lead's brief to successor 77 (2026-11-13): «FREEZE the
packet P-N5-KEY1P (statement first, then the file)»; «Every premise from landed RESULTS, quoted by script with its R-id»; «This packet
is on the critical path of BOTH outcomes: a kill family on 1P(G) transfers to N5 only through REDUCTION, and a bound on 1P(G) likewise.»
Statement sent to the Lead 2026-11-13 12:04Z (date -u) before this file; Lead 12:07Z: «Write the packet AS STATED in your (2), items
1-7, unconditional on landed R104 / R105 / R117.»; «B-1: cite R117's KEY3 (a) with the pointer and the quoted statement; do NOT re-prove
it.»; «Kill form in item 7: state it by max_x sw(x) or T against N + M (SW-POLY is the exact statement), with k only as a
degree-≥-2 diagnostic.» File written from 12:11Z, referee items applied from 12:29Z (date -u). FROZEN at push: later text
goes into docs/new/P-N5-KEY1P-fixes.md (append-only). Source (history only): docs/new/N5-QUIETKEY-box217.md (a143d406), §1, §2, §5 A6′,
§6; this packet carries every proof in full and is checked against this text only.
Labels: PROVED (L-NEW, unrefereed) / COROLLARY of a landed result / OPEN / DATA / REMARK (not to sign). NOT a TARGET.md claim; does NOT
decide G-N5-TIME; NOT M3; NOT M4; not a step-4 pass. It bounds nothing polynomially and asserts nothing about whether long key runs exist.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §1 | the model 1P(G) (definition) | definition | G a genome of R104 with an acyclic Ξ-graph |
| §2 | Lemma IDEAL-1P: 1P(G) is R104's IDEAL model on G; T_key(G) = L(G) | PROVED | as §1; premises R104's definition, R105 ENC |
| §3 | Theorem RED-1P (a)-(c); Corollaries KILL-TRANSFER, BOUND-TRANSFER | COROLLARY of R117 REACH3 with S3-START, and §2 | as §1; N5 from S3 on Γ3(G) with R117's vertex indices |
| §4 | Lemma 0 (a)-(c) | PROVED | as §1 |
| §5 | A1 MONO-1P | PROVED (the V half is R105 MONO, re-proved) | as §1 |
| §6 | A2 SWITCH-BOUND; Corollary A2-POLY | PROVED | as §1; A2-POLY's N5 form by §3 |
| §7 | A3 PAIR-1P (i), (ii) | PROVED | a mover of degree 2 |
| §8 | A4 HEREDITY (i)-(iii) | PROVED | (i), (ii) any degree; (iii) deg(x) = 2 |
| §9 | SW-POLY (exact); ENUM-NEC (necessary only; k and k_c are defined only when every mover has degree ≥ 2) | PROVED | SW-POLY: as §1; ENUM-NEC: every mover of degree ≥ 2 |
| §9 | QUIET-KEY-1P; the converse of ENUM-NEC | OPEN (not claimed) | |
| §10-§12 | DATA, remarks, not-claimed list, TARGET.md diff | DATA / REMARK (not to sign) | |

## 0. Premises (landed; quoted by script, experiments/new/box217/quotes_key1p.out; nothing else is used)
- [SPEC] N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md; a transition is a FALLBACK if S4c fired at it. [Q R117] The setting of R117:
  «N5 (SPEC S1-S5) from its DEFAULT start S3 (SPEC S3 with FIX 1)».
- [DEF] The genome and the IDEAL model. [Q R104] «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each
  with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a
  distinct gate index, and a start»; «under a state s the Ξ-value of option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)),
  … up to the first Ξ-target X, compared by the β of largest rank in the symmetric difference: the option whose set contains that β is
  the better one if its parity is even and the worse one if odd»; «an IDEAL step moves every mover to the lexicographically least key
  (gate indices of the chain of W-targets under the new state, lowest level first) among its current option and the options with a
  strictly better Ξ-value, and the run stops when nothing is available or nothing changes, L(G) := its number of steps»; «the Ξ-graph
  has an edge x → xt(x, k) for every option with a mover as Ξ-target».
- [DEF], the same in the words of R104's packet. [Q docs/red/P-N5-REALIZE.md@e609c5d2] «a gate index gate(x, k), a bijection of the
  options onto 0..M − 1»; «IDEAL step from s. Availability A_s(x) := {s(x)} ∪ {k : (x, k) ▷_s (x, s(x))}.»; «If |A_s(x)| = 1 for every
  x, the run STOPS»; «key(x, k) := (gate(x, k)) if lev(x) = 0, and key_(s')(wt(x, k), s'(wt(x, k))) followed by gate(x, k) otherwise (a
  tuple of length lev(x) + 1); s'(x) := the k ∈ A_s(x) with the lexicographically least key.»; «If s' = s, the run STOPS»; «Otherwise
  s → s' is one IDEAL step. L(G) := the number of IDEAL steps from s_0»; (Fact X) «For IDEAL-ACYC and two options k ≠ k' of ONE mover
  x, B_s(x, k) ≠ B_s(x, k')».
- [ENC] [Q R105] «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) :=
  ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the
  Ξ-target is the exit X)»; «(MONO) the current Ξ-value of every mover never decreases along a run». (R105's ε is this packet's ω.)
- [NUM] The game and its vertex indices. [Q R104] «vertex indices: movers, gates in gate-index order, β-vertices, e-vertices in the order
  of their gates' gate indices, the unused loop, c_W, K0 to K3 (packet §3.1), on which the root-first key comparison depends».
  [Q docs/red/P-N5-REALIZE.md@e609c5d2] «e_g: indices N + 2M, … allocated in GATE-INDEX order». Γ3(G) is R117's game, R104's Γ(G) with
  its indices unchanged and the pads appended (quoted in [REACH3]). So on Γ3(G) the e-vertex of option (x, k) has index
  N + 2M + gate(x, k): the gate indices order the options exactly as their e-vertex indices do.
- [REACH3] [Q R117] «for every G with an ACYCLIC Ξ-graph, the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of
  priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every
  β_g → u, and m_(x,k) on every mover edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s
  vertices; n = N + 7M + 10) has S3's start pair equal to R104's stated start transported through the pads (Lemma S3-START), no pad is
  ever a cycle node or in a P-set (Lemma PAD), and the N5 run of Γ3(G) FROM S3 has states 0, …, L(G) equal to the transported REALIZE
  states of the IDEAL run, transitions 1, …, L(G) are FL transitions and transition L(G) + 1 is a fallback»; «a family of acyclic
  genomes with L super-polynomial in N + M would give games on which N5 from its default start makes super-polynomially many iterations».
- [REACH3], the same in the words of R117's packet (sha1 b7bd693744fdec2aa993f2133c22cbe724933ff0, signed by both referees).
  [Q docs/new/P-N5-REACH.md@73b3d1fd] «The STANDARD STATE of Γ3 for a mover state s is the transport of R104's start with the genome
  start replaced by s: σ(x) = m_(x,s(x)); σ(β_g) = xt(g) if xt(g) is a mover, pb_g otherwise; σ(K0) = pA, σ(K1) = s, σ(K3) = K2; τ(g) =
  pe_g at every gate, τ(K2) = K2; forced choices elsewhere.»; «Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L, L = L(G). Then
  the N5 run of Γ3(G) FROM S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L; transitions 1, …, L are FL
  transitions; transition L + 1 is a fallback.»; «Let IDEAL-ACYC-POLY mean: there is a polynomial q with L(G) ≤ q(N + M) for every
  G ∈ IDEAL-ACYC.»; «(b) Conversely, if (G_i) ⊆ IDEAL-ACYC has L(G_i) super-polynomial in N_i + M_i, then on the games Γ3(G_i) (n_i =
  N_i + 7M_i + 10 vertices, polynomial input size, §3) N5 FROM ITS DEFAULT START S3 makes at least L(G_i) + 1 iterations:
  super-polynomially many in n_i.»
- [FL] [Q R104] «one FL run (a maximal set of consecutive non-fallback transitions that keep τ, change σ and keep that valuation
  everywhere)»: an FL transition is not a fallback.
- [REACH3]'s own premises. R117 is used as landed, with the premises its title names; this packet adds none. [Q R117] «with R104's
  premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24 (b)'s choice rule with RESULTS R103's
  bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d) for termination only».
- NOT used (named so that a referee can check their absence): box 213's KEY-TAU (CANDIDATE), box 212's [IMP3] and RF-A..RF-D, box 213's
  G-2, the lane lemma STD-N5, RESULTS R122 and R125. They concern Ξ-cyclic genomes, N5′-xi or other numberings (§11).

## 1. The model 1P(G) (definition)
Let G be a genome ([DEF]) whose Ξ-graph is acyclic: movers x = 0, …, N − 1 with levels lev(x); options (x, k), k < deg(x), M := Σ_x deg(x),
D := max_x deg(x); per option a W-target wt(x, k) (a mover of level lev(x) − 1; none if lev(x) = 0), a Ξ-target xt(x, k) (a mover or the
exit X), a β with a rank and a parity (ranks distinct over all options), a gate index gate(x, k) (distinct over all options); a start
s_0. A STATE s is one option s(x) per mover.
- Weights and values. ω(x, k) := +2^rank if the β of (x, k) has even parity, −2^rank if odd. V_s(X) := 0; v_s(x, k) := ω(x, k) +
  V_s(xt(x, k)); V_s(x) := v_s(x, s(x)) (integers; well defined by recursion along the acyclic Ξ-graph, targets first).
- Availability. A_s(x) := {s(x)} ∪ {k : v_s(x, k) > V_s(x)}.
- Keys. key_s(x, k) := (gate(x, k)) if lev(x) = 0, and key_s(wt(x, k), s(wt(x, k))) ++ (gate(x, k)) otherwise: a tuple of length
  lev(x) + 1, read from level 0 up to x (root first). Tuples of one length are compared lexicographically. μ_s(x) := key_s(x, s(x)).
- KEY step s → s′. By increasing level: s′(x) := the k ∈ A_s(x) with the least key_(s′)(x, k) (key_(s′) at x reads s′ only at lower
  levels, already defined; the least element is unique by Lemma 0 (a)).
- Key run. s_0 := the genome start, s_(t+1) := (s_t)′; T_key(G) := the first T with (s_T)′ = s_T; the run is s_0, …, s_T, and step t
  (0 ≤ t < T) is s_t → s_(t+1). (T_key(G) is finite: Lemma IDEAL-1P and R104's L(G), or directly A2.)
- Counts. sw(x) := #{t < T : s_(t+1)(x) ≠ s_t(x)}. A W-PATH from x is a sequence of options o_ℓ, o_(ℓ−1), …, o_0 with o_ℓ an option of x,
  ℓ = lev(x), and o_(i−1) an option of the W-target of o_i; its key is (gate(o_0), …, gate(o_ℓ)); K(x) := the set of keys of the W-paths
  from x. A Ξ-PATH from x is a sequence of options (x_0, k_0), …, (x_r, k_r) with x_0 = x, x_(i+1) = xt(x_i, k_i) a mover for i < r and
  xt(x_r, k_r) = X; its value is Σ_i ω(x_i, k_i); PΞ(x) := the set of Ξ-paths from x; hΞ(x) := the largest r over PΞ(x).
- V_t, v_t, A_t, μ_t abbreviate V_(s_t), v_(s_t), A_(s_t), μ_(s_t). Writing one option per mover, the Ξ-path of x UNDER s is the one
  with k_i = s(x_i) for i ≥ 1 and k_0 = s(x), and V_s(x) is its value; v_s(x, k) is the value of the Ξ-path with k_0 = k that follows s.

## 2. Lemma IDEAL-1P (PROVED; premises [DEF], [ENC])
For every genome G with an acyclic Ξ-graph, 1P(G) is R104's IDEAL model on G, clause by clause: (a) for every state s, mover x and
options k, k′, option (x, k) has a strictly better Ξ-value than (x, k′) in [DEF]'s order iff v_s(x, k) > v_s(x, k′); so A_s(x) is
[DEF]'s availability; (b) key_s is [DEF]'s key; (c) the KEY step's s′ is the IDEAL step's s′; (d) the key run stops at the state at
which the IDEAL run stops. Hence s_0, …, s_T is the IDEAL run of G and T_key(G) = L(G).
Proof.
- (a) [DEF]'s Ξ-value of (x, k) under s is the set B of the β's of the options on its chain; the chain is the Ξ-path with first option
  (x, k) that follows s, a path of distinct movers (acyclic Ξ-graph), so its β's are distinct and Σ_(β ∈ B) ±2^rank(β) = ω(x, k) +
  V_s(xt(x, k)) = v_s(x, k) by the recursion of §1. By [ENC] the order of the β-sets is the order of these integers. So «strictly
  better Ξ-value» is «v_s larger», and [DEF]'s availability {s(x)} ∪ {k : (x, k) ▷_s (x, s(x))} is A_s(x).
- (b) By induction on the level, key_s(x, k) is the tuple of the gate indices of the chain of W-targets of (x, k) under s, lowest level
  first: at level 0 it is (gate(x, k)); at level ≥ 1 the chain of (x, k) is the chain of (wt(x, k), s(wt(x, k))) followed by (x, k).
  This is [DEF]'s key, with the same lexicographic comparison.
- (c) Both steps define s′ level by level and take, at x, the option of A_s(x) with the least key under s′: the same option, by (a), (b).
- (d) The IDEAL run stops at s when no mover has an available option other than its own, or when s′ = s; in the first case every
  A_s(x) = {s(x)}, so s′ = s. The key run stops at the first s with s′ = s. Both runs start at the genome start s_0, so by induction
  on t they have the same states, and L(G), the number of IDEAL steps, is T_key(G). ∎
Note. 1P(G) therefore adds nothing to R104's model; it is that model written with the two integer potentials used below. The tool
one217.py computes values as pairs (v, number of options on the path) compared lexicographically; by Lemma 0 (c) the second
coordinate never decides between two options of one mover, so its A_s(x) is §1's (DATA counter l0).

## 3. Theorem RED-1P (a COROLLARY of landed R117 Theorem REACH3 with Lemma S3-START, and of §2; no other premise)
Let G be a genome with an acyclic Ξ-graph, s_0, …, s_T the key run of 1P(G), T = T_key(G). Consider the run of N5 from its default
start S3 on Γ3(G) ([NUM]: R117's game with its vertex indices, n = N + 7M + 10 vertices). Then, under R117's premises as landed (§0):
- (a) for j = 0, …, T, state j of the N5 run is the standard state of Γ3 for s_j: at every mover x, σ_j(x) = m_(x, s_j(x)), and σ_j off
  the movers and τ_j are the same for all j ≤ T;
- (b) transitions 1, …, T are not fallbacks;
- (c) transition T + 1 is a fallback. So the first fallback of the run is transition F = T_key(G) + 1, and the run of N5 up to its
  first fallback, read at the movers, is the key run of 1P(G).
Proof. By Lemma IDEAL-1P the key run is the IDEAL run s_0 → … → s_L of G with L = L(G) = T. [REACH3] (both forms quoted in §0): the N5
run of Γ3(G) from S3 has states 0, …, L equal to the standard states of Γ3 for s_0, …, s_L, which is (a) by the definition of the
standard state (state 0 is S3's start pair, the standard state for the genome start, by Lemma S3-START); transitions 1, …, L are FL
transitions, hence not fallbacks ([FL]), which is (b); and transition L + 1 is a fallback, which is (c). ∎
**Corollary KILL-TRANSFER** (= R117's Corollary REAL-IDEAL-S3 (b) in the notation of 1P). If (G_i) is a family of genomes with acyclic
Ξ-graphs and T_key(G_i) super-polynomial in N_i + M_i, then on the games Γ3(G_i) (n_i = N_i + 7M_i + 10 vertices) N5 from its default
start S3 makes at least T_key(G_i) + 1 iterations: super-polynomially many in n_i. Proof: RED-1P (b), (c). ∎
**Corollary BOUND-TRANSFER.** If T_key(G) ≤ p(N + M) for a genome G with an acyclic Ξ-graph, then the N5 run from S3 on Γ3(G) reaches
its first fallback at transition T_key(G) + 1 ≤ p(N + M) + 1. Proof: RED-1P (c). ∎ Nothing is claimed about the run after its first
fallback.
**QUIET-KEY-1P (OPEN; not claimed).** There is a polynomial p with T_key(G) ≤ p(N + M) for every genome G with an acyclic Ξ-graph. By
Lemma IDEAL-1P this is word for word R117's IDEAL-ACYC-POLY (quoted in §0); it is the statement the fleet's notes call O1.

## 4. Lemma 0 (facts; PROVED; G as in §1)
- (a) For every state s, key_s(x, k) is the key of a W-path from x whose first option is (x, k), so key_s(x, k) ∈ K(x), and its last
  entry is gate(x, k): distinct options of one mover have distinct keys at every state. |K(x)| = deg(x) if lev(x) = 0 and |K(x)| =
  Σ_k |K(wt(x, k))| otherwise; so |K(x)| ≤ D^(lev(x) + 1), and |K(x)| ≥ 2^(lev(x) + 1) if every mover has degree ≥ 2.
- (b) Distinct Ξ-paths from x have distinct values. |PΞ(x)| = Σ_k |PΞ(xt(x, k))| with |PΞ(X)| := 1; so |PΞ(x)| ≤ D^(hΞ(x) + 1).
- (c) For every state s and mover x, the values v_s(x, k), k < deg(x), are pairwise distinct; and V_s(x), v_s(x, k) are values of
  Ξ-paths from x.
Proof.
- (a) Induction on the level (the chain of W-targets of (x, k) under s is a W-path). The map (k, κ) ↦ κ ++ (gate(x, k)), κ ∈ K(wt(x, k)),
  is onto K(x) by the definition of a W-path, and injective because gate indices are distinct: the last entry names k, the rest is κ.
  The two bounds follow by induction on the level.
- (b) Let two distinct Ξ-paths from x first differ at position i: they share (x_0, k_0), …, (x_(i−1), k_(i−1)) and the mover x_i, and
  take options k_i ≠ k_i′ there (two paths with a common prefix cannot differ by one ending earlier: the option (x_(i−1), k_(i−1)) has
  one Ξ-target). The β of (x_i, k_i) is not on the second path: its options before position i belong to movers from which x_i is reached
  by at least one Ξ-edge, its options after position i to movers reached from x_i by at least one Ξ-edge, and neither kind is x_i (the
  Ξ-graph is acyclic); at position i it has (x_i, k_i′). Each option has its own β. So the two β-sets differ. Let r be the largest
  rank in their symmetric difference; the difference of the two values is ±2^r plus a sum of terms ±2^i with distinct i < r, of
  absolute value at most 2^r − 1: not zero. The count and the bound follow by induction along the Ξ-graph (hΞ(y) ≤ hΞ(x) − 1 for a
  mover y = xt(x, k)).
- (c) v_s(x, k) and v_s(x, k′), k ≠ k′, are the values of two distinct Ξ-paths from x (they differ in their first option): apply (b).
  V_s(x) = v_s(x, s(x)). ∎

## 5. A1 MONO-1P (PROVED)
For every mover x and step t (0 ≤ t < T): (V) V_(t+1)(x) ≥ V_t(x), and V_(t+1)(x) > V_t(x) if s_(t+1)(x) ≠ s_t(x); (μ) μ_(t+1)(x) ≤
μ_t(x), and μ_(t+1)(x) < μ_t(x) if s_(t+1)(x) ≠ s_t(x). ((V) without its second clause is R105 (MONO), landed; it is re-proved here.)
Proof.
- (V), by induction along the Ξ-graph, targets first. Let k′ := s_(t+1)(x) and y′ := xt(x, k′). V_(t+1)(y′) ≥ V_t(y′) (induction, or
  y′ = X and both are 0). So V_(t+1)(x) = ω(x, k′) + V_(t+1)(y′) ≥ ω(x, k′) + V_t(y′) = v_t(x, k′). The KEY step takes k′ in A_t(x), so
  v_t(x, k′) ≥ V_t(x), with v_t(x, k′) > V_t(x) if k′ ≠ s_t(x) (definition of A_t).
- (μ), by induction on the level. Let k := s_t(x); k ∈ A_t(x). μ_(t+1)(x) is the least of key_(s_(t+1))(x, j) over j ∈ A_t(x), so
  μ_(t+1)(x) ≤ key_(s_(t+1))(x, k). At level 0 the right side is (gate(x, k)) = μ_t(x). At level ≥ 1, with w := wt(x, k), it is
  μ_(t+1)(w) ++ (gate(x, k)) ≤ μ_t(w) ++ (gate(x, k)) = μ_t(x) by induction (for tuples a ≤ b of one length, a ++ c ≤ b ++ c). If
  s_(t+1)(x) ≠ k, the least key is attained at s_(t+1)(x) only (Lemma 0 (a)), so the first inequality is strict. ∎

## 6. A2 SWITCH-BOUND and Corollary A2-POLY (PROVED)
**A2.** For every mover x: sw(x) ≤ min(|K(x)|, |PΞ(x)|) − 1. And max_x sw(x) ≤ T_key(G) ≤ Σ_x sw(x) ≤ Σ_x (min(|K(x)|, |PΞ(x)|) − 1).
Proof. μ_0(x), …, μ_T(x) lie in K(x) (Lemma 0 (a)), never increase and strictly decrease at every switch of x (A1): at most |K(x)| − 1
switches. V_0(x), …, V_T(x) are values of Ξ-paths from x, of which there are at most |PΞ(x)| (Lemma 0 (b), (c)), never decrease and
strictly increase at every switch of x (A1): at most |PΞ(x)| − 1 switches. Every step t < T has s_(t+1) ≠ s_t (definition of T), so it
switches at least one mover: T ≤ Σ_x sw(x); and a mover switches at most once per step: sw(x) ≤ T. ∎
**Corollary A2-POLY.** If every mover x of G has min(lev(x), hΞ(x)) ≤ c·log2 N, then T_key(G) ≤ N·D^(1 + c·log2 N) = D·N^(1 + c·log2 D):
polynomial in N for bounded D. For N5 itself: by Corollary BOUND-TRANSFER the N5 run from S3 on Γ3(G) then reaches its first fallback
within D·N^(1 + c·log2 D) + 1 transitions. Proof. A2 with Lemma 0 (a), (b): min(|K(x)|, |PΞ(x)|) ≤ D^(1 + min(lev(x), hΞ(x))). ∎
So a super-polynomial key run needs movers that are deep in BOTH graphs. Not claimed: anything for other genomes.

## 7. A3 PAIR-1P (PROVED)
Let x be a mover of degree 2 with options a, b. (i) If lev(x) = 0 or wt(x, a) = wt(x, b), then sw(x) ≤ 1. (ii) If xt(x, a) = xt(x, b)
(both X included), then sw(x) ≤ 1; this holds for every sequence of states with s_(t+1)(x) ∈ A_t(x) for all t, whatever the rule.
Proof. (i) At every state the keys of (x, a) and (x, b) have the same entries before the last one (none at level 0; the key of the
common W-target otherwise) and last entries gate(x, a) ≠ gate(x, b); say gate(x, a) < gate(x, b). Then key(x, a) < key(x, b) at every
state. The current option is always in A_t(x), so a switch from a to b at step t would choose b although a ∈ A_t(x) has the smaller
key under s_(t+1): impossible. So x switches at most once (from b to a). (ii) v_s(x, a) − v_s(x, b) = ω(x, a) − ω(x, b) at every state
(the same term V_s(xt) on both sides), a nonzero constant; say it is positive. A switch goes to a strictly better option, so it can
only be from b to a: at most once. ∎ ((i) is also a consequence of landed R111 PAIR-KF with R105 KEYFLIP; (ii) is its Ξ-side twin.)

## 8. A4 HEREDITY (PROVED)
Let x be a mover with sw(x) = |K(x)| − 1. Then: (i) μ_t(x), t = 0, …, T, takes every value of K(x), and μ_(t+1)(x) ≠ μ_t(x) only at
steps where x switches; (ii) if lev(x) ≥ 1, then for every option k of x, μ_t(wt(x, k)), t = 0, …, T, takes every value of K(wt(x, k));
(iii) if deg(x) = 2, with options a, b: XF_x ≥ |K(x)| − 2, where XF_x := #{t ∈ [1, T] : the sign of v_t(x, a) − v_t(x, b) differs from
the sign of v_(t−1)(x, a) − v_(t−1)(x, b)}. More generally every mover of degree 2 has sw(x) ≤ 1 + XF_x.
Proof. (i) By A1 the sequence μ_t(x) is non-increasing in K(x) and has a strict decrease at each of the |K(x)| − 1 switches of x; a
non-increasing sequence in a set of |K(x)| elements has at most |K(x)| − 1 strict decreases, so these are all of them, and the sequence
takes |K(x)| distinct values: all of K(x). (ii) Let κ ∈ K(wt(x, k)). κ ++ (gate(x, k)) ∈ K(x) (Lemma 0 (a)), so by (i) it is μ_t(x) for
some t; its last entry names the option, so s_t(x) = k and μ_t(wt(x, k)) = κ. (iii) Let x (degree 2) switch at steps t_1 < t_2 < … <
t_m, m = sw(x). The switch at step t_i goes to the option that is strictly better under s_(t_i) (it is in A_(t_i)(x) and is not the
current one), and the switch at t_(i+1) goes back to the other option, which is strictly better under s_(t_(i+1)). So the sign of
v(x, a) − v(x, b) (never zero, Lemma 0 (c)) at state t_(i+1) differs from the sign at state t_i, and some t ∈ (t_i, t_(i+1)] is counted
by XF_x. The m − 1 intervals are disjoint: XF_x ≥ m − 1. ∎

## 9. SW-POLY (exact) and ENUM-NEC (necessary only; degree ≥ 2) (PROVED); what is OPEN
- **SW-POLY.** «There is a polynomial q with sw(x) ≤ q(N + M) for every genome G with an acyclic Ξ-graph and every mover x of G.»
  QUIET-KEY-1P ⟺ SW-POLY. Proof: max_x sw(x) ≤ T_key(G) ≤ N·max_x sw(x) (A2). ∎ This is the exact statement; the depths below are
  diagnostics.
- Enumeration depths, DEFINED ONLY for genomes in which every mover has degree ≥ 2 (then |K(x)| ≥ 2^(lev(x) + 1), Lemma 0 (a)). For
  0 < c ≤ 1: k_c(G) := 1 + the largest level of a mover x with sw(x) + 1 ≥ |K(x)|^c (0 if there is none). k(G) := k_1(G): by A2,
  sw(x) + 1 ≥ |K(x)| iff sw(x) = |K(x)| − 1, so k(G) is 1 + the largest level of a mover that switches through every one of its keys.
- **ENUM-NEC.** Let every mover of G have degree ≥ 2 and T_key(G) ≤ P. Then k_c(G) ≤ (1/c)·log2(P + 1) for every 0 < c ≤ 1; in
  particular k(G) ≤ log2(P + 1). So QUIET-KEY-1P implies k_c(G) = O((1/c)·log(N + M)) on such genomes (ENUM-LOG).
  Proof. A witness x of k_c(G) = k ≥ 1 has level k − 1, so |K(x)| ≥ 2^k (Lemma 0 (a)), and P ≥ T_key(G) ≥ sw(x) ≥ |K(x)|^c − 1 ≥
  2^(c·k) − 1 (A2). ∎
- The degree hypothesis cannot be dropped from the definition: with movers of degree 1 the same reading of k grows linearly in N at
  constant T_key (the family LIFT, §11 and §10).
- **Kill form (by SW-POLY, not by k).** A family (G_i) of genomes with acyclic Ξ-graphs with max_x sw(x), equivalently T_key(G_i),
  super-polynomial in N_i + M_i refutes QUIET-KEY-1P, and Corollary KILL-TRANSFER applies to it. When every mover of every G_i has
  degree ≥ 2, T_key(G_i) ≥ 2^(c·k_c(G_i)) − 1 (proof of ENUM-NEC), so super-polynomial 2^(c·k_c(G_i)) suffices; k and k_c are
  diagnostics of such a family, not its definition.
- **OPEN, not claimed.** QUIET-KEY-1P; SW-POLY; the converse of ENUM-NEC (k_c(G) = O(log(N + M)) for every c, on every genome with all
  degrees ≥ 2, does NOT give QUIET-KEY-1P by anything proved here: a mover could switch super-polynomially often and still stay below
  |K(x)|^c for every fixed c). Box 217's earlier sentence that QUIET-KEY-1P is equivalent to k(G) = O(log N) is withdrawn (box 217 §5
  A6′; REFEREE-2 40, B-6), and so is its sentence that any polynomial bound must prove k(G) = O(log N) (false on genomes with movers
  of degree 1: LIFT).

## 10. DATA (not to sign). Tool experiments/new/box217/key1p.py (model: one217.OneP); outputs pinned in experiments/new/box217/out
Named must-0 counters (one line per genome or set): ideq (the key run of 1P(G) differs from R104's reference IDEAL simulator
experiments/red/r187/ideal.traj at some state or in length: Lemma IDEAL-1P); mism (the key run differs, state by state at the movers,
from N5 itself (n5v, SPEC mode) from S3 on Γ3(G) (box 189's builder) up to N5's first fallback: RED-1P (a), (b)); nofb (N5's transition
T + 1 is not a fallback: RED-1P (c)); l0 (Lemma 0 (c), and the pair order of one217.py against the integer order); a1mu, a1v (A1);
a2 (A2, both bounds and both inequalities on T); a3 (A3); a4h (A4 (i), (ii)); a4x (sw(x) > 1 + XF_x at degree 2: A4 (iii)).
| set (pinned file in out/) | genomes | key-run steps in all | largest T_key | ideq, l0, a1mu, a1v, a2, a3, a4h, a4x | mism, nofb (N5 itself) |
| --- | --- | --- | --- | --- | --- |
| five towers (key1p_towers_n5.out) | 5 | 741 | 299 | all 0 | 0, 0 on all 5 |
| climbed records (key1p_rec.out, key1p_rec_n5.out) | 63 | 1,945 | 340 | all 0 | 0, 0 on all 63 |
| mutated towers (key1p_mut.out) | 1,000 | 44,353 | 299 | all 0 | not run |
| mutated DBL4 / RECF4 (key1p_mut_n5.out) | 24 | 488 | 67 | all 0 | 0, 0 on all 24 |
| random (key1p_rand.out: eg195 «acyc» 3 × 300; random ladders 3 × 2,000 and 2 × 200) | 7,300 | 9,241 | 5 | all 0 | 0, 0 on the 400 ladders of the last two seeds; not run on the others |
| LIFT(H5, D), D = 0, 10, 40 (key1p_lift.out) | 3 (D = 10, 40 also with N5: 5 lines) | 136 each | 136 | all 0 | 0, 0 for D = 10, 40 |
The sums are printed by summ_key1p.py (out/summ_key1p.txt: «all files must0_sum 0»); files pinned by out/SHA1SUMS_key1p. The verify-time
subset is check_key1p.sh (pinned output check_key1p.out).
Reading of the table: the sets are the five towers (experiments/new/box212/inst: DBL4_d20_F30, H5_d20_F62, H6_d24_F126, HIT7_d28_F254,
RECF4_d20_F60; T_key 30, 136, 209, 299, 67), the 63 climbed records of box 217 (out/rec, T_key up to 340), 1,000 mutated towers (200 per
tower, 1 to 4 random mutations each), random genomes of two generators (short runs, T_key ≤ 5: they test the definitions, not long
runs), and three genomes of the family LIFT (§11). Random sets and mutations are tests, not a claim that long runs are rare or common.
- Controls (each must fire, check_key1p.out): perm (the keys of 1P use a random permutation of the gate indices): ideq and mism fire;
  howard (Howard's rule in place of KEY): a1mu fires; down (movers take options outside A_s): a1v fires; a2half (|K(x)|/2 in place of
  |K(x)|): a2 fires on HIT7; a3all (A3's test on every degree-2 mover): a3 fires; a4any (A4's tests without the hypothesis sw(x) =
  |K(x)| − 1): a4h and a4x fire; w0 (all β weights 0): l0 fires; fbearly (N5's fallback flag read at transition T instead of T + 1):
  nofb fires.
- The |K| convention and the per-level table (out/key1p_towers_n5.out, lines «level»): |K(x)| is the number of W-paths from x (Lemma 0
  (a)); every tower has two movers per level and degree 2, so |K(x)| = 2^(lev(x) + 1). The largest sw of a level-l mover against
  |K| − 1, for l = 0, 1, …: DBL4 0/1, 1/3, 3/7, 7/15, 15/31, then 5/63, …; RECF4 1/1, 3/3, 7/7, 15/15, 30/31, then 7/63, …; H5 1/1, 3/3,
  7/7, 15/15, 31/31, then 31/63, 31/127, 15/255, …; H6 1/1, …, 63/63 (levels 0-5), then 32/127, …; HIT7 1/1, …, 127/127 (levels 0-6), then
  33/255, 62/511, 96/1023, …. So k(G) = 0 (DBL4: no mover enumerates fully; its level-l movers switch |K|/2 − 1 times, l = 1..4, a HALF
  enumeration), 4 (RECF4), 5 (H5), 6 (H6), 7 (HIT7), at d = 20, 20, 20, 24, 28 levels; k_(3/4) = 5, 5, 6, 6, 7 (the tool's columns k,
  k34; every tower has all degrees 2). (This corrects box 217 §5 A6's entry «(4, 20) DBL4»: REFEREE-2 40, N-5.)
- LIFT (out/key1p_lift.out): LIFT(H5, D) for D = 0, 10, 40 has T_key = 136 and largest sw = 31 each time, while the tool's column k
  (read without the degree hypothesis) is 5, 15, 45; for D = 10, 40 N5 itself from S3 on Γ3 agrees state by state (mism 0, nofb 0).
- Second engine (not mine). [Q docs/referee-2/R2-key-preread.md@abd629d7] REFEREE-2 40's r2onep.py: «mism 0 on the 5 towers (T_1P = 30,
  67, 136, 209, 299 = N5's; my F = T + 1 on each) and on 600 random Ξ-acyclic genomes»; «a1mu, a1v, a2, a3, a4h, a4x all 0».
- Quotes: every quotation of §0 and of this section is checked by script (experiments/new/box212/quotes212.py against trunk 5d7aab0f
  and the named commits; quotes_key1p.out: 35 quotes, 0 missing, last line pinned in experiments/new/check.sh; with the tool's control
  QCTRL=1, 34 of the 35 are missed, the one hit being a quotation that ends right before a heading).

## 11. Remarks (not to sign)
- REFEREE-2 40's pre-read items (docs/referee-2/R2-key-preread.md, Addendum 2, claude/referee-2 abd629d7), and where they went.
  B-1 (state the value lemma with its proof): the lemma that the Ξσ-order of a mover's pads is 1P's order is KEY3 (a) of R117's
  packet, already signed; by the Lead's ruling (header) it is cited with its statement and not re-proved: see the next remark; this
  packet uses only the theorem built on it ([REACH3]). B-2 (the start): Lemma
  S3-START, quoted in [REACH3]. B-3 (F = T_key + 1; no [IMP3], no G-2): RED-1P (c), from [REACH3]; QUIET-KEY-1P is identified with
  R117's IDEAL-ACYC-POLY, not through box 212. B-4: «deg(x) = 2» is in A4 (iii). B-5: the |K| convention and the per-level table are
  in §10. B-6: §9 (ENUM-NEC is necessary only; the equivalence is withdrawn). N-5: §10 (DBL4 has k = 0).
- KEY3 (a), the bridge between 1P's availability and SPEC's, as signed in R117's packet (R(x) there is the set of options of x in
  S4a's arena, {σ(x)} ∪ Iσ(x)). [Q docs/new/P-N5-REACH.md@73b3d1fd] «(a) R(x) = {m_(x,k) : k ∈ A_s(x)}, A_s(x) := {s(x)} ∪ {k : (x, k)
  strictly Ξ-better than (x, s(x)) under s} ([DEF]).»; and for the keys, KEY3 (b): «e-indices follow gate indices ([DEF]; unchanged
  in Γ3)».
- New against landed text, and restated (REFEREE-2 41's map, relayed by the Lead 12:07Z; each landed clause checked by me and quoted).
  By Lemma IDEAL-1P every landed statement about R104's IDEAL model on acyclic Ξ-graphs (RESULTS R105-R116, R119, R120, each in its
  stated scope) is a statement about 1P(G). RESTATED here: A1 (V) is [Q R105] «(MONO) the current Ξ-value of every mover never
  decreases along a run» with [Q R114] «(MOVE-RISE) at any degree, a move of z at step t gives cv_(s_t)(z) > cv_(s_(t−1))(z)»; the
  Ξ half of A2 is [Q R113] «(PATH-RISE) at any degree, the current value cv(z) of every mover z rises at most P(z) − 1 times in a run»
  (P(z) = |PΞ(z)|) with MOVE-RISE; Lemma 0 (b)'s integer form is R105 (ENC) with R104's Fact X; A3 (i) at level ≥ 1 is [Q R111]
  «(PAIR-KF) for a mover x of degree 2 and level ≥ 1 with W-targets a, b of its two options, KF_x = 0 if a = b» with [Q R105] «(KEYFLIP)
  moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes»; A3 (ii) follows from [Q R111] «(MERGE) at any degree, for
  two distinct options k, k′ of x and a state s, v_s(x, k) − v_s(x, k′) depends only on the options under s of the movers of the two
  chains before their first common mover»; A4 (iii)'s count is the Ξ-side twin of KEYFLIP and is close to [Q R111] «(RETURN) for a
  mover x of degree 2 that moves to o at step t_1 and next moves at step t_2, the Ξ-target z of its other option is a mover with
  cv_(s_(t_2−1))(z) > cv_(s_(t_1−1))(z)». NEW, as far as REFEREE-2 41 and I can find: the μ half of A1 at any degree, the key half of
  A2 on every genome (hence A2 with the minimum), A2-POLY, A4 (i)-(ii), and §9's SW-POLY / ENUM-NEC bookkeeping.
- LIFT (REFEREE-2 41's family, relayed by the Lead 12:07Z; its own text was not on origin at this writing, so the numbers of §10 are
  my reproduction). LIFT(G, D): a chain of D movers c_0, …, c_(D−1) of degree 1, c_i of level i with W-target c_(i−1) and Ξ-target X,
  put under G: every option of an old level-0 mover gets W-target c_(D−1), and every old level rises by D. The chain never switches
  (degree 1); every key of an old mover gets the same D-entry prefix, so the order of any two keys of one old mover is unchanged; no
  Ξ-path of an old mover meets the chain. So the run on the old movers, T_key and every sw are those of G, and |K(x)| is unchanged
  for old x, while every old level grows by D: «1 + the largest level of a mover with sw = |K| − 1», read on all genomes, grows by D at
  constant T_key. This is why §9 defines k and k_c only when every mover has degree ≥ 2.
- Why the packet is unconditional. Box 217 stated the reduction as conditional on KEY-TAU (i) (box 213, CANDIDATE) and [IMP3]. Both
  are avoided: for Ξ-acyclic genomes the landed Theorem REACH3 is the reduction, once 1P(G) is recognised as the IDEAL model (§2).
  KEY-TAU, STD-N5 and box 215's e-index keys remain what a statement for Ξ-CYCLIC genomes would need; none is used or claimed here.
- Other numberings. N5's tie rules read vertex indices, so the run can differ on a renumbered copy of Γ3(G) (L-RED 69, R241). RED-1P
  is for R117's indices only. This loses nothing for either transfer: the gate indices are a free bijection of the genome, so every
  order of the options is realised by a genome in R117's layout. For a renumbered copy the e-index form of the key (ε(x, k) := the
  index of e_(x,k)) is DATA only here: one217.py --renum --check, mism 0 on 20 renumbered towers (out/key1p_renum.out: the five towers,
  e-vertices permuted or all vertices permuted, seeds 11, 12; the renumbered runs have 1 to 6 steps against 30 to 299 in R117's
  layout); a proof would go through KEY-TAU (i).
- Not in the packet: box 217 §7 (A7 FLIP-SUPPLY, A7′), its climbs (track B), and every statement about how large k(G) can be.

## 12. Not claimed; TARGET.md diff
No polynomial bound for N5, for 1P(G) or for L(G); no super-polynomial family; nothing after N5's first fallback; nothing for genomes
with a Ξ-cycle; nothing for N5′-xi; nothing for games that are not Γ3(G). TARGET.md §2 asks for an algorithm that solves every parity
game in time p(n + m); this packet proves statements about one candidate (N5) on one family of games (Γ3(G), G Ξ-acyclic) before its
first fallback. It is a reduction and a set of structure lemmas: not M3 (TARGET.md §4: a restricted class, and no polynomial bound even
there), not M4, not a gauntlet step-4 pass. **G-N5-TIME stays OPEN.**
