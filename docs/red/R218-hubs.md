# R218 hubs vs CANDIDATE N5′-xi (L-RED successor 55; Lead GO 18:42Z 2026-11-07)
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (named premise) / DATA (unit, set, scope) / DEAD (instance) / READING (not to sign).
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Setting, notation and premises ([LOC], F1-F6,
IDEAL-CYC, MERGE, E-DOM-CHOICE, LEAK-ARCH) are those of docs/red/R217-ovt.md and L-NEW's frozen packets docs/new/P-N5-XICYC.md and
docs/new/N5-RPOT-box192.md (claude/l-new a2db977d). Tools: experiments/red/r218/ (own.py = R217's independent implementation, copied;
t1.py … t4.py = constructions; lam.py = cycle nodes; play.py = plays at a state; meas.py = bit words, re-arms, D(v); otrace.py = named trace; xcheck.py = the 4-route check, copied).

## 0. Answers (milestone 1, 19:0xZ)
- Test (1), a hub H that tracks only the HIGHEST set bit: run (§2). DEAD as a counter. Every lane node re-arms at most once in the
  whole run (ROOT s) or never (ROOT H). D(H) ≤ n + 1, and (M 2) T = 2n + 6 (ROOT s, n 3-8) or 4n − 4 (ROOT H, n 4-8; n 3: 9). Four routes agree.
- Why this cannot be repaired by tuning: Lemma SWITCH-IN-DV (§1, PROVED-CONDITIONAL on F1). A mover adopts an option o at most
  D(g_o) times, where D(g_o) is the number of distinct values of o's gate vertex. Corollary REARM-DV: a lane node re-arms (adopts
  EXIT) at most D(X) + 1 times, where X is the exit target. Its chain is re-formed at most D(Y) + 2 times, where Y is the target of the
  lane root. So a hub with D(H) ≤ n + 1 re-arms its lanes at most n + 2 times. This proves the predecessor's reading of test (1)
  (R217 §11), with the constant.
