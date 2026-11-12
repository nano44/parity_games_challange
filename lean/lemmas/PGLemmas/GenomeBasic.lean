/-
First facts about the game Γ(G) of `PGLemmas/Genome.lean`, read off the definitions (no premise):

* `pos_inj`, `pos_lt`        the (x, k) order position is a bijection of the options onto 0..M − 1;
* `idx_injective`            under `WF`, the vertex index is injective;
* `pr_lt_iff`, `pr_injective`, `even_pr`
                             the injective priority `pr` orders the vertices by (priority, index)
                             and has the parity of the priority ([SI]: p' = 2·rank + parity);
* `prio_*`                   the bands of P-N5-REALIZE §3.1's «Rank facts»: movers, gates, c_X, K2
                             < K1 < every β < every e < c_W < K0 < K3 by Ω; every Ω(e) and top even.
-/
import PGLemmas.Genome
import Mathlib.Tactic

namespace PG

namespace Genome

variable {G : Genome}

/-! ## The order by (priority, index) and the injective priority -/

/-- The order by (priority, index). -/
def lexLt (G : Genome) (u v : G.Vertex) : Prop :=
  G.prio u < G.prio v ∨ (G.prio u = G.prio v ∧ G.idx u < G.idx v)

theorem rk_lt_of_lexLt {u v : G.Vertex} (h : G.lexLt u v) : G.rk u < G.rk v := by
  unfold rk
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset]
  · refine ⟨u, Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩, fun hu => ?_⟩
    have h1 := (Finset.mem_filter.mp hu).2
    omega
  · intro w hw
    have hw' := (Finset.mem_filter.mp hw).2
    refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩
    unfold lexLt at h
    omega

theorem lexLt_total (hidx : Function.Injective G.idx) {u v : G.Vertex} (hne : u ≠ v) :
    G.lexLt u v ∨ G.lexLt v u := by
  unfold lexLt
  have : G.idx u ≠ G.idx v := fun e => hne (hidx e)
  omega

theorem rk_injective (hidx : Function.Injective G.idx) : Function.Injective G.rk := by
  intro u v e
  by_contra hne
  rcases lexLt_total hidx hne with h | h
  · have := rk_lt_of_lexLt h
    omega
  · have := rk_lt_of_lexLt h
    omega

/-- `pr` is injective once the vertex index is. -/
theorem pr_injective_of_idx (hidx : Function.Injective G.idx) : Function.Injective G.pr := by
  intro u v e
  apply rk_injective hidx
  unfold pr at e
  omega

/-- The relevance order of `pr` is the order by (priority, index). -/
theorem pr_lt_iff_of_idx (hidx : Function.Injective G.idx) {u v : G.Vertex} :
    G.pr u < G.pr v ↔ G.lexLt u v := by
  constructor
  · intro h
    by_contra hn
    have hne : u ≠ v := by
      rintro rfl
      exact lt_irrefl _ h
    rcases lexLt_total hidx hne with h' | h'
    · exact hn h'
    · have := rk_lt_of_lexLt h'
      unfold pr at h
      omega
  · intro h
    have := rk_lt_of_lexLt h
    unfold pr
    omega

/-- `pr` has the parity of the priority. -/
theorem even_pr {v : G.Vertex} : Even (G.pr v) ↔ Even (G.prio v) := by
  unfold pr
  rw [Nat.even_iff, Nat.even_iff]
  omega

/-! ## The (x, k) order position -/

/-- `Σ_{x' < x} deg(x')`. -/
def below (G : Genome) (x : Fin G.N) : ℕ :=
  ∑ x' ∈ Finset.univ.filter (fun x' : Fin G.N => x' < x), G.deg x'

theorem M_eq : G.M = ∑ x, G.deg x := by
  unfold M
  rw [Fintype.card_sigma]
  simp

