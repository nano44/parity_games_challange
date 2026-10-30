# R144: composing rel2's strict releases with latew's many frozen stretches does not multiply. Delay CAN be shared inside a stretch (rel3: R strict releases of one edge in one stretch at n = 54R − 20, so R° = Θ(n)), but releases are transitions: Σ_Φ R°_Φ ≤ |F| − SB_F. latew's quadratic stretch count comes from σ̄ flipping at almost every transition (stretches of length ≤ 2, 0 strict releases). No super-quadratic W-run; the costs add
L-RED successor 34 (Opus 5.5; D1/D18). Lead 2026-10-30 16:36Z: «R144 … COMPOSE them: one W-run where many stretches each carry ≥ 2 strict
releases, giving |F| super-quadratic in n. Or measure precisely why the costs add rather than multiply … can the delay chains of rel2 be
SHARED across stretches? Report |F| against n with fits, pins and the usual checks.» Written 2026-10-30 from 16:37Z (date -u). Labels:
PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.
BIP-RED (L-NEW box 89, under [SUB]): |F| ≤ SB_F + (SB_F + 1)(n − 1)(R° + 1) + FL_F. R°_Φ = transitions of the frozen stretch Φ that carry a
strict release; R° = max_Φ R°_Φ.

## 1. Baseline: latew (span/mkrw.py LATE=1) has many stretches, all of length ≤ 2 (DATA, bip/strictrel.py, rel2/swcount.py)
| K | m | n | \|F\| | frozen stretches | max strict releases of one edge in one stretch |
| --- | --- | --- | --- | --- | --- |
| 4 | 8 | 122 | 44 | 34 | 0 |
| 4 | 16 | 186 | 76 | 66 | 0 |
| 8 | 16 | 242 | 152 | 130 | 0 |
| 8 | 32 | 370 | 280 | 258 | 0 |
- Exact fits: |F| = K(m + 3) and n = 8m + 14K + 2. At fixed n the maximum, at K ≈ n/28 and m ≈ n/16, is |F| ≈ n²/448.
- Frozen stretches = |F| − 3K + 2 on all four (strictrel count). σ̄ flips at almost every transition, because every reactor flip changes Odd's reply on the wave.
- So latew's stretches have length ≤ 2 and cannot hold a strict release, which needs a block and a later release in the same stretch.
  Its releases (R*_F = K·m, R138) are all non-strict: block and release lie in different stretches.
- Switch counts (rel2/swcount.py): K 4 m 8: SW 129, 16 vertices switch ≥ 3 times, max 8 = 2K, longest stretch 2 transitions; K 8 m 16:
  SW 513, 32 vertices ≥ 3 times, max 16 = 2K, longest stretch 2. So 2m reactor vertices each switch up to 2K times.

## 2. Sharing the delay inside one stretch: rel3 (rel2/mkrel3.py; DATA, exact)
- rel2 paid each rise with its own delay chain, all running in parallel from state 0. The chain for rise j has length 6j, so n ≈ 20R².
- rel3 puts the chains IN SEQUENCE. Chain j of a gadget starts when chain j − 1's top rises, so its length is only the gap
  E_j − E_(j−1) = 6. The parts are:
  - one shared base H (top even priority);
  - stay markers in a band between all levels and H;
  - each value level on an internal chain vertex v_2, so it is absent from the top's pre-rise value and the next chain's bottom offer
    appears exactly at the rise.
  - Risen values are H + {levels so far}, ordered by the latest level. The interleaving h_i < a_(i+1) < b_i < h_(i+1) is as in rel2, and
    the gadget vertex A, h or B (Even) moves to each newly risen top.

  | R | n | \|F\| | strict releases of (y, oz) in one frozen stretch | frozen stretches |
  | --- | --- | --- | --- | --- |
  | 2 | 88 | 14 | 2 | 2 |
  | 3 | 142 | 20 | 3 | 2 |
  | 4 | 196 | 26 | 4 | 2 |
  | 8 | 412 | 50 | 8 | 2 |
  | 16 | 844 | 98 | 16 | 2 |

  - Exact fits: n = 54R − 20 and |F| = 6R + 2. So R° = (n + 20)/54 = Θ(n), against Θ(√n) for rel2. R = 32 (n ≈ 1708) did not finish
    in 900 s (n5b in Python); not run to the end.
  - Pin rel2/instances/rel3_R4_n196: strictrel 4 = L-NEW relpe.py STRICT=1 frozen_edge 4 (runs 1, so one W-run); xeng identical; Oink zlk +
    verify OK.
