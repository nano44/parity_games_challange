/-
Additive weights for path components (towards premise (M), VJ00 Lemma 5.7, on one-player games).

On sets, `ext(v, ·)` is monotone only when `v` is in neither path component (F4′).  VJ00 §4.5
repairs this with multisets; here the path component `M` is replaced by the integer
`wt M = Σ_{u ∈ M} ±2^(pr u)` (+ for even, − for odd priority).  Under an injective priority
function the order on path components is the order of the weights (`setLt_iff_wt_lt`), and
prepending a vertex adds a fixed amount (`wt_ext`, `sl_ext`), so inequalities along a walk can be
added up.  (The fleet's engine experiments/si/si.py compares path sets by the same weight.)
-/
import PGLemmas.Play
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Intervals

namespace PG

open Classical
open scoped symmDiff

noncomputable section

variable {V : Type*} {pr : V → ℕ}

/-- the unsigned weight `Σ 2^(pr u)` -/
def pw (pr : V → ℕ) (S : Finset V) : ℤ := ∑ u ∈ S, (2 : ℤ) ^ pr u

/-- the signed weight of one vertex: `+2^(pr u)` for even, `−2^(pr u)` for odd priority -/
def sgw (pr : V → ℕ) (u : V) : ℤ := if Even (pr u) then (2 : ℤ) ^ pr u else -(2 : ℤ) ^ pr u

/-- the weight of a path component -/
def wt (pr : V → ℕ) (S : Finset V) : ℤ := ∑ u ∈ S, sgw pr u

theorem sgw_le (u : V) : sgw pr u ≤ (2 : ℤ) ^ pr u := by
  have h : (0 : ℤ) < 2 ^ pr u := by positivity
  unfold sgw
  split_ifs <;> linarith

theorem neg_le_sgw (u : V) : -(2 : ℤ) ^ pr u ≤ sgw pr u := by
  have h : (0 : ℤ) < 2 ^ pr u := by positivity
  unfold sgw
  split_ifs <;> linarith

theorem wt_le_pw (S : Finset V) : wt pr S ≤ pw pr S :=
  Finset.sum_le_sum (fun u _ => sgw_le u)

theorem neg_pw_le_wt (S : Finset V) : -pw pr S ≤ wt pr S := by
  unfold pw wt
  rw [← Finset.sum_neg_distrib]
  exact Finset.sum_le_sum (fun u _ => neg_le_sgw u)

theorem pw_union {A B : Finset V} (h : Disjoint A B) : pw pr (A ∪ B) = pw pr A + pw pr B :=
  Finset.sum_union h

/-- Distinct priorities below `p`: the unsigned weight is below `2^p`. -/
theorem pw_lt (hpr : Function.Injective pr) {S : Finset V} {p : ℕ} (hS : ∀ u ∈ S, pr u < p) :
    pw pr S < (2 : ℤ) ^ p := by
  have h1 : (∑ k ∈ S.image pr, 2 ^ k : ℕ) < 2 ^ p := by
    apply Nat.geomSum_lt (le_refl 2)
    intro k hk
    obtain ⟨u, hu, rfl⟩ := Finset.mem_image.mp hk
    exact hS u hu
  rw [Finset.sum_image (fun x _ y _ h => hpr h)] at h1
  unfold pw
  exact_mod_cast h1

/-- If the most relevant vertex of `A ∪ B` lies in `A` and is even, `A` is heavier than `B`. -/
theorem wt_sub_pos (hpr : Function.Injective pr) {A B : Finset V} (hdisj : Disjoint A B) {d : V}
    (hdA : d ∈ A) (hmax : ∀ u ∈ A ∪ B, pr u ≤ pr d) (hev : Even (pr d)) : wt pr B < wt pr A := by
  have h1 : sgw pr d + wt pr (A.erase d) = wt pr A := Finset.add_sum_erase A _ hdA
  have h2 : sgw pr d = (2 : ℤ) ^ pr d := by unfold sgw; rw [ite_eq_left hev]
  have hdisj' : Disjoint (A.erase d) B := Finset.disjoint_of_subset_left (Finset.erase_subset _ _) hdisj
  have h3 : pw pr (A.erase d ∪ B) < (2 : ℤ) ^ pr d := by
    apply pw_lt hpr
    intro u hu
    rcases Finset.mem_union.mp hu with hu | hu
    · exact lt_of_le_of_ne (hmax u (Finset.mem_union_left _ (Finset.mem_of_mem_erase hu)))
        (fun e => Finset.ne_of_mem_erase hu (hpr e))
    · exact lt_of_le_of_ne (hmax u (Finset.mem_union_right _ hu))
        (fun e => Finset.disjoint_left.mp hdisj hdA (hpr e ▸ hu))
  rw [pw_union hdisj'] at h3
  have h4 := neg_pw_le_wt (pr := pr) (A.erase d)
  have h5 := wt_le_pw (pr := pr) B
  linarith

/-- If the most relevant vertex of `A ∪ B` lies in `A` and is odd, `A` is lighter than `B`. -/
theorem wt_sub_neg (hpr : Function.Injective pr) {A B : Finset V} (hdisj : Disjoint A B) {d : V}
    (hdA : d ∈ A) (hmax : ∀ u ∈ A ∪ B, pr u ≤ pr d) (hodd : ¬ Even (pr d)) : wt pr A < wt pr B := by
  have h1 : sgw pr d + wt pr (A.erase d) = wt pr A := Finset.add_sum_erase A _ hdA
  have h2 : sgw pr d = -(2 : ℤ) ^ pr d := by unfold sgw; rw [ite_eq_right hodd]
  have hdisj' : Disjoint (A.erase d) B := Finset.disjoint_of_subset_left (Finset.erase_subset _ _) hdisj
  have h3 : pw pr (A.erase d ∪ B) < (2 : ℤ) ^ pr d := by
    apply pw_lt hpr
    intro u hu
    rcases Finset.mem_union.mp hu with hu | hu
    · exact lt_of_le_of_ne (hmax u (Finset.mem_union_left _ (Finset.mem_of_mem_erase hu)))
        (fun e => Finset.ne_of_mem_erase hu (hpr e))
    · exact lt_of_le_of_ne (hmax u (Finset.mem_union_right _ hu))
        (fun e => Finset.disjoint_left.mp hdisj hdA (hpr e ▸ hu))
  rw [pw_union hdisj'] at h3
  have h4 := wt_le_pw (pr := pr) (A.erase d)
  have h5 := neg_pw_le_wt (pr := pr) B
  linarith

theorem wt_empty : wt pr (∅ : Finset V) = 0 := Finset.sum_empty

theorem wt_pos_of_max_even (hpr : Function.Injective pr) {S : Finset V} {d : V} (hd : d ∈ S)
    (hmax : ∀ u ∈ S, pr u ≤ pr d) (hev : Even (pr d)) : 0 < wt pr S := by
  have := wt_sub_pos hpr (Finset.disjoint_empty_right S) hd
    (by intro u hu; rw [Finset.union_empty] at hu; exact hmax u hu) hev
  rwa [wt_empty] at this

theorem wt_neg_of_max_odd (hpr : Function.Injective pr) {S : Finset V} {d : V} (hd : d ∈ S)
    (hmax : ∀ u ∈ S, pr u ≤ pr d) (hodd : ¬ Even (pr d)) : wt pr S < 0 := by
  have := wt_sub_neg hpr (Finset.disjoint_empty_right S) hd
    (by intro u hu; rw [Finset.union_empty] at hu; exact hmax u hu) hodd
  rwa [wt_empty] at this

theorem wt_split (M N : Finset V) : wt pr (M ∩ N) + wt pr (M \ N) = wt pr M := by
  have h := Finset.sum_sdiff (f := sgw pr) (Finset.inter_subset_left : M ∩ N ⊆ M)
  rw [Finset.sdiff_inter_self_left] at h
  unfold wt
  linarith

/-- `M ≺ N` implies `wt M < wt N`. -/
theorem wt_lt_of_setLt (hpr : Function.Injective pr) {M N : Finset V} (h : setLt pr M N) :
    wt pr M < wt pr N := by
  obtain ⟨d, hd, hmax, hside⟩ := h
  have hM : wt pr (M ∩ N) + wt pr (M \ N) = wt pr M := wt_split M N
  have hN : wt pr (N ∩ M) + wt pr (N \ M) = wt pr N := wt_split N M
  rw [Finset.inter_comm N M] at hN
  rw [Finset.mem_symmDiff] at hd
  have hdisj : Disjoint (N \ M) (M \ N) := by
    rw [Finset.disjoint_left]
    intro u hu hu'
    exact (Finset.mem_sdiff.mp hu).2 (Finset.mem_sdiff.mp hu').1
  have hmax' : ∀ u ∈ (N \ M) ∪ (M \ N), pr u ≤ pr d := by
    intro u hu
    apply hmax
    rw [Finset.mem_symmDiff]
    rcases Finset.mem_union.mp hu with hu | hu
    · exact Or.inr ⟨(Finset.mem_sdiff.mp hu).1, (Finset.mem_sdiff.mp hu).2⟩
    · exact Or.inl ⟨(Finset.mem_sdiff.mp hu).1, (Finset.mem_sdiff.mp hu).2⟩
  rcases hside with ⟨hdN, hev⟩ | ⟨hdM, hodd⟩
  · have hdA : d ∈ N \ M := by
      rw [Finset.mem_sdiff]
      rcases hd with ⟨_, h2⟩ | h
      · exact absurd hdN h2
      · exact h
    have := wt_sub_pos hpr hdisj hdA hmax' hev
    linarith
  · have hdA : d ∈ M \ N := by
      rw [Finset.mem_sdiff]
      rcases hd with h | ⟨_, h2⟩
      · exact h
      · exact absurd hdM h2
    have hmax'' : ∀ u ∈ (M \ N) ∪ (N \ M), pr u ≤ pr d := by
      intro u hu; rw [Finset.union_comm] at hu; exact hmax' u hu
    have := wt_sub_neg hpr hdisj.symm hdA hmax'' hodd
    linarith

/-- Different path components have different weights. -/
theorem wt_injective (hpr : Function.Injective pr) {M N : Finset V} (h : wt pr M = wt pr N) :
    M = N := by
  by_contra hne
  rcases setLt_total (pr := pr) hne with h' | h'
  · exact absurd h (wt_lt_of_setLt hpr h').ne
  · exact absurd h.symm (wt_lt_of_setLt hpr h').ne

/-- The order on path components is the order of the weights. -/
theorem setLt_iff_wt_lt (hpr : Function.Injective pr) {M N : Finset V} :
    setLt pr M N ↔ wt pr M < wt pr N := by
  refine ⟨wt_lt_of_setLt hpr, fun h => ?_⟩
  by_cases hne : M = N
  · rw [hne] at h; exact absurd h (lt_irrefl _)
  · rcases setLt_total (pr := pr) hne with h' | h'
    · exact h'
    · exact absurd h (not_lt.mpr (wt_lt_of_setLt hpr h').le)

/-! ### Keys: a node valuation with a fixed cycle node as a pair of integers -/

/-- the signed length: longer is better at an odd cycle node, worse at an even one -/
def sl (pr : V → ℕ) (x : Val V) : ℤ := if Even (pr x.top) then -(x.len : ℤ) else (x.len : ℤ)

/-- the weight a vertex `v` adds to a path towards the cycle node `ℓ` -/
def dw (pr : V → ℕ) (ℓ v : V) : ℤ := if pr ℓ < pr v then sgw pr v else 0

/-- the signed length one step adds on a path towards the cycle node `ℓ` -/
def ds (pr : V → ℕ) (ℓ : V) : ℤ := if Even (pr ℓ) then -1 else 1

/-- the lexicographic order on pairs of integers, written out -/
def LexLe (a₁ a₂ b₁ b₂ : ℤ) : Prop := a₁ < b₁ ∨ (a₁ = b₁ ∧ a₂ ≤ b₂)

theorem wt_ext {v : V} {x : Val V} (hv : v ∉ x.set) :
    wt pr (ext pr v x).set = wt pr x.set + dw pr x.top v := by
  unfold ext dw wt
  dsimp only
  split_ifs
  · rw [Finset.sum_insert hv]; ring
  · ring

theorem sl_ext (v : V) (x : Val V) : sl pr (ext pr v x) = sl pr x + ds pr x.top := by
  unfold sl ds
  simp only [ext_top, ext_len]
  by_cases hp : Even (pr x.top)
  · simp only [hp, ite_true]; push_cast; ring
  · simp only [hp, ite_false]; push_cast; ring

/-- With equal cycle nodes, `x ⊴ y` is the lexicographic order of the keys `(wt, sl)`. -/
theorem Val.le_iff_lex (hpr : Function.Injective pr) {x y : Val V} (h : x.top = y.top) :
    Val.le pr x y ↔ LexLe (wt pr x.set) (sl pr x) (wt pr y.set) (sl pr y) := by
  unfold LexLe
  constructor
  · rintro (hlt | rfl)
    · rw [Val.lt_iff] at hlt
      rcases hlt with hr | ⟨-, hs | ⟨es, hl⟩⟩
      · rw [h] at hr; exact absurd hr (_root_.lt_irrefl _)
      · exact Or.inl (wt_lt_of_setLt hpr hs)
      · refine Or.inr ⟨by rw [es], ?_⟩
        unfold sl
        rw [← h]
        rcases hl with ⟨hl, hp⟩ | ⟨hl, hp⟩
        · rw [ite_eq_right hp, ite_eq_right hp]; exact_mod_cast hl.le
        · rw [ite_eq_left hp, ite_eq_left hp]
          have : (y.len : ℤ) < x.len := by exact_mod_cast hl
          linarith
    · exact Or.inr ⟨rfl, le_rfl⟩
  · rintro (hw | ⟨hw, hs⟩)
    · exact Or.inl (Val.lt_iff.mpr (Or.inr ⟨h, Or.inl ((setLt_iff_wt_lt hpr).mpr hw)⟩))
    · have es : x.set = y.set := wt_injective hpr hw
      unfold sl at hs
      rw [← h] at hs
      by_cases hp : Even (pr x.top)
      · rw [ite_eq_left hp, ite_eq_left hp] at hs
        have hle : y.len ≤ x.len := by
          have : (y.len : ℤ) ≤ x.len := by linarith
          exact_mod_cast this
        rcases Nat.lt_or_ge y.len x.len with hlt | hge
        · exact Or.inl (Val.lt_iff.mpr (Or.inr ⟨h, Or.inr ⟨es, Or.inr ⟨hlt, hp⟩⟩⟩))
        · exact Or.inr (Val.ext h es (by omega))
      · rw [ite_eq_right hp, ite_eq_right hp] at hs
        have hle : x.len ≤ y.len := by exact_mod_cast hs
        rcases Nat.lt_or_ge x.len y.len with hlt | hge
        · exact Or.inl (Val.lt_iff.mpr (Or.inr ⟨h, Or.inr ⟨es, Or.inl ⟨hlt, hp⟩⟩⟩))
        · exact Or.inr (Val.ext h es (by omega))

end

end PG
