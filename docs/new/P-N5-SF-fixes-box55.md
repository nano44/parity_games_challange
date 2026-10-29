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
