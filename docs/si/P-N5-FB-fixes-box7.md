# Fixes to packet P-N5-FB (docs/si/P-N5-FB-box7.md, sha1 9ece9994, pinned trunk 348393b; the packet itself is never edited)
L-SI successor 3 (Opus 5.5, D18/L40). Started 2026-10-24 22:5xZ (date -u).
- This file answers the referee items as the Lead relayed them: REFEREE R-N5-FB, claude/referee eb1ec3c, docs/referee/R-N5-FB.md, Lead
  22:5xZ. I have not opened the report itself; it is outside my lane's reading list. REFEREE-2's items will follow when it reports.
- Each fix gives the packet location, the corrected text or proof, and its status.

## FB-1 (Theorem FB step (2): "M < ∞ by NOINF")
- The gap: NOINF bounds only the levels of SWITCHED edges, while M is the max over ALL gate edges.
- Corrected step. At an in-phase S4c fallback i, every vertex y with a gate edge switches, to its best gate target z* (§0, S4c).
  Suppose some gate edge (y, z) has level ∞, i.e. λ_i(z) ≠ λ_i(σ_i y).
  - Since Ξ_i(z) ▷ Ξ_i(σ_i y) and the cycle nodes differ, reward(λ_i z) > reward(λ_i σ_i y).
  - z* ⊵ z gives reward(λ_i z*) ≥ reward(λ_i z) > reward(λ_i σ_i y). So λ_i(z*) ≠ λ_i(σ_i y): the switched edge (y, z*) has level ∞.
  - That contradicts NOINF (λ_{i+1} = λ_i inside the phase). Hence M_i < ∞.
- The packet's "Consequence" line under NOINF is to be read with this argument.
- Status: PROVED (L-SI succ. 3).

## FB-2 ("transitions of the phase" and the phase-exit fallback)
- Reading confirmed: the packet counts transitions with both endpoints in the phase. The transition that leaves the phase (at most one
  per phase) is not covered.
- Corrected statement of Theorem FB:
  - a phase has at most n_E(2n − 1)(J + 1) + J S4c fallbacks among its in-phase transitions;
  - so at most n_E(2n − 1)(J + 1) + J + 1 S4c fallbacks if the transition leaving the phase is counted with it.
- The Corollary changes the same way (+1). Summed over phases, the extra terms are ≤ #phases, which is already a factor in every
  per-phase bound (Lemma Φ, unrefereed).
- Status: PROVED (bookkeeping).

## CAP-1 (CAP uses "b minimises Ξ_{k+1} over succ(o)"; SPEC's σ̄ at a cycle node is the FIX-2 DFS choice)
- REFEREE's point stands: σ̄_{k+1}(o) need not be a ⊴-minimiser when λ(o) = o.
- Repaired proof of CAP that uses no minimality.
- **CAP (restated).** Inside a phase on 𝒞^1O, let k → k+1 be non-tame and a := σ̄_k(o). Then every e ∈ succ(o) with
  lev(Ξ_k a, Ξ_k e) ≤ M_k lies in R̄_{k+1}.
- Proof.
  - Suppose e ∉ R̄_{k+1}. Since the transition is non-tame, M := M_k is finite and ≠ ⊥ (TAME, packet §2 (b)).
  - Let τ″ := the Odd strategy with τ″(o) = e (on 𝒞^1O every other Odd vertex is forced), and let H″ := the (σ_{k+1}, τ″)-graph.
  - (E) of (T) holds at every vertex:
    - switched Even vertices: gate level ≤ M (R15 (d), (C2));
    - o: COARSE_M(Ξ_k e) = COARSE_M(Ξ_k a), by (C2) and the hypothesis;
    - elsewhere: trivial.
  - The cycle condition holds. e's (σ_{k+1})-play avoids o (e ∉ R̄_{k+1}), so no cycle of H″ passes through o. Off o, H″ agrees with
    H_{k+1}. So every cycle of H″ is a cycle of H_{k+1}, and its top t has λ_k(t) = λ_{k+1}(t) = t (Lemma 5.2; phase).
  - (T) gives COARSE_M(Θ_{H″}) = COARSE_M(Ξ_k) pointwise.
  - Ξ_k ⊴ Ξ_{k+1} (R15 (a)) ⊴ Θ_{σ_{k+1} τ″} = Θ_{H″} (VJ00 (11)).
  - By (C1) and (C3), COARSE_M(Ξ_{k+1}) = COARSE_M(Ξ_k): the transition is tame. Contradiction. □
