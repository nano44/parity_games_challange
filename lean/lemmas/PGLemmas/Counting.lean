/-
Counting lemmas (statements in `PGLemmas/Statements2.lean`):
* `two_cross`    Lemma TWO-CROSS (claude/l-si docs/si/box100-scclin.md §2), any preorder;
* `lam_count`    a non-falling sequence of node valuations changes its cycle node ≤ n − 1 times;
* `howard_run`   Corollary L1-POLY (box 101 §3), abstract: a Howard run with only `Ch` moving has
                 at most n(n−1) + (n(n−1)+1)·|Ch| steps, given (M).
-/
import PGLemmas.LamGap
import PGLemmas.Statements2

namespace PG

open Classical

noncomputable section

/-! ### TWO-CROSS -/

/-- **Lemma TWO-CROSS**, abstract form. -/
theorem two_cross (α : Type*) [Preorder α] (F : Type*) : TwoCrossStatement α F := by
  intro a b T face Ω hface hF1 hnotie hloc
  have hab : a ≠ b := fun e => hnotie 0 (by omega) (by rw [e])
  -- (i)
  have hi : ∀ t, t < T → (face t = a → face (t + 1) = b → Ω t a < Ω (t + 1) a) ∧
      (face t = b → face (t + 1) = a → Ω t b < Ω (t + 1) b) := by
    intro t ht
    constructor
    · intro h0 h1
      have l0 : Ω t a < Ω t b := (hloc t (by omega)).1 h0 (hnotie t (by omega))
      have l1 : Ω (t + 1) b < Ω (t + 1) a :=
        (hloc (t + 1) (by omega)).2 h1 (hnotie (t + 1) (by omega)).symm
      exact (l0.trans_le (hF1 t ht).2).trans l1
    · intro h0 h1
      have l0 : Ω t b < Ω t a := (hloc t (by omega)).2 h0 (hnotie t (by omega)).symm
      have l1 : Ω (t + 1) a < Ω (t + 1) b :=
        (hloc (t + 1) (by omega)).1 h1 (hnotie (t + 1) (by omega))
      exact (l0.trans_le (hF1 t ht).1).trans l1
  refine ⟨hi, ?_⟩
  -- a flip leaves `a` or leaves `b`
  have hflip : ∀ t, t < T → face (t + 1) ≠ face t →
      (face t = a ∧ face (t + 1) = b) ∨ (face t = b ∧ face (t + 1) = a) := by
    intro t ht hne
    rcases hface t (by omega) with h0 | h0 <;> rcases hface (t + 1) (by omega) with h1 | h1
    · exact absurd (h1.trans h0.symm) hne
    · exact Or.inl ⟨h0, h1⟩
    · exact Or.inr ⟨h0, h1⟩
    · exact absurd (h1.trans h0.symm) hne
  -- the flips away from `a` and away from `b`, up to time `n`
  let FA : ℕ → Finset ℕ := fun n =>
    (Finset.range n).filter (fun t => face t = a ∧ face (t + 1) = b)
  let FB : ℕ → Finset ℕ := fun n =>
    (Finset.range n).filter (fun t => face t = b ∧ face (t + 1) = a)
  have hFAsucc : ∀ n, (FA (n + 1)).card =
      (FA n).card + (if face n = a ∧ face (n + 1) = b then 1 else 0) := by
    intro n
    show ((Finset.range (n + 1)).filter _).card = _
    rw [Finset.range_add_one, Finset.filter_insert]
    split_ifs with h
    · rw [Finset.card_insert_of_notMem (by simp)]
    · rfl
  have hFBsucc : ∀ n, (FB (n + 1)).card =
      (FB n).card + (if face n = b ∧ face (n + 1) = a then 1 else 0) := by
    intro n
    show ((Finset.range (n + 1)).filter _).card = _
    rw [Finset.range_add_one, Finset.filter_insert]
    split_ifs with h
    · rw [Finset.card_insert_of_notMem (by simp)]
    · rfl
  -- alternation: the two counts differ by at most one
  have halt : ∀ n, n ≤ T →
      (face n = a → (FA n).card ≤ (FB n).card ∧ (FB n).card ≤ (FA n).card + 1) ∧
      (face n = b → (FB n).card ≤ (FA n).card ∧ (FA n).card ≤ (FB n).card + 1) := by
    intro n
    induction n with
    | zero => intro _; simp [FA, FB]
    | succ n ih =>
      intro hn
      obtain ⟨iha, ihb⟩ := ih (by omega)
      rw [hFAsucc, hFBsucc]
      rcases hface n (by omega) with h0 | h0 <;> rcases hface (n + 1) hn with h1 | h1
      · -- `a → a`
        have hA : ¬ (face n = a ∧ face (n + 1) = b) := fun h => hab (h1.symm.trans h.2)
        have hB : ¬ (face n = b ∧ face (n + 1) = a) := fun h => hab (h0.symm.trans h.1)
        rw [ite_eq_right hA, ite_eq_right hB]
        have := iha h0
        exact ⟨fun _ => by omega, fun e => absurd (h1.symm.trans e) hab⟩
      · -- `a → b`
        have hA : face n = a ∧ face (n + 1) = b := ⟨h0, h1⟩
        have hB : ¬ (face n = b ∧ face (n + 1) = a) := fun h => hab (h0.symm.trans h.1)
        rw [ite_eq_left hA, ite_eq_right hB]
        have := iha h0
        exact ⟨fun e => absurd (e.symm.trans h1) hab, fun _ => by omega⟩
      · -- `b → a`
        have hA : ¬ (face n = a ∧ face (n + 1) = b) := fun h => hab (h.1.symm.trans h0)
        have hB : face n = b ∧ face (n + 1) = a := ⟨h0, h1⟩
        rw [ite_eq_right hA, ite_eq_left hB]
        have := ihb h0
        exact ⟨fun _ => by omega, fun e => absurd (h1.symm.trans e) hab⟩
      · -- `b → b`
        have hA : ¬ (face n = a ∧ face (n + 1) = b) := fun h => hab (h.1.symm.trans h0)
        have hB : ¬ (face n = b ∧ face (n + 1) = a) := fun h => hab (h.2.symm.trans h1)
        rw [ite_eq_right hA, ite_eq_right hB]
        have := ihb h0
        exact ⟨fun e => absurd (e.symm.trans h1) hab, fun _ => by omega⟩
  -- the counts of the statement
  intro flips chA chB
  have hsub : (Finset.range T).filter (fun t => face (t + 1) ≠ face t) ⊆ FA T ∪ FB T := by
    intro t ht
    obtain ⟨htr, hne⟩ := Finset.mem_filter.mp ht
    have htT : t < T := Finset.mem_range.mp htr
    rw [Finset.mem_union]
    rcases hflip t htT hne with h | h
    · exact Or.inl (Finset.mem_filter.mpr ⟨htr, h⟩)
    · exact Or.inr (Finset.mem_filter.mpr ⟨htr, h⟩)
  have hflips : flips ≤ (FA T).card + (FB T).card :=
    (Finset.card_le_card hsub).trans (Finset.card_union_le _ _)
  have hA : (FA T).card ≤ chA := by
    apply Finset.card_le_card
    intro t ht
    obtain ⟨htr, h0, h1⟩ := Finset.mem_filter.mp ht
    exact Finset.mem_filter.mpr ⟨htr, ((hi t (Finset.mem_range.mp htr)).1 h0 h1).ne⟩
  have hB : (FB T).card ≤ chB := by
    apply Finset.card_le_card
    intro t ht
    obtain ⟨htr, h0, h1⟩ := Finset.mem_filter.mp ht
    exact Finset.mem_filter.mpr ⟨htr, ((hi t (Finset.mem_range.mp htr)).2 h0 h1).ne⟩
  have hdiff : (FA T).card ≤ (FB T).card + 1 ∧ (FB T).card ≤ (FA T).card + 1 := by
    obtain ⟨h1, h2⟩ := halt T le_rfl
    rcases hface T le_rfl with h | h
    · have := h1 h; omega
    · have := h2 h; omega
  refine ⟨by omega, ?_⟩
  rcases le_total chA chB with h | h
  · rw [min_eq_left h]; omega
  · rw [min_eq_right h]; omega

