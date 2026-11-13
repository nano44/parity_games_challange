# P-N5-KEY1P after the kill candidate EXP-IDEAL: DRAFT of the fixes entry and of the RESULTS line L-1, to be applied only after P-N5-EXP lands (not a fixes entry yet; the frozen packet docs/new/P-N5-KEY1P.md, sha1 f7191623e9ee212fa127c7e4a224f7ab9d689156, is not edited)
L-NEW successor 77 (session_01V5yGRaRvmT6aAyZLgMCHoW). Lead 2026-11-13 12:42Z (read 13:05Z by date -u): «QUIET-KEY-1P (your §3's OPEN
statement, = R117's IDEAL-ACYC-POLY) has a KILL CANDIDATE»; «Nothing to change in the frozen packet: QUIET-KEY-1P stays «OPEN» in it
until the kill is refereed; do not edit a frozen file. Prepare, as a separate short file to be applied after the kill lands (fixes
entry + L-1 text), the one-line change … and what remains true and useful in the packet». Written 2026-11-13 from 13:12Z (date -u).
Status of everything below: DRAFT. «R‹n›» stands for the RESULTS number that P-N5-EXP will get; nothing here is in force before
that entry exists on trunk. The family: L-RED-B 5's G_k (packet P-N5-EXP, claude/l-red-b 350d84eb, docs/red-b/P-N5-EXP.md; frozen,
unrefereed): k ≥ 3, Ξ-acyclic, degree 2, N = 9k − 16, M = 2N, k + 1 W-levels, L(G_k) = 2^k − 2.
MY INDEPENDENT REPLAY (added between 13:50Z and 13:52Z, by date -u before and after the edit; DATA, experiments/new/box217: inst_gk/ = byte copies of their G_3 … G_14 with
SOURCE.txt; out/key1p_gk.out, out/gk_total.out): with key1p.py (my 1P engine, R104's reference simulator ideal.traj as the second
engine) T_key(G_k) = 2^k − 2 for every k = 3, …, 14 (6, 14, …, 16382), ideq 0, largest sw = 2^(k−2), the tool's k = 1 and
k34 = 1 for k ≤ 7, then 8, 9, 10, 12, 13, 14, 15 for k = 8, …, 14; every packet counter (l0, a1mu, a1v, a2, a3, a4h, a4x) 0; with N5 itself
(n5v, SPEC mode, from S3 on box 189's Γ3) mism 0 and nofb 0 for k = 3, …, 9; and gk_total.py: N5 makes exactly T_key + 3 = 2^k + 1
iterations with one fallback, at transition 2^k − 1 (the exact count of landed RESULTS R124, Corollary EXACT-L: «exactly L(G) + 3
iterations»; R117 alone gives ≥ L + 1).

## 1. The one-line change (fixes entry, to append to docs/new/P-N5-KEY1P-fixes.md when R‹n› is on trunk)
«Entry ‹j› (after RESULTS R‹n›, P-N5-EXP). §3, last paragraph, and §9, last bullet: the label of QUIET-KEY-1P and of SW-POLY changes
from OPEN to **FALSE by RESULTS R‹n› (P-N5-EXP)**: the genomes G_k of R‹n› have acyclic Ξ-graphs and T_key(G_k) = L(G_k) = 2^k − 2
(Lemma IDEAL-1P) with N + M = 27k − 48. No statement, proof, tool, output or instance of the packet changes: the packet claimed
neither. This entry carries no proof.»
Consequences to state in the same entry, each a reading of the packet's own statements on G_k (to be checked on the family's files
before the entry is written; the counters are key1p.py's):
- RED-1P (c) on G_k: the first fallback of N5 from S3 on Γ3(G_k) is transition 2^k − 1 (measured by three lanes' engines and by
  mine: agreement, not a new claim). KILL-TRANSFER is the route by which R‹n› reaches N5; it is R117's Corollary REAL-IDEAL-S3 (b), so R‹n› does not depend
  on this packet.
- SW-POLY is the exact form that fails: max_x sw(x) = 2^(k−2) (replayed), consistent with A2 (max_x sw(x) ≤ T_key ≤ N·max_x sw(x):
  2^(k−2) ≤ 2^k − 2 ≤ (9k − 16)·2^(k−2)).
- ENUM-NEC is not touched, and its converse at c = 1 is now FALSE: k(G_k) = 1 (replayed; every mover of G_k has degree 2) while
  T_key is exponential, so «k(G) = O(log(N + M))» does not give a polynomial bound. (The packet said the converse was not claimed;
  §9.) For c < 1 the depths do see the family: k_(3/4)(G_k) = k or k + 1 for k = 8, …, 14 (a mover with sw = 2^(k−2) on one of
  k + 1 levels has |K(x)| ≤ 2^(k+1)): k_c, not k, is the diagnostic that detects a half-rate family.
- A2-POLY stays a positive subclass result and G_k must lie outside its class: some mover of G_k has min(lev(x), hΞ(x)) > c·log2 N
  for every fixed c and large k (otherwise T_key ≤ D·N^(1 + c·log2 D)). Scratch measurement (not pinned): the largest
  min(lev(x), hΞ(x)) over the movers of G_k is k at k = 5, 8, 12, and the largest hΞ is 8, 14, 22.
- A1, A3, A4 and Lemma 0 hold on G_k as on every Ξ-acyclic genome: the counters are 0 on G_3, …, G_14 (above). A3 bounds every
  «wire» mover (two options on one W-target: 5, 11, 19 such movers at k = 5, 8, 12, scratch count) and every mover with one
  Ξ-target for both options (7, 13, 21) by one switch each; a3 = 0 confirms it on the family.

## 2. What remains true and useful in the packet after the kill
| item | status after R‹n› | use |
| --- | --- | --- |
| Lemma IDEAL-1P | unchanged (PROVED lane, to be signed) | lets every statement about 1P(G) be read as one about R104's IDEAL model and back |
| Theorem RED-1P, KILL-TRANSFER | unchanged | N5's run on Γ3(G) IS the key run up to transition T_key + 1: the exact form of the transfer (R117 gives ≥ L + 1 iterations) |
| BOUND-TRANSFER | unchanged, now only for subclasses | with A2-POLY: N5 is polynomial up to its first fallback on Γ3(G) for log-deep G |
| Lemma 0, A1, A2 | unchanged | the two potentials; A2 is tight in neither coordinate on G_k (half-rate), and is the upper bound any family must respect |
| A2-POLY | unchanged | the positive subclass: every exponential family needs movers deep in both graphs |
| A3, A4 | unchanged | structure of full enumeration; G_k shows full enumeration is not needed for an exponential run |
| SW-POLY ⟺ QUIET-KEY-1P | unchanged as an equivalence; both sides FALSE | names the statement that fails |
| ENUM-NEC | unchanged (necessary only) | its converse at c = 1 is refuted by G_k |
| QUIET-KEY-1P, SW-POLY (OPEN in the packet) | FALSE by R‹n› | — |

## 3. RESULTS line L-1 (draft title; the clause in ⟦ ⟧ depends on the order of landing)
The one-player key model 1P(G) of a genome G of RESULTS R104 with an acyclic Ξ-graph (N movers with levels, M options, largest degree
D; per option a W-target one level down, a Ξ-target (a mover or the exit), a β with a rank and a parity, a gate index; ω(x, k) :=
±2^rank (+ for even parity), V_s(X) := 0, v_s(x, k) := ω(x, k) + V_s(xt(x, k)), V_s(x) := v_s(x, s(x)); availability A_s(x) := the
current option and the options of strictly larger v_s; key_s(x, k) := the gate indices of the chain of W-targets of (x, k) under s,
lowest level first; KEY step: level by level every mover takes the option of A_s(x) with the least key under the new state; T_key(G)
:= the number of steps from the genome start until nothing changes) is R104's IDEAL model on G, clause by clause, so T_key(G) = L(G)
(Lemma IDEAL-1P; premises: R104's definition of the model and RESULTS R105's ENC only); hence, by RESULTS R117 (Theorem REACH3 with
Lemma S3-START) under R117's premises as landed, the N5 run from S3 on Γ3(G) has its states 0, …, T_key(G) equal to the standard
states of Γ3 for the states of the key run, its transitions 1, …, T_key(G) are not fallbacks and its transition T_key(G) + 1 is a
fallback (Theorem RED-1P), so a family of such genomes with T_key super-polynomial in N + M gives games on which N5 from S3 makes
super-polynomially many iterations (Corollary KILL-TRANSFER, = R117's Corollary REAL-IDEAL-S3 (b)) and a bound T_key(G) ≤ p(N + M)
bounds the first fallback of N5 on Γ3(G) by p(N + M) + 1 (Corollary BOUND-TRANSFER); in 1P(G), with μ_s(x) := key_s(x, s(x)), K(x)
the keys of the W-paths from x, PΞ(x) the Ξ-paths from x, hΞ(x) the largest number of movers after x on a Ξ-path and sw(x) the
number of switches of x in the key run: keys of distinct options of a mover differ, distinct Ξ-paths from a mover have distinct
values, |K(x)| ≤ D^(lev(x)+1) and |PΞ(x)| ≤ D^(hΞ(x)+1) (Lemma 0); along the run V(x) never falls and μ(x) never rises, both strictly
at every switch of x (A1 MONO-1P); sw(x) ≤ min(|K(x)|, |PΞ(x)|) − 1 and max_x sw(x) ≤ T_key(G) ≤ Σ_x sw(x) (A2 SWITCH-BOUND); if every
mover has min(lev(x), hΞ(x)) ≤ c·log2 N then T_key(G) ≤ D·N^(1 + c·log2 D), and N5 from S3 on Γ3(G) reaches its first fallback
within that many transitions plus one (Corollary A2-POLY); a mover of degree 2 of level 0 or with equal W-targets, or with equal
Ξ-targets, switches at most once (A3 PAIR-1P); a mover with sw(x) = |K(x)| − 1 takes every key of K(x), changes its key only when it
switches, has W-targets whose keys take every value, and at degree 2 the order of its two option values changes at least
|K(x)| − 2 times (A4 HEREDITY); T_key is polynomially bounded on these genomes iff every mover switches polynomially often
(SW-POLY), and on genomes with every degree ≥ 2 a bound T_key(G) ≤ P gives k_c(G) ≤ (1/c)·log2(P + 1) for the depths k_c(G) := 1 +
the largest level of a mover with sw(x) + 1 ≥ |K(x)|^c, 0 < c ≤ 1 (ENUM-NEC, a necessary condition only) (2026-11-13) — a REDUCTION /
STRUCTURE statement; the only polynomial bound is A2-POLY's, on a subclass; ⟦before R‹n›: QUIET-KEY-1P (T_key ≤ poly(N + M) on
every such genome; = R117's IDEAL-ACYC-POLY) is OPEN and not claimed ∣ after R‹n›: QUIET-KEY-1P is FALSE by RESULTS R‹n›
(P-N5-EXP)⟧; Ξ-cyclic genomes, N5′-xi, other vertex numberings of Γ3(G) and the run after the first fallback are not covered;
G-N5-TIME ⟦stays OPEN ∣ as decided by R‹n›⟧; not M3, not a step-4 pass, not a TARGET.md claim (DATA: must-0 counters ideq, l0, a1mu,
a1v, a2, a3, a4h, a4x 0 on 5 tower genomes, 63 climbed genomes, 1,000 mutated towers and 7,300 random genomes, and mism, nofb (N5
itself from S3 on Γ3) 0 on the 5 towers, the 63 climbed genomes, 24 mutated towers and 400 random ladders; nine controls fire)
(P-N5-KEY1P, docs/new/P-N5-KEY1P.md; L-NEW successor 77)
- Not a line file yet: L-1 is written as docs/new/P-N5-KEY1P-line-L1.txt on the Lead's word, after the referees' first round, with
  the ⟦ ⟧ clauses resolved and every DATA number re-read from experiments/new/box217/out/summ_key1p.txt.
