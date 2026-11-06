# R212 FLIP-ADD under attack: co-designed lower bounds for T_1, T_2 at m 4-7; Lemma FROZEN-EMBED (L-RED successor 51)
Started 2026-11-06 07:4xZ (date -u). Lead BOX R212 (brief to successor 51). Model: the external-flip model of RESULTS R110 (T_k(m) over
the ISO genomes of 𝓛^R_(m+1), level 0 frozen, a c-step sequence with ≤ k changes of c); T^R(m) over 𝓛^R_m (RESULTS R110).
Labels: PROVED (lane, unrefereed), MACHINE (exhaustive check by a stated tool, no Lean), DATA (replayed witnesses; lower bounds
only), READING. Not a TARGET.md claim. FLIP-ADD and G-N5-TIME stay OPEN. No SAT is used in this file.

## 0. Answers
(filled at the end of the box: §2)

## 1. Lemma FROZEN-EMBED (PROVED, lane; unrefereed)
Statement. Let G be an ISO genome of 𝓛^R_(m+1) (m ≥ 1) and c ∈ {0, 1}. Let Lad_c(G) be the genome obtained as follows:
- drop movers 0 and 1; rename mover x ≥ 2 as x − 2, so level l becomes level l − 1;
- every option keeps its Ξ-target (renamed; ISO: never 0 or 1) and its β (rank and parity);
- options of levels ≥ 2 keep their W-target (renamed) and gate;
- the four options of the old level-1 movers lose their W-target (they are now level-0 options) and receive the four old level-1
  gates re-assigned in the lexicographic order of the pairs (κ^c_w, g), where w is the option's old W-target (mover 0 or 1),
  κ^c_0 = 1 − c, κ^c_1 = c (RESULTS R110's c-step keys) and g its old gate.

Then (a) Lad_c(G) ∈ 𝓛^R_m, and (b) for every state u of the levels ≥ 1 of G, the IDEAL step of Lad_c(G) from u equals the c-step of G
from u (states identified through the renaming).

Proof.
- (a) Two movers per level, all of degree 2, option k of a mover of level l ≥ 1 W-points to mover 2(l − 1) + k (renaming by −2 keeps
  the convention), no other movers. The Ξ-graph is a subgraph of G's, so it is acyclic. Ranks are a subset of G's, so distinct.
  Gates: the four level-1 values are permuted among themselves, so they stay distinct.
- (b) A-sets. The face of an option is the β-sum along its Ξ-chain under the old state. By ISO no chain of an option of level ≥ 1
  visits 0 or 1, so the chains, the β's and hence the faces are the same in G and in Lad_c(G) under the same state u. So the A-sets
  agree. (This is RESULTS R110 W-ONLY (b): the A-sets of the levels ≥ 1 do not depend on the options of 0 and 1.)
- (b) Keys. Write key_G for the c-step keys of G (level-1 option (x, k): (κ^c_w, g(x, k)); higher option: key_G of its W-target's new
  option followed by its gate), and key_L for the keys of Lad_c(G) (level-0 option: (h(x, k)); higher: as in G). Claim: for two
  options of the same level, key_G(o) < key_G(o′) iff key_L(o) < key_L(o′), under the same new state of the levels below.
  - Old level 1: h is the rank of (κ^c_w, g) among the four, read in the four old gate values, so the orders agree by construction.
  - Higher level: both keys are lexicographic tuples «key of the W-target's new option, then gate». The first components compare as
    at the level below (induction; equal iff the two W-targets are the same mover); the gates are the same in both genomes.
- (b) Moves. Each mover takes the key-least option of its A-set, lowest level first, keys under the new state, in both genomes. The
  A-sets agree and the key orders agree level by level (induction from the bottom), so the chosen options agree. ∎

Corollaries (PROVED, lane).
- (C1) T_0(m) ≤ T^R(m). Each maximal interval of a c-step sequence on which c is constant is, on its counted steps, a prefix of a run
  of Lad_c(G) (a state where the c-step does not move stays fixed under the c-step).
- (C2) T_k(m) ≤ (k + 1)·T^R(m) for every k. Hence the excess E_k(m) := T_k(m) − T^R(m) is at most k·T^R(m).
- (C3) FLIP-ADD can only fail through a superlinear T^R: if T^R(m) = O(m) then E_2(m) ≤ 2T^R(m) = O(m) and FLIP-ADD holds. So no
  amount of data at fixed small m can refute FLIP-ADD; the adversarial measure is the ratio T_2(m) / T^R(m) together with the growth of
  T^R. (With W-ONLY: FLIP-ADD ⇒ T^R_ISO(d) ≤ T^R(d − 1) + O(d), and C2 gives back only T^R_ISO(d) ≤ 3T^R(d − 1) + 2.)
- (C4) Lad_0(G) and Lad_1(G) differ only in the order of their four level-0 gates: the two «classes» (options W-pointing to old mover 0,
  resp. 1) swap places, each class keeping its inner order. So T_k(m) is the longest alternation, with ≤ k switches, between the runs
  of a «class-separated» ladder of 𝓛^R_m and its class swap. (Compare RESULTS R110 SWAP, which leaves 𝓛^R; this form stays in 𝓛^R_m.)

Converse (LIFT, r212/lift.py). A ladder L of 𝓛^R_m whose two smallest level-0 gates belong to different movers is Lad_1(G) of an ISO
genome G of 𝓛^R_(m+1) (after relabelling the options of a level-0 mover of L). So T_0(G) ≥ T(L) for such L.

Machine check (r212/embed.py; runs of Lad_c(G) under r187/ideal.py compared state by state with the c-step runs of L-SI's flipdp.py
Ext.step, every state, both c): 0 mismatches on 100 random ISO genomes at m 2 (3,200 runs), 100 at m 3 (12,800), 30 at m 4 (15,360), and
L-SI's inf18_m3 (128). Negative control NEG=1 (old level-1 gates kept, no re-ranking): 6,677 mismatches of 12,800 at m 3.

Scope (READING, D1): RESULTS R110 signs «T ≤ T_2(d − 1) + 2» for the runs of ISO genomes of 𝓛^R_d only. The brief's «T^R(d) ≤
T_2(d − 1) + 2» therefore covers T^R_ISO(d), not T^R(d): ladders with Ξ-targets at level 0 are outside W-ONLY (b)-(d). FLIP-ADD would
make T^R_ISO polynomial; the non-ISO part of T^R needs another reduction.
