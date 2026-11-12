/-
Box 208 Addendum A, Lemma PLATEAU on the genome, and the quiet window of §4 (C4):
`plateau_g : G.PlateauGStatement`, `quiet : G.QuietStatement`
(`PGLemmas/GenomeLevelStatement.lean`).  No premise.

One lemma serves both, `IdealCycRun.window_le`: on a window u..v of a run let Y be a set of
vertices such that at every state of the window (a) the classes of Y are those of state u, (b) Y
is closed under the successor map, (c) every gate of a mover of Y is in Y, and (d) every step
switches a mover of Y.  Then v − u ≤ N.  It is `plateau` (`PGLemmas/Plateau.lean`) with
Ch := the movers of Y; the hypothesis of `plateau` that needs work is that Odd does not move in Y:

* `IdealCycRun.gate_const` ((P4)): a gate of Y has the same chosen face at any two states of the
  window.  The chosen face is in Y (b).  If Odd were at the W-face at one state and at the Ξ-face
  at another, both faces are in Y and (K4) at the two states gives them EQUAL classes; then
  - `gate_of_cls_eq_some`: if the W-target is a mover, e_g ∈ E(e_g) = E(β_g), so the play of β_g
    passes e_g, whose only predecessor is g (`succ_eq_eface`): Odd is at the W-face;
  - `gate_of_cls_eq_none`: if the W-face leads to c_W, both values are (c_W, ∅, ·) with lengths 1
    and ≥ 2, and c_W is even, so LOC-GATE (`OptCounter.le_succ`) puts Odd at the Ξ-face.
  (The second case is not in box 208's text; it is met only with Y := all vertices.)

* `plateau_g`: Y := the vertices whose key at u is at most the front's.  (P1) the front of u and
  its classes persist through stalls; (P2) classes do not rise along plays; (P3) by (K5); (P6) with
  the repair of REFEREE 32 (R-box208-preread §5.2) = Addendum B1 (1)(a): if a step of the window
  switched no mover of Y, then by induction up to b the movers of Y keep their gates and the
  values on Y are those of that state (≤ by optimality against the answer σ̄ of that state,
  `val_congr`; ≥ by F1), so the front would not lag.
* `quiet`: Y := all vertices; (d) is `IdealCycRun.moves`.
-/
import PGLemmas.GenomeLevel
import PGLemmas.Plateau

namespace PG

open Classical

noncomputable section

namespace Genome

variable {G : Genome}

/-! ### One state -/

section State

variable {s : G.Vertex → G.Vertex}

/-- The only vertex whose successor is `e_g` is the gate `g`. -/
theorem succ_eq_eface (hs : G.IsState s) {p : G.Vertex} {o : G.Opt}
    (hp : s p = Vertex.eface o) : p = Vertex.gate o := by
  rcases p with x | o' | o' | o' | _ | _ | _ | _ | _ | _
  · obtain ⟨k, hk⟩ := hs.mover x
    rw [hk] at hp
    cases hp
  · rcases hs.gate o' with hk | hk <;> rw [hk] at hp <;> cases hp
    rfl
  · rw [hs.beta o'] at hp
    simp only [start0] at hp
    cases hx : G.xt o' <;> rw [hx] at hp <;> cases hp
  · rw [hs.eface o'] at hp
    simp only [start0] at hp
    cases hx : G.wt o' <;> rw [hx] at hp <;> cases hp
  · rw [hs.cX] at hp
    cases hp
  · rw [hs.cW] at hp
    cases hp
  · rw [hs.K0] at hp
    cases hp
  · rw [hs.K1] at hp
    cases hp
  · rcases hs.K2 with hk | hk <;> rw [hk] at hp <;> cases hp
  · rw [hs.K3] at hp
    cases hp

/-- Only `K0` and `K3` are more relevant than `c_W`. -/
theorem cW_dom (h : G.WF) {u : G.Vertex} (hu : G.pr Vertex.cW < G.pr u) :
    u = Vertex.K0 ∨ u = Vertex.K3 := by
  have hlow : ∀ w : G.Vertex, G.prio w < G.prio Vertex.cW → ¬ G.pr Vertex.cW < G.pr w :=
    fun w hp => lt_asymm (pr_lt_of_prio_lt h hp)
  have h1 := pmax_lt_top (G := G)
  have h2 := two_le_pmax (G := G)
  rcases u with x | o | o | o | _ | _ | _ | _ | _ | _
  · exact absurd hu (hlow _ (by simp only [prio]; omega))
  · exact absurd hu (hlow _ (by simp only [prio]; omega))
  · exact absurd hu (hlow _ (by simp only [prio]; exact bprio_lt_top o))
  · exact absurd hu (hlow _ (by simp only [prio]; exact eprio_lt_top o))
  · exact absurd hu (hlow _ (by simp only [prio]; omega))
  · exact absurd hu (lt_irrefl _)
  · exact Or.inl rfl
  · exact absurd hu (hlow _ (prio_K1_lt_top h))
  · exact absurd hu (hlow _ (by simp only [prio]; omega))
  · exact Or.inr rfl

/-- A play that ends in `c_W` has an empty path component. -/
theorem pset_of_lam_cW (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1)
    {v : G.Vertex} (hl : lam G.pr s v = Vertex.cW) : pset G.pr s v = ∅ := by
  ext u
  simp only [Finset.notMem_empty, iff_false]
  intro hu
  have hlt := (mem_pset.mp hu).1
  rw [hl] at hlt
  rcases cW_dom h hlt with rfl | rfl
  · have e := lam_of_K0_mem h hs hk hu
    rw [hl] at e
    cases e
  · have e := lam_of_K3_mem h hs hk hu
    rw [hl] at e
    cases e

/-- Equal classes at the two faces of a gate whose W-target is a mover: Odd is at the W-face. -/
theorem gate_of_cls_eq_some (h : G.WF) (hs : G.IsState s) (hb : G.BOnly s) {o : G.Opt}
    {y : Fin G.N} (hw : G.wt o = some y)
    (he : G.cls s (Vertex.eface o) = G.cls s (Vertex.beta o)) :
    s (Vertex.gate o) = Vertex.eface o := by
  have hc := (cls_eface h hs hb hw).1
  have hmem : Vertex.eface o ∈ G.eset s (Vertex.beta o) := by
    have h2 : (G.cls s (Vertex.eface o)).2 = G.eset s (Vertex.beta o) := by
      rw [he]
      rfl
    rw [← h2, hc]
    exact Finset.mem_insert_self _ _
  obtain ⟨-, j, -, hj⟩ := mem_pset.mp (mem_eset.mp hmem).1
  cases j with
  | zero =>
    rw [Function.iterate_zero_apply] at hj
    cases hj
  | succ i =>
    rw [Function.iterate_succ_apply'] at hj
    have e := succ_eq_eface hs hj
    rw [e] at hj
    exact hj

/-- Equal classes at the two faces of a gate whose W-face leads to `c_W`: Odd is at the Ξ-face.
`hloc` is LOC-GATE at this gate (`OptCounter.le_succ`). -/
theorem gate_of_cls_eq_none (h : G.WF) (hs : G.IsState s) (hk : s Vertex.K2 = Vertex.K1)
    {o : G.Opt}
    (hloc : Val.le G.pr (val G.pr s (s (Vertex.gate o))) (val G.pr s (Vertex.beta o)))
    (hw : G.wt o = none) (he : G.cls s (Vertex.eface o) = G.cls s (Vertex.beta o)) :
    s (Vertex.gate o) = Vertex.beta o := by
  have hpr := pr_injective h
  rcases hs.gate o with hg | hg
  · exfalso
    have hce := cls_eface_none h hs hw
    have hle : lam G.pr s (Vertex.eface o) = Vertex.cW := congrArg Prod.fst hce
    have hlb : lam G.pr s (Vertex.beta o) = Vertex.cW :=
      (congrArg Prod.fst he).symm.trans hle
    have hse : s (Vertex.eface o) = Vertex.cW := by
      rw [hs.eface o]
      simp only [start0, hw]
    have hpe : plen G.pr s (Vertex.eface o) = 1 := by
      have hne : lam G.pr s (Vertex.eface o) ≠ Vertex.eface o := by
        rw [hle]
        exact fun e => by cases e
      rw [plen_succ hpr hne, hse, plen_eq_zero_of_lam_eq (lam_cW hs)]
    have hpb : 2 ≤ plen G.pr s (Vertex.beta o) := by
      have hne1 : lam G.pr s (Vertex.beta o) ≠ Vertex.beta o := by
        rw [hlb]
        exact fun e => by cases e
      have h1 := plen_succ hpr hne1
      have hl2 : lam G.pr s (s (Vertex.beta o)) = Vertex.cW := by
        rw [lam_succ hpr]
        exact hlb
      have hne2 : lam G.pr s (s (Vertex.beta o)) ≠ s (Vertex.beta o) := by
        rw [hl2, hs.beta o]
        simp only [start0]
        cases G.xt o <;> exact fun e => by cases e
      have h2 := plen_succ hpr hne2
      omega
    have hse' := pset_of_lam_cW h hs hk hle
    have hsb' := pset_of_lam_cW h hs hk hlb
    rw [hg] at hloc
    rcases hloc with hlt | heq
    · rcases hlt with h1 | ⟨-, h2⟩ | ⟨-, -, -, h4⟩ | ⟨-, -, h3, -⟩
      · have h1' : rew G.pr (lam G.pr s (Vertex.eface o)) <
            rew G.pr (lam G.pr s (Vertex.beta o)) := h1
        rw [hle, hlb] at h1'
        exact lt_irrefl _ h1'
      · have h2' : setLt G.pr (pset G.pr s (Vertex.eface o)) (pset G.pr s (Vertex.beta o)) := h2
        rw [hse', hsb'] at h2'
        exact setLt_irrefl _ h2'
      · have h4' : ¬ Even (G.pr (lam G.pr s (Vertex.eface o))) := h4
        rw [hle] at h4'
        apply h4'
        rw [even_pr]
        simp only [prio]
        exact Nat.even_iff.mpr top_even
      · have h3' : plen G.pr s (Vertex.beta o) < plen G.pr s (Vertex.eface o) := h3
        omega
    · have h' : plen G.pr s (Vertex.eface o) = plen G.pr s (Vertex.beta o) :=
        congrArg Val.len heq
      omega
  · exact hg

end State

/-! ### Two states of a run -/

variable {σ τ : ℕ → G.Vertex → G.Vertex} {T : ℕ}

/-- Odd cannot be at the W-face of a gate at one state and at its Ξ-face at another, if both
faces lie in a set `Y` whose classes agree at the two states. -/
theorem IdealCycRun.gate_const_aux (h : G.WF) (R : G.IdealCycRun σ τ T) {t t' : ℕ} (ht : t ≤ T)
    (ht' : t' ≤ T) {Y : Finset G.Vertex}
    (hcls : ∀ x ∈ Y, G.cls (nxt G.V0 σ τ t) x = G.cls (nxt G.V0 σ τ t') x) {o : G.Opt}
    (he : Vertex.eface o ∈ Y) (hβ : Vertex.beta o ∈ Y)
    (hg : nxt G.V0 σ τ t (Vertex.gate o) = Vertex.eface o)
    (hg' : nxt G.V0 σ τ t' (Vertex.gate o) = Vertex.beta o) : False := by
  have hs := R.isState ht
  have hs' := R.isState ht'
  have hbo := R.bOnly h ht
  have hbo' := R.bOnly h ht'
  have k := k4 h (σ t) (τ t) (R.opt t ht) hs o
  have k' := k4 h (σ t') (τ t') (R.opt t' ht') hs' o
  have c1 : G.cls (nxt G.V0 σ τ t) (Vertex.gate o) =
      G.cls (nxt G.V0 σ τ t) (Vertex.eface o) := by
    rw [cls_step h hs hbo (v := Vertex.gate o) rfl, hg]
  have c2 : G.cls (nxt G.V0 σ τ t') (Vertex.gate o) =
      G.cls (nxt G.V0 σ τ t') (Vertex.beta o) := by
    rw [cls_step h hs' hbo' (v := Vertex.gate o) rfl, hg']
  have l1 : G.clsLe (G.cls (nxt G.V0 σ τ t) (Vertex.eface o))
      (G.cls (nxt G.V0 σ τ t) (Vertex.beta o)) := by
    rw [← c1]
    exact k.2.2
  have l2 : G.clsLe (G.cls (nxt G.V0 σ τ t') (Vertex.beta o))
      (G.cls (nxt G.V0 σ τ t') (Vertex.eface o)) := by
    rw [← c2]
    exact k'.2.1
  rw [← hcls _ hβ, ← hcls _ he] at l2
  have heq : G.cls (nxt G.V0 σ τ t) (Vertex.eface o) =
      G.cls (nxt G.V0 σ τ t) (Vertex.beta o) :=
    clsKey_injective h (le_antisymm ((clsKey_le_iff h).mp l1) ((clsKey_le_iff h).mp l2))
  cases hw : G.wt o with
  | some y =>
    have heq' : G.cls (nxt G.V0 σ τ t') (Vertex.eface o) =
        G.cls (nxt G.V0 σ τ t') (Vertex.beta o) := by
      rw [← hcls _ he, ← hcls _ hβ]
      exact heq
    have e := gate_of_cls_eq_some h hs' hbo' hw heq'
    rw [hg'] at e
    cases e
  | none =>
    have hloc := OptCounter.le_succ (pr_injective h) (R.opt t ht) (gate_notMem_V0 o)
      (mem_E_gate.mpr (Or.inr rfl)) (lam_ne_gate h hs _ o)
    have e := gate_of_cls_eq_none h hs (R.k2 h ht) hloc hw heq
    rw [hg] at e
    cases e

/-- (P4): a gate of a set `Y` that is closed at two states and has the same classes at both has
the same chosen face at both. -/
theorem IdealCycRun.gate_const (h : G.WF) (R : G.IdealCycRun σ τ T) {t t' : ℕ} (ht : t ≤ T)
    (ht' : t' ≤ T) {Y : Finset G.Vertex}
    (hcls : ∀ x ∈ Y, G.cls (nxt G.V0 σ τ t) x = G.cls (nxt G.V0 σ τ t') x)
    (hcl : ∀ x ∈ Y, nxt G.V0 σ τ t x ∈ Y) (hcl' : ∀ x ∈ Y, nxt G.V0 σ τ t' x ∈ Y)
    {o : G.Opt} (ho : Vertex.gate o ∈ Y) :
    nxt G.V0 σ τ t (Vertex.gate o) = nxt G.V0 σ τ t' (Vertex.gate o) := by
  have hin := hcl _ ho
  have hin' := hcl' _ ho
  rcases (R.isState ht).gate o with hg | hg <;> rcases (R.isState ht').gate o with hg' | hg'
  · rw [hg, hg']
  · exfalso
    rw [hg] at hin
    rw [hg'] at hin'
    exact R.gate_const_aux h ht ht' hcls hin hin' hg hg'
  · exfalso
    rw [hg] at hin
    rw [hg'] at hin'
    exact R.gate_const_aux h ht' ht (fun x hx => (hcls x hx).symm) hin' hin hg' hg
  · rw [hg, hg']

/-- The window lemma: a window of a run on which a closed set `Y` keeps its classes, contains the
gates of its movers and has a mover switching at every step has at most `N` steps. -/
theorem IdealCycRun.window_le (h : G.WF) (R : G.IdealCycRun σ τ T) {u v : ℕ} (huv : u ≤ v)
    (hvT : v ≤ T) (Y : Finset G.Vertex)
    (hcls : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ Y,
      G.cls (nxt G.V0 σ τ t) x = G.cls (nxt G.V0 σ τ u) x)
    (hclosed : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ Y, nxt G.V0 σ τ t x ∈ Y)
    (hgates : ∀ x, Vertex.mover x ∈ Y → ∀ y ∈ G.E (Vertex.mover x), y ∈ Y)
    (hmoves : ∀ t, u ≤ t → t < v →
      ∃ x, Vertex.mover x ∈ Y ∧ σ (t + 1) (Vertex.mover x) ≠ σ t (Vertex.mover x)) :
    v - u ≤ G.N := by
  have hpr := pr_injective h
  have huT : u ≤ T := huv.trans hvT
  have hfixed : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ Y, x ∉ G.Mov ∩ Y →
      nxt G.V0 σ τ t x = nxt G.V0 σ τ u x := by
    intro t hut htv x hx hxc
    have htT : t ≤ T := htv.trans hvT
    have hs := R.isState htT
    have hsu := R.isState huT
    rcases x with x' | o | o | o | _ | _ | _ | _ | _ | _
    · exact absurd (Finset.mem_inter.mpr ⟨mem_Mov.mpr ⟨x', rfl⟩, hx⟩) hxc
    · exact R.gate_const h htT huT (hcls t hut htv) (hclosed t hut htv)
        (hclosed u le_rfl huv) hx
    · rw [hs.beta o, hsu.beta o]
    · rw [hs.eface o, hsu.eface o]
    · rw [hs.cX, hsu.cX]
    · rw [hs.cW, hsu.cW]
    · rw [hs.K0, hsu.K0]
    · rw [hs.K1, hsu.K1]
    · rw [R.k2 h htT, R.k2 h huT]
    · rw [hs.K3, hsu.K3]
  have hsucc : ∀ x ∈ G.Mov ∩ Y, G.E x ⊆ Y := by
    intro x hx y hy
    obtain ⟨hm, hxY⟩ := Finset.mem_inter.mp hx
    obtain ⟨x', rfl⟩ := mem_Mov.mp hm
    exact hgates x' hxY y hy
  have hedges : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ G.Mov ∩ Y, nxt G.V0 σ τ t x ∈ G.E x :=
    fun t _ htv x _ => (R.isState (htv.trans hvT)).edge x
  have hhow : ∀ t, u ≤ t → t < v → ∀ x ∈ G.Mov ∩ Y,
      HowardAt G.pr G.E (nxt G.V0 σ τ t) (nxt G.V0 σ τ (t + 1)) x := by
    intro t _ htv x hx
    obtain ⟨x', rfl⟩ := mem_Mov.mp (Finset.mem_inter.mp hx).1
    exact R.howard t (lt_of_lt_of_le htv hvT) x'
  have hlam : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ Y,
      lam G.pr (nxt G.V0 σ τ t) x = lam G.pr (nxt G.V0 σ τ u) x :=
    fun t hut htv x hx => congrArg Prod.fst (hcls t hut htv x hx)
  have hmv : ∀ t, u ≤ t → t < v →
      ∃ x ∈ G.Mov ∩ Y, nxt G.V0 σ τ (t + 1) x ≠ nxt G.V0 σ τ t x := by
    intro t hut htv
    obtain ⟨x, hxY, hne⟩ := hmoves t hut htv
    refine ⟨Vertex.mover x, Finset.mem_inter.mpr ⟨mem_Mov.mpr ⟨x, rfl⟩, hxY⟩, ?_⟩
    rw [nxt_mover, nxt_mover]
    exact hne
  have hmain := plateau (V := G.Vertex) G.pr hpr G.E Y (G.Mov ∩ Y) Finset.inter_subset_right
    (nxt G.V0 σ τ) u v huv hclosed hfixed hsucc hedges hhow hlam hmv
  have hsub : G.Mov ⊆ Finset.univ.image (Vertex.mover : Fin G.N → G.Vertex) := by
    intro x hx
    obtain ⟨x', rfl⟩ := mem_Mov.mp hx
    exact Finset.mem_image.mpr ⟨x', Finset.mem_univ _, rfl⟩
  have hcard : (G.Mov ∩ Y).card ≤ G.N := by
    refine (Finset.card_le_card Finset.inter_subset_left).trans ?_
    refine (Finset.card_le_card hsub).trans (Finset.card_image_le.trans ?_)
    rw [Finset.card_univ, Fintype.card_fin]
  exact hmain.trans hcard

/-! ### QUIET -/

/-- **QUIET** (the content of RESULTS R126 QUIET-N; box 208 §4 (C4)): a window of constant
classes has at most `N` steps. -/
theorem quiet : G.QuietStatement := by
  intro h σ τ T R u v huv hvT hc
  have hpr := pr_injective h
  refine R.window_le h huv hvT Finset.univ (fun t hut htv x _ => hc t hut htv x)
    (fun _ _ _ _ _ => Finset.mem_univ _) (fun _ _ _ _ => Finset.mem_univ _) ?_
  intro t _ htv
  have htT : t < T := lt_of_lt_of_le htv hvT
  obtain ⟨x, y, hy, hlt⟩ := R.moves t htT
  refine ⟨x, Finset.mem_univ _, fun e => ?_⟩
  have hbest := (R.howard t htT x).2.1 y hy
  rw [nxt_mover, e] at hbest
  exact Val.not_le_of_lt hpr hlt hbest

/-! ### PLATEAU -/

/-- **Lemma PLATEAU** on the genome (box 208 Addendum A), with the bound `N`. -/
theorem plateau_g : G.PlateauGStatement := by
  intro h σ τ T R b u v huv hvb hbT hstall
  have hpr := pr_injective h
  rcases Nat.eq_or_lt_of_le huv with rfl | hlt
  · simp
  have hvT : v ≤ T := hvb.trans hbT
  -- a vertex of the front at `u`
  obtain ⟨z0, hz0⟩ := lc_front_exists (c := G.ck σ τ) (b := b) (hstall u le_rfl hlt).1
  -- (L1), stall part: the front of `u` and its classes persist up to `v`
  have hpers : ∀ t, u ≤ t → t ≤ v → ∀ x, FrontAt (G.ck σ τ) b u x →
      G.ck σ τ t x = G.ck σ τ u x ∧ FrontAt (G.ck σ τ) b t x := by
    intro t hut
    induction t, hut using Nat.le_induction with
    | base => exact fun _ x hx => ⟨rfl, hx⟩
    | succ t hut ih =>
      intro htv x hx
      obtain ⟨e1, f1⟩ := ih (by omega) x hx
      have hst := hstall t hut (by omega)
      have e2 : G.ck σ τ (t + 1) x = G.ck σ τ t x := hst.2 x f1
      refine ⟨e2.trans e1, ?_, ?_⟩
      · rw [e2]
        exact f1.1
      · intro w hw
        have hwt : G.ck σ τ t w ≠ G.ck σ τ b w :=
          lc_lag_of_lag (c := G.ck σ τ) (a := 0) (b := b)
            (fun t' _ ht' x' => R.ck_step h (lt_of_lt_of_le ht' hbT) x') (Nat.zero_le _)
            (Nat.le_succ t) (by omega) hw
        rw [e2]
        exact (f1.2 w hwt).trans (R.ck_step h (by omega) w)
  -- Y: the vertices at or below the front's class at `u`
  obtain ⟨Y, hY⟩ : ∃ Y : Finset G.Vertex, ∀ x, x ∈ Y ↔ G.ck σ τ u x ≤ G.ck σ τ u z0 :=
    ⟨Finset.univ.filter (fun x => G.ck σ τ u x ≤ G.ck σ τ u z0), fun x => by simp⟩
  -- (P1)
  have hP1 : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ Y, G.ck σ τ t x = G.ck σ τ u x := by
    intro t hut htv x hx
    by_cases hl : G.ck σ τ u x = G.ck σ τ b x
    · refine le_antisymm ?_ (R.ck_mono h hut (htv.trans hvT) x)
      rw [hl]
      exact R.ck_mono h (htv.trans hvb) hbT x
    · exact (hpers t hut htv x ⟨hl, fun w hw => ((hY x).mp hx).trans (hz0.2 w hw)⟩).1
  -- (P2)
  have hclosed : ∀ t, u ≤ t → t ≤ v → ∀ x ∈ Y, nxt G.V0 σ τ t x ∈ Y := by
    intro t hut htv x hx
    have htT := htv.trans hvT
    rw [hY]
    calc G.ck σ τ u (nxt G.V0 σ τ t x) ≤ G.ck σ τ t (nxt G.V0 σ τ t x) := R.ck_mono h hut htT _
      _ ≤ G.ck σ τ t x := (ck_le_iff h).mpr (cls_succ_le h (R.isState htT) (R.bOnly h htT) x)
      _ = G.ck σ τ u x := hP1 t hut htv x hx
      _ ≤ G.ck σ τ u z0 := (hY x).mp hx
  -- (P3)
  have hgates : ∀ x, Vertex.mover x ∈ Y → ∀ y ∈ G.E (Vertex.mover x), y ∈ Y := by
    intro x hx y hy
    rw [hY]
    calc G.ck σ τ u y ≤ G.ck σ τ (u + 1) (Vertex.mover x) :=
          (ck_le_iff h).mpr (k5 h σ τ T R u (lt_of_lt_of_le hlt hvT) x y hy)
      _ = G.ck σ τ u (Vertex.mover x) := hP1 (u + 1) (Nat.le_succ u) (by omega) _ hx
      _ ≤ G.ck σ τ u z0 := (hY _).mp hx
  -- (P6)
  have hP6 : ∀ t, u ≤ t → t < v →
      ∃ x, Vertex.mover x ∈ Y ∧ σ (t + 1) (Vertex.mover x) ≠ σ t (Vertex.mover x) := by
    intro t hut htv
    by_contra hno
    have hno' : ∀ x, Vertex.mover x ∈ Y → σ (t + 1) (Vertex.mover x) = σ t (Vertex.mover x) := by
      intro x hx
      by_contra hne
      exact hno ⟨x, hx, hne⟩
    have htT : t ≤ T := (le_of_lt htv).trans hvT
    have hclt := hclosed t hut (le_of_lt htv)
    have hclaim : ∀ k, t + k ≤ b →
        (∀ x, Vertex.mover x ∈ Y → σ (t + k) (Vertex.mover x) = σ t (Vertex.mover x)) ∧
        (∀ y ∈ Y, val G.pr (nxt G.V0 σ τ (t + k)) y = val G.pr (nxt G.V0 σ τ t) y) := by
      intro k
      induction k with
      | zero => exact fun _ => ⟨fun _ _ => rfl, fun _ _ => rfl⟩
      | succ k ih =>
        intro hk
        obtain ⟨hA, hB⟩ := ih (by omega)
        have hsT : t + k < T := by omega
        show (∀ x, Vertex.mover x ∈ Y →
            σ (t + k + 1) (Vertex.mover x) = σ t (Vertex.mover x)) ∧
          (∀ y ∈ Y, val G.pr (nxt G.V0 σ τ (t + k + 1)) y = val G.pr (nxt G.V0 σ τ t) y)
        -- no mover of Y switches at the step t + k → t + k + 1
        have hA' : ∀ x, Vertex.mover x ∈ Y →
            σ (t + k + 1) (Vertex.mover x) = σ t (Vertex.mover x) := by
          intro x hx
          have hbest := (R.howard t (lt_of_lt_of_le htv hvT) x).2.1
          rw [nxt_mover, hno' x hx] at hbest
          have hkeep := (R.howard (t + k) hsT x).2.2
          rw [nxt_mover, nxt_mover, hA x hx] at hkeep
          apply hkeep
          have hin : σ t (Vertex.mover x) ∈ G.E (Vertex.mover x) := R.legal t htT x
          refine ⟨hin, fun w hw => ?_⟩
          rw [hB w (hgates x hx w hw), hB _ (hgates x hx _ hin)]
          exact hbest w hw
        refine ⟨hA', fun y hy => ?_⟩
        apply Val.le_antisymm hpr
        · -- optimality at t + k + 1, against Odd's answer of state t
          have hopt := (R.opt (t + k + 1) (by omega)).2 (τ t) (R.opt t htT).1 y
          have hcongr : val G.pr (pair G.V0 (σ (t + k + 1)) (τ t)) y =
              val G.pr (nxt G.V0 σ τ t) y := by
            refine val_congr hpr hclt (fun x hx => ?_) hy
            by_cases hxo : x ∈ G.V0
            · rw [pair_of_mem hxo]
              show _ = pair G.V0 (σ t) (τ t) x
              rw [pair_of_mem hxo]
              by_cases hm : ∃ x', x = Vertex.mover x'
              · obtain ⟨x', rfl⟩ := hm
                exact hA' x' hx
              · have hnm : ∀ x', x ≠ Vertex.mover x' := fun x' e => hm ⟨x', e⟩
                rw [R.frozen (t + k + 1) (by omega) x hxo hnm, R.frozen t htT x hxo hnm]
            · rw [pair_of_notMem hxo]
              show _ = pair G.V0 (σ t) (τ t) x
              rw [pair_of_notMem hxo]
          rw [hcongr] at hopt
          exact hopt
        · -- F1
          rw [← hB y hy]
          exact R.f1 h hsT y
    -- at `b` the front vertex `z0` has its value of state `t`: it does not lag at `t`
    obtain ⟨k, hk⟩ := Nat.exists_eq_add_of_le ((le_of_lt htv).trans hvb)
    have hval := (hclaim k (by omega)).2 z0 ((hY z0).mpr le_rfl)
    rw [← hk] at hval
    apply (hpers t hut (le_of_lt htv) z0 hz0).2.1
    apply (ck_eq_iff h).mpr
    have h1 : lam G.pr (nxt G.V0 σ τ b) z0 = lam G.pr (nxt G.V0 σ τ t) z0 :=
      congrArg Val.top hval
    have h2 : pset G.pr (nxt G.V0 σ τ b) z0 = pset G.pr (nxt G.V0 σ τ t) z0 :=
      congrArg Val.set hval
    unfold cls eset
    rw [h1, h2]
  exact R.window_le h huv hvT Y (fun t hut htv x hx => (ck_eq_iff h).mp (hP1 t hut htv x hx))
    hclosed hgates hP6

end Genome

end

end PG
