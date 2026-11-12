# Box 102: DEEP3 from the proof side: depth is e-depth (CORE-ABOVE), face changes inherit their target's e-depth (PROPAGATE), so DEEP3 ⇐ MOVER-DEEP3; DEEP3's exact quantity measured
L-SI successor 51 (Opus 5.5), D18 / D14 / D1; Lead 09:56Z («BOX 102, DEEP3 from the proof side, approved: why internal-gate value changes
stay shallow (depth ≤ 3 on MWR at every n). L-RED 66 attacks DEEP3 from the kill side in parallel»). Labels: PROVED (L-SI lane,
unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / READING. Not a TARGET.md claim; G-N5-TIME stays OPEN; N5′-xi stays a
CANDIDATE (D1). Tools: experiments/si/box102/ (deep102.py, run102.sh, check102.sh); engine L-RED 65 how3_232 (claude/l-red 59daaef2, read-only).

## 0. Answer
- DEEP3 is NOT proved. This box makes it precise and moves it one level down.
- Lemma CORE-ABOVE (PROVED, lane; §1). In Γ3(G) the only vertices more relevant than an e-vertex are c_W, K0 and K3. So whenever the most
  relevant difference z of a Π-change is an e-vertex, depth = e-depth + #core above, with e-depth := #e-vertices above z, and
  0 ≤ depth − e-depth ≤ 3. DEEP3 can therefore be stated with e-depth (box 206's notion) at the cost of shifting c by ≤ 3.
- Lemma PROPAGATE (PROVED, lane; §2). For an internal gate g of option (x, k), a change of its face pe (resp. pβ) at a step with fixed Λ
  has the same most relevant difference z as the change of its W-target (resp. Ξ-target) mover at that step. Its e-depth equals the
  target's e-depth, or that plus one (g's own e-vertex above z).
- Corollary DEEP3 ⇐ MOVER-DEEP3 (PROVED, lane; §2): Deep^e_c(C) ≤ M_C · MD_(c−1)(C), where Deep^e_c counts the internal flips after t0
  charged to e-depth > c, and MD_c counts the value changes of C's movers after t0 at e-depth > c. MOVER-DEEP3 («MD_c(C) is polynomial
  for some fixed c») is the mover form of L-NEW 70's CONJECTURE DEEP-k1 (box 206 §2 «Mover form»), now on Γ3 and for one SCC. It stays a
  CONJECTURE.
- Why MWR is shallow (DATA + READING, §3). On MWR4 / 8 / 16_2 every internal flip after t0 is charged to a change of e-depth 0 or 1, at
  every n. The charged changes are the hub's top e-vertex climbing (e(30,0) → … → e(33,0) on MWR4_2, box 100 §5.3). By DEPTH-COUNT3 with
  c = 0, a top only rises: ≤ M times per Λ-interval. So MWR's re-arm is paid for by top rises, which DEPTH-COUNT3 counts polynomially.
  A family that defeats DEEP3 would need re-arms paid by changes BELOW a fixed top: an odometer on lower e-vertices.
- DATA (§3): DEEP3's exact quantity is small everywhere measured. Internal flips after t0 at e-depth > 1 number 38 on the 26 frozen instances and 0 on the 400 random genomes. The largest
  count is 24, on DHIB26_2804 at N = 108. MWR4/8/16_2 have none, and their movers have no change at e-depth > 1 after t0 (MD_1 = 0).

## 1. Lemma CORE-ABOVE (PROVED, lane)
Premise: Γ3's priorities (RESULTS R104 / R117; implementation pinned as l-new fcba92fc experiments/new/box189/gamma3.py l. 40-61, the
builder both referees used for R117-R125):
- prio(e_q) = eb + 2i with eb > bmax ≥ prio(β) for every β;
- gates, pads, m-pads ≤ 2; movers 0; c_X 2; K1 5; K2 3;
- c_W = top := max(other priorities) + 2; K0 = top + 2; K3 = top + 3.
Relevance is (prio, index).

Statement. Every vertex more relevant than some e-vertex is an e-vertex or one of c_W, K0, K3. Hence, for a change at fixed Λ whose most
relevant difference z is an e-vertex, depth = e-depth + |{c_W, K0, K3} ∩ above(z)| ∈ [e-depth, e-depth + 3].
For a length-only change: depth = |Π|, and e-depth = #e-vertices of Π.

Proof: read off the priorities. eb > bmax ≥ 6 > 5, 3, 2, … puts every non-e, non-core vertex below every e-vertex, and the core above
all. ∎
- DATA: counter abovefail (an element above z that is neither an e-vertex nor core) is 0 on every charged change (§3). Since β-vertices
  are below every e-vertex, a change whose z is a β has every e-vertex of Π above it.

## 2. Lemma PROPAGATE and Corollary DEEP3 ⇐ MOVER-DEEP3 (PROVED, lane)
Premises: Γ3's edges (R104 / R117: pe_q → e_q → (W-target w, or c_W); pβ_q → β_q → (Ξ-target y, frozen at the standard state)); R125
Lemma CN2-3 («no mover, gate or pad is ever a cycle node or in a set Π»); the VJ value of a single-successor vertex v that is not a cycle
node is ext(v, value of its successor).

