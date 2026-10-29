# Packet P-N5-MATCHPHI: inside one phase, the path-set changes of a vertex are at most (K(K+1)/2)(NM + 1) + NM, NM its carries (Lemma MATCH-Φ) — every game
L-LIT successor (Opus 5.5), D18, Lead reading L40. Lead's decision of 10:43Z (message): "freeze MATCH-Φ as a referee packet
docs/lit/P-N5-MATCHPHI.md, with its pinned check. The one statement it adds to RESULTS: "PCH_P(v) ≤ (K(K+1)/2)(NM+1) + NM per vertex per
phase"". Written 2026-10-29 from 10:55Z (date -u). FROZEN at push: later text goes into a fixes file (docs/lit/P-N5-MATCHPHI-fixes.md).

**What this is and is not.**
- It REDUCES the path-set changes of one vertex in one phase to its carries. A carry is a change that does not decompose into
  individually improving one-for-one rank exchanges.
- It does NOT bound the carries.
  - NM is OPEN. L-COMP box 18 DATA (claude/l-comp fc0758fc, experiments/n5-box18/README.md): max NM per (vertex, phase) 62 at n 581;
    max NM/n 0.90 on pinned starts and 1.18 on pl130_n40.
  - Monotonicity and the set order alone allow exponentially many carries (docs/lit/T33-match-phi.md §2.2, Part B of the check).
- Not a TARGET.md claim; no running-time bound; G-N5-TIME stays open.

**Labels.** PROVED (L-LIT, unrefereed; to sign) / DATA / READING.

**Working note.** docs/lit/T33-match-phi.md §1 (same content, with the ARV transfer discussion in §2). This packet governs.

**Pinned check.** docs/lit/T33-match-phi-check.py, sha1 6853179bf10bdf1c3d9cae61c939b1054aa4b70c, run as
`python3 -I docs/lit/T33-match-phi-check.py`. Expected output:
- Part A: `A: improving pairs 80640 | matched with phi rise < 1: 0 | carries: 32534`.
- Part B: eight lines `B: k=… strict-rise=True fixed-top=True carries(NM)=…`, NM = 0, 0, 1, 3, 7, 15, 31, 63 for k = 1..8.

**Quote check.** docs/lit/P-N5-MATCHPHI-quotecheck.py checks every [Q …] quote below against git at its commit. Expected output:
`quotes=5 bad=0`.

**Independent cross-check of the MATCHED test (DATA, L-COMP box 18 via the Lead's message of 10:43Z).** "Matching rule cross-checked
against your T32 match(): 258,048 pairs, 0 disagreements."

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Definitions: pos, w, Φ, MATCHED / CARRY, NM | definitions |
| §2 | Fact 1 (MATCHED = decomposes into individually improving one-rank moves) | PROVED (to sign; elementary) |
| §2 | Lemma MATCH-Φ (Φ rises by ≥ 1 at every MATCHED P-change) | PROVED (to sign) |
| §2 | Corollary: PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) ≤ (n²/2)(NM + 1) + NM, per vertex per phase, every game | PROVED (to sign) |
| §3 | the pinned check (Part A brute force, Part B counter) | DATA (not to sign) |
| §4 | the ARV reading | READING (not to sign) |

**Premises (LANDED).**
- SPEC S1's rank and valuation:
  - [Q docs/new/N5-ssi-global.md@6abea2e6:27] «injective priorities: rank(v) = position of v in V sorted by (Ω(v), v); p'(v) = 2·rank(v) + (Ω(v) mod 2).»
  - [Q docs/new/N5-ssi-global.md@6abea2e6:28] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends in, P = set of»
  - [Q docs/new/N5-ssi-global.md@6abea2e6:31] «Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.»
- RESULTS R84 (a) Fact DELTA, signed by both referees:
  - [Q docs/RESULTS.md@6abea2e6:4967] «(a) Fact DELTA (§1, with F4): for sets A ≠ B of ranks, weight(B) > weight(A) iff d := d(A, B) is even and d ∈ B ∖ A, or d is odd and»
- R84's setting, which fixes P_t and the phase:
  - [Q docs/RESULTS.md@6abea2e6:4960] «P, then ℓ. v: a fixed vertex; c := λ(v), constant on P; P_t := P(Ξ_t v) ⊆ {u : rank(u) > rank(c)}, read as a set of ranks; top_t := the»
- The Lemma and the Corollary use none of (MON), R15 or R84's TOP-SHAPE. They need only that ranks are distinct and that P_t ⊆ R_c
  for every state t of the phase. (MON) and Fact DELTA are used only by Fact 1, which is the reading of MATCHED, not a step of the
  Corollary.

