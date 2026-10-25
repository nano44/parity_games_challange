# Fixes to packet P-N5-CLS (docs/si/P-N5-CLS-box8.md, sha1 5bbfd872, l-si 04ca0b8c; the packet itself is never edited)
L-SI successor 3 (Opus 5.5, D18/L40). Written 2026-10-25 03:1xZ (date -u).
- A record of the referees' items, one line per row of REFEREE-2's §C joint map, as the Lead relayed them at 03:03Z.
- Sources: REFEREE docs/referee/R-N5-CLS.md (a0b92ec); REFEREE-2 docs/referee-2/R2-N5-CLS.md (ffe10e1, §C 848839e). Both sign; no
  disagreement. I have not opened the reports themselves. REFEREE's §C is pending; any row it adds goes into a later part.
- Each item below is wording or a dependency made explicit. None changes a statement.

## Rows
1. **CLS-1 (§3 OFFGATE).** Replace "If M_k = ⊥, σ and Ξ are unchanged" by: "M_k ≥ −1 at every in-phase transition."
   - Reason: with no gate (Iσ_k = ∅), σ is unchanged (R15 (d)). A transition then requires Iτ_k ≠ ∅, and τ changes, through S4b or
     Odd's fallback. That leaves the phase.
   - So the case M_k = ⊥ does not occur inside a phase. The same holds for the "M_k = ⊥" sentences in §5.
2. **CLS-2 (§4 CN).** Read the hypothesis as "an EVEN vertex y with λ_k(y) = y switches to z". Only Even vertices switch σ.
3. **CLS-3 = G-CLS-1 (§6 Theorem CLS1).** The citation of FBL means R20 (b) in its u* ≠ none strong form, applied at the single state k1:
   at k1 there is no F → R and no R → R gate edge.
   - Its proof uses only state k1: the fallback is Even's; S4a returned σ_{k1}; Lemma G (c); and P(w) = ∅ ⇒ u* = none
     (R-N5-XA §3, R2-N5-XA §2).
   - So no hypothesis about a longer throttled stretch is needed. This replaces the packet's sentence "A single fallback state with (h)
     and θ ◁ w is a throttled stretch of length 1" (§0).
4. **CLS-4 (§6 Corollary).** Drop the word "evicting".
   - The Corollary reads: "Along a scope run, the levels of its THR fallbacks with u* ≠ none form a non-increasing sequence. These are
     all its fallbacks before the first EQ / u* = none state (Fact R)."
   - Every in-scope fallback with u* ≠ none is THR, so the remaining clause added nothing.
5. **N-CLS-1 (§3 OFFGATE).** OFF's R̄ (R25, defined by honest reachability of o) is the packet's R̄ (defined through (σ, τ)-plays).
   - Honest plays and (σ, τ)-plays agree up to the first visit of o, because Odd is forced off o on 𝒞^1O (§0). So whether o is
     reached is the same in both.

## Referees' note on the data
- In experiments/si/coarse/cls2.py, the counter MF_up (1 in the logs) is OG′'s counter at x31_re24, transition 1 → 2, an S4a step. It is
  not a rise of a fallback level.
- §8's line "OG′: 1 violation" refers to it. No CLS1 or (CL-S) violation occurs in any log.

## Status
- Packet statements: unchanged and signed by both referees, as above.
- Open items (packet §7: H-EQ, the per-level count, Θ per scope run): unchanged.
- Lane note, not acted on (Lead 03:03Z): L-NEW successor 13 reports ABS-L and a reduction of the per-level count to releases of
  absorbed exits at level-M fallbacks (docs/new/N5-K-box33.md §8-§9). It is relevant to the packet's second open item; NEXT list in
  notes/L-SI.md.
