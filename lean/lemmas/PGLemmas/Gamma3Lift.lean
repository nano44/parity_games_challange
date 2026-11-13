/-
`Genome.pad_value : G.PadValueStatement` (RESULTS R117 Lemma PAD (c), the value transport) and
`Genome.lift_start : G.LiftStartStatement` (PGLemmas/Gamma3LiftStatement.lean).

Route (P-N5-REACH §5 (c)):
* p′ of Γ3 restricted to Γ's vertices orders them as p′ of Γ and has the same parity (`pr3_old_lt_iff`,
  `even_pr3_old`): the priorities and indices of Γ's vertices are unchanged (`gamma3_old`), and p′ is the
  order by (priority, index).
* `lift3 s` is legal in Γ3 (`lift3_legal`), so Lemma PAD (`pad`) applies to it.
* The play of `old v` in Γ3 is v's play in Γ with one pad inserted after each padded step:
  `lift3 s`^[f n] (old v) = old (s^[n] v) with f n = n + npad s v n (`iterate_f`), and every other iterate is
  a pad (`cover`).
* So the cycle node (by PAD it is no pad), the first visit of it, and the P-set correspond; a pad takes its
  successor's value with one more step (`val_step`, PAD); and the order of two values whose (Λ, Π) differ is
  read off Λ and Π only.
-/
import PGLemmas.Gamma3LiftStatement
import PGLemmas.Gamma3Pad
import PGLemmas.Gamma3Basic
import PGLemmas.Play
import PGLemmas.Order
import Mathlib.Tactic

namespace PG

namespace Genome

variable {G : Genome}

open Classical
open scoped symmDiff

/-! ## The first visit of the cycle node, for any vertex type -/

theorem plen_eq_iff {V : Type*} [Fintype V] (pr : V → ℕ) (s : V → V) (v : V) (n : ℕ) :
    plen pr s v = n ↔ s^[n] v = lam pr s v ∧ ∀ j < n, s^[j] v ≠ lam pr s v := by
  unfold plen
  rw [Nat.find_eq_iff]

/-! ## p′ of Γ3 on Γ's vertices -/

/-- The order by (priority, index) on Γ3. -/
def lex3Lt (G : Genome) (π : G.Carrier) (u v : G.Vertex3) : Prop :=
  G.prio3 π u < G.prio3 π v ∨ (G.prio3 π u = G.prio3 π v ∧ G.idx3 u < G.idx3 v)

theorem rk3_lt_of_lex3Lt {π : G.Carrier} {u v : G.Vertex3} (h : G.lex3Lt π u v) :
    G.rk3 π u < G.rk3 π v := by
  unfold rk3
  apply Finset.card_lt_card
  rw [Finset.ssubset_iff_of_subset]
  · refine ⟨u, Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩, fun hu => ?_⟩
    have h1 := (Finset.mem_filter.mp hu).2
    omega
  · intro w hw
    have hw' := (Finset.mem_filter.mp hw).2
    refine Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩
    unfold lex3Lt at h
    omega

theorem pr3_lt_iff (h : G.WF) {π : G.Carrier} {u v : G.Vertex3} :
    G.pr3 π u < G.pr3 π v ↔ G.lex3Lt π u v := by
  have hidx := idx3_injective h
  have total : ∀ {a b : G.Vertex3}, a ≠ b → G.lex3Lt π a b ∨ G.lex3Lt π b a := by
    intro a b hne
    unfold lex3Lt
    have : G.idx3 a ≠ G.idx3 b := fun e => hne (hidx e)
    omega
  constructor
  · intro hl
    by_contra hn
    have hne : u ≠ v := by
      rintro rfl
      exact lt_irrefl _ hl
    rcases total hne with h' | h'
    · exact hn h'
    · have := rk3_lt_of_lex3Lt h'
      unfold pr3 at hl
      omega
  · intro hl
    have := rk3_lt_of_lex3Lt hl
    unfold pr3
    omega