## 0. Setting
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md) with FIX 1-4. A phase 𝒫 is a maximal run of states with λ (Ξ's cycle-node map) and τ
  constant (RESULTS R38 (a), as in R84).
- Fix a vertex v. c := λ(v), constant on 𝒫. P_t := P(Ξ_t v), a set of ranks, ⊆ R_c := {rank(u) : rank(u) > rank(c)}.
- A rank r is EVEN or ODD as Ω of the vertex of rank r (R84 F5). K := |R_c| ≤ n − 1. r_1 < … < r_K are the elements of R_c.
- A P-change of v in 𝒫 is a transition t → t + 1 of 𝒫 (in-phase S4c fallbacks included) with P_t ≠ P_{t+1}. PCH_𝒫(v) is their number.

## 1. Definitions
- pos(r_k) := k (1 ≤ k ≤ K).
- w(r) := +pos(r) if r is even, −pos(r) if r is odd.
- Φ(A) := Σ_{r ∈ A} w(r) for A ⊆ R_c.
- A P-change A := P_t → B := P_{t+1} is MATCHED if there is a matching M ⊆ (A ∖ B) × (B ∖ A) (each rank in at most one pair) with:
  - (M1) w(i) > w(o) for every (o, i) ∈ M;
  - (M2) every i ∈ B ∖ A not covered by M is even;
  - (M3) every o ∈ A ∖ B not covered by M is odd.
- Otherwise the P-change is a CARRY. NM_𝒫(v) is the number of carries of v in 𝒫.
- Deciding MATCHED is a bipartite matching problem: cover the even outgoing and the odd incoming ranks with pairs satisfying (M1).
  It is polynomial per P-change.

## 2. Statements and proofs (PROVED, L-LIT, unrefereed; to sign)
**Fact 1.** For distinct ranks o, i, w(i) > w(o) iff weight({i}) > weight({o}). Adding an even rank, or removing an odd rank, raises
the signed weight. So a MATCHED change is one that decomposes into individually weight-raising one-for-one exchanges, additions of
even ranks and removals of odd ranks.

Proof. Fact DELTA on {o} vs {i}, d = max(o, i).
- If i > o, the exchange raises the weight iff i is even.
  - i even: w(i) = pos(i) > pos(o) ≥ |w(o)| ≥ w(o).
  - i odd: w(i) = −pos(i) < −pos(o) ≤ w(o).
- If o > i, the exchange raises the weight iff o is odd.
  - o odd: w(o) = −pos(o) < −pos(i) ≤ w(i).
  - o even: w(o) = pos(o) > pos(i) ≥ w(i).
- Additions and removals: Fact DELTA with d the added rank (∈ B ∖ A) or the removed rank (∈ A ∖ B). □

**Lemma MATCH-Φ.** At every MATCHED P-change A → B, Φ(B) − Φ(A) ≥ 1.

Proof. Φ(B) − Φ(A) = Σ_{i ∈ B∖A} w(i) − Σ_{o ∈ A∖B} w(o). Regroup the sum as:
- Σ_{(o,i) ∈ M} (w(i) − w(o)): each term is an integer ≥ 1 by (M1);
- Σ_{uncovered i} w(i) = Σ_{uncovered i} pos(i): each term ≥ 1 by (M2);
- −Σ_{uncovered o} w(o) = Σ_{uncovered o} pos(o): each term ≥ 1 by (M3).

All terms are integers ≥ 1, and there is at least one term since A ≠ B. □

**Corollary.** For every game, every vertex v and every phase 𝒫 of N5:
PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v) ≤ (n²/2)·(NM_𝒫(v) + 1) + NM_𝒫(v).

Proof.
- For every A ⊆ R_c, −Σ_{odd r} pos(r) ≤ Φ(A) ≤ Σ_{even r} pos(r). This interval has width W := Σ_{k ≤ K} k = K(K+1)/2.
- Along 𝒫, Φ(P_t) changes only at P-changes.
- Each MATCHED P-change raises Φ by ≥ 1 (Lemma). Each carry changes Φ by at most W in absolute value (both values lie in the
  interval).
- Summing over 𝒫: #MATCHED ≤ (total rise) ≤ W + (total fall) ≤ W + W·NM.
- Add the NM carries. K ≤ n − 1 gives K(K+1)/2 ≤ n²/2. □

**Remarks (not to sign).**
- R84's premise that every P-change of a phase strictly raises weight(P) is NOT used. The Corollary holds for any sequence of subsets
  of R_c.
- What N5 contributes is only the setting: P_t ⊆ R_c with c fixed on the phase.
- What makes the bound informative is the reading of Fact 1. Under N5's strict rise, a non-carry is an improvement made of
  improvements. A carry is a "1-k exchange": a single rank outweighs several others, which is where a binary counter would live
  (§4).

## 3. DATA (pinned check; not to sign)
- **Part A.** All ordered pairs (A, B) of subsets of K = 6 ranks with weight(B) > weight(A), for 40 random parity patterns (seed 1).
  Result: 80,640 improving pairs; 0 MATCHED pairs with Φ rise < 1; 32,534 carries.
- **Part B.** The ascending binary counter {T} ∪ {bits set} (k even bits below a fixed even top T). Results:
  - every change raises the weight;
  - the top is fixed;
  - NM = 2^{k−2} − 1 for k ≥ 2 (k = 8: 63 carries among 255 P-changes).
- So the Corollary cannot bound PCH without a bound on NM.
- **N5 data, not run by L-LIT (L-COMP box 18, via the Lead).**
  - Max NM per (vertex, phase): 31 on alt_all (0.775n); 62 at n 581; 47 = 1.18n on pl130_n40.
  - Carries are 60-75% of the P-changes on the long pins (pl130: 157 = 41 matched + 116 carries).

## 4. READING (not to sign)
- The Corollary transfers Ackermann-Röglin-Vöcking's rank-replacement argument (ECCC TR06-067, Lemma 4 and Theorem 3, p.5): a move
  that decomposes into non-worsening one-for-one exchanges lowers a rank potential.
- Their Def. 8 / Lemma 10 (p.7-9) build exponential best-response counters from 1-2 exchanges.
- docs/lit/T33-match-phi.md §2 records that the N5 facts (MON), λ and τ fixed, Fact DELTA and TOP-SHAPE do not exclude such a counter
  for one vertex. Only ARV's free schedule fails for N5.
- So a bound on NM must use S4a's rule. With L-COMP's data (NM ≤ 1.18n), CONJECTURE NM = O(n) per vertex per phase is the step that
  would turn this Corollary into an O(n³) bound on the path-set changes per vertex per phase. It is OPEN.
