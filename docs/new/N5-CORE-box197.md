# Box 197 (D18): Howard on Γ3 against Lemma BIN; the open core is the top re-entries (L-NEW successor 65, Opus; 2026-11-08, date -u)
Lead brief (10:18Z «go»): «find WHICH property of Howard's dynamics on Γ3(G) excludes BIN's 2^M − 1 hub-value runs, or show by a built
instance that Howard realizes them … Labels: PROVED (lane) / CONJECTURE / DATA / DEAD; every DATA clause names its counter».
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Not M3, not M4, not a gauntlet step-4 pass.
Tools: experiments/new/box197/asc197.py (counters), dump197.py (one e-set sequence); output box197/sweep197.out (record; run from the
scratchpad copy of the same code with ROOT set); check197.sh (a fixed subset, ~8 s), output check197.out, re-run by check.sh block «BOX 197 CORE».

## 0. Answer so far (one paragraph)
- Neither half of the brief is closed. I did not build a BIN run, and I did not find a Howard invariant that excludes one.
- What is new: (i) two game lemmas CS(M) lacks (ASC-WIT, ASC-ROOT, §2): an ascent of a hub's e-sequence exists only while Odd, at a gate
  below it, avoids a W-face whose cycle node is STRICTLY better than the hub's; (ii) an exact reduction of the open core (§3, Theorem
  RE-EQUIV): first entries of e-vertices are polynomially many for free, so T3 is polynomial iff the number Rtop of TOP RE-ENTRIES (a
  change of an e-set whose most relevant new element had been in that e-set before, in the same Λ-interval) is; BIN is the case where
  every change but M is a top re-entry; (iii) a D18 link (§4): the sequence of tops of one vertex is a Davenport–Schinzel-type sequence; a
  fixed bound on its alternation order s would make T3 polynomial (λ_s near-linear); BIN's tops (the ruler sequence) have unbounded order.
  DATA: the order grows slowly with L-SI's tower height (alternation 3, 4, 4, 5 on TC2, TC3, TC4m, TC5m), so this is an OPEN question,
  not a conjecture I can back.

## 1. Setting and premises
- HOW3(G), T3, n3 = N + 7M + 10, Ω_t, σ̄_t, seq_t(v), E_t(v), class_t(v) = (Λ_t(v), E_t(v)) and D^tot_E(v) exactly as in P-N5-CHAIN
  (docs/new/P-N5-CHAIN.md frozen at l-new 93531b03, §2 and §5-§7). Used from it (lane, REFEREE 29 SIGN, landing pending): F1, F2, F3, CYC
  (§4); CN2-3, LOC-GATE3, B-ONLY3, NO-TIE3 (§5); Corollary T-QUIET3 (§6); E-MON3, CHAIN-DECOMP3 (§7); HYPOTHESIS [E-LEV] (§1) for §2 only.
- CS(M), forest, run, hub: P-N5-ASC §2. Lemma BIN: L-RED 59, docs/red/R225-core.md §2 (claude/l-red 65ffc396): CS(M) has a run whose
  hub takes 2^M − 1 values (S_t = the set bits of t, next_t(x) = the next set bit above x).
- lev(e_(x,k)) := lev(x); lev(g) := lev(x) for the gate g = (x, k). Under [E-LEV], f more relevant than f′ implies lev(f) ≥ lev(f′).

## 2. Ascents need an avoided better cycle (PROVED, lane, under [E-LEV])
**Lemma ASC-WIT.** Let t be a state, v a vertex, seq_t(v) = (c_1, …, c_p), w := Λ_t(v), and c_(i+1) more relevant than c_i. Let y be the
successor of c_i and g1 the gate of σ_t(y) (the play runs c_i → y → m → g1). Then
(a) σ̄_t(g1) = pβ_(g1); (b) Ω_t(pe_(g1)) ⊳ Ω_t(pβ_(g1)); (c) if Λ_t(pe_(g1)) = w, then E_t(pe_(g1)) contains an e-vertex at least as
relevant as c_(i+1); (d) if Λ_t(pe_(g1)) ≠ w, the reward of Λ_t(pe_(g1)) is strictly larger than that of w.
Proof.
- y is a mover (CHAIN-DECOMP3), of level lev(c_i) − 1; the play from y passes its pad m and the gate g1 = (y, σ_t(y)).
- (a) If σ̄_t(g1) = pe_(g1), the play goes on to e_(g1). By B-ONLY3 every e-vertex is more relevant than w, so e_(g1) ∈ Π_t(v), and no
  e-vertex lies between c_i and e_(g1); so e_(g1) = c_(i+1). But lev(e_(g1)) = lev(c_i) − 1 < lev(c_i), so by [E-LEV] e_(g1) is LESS
  relevant than c_i: no ascent. Contradiction.