theorem pr3_injective (h : G.WF) (π : G.Carrier) : Function.Injective (G.pr3 π) := by
  intro u v e
  by_contra hne
  have hidx := idx3_injective h
  have : G.idx3 u ≠ G.idx3 v := fun e' => hne (hidx e')
  have h1 := (pr3_lt_iff h (π := π) (u := u) (v := v)).mpr
  have h2 := (pr3_lt_iff h (π := π) (u := v) (v := u)).mpr
  unfold lex3Lt at h1 h2
  omega

theorem pr3_old_lt_iff (h : G.WF) {u w : G.Vertex} :
    G.pr3 G.r104 (.old u) < G.pr3 G.r104 (.old w) ↔ G.pr u < G.pr w := by
  rw [pr3_lt_iff h, pr_lt_iff h]
  unfold lex3Lt lexLt
  rw [prio3_r104_old, prio3_r104_old]
  rfl

theorem pr3_old_le_iff (h : G.WF) {u w : G.Vertex} :
    G.pr3 G.r104 (.old u) ≤ G.pr3 G.r104 (.old w) ↔ G.pr u ≤ G.pr w := by
  rw [← not_lt, ← not_lt, pr3_old_lt_iff h]

theorem even_pr3_old {u : G.Vertex} : Even (G.pr3 G.r104 (.old u)) ↔ Even (G.pr u) := by
  unfold pr3 pr
  rw [prio3_r104_old, Nat.even_iff, Nat.even_iff]
  omega

/-! ## Pads and the lift -/

theorem padAt_spec {a b : G.Vertex} {p : G.Vertex3} (hp : G.padAt a b = some p) :
    Vertex3.isPad G p = true ∧ G.padSucc p = .old b := by
  cases a <;> cases b <;> simp only [padAt] at hp <;>
  (try split_ifs at hp) <;> (try simp at hp) <;> (try subst hp) <;>
  (try (rename_i e; subst e)) <;>
  simp_all [Vertex3.isPad, padSucc]

theorem lift3_old (s : G.Vertex → G.Vertex) (a : G.Vertex) :
    G.lift3 s (.old a) = (G.padAt a (s a)).getD (.old (s a)) := rfl

theorem lift3_pad (s : G.Vertex → G.Vertex) {p : G.Vertex3} (hp : Vertex3.isPad G p = true) :
    G.lift3 s p = G.padSucc p := by
  cases p with
  | old v => simp [Vertex3.isPad] at hp
  | _ => rfl

theorem lift3_old_none {s : G.Vertex → G.Vertex} {a : G.Vertex} (hn : G.padAt a (s a) = none) :
    G.lift3 s (.old a) = .old (s a) := by
  rw [lift3_old, hn]
  rfl

theorem lift3_old_some {s : G.Vertex → G.Vertex} {a : G.Vertex} {p : G.Vertex3}
    (hp : G.padAt a (s a) = some p) : G.lift3 s (.old a) = p := by
  rw [lift3_old, hp]
  rfl

/-- The lift of a legal successor map of Γ is legal in Γ3. -/
theorem lift3_legal {s : G.Vertex → G.Vertex} (hs : ∀ a, s a ∈ G.E a) :
    ∀ x, G.lift3 s x ∈ G.E3 x := by
  intro x
  cases x with
  | old a =>
    have ha := hs a
    rw [lift3_old]
    cases a with
    | mover x =>
      simp only [E, Finset.mem_image, Finset.mem_univ, true_and] at ha
      obtain ⟨k, hk⟩ := ha
      rw [← hk]
      simp [padAt, E3]
    | gate o =>
      simp only [E, Finset.mem_insert, Finset.mem_singleton] at ha
      rcases ha with hk | hk <;> rw [hk] <;> simp [padAt, E3]
    | beta o =>
      cases hx : G.xt o with
      | none =>
        simp only [E, hx, Finset.mem_singleton] at ha
        rw [ha]
        simp [padAt, E3, hx]
      | some y =>
        simp only [E, hx, Finset.mem_insert, Finset.mem_singleton] at ha
        rcases ha with hk | hk <;> rw [hk] <;> simp [padAt, E3, hx]
    | eface o =>
      cases hw : G.wt o with
      | none =>
        simp only [E, hw, Finset.mem_singleton] at ha
        rw [ha]
        simp [padAt, E3, hw]
      | some y =>
        simp only [E, hw, Finset.mem_singleton] at ha
        rw [ha]
        simp [padAt, E3, hw]
    | cX =>
      simp only [E, Finset.mem_singleton] at ha
      rw [ha]; simp [padAt, E3]
    | cW =>
      simp only [E, Finset.mem_singleton] at ha
      rw [ha]; simp [padAt, E3]
    | K0 =>
      simp only [E, Finset.mem_insert, Finset.mem_singleton] at ha
      rcases ha with hk | hk <;> rw [hk] <;> simp [padAt, E3]
    | K1 =>
      simp only [E, Finset.mem_insert, Finset.mem_singleton] at ha
      rcases ha with hk | hk <;> rw [hk] <;> simp [padAt, E3]
    | K2 =>
      simp only [E, Finset.mem_insert, Finset.mem_singleton] at ha
      rcases ha with hk | hk <;> rw [hk] <;> simp [padAt, E3]
    | K3 =>
      simp only [E, Finset.mem_insert, Finset.mem_singleton] at ha
      rcases ha with hk | hk <;> rw [hk] <;> simp [padAt, E3]
  | _ => simp [lift3, padSucc, E3]

