# Fixes to P-N5-SF (box 55): appended items only; the packet docs/new/P-N5-SF-box55.md stays frozen at l-new 95a7a581 (sha1 dbc2345f…)
L-NEW successor 33 (Opus 5.5). Each item is a CLARIFICATION: no statement of the packet is widened or changed. Anything that would widen a
statement goes to both referees first. Source of the notes: REFEREE-2 20, docs/referee-2/R2-N5-SF.md §4 (referee-2 3ae22a6d; SIGNED in full,
no gap, nothing FALSE), routed by the Lead 16:19Z. REFEREE 18's report: pending at writing. Written 2026-10-29 from 16:21Z (date -u).

## F1 (answers N-SF-1): ONE-PLAYER (a) rests on SPEC conformance
Lemma ONE-PLAYER (a) uses that SPEC S1's procedure, run on G_σ̄, returns the valuation of the play pair (σ, σ̄). This is the same
SPEC-conformance premise as RESULTS R15 limit (ii) (G-N5T-1, DATA: si.py against a VJ00 brute force). It is a standing premise of the packet,
in addition to those listed under «Premises». REFEREE-2's OPa: 0 mismatches over 45,163 checks.

## F2 (answers N-SF-2): the τ-side mirror of ONE-PLAYER (b)
For τ, F^d(τ) runs S1 on S4b′'s arena H′ ⊆ G. N5's S4a on the one-player game G^d_τ̄ runs S1 on the dual of an arena of G^d. That is H′
with priorities Ω + 2, owners as in G. Ω + 2 keeps every rank, every parity and every successor list, so S1's output is the same. This is
the argument of SPEC's A3 row, applied twice. So the mirror of ONE-PLAYER (b) holds verbatim. REFEREE-2's OPb on Odd's side: 17,111
checks, 0 mismatches.

## F3 (answers N-SF-3): "a prefix of a λ-phase" in SF-RED (a)
In the proof of SF-RED (a), «these b − a transitions lie in one λ-phase of that run» is to be read as: they are a PREFIX of a λ-phase of
N5's run on G_σ̄ started at (σ^(a), σ̄). That run may continue past b while N5-SF moves to another σ̄. R17 (c) bounds the whole λ-phase,
hence the prefix. The bound b − a ≤ n + m is unchanged.

## F4 (answers N-SF-4): the start convention of §4's checker
experiments/new/box55/pcheck.py reads a start file with n5x.start_pair: every vertex the file does not list takes its S3 (best-reward)
start successor. This applies to both σ_0 and τ_0, and to the second runs of TAU_V. The ROW figures of §4 and of check.sh's "Box 55"
block are under this convention. Under another fill the runs differ (REFEREE-2: n3cov_lean gives E SBC 12 and 13 stretches when unlisted
vertices take their FIRST successor, against 11 and 12 here). This is DATA only. The theorems are per run and hold for every start.

## F5 (answers N-SF-5): Remark 1 is invisible in the data
No stretch in the data reaches the signed n + m, or the sharper n + m − 1 of Remark 1. REFEREE-2's maximum is 69, on games with n + m in
the hundreds. Mine is 101 on switchbestexp_16 (n = 410, n + m = 1,380; N5-SF-box54.md §3 extension, sfrun.py SEGMAX). Remark 1 stays a remark.

## F6 (answers N-SF-6): the reading of «iff» in SF-RED (c)
"N5-SF makes polynomially many iterations on a class of games iff SBC is polynomially bounded there" quantifies over all runs on the class,
i.e. every game of the class and every start pair. (b) and (c) are inequalities per run, so the same equivalence also holds for any fixed
start rule (e.g. SPEC S3): polynomial over the S3 runs of the class iff SBC is polynomial over those runs.

## Items F7-F13: REFEREE 18's notes SF-N1..SF-N7 (docs/referee/R-N5-SF.md, referee 500b51d7; SIGNED in full, no gap, nothing FALSE), with the Lead's 16:46Z additions
Both §Cs are in (REFEREE 6bbf0aed, REFEREE-2 42022bca): the joint gap map is empty and F1-F6 are accepted as clarifications. F7-F13 are
clarifications too; the packet is not touched. Quotes are at trunk e251d147 and are checked by experiments/new/box49/quotecheck3.py on this
file. Written 2026-10-29 from 16:52Z (date -u).