- Switch counts (rel3 R = 4): 61 vertices switch once, 0 twice, 4 at least 3 times (y 7, plus the three gadget vertices). Max 7.
  Every chain vertex switches exactly once in the whole run.
- So delay chains CAN be shared within a stretch, by reading them in sequence. That makes R° linear. It does not make time longer: every
  transition is still paid by a chain vertex that switches once.

## 3. Why the costs add (PROVED, lane, elementary) and what multiplication would need
- Lemma ADD. R°_Φ ≤ |Φ| for every frozen stretch Φ, so Σ_Φ R°_Φ ≤ |F| − SB_F.
  - Proof: R°_Φ counts transitions inside Φ, the stretches are disjoint, and the SB_F σ̄-changing transitions lie between them. □
  - Also, two strict releases of one edge need y to leave the edge in between, so one edge has at most ⌈|Φ|/2⌉ of them.
- Consequence. Strict releases are themselves transitions. Many stretches × many releases per stretch cannot give more than |F|, and
  BIP-RED's product (SB + 1)(n − 1)(R° + 1) is an upper bound that composition cannot attain multiplicatively. A super-quadratic |F| through
  BIP-RED needs super-quadratic SB_F, or stretches whose release EPOCHS are long (GP* allows up to n − 1 per epoch). Either way the length
  must come from delay.
- Time accounting (DATA). |F| ≤ SW_F := Σ_v SW_F(v), the total number of Even switches (every transition switches some Even vertex,
  except fallbacks).
  - In rel2 / rel3 almost every vertex switches once, so |F| = O(n).
  - In latew the reactors are a REUSABLE delay line: 2m vertices switch up to 2K times each (SW 129 at K 4 m 8; 513 at K 8 m 16).
  - Every reuse is paid by a pivot-ladder rung (a fresh marker and climb), so |F| = (rungs) × (line) = K·m.
- READING (the wall, restated as a switch count). A super-quadratic W-run needs SW_F super-quadratic, spread over distinct transitions.
  That means Ω(n^(1+ε)) vertices each switching ω(n) times, or a reusable line whose resets are not paid by fresh rungs.
  - A reset of a line vertex is a return. By RETURN-CHARGE (L-SI box 51b §10.3) it needs a strict Ξ-rise of the returned-to option. So
    resets need values that rise ω(n) times without fresh vertices, i.e. a counter. That is exactly the doubling that the arena optimum
    removes (R140 ARENA-MAX / DECEL-RED; R142 §3, static ρ).
- Sharing ACROSS stretches. A rel3 chain vertex would have to switch more than once, i.e. return. Inside a frozen stretch every return is
  a RETURN-CHARGE event (Ξ-rise of a stay). Across stretches, σ̄ changes can supply those rises without fresh vertices (mechanism O; latew
  does exactly this). But then the stretches are short (§1), so they carry no strict releases. So the two quadratic mechanisms compete for
  the same transitions: long frozen stretches (rel3) against frequent σ̄ flips (latew).

## DONE / FINDINGS / NEEDS
- DONE: rel2/mkrel3.py (shared-delay generator), rel2/swcount.py (time accounting), pin rel2/instances/rel3_R4_n196; check.sh "R144";
  this note; notes/L-RED.md.
- FINDINGS:
  1. DATA: rel3 gives R strict releases of one edge in one frozen stretch at n = 54R − 20 (R ≤ 16 run), so R° = Θ(n). Delay chains can be
     shared inside a stretch, read in sequence. |F| = 6R + 2 stays linear.
  2. DATA: latew's quadratic stretch count (|F| = K(m + 3), stretches = |F| − 3K + 2) comes from stretches of length ≤ 2 with 0 strict releases.
  3. PROVED (lane, elementary): Lemma ADD, Σ_Φ R°_Φ ≤ |F| − SB_F. Releases are time, so they cannot multiply with stretches. BIP-RED's
     product bound is not attained by composition.
  4. READING: the wall as a switch count. Multiplying needs a reusable delay line reset without fresh rungs, i.e. a counter, which
     ARENA-MAX removes. No super-quadratic W-run.
- NEEDS: none from the owner.