/-! ### The cycle node of a non-falling sequence changes at most `n − 1` times -/

variable {V : Type*} [Fintype V]

/-- A non-falling sequence of node valuations changes its cycle component at most `n − 1`
times. -/
theorem lam_count : LamCountStatement V := by
  intro pr hpr x T hle
  -- the reward of the cycle component never falls
  have hmono : ∀ d t, t + d ≤ T → rew pr (x t).top ≤ rew pr (x (t + d)).top := by
    intro d
    induction d with
    | zero => intro t _; exact le_rfl
    | succ d ih =>
      intro t ht
      have h1 := ih t (by omega)
      rcases Val.top_of_le (hle (t + d) (by omega)) with e | h
      · exact h1.trans (le_of_eq (congrArg (rew pr) e))
      · exact h1.trans h.le
  have hmono' : ∀ t t', t ≤ t' → t' ≤ T → rew pr (x t).top ≤ rew pr (x t').top := by
    intro t t' htt' ht'
    have := hmono (t' - t) t (by omega)
    have e : t + (t' - t) = t' := by omega
    rwa [e] at this
  -- and rises strictly where the cycle component changes
  have hstrict : ∀ t, t < T → (x t).top ≠ (x (t + 1)).top →
      rew pr (x t).top < rew pr (x (t + 1)).top := by
    intro t ht hne
    rcases Val.top_of_le (hle t ht) with e | h
    · exact absurd e hne
    · exact h
  -- the new cycle components are pairwise different, and different from the first one
  have hcard : ((Finset.range T).filter (fun t => (x t).top ≠ (x (t + 1)).top)).card ≤
      (Finset.univ.erase (x 0).top).card := by
    apply Finset.card_le_card_of_injOn (fun t => (x (t + 1)).top)
    · intro t ht
      obtain ⟨htr, hne⟩ := Finset.mem_filter.mp ht
      have htT : t < T := Finset.mem_range.mp htr
      rw [Finset.mem_coe, Finset.mem_erase]
      refine ⟨fun e => ?_, Finset.mem_univ _⟩
      dsimp only at e
      have h1 := hmono' 0 t (by omega) (by omega)
      have h2 := hstrict t htT hne
      rw [e] at h2
      exact absurd (h1.trans_lt h2) (lt_irrefl _)
    · intro t ht t' ht' e
      obtain ⟨htr, hne⟩ := Finset.mem_filter.mp ht
      obtain ⟨htr', hne'⟩ := Finset.mem_filter.mp ht'
      have htT : t < T := Finset.mem_range.mp htr
      have htT' : t' < T := Finset.mem_range.mp htr'
      dsimp only at e
      by_contra hneq
      rcases Nat.lt_or_gt_of_ne hneq with hlt | hgt
      · have h1 := hmono' (t + 1) t' (by omega) (by omega)
        have h2 := hstrict t' htT' hne'
        rw [← e] at h2
        exact absurd (h1.trans_lt h2) (lt_irrefl _)
      · have h1 := hmono' (t' + 1) t (by omega) (by omega)
        have h2 := hstrict t htT hne
        rw [e] at h2
        exact absurd (h1.trans_lt h2) (lt_irrefl _)
  rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ] at hcard
  have hpos : 0 < Fintype.card V := Fintype.card_pos_iff.mpr ⟨(x 0).top⟩
  omega

/-! ### The length of a Howard run -/

/-- If among the steps `0, …, T − 1` every `N + 1` consecutive ones contain a step of `B`, then
`T ≤ |B|·(N + 1) + N`. -/
theorem steps_le_of_breaks (B : Finset ℕ) (N T : ℕ)
    (h : ∀ a, a + N < T → ∃ t ∈ B, a ≤ t ∧ t ≤ a + N) : T ≤ B.card * (N + 1) + N := by
  -- invariant: `r` trailing steps without a break
  have key : ∀ n, n ≤ T → ∃ r, r ≤ n ∧ (∀ t, n - r ≤ t → t < n → t ∉ B) ∧
      n ≤ (B.filter (fun t => t < n)).card * (N + 1) + r ∧ r ≤ N := by
    intro n
    induction n with
    | zero => intro _; exact ⟨0, le_rfl, fun t _ ht => absurd ht (by omega), by omega, by omega⟩
    | succ n ih =>
      intro hn
      obtain ⟨r, hrn, hfree, hbound, hrN⟩ := ih (by omega)
      by_cases hB : n ∈ B
      · refine ⟨0, by omega, fun t h1 h2 => absurd h2 (by omega), ?_, by omega⟩
        have hfil : B.filter (fun t => t < n + 1) = insert n (B.filter (fun t => t < n)) := by
          ext t
          simp only [Finset.mem_filter, Finset.mem_insert]
          constructor
          · rintro ⟨h1, h2⟩
            by_cases e : t = n
            · exact Or.inl e
            · exact Or.inr ⟨h1, by omega⟩
          · rintro (rfl | ⟨h1, h2⟩)
            · exact ⟨hB, by omega⟩
            · exact ⟨h1, by omega⟩
        rw [hfil, Finset.card_insert_of_notMem (by simp)]
        have : ((B.filter (fun t => t < n)).card + 1) * (N + 1) =
            (B.filter (fun t => t < n)).card * (N + 1) + (N + 1) := by ring
        omega
      · have hfil : B.filter (fun t => t < n + 1) = B.filter (fun t => t < n) := by
          ext t
          simp only [Finset.mem_filter]
          constructor
          · rintro ⟨h1, h2⟩
            refine ⟨h1, ?_⟩
            by_contra hlt
            have e : t = n := by omega
            exact hB (e ▸ h1)
          · rintro ⟨h1, h2⟩
            exact ⟨h1, by omega⟩
        have hfree' : ∀ t, n + 1 - (r + 1) ≤ t → t < n + 1 → t ∉ B := by
          intro t h1 h2
          by_cases e : t = n
          · rw [e]; exact hB
          · exact hfree t (by omega) (by omega)
        refine ⟨r + 1, by omega, hfree', by rw [hfil]; omega, ?_⟩
        -- `r + 1 ≤ N`: otherwise `N + 1` consecutive steps without a break
        by_contra hgt
        obtain ⟨t, htB, h1, h2⟩ := h (n + 1 - (r + 1)) (by omega)
        exact hfree' t h1 (by omega) htB
  obtain ⟨r, -, -, hbound, hrN⟩ := key T le_rfl
  have hle : (B.filter (fun t => t < T)).card ≤ B.card := Finset.card_le_card (Finset.filter_subset _ _)
  have : (B.filter (fun t => t < T)).card * (N + 1) ≤ B.card * (N + 1) :=
    Nat.mul_le_mul_right _ hle
  omega

/-- **Corollary L1-POLY**, abstract form: the length of a Howard run on which only `Ch` moves. -/
theorem howard_run : HowardRunStatement V := by
  intro pr hpr E Ch s T hfixed hhow hmono hmoves
  -- the steps at which some vertex changes its cycle node
  let Bv : V → Finset ℕ := fun v =>
    (Finset.range T).filter (fun t => lam pr (s t) v ≠ lam pr (s (t + 1)) v)
  let B : Finset ℕ := Finset.univ.biUnion Bv
  -- each vertex changes its cycle node at most `n - 1` times
  have hBv : ∀ v ∈ (Finset.univ : Finset V), (Bv v).card ≤ Fintype.card V - 1 := by
    intro v _
    have := lam_count pr hpr (fun t => val pr (s t) v) T (fun t ht => hmono t ht v)
    have e : (Bv v).card =
        ((Finset.range T).filter (fun t => (val pr (s t) v).top ≠ (val pr (s (t + 1)) v).top)).card :=
      rfl
    omega
  have hB : B.card ≤ Fintype.card V * (Fintype.card V - 1) := by
    have := Finset.card_biUnion_le_card_mul (Finset.univ : Finset V) Bv (Fintype.card V - 1) hBv
    rwa [Finset.card_univ] at this
  -- `|Ch| + 1` consecutive steps contain such a step: otherwise they form a window that is too long
  have hbreak : ∀ a, a + Ch.card < T → ∃ t ∈ B, a ≤ t ∧ t ≤ a + Ch.card := by
    intro a ha
    by_contra hnone
    have hquiet : ∀ t, a ≤ t → t ≤ a + Ch.card → ∀ v, lam pr (s t) v = lam pr (s (t + 1)) v := by
      intro t h1 h2 v
      by_contra hne
      exact hnone ⟨t, Finset.mem_biUnion.mpr ⟨v, Finset.mem_univ _,
        Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), hne⟩⟩, h1, h2⟩
    have hlam : ∀ d, d ≤ Ch.card + 1 → ∀ v, lam pr (s (a + d)) v = lam pr (s a) v := by
      intro d
      induction d with
      | zero => intro _ v; rfl
      | succ d ih =>
        intro hd v
        rw [← ih (by omega) v]
        exact (hquiet (a + d) (by omega) (by omega) v).symm
    have W : Window pr E Ch s a (a + Ch.card + 1) := by
      refine ⟨by omega, ?_, ?_, ?_, ?_, ?_⟩
      · intro t _ ht v hv
        rw [hfixed t (by omega) v hv, hfixed a (by omega) v hv]
      · intro t _ ht v hv
        exact hhow t (by omega) v hv
      · intro t _ ht v
        exact hmono t (by omega) v
      · intro t h1 h2 v
        have := hlam (t - a) (by omega) v
        have e : a + (t - a) = t := by omega
        rwa [e] at this
      · intro t _ ht
        exact hmoves t (by omega)
    have := lam_gap_sharp pr hpr E Ch s a (a + Ch.card + 1) W
    omega
  have hT := steps_le_of_breaks B Ch.card T hbreak
  have h1 : B.card * (Ch.card + 1) ≤ Fintype.card V * (Fintype.card V - 1) * (Ch.card + 1) :=
    Nat.mul_le_mul_right _ hB
  have h2 : Fintype.card V * (Fintype.card V - 1) * (Ch.card + 1) + Ch.card =
      Fintype.card V * (Fintype.card V - 1) +
        (Fintype.card V * (Fintype.card V - 1) + 1) * Ch.card := by ring
  omega

end

end PG