## F7 (answers SF-N1; extends F1): the standing premise of ONE-PLAYER (a), both forms
Lemma ONE-PLAYER (a) identifies S1's Ξσ on G with the play value of the pair (σ, σ̄(σ)), where σ̄(σ) is the counterstrategy that S1's
procedure itself RETURNS (SPEC S1: [Q docs/new/N5-ssi-global.md@e251d147:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once).»).
This rests on two premises, both standing:
- (i) the code's match to SPEC, RESULTS R15 limit (ii) = G-N5T-1 (DATA; see F1);
- (ii) that S1's procedure realises an optimal σ̄. This is RESULTS R57 (b)'s standing premise (REFEREE's P1′): [Q docs/RESULTS.md@e251d147:2915-2916] «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance, and the code's match to SPEC is DATA (R15 G-N5T-1)».
It is NOT the VJ00 Lemma 5.8 / G-N5T-3 premise; SF-RED does not use output correctness. Correction of wording (REFEREE-2's C.4): the
packet's Remark 2 («nothing about σ̄ beyond its being a function of σ») understates this. SF-RED also uses, through ONE-PLAYER (a), that
σ̄(σ) is the optimal counterstrategy whose play values are Ξσ. F1 and F7 together replace that phrase of Remark 2.

## F8 (answers SF-N2; an E-item): the S4c step changes no valuation, citation
SF-RED (a)'s sentence «The S4c step is value-flat (R17 (e): «fires only in the value-flat situation»), so at most n − 1 transitions change
Ξ» reads R17 (e) through R17's source proof. The source is docs/new/N5-phase-bound-box10.md, §3, proof of Theorem PH, lines 69-73 (the
frozen §§1-3 of R17's object): [Q docs/new/N5-phase-bound-box10.md@e251d147:69-71] «Otherwise step n is value-flat: it switches only vertices x that are their own cycle nodes, each to some z ∈ I(x), i.e. with Ω(z) ≻ Ω(ρ(x))»
and [Q docs/new/N5-phase-bound-box10.md@e251d147:71-72] «no valuation changes (every play that met x still meets x with the same path set)».
The S4c step switches each such own-cycle-node x to an Ω-best improving successor (the Remark after Theorem PH), so it is a step of that
kind and changes no valuation.

## F9 (answers SF-N3; an E-item): the full S4a quote
SF-TERM (i) uses S4a's last sentence, which the packet's [S4a] quote stops before. Verbatim, with it:
[Q docs/new/N5-ssi-global.md@e251d147:51-53] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»

## F10 (answers SF-N4): "the same arena H" in ONE-PLAYER (b)
"The same arena H" means the same graph: the same vertex ids, owners and priorities, and the same successor lists in increasing index
order, which S1's procedure uses ([Q docs/new/N5-ssi-global.md@e251d147:44] «Successor and predecessor lists are in increasing index order.»).
S4a′ on G and N5's S4a on G_σ̄ (τ = σ̄) both keep, at Even v, the sorted list of A(v), and at Odd v the single edge σ̄(v). So S1 runs on
identical input in both and returns the same output.

## F11 (answers SF-N5): n3cov_lean.start's SIGMA0 entry on an Odd vertex
red/n3/instances/n3cov_lean.start lists SIGMA0 47:18, and vertex 47 is Odd. pcheck.py (through n5x.start_pair) writes the entry into the σ
array. It has no effect on any run: S1 reads σ only at Even vertices (Engine.evaluate takes Odd entries as free), and N5-SF's steps
change σ only at Even vertices. pcheck compares strategy sequences on the player's OWN vertices (§4, and the projection in
distinct()), so the entry is ignored there too. Every other listed vertex keeps its start; unlisted vertices take S3 (F4). REFEREE's
parser rejects the file and its n3cov_lean runs use S3. So the two runs differ as starts, not as a disagreement. DATA only.
Check (inline, 16:5xZ): the valuation with σ[47] = 18 equals the valuation with σ[47] = −1, and the N5-SF run from the file equals the
run from the file without the 47:18 entry (29 states, identical on Even's vertices).

## F12 (answers SF-N6): sharpness of the stretch bound (DATA)
REFEREE: no stretch exceeds n − 1 transitions (max 47 on the families, 44 on the library). In my data, the stretch maximum stays below
n − 1 as well: SEGMAX 101 at switchbestexp_16, n = 410; ≤ 0.94n on the library (box 54 §3). So n + m is loose by a factor of about
(n + m)/n in all data. The signed bound is unchanged; a sharper statement (n − 1) would be a new claim for both referees.

## F13 (answers SF-N7): LAM_σ ≤ n(n − 1) is proved in place
SF-RED (b)'s LAM argument uses only R15 (a) (pointwise monotone Ξ along σ-changes), SPEC S1's order (cycle-node reward first) and the
injectivity of p'. It is self-contained, and it repeats for N5-SF's σ-sequence the counting of RESULTS R47 Lemma Φ (a)/(c), which is
deliberately not cited (R47 is about N5's own run).