- (b) LOC-GATE3 and NO-TIE3.
- (c) The play from pβ_(g1) is a suffix of v's play: Λ_t(pβ_(g1)) = w and E_t(pβ_(g1)) = {c_(i+1), …, c_p}. With equal cycle nodes [VJ]
  compares Π: let z be the most relevant vertex of Π_t(pe_(g1)) Δ Π_t(pβ_(g1)). As in E-MON3's proof (E-DOM; c_W, K0, K3 are in both Π's
  or in neither when the cycle nodes agree), if the e-parts differ then z is an e-vertex, and z is even, so (b) puts z in Π_t(pe_(g1)).
  If the e-parts are equal, c_(i+1) ∈ E_t(pe_(g1)). Otherwise, if c_(i+1) ∉ E_t(pe_(g1)), then c_(i+1) is in the symmetric difference,
  so z is more relevant than c_(i+1).
- (d) [VJ] compares the reward of the cycle node first, and distinct vertices have distinct rewards (F2); with (b). ∎
**Lemma ASC-ROOT.** If seq_t(v) has an ascent and (c_i, c_(i+1)) is its first one, there is a gate g* with lev(g*) < lev(c_i),
σ̄_t(g*) = pβ_(g*) and Ω_t(pe_(g*)) ⊳ Ω_t(pβ_(g*)), whose W-face's cycle node Λ_t(pe_(g*)) has STRICTLY larger reward than Λ_t(v);
it is reached by at most lev(c_i) applications of ASC-WIT, each to the W-face pad of the previous gate.
Proof. Induction on ℓ := lev(c_i). Apply ASC-WIT to (v, i); if (d), g* := g1. Else Λ_t(pe_(g1)) = w. If lev(g1) = 0, e_(g1)'s successor
is c_W, so Λ_t(pe_(g1)) = c_W; but w ≠ c_W (E_t(v) ≠ ∅ and only K0, K3 lie above c_W, B-ONLY3); so lev(g1) ≥ 1, B-ONLY3 applies to
pe_(g1), and seq_t(pe_(g1)) starts with e_(g1) (level ℓ − 1) and by (c) contains an e at least as relevant as c_(i+1), which is more
relevant than c_i and so than e_(g1): seq_t(pe_(g1)) has an ascent. Up to its first ascent (c′_j, c′_(j+1)) the sequence only descends,
so lev(c′_j) ≤ ℓ − 1 ([E-LEV]). By induction (the base ℓ = 0 is vacuous: an ascent from a level-0 c_i would need c_i's successor to
be a mover, but it is c_W) there is g* with lev(g*) < lev(c′_j) ≤ ℓ − 1 whose W-face's cycle node beats Λ_t(pe_(g1)) = w. ∎
- What it gives: a game invariant that CS(M) lacks. In BIN every hub state with |S_t| ≥ 2 has an ascent, so in a game realization every
  such state must have, below the hub's first ascent, a gate where Odd avoids a W-face with a strictly better cycle node. It is a
  property of every state (any σ against an optimal σ̄), not of Howard's rule, and it does not bound anything by itself: avoided better
  cycles are cheap to build. I record it because any BIN embedding must supply these witnesses, and because the witness chain is the
  natural place where Howard's rule (every mover to its ⊴-best successor) has to enter.
- DATA (counters awA, awB, rootfail in asc197.py; unit: (state, vertex, ascent) triples; set and scope in §5): all 0; controls fire.