theorem below_add_le {x x' : Fin G.N} (h : x < x') : G.below x + G.deg x ≤ G.below x' := by
  unfold below
  have hx : x ∉ Finset.univ.filter (fun x'' : Fin G.N => x'' < x) := by simp
  rw [add_comm, ← Finset.sum_insert hx]
  apply Finset.sum_le_sum_of_subset
  intro y hy
  rcases Finset.mem_insert.mp hy with rfl | hy
  · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩
  · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, lt_trans (Finset.mem_filter.mp hy).2 h⟩

theorem below_add_le_M (x : Fin G.N) : G.below x + G.deg x ≤ G.M := by
  rw [M_eq]
  unfold below
  have hx : x ∉ Finset.univ.filter (fun x'' : Fin G.N => x'' < x) := by simp
  rw [add_comm, ← Finset.sum_insert hx]
  exact Finset.sum_le_sum_of_subset (Finset.subset_univ _)

theorem pos_eq (x : Fin G.N) (k : Fin (G.deg x)) : G.pos ⟨x, k⟩ = G.below x + (k : ℕ) := rfl

theorem pos_lt (o : G.Opt) : G.pos o < G.M := by
  obtain ⟨x, k⟩ := o
  have hk := k.isLt
  have := below_add_le_M x
  rw [pos_eq]
  omega

theorem pos_inj {o o' : G.Opt} (e : G.pos o = G.pos o') : o = o' := by
  obtain ⟨x, k⟩ := o
  obtain ⟨x', k'⟩ := o'
  have hk := k.isLt
  have hk' := k'.isLt
  rw [pos_eq, pos_eq] at e
  rcases lt_trichotomy x x' with h | h | h
  · have := below_add_le h
    omega
  · subst h
    have : k = k' := Fin.ext (by omega)
    rw [this]
  · have := below_add_le h
    omega

/-! ## The vertex index is injective -/