- Remarks.
  - This is COARSE-SI (a) with σ̄_k replaced by any Odd strategy that agrees with it up to level M at the switched Odd vertices.
  - For e = a it is §2 (a) itself. REFEREE's case split (λ(o) ≠ o: σ̄(o) is a minimiser by (11); λ(o) = o: a finite-level exit has
    cycle node o and lies in R̄) is an equally valid proof. The version above avoids the cases.
  - J1 does not use minimality: it is the contrapositive of TAME, whose (E) at o is the level hypothesis itself. OFF does not use
    it either.
- Status: PROVED (L-SI succ. 3). The packet's §5 CAP proof is replaced by this one.
- Lane note, outside the packet: box 7 §9 (D1′, NOREL-A) also used "a minimises Ξ_k over the exits". There (h) holds at k, so
  λ_k(o) ≠ o (H1). The minimality is then derived from (11) in N5-C-box7.md §9 (corrected there), including exits e ∈ R_k:
  - the loop o → e → … → o has a top t with reward(t) > reward(c), because Odd's best value at o has cycle node c ≠ t;
  - in every parity case this makes L := (π_e, o) non-negative.

## V-1 (page of Prog)
- VJ00's definition of Prog(Ξ, e) (conditions 1-3) is on printed p. 15 (footer page numbers), not p. 14.
- p. 14: the definition of σ̄. p. 15: Prog and Lemma 5.2. p. 16: (11).
- Every "p. 14, definition of Prog" in the packet (§0) reads "p. 15". Status: wording.

## V-2 ((P3) quotes half of clause 3)
- VJ00's clause 3 reads: if Λ(v) = v then Π(v) ≅_{Λ(v)} Π(w) ⊕ v AND Π(v) = (∅, 0).
- The packet's (P3) keeps only the second conjunct, Π(v) = (∅, 0), which is all that (T) (iii) uses. The first conjunct (the cycle
  closes up to ≅_ℓ) is not used anywhere in the packet. Status: wording.

## ENG-1 (inherited engine assumption)
- (T), and through it COARSE-SI, TAME, OFF and CAP, applies VJ00 Lemma 5.2 to the (σ_k, σ̄_k)-graph, where σ̄_k is SPEC's
  counterstrategy (si.py; SPEC FIX 2 at cycle nodes). That needs Ξ_k = Θ_{σ_k σ̄_k}: the engine's valuation equals the play values of
  the graph formed by σ_k and the engine's own σ̄_k.
- CAP (as repaired) and COARSE-SI (a) also use Ξ_k = Ω_{σ_k} (VJ00's optimal valuation), so that (11) applies.
- Both are inherited from the engine, as in R15/R17-R23; they are not new to this packet.
- DATA (lane check experiments/si/coarse/eng1.py, independent lasso walk): Ξ = Θ_{σσ̄} at all 73,016 vertex values of 2,166 states
  (the named set of packet §7 plus the four jcl_* climb bests), 0 mismatches. REFEREE reports 0 failures in its own data.
- Status: inherited assumption, stated.

## Data added after the packet (lane, not refereed; N5-C-box7.md §10-§11)
- J-climbs: max J per phase 12 at n 32 and 17 at n 48 (pinned jcl_*, re-verified).
- (JU2) is FALSE on jcl_x31_cu32i (sha1 00e09994).
- Neither changes a packet claim.
