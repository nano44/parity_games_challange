# N5-SBC2 (box 56): SBC resists a direct potential; under an Odd-EXIT hypothesis the one-sided rule F is polynomial (Theorem EXIT)
L-NEW successor 33 (Opus 5.5; D14, D18, Lead reading L40). Lead's message 2026-10-29 15:54Z, BOX 56: «(1) attack SBC directly. Find a
potential that bounds the σ̄-changes along the τ-free orbit of F, or show that the P-leapfrog at 14N+16 forces a lower bound, cross-informed
by L-LIT T46/T47 (friedmannsubexp/fearnleysubexp, the kill target). (2) If SBC resists, name the weakest extra hypothesis under which
SF-POLY holds (e.g. bounded priorities d, a one-player structure) and prove it.» Written from 16:00Z (date -u).
Working note, unrefereed, not frozen, not a TARGET.md claim. Symbols as in docs/new/P-N5-SF-box55.md §0 (F, σ^(j), SBC_σ, λ_Ξ, G_σ̄, stretch)
and N5-SBC-box55.md (MONO-XI, NO-TRANSFER). Labels: PROVED (lane) / ASSUMPTION / CONJECTURE / OPEN / DATA / DEAD / READING.
Tools: experiments/new/box55/grp.py (per-group counts, §1); experiments/new/box56/exit.py (classes FIX / CH / H-EXIT / H-TOP, ties, flips,
Lemma LOC-OPT check, random class games), box56/libexit.sh; logs box55/grp_alt.txt, grp_si.txt, box56/exit_alt.txt.
T47 was not opened (I found only T46 on claude/l-lit at 15:53Z); T46 was read in its Summary and §1 (a)-(c).

## 0. Summary
- (1) No potential found; SBC resists. Two findings:
  - The σ̄-sequence on switchbestexp IS a binary counter on the N cycle-centre vertices CC(i) (the only Odd vertices whose σ̄ ever
    changes): it visits all 2^N patterns for N ≤ 4 (DSB = 4, 8, 16), with carries done Gray-style. For N ≥ 5 the counter takes an EARLY
    CARRY at the same orbit index for every N (j = 219 → 221: 01100 → 11110 at N = 5), skipping the last two low counts, and again at
    each later carry. This is what makes N5-SF linear-ish there (DATA, §1). The lower-bound direction is L-RED's (D1); I built no family.
  - CONJECTURE GROUP (per λ-interval and per σ̄ VALUE s, all stretches of s together make ≤ n − 1 Ξ-changing F-steps) holds on all data
    (689 library games, switchbestexp N ≤ 10: max 78 at n = 260), and would bound #σ by poly(n)·DSB (distinct best replies) instead of SBC.
    Its proof fails at one exact point (§1, "lost progress"). Even proved, it would not reach polynomial: the counter makes DSB = 2^N.
- (2) Theorem EXIT (PROVED, lane; under ASSUMPTION NT, §2): if an Odd vertex u has at most ONE successor from which an Even choice is
  reachable (H-EXIT) and u is the most relevant vertex of no cycle (H-TOP), then σ̄(u) changes at most once along the orbit of F. So on
  games where every Odd choice vertex is such an EXIT, SBC_σ ≤ n and the one-sided rule F makes fewer than (n + m + 1)(n² + 1) steps
  (and N5-SF fewer than 2(n + m + 1)(n² + 1) iterations if the mirror holds for Even). Both hypotheses fail exactly at switchbestexp's
  cycle centres, where the leapfrog lives (§3). The class is narrow (Odd can only "continue on one edge or exit to a σ-independent part");
  it is a statement about F, not a new polynomial class of parity games.

