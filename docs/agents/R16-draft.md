# Draft RESULTS R16 (Lead, 2026-10-19 02:35Z by date -u) — DRAFT, not landed; awaits CHECKER C19 (rev. 02:45Z: both §C-A1, K; rev. 02:55Z: REFEREE K attribution; rev. 03:14Z: C19 E-3, E-4, N-2..N-5)

### R16 [refereed-only] A_DTL on one-player games 𝒞^1P: the search count per phase is n^{O(NEST*)}, so GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED) (2026-10-19) — partial step-4 reduction on a subclass (not M3, not a step-4 pass, not M4)
- Object: A_DTL = `oink --dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, every order datum (frozen §0, L26). Class (GAP-A-M
  §27b): 𝒞_C (C ∈ {0, 1}): every vertex of player q = 1 − C has exactly one successor; 𝒞_C^dist adds: q's priorities are pairwise
  distinct; 𝒞^1P := 𝒞_0^dist ∪ 𝒞_1^dist. Packet P-C1P pinned at trunk 01d63d7 (docs/alg/GAP-A-M.md §27b, §28e, §33b, §35b, L-ALG
  successors 9-10; docs/red/R46-nest-bound.md §1, §2b, §3, L-RED successor 9) and addendum A1 pinned at trunk da63c40
  (docs/red/R47-chainkeep.md §1-§5, L-RED successor 9, l-red b9d7580).
- Claims signed (both referees, all labelled "(Opus 5.5, D12)"):
  (a) Lemma CTRL: in 𝒞_C every tangle that search(C) extracts is a dominion; player C makes ≤ n + 1 searches in the run.
  (b) Lemma NOSTEAL-1P: in 𝒞_C^dist, in every phase of q, under every order datum, there is no relevant steal (RESULTS R11
      definition) in any best_vertices context.
  (c) Lemma OUTCOME-MONO-1P: in 𝒞_C^dist, at a fixed context R in a q-phase, consecutive visits have monotone round sets
      V_r, a stable visit is followed by a stable one with V* nested, and a −1 visit by a stable one or a −1 one with
      emptying round e not smaller, and prevV nested when e is equal (e = the FIRST round with V_e = ∅).
  (d) Lemma SAME-CTX: equal depth-0 context SET R at a position in two searches of a q-phase ⇒ the call is a function of
      (R, T), its outcome does not fall, and with equal outcome the piece is ⊆-monotone (ρ carries the emptying round e;
      T-monotonicity on the consumed Dom subgame cites RESULTS R9 (b)).
  (e) Lemma LEX, in the form signed: at every transition whose depth-0 chain changes, the chain rises strictly in the
      tree-lexicographic per-context order; hence c(s′) ≤ c(s″) for all searches s′ < s″ of a phase. (The strict form "for ALL
      pairs" needs (CHAIN-CHANGE), DATA only; nothing below uses it.)
  (f) K-constraint (R46 §1): between two consecutive transitions at positions < p, at most K transitions have position p,
      K ≤ (n+2)²(n+1) = O(n³) (R46 §1 count; R47 §7 uses this signed K).
  (g) L-NEST* (R46 §2b): a sequence over m positions satisfying the K-constraint with NEST* ≤ d has length ≤ (2(d+2)m²K)^d;
      NEST* (first-to-last-occurrence nesting) is monotone under subsequences.
  (h) Lemma EMPTY-REC (R47 §1): in 𝒞_C (out-degree-1 hypothesis only), every recursive search_rec call of a q-search gets an
      empty subgame (dtl.cpp 898-955).
  (i) Theorem CK (R47 §2-§4): on 𝒞_C^dist every q-phase has I ≤ (n+1)(|P|+1)(H+1+n²) + 1 chain-keeping transitions (H from
      RESULTS R7 (d)), using Lemma DOM-MONO (fixed-input Dom step outputs monotone in T) and Lemma SPTL-SANDWICH; the case of e*
      in search()'s dominion attractor is excluded by STR-DET (RESULTS R8); CHECK_UNIQUE = 1 (dtl.cpp 23).
  (j) THEOREM (NEST*-BOUND with CK; R46 §3 + R47 §5): on 𝒞^1P every q-phase has S − 1 = |P| + I with
      |P| ≤ (2(d+2)(n+1)²K)^d, d = NEST*(P), and I as in (i). So S ≤ n^{O(NEST*)}, and with CTRL (≤ n + 1 searches for C) and
      the phase count, GAP-A on 𝒞^1P ⇐ (NEST*-BOUNDED): "NEST* ≤ c on 𝒞^1P for a constant c" (R46 §3; NEST* of the first-difference
      sequences P of the q-phases). ONE named statement; (CHAIN-CHANGE) is not needed.
- Honest limits: (i) a REDUCTION, not a bound: (NEST*-BOUNDED) is DATA only (class best NEST* 3: nest3_n20, nest3_n24), with no
  proof route; NEST* = Θ(log n) would allow up to n^{O(log n)}, so even its failure in that form would not give a super-polynomial
  lower bound. (ii) Subclass only: LEX fails in two-player games (GAP-A-M §36b), so (e)-(j) do not apply there; GAP-A in general
  is unchanged. (iii) The L32 criterion asks for one named statement WITH a proof route; this gives the statement, not the
  route. (iv) DATA caveats: REFEREE-2's DOM-MONO pairs (163) all had identical step vectors (vacuous as data; the verdict rests
  on the proof); REFEREE-2's logs are Oink order only.
- Data (DATA, not proof): REFEREE (lanes' tools, both orders): samectx 646 pairs 0 failures; lexchk 169 pairs per order 0
  violations; neststar K=2, d=2, m ≤ 3 far below the bound; dagchk 188 depth-≥1 calls, max |R| = 0. REFEREE-2 (own logging patch
  on pinned 8fbf0a7 + own analyser, Oink order): 13 pinned class instances, 0 violations of CTRL, CHAIN-CHANGE, LEX, K, the
  bound and CK (I = 0, total |P| = 79); 7,500 random class games 0 violations (trivial phases); nestbf = R46's tables. L-RED:
  DOM-MONO 12,043 + 1,434 same-input pairs per order, 0 violations (R47 §6).
- Signatures: REFEREE docs/referee/R-C1P.md (referee 2ad62df; §C 2d69929; A1 83c2916; §C-A1 4701783). REFEREE-2
  docs/referee-2/R2-C1P.md (referee-2 1ecc8d5; §C ff4011f; A1 8e7a02c + 22e5d2d; §C-A1 420b14b). Both §C-A1: no conflict. Closed gaps: S-1 = G-SC-1, S-2, S-3,
  G-SC-2 (REFEREE-2 citation point) (SAME-CTX), O-1/O-2 (OUTCOME-MONO-1P), N-1 (NOSTEAL-1P wording), R-1 (L-NEST* wording), A1-1..A1-5 and
  A1-G1/A1-G2, A1-N1..A1-N3. Closed by A1 for the theorem: R-2 = G-R46-1. L-1 = G-LEX-1 stays open as a statement about LEX's strict all-pairs form,
  which nothing here uses.
- Constant K: at the pin both referees signed (trunk 01d63d7), R46 §1 and §3 state K ≤ (n+2)²(n+1); R46 §1 (the K line and the last sentence of its
  proof, now a different count) and §3 (the K line) were changed AFTER the pin to (n+3)(n+1)² (l-red 938cea5; a process slip,
  recorded); the signed text is the 01d63d7 one, and R47 §5 at da63c40 quotes (n+3)(n+1)². REFEREE signed R46
  §1's (n+2)²(n+1); its own count had an arithmetic slip, corrected 02:47Z (referee 89fee50, R-C1P "Correction note"); the bound
  holds by REFEREE-2's count (n²+n+1)·n ≤ (n+2)²(n+1), which also makes (n+3)(n+1)² valid. This entry states the signed
  K ≤ (n+2)²(n+1); R47 §7 (l-red 28c0a20) uses it.
- Gauntlet: partial step-4 reduction for A_DTL on a subclass. GAP-A (general) stays OPEN; GAPS gets a row for (NEST*-BOUNDED).
