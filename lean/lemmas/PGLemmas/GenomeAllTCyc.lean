/-
Box 208 Addendum A, Theorem ALL-TCYC on the genome: `all_tcyc_sharp : G.AllTCycSharpStatement`
and `all_tcyc : G.AllTCycStatement` (`PGLemmas/GenomeLevelStatement.lean`).  No premise.

The assembly of box 208 A3, with reference state b := T and a := 0:
* `level_count` (`PGLemmas/LevelCount.lean`) on the keys `G.ck σ τ` in `ℤ ×ₗ ℤ`, with
  - (K1): `IdealCycRun.ck_step`;
  - the set of front classes: the classes at T of the gates and the classes (β, ∅), at most 2M
    (`l5`, first factor);
  - fronts of at most N + 2M vertices (`l5`, second factor);
  - at most N consecutive stalls (`plateau_g`);
  so every state at which something lags is among the first 2M·(N + 2M)·(N + 1) states;
* from the first state b′ at which nothing lags, no class changes ((K1)), so T − b′ ≤ N (`quiet`).
Together T ≤ 2M·(N + 2M)·(N + 1) + N, which is at most the lane's P·(N + 2M + 6) + N.
-/
import PGLemmas.GenomePlateau

namespace PG

open Classical

noncomputable section

namespace Genome

variable {G : Genome}

/-- **Theorem ALL-TCYC** with the bound `2M(N + 2M)(N + 1) + N`. -/
theorem all_tcyc_sharp : G.AllTCycSharpStatement := by
  intro h σ τ T R
  -- the possible classes of a front: the classes at `T` of the gates, and `(β, ∅)`
  obtain ⟨S, hS, hSmem⟩ : ∃ S : Finset (ℤ ×ₗ ℤ), S.card ≤ 2 * G.M ∧
      ∀ t, t ≤ T → ∀ v, FrontAt (G.ck σ τ) T t v → G.ck σ τ t v ∈ S := by
    refine ⟨Finset.univ.image (fun o : G.Opt => G.ck σ τ T (Vertex.gate o)) ∪
      Finset.univ.image (fun o : G.Opt => G.clsKey (Vertex.beta o, ∅)), ?_, ?_⟩
    · refine (Finset.card_union_le _ _).trans ?_
      have h1 : (Finset.univ.image (fun o : G.Opt => G.ck σ τ T (Vertex.gate o))).card ≤ G.M := by
        refine Finset.card_image_le.trans ?_
        rw [Finset.card_univ]
        rfl
      have h2 : (Finset.univ.image
          (fun o : G.Opt => G.clsKey (Vertex.beta o, ∅))).card ≤ G.M := by
        refine Finset.card_image_le.trans ?_
        rw [Finset.card_univ]
        rfl
      omega
    · intro t ht v hv
      rcases (l5 h σ τ T R T t ht le_rfl).1 v hv with ⟨o, ho⟩ | ⟨o, ho⟩
      · exact Finset.mem_union.mpr (Or.inl (Finset.mem_image.mpr
          ⟨o, Finset.mem_univ _, ((ck_eq_iff h).mpr ho).symm⟩))
      · refine Finset.mem_union.mpr (Or.inr (Finset.mem_image.mpr ⟨o, Finset.mem_univ _, ?_⟩))
        show G.clsKey (Vertex.beta o, ∅) = G.clsKey (G.cls (nxt G.V0 σ τ t) v)
        rw [ho]
  have hcount := level_count G.Vertex (ℤ ×ₗ ℤ) (G.ck σ τ) 0 T S (G.N + 2 * G.M) G.N
    (fun t _ ht v => R.ck_step h ht v)
    (fun t _ ht v hv => hSmem t ht v hv)
    (fun t _ ht => (l5 h σ τ T R T t ht le_rfl).2)
    (fun u v _ huv hvT hst => plateau_g h σ τ T R T u v huv hvT le_rfl hst)
  -- the first state at which nothing lags
  have hex : ∃ t, t ≤ T ∧ ∀ v, G.ck σ τ t v = G.ck σ τ T v := ⟨T, le_rfl, fun _ => rfl⟩
  obtain ⟨hb'T, hb'⟩ := Nat.find_spec hex
  have hb'P : Nat.find hex ≤ S.card * (G.N + 2 * G.M) * (G.N + 1) := by
    rcases Nat.eq_zero_or_pos (Nat.find hex) with h0 | hpos
    · rw [h0]
      exact Nat.zero_le _
    · have hmin := Nat.find_min hex (m := Nat.find hex - 1) (by omega)
      have hlag : ∃ v, G.ck σ τ (Nat.find hex - 1) v ≠ G.ck σ τ T v := by
        by_contra hno
        apply hmin
        refine ⟨by omega, fun v => ?_⟩
        by_contra hne
        exact hno ⟨v, hne⟩
      have hc := hcount (Nat.find hex - 1) (Nat.zero_le _) (by omega) hlag
      omega
  -- after it no class changes
  have htail : T - Nat.find hex ≤ G.N := by
    apply quiet h σ τ T R (Nat.find hex) T hb'T le_rfl
    intro t hbt htT x
    apply (ck_eq_iff h).mp
    have h1 := R.ck_mono h hbt htT x
    have h2 := R.ck_mono h htT le_rfl x
    rw [← hb' x] at h2
    exact le_antisymm h2 h1
  have hmul : S.card * (G.N + 2 * G.M) * (G.N + 1) ≤ 2 * G.M * (G.N + 2 * G.M) * (G.N + 1) :=
    Nat.mul_le_mul_right _ (Nat.mul_le_mul_right _ hS)
  omega

/-- **Theorem ALL-TCYC** (box 208 Addendum A0), with the lane's bound `P·(N + 2M + 6) + N`,
`P = 2M(N + 2M)`. -/
theorem all_tcyc : G.AllTCycStatement := by
  intro h σ τ T R
  have hs := all_tcyc_sharp h σ τ T R
  have hle : 2 * G.M * (G.N + 2 * G.M) * (G.N + 1) ≤
      2 * G.M * (G.N + 2 * G.M) * (G.N + 2 * G.M + 6) := Nat.mul_le_mul_left _ (by omega)
  omega

end Genome

end

end PG