## 1. Attack on SBC (OPEN; DATA and one failed proof)
The counter (DATA; experiments/new/box54/n5sf.py, inline run 16:0xZ). Odd vertices whose σ̄ ever changes on switchbestexp_N (S3 start):
exactly N, the cycle centres CC(i) (vertex ids 58, 71, 81 at N = 3; 72, 85, 96, 106 at N = 4; …), each with two successors (CycleNode0(i),
CycleLeaver(i)). Writing bit i = 1 when CC(i) takes its larger-id successor, the pattern sequence at N = 4 (with orbit index) is
0000@0 0001@10 0011@29 0010@33 0011@42 0111@67 0101@71 0100@72 0101@80 0111@99 0110@102 0111@113 1111@144 1011@148 1001@149 1000@150 1001@157
1011@176 1010@179 1011@190 1111@215 1101@218 1100@219 1110@221 1111@223 1110@224 1111@230: a counter whose carries pass through 1-patterns
(0011 → 0111 → 0101 → 0100). At N = 5 the prefix up to j = 219 is identical, then 01100@219 → 11110@221: bit 4 is set before bits 1-0
count again (the full counter would go 01101, 01110, 01111, 11111). Later carries are cut the same way (10100@292 → 11110@294). The orbit
index of the first cut is 219-221 for every N ≥ 4. DSB (distinct σ̄) = 4, 8, 16, 30, 35, 48, 62 at N = 2, 3, 4, 5, 6, 8, 10; SBC = 4, 11, 26,
49, 56, 75, 97. READING: a switch-best-type counter that N5-SF follows until it can carry early; T46 §1 (c) (Fearnley) gives a mechanism
for early closing. Whether a modified family prevents the early carry is the kill question (L-RED 28, T46's friedmannsubexp).
CONJECTURE GROUP. For every λ-interval (a maximal stretch of the orbit with λ_Ξ constant; these are intervals because λ_Ξ(v)'s reward is
monotone, MONO-XI) and every Odd strategy s, the F-steps from states with σ̄ = s inside the interval, summed over ALL stretches of s, change
Ξ at most n − 1 times. DATA (box55/grp.py): 0 violations on alt_all (413) and sicorpus (276; 1 skipped, no TAU0 line); max ratio 0.92n
(red/xing/instances/x32_rand48, one stretch); switchbestexp N = 10: a group of 8 stretches makes 78 Ξ-changing steps, n − 1 = 259.
Consequence if true: #σ − 1 ≤ ((n − 1)·DSB + 1)(1 + LAM_σ)(2n(n − 1) + 1) (flat runs are ≤ 2n(n − 1) long by R15 (c)'s φ).
Where the proof breaks (exact). R17's Lemma P is an induction over consecutive switch-best steps on ONE one-player game G_s; its invariant
is Ω(x) ⪰ value(r) for paths r of ≤ k edges in G_s. Between two stretches of s the run passes through states with σ̄ ≠ s. Across them Ξ is
monotone (MONO-XI), but the step that LEFT s gained val(σ′, s), and Ξ_{σ′} = val(σ′, σ̄(σ′)) ⊴ val(σ′, s): Odd's new reply takes part of the
gain away. At the return to s only Ξ_{σ″} ⊵ Ξ_{σ′} is known, not ⊵ val(σ′, s), so the invariant built in the first stretch is lost. In
data it is never lost (GROUP holds), but I have no argument.
Dead: a GROUP-type bound gives no polynomial in general, because DSB is exponential on the counter for N ≤ 4 (16 = 2^4 patterns, all
distinct, switchbestexp_4, sha1 57b27b74…). So distinct best replies are no better a currency than changes on counters.

## 2. Theorem EXIT (PROVED, lane)
Definitions. CH := Odd vertices with ≥ 2 distinct successors. FIX := vertices from which no Even vertex with ≥ 2 distinct successors is
reachable (FIX is closed under successors). H-EXIT(u): at most one successor of u lies outside FIX. H-TOP(u): there is no cycle of G whose
most relevant vertex (largest p', SPEC S1) is u. NT(u) (ASSUMPTION, run-level): at every σ^(j) of the orbit, the minimum of Ξ_{σ^(j)}
over succ(u) (SPEC S1's order) is attained at exactly one successor.
Premises: SPEC S1 («Ξσ = valuation … under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once)»), S2;
RESULTS R15 (a) Lemma A and (b) Lemma B (as quoted in P-N5-SF §Premises for (a); (b): «if moreover Ω_{Switch_I(σ)} = Ωσ, then every
(v, w) ∈ I is a length-only switch at a cycle node: Λσ(v) = v», RESULTS l. 633 at 305cc8be), applied on the DUAL of a one-player game
(R15 is stated for VJ00 strategy improvement on any game; on G^d the improving player is Odd, SPEC S1 «Odd's side»).
Lemma LOC-OPT. For every Even strategy σ and every Odd u with λ_Ξ(σ)(u) ≠ u: Ξσ(σ̄(u)) ⊴ Ξσ(w) for every w ∈ succ(u).
Proof. Let G_σ be G with every Even vertex cut to σ; Odd strategies of G are the strategies of the one-player game G_σ, and in its dual the
valuation of σ̄ against the opponent's only strategy is the valuation of the play pair (σ, σ̄), i.e. Ξσ read in the dual order (SPEC A3:
ranks are kept, parities and rewards flip). Suppose Ξσ(w) ◁ Ξσ(σ̄(u)). Then (u, w) is an improving switch of σ̄ in that dual game (S2), and
R15 (a) gives val(σ, σ̄[u → w]) ⊴ Ξσ pointwise (better for Odd). σ̄ minimises at every vertex at once (S1), so val(σ, σ̄[u → w]) ⊵ Ξσ;
hence equality, and R15 (b) makes (u, w) a length-only switch at a cycle node, Λ(u) = u, i.e. λ_Ξ(σ)(u) = u. Contradiction. The order
on valuations is total (S1), so Ξσ(σ̄(u)) ⊴ Ξσ(w). □
Lemma FIX. For w ∈ FIX, Ξσ(w) is the same for every Even strategy σ.
Proof. Every play from w stays in FIX, where every Even vertex has one successor; so val(σ, τ)(w) depends on τ alone. Ξσ(w) is the value
of a pointwise minimiser (S1), hence the minimum over all Odd strategies τ of val(σ, τ)(w), which does not depend on σ. □
Theorem EXIT. Let u ∈ CH satisfy H-EXIT(u), H-TOP(u) and NT(u). Then σ̄(σ^(j))(u) changes at most once along the distinct-σ sequence
(equivalently along the orbit of F, P-N5-SF Lemma DECOUPLE).
Proof. H-TOP: if λ_Ξ(σ)(u) = u, the play from u ends in a cycle through u whose most relevant vertex is u; so λ_Ξ(σ)(u) ≠ u for every σ,
and LOC-OPT applies at every j: σ̄_j(u) minimises Ξ_j over succ(u), and by NT it is the unique minimiser. If all successors lie in FIX,
their values are constant (Lemma FIX), so the unique minimiser is the same at every j: no change. Otherwise let w_1 be the successor
outside FIX, c := the minimum of the (constant) values of the others, X_j := Ξ_{σ^(j)}(w_1). By MONO-XI (R15 (a)) X_j never falls. NT
excludes X_j = c. So σ̄_j(u) = w_1 when X_j ◁ c and = the unique FIX-minimiser w* (the same vertex for all such j) when X_j ▷ c, and
{j : X_j ◁ c} is an initial segment. One change at most. □
Corollary EXIT-RED. If every u ∈ CH satisfies H-EXIT, H-TOP and NT, then SBC_σ ≤ |CH| ≤ n, and the one-sided rule F (equivalently N5-SF from
any τ* with Iτ* = ∅, NO-TRANSFER) makes #σ − 1 < (n + m + 1)(1 + n(n − 1) + n) = (n + m + 1)(n² + 1) steps (P-N5-SF Theorem SF-RED (b)).
If moreover the mirror holds for every Even vertex with ≥ 2 successors on G^d (at most one successor from which an Odd choice is
reachable, H-TOP on G^d, and NT^d), then N5-SF makes I < 2(n + m + 1)(n² + 1) iterations.
Proof. Each j counted in SBC_σ changes σ̄ at some u ∈ CH (vertices outside CH have one choice); each u changes at most once. SF-RED (b)
with LAM_σ ≤ n(n − 1). The mirror is the same argument on G^d, and SF-TERM gives I ≤ (#σ − 1) + (#τ − 1). □
DATA (box56/exit.py). Lemma LOC-OPT checked at every orbit state for every u ∈ CH (not only the EXIT ones): 0 violations on alt_all (413
games, 5,858 choice vertices; box56/exit_alt.txt) and on 800 random class games (seeds 1, 2; with 50% H-EXIT violations in seed 2). 750
library choice vertices satisfy H-EXIT, H-TOP and NT; none changes σ̄ more than once (Theorem EXIT). Choice vertices OUTSIDE the hypotheses change up to
3 times in the random games (seed 2, 50% second general successors), so the bound is not automatic. The random runs are short (mean 3.3 σ-values), so they test the
lemma, not the bound. NT failed at 942 library choice vertices and 142 + 298 random ones, with no extra change seen: CONJECTURE EXIT
without NT is OPEN (S1's tie-breaks, SPEC FIX 2 / FIX 4, depend on σ elsewhere).

## 3. Why this is the boundary, and what it is not
- On switchbestexp_N every cycle centre CC(i) fails H-TOP (it tops its simple cycle) and N − 1 of them fail H-EXIT (both CycleNode0(i)
  and CycleLeaver(i) → UpperSelector(i) reach Even choices; CC(N − 1) passes H-EXIT, its leaver reaching only FinalSink). exit.py on
  switchbestexp_2 / _10: CH 2 / 10, EXIT 1 / 1, TOP 0 / 0, flips up to 3 / 41. The leapfrog of N5-SBC §3 needs two σ-dependent successors,
  and Theorem EXIT shows that one is not enough (with H-TOP, NT). So the obstruction is located: SF-POLY is open exactly on games whose
  Odd choices see two Even-influenced futures.
- Not shown: anything about two-player games beyond this class; anything about bounded priorities d (VJ00's valuation makes p' injective,
  so d does not bound the P component; I found no argument); that the class is hard (it is not: Odd's choices are stopping decisions,
  READING).
- Labels for the Lead: Theorem EXIT, Lemmas LOC-OPT, FIX, Corollary EXIT-RED: PROVED (lane), under ASSUMPTION NT; CONJECTURE GROUP OPEN;
  SF-POLY OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box55/grp.py, box56/exit.py, box56/libexit.sh; logs box55/grp_alt.txt, grp_si.txt, box56/exit_alt.txt;
  check.sh block "Box 56".
- FINDINGS: (1) switchbestexp's σ̄ is an N-bit counter on the cycle centres, complete for N ≤ 4 (DSB 2^N), early carry at j ≈ 220 for
  N ≥ 5 (DATA; the kill lead for L-RED). (2) CONJECTURE GROUP (per-best-reply Ξ-changes ≤ n − 1 across stretches): 0 violations, proof
  breaks at "lost progress"; useless on counters anyway. (3) Theorem EXIT (PROVED lane, under NT): one σ-dependent successor and no cycle
  top ⇒ σ̄(u) changes ≤ once; F polynomial on Odd-exit games, (n + m + 1)(n² + 1). Boundary = switchbestexp's cycle centres.
- NEEDS: none from the owner. To the Lead: route the early-carry observation to L-RED 28; T47 not seen on claude/l-lit at 15:53Z.