/-! ## The play of `old v` in Γ3 -/

section Play

variable {s : G.Vertex → G.Vertex}

/-- Padded steps among the first n. -/
theorem npad_succ (s : G.Vertex → G.Vertex) (v : G.Vertex) (n : ℕ) :
    G.npad s v (n + 1) =
      G.npad s v n + (if (G.padAt (s^[n] v) (s (s^[n] v))).isSome then 1 else 0) := by
  unfold npad
  rw [Finset.range_add_one, Finset.filter_insert]
  split_ifs with hc
  · rw [Finset.card_insert_of_notMem (by simp)]
  · rfl

/-- `lift3 s`^[n + npad n] (old v) = old (s^[n] v). -/
theorem iterate_f (s : G.Vertex → G.Vertex) (v : G.Vertex) (n : ℕ) :
    (G.lift3 s)^[n + G.npad s v n] (.old v) = .old (s^[n] v) := by
  induction n with
  | zero => simp [npad]
  | succ n ih =>
    rw [npad_succ]
    cases hp : G.padAt (s^[n] v) (s (s^[n] v)) with
    | none =>
      simp only [Option.isSome_none, Bool.false_eq_true, ite_false, add_zero]
      rw [show n + 1 + G.npad s v n = 1 + (n + G.npad s v n) by omega, Function.iterate_add_apply, ih]
      simp only [Function.iterate_one]
      rw [lift3_old_none hp, Function.iterate_succ_apply']
    | some p =>
      simp only [Option.isSome_some, ite_true]
      rw [show n + 1 + (G.npad s v n + 1) = 2 + (n + G.npad s v n) by omega,
        Function.iterate_add_apply, ih]
      have hpad := padAt_spec hp
      rw [show (2 : ℕ) = 1 + 1 from rfl, Function.iterate_add_apply]
      simp only [Function.iterate_one]
      rw [lift3_old_some hp, lift3_pad s hpad.1, hpad.2, Function.iterate_succ_apply']

/-- The iterate after a padded step is the pad. -/
theorem iterate_f_pad (s : G.Vertex → G.Vertex) (v : G.Vertex) (n : ℕ) {p : G.Vertex3}
    (hp : G.padAt (s^[n] v) (s (s^[n] v)) = some p) :
    (G.lift3 s)^[n + G.npad s v n + 1] (.old v) = p := by
  rw [Function.iterate_succ_apply', iterate_f, lift3_old_some hp]

theorem f_strictMono (s : G.Vertex → G.Vertex) (v : G.Vertex) :
    StrictMono (fun n => n + G.npad s v n) := by
  apply strictMono_nat_of_lt_succ
  intro n
  show n + G.npad s v n < n + 1 + G.npad s v (n + 1)
  rw [npad_succ]
  split_ifs <;> omega

/-- Every iterate of `old v` is `old (s^[n] v)` at time f n or the pad after a padded step n. -/
theorem cover (s : G.Vertex → G.Vertex) (v : G.Vertex) (N : ℕ) :
    ∃ n, N = n + G.npad s v n ∨
      (N = n + G.npad s v n + 1 ∧ ∃ p, G.padAt (s^[n] v) (s (s^[n] v)) = some p) := by
  induction N with
  | zero => exact ⟨0, Or.inl (by simp [npad])⟩
  | succ N ih =>
    obtain ⟨n, hn | ⟨hn, p, hp⟩⟩ := ih
    · cases hq : G.padAt (s^[n] v) (s (s^[n] v)) with
      | none =>
        refine ⟨n + 1, Or.inl ?_⟩
        rw [npad_succ, hq]
        simp only [Option.isSome_none, Bool.false_eq_true, ite_false]
        omega
      | some q => exact ⟨n, Or.inr ⟨by omega, q, hq⟩⟩
    · refine ⟨n + 1, Or.inl ?_⟩
      rw [npad_succ, hp]
      simp only [Option.isSome_some, ite_true]
      omega

/-- An iterate of `old v` that is a vertex of Γ comes at a time f n. -/
theorem iterate_old (s : G.Vertex → G.Vertex) (v : G.Vertex) {N : ℕ} {u : G.Vertex}
    (h : (G.lift3 s)^[N] (.old v) = .old u) : ∃ n, N = n + G.npad s v n ∧ s^[n] v = u := by
  obtain ⟨n, hn | ⟨hn, p, hp⟩⟩ := cover s v N
  · refine ⟨n, hn, ?_⟩
    rw [hn, iterate_f] at h
    exact Vertex3.old.inj h
  · exfalso
    rw [hn, iterate_f_pad s v n hp] at h
    have := (padAt_spec hp).1
    rw [h] at this
    simp [Vertex3.isPad] at this

theorem npad_zero (s : G.Vertex → G.Vertex) (v : G.Vertex) : G.npad s v 0 = 0 := by
  simp [npad]

/-- Cycles of Γ3 through Γ's vertices are the cycles of Γ. -/
theorem onCycle_old_iff (s : G.Vertex → G.Vertex) (v u : G.Vertex) :
    OnCycle (G.lift3 s) (.old v) (.old u) ↔ OnCycle s v u := by
  constructor
  · rintro ⟨⟨N, hN⟩, P, hP0, hP⟩
    obtain ⟨n, -, hn⟩ := iterate_old s v hN
    obtain ⟨m, hm, hmu⟩ := iterate_old s u hP
    refine ⟨⟨n, hn⟩, m, ?_, hmu⟩
    rcases Nat.eq_zero_or_pos m with h0 | h0
    · subst h0
      rw [npad_zero] at hm
      omega
    · exact h0
  · rintro ⟨⟨n, hn⟩, p, hp0, hp⟩
    refine ⟨⟨n + G.npad s v n, by rw [iterate_f, hn]⟩, p + G.npad s u p, by omega, ?_⟩
    rw [iterate_f, hp]

end Play

section Transport

variable {s : G.Vertex → G.Vertex}

theorem r104_pb_ge (o : G.Opt) : 3 ≤ G.r104.pb o := by
  show 3 ≤ G.bprio o
  have := six_le_bprio (G := G) o
  omega

theorem r104_pe_ge (o : G.Opt) : 3 ≤ G.r104.pe o := by
  show 3 ≤ G.eprio o
  have h1 := eb_le_eprio (G := G) o
  have h2 := bmax_lt_eb (G := G)
  have h3 := bprio_le_bmax (G := G) o
  have h4 := six_le_bprio (G := G) o
  omega

/-- (c1) The cycle node of `old v` is `old` of v's cycle node. -/
theorem lam_old (h : G.WF) (hs : ∀ a, s a ∈ G.E a) (v : G.Vertex) :
    lam (G.pr3 G.r104) (G.lift3 s) (.old v) = .old (lam G.pr s v) := by
  have hp := (pad (G := G) G.r104 r104_pb_ge r104_pe_ge (G.lift3 s) (lift3_legal hs) (.old v)).2.1
  have hspec := lam_spec (G.pr3 G.r104) (G.lift3 s) (.old v)
  obtain ⟨c', hc'⟩ : ∃ c', lam (G.pr3 G.r104) (G.lift3 s) (.old v) = .old c' := by
    revert hp
    cases lam (G.pr3 G.r104) (G.lift3 s) (.old v) with
    | old c => exact fun _ => ⟨c, rfl⟩
    | _ => simp [Vertex3.isPad]
  rw [hc'] at hspec ⊢
  have hcyc' := (onCycle_old_iff s v c').mp hspec.1
  have hc := lam_spec G.pr s v
  have h1 := hspec.2 _ ((onCycle_old_iff s v _).mpr hc.1)
  rw [pr3_old_le_iff h] at h1
  have h2 := hc.2 _ hcyc'
  have : c' = lam G.pr s v := pr_injective h (le_antisymm h2 h1)
  rw [this]

/-- (c1) The first visit of the cycle node comes after ℓ + npad steps. -/
theorem plen_old (h : G.WF) (hs : ∀ a, s a ∈ G.E a) (v : G.Vertex) :
    plen (G.pr3 G.r104) (G.lift3 s) (.old v) = plen G.pr s v + G.npad s v (plen G.pr s v) := by
  have hl := iterate_plen G.pr s v
  have hmin : ∀ j < plen G.pr s v, s^[j] v ≠ lam G.pr s v := fun j hj => iterate_ne_lam_of_lt_plen hj
  have hlam := lam_old h hs v
  generalize plen G.pr s v = ℓ at hl hmin ⊢
  rw [plen_eq_iff]
  refine ⟨?_, ?_⟩
  · rw [iterate_f, hl, hlam]
  · intro N hN he
    rw [hlam] at he
    obtain ⟨n, hn, hnv⟩ := iterate_old s v he
    have : n < ℓ := by
      by_contra hc
      have := (f_strictMono s v).monotone (not_lt.mp hc)
      omega
    exact hmin n this hnv

/-- (c1) The P-set of `old v` is the image of v's P-set. -/
theorem pset_old (h : G.WF) (hs : ∀ a, s a ∈ G.E a) (v : G.Vertex) :
    pset (G.pr3 G.r104) (G.lift3 s) (.old v) = (pset G.pr s v).image Vertex3.old := by
  ext u
  constructor
  · intro hu
    have hnp := (pad (G := G) G.r104 r104_pb_ge r104_pe_ge (G.lift3 s) (lift3_legal hs) (.old v)).2.2 u hu
    rw [mem_pset, lam_old h hs, plen_old h hs] at hu
    obtain ⟨hgt, N, hN, hNu⟩ := hu
    cases u with
    | old b =>
      obtain ⟨n, hn, hnb⟩ := iterate_old s v hNu
      have hlt : n < plen G.pr s v := (f_strictMono s v).lt_iff_lt.mp (by show n + G.npad s v n < plen G.pr s v + G.npad s v (plen G.pr s v); omega)
      rw [pr3_old_lt_iff h] at hgt
      exact Finset.mem_image.mpr ⟨b, mem_pset.mpr ⟨hgt, n, hlt, hnb⟩, rfl⟩
    | _ => simp [Vertex3.isPad] at hnp
  · intro hu
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp hu
    obtain ⟨hgt, n, hn, hnb⟩ := mem_pset.mp hb
    rw [mem_pset, lam_old h hs, plen_old h hs, pr3_old_lt_iff h]
    refine ⟨hgt, n + G.npad s v n, (f_strictMono s v).lt_iff_lt.mpr hn, ?_⟩
    rw [iterate_f, hnb]

theorem val_old (h : G.WF) (hs : ∀ a, s a ∈ G.E a) (v : G.Vertex) :
    val (G.pr3 G.r104) (G.lift3 s) (.old v) =
      ⟨.old (lam G.pr s v), (pset G.pr s v).image Vertex3.old,
        plen G.pr s v + G.npad s v (plen G.pr s v)⟩ := by
  unfold val
  rw [lam_old h hs, pset_old h hs, plen_old h hs]

/-- (c2) A pad takes its successor's value with one more step. -/
theorem pad_step (h : G.WF) (hs : ∀ a, s a ∈ G.E a) {p : G.Vertex3}
    (hp : Vertex3.isPad G p = true) :
    lam (G.pr3 G.r104) (G.lift3 s) p = lam (G.pr3 G.r104) (G.lift3 s) (G.padSucc p) ∧
    pset (G.pr3 G.r104) (G.lift3 s) p = pset (G.pr3 G.r104) (G.lift3 s) (G.padSucc p) ∧
    plen (G.pr3 G.r104) (G.lift3 s) p = plen (G.pr3 G.r104) (G.lift3 s) (G.padSucc p) + 1 := by
  have hpr := pr3_injective h G.r104
  have hP := pad (G := G) G.r104 r104_pb_ge r104_pe_ge (G.lift3 s) (lift3_legal hs) p
  have hne : lam (G.pr3 G.r104) (G.lift3 s) p ≠ p := by
    intro e
    have := hP.2.1
    rw [e, hp] at this
    exact Bool.noConfusion this
  have hsucc := lift3_pad s hp
  refine ⟨?_, ?_, ?_⟩
  · rw [← hsucc]
    exact (lam_succ hpr p).symm
  · have hv := congrArg Val.set (val_step hpr hne)
    simp only [val, ext] at hv
    by_cases hc : G.pr3 G.r104 (lam (G.pr3 G.r104) (G.lift3 s) (G.lift3 s p)) < G.pr3 G.r104 p
    · simp only [hc, ↓reduceIte] at hv
      exfalso
      have hmem : p ∈ pset (G.pr3 G.r104) (G.lift3 s) p := by
        rw [hv]
        simp only [Finset.mem_insert, true_or]
      have := hP.2.2 p hmem
      rw [hp] at this
      exact Bool.noConfusion this
    · simp only [hc, ↓reduceIte] at hv
      rw [hv, hsucc]
  · rw [← hsucc]
    exact plen_succ hpr hne

theorem rew_old_lt_iff (h : G.WF) {a b : G.Vertex} :
    rew (G.pr3 G.r104) (.old a) < rew (G.pr3 G.r104) (.old b) ↔ rew G.pr a < rew G.pr b := by
  have h1 := pr3_old_lt_iff h (u := a) (w := b)
  have h2 := pr3_old_lt_iff h (u := b) (w := a)
  have pos : ∀ n : ℕ, ¬ Even n → 0 < n := fun n hn =>
    Nat.pos_of_ne_zero (fun e => hn (by rw [e]; exact ⟨0, rfl⟩))
  have pa := pos (G.pr a)
  have pb := pos (G.pr b)
  have qa := pos (G.pr3 G.r104 (.old a))
  have qb := pos (G.pr3 G.r104 (.old b))
  have ea : Even (G.pr3 G.r104 (.old a)) ↔ Even (G.pr a) := even_pr3_old
  have eb : Even (G.pr3 G.r104 (.old b)) ↔ Even (G.pr b) := even_pr3_old
  unfold rew
  by_cases ha : Even (G.pr a) <;> by_cases hb : Even (G.pr b) <;>
  simp only [ea, eb, ha, hb, ↓reduceIte] <;>
  (try have := pa ha) <;> (try have := pb hb) <;>
  (try have := qa (by rwa [ea])) <;> (try have := qb (by rwa [eb])) <;>
  omega

theorem old_injective : Function.Injective (Vertex3.old : G.Vertex → G.Vertex3) :=
  fun _ _ e => Vertex3.old.inj e

theorem setLt_image_iff (h : G.WF) (A B : Finset G.Vertex) :
    setLt (G.pr3 G.r104) (A.image Vertex3.old) (B.image Vertex3.old) ↔ setLt G.pr A B := by
  unfold setLt
  constructor
  · rintro ⟨d, hd, hmax, hpar⟩
    have hd2 := hd
    simp only [Finset.mem_symmDiff, Finset.mem_image] at hd2
    obtain ⟨d', rfl⟩ : ∃ d', d = Vertex3.old d' := by
      rcases hd2 with ⟨⟨y, -, rfl⟩, -⟩ | ⟨⟨y, -, rfl⟩, -⟩ <;> exact ⟨y, rfl⟩
    refine ⟨d', ?_, fun x hx => ?_, ?_⟩
    · simp only [Finset.mem_symmDiff, old_injective.mem_finset_image] at hd ⊢
      exact hd
    · apply (pr3_old_le_iff h).mp
      apply hmax
      simp only [Finset.mem_symmDiff, old_injective.mem_finset_image] at hx ⊢
      exact hx
    · rwa [even_pr3_old, old_injective.mem_finset_image, old_injective.mem_finset_image] at hpar
  · rintro ⟨d, hd, hmax, hpar⟩
    refine ⟨.old d, ?_, fun x hx => ?_, ?_⟩
    · simp only [Finset.mem_symmDiff, old_injective.mem_finset_image] at hd ⊢
      exact hd
    · have hx2 := hx
      simp only [Finset.mem_symmDiff, Finset.mem_image] at hx2
      obtain ⟨x', rfl⟩ : ∃ x', x = Vertex3.old x' := by
        rcases hx2 with ⟨⟨y, -, rfl⟩, -⟩ | ⟨⟨y, -, rfl⟩, -⟩ <;> exact ⟨y, rfl⟩
      apply (pr3_old_le_iff h).mpr
      apply hmax
      simp only [Finset.mem_symmDiff, old_injective.mem_finset_image] at hx ⊢
      exact hx
    · rwa [even_pr3_old, old_injective.mem_finset_image, old_injective.mem_finset_image]

/-- (c3) Values whose (Λ, Π) differ compare as in Γ. -/
theorem val_old_lt_iff (h : G.WF) (hs : ∀ a, s a ∈ G.E a) {u w : G.Vertex}
    (hne : (lam G.pr s u, pset G.pr s u) ≠ (lam G.pr s w, pset G.pr s w)) :
    Val.lt (G.pr3 G.r104) (val (G.pr3 G.r104) (G.lift3 s) (.old u))
        (val (G.pr3 G.r104) (G.lift3 s) (.old w)) ↔
      Val.lt G.pr (val G.pr s u) (val G.pr s w) := by
  have hne' : ¬ (lam G.pr s u = lam G.pr s w ∧ pset G.pr s u = pset G.pr s w) :=
    fun ⟨a, b⟩ => hne (Prod.ext a b)
  rw [val_old h hs, val_old h hs]
  unfold Val.lt val
  simp only [Vertex3.old.injEq, (Finset.image_injective old_injective).eq_iff]
  rw [rew_old_lt_iff h, setLt_image_iff h]
  constructor
  · rintro (h1 | ⟨h1, h2⟩ | ⟨h1, h2, -⟩ | ⟨h1, h2, -⟩)
    · exact Or.inl h1
    · exact Or.inr (Or.inl ⟨h1, h2⟩)
    · exact absurd ⟨h1, h2⟩ hne'
    · exact absurd ⟨h1, h2⟩ hne'
  · rintro (h1 | ⟨h1, h2⟩ | ⟨h1, h2, -⟩ | ⟨h1, h2, -⟩)
    · exact Or.inl h1
    · exact Or.inr (Or.inl ⟨h1, h2⟩)
    · exact absurd ⟨h1, h2⟩ hne'
    · exact absurd ⟨h1, h2⟩ hne'

end Transport

/-- **Lemma PAD (c)**, the value transport (RESULTS R117; P-N5-REACH §5 (c)). -/
theorem pad_value : G.PadValueStatement := by
  intro h s hs
  exact ⟨fun v => ⟨lam_old h hs v, pset_old h hs v, plen_old h hs v⟩,
    fun p hp => pad_step h hs hp, fun u w hne => val_old_lt_iff h hs hne⟩

/-- **The lift of Γ's start is Γ3's standard start.** -/
theorem lift_start : G.LiftStartStatement := by
  intro v
  cases v with
  | old a =>
    cases a with
    | beta o =>
      cases hx : G.xt o <;> simp [lift3, padAt, start0, start3, std3, hx]
    | eface o =>
      cases hw : G.wt o <;> simp [lift3, padAt, start0, start3, std3, hw]
    | _ => simp [lift3, padAt, start0, start3, std3]
  | _ => rfl

end Genome

end PG