## 3. The open core is the top re-entries (PROVED, lane, on P-N5-CHAIN's premises; no [E-LEV])
Definitions. For a vertex v, a Λ-interval I of v is a maximal interval of states on which Λ_t(v) is constant. Inside I, a change is a
step t − 1 → t with E_(t−1)(v) ≠ E_t(v); its top is the most relevant e-vertex of E_(t−1)(v) Δ E_t(v). Mact_I(v) := |⋃_(t∈I) E_t(v)|. A
change is a top re-entry if its top lies in E_s(v) for some s ∈ I, s < t − 1. Rtop_I(v) := the number of top re-entries in I;
Rtop := Σ_v Σ_I Rtop_I(v).
**Lemma RE-COUNT.** D_I(v) := |{E_t(v) : t ∈ I}| ≤ 1 + Mact_I(v) + Rtop_I(v).
Proof. By E-MON3 every change is a strict lex increase, so the top lies in E_t(v) \ E_(t−1)(v), and the sets of I are pairwise distinct:
D_I(v) = 1 + (number of changes). A change whose top is not a re-entry is the first entry into ⋃ E of its top; there are at most
Mact_I(v) of those. ∎
**Theorem RE-EQUIV.** With L3 and n3 as in P-N5-CHAIN,
  T3 ≤ (1 + n3·((2M + 3)(M + 1) − 1) + Rtop)·(L3 + 1), and Rtop ≤ n3·T3.
So T3 (and N5′-xi's iteration count on Γ3, by P-N5-END's ENDGAME-3) is polynomial in N + M iff Rtop is.
Proof. By F1 and F2, Λ_t(v) changes only to a vertex of strictly larger reward, so the Λ-intervals of v have distinct cycle nodes, and
by CYC there are at most 2M + 3 of them. Classes of different intervals differ in Λ, so D^tot_E(v) = Σ_I D_I(v) ≤ Σ_I (1 + M + Rtop_I(v))
(RE-COUNT, Mact ≤ M) ≤ (2M + 3)(M + 1) + Σ_I Rtop_I(v). Sum D^tot_E(v) − 1 over the n3 vertices and use T-QUIET3. For the second bound,
each top re-entry is one change of one vertex at one step, and a vertex changes at most once per step. ∎
- Reading. Lemma EQUIV (R225-core §1) says Σ_v D^tot_E ≍ T3, so CHAIN3's residue restated G-N5-TIME on Γ3. RE-EQUIV sharpens it: the
  first entries, which are what P-N5-ASC's HUB-ASC counts through ascents, are polynomial without any ascent bound; what is not bounded is
  how often an e-vertex comes BACK as the most relevant new element. In BIN, item 1 comes back 2^(M−1) − 1 times, item 2 2^(M−2) − 1
  times, …: all but M of the 2^M − 2 changes are top re-entries.
- A built BIN run is therefore exactly a family with Rtop exponential. Howard's rule must exclude it, or allow it, through the dynamics
  of top re-entries: the most relevant new e of a vertex's play returns after a more relevant one has entered and (by lex monotonicity)
  stayed, i.e. only BELOW a more relevant element that is fixed. This is the shape of a counter's carry, and also of L-SI's ACCESS-LATCH
  / LEAPFROG towers (claude/l-si docs/si/box83-ladder.md §2, cited, not re-read here).

## 4. D18: tops as Davenport–Schinzel sequences (READING and DATA; OPEN)
- For one (v, I), list the tops of its changes: τ_1, τ_2, …. Two consecutive tops differ (the top of a change is in the new set, the next
  top is not in the old one). So it is a sequence over Mact_I(v) symbols without immediate repetitions, as in Davenport–Schinzel theory.
- If for a fixed s no two symbols alternate s + 2 times (x … y … x … y …) in any tops sequence, then the length is at most λ_s(M), the
  DS maximum (λ_1(n) = n, λ_2(n) = 2n − 1, λ_3(n) = Θ(n α(n)), near-linear for every fixed s). With RE-COUNT this would give
  D_I(v) ≤ 1 + λ_s(M) and T3 ≤ (1 + n3((2M + 3)(1 + λ_s(M)) − 1))(L3 + 1): polynomial.
  Source to open before any citation in a packet: Sharir–Agarwal, «Davenport–Schinzel sequences and their geometric applications»
  (Cambridge UP 1995), Ch. 1-2 for λ_2 = 2n − 1 and λ_3 = Θ(n α(n)). NOT opened in this box; nothing above depends on it (the
  implication is the definition of λ_s).
- BIN's tops form the ruler sequence 1, 2, 1, 3, 1, 2, 1, 4, …: items 1 and 2 alternate 2^(M−1) times. So «bounded DS order» is exactly
  a property that excludes BIN, and it is a statement about Howard's dynamics, not about CS(M).