Statement. Let g be the gate of option q = (x, k) with targets w (W) and y (Ξ) both movers, let f ∈ {pe_q, pβ_q} and t its target (w for
pe_q, y for pβ_q). At every step t → t + 1 with Λ_t(f) = Λ_(t+1)(f):
- Ω(f) changes iff Ω(t-target) changes, with the same most relevant difference z (or both length-only);
- e-depth(f) ∈ {e-depth(target), e-depth(target) + 1}, where the + 1 occurs iff f = pe_q and e_q ∈ Π (more relevant than Λ) and e_q is
  more relevant than z.

Proof.
- pe_q and pβ_q are pads, so not cycle nodes (CN2-3). e_q's only predecessor is pe_q and β_q's only predecessor is pβ_q, so neither is
  a cycle node either: a cycle through e_q would pass through pe_q.
- For the same reason the target's play never visits f or its e / β vertex: it would close a cycle through a pad.
- So Ω(f) = ext(f, ext(e_q or β_q, Ω(target))) at both states, with the same Λ. The vertices f and e_q / β_q enter Π identically at t and
  t + 1, so Π_t(f) Δ Π_(t+1)(f) = Π_t(target) Δ Π_(t+1)(target).
- Of the added vertices only e_q is an e-vertex. ∎

Corollary. Deep^e_c(C) ≤ Σ_(y ∈ C) indeg_C(y) · #{t ≥ t0 : Ω(y) changes at e-depth ≥ c} ≤ M_C · MD_(c−1)(C).
Proof: TWO-CROSS charges each flip to its face's change at the same step (injectively per gate). By PROPAGATE that change has the
target's z and e-depth ≥ (face e-depth) − 1. A target change at step t is charged by at most one flip per gate pointing at it. ∎

- Reading. DEEP3 is thereby reduced to deep changes at the MOVERS of one SCC, the same object as L-NEW 70's mover form of DEEP-k1 (box
  206 §2), here on Γ3 and after t0(C).
- The reduction is lossy. Most deep mover changes cause no flip (§3: DHIB26_2804 has MD_1 = 288 but only 24 flips at e-depth > 1).
  MOVER-DEEP3 is therefore STRONGER than DEEP3. It is the natural object for a proof, because a mover's value changes only through a
  switch or a change of its chosen gate's face, which a proof can follow along plays.

## 3. DATA (deep102.py; run102.sh; outputs experiments/si/box102/out/)
Unit: flip of an internal gate after t0(C) (DEEP3's exact quantity; box 100's cross100 counted every gate over the whole run). Sets: box
99's 26 frozen instances; 400 random genomes (rand191.rgen seed 10001). Must-0: abovefail (CORE-ABOVE), propfail (PROPAGATE). Control
PCTRL=1 (charge to the OTHER face's target) must fire.
- Totals:
  - 26 instances: 757 internal flips after t0; e-depth histogram {Λ change: 176, 0: 430, 1: 113, 2: 27, 3: 6, 4: 5}. Deep^e_1 = 38,
    Deep^e_2 = 11, max per gate (e-depth > 1) 7. abovefail 0, propfail 0. Mover changes after t0: 6,462, of which 502 at e-depth > 1.
  - 400 random genomes: 630 internal flips; histogram {Λ: 435, 0: 192, 1: 3}. Deep^e_1 = 0; abovefail 0, propfail 0. Mover changes:
    4,536, of which 4 at e-depth > 1.
  - Control PCTRL=1 (3 instances): propfail 125 (fires).
- Per instance (e-depth > 1 internal flips / mover changes after t0 at e-depth > 1):
  - MWR4_2, MWR8_2, MWR16_2 (sha1 856d369b, 918f1414, 2ccda9a9): 0 / 0 at every n. Flips at e-depth 0 / 1: 5 / 4, 9 / 8, 17 / 16.
  - DHIB26_2804: 24 / 288 (e-depth up to 4).
  - DWT20_2803: 9 / 114.
  - C6G8_n54: 3 / 29.
  - DHIB18_2805: 2 / 61.
  - RWX_n95: 0 / 2.
  - C98 climbs, WC, FW, MW, Ku, Kprev: 0 internal flips at e-depth > 1. MW / Ku / FW have no internal flip after t0 at all; box 100's
    MW deep flips were ext gates before t0.
- Shape of the deep flips (profile102.py, out/profile102.out: DHIB26_2804, DWT20_2803, MW8_2; depth > 3 over all gates):
  - Cascades: gates (75..83, 1) flip once each in successive steps. Each is charged to the change of its own e-vertex, under the same two
    common e-vertices (e(40,9), e(38,5)) and the core.
  - One repeater: gate (10, 0) has 7 flips at e-depth > 1.
  - Nothing grows with a family parameter here: DHIB / DWT are single climb records, not families.

## 4. What is open, and the next step
- MOVER-DEEP3 / DEEP3: open. A proof must explain why a mover of one SCC does not change its value super-polynomially often below a fixed
  set of top e-vertices.
- On MWR the answer is that every change that pays for a re-arm is a top rise (e-depth 0-1).
- The proof-side candidate (READING, not attempted here), «SOURCE»: follow a deep mover change along the play to the vertex where the
  old and new plays first diverge (a switch or a flip at that step). A deep change needs a deep divergence there. Show that each
  divergence at e-depth > c consumes a change at e-depth ≤ c elsewhere: a potential argument on P_c sets (DEPTH-COUNT3's object).
- Instances for L-RED 66 (through the Lead): DHIB26_2804 (sha1 2c49fd10; Deep^e_1 = 24, Deep^e_2 = 11, max 7 at gate (10, 0)) and
  DWT20_2803 (sha1 ca731061; Deep^e_1 = 9).