- Test (2), hierarchical (prefix / Fenwick-style) hubs, v1 (§3): bit k's lane exits to a probe chain P^k over the lower bits. Its value
  encodes the whole lower state (mirror e's below every bit e). The leak of LEAK-ARCH does NOT occur (Lemma MIRROR-NOLEAK). But the
  lanes still re-arm at most once per node, and the bits fill up in unary (0001 → 0011 → 0111 → 1111). DEAD as a counter (instances
  in §3). The data is exactly what REARM-DV predicts: a rich exit hub (D up to 2k + 1 in these runs) does not help when the root
  target has D = 1 (ROOT s), or when root and exits see the same hub (ROOT P).
- The precise requirement (Corollary REARM-PAIR, §1): a lane that re-arms at every lower event needs TWO vertices X (exits) and Y
  (root) that overtake each other at every such event. Each overtake is a strict increase of the overtaker. With E-DOM, every pair I
  could build fails (READING §4, a trilemma on where an open bit's hidden route goes). Down (top-down chains): the bit-0 probe comes
  after the merge, and two plays cannot split after they merge, so no pair. Up through the real chain: a set bit's own lane option
  reaches its own SET gate, so the leak of LEAK-ARCH H2 occurs. Up through a mirror chain: a cycle through the open bit's own lane,
  which Odd keeps or breaks by misreading a probe. DEAD instance of the third branch: T3 (§4), every bit sets at step 1.
- H1 hub without access edges (Lead 20:01Z hint; §6): DEAD. Fact E-CYCLE: every cycle through an e is Even-won. So an H1 hub that open
  bits' lanes reach closes Even-won cycles through the lowest set bit's escape, and Odd hides that bit (Proposition H1-CYCLE; T4).
- Box goal (doubling T per added bit, O(1) size growth): NOT reached. The obstruction is NOT proved. What is proved: SWITCH-IN-DV,
  REARM-DV, REARM-PAIR, MIRROR-NOLEAK, SET-ROUTE-WINS, PLAY-BLIND, E-CYCLE, H1-CYCLE. Open: an E-DOM hub pair (X, Y) that overtakes at every carry, outside the
  three branches of §4.

## 1. Lemma SWITCH-IN-DV and corollaries (PROVED-CONDITIONAL on F1, lane)
Setting: the IDEAL-CYC Howard run σ_0, σ_1, … of any genome (any d). σ_t(x) is computed from the values Ω_(t−1) of state t − 1. Every
mover moves to a ⊴-best option, keeps its current option on a tie (own.py; own.py = box191 idealcyc trajectory state by state on every
instance below), and switches only on a strict improvement. F1 (box 192): Ω_t(v) is ⊴-non-decreasing in t for every vertex v.
For an option o of mover x write g_o for its gate vertex, and D(g_o) for the number of distinct values Ω_t(g_o) over the run.
**Lemma SWITCH-IN-DV.** The number of steps t ≥ 1 with σ_t(x) = o ≠ σ_(t−1)(x) is at most D(g_o).
Proof.
- Let t ≥ 2 be such a step and o′ := σ_(t−1)(x). Howard moved x off o′, so Ω_(t−1)(g_o) ▷ Ω_(t−1)(g_o′).
- σ_(t−1)(x) = o′ was chosen from Ω_(t−2), so Ω_(t−2)(g_o′) ⊵ Ω_(t−2)(g_o).
- F1 gives Ω_(t−1)(g_o′) ⊵ Ω_(t−2)(g_o′). Chaining: Ω_(t−1)(g_o) ▷ Ω_(t−2)(g_o). So Ω(g_o) increases strictly from state t − 2 to t − 1.
- Different steps t give different pairs (t − 2, t − 1). The strict increases of Ω(g_o) number at most D(g_o) − 1. Add the step t = 1. ∎
Corollary REARM-DV. Let b be a lane node (level 0) with options EXIT (β → X) and CHAIN (β → the next lane node, or → the root d).
- A level-0 option's e-face leads to c_W, so Odd always takes its β-face. If g is not on its own cycle, Ω(g) = ext(g, ext(β, Ω(X)))
  and ext is injective (F3, F4). If it is, Ω(g) takes one value. So D(g_EXIT) ≤ D(X) + 1.
- So b re-arms (adopts EXIT) at most D(X) + 1 times. The first lane node b_0 adopts CHAIN at most D(d) + 1 ≤ D(Y) + 2 times, where Y
  is the root's target. ∎
Corollary REARM-PAIR. A mover with exactly two options alternates between them. So the number of complete re-arm / re-chain cycles at
b_0 is at most min(D(X) + 1, D(Y) + 2). A lane that re-arms at R events needs D(X) ≥ R − 1 and D(Y) ≥ R − 2. Moreover, between two
re-arms the order of Ω(EXIT) and Ω(CHAIN) at b_0 flips twice. So X-routes and Y-routes overtake each other (OVT-DV setting, R217 §2). ∎
- Meaning for counters. In [F09] a bit hides in a shared lane, and the lane must re-arm at every set event: Θ(2^n) times. So some exit
  target and some root target must each take Θ(2^n) values and overtake each other Θ(2^n) times. This is not an obstruction (values
  can count in binary over e's). It is the necessary shape of any design.

## 2. Test (1): hub H that tracks only the highest set bit (t1.py; DATA; DEAD)
Construction T1(n, M, ROOT) (experiments/red/r218/t1.py; d = 2):
- Bits B_k (level 1): SET_k (escape e_k → F_k → U_k), lane options → a_m for m < 2k + 2 (bits hide in the shared lane), and
  ACC_kj for j > k: an access mover A_kj with a copy gate (e-face e_acc → U_j, β-face → B_j); e_(j−1) < e_acc(·, j) < e_j.
- U_k (level 0): upper selector → B_(k+1) … B_(n−1) or s. F_k: M movers, EXIT → H, CHAIN → next (end → U_k).
- Hub H (level 0): → s or → probe C_k. C_k is a copy gate: e-face e_ck → s, β-face → B_k with the top odd β. Probe e's lie below every
  bit e: e_c0 < … < e_c(n−1) < e_0. If B_k is set, Odd takes e_ck (smaller), so H picks the highest set bit. If B_k is open, the
  β-face is either an odd-topped cycle through H or B_k's hidden route, and H does not pick it.
- Shared lane a_m (even β, increasing) → b_m; b_m: EXIT → H or CHAIN → b_(m−1) (b_0 → d); d: bonus even β → ROOT (s or H).
- (A first version had the probe β at 45, below the lane bonus 50. Then H → C_2 → B_2 → lane → d → H was an even-topped cycle, and Odd
  escaped to e_c2 while B_2 was open. Fixed: probe β 60. Only the fixed version is reported.)
DATA (out/t1_meas.txt, own.py; unit: steps; re-arms = switches INTO an option labelled X, over all lane / F movers; D(H) = distinct
values of Ω(H); set: n ∈ {2, 3, 4, 5, 6, 8}, M ∈ {0, 2}, ROOT ∈ {s, H}; scope IDEAL-CYC):

| n | ROOT | M | N | T | bit words visited (high … low) | re-arms total / max per mover | D(H) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | s | 2 | 34 | 12 | 000 001 011 110 100 111 110 111 | 9 / 1 | 4 |
| 4 | s | 2 | 46 | 14 | 0000 0001 0011 1010 1000 1111 1100 1110 1111 | 11 / 1 | 4 |
| 5 | s | 2 | 59 | 16 | 10 words | 13 / 1 | 4 |
| 8 | s | 2 | 104 | 22 | 13 words | 19 / 1 | 4 |
| 4 | H | 2 | 46 | 12 | 0000 0001 0011 0010 0111 0100 1110 1111 | 0 / 0 | 5 |
| 5 | H | 2 | 59 | 16 | 00000 00001 00011 00010 00111 00100 01110 01000 11100 11110 11111 | 0 / 0 | 6 |
| 6 | H | 2 | 73 | 20 | 14 words | 0 / 0 | 7 |
| 8 | H | 2 | 104 | 28 | 20 words | 0 / 0 | 9 |

- ROOT s: once any bit is set, EXIT (probe e) beats CHAIN (no e) for good. The lane chains once, then never again. T = 2n + 6 (M 2).
- ROOT H: exits and chain end in the same hub, so every change of H reaches both in the same step. The lane never re-arms. T = 4n − 4 (M 2, n 4-8).
  The words show the pattern «each new highest bit resets the bits below it once»: 00010 → 00111 → 00100 → 01110 → 01000 → 11100.
  That is n carries, not 2^n.
- Four routes agree on every instance checked (out/t1_xcheck.txt: n 3, 4, 5, 8; both ROOTs): own.py trajectory = box191 idealcyc;
  subrun191 C 0, R / p as listed; Γ3 (gamma3.build, all pads) solved by Oink 8fbf0a7 --zlk, regions = n5v xi = n5bxi, verify.check 0
  errors on both; N5′-xi iterations n5v xi = n5bxi = T + 3 (e.g. n 8 ROOT H: T 28, xi 31, Γ3 n 2018).
- Frozen: experiments/red/r218/inst/t1_n{3,4,5,8}_M2_s.json, t1_n{5,8}_M2_H.json (+ .names / .labels; sha1 in inst/SHA1SUMS).
- Verdict: test (1) is DEAD as a counter; linear, as the predecessor's reading said. REARM-DV turns the reading into a bound:
  re-arms per lane node ≤ D(H) + 1. D(H) ≤ n + 1 is DATA here; for this H it holds because Ω(H) is fixed once the highest set bit is
  fixed and that bit only rises (READING).

## 3. Test (2) v1: hierarchical prefix hubs (t2.py; DATA; DEAD)
Construction T2(n, M, ROOT): as T1, but every bit k ≥ 1 has its OWN lane (length 2k + 2), and that lane's exits go to P^k, a probe chain
over the lower bits (copy k). The probe P^k_j is a copy gate: e-face e_m(k, j) → P^k_(j−1) (→ s at j = 0), β-face → B_j (top odd β).
Mirror e's lie below every bit e and are ordered by (j, k). The lane root d_k → ROOT (s or P^k). F_k exits → P^k.
- Encoding (READING, checked on the runs): if B_j is set, the β-face carries e_j, so Odd takes the mirror. If B_j is open, the β-face
  enters B_j's hidden route → lane_j → P^j. That carries only mirrors of bits below j, while the e-face carries e_m(k, j), which ranks
  above them. So Odd takes the β-face, and no mirror is collected for j. Hence Ω(P^k) = the set of mirrors of the set bits below k:
  up to 2^k values. In the runs, D(P^(n−1)) = 2n + 1 (n 3-6).
**Lemma MIRROR-NOLEAK (PROVED, lane; from E-DOM-CHOICE).** Let B_i be on SET_i at a state, and let o be another option of B_i whose
play, before it merges with SET_i's play, contains no e-vertex more relevant than e_i. Suppose also that the merge vertex lies after e_i
on SET_i's play and Λ is shared and below e_i. Then Ω(SET_i) ▷ Ω(o).
- Proof: apply E-DOM-CHOICE with ε := e_i ∈ B′ (SET_i's pre-merge part) and A′ := o's pre-merge part. ∎
- Use: an access or lane option through an open bit's hidden route whose pre-merge part carries only mirror e's (all below e_i)
  cannot reset B_i. This is the leak of LEAK-ARCH (H1) avoided: hubs built from mirror e's ranked below the bit e's do not leak.
**Lemma SET-ROUTE-WINS (PROVED, lane; from E-DOM-CHOICE).** Let V be a mover with options o_a, o_k entering the bit movers B_a, B_k
(a < k), with B_a on SET_a and B_k open. Suppose B_k's hidden route contains no e-vertex more relevant than e_a before it meets
SET_a's play, and the plays share Λ below e_a. Then Ω(o_a) ▷ Ω(o_k).
- Proof: E-DOM-CHOICE with ε := e_a, which lies on o_a's play before the merge. ∎
- Use: under the no-leak condition, no selector can sit on «the lowest open bit above i» while a set bit lies between. So a carry into j
  cannot reach a set lower bit i through a hub that already passes the open B_j. The reset must come from an option that switches
  at the carry (RS2's access copy). Then the reset bit sits on a real-e option, and it re-sets as soon as its own chain is fresh
  (R217 §12, CHAIN-SHIELD).
DATA (out/t2_meas.txt; own.py; set n 3-6, M 0 / 2, ROOT s / P):
- ROOT s, M 0: T = 2 for every n (word 0…01 → 1…1: once B_0 sets, every higher lane's exits show a mirror, and all bits set at once).
  ROOT s, M 2: T = 2n + 1, words 0…0 → 0…01 → 1…1 → 10…0 → 1…1 → 110…0 → … (one reset wave, then refill). Re-arms ≤ 1 per mover;
  D(P^(n−1)) = 3.
- ROOT P: T = 2n + 2, words 0…0 → 0…01 → 0…011 → … → 1…1 (unary fill, no carry ever resets a lower bit, because the lower bits' SET
  chains reach every new set bit at once: CHAIN-SHIELD). Re-arms 0 (M 0) or ≤ 1 per mover (M 2); D(P^(n−1)) = 2n + 1.
- Four routes (out/t2_xcheck.txt: t2_n4_M2_s, t2_n6_M2_s, t2_n6_M2_P, t2_n6_M0_P): own = idealcyc, subrun191 C 0, Γ3 regions = Oink
  = n5v xi = n5bxi, verify 0 / 0, xi = T + 3 (n 6 ROOT P: T 14, xi 17, Γ3 n 1999).
- Frozen: inst/t2_n4_M2_s, t2_n6_M2_s, t2_n6_M2_P, t2_n6_M0_P (.json + .names + .labels; sha1 in inst/SHA1SUMS).
- Verdict: DEAD as a counter. The hub is rich (it counts the lower state) and does not leak, but a lane needs a PAIR of hubs that
  overtake (REARM-PAIR). Here Y is s (D 1) or Y = X.

## 4. The hub pair (the open crux, sharpened; READING plus one DEAD instance)
Needed (REARM-PAIR): for bit k's lane, two hub values X_k, Y_k that overtake each other at every event of the lower counter. Every
increment flips bit 0, so sign(Ω(X_k) − Ω(Y_k)) must depend on bit 0. Both values must also rise at every carry, so both must encode
the lower state.
- **Lemma PLAY-BLIND (PROVED-CONDITIONAL on F1, lane).** Let v be any vertex at state t, and let π be its play under (σ_t, τ_t), with
  τ_t Odd's optimal counterstrategy. If π contains no mover that switches at step t + 1, then Ω_(t+1)(v) = Ω_t(v).
  - Proof: σ_(t+1) agrees with σ_t on every mover of π. So under (σ_(t+1), τ_t) the play from v is again π, with the same value. Odd's
    optimal value is at most the value of any Odd strategy, so Ω_(t+1)(v) ⊴ Ω_t(v). F1 gives ⊵. ∎
  - Use (ODD-BLIND): a hub sees the SET of B_j at step t + 1 only if its play at t passes B_j or another mover that switches at t + 1.
    A hub that is to react to bit j's SET therefore passes B_j while B_j is open, i.e. it follows B_j's hidden route. That route is the
    same for every hub (one successor per vertex), so private copies cannot change it.
- Order of reading. Two plays that merge coincide afterwards. So X_k and Y_k can differ only before their merge vertex.
  - Top-down chains (T2's P^k: bit k − 1 first): they divert at the HIGHEST open bit. The pre-merge part holds the leading ones of the
    lower counter, which change only at carries into the top. Bit 0 is read after the merge. No pair.
  - Bottom-up chains (bit 0 first): they divert at the LOWEST open bit j, i.e. after the trailing ones. The decision works abstractly:
    with copy B's mirrors ranked above copy A's at every level, and the bit-0 probe β's deciding when bit 0 is open, X ▷ Y iff the
    counter is even. But then the rest of the value (bits above j) must come from B_j's hidden route, which must therefore go UP.
- Trilemma for an open bit's hidden route (READING; each branch with its mechanism):
  (a) Down (T2): no cycle, no leak, but no pair (above).
  (b) Up through the real chain (the upper selectors U, which pass every set bit): then a set bit i's own lane option reaches its own
      SET gate after carrying mirror e's. The merge vertex is SET_i's gate, so SET_i's pre-merge part is empty, and E-DOM-CHOICE makes
      the lane option win: a premature reset. This is LEAK-ARCH's H2 case.
  (c) Up through the mirror chain C (bottom-up probes of every bit): B_j's route passes the probe of the open bit k, hence lane_k,
      hence X_k / Y_k, which read bit j again: a cycle. Odd keeps it if its top is odd, so every hidden route through it looks
      terrible. Otherwise Odd breaks it at a probe e-face, which misreads an open bit as set.
- DEAD instance for (c): T3(n, UP, TAIL) (r218/t3.py; per-lane hub pair XA_k, XB_k = bottom-up probe copies A / B, root selector T_k,
  B_0's hidden route → C_1). At state 0 (all bits open) the play from C_1 is the cycle C_1 → B_1 → a1_0 → b1_0 → PA1_0 → B_0 → C_1
  (out/t3_play.txt). Its top vertex is the odd β of the probe PA1_0, so Odd keeps it. Every bit then sets at step 1
  (word 0…0 → 1…1) for every n 3-6, UP 0 / 1, TAIL C / s. T = 2n + 2 or 2n + 3; D(hubs) ≤ 3; re-arms ≤ 1 per node.
  Four routes (out/t3_xcheck.txt, n 4 and 6, UP 0, TAIL C): own = idealcyc (T 10 / 14); subrun191 C 1 (the state-0 cycle is left at
  step 1: Λ changes from that β to K1), R 6 / 10; Γ3 regions = Oink = n5v xi = n5bxi, verify 0 / 0, xi = T + 3 (13 / 17).
  Frozen: inst/t3_n4_u0_C.json (sha1 5ec72f3b…), t3_n6_u0_C.json (+ names / labels; inst/SHA1SUMS).
- A «third chain» that goes up through the bits with copy gates whose e's lie below the mirrors (witnesses instead of mirrors) IS
  branch (c). An open bit's copy gate still hands the play to its hidden route, so the cycle is the same whatever the witness ranks.
  Not excluded by anything proved: a reset mechanism other than access copies, or hidden routes that read the bits above j through a
  structure that is not a chain of per-bit gates.
- CYCLE-BREAK (READING, from the T3 run and the structure). Any lane hub that reads bit 0 enters B_0's hidden route (ODD-BLIND). If
  that route goes up through probes of every bit, then with B_0 and B_u open the play closes a cycle through lane_u. The only Odd vertices
  on that cycle where Odd can leave it are probes: the global probes C_1 … C_u and lane u's private probes. Level-0 gates send their
  e-face to c_W, and a bit's lane-option gates send theirs to DUMMY, so Odd never leaves there. So Odd must either keep the cycle (odd
  top: every hidden route through it looks terrible, and all bits set at once, as in T3) or misread some probe. A global misread at C_u
  drops bit u from every hub. A private misread at lane u's bit-0 probe kills lane u's parity pair.
- Even-reading instead of Odd-reading: a level-0 selector that enters a bit when it is set reads by going INTO the set bit's real
  chain. Bottom-up, that is «go to the lowest set bit», i.e. [F09]'s s-hub, which is LEAK-ARCH's H1.

## 5. Next
1. Try to make §4 a lemma («under E-DOM, no hub pair over a common bit-probe chain overtakes at every bit-0 event»), or build a pair with
   private copies of the low bits' hidden routes. Each copy costs O(k) per lane, still O(n²) in all.
2. A reset mechanism outside access copies that lands the reset bit in its lane. SET-ROUTE-WINS says it must switch at the carry.

## 6. H1 hub WITHOUT access edges (Lead 20:01Z hint from L-NEW 61 box 193; t4.py; DATA; DEAD)
Hint, as relayed (not opened by me as a source; L-NEW's file docs/new/N5-ASC-box193.md @ claude/l-new 2dc81001): all 2^M e-sets need
an H1-type (lowest-first) hub; LEAK-ARCH kills H1 only together with H2 + H3 (access edges). So: an H1 hub whose lanes are re-armed
without access edges.
**Fact E-CYCLE (PROVED, lane; from E-DOM-ALL-d).** In IDEAL-CYC of any genome, at any d, every cycle of a play that contains an
e-vertex has an even top. So Even wins it, with Λ above every play that ends in K1.
- Proof: c_W has only its self-loop. K0 and K3 lead only to K2 and K1, which never return. So a cycle with an e contains neither, and
  its most relevant vertex is an e (E-DOM-ALL-d), whose priority is even. ∎
Construction T4(n, ROOT, PROBE) (r218/t4.py): bits B_k with SET_k (e_k → U_k, U_k = upper selector → B_(k+1) … or s) and lane options
→ the shared lane (2k + 2 entries). NO access options. Lane exits → hub S; S → s or → B_k (PROBE 0), or → B_k through a copy gate Q_k
(PROBE 1: e-face e_q(k) → U_k with e_k < e_q(k) < e_(k+1), so Odd ENTERS a set bit; β-face → B_k with the top odd β). S is therefore the
lowest set bit's SET play, which runs up through every set bit (H1). Root d → s or → S.
DATA (own.py; n 2-6; out/t4_meas.txt):
- PROBE 0: no bit ever sets (words 0…0 only). S enters an open bit, and S → B_k → lane → d → S is a cycle whose top is the lane bonus
  (even): every value is Even-won above K1, and no SET improves on it. T 2 (ROOT s) / 4 (ROOT S).
- PROBE 1, ROOT S: bits set ONE AT A TIME and each resets at the next step: 0…01 → 0…0 → 0…010 → 0…0 → … (n 6: 11 words, T 14 = 2n + 2).
  ROOT s: T 9, e.g. 000001 → 000010 → 011100 → 000000. No bit stays set while a higher one sets; there are no carries.
- Mechanism (out/t4_play.txt, n 3, ROOT S, t 4-5): U_0's best option is the OPEN bit B_2, whose hidden route runs lane → d → S. Once S
  enters B_0 (t 5), B_0's escape e_0 → U_0 → B_2 → lane → S → Q_0 → B_0 closes a cycle through e_0. By E-CYCLE it is Even-won with top
  e_0, so Odd declines the escape and HIDES SET_0 (its β-face: the smaller even cycle B_0 → β_set → B_0). The set bit is reset by Odd's
  choice, not by any access edge.
**Proposition H1-CYCLE (PROVED, lane; from E-CYCLE).** Assume (H1′) every open bit's hidden route reaches a hub S whose play enters
the escape e_l of a set bit B_l, and (U) some Even mover on e_l's escape continuation has an option whose play enters an open bit. Then
that option's play is a cycle through e_l. So it is Even-won and beats every K1-play: Howard takes it at the next step unless an
option of equal Λ is already chosen. After that, Odd's optimal response must leave the cycle at an Odd vertex on it. The only Odd
vertices there whose other face is not c_W or DUMMY are SET gates (hiding a set bit) and probe gates (misreading a bit).
- Proof: the option's play passes the open bit, then its hidden route to S, then e_l, then the continuation back to the mover: a cycle
  containing e_l. E-CYCLE. The Odd vertices of IDEAL-CYC are gates; a level-0 gate's e-face leads to c_W and a lane option's to DUMMY. ∎
- Avoiding (U) needs the escape chain to read the higher bits without entering open ones. With Even-reading (a selector enters a bit),
  (U) holds whenever a higher bit is open. With Odd-reading (a probe whose β-face enters the bit), Odd enters a set bit only if the
  skip face is ⊵ the SET face. That means a skip e above e_j, so open bits would count MORE than set bits. That inverts the order the
  counter needs (READING).
- So under E-DOM, H1 fails without access edges as well: by H1-CYCLE (T4, instances below), or by the inverted reading.
- Frozen: inst/t4_n4_S, t4p_n4_S, t4p_n6_S, t4p_n6_s (.json + names + labels; inst/SHA1SUMS).
- Four routes (t4_n4_S, t4p_n4_S, t4p_n6_S, t4p_n6_s): own = idealcyc; subrun191 C 2 / 5 / 9 / 4 (the cycle changes are counted as C
  steps); Γ3 regions = Oink = n5v xi = n5bxi, verify 0 / 0, xi = T + 3. File out/t4_xcheck.txt.
- Not addressed: L-NEW's ASC-GATE cases (ii) «the declined escape reaches b» and (iii) «reaches an e above b» as re-arming mechanisms.
  T4's hiding is case (i): the declined escape reaches a better cycle node (the e_0 cycle). I did not open box 193 and have not built
  (ii) or (iii).