- DATA (counter maxalt in asc197.py: the longest alternation of two symbols in one tops sequence; unit: (genome, v, I); set §5): random
  families: maxalt ≤ 3 (1,600 runs); pinned genomes: maxalt up to 5 (CL2_21, CL2_22, TC5m, rd2_d9). Along L-SI's tower genomes TC2, TC3, TC4m, TC5m:
  3, 4, 4, 5. It grows with the tower, slowly; four points do not separate a constant, log or linear order. OPEN; I do not state a
  conjecture.
- Other D18 ideas tried and what each gives:
  - Monotone potential (Σ_v rank of Ω_t(v)): strictly increasing (F1), but the value lattice is exponential: gives nothing.
  - Matroid exchange over the policy sequence: a Howard switch set is not an exchange of a basis (several movers switch at once,
    and a mover's options are not a matroid on the e-vertices); I found no exchange axiom that the policies satisfy. Nothing.
  - Bellman–Ford layering (READING): on Ξ-acyclic genomes Rtop = 0 in every run of the acyc family (DATA §5), consistent with L-SI 43's
    ACYC-LIN (cited from R225-core §0, not re-read). Top re-entries seem to need upward Ξ-edges feeding values back down, the feedback
    that counters use; I have no proof of this.

## 5. DATA (tool experiments/new/box197/asc197.py on P-N5-CHAIN's engine: box 189 gamma3.build, box 190 n5v.step mode xi from S3, up to
## the first fallback; output box197/sweep197.out)
- Set: box195 eg195.gen families rand, esc, noesc, deep, dense, lvl0, late, acyc × 200, seed 1971 (1,600 runs); the 69 pinned genomes of
  box196/inst, box196/inst_si85 (L-SI's 11 box-85 towers), box191-box195/inst, box189/corpus (DEAD_SEGT_n20 skipped: not a genome).
  Scope: gamma3.py's e-priorities by (lev, gate), so [E-LEV] holds.
- Counters, all 0 on every row: awA, awB (ASC-WIT; unit: (state, vertex, ascent)); rootfail (ASC-ROOT; unit: (state, vertex with an
  ascent)); dfail (RE-COUNT; unit: (v, I)); lexdec (E-MON3 restated; unit: changes).
- Controls fire: ctrl1 (faces swapped) awA 1,070; ctrl2 (reward test reversed) rootfail 1,062; ctrl3 (awB target above all of E(v))
  awB 430 (deep, seed 1973, 30 runs each); ctrl4 (Rtop := 0 in RE-COUNT) dfail 72 (TC3).
- Record only: max ASC-ROOT depth (rounds of ASC-WIT) 8; max re-entries (top or not) in one (v, I): 66 (LEAP_k64) on the pinned set,
  1 in the random families; acyc family: Rtop 0; maxalt as in §4.
- Every run is short (max T3 129, LEAP_k64): the data test the lemmas, not any growth claim.

## 6. Next (for the Lead; nothing running)
- Coordinate with L-RED 59's composition test (multiply vs add): in TC5m (dump197.py) the hub x6's e-sets show a top-level change
  followed by a lower sweep, and the lower sweep after the second top change repeats the first (the columns after the first four of dump197.py's
  output at states 26, 28-31 equal those at 39-43); lower sweeps
  do not nest inside one another there. So on L-SI's towers the heights ADD per top change. READING on one instance.
- The measurable question that decides BIN: does maxalt (DS order of tops) stay bounded on a tower family of growing height? Next step:
  maxalt on L-SI's tower generator at heights 2..8 (needs its generator; read only, claude/l-si).

## Addendum 1 (L-NEW successor 65, 12:12Z by date -u; Lead 10:55Z: «open the source … state the bounded-order hypothesis as a CONJECTURE with its exact form»; tower family read-only from claude/l-si)
### Source opened (replaces the «not opened» note of §4)
- S. Pettie, «Sharp Bounds on Davenport-Schinzel Sequences of Every Order», arXiv:1204.1086 v2 (18 May 2013), opened 11:25Z-11:30Z:
  - §1, p. 1: an order-s DS sequence is «a repetition-free sequence over the alphabet {1, …, n} that does not contain any alternating
    subsequences of the form ··· a ··· b ··· a ··· b ··· with length s + 2»; λ_s(n) is the maximum length of one (§1.1, p. 2).
  - §1.2, p. 3: Davenport and Schinzel (1965) «proved that λ_1(n) = n, λ_2(n) = 2n − 1»; Szemerédi (1973) showed «λ_s(n) = O(n log* n),
    where the leading constant depends on s» (all s ≥ 3); Hart and Sharir (1984) settled λ_3(n) = Θ(nα(n)).
- Sharir–Agarwal (CUP 1995) NOT opened (not reachable from this container); Pettie §1.2 is the cited source. λ_s(n) is non-decreasing
  in n (a sequence over fewer letters is one over more).
### CONJECTURE DS-TOPS (exact form)
- For a vertex v of Γ3(G) and a Λ-interval I of v in HOW3(G) (§3), tops(v, I) := the sequence of the tops of the changes of E_t(v) in I,
  in time order. It is repetition-free (§4).
- **CONJECTURE DS-TOPS.** There is a constant s such that for every genome G satisfying [E-LEV], every vertex v of Γ3(G) and every
  Λ-interval I of v, tops(v, I) contains no alternating subsequence x … y … x … y … (x ≠ y) of length s + 2; i.e. tops(v, I) is an
  order-s Davenport–Schinzel sequence. The data (below) are consistent with s = 4 and with no smaller s.
- **Corollary DS-POLY (PROVED, lane, CONDITIONAL on DS-TOPS(s) and on P-N5-CHAIN's premises).** D_I(v) = 1 + |tops(v, I)| ≤ 1 + λ_s(M),
  so T3 ≤ (1 + n3·((2M + 3)(1 + λ_s(M)) − 1))·(L3 + 1), with λ_s(M) = O(M log* M) (Szemerédi, as above): polynomial in N + M.
  Proof: D_I(v) = 1 + (number of changes) (RE-COUNT's proof); the tops sequence is order-s DS over at most M letters; then as in RE-EQUIV
  with RE-COUNT's bound replaced. ∎
- It excludes BIN: BIN's tops are the ruler sequence (the top of the change t − 1 → t is the lowest set bit of t), which contains the alternation
  1 2 1 2 … 1 of length 2^(M−1) + 1 (M ≥ 2: item 1 is the top at odd t, item 2 at the 2^(M−2) values t ≡ 2 (mod 4), and an odd t lies
  between any two of those).
- What would kill it: one family of genomes (with [E-LEV]) whose maximum alternation in a tops sequence grows without bound.
### DATA: the tower family (counter maxalt of asc197.py; unit: (genome, v, I), max over the genome; scope [E-LEV])
- Set: L-SI box 85 two85.build (claude/l-si experiments/si/box85/two85.py + gen83.py, copied read-only into the scratchpad; check: cfg
  TC5m rebuilds byte-equal to box196/inst_si85/TC5m.json), cfg {w ["L"], lw ["M+"], lup "M+", lexit "M+"} (TC5m's), heights h = 2..8,
  three lane formulas per height (A: L = LL = (2, 5, 9, 14, 20, 27, 35, 44)[:h], LM_l = 6(l + 1); B: L_l = 3l + 1, LM_l = 5 + 4l, LL as A;
  C: L, LM random, seed 1970 + h, LL as A); generator box197/mkh197.py (argument: the folder holding the copied two85.py, gen83.py), instances box197/hfam/
  (21 genomes), output box197/hfam197.out (record; not re-run by check.sh).
| h | maxalt A / B / C | T3 A / B / C | longest tops sequence A / B / C |
  | --- | --- | --- | --- |
  | 2 | 2 / 2 / 2 | 9 / 8 / 13 | 3 / 4 / 2 |
  | 3 | 4 / 3 / 4 | 17 / 14 / 20 | 7 / 6 / 7 |
  | 4 | 5 / 4 / 4 | 25 / 20 / 31 | 9 / 8 / 10 |
  | 5 | 4 / 4 / 2 | 33 / 26 / 24 | 11 / 11 / 4 |
  | 6 | 4 / 4 / 4 | 41 / 32 / 51 | 12 / 14 / 12 |
  | 7 | 2 / 4 / 4 | 39 / 37 / 74 | 4 / 11 / 13 |
  | 8 | 2 / 3 / 4 | 47 / 46 / 80 | 4 / 6 / 16 |
- Every row: awA, awB, rootfail, dfail, lexdec 0 (§2, §3 counters).
- Reading: maxalt does not grow past 5 on this family up to height 8 (T3 up to 80), while T3 grows about linearly. Weak support for
  DS-TOPS with s = 4 on L-SI's towers; nothing about other families. L-SI's towers are the fleet's best designed counters on N5′-xi, so
  this is the family where growth would have shown first. Every run is short; the data test the conjecture only at these sizes.
