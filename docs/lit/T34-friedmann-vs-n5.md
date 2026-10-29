# T34: Friedmann's deterministic-rule counters against N5, and the T33 §2.3 merge (L-LIT, 2026-10-29)

Asked by the Lead at 10:36Z (date -u), after T33. Owner ruling D18:
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems.

**Labels.**
- PROVED (source): a theorem of the opened source.
- PROVED (L-LIT, unrefereed): proved here, elementary, not refereed.
- DATA: measured by the script named.
- CONJECTURE, OPEN, READING: as in D18 / L40.

Nothing here bounds N5's running time; G-N5-TIME stays OPEN.

**Sources and fleet files used.**
- [F]: O. Friedmann, LMCS 7(3:19) 2011, arXiv 1106.0778 v2. Re-opened by L-LIT. PDF sha256 46c96f44775aa2b0…, the same file
  L-COMP (experiments/friedmann-hn/README.md) and L-NEW 29 (docs/new/N5-ALTLIT-box49.md) opened. Printed page numbers.
- Fleet files:
  - docs/lit/T20-N5-barriers.md (B8 rows);
  - docs/new/N5-ALTLIT-box49.md §2 (L-NEW 29);
  - experiments/friedmann-hn/README.md (L-COMP box 16: N5 on [F]'s H_n, 1,612 runs + variants);
  - SPEC docs/new/N5-ssi-global.md S1-S4;
  - experiments/n5-second/n5b.py (read, used read-only).

**Check script.** docs/lit/T34-gateshut-check.py, sha1 7c33508b2ef6639da2ce736028bcf013f152ed75. It imports L-COMP's hn.py,
census.py and n5b.py read-only. Run it as `python3 -I docs/lit/T34-gateshut-check.py N R SEED`.

## 0. Answers
1. **Which step of Friedmann's counters N5 breaks.**
   - Both counters ([F] §6 for I^loc, §8 for I^glo) delay the closing of a bit's cycle by HIDING its profit. Player 1 plays its best
     response τ_σ inside the open cycle ([F] §6.1, Lemma 6.1 (3)). The policy compares edges by Ξ_σ, which is computed against that
     best response.
   - N5 differs in two ways.
     - (a) S4b improves Odd's own τ. Lemma GATE-SHUT (§2, new, PROVED L-LIT, unrefereed) says that once τ(e) = h at a Friedmann
       gate, τ never returns into the cycle while the cycle node of h's play is below the gate.
     - (b) S4a chooses by W, the valuation against the fixed τ, not by Ξ_σ. With the gate shut, W prices the edge into the gate
       at its full value e ⊕ W(h), with or without the cycle closed.
   - So the hiding has nothing to act on.
     - [F]'s Lemma 6.2 (2) ("open cycle remains open", postponement by the deceleration lane) and §8.2's stubborn-cycle property
       ("the global policy makes no progress towards closing the cycle") are the steps that fail.
     - DATA: L-COMP box 16 (N5 linear on H_n, 1,612 runs; τ shuts the gates in the first n iterations from [F]'s start). T34's
       check: 0 violations of GATE-SHUT in 34,308 gate-state checks (table rows overlap on S3 and F for n = 3-5); every one of 247 reopenings h → d1 happened where its hypothesis
       fails.
2. **Is the T33 §2.3 sequencing the scheduling Friedmann gets from his rule? Can the two be merged?**
   - Partly. §2.3's lever, Odd's best reply σ̄ at a gate, IS Friedmann's lever. But under N5 it survives in one form only: whether
     an edge is in Iσ (Ξ_σ-improving or not). It does not survive as a magnitude (the edge looking cheaper than it is), because
     S4a's choice is by W.
   - Friedmann's gates use the magnitude form. [F] §6.1: "e_i is an improving node for d_i" while the cycle is open, so the edge
     is in the arena. The delay comes from it looking small.
   - So the direct merge (Friedmann's gadgets with §2.3) is BLOCKED by GATE-SHUT plus choice-by-W. Both are facts (§2, §3), not
     conjectures.
   - A merge in which every bit is sequenced by Iσ-membership alone is not excluded by anything L-LIT can prove.
   - I could not produce a gadget specification with a verified k = 2, 3 state sequence and a predicted count. None is given;
     §4 lists what such a gadget must satisfy.
   - The one-line conjecture for the Friedmann-gadget class is CONJECTURE NO-HIDE (§4).

## 1. Friedmann's two counters: the steps that carry the delay (PROVED, source)
- **Policies, [F] §4 p.6-7.**
  - I^loc: "for every strategy σ, every player 0 node v and every w ∈ vE that w ⪯_σ I^loc(σ)(v)".
  - I^glo: "computes a globally optimal successor strategy in the sense that the associated valuation is the best under all
    allowed successor strategies".
  - Both compare by Ξ_σ, the valuation against player 1's optimal counterstrategy τ_σ (§3, Theorem 3.2 [VJ00]).
  - Player 1 never improves a strategy of its own.
- **1-sink games, [F] §5 p.8.** "there is no real benefit in actually using different cycle nodes". Sink Seeking: the cycle
  component of Ξ_σ(w) is the sink v* for every σ reached. In N5 terms λ_Ξ is constant along the whole run, so [F]'s counting would
  sit inside one N5 phase if τ stayed constant (ALTLIT §2).
- **Simple cycle (I^loc), [F] §6.1 p.9-10.**
  - Lemma 6.1 (3): "If cycle i is open and σ(d_i) ≺_σ h_i, we have τ_σ(e_i) = d_i".
  - Then "e_i is an improving node for d_i ... but updating to e_i would yield a much greater reward than just Ξ_σ(e_i) ... by moving
    to d_i, the player 1 node hides the fact that there is a highly profitable node on the other side."
  - Lemma 6.2 (2): "If cycle i is open, σ(d_i) ≠ w or h_i ≺_σ w, we have σ′(d_i) = w ('open cycle remains open')", w the best
    lane node.
- **Deceleration lane, [F] §6.2 p.11-12.** Lemmas 6.3-6.4: a new best-valued input node in each iteration. Its purpose (p.12): "to
  absorb the update activity of other nodes in such a way that wise ... strategy updates are postponed".
- **I^glo, [F] §8 p.26.**
  - "the latter takes cross-effects of improving switches into account"; "the trick is to hide very profitable choices by
    structures that cannot be solved by a single strategy iteration".
  - §8.2 (stubborn cycle d1_i, d2_i, d3_i, e_i): "two nodes leave the stubborn cycle to the deceleration lane and one node moves
    into the stubborn cycle ... the global policy makes no progress towards closing the cycle".
  - Lemma 8.2 (gate access), Table 7 (H_n), Theorem 8.4: "at least 2^n improvement steps on H_n starting with ι_{H_n}".
- **The common step (READING).** In both counters the bit's profit is realized only when the cycle is CLOSED, because closing forces
  player 1 out to h_i ([F] §6.1: "setting a bit corresponds to forcing player 1 out of the cycle"). The policy's metric (Ξ_σ against
  τ_σ) does not see that profit before the closing. The delay is that blindness.

## 2. Lemma GATE-SHUT (PROVED, L-LIT, unrefereed; elementary)
**Setting.** N5 (SPEC S1-S4); τ Odd's current strategy.
- Ξτ: the S1 valuation of τ computed on the dual game G^d (SPEC "Odd's side").
- τ̄: Even's optimal counterstrategy to τ.
- Iτ: Odd's improving edges (SPEC S2 on G^d: (e, w) ∈ Iτ iff Ξτ(w) is strictly better for Odd than Ξτ(τ(e))).

**Statement.** Let e be an Odd vertex, h := τ(e), and d a successor of e. Suppose there is an Even-owned route π = (d = π_1, …,
π_m) with an edge π_m → e. Let c be the cycle node of Ξτ(h) and Q := {π_1, …, π_m, e}. If:
- (H1) every vertex of Q has rank above rank(c);
- (H2) the (τ̄, τ)-play from h avoids Q;
- (H3) the highest rank in Q belongs to a vertex of even priority;

then (e, d) ∉ Iτ. In words, a shut gate does not reopen.

**Proof.**
- Let τ′ := τ̄ changed on π to follow π. By (H2) the (τ′, τ)-play from h is the (τ̄, τ)-play.
- The (τ′, τ)-play from d is therefore π, then e, then h's (τ̄, τ)-play. Its valuation is V := (c, P(Ξτ h) ∪ Q, ℓ(Ξτ h) + |Q|).
  - Q is disjoint from h's play by (H2).
  - Q ⊆ ranks above c by (H1), so all of Q enters P.
- τ̄ is Even's pointwise-optimal counterstrategy to τ. This is the dual form of RESULTS R57 (a)'s premise (VJ), applied on G^d.
  Hence Ξτ(d) is at least as good for Even as V.
- V vs Ξτ(h): same cycle node, and the path sets differ exactly by Q. Fact DELTA (R84 (a)) with (H3) makes V strictly better for
  Even.
- So Ξτ(d) is strictly better for Even than Ξτ(h) = Ξτ(τ(e)), i.e. strictly worse for Odd.
- The dual order reverses the comparison of path sets with the same cycle node: G^d keeps the ranks and flips every parity (SPEC
  A3). So d is not Odd-improving at e. □

**Instance.** In H_n ([F] Table 7 with L-COMP's mode fig) the gate is e_i, d = d1_i, π = (d1_i, d2_i, d3_i).
- (H3) holds: e_i has the top even priority of the gate.
- (H1) holds whenever the cycle node of h_i's play is the sink x (the lowest rank).

**DATA (T34-gateshut-check.py: n5b SPEC; S3, F and L-COMP's random starts).** "Gate-states" means states with τ(e_i) = h_i.

| n | starts | gate-states | with (H1), (H2) | violations | h → d1 reopenings | of which with (H1), (H2) |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | S3 + F + 200 random (seed 3) | 14,385 | 14,217 | 0 | 102 | 0 |
| 4 | S3 + F + 100 random (seed 4) | 12,045 | 11,911 | 0 | 97 | 0 |
| 5 | S3 + F + 30 random (seed 5) | 5,783 | 5,705 | 0 | 48 | 0 |
| 3, 4, 5, 6, 8 | S3 + F only | 135, 228, 350, 510, 872 | all | 0 | 0 | 0 |

- **The reopenings are real and explained.** They are the "gate flips h → d1 → h" of L-COMP box 16 §4. Every one happens at a
  state where (H1) fails.
- **Example: rand4, n = 3, iteration 0.**
  - The cycle node of Ξτ(h1) is e2, the closed stubborn cycle of gate 2, which is above gate 1's vertices.
  - The path sets of d1_1 and h1 are then equal ({f2, g2, h1, k1, y2}). Only the lengths differ (9 vs 5), and with an even cycle
    node the longer play is better for Odd.
- **From [F]'s start (F) and SPEC's start (S3)** the hypotheses hold at 100% of gate-states and no gate reopens.

**Limits.**
- Unrefereed.
- (H2) and the dual form of (VJ) are the steps a referee should check.
- It covers gates of Friedmann's shape (top-even route back to the Odd vertex). It does not cover other Odd vertices.

## 3. Why GATE-SHUT plus choice-by-W voids the hiding
- **S4a chooses by W.** n5b.py step 2 (l. 234-241) computes "Even's optimum against fixed τ, Even restricted to A_σ". The arena is
  restricted to Iσ-edges (Ξ_σ, i.e. σ̄-based), and Odd is fixed to τ. So S4a's metric is the valuation against τ (W in the lanes'
  notation; ALTLIT §2 (a); T20 l. 27).
- **With τ(e_i) = h_i** (GATE-SHUT keeps it there), the W-value of the edge d3_i → e_i is e_i ⊕ W(h_i), the full bit reward:
  - the cycle need not be closed (with τ(e_i) = h_i, closing it is W-invisible: ALTLIT §2 (c); box 16 §3);
  - no other d^j_i needs to point in, so the stubborn cycle's three-edge structure is irrelevant.
- **So, at the first state where d3_i → e_i is in Iσ and e_i ⊕ W(h_i) is W-best in d3_i's arena, S4a takes it.**
  - [F]'s postponement (Lemma 6.2 (2); §8.2) needs that edge to be in the arena but beaten by a lane node in the policy's metric.
  - Under W, a lane node beats it only if the lane node's W-value already contains a reward above h_i's.
  - In H_n the lane's roots s, r (20n + 2, 20n + 4) are below every h_i (20n + 4i + 6), so the closing wins.
  - DATA: box 16 §2-§3. The [F] counter "never runs"; iterations are 6n + 4 (S3) and 8.06n + 9.4 (F); the longest phase is ≤ 9n
    over 1,612 starts.
- **What is left of σ̄ (READING).** Whether d3_i → e_i is in Iσ at all is decided by Ξ_σ, against σ̄.
  - [F] Lemma 6.1 (2) vs (3) is that boundary: σ̄(e_i) = h_i (not improving if h_i ≺_σ σ(d_i)) vs σ̄(e_i) = d_i (improving, by
    {d, e} with e even on top).
  - This is the only channel through which Odd's best reply still gates Even under N5. §2.3's lever is this channel.

## 4. The merge question
**The direct merge is blocked (by §2 and §3, both facts).**
- §2.3's step 4 proposed an Odd o_j whose σ̄ gates when x_j → b_j enters Iσ. Taking Friedmann's gates for o_j, GATE-SHUT shuts τ(o_j)
  early and then S4a sees the full value at the first Iσ-entry.
- The counter can then only be as slow as the sequence of Iσ-entries. Friedmann's lane and stubborn cycles do not control those
  entries: they control magnitudes under Ξ_σ.

**CONJECTURE NO-HIDE (one line).** No 1-sink family whose bits are Friedmann-type gates (an Odd vertex e with an exit h and an
Even route back to e, top rank even) gives N5 a super-polynomial run from the S3 or F start.
- Reason (READING, from §2-§3):
  - GATE-SHUT keeps each gate shut once S4b shuts it, while the cycle node stays below the gates.
  - After that, S4a's W-choice prices the gate edge at its full value. So each bit closes at the first state its edge is Iσ-improving
    and W-best, and [F]'s delay (hiding by τ_σ) is unavailable.
- Data: box 16 (H_n, two variants, 1,612 + variant runs, linear) and T34's check.
- OPEN, not refereed. It would be killed by a 1-sink family with a gate that S4b never shuts, or with lane rewards above the bit
  rewards.

**What a non-Friedmann gadget would have to do (a design target for L-RED, not a specification).**
- (R1) Sequence bits by Iσ-membership only. The bit edge must be Ξ_σ-NON-improving until the lower bits are set. Through σ̄, that
  means [F] Lemma 6.1 (2)'s side (σ̄ at the exit) until the right state.
  - A decision at x_j sees only suffix values (the plays from its successors). T33 §2.2's ascending layout makes those suffixes
    independent of the lower bits.
  - So the lower bits must reach x_j's suffix through extra edges, as [F]'s roots r, s and the k_i → g_j connections do.
- (R2) Keep Odd's τ from shutting the sequencing vertex, or make the shut vertex irrelevant. GATE-SHUT applies only under (H1)-(H3).
  A sequencing Odd vertex whose route back has an ODD top rank (H3 fails) is not covered, and its τ may move both ways.
  - This is the one structural escape L-LIT sees.
  - The cost: such a cycle is Odd-won when closed, which changes a cycle node and ends the N5 phase. Within one phase it must
    therefore never close. A counter would then run across phases, and R15 bounds the number of phases only exponentially.
- (R3) Reset without λ changes. T33 §2.3 step 5.
- If (R1)-(R3) can be met together, that is an N5 lower bound. L-LIT found no construction and has no proof that they cannot be met.
  NM = poly(n) (T33 §2.4) stays OPEN.

## 5. Not done
- No merged gadget specification, no k = 2, 3 state sequence, no predicted PCH or iteration count: none could be checked, and an
  unchecked one would mislead L-RED.
- [F]'s §6.3-§6.5 (cycle gates, counter phases, Lemmas 6.5-6.13) were not re-read beyond the lemma statements cited. Box 16 and
  ALTLIT §1 cite them.

## DONE / FINDINGS / NEEDS
- DONE:
  - docs/lit/T34-friedmann-vs-n5.md;
  - docs/lit/T34-gateshut-check.py (sha1 7c33508b…), with outputs in §2;
  - notebook rows.
- FINDINGS:
  1. Lemma GATE-SHUT (PROVED, L-LIT, unrefereed): at a Friedmann-type gate, a shut Odd gate (τ(e) = h) does not reopen while
     (H1)-(H3) hold. 0 violations in 34,308 gate-state checks. All 247 reopenings on random starts happen where (H1) or (H2) fails.
  2. Friedmann's counters break at the hiding step ([F] §6.1 with Lemma 6.1 (3) and Lemma 6.2 (2); §8 p.26; §8.2). N5's τ shuts the
     gates, and S4a's W-choice then sees the full bit value at the first Iσ-entry.
  3. T33 §2.3's σ̄ lever = Friedmann's lever, but under N5 only its Iσ-membership form survives. The direct merge is blocked.
     CONJECTURE NO-HIDE stated. A non-Friedmann gadget needs (R1)-(R3). (R2)'s only escape is an odd-top route, which costs phase
     changes.
- NEEDS (Lead to route; nothing for the owner):
  - (a) A referee read of GATE-SHUT, (H2) and the dual (VJ) step.
  - (b) If the Lead wants a lower-bound attempt: L-RED on (R1)-(R3), with the warning in (R2).
  - (c) None of this changes L-COMP 7's NM measurement.