theorem idx_injective (h : G.WF) : Function.Injective G.idx := by
  intro u v e
  rcases u with x | o | o | o | _ | _ | _ | _ | _ | _ <;>
  rcases v with x' | o' | o' | o' | _ | _ | _ | _ | _ | _ <;>
  simp only [idx] at e <;>
  (try have g1 := h.gate_lt o) <;> (try have g2 := h.gate_lt o') <;>
  (try have p1 := pos_lt o) <;> (try have p2 := pos_lt o') <;>
  (try have x1 := x.isLt) <;> (try have x2 := x'.isLt) <;>
  first
  | rfl
  | (exfalso; omega)
  | (have e' := h.gate_inj (by omega : G.gate o = G.gate o'); subst e'; rfl)
  | (have e' := pos_inj (by omega : G.pos o = G.pos o'); subst e'; rfl)
  | (have e' : x = x' := Fin.ext (by omega); subst e'; rfl)

theorem pr_injective (h : G.WF) : Function.Injective G.pr :=
  pr_injective_of_idx (idx_injective h)

theorem pr_lt_iff (h : G.WF) {u v : G.Vertex} : G.pr u < G.pr v ↔ G.lexLt u v :=
  pr_lt_iff_of_idx (idx_injective h)

/-- A smaller priority is less relevant. -/
theorem pr_lt_of_prio_lt (h : G.WF) {u v : G.Vertex} (hp : G.prio u < G.prio v) :
    G.pr u < G.pr v :=
  (pr_lt_iff h).mpr (Or.inl hp)

/-! ## The priority bands (P-N5-REALIZE §3.1, «Rank facts») -/

theorem six_le_bprio (o : G.Opt) : 6 ≤ G.bprio o := by
  unfold bprio
  omega

theorem bprio_le_bmax (o : G.Opt) : G.bprio o ≤ G.bmax :=
  Finset.le_sup (f := G.bprio) (Finset.mem_univ o)

theorem bmax_lt_eb : G.bmax < G.eb := by
  unfold eb
  omega

theorem eb_even : G.eb % 2 = 0 := by
  unfold eb
  omega

theorem eb_le_eprio (o : G.Opt) : G.eb ≤ G.eprio o := by
  unfold eprio
  omega

theorem eprio_even (o : G.Opt) : G.eprio o % 2 = 0 := by
  have := eb_even (G := G)
  unfold eprio
  omega

theorem two_le_pmax : 2 ≤ G.pmax := le_max_left _ _

theorem bmax_le_pmax : G.bmax ≤ G.pmax :=
  le_trans (le_max_left _ _) (le_max_right _ _)

theorem eprio_le_pmax (o : G.Opt) : G.eprio o ≤ G.pmax :=
  le_trans (Finset.le_sup (f := G.eprio) (Finset.mem_univ o))
    (le_trans (le_max_right _ _) (le_max_right _ _))

theorem pmax_lt_top : G.pmax + 2 ≤ G.top := by
  unfold top
  omega

theorem top_even : G.top % 2 = 0 := by
  unfold top
  omega

/-- Every β is below every e-vertex. -/
theorem bprio_lt_eprio (o o' : G.Opt) : G.bprio o < G.eprio o' :=
  lt_of_le_of_lt (bprio_le_bmax o) (lt_of_lt_of_le bmax_lt_eb (eb_le_eprio o'))

/-- Every e-vertex is below `c_W`. -/
theorem eprio_lt_top (o : G.Opt) : G.eprio o < G.top := by
  have := eprio_le_pmax o
  have := pmax_lt_top (G := G)
  omega

/-- Every β is below `c_W`. -/
theorem bprio_lt_top (o : G.Opt) : G.bprio o < G.top := by
  have := bprio_le_bmax o
  have := bmax_le_pmax (G := G)
  have := pmax_lt_top (G := G)
  omega

/-- §3.1 «Rank facts»: `K1 < c_W` by Ω.  This is where `WF.one_le_N` (an option exists) is used. -/
theorem prio_K1_lt_top (h : G.WF) : G.prio Vertex.K1 < G.prio Vertex.cW := by
  have o : G.Opt := ⟨⟨0, h.one_le_N⟩, G.start ⟨0, h.one_le_N⟩⟩
  have := six_le_bprio o
  have := bprio_lt_top o
  simp only [prio]
  omega

/-- The e-vertices: the vertices `e_g`. -/
def isE (G : Genome) : G.Vertex → Bool
  | .eface _ => true
  | _ => false

/-- R121 E-DOM, from the priorities alone: «Every vertex more relevant than some e-vertex is an
e-vertex, c_W, K0 or K3, by [DEF]». -/
theorem e_dom (h : G.WF) {v : G.Vertex} {o : G.Opt} (hv : G.pr (Vertex.eface o) < G.pr v) :
    G.isE v = true ∨ v = Vertex.cW ∨ v = Vertex.K0 ∨ v = Vertex.K3 := by
  have hl := (pr_lt_iff h).mp hv
  unfold lexLt at hl
  have h6 := six_le_bprio o
  have hbo := bprio_lt_eprio o o
  have hb := fun o' => bprio_lt_eprio (G := G) o' o
  rcases v with x | o' | o' | o' | _ | _ | _ | _ | _ | _
  · -- a mover has priority 0
    exfalso
    have := hb o
    simp only [prio] at hl
    omega
  · exfalso
    have := hb o
    simp only [prio] at hl
    omega
  · exfalso
    have := hb o'
    simp only [prio] at hl
    omega
  · exact Or.inl rfl
  · exfalso
    have := hb o
    simp only [prio] at hl
    omega
  · exact Or.inr (Or.inl rfl)
  · exact Or.inr (Or.inr (Or.inl rfl))
  · exfalso
    have := hb o
    simp only [prio] at hl
    omega
  · exfalso
    have := hb o
    simp only [prio] at hl
    omega
  · exact Or.inr (Or.inr (Or.inr rfl))

end Genome

end PG
