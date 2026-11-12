/-
Lemma LAM-GAP in its SHARP form (claude/l-si docs/si/box101-lamgap.md §2; claude/l-red
docs/red/R234-lamgap.md §3), and its corollaries BR-SEG and BR-SEG-G (RESULTS R118 (d), (i)(a)).
The statements are in `PGLemmas/Statements.lean`; this file proves them.

Proof outline (box 101 §2's steps, with R234 §3's sharpening):
* `SPath`           a simple path to a top, with its vertex set, its value and its number of
                    choice vertices before the end (box 101: P, value(P), c(P));
* `lower_bound`     claim (L): after `k` steps every value dominates the value of every simple
                    path with at most `k` choice vertices;
* `play_spath`      claim (U): the play prefix of a vertex is such a path, with the vertex's value;
* `lam_gap_sharp`   if the window had a step after time `a + |Ch|`, some `x ∈ Ch` would switch
                    there; both for a top `x` (R234 §3) and for a non-top `x` (box 101 (E)) this
                    contradicts Howard's rule.
-/
import PGLemmas.Play
import PGLemmas.Statements

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V] {pr : V → ℕ}

/-- The edges a path may use: any edge `v → u ∈ E v` at a choice vertex, the one fixed edge
`v → f v` elsewhere. -/
def Edge (E : V → Finset V) (Ch : Finset V) (f : V → V) (v u : V) : Prop :=
  (v ∈ Ch ∧ u ∈ E v) ∨ (v ∉ Ch ∧ u = f v)

/-- `SPath pr edge Ch ℓ v S x c`: a simple path from `v` to `ℓ` along `edge`, with vertex set
`S`, value `x` (box 101's `value(P)`) and `c` vertices of `Ch` before `ℓ` (box 101's `c(P)`). -/
inductive SPath (pr : V → ℕ) (edge : V → V → Prop) (Ch : Finset V) (ℓ : V) :
    V → Finset V → Val V → ℕ → Prop
  | nil : SPath pr edge Ch ℓ ℓ {ℓ} ⟨ℓ, ∅, 0⟩ 0
  | cons {v u : V} {S : Finset V} {x : Val V} {c : ℕ} :
      edge v u → v ∉ S → SPath pr edge Ch ℓ u S x c →
      SPath pr edge Ch ℓ v (insert v S) (ext pr v x) (if v ∈ Ch then c + 1 else c)

omit [Fintype V] in
theorem SPath.top_eq {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V} {x : Val V}
    {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) : x.top = ℓ := by
  induction h with
  | nil => rfl
  | cons _ _ _ ih => simpa using ih

omit [Fintype V] in
theorem SPath.end_mem {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V} {x : Val V}
    {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) : ℓ ∈ S := by
  induction h with
  | nil => exact Finset.mem_singleton_self ℓ
  | cons _ _ _ ih => exact Finset.mem_insert_of_mem ih

omit [Fintype V] in
theorem SPath.set_subset {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V}
    {x : Val V} {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) : x.set ⊆ S := by
  induction h with
  | nil => exact Finset.empty_subset _
  | cons _ _ _ ih =>
    exact (ext_set_subset _ _).trans (Finset.insert_subset_insert _ ih)

omit [Fintype V] in
/-- The choice vertices before the end are counted by `c`; the end is not counted. -/
theorem SPath.count_eq {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V}
    {x : Val V} {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) :
    c + (if ℓ ∈ Ch then 1 else 0) = (Ch ∩ S).card := by
  induction h with
  | nil =>
    by_cases hℓ : ℓ ∈ Ch
    · simp [hℓ]
    · simp [hℓ]
  | @cons v u S x c _ hvS _ ih =>
    by_cases hv : v ∈ Ch
    · have hnot : v ∉ Ch ∩ S := fun hmem => hvS (Finset.mem_inter.mp hmem).2
      rw [Finset.inter_insert_of_mem hv, Finset.card_insert_of_notMem hnot, ← ih]
      simp only [hv, ite_true]
      omega
    · rw [Finset.inter_insert_of_notMem hv, ← ih]
      simp only [hv, ite_false]

omit [Fintype V] in
theorem SPath.count_le {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V}
    {x : Val V} {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) : c ≤ Ch.card := by
  have h1 := h.count_eq
  have h2 : (Ch ∩ S).card ≤ Ch.card := Finset.card_le_card Finset.inter_subset_left
  omega

omit [Fintype V] in
theorem SPath.count_lt {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V}
    {x : Val V} {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) (hℓ : ℓ ∈ Ch) : c + 1 ≤ Ch.card := by
  have h1 := h.count_eq
  have h2 : (Ch ∩ S).card ≤ Ch.card := Finset.card_le_card Finset.inter_subset_left
  simp only [hℓ, ite_true] at h1
  omega

/-- One step of claim (L) inside one state `σ`: if `x` is dominated by the value of `v`'s
successor, `v` is not the end of `x`'s path and not on it, then `ext(v, x)` is dominated by the
value of `v`.  Both cases of box 101 §2 (L): `v ≠ Λ(v)` by (P1), (P2); `v = Λ(v)` by rewards. -/
theorem ext_le_val (hpr : Function.Injective pr) {σ : V → V} {v : V} {x : Val V}
    (h : Val.le pr x (val pr σ (σ v))) (htop : x.top ≠ v) (hv : v ∉ x.set) :
    Val.le pr (ext pr v x) (val pr σ v) := by
  by_cases hl : lam pr σ v = v
  · rw [val_of_lam_eq hl]
    have htop' : (val pr σ (σ v)).top = v := by
      show lam pr σ (σ v) = v
      rw [lam_succ hpr, hl]
    rcases Val.top_of_le h with e | hlt
    · exact absurd (e.trans htop') htop
    · rw [htop'] at hlt
      exact Val.le_of_lt (Val.lt_of_rew_lt hlt)
  · rw [val_step hpr hl]
    exact ext_le hv (notMem_pset_succ hpr hl) h

/-- Claim (L) of box 101 §2.  In a window, `k` steps after `a`, the value of every vertex `v`
dominates the value of every simple path from `v` to a top `ℓ` that has at most `k` choice
vertices before `ℓ`. -/
theorem lower_bound (hpr : Function.Injective pr) {E : V → Finset V} {Ch : Finset V}
    {s : ℕ → V → V} {a b : ℕ} (W : Window pr E Ch s a b) :
    ∀ k, a + k ≤ b → ∀ ℓ, lam pr (s a) ℓ = ℓ → ∀ {v : V} {S : Finset V} {x : Val V} {c : ℕ},
      SPath pr (Edge E Ch (s a)) Ch ℓ v S x c → c ≤ k → Val.le pr x (val pr (s (a + k)) v) := by
  -- the two cases that do not look back in time
  have hnil : ∀ t, a ≤ t → t ≤ b → ∀ ℓ, lam pr (s a) ℓ = ℓ →
      Val.le pr ⟨ℓ, ∅, 0⟩ (val pr (s t) ℓ) := by
    intro t hat htb ℓ hℓ
    rw [val_of_lam_eq ((W.lamConst t hat htb ℓ).trans hℓ)]
    exact Val.le_refl _
  have hfix : ∀ t, a ≤ t → t ≤ b → ∀ {ℓ v u : V} {S : Finset V} {x : Val V} {c : ℕ},
      SPath pr (Edge E Ch (s a)) Ch ℓ u S x c → v ∉ S → v ∉ Ch → Edge E Ch (s a) v u →
      Val.le pr x (val pr (s t) u) → Val.le pr (ext pr v x) (val pr (s t) v) := by
    intro t hat htb ℓ v u S x c hP hvS hvCh hedge hle
    have hu : u = s t v := by
      rcases hedge with ⟨h, -⟩ | ⟨-, h⟩
      · exact absurd h hvCh
      · rw [h, W.fixed t hat htb v hvCh]
    rw [hu] at hle
    refine ext_le_val hpr hle ?_ (fun hmem => hvS (hP.set_subset hmem))
    rw [hP.top_eq]
    rintro rfl
    exact hvS hP.end_mem
  intro k
  induction k with
  | zero =>
    intro hk ℓ hℓ v S x c hP
    induction hP with
    | nil => intro _; exact hnil a le_rfl hk ℓ hℓ
    | @cons v u S x c hedge hvS hP' ih =>
      intro hc
      by_cases hvCh : v ∈ Ch
      · simp only [hvCh, ite_true] at hc
        omega
      · simp only [hvCh, ite_false] at hc
        exact hfix a le_rfl hk hP' hvS hvCh hedge (ih hc)
  | succ k ihk =>
    intro hk ℓ hℓ v S x c hP
    induction hP with
    | nil => intro _; exact hnil (a + (k + 1)) (by omega) hk ℓ hℓ
    | @cons v u S x c hedge hvS hP' ih =>
      intro hc
      by_cases hvCh : v ∈ Ch
      · -- a choice vertex: look one step back
        simp only [hvCh, ite_true] at hc
        have hprev : Val.le pr x (val pr (s (a + k)) u) := ihk (by omega) ℓ hℓ hP' (by omega)
        have huE : u ∈ E v := by
          rcases hedge with ⟨-, h⟩ | ⟨h, -⟩
          · exact h
          · exact absurd hvCh h
        obtain ⟨-, hbest, -⟩ := W.howard (a + k) (by omega) (by omega) v hvCh
        have hmono := W.mono (a + k) (by omega) (by omega) (s (a + k + 1) v)
        have hle : Val.le pr x (val pr (s (a + k + 1)) (s (a + k + 1) v)) :=
          Val.le_trans hpr (Val.le_trans hpr hprev (hbest u huE)) hmono
        refine ext_le_val hpr hle ?_ (fun hmem => hvS (hP'.set_subset hmem))
        rw [hP'.top_eq]
        rintro rfl
        exact hvS hP'.end_mem
      · simp only [hvCh, ite_false] at hc
        exact hfix (a + (k + 1)) (by omega) hk hP' hvS hvCh hedge (ih hc)

/-- Claim (U) of box 101 §2: the play prefix of `v` under `σ` is a simple path from `v` to
`Λ(v)` whose value is `val v`. -/
theorem play_spath (hpr : Function.Injective pr) {E : V → Finset V} {Ch : Finset V} {f : V → V}
    {σ : V → V} (hσ : ∀ v, Edge E Ch f v (σ v)) :
    ∀ n v, plen pr σ v = n → ∃ S c, SPath pr (Edge E Ch f) Ch (lam pr σ v) v S (val pr σ v) c ∧
      ∀ u ∈ S, ∃ j, j ≤ n ∧ σ^[j] v = u := by
  intro n
  induction n with
  | zero =>
    intro v hv
    have hl := lam_eq_of_plen_eq_zero hv
    refine ⟨{v}, 0, ?_, ?_⟩
    · rw [val_of_lam_eq hl, hl]
      exact SPath.nil
    · intro u hu
      rw [Finset.mem_singleton] at hu
      exact ⟨0, le_rfl, hu.symm⟩
  | succ n ih =>
    intro v hv
    have hl : lam pr σ v ≠ v := by
      intro h
      rw [plen_eq_zero_of_lam_eq h] at hv
      omega
    have hp := plen_succ hpr hl
    obtain ⟨S, c, hP, hS⟩ := ih (σ v) (by omega)
    have hvS : v ∉ S := by
      intro hmem
      obtain ⟨j, hj, hjv⟩ := hS v hmem
      exact iterate_succ_ne_self hpr hl (by omega) hjv
    refine ⟨insert v S, if v ∈ Ch then c + 1 else c, ?_, ?_⟩
    · rw [val_step hpr hl, ← lam_succ hpr v]
      exact SPath.cons (hσ v) hvS hP
    · intro u hu
      rw [Finset.mem_insert] at hu
      rcases hu with rfl | hu
      · exact ⟨0, by omega, rfl⟩
      · obtain ⟨j, hj, hju⟩ := hS u hu
        exact ⟨j + 1, by omega, by rw [Function.iterate_succ_apply]; exact hju⟩

/-- (L) and (U) together: a value at a later state `t'` of the window is dominated by the value
`k` steps after `a`, as soon as `k` bounds the choice vertices a play prefix can have. -/
theorem val_le_of_play (hpr : Function.Injective pr) {E : V → Finset V} {Ch : Finset V}
    {s : ℕ → V → V} {a b : ℕ} (W : Window pr E Ch s a b) {k t' : ℕ} (hk : a + k ≤ b)
    (hat' : a + 1 ≤ t') (ht'b : t' ≤ b) (v : V)
    (hcount : Ch.card ≤ k ∨ (lam pr (s t') v ∈ Ch ∧ Ch.card ≤ k + 1)) :
    Val.le pr (val pr (s t') v) (val pr (s (a + k)) v) := by
  -- the state `t'` follows the edges
  have hσ : ∀ u, Edge E Ch (s a) u (s t' u) := by
    intro u
    by_cases hu : u ∈ Ch
    · obtain ⟨hE, -, -⟩ := W.howard (t' - 1) (by omega) (by omega) u hu
      have e : t' - 1 + 1 = t' := by omega
      rw [e] at hE
      exact Or.inl ⟨hu, hE⟩
    · exact Or.inr ⟨hu, W.fixed t' (by omega) ht'b u hu⟩
  obtain ⟨S, c, hP, -⟩ := play_spath hpr hσ (plen pr (s t') v) v rfl
  have hℓ : lam pr (s a) (lam pr (s t') v) = lam pr (s t') v := by
    rw [W.lamConst t' (by omega) ht'b v]
    exact lam_lam hpr v
  have hc : c ≤ k := by
    rcases hcount with h | ⟨hmem, h⟩
    · exact hP.count_le.trans h
    · have := hP.count_lt hmem
      omega
  exact lower_bound hpr W k hk _ hℓ hP hc

/-- **Lemma LAM-GAP, SHARP form.**  A window of a Howard run on which every vertex keeps its
cycle node has at most `|Ch|` steps. -/
theorem lam_gap_sharp : LamGapSharpStatement V := by
  intro pr hpr E Ch s a b W
  by_contra hcon
  have hb : a + Ch.card < b := by omega
  -- `Ch` is not empty: otherwise the first step changes nothing
  have hne : Ch.Nonempty := by
    by_contra hemp
    rw [Finset.not_nonempty_iff_eq_empty] at hemp
    apply W.moves a le_rfl (by omega)
    funext v
    exact W.fixed (a + 1) (by omega) (by omega) v (by simp [hemp])
  obtain ⟨m, hm⟩ : ∃ m, Ch.card = m + 1 := ⟨Ch.card - 1, by
    have := Finset.card_pos.mpr hne
    omega⟩
  -- times: `a + m = t* - 1`, `a + m + 1 = t*`, `a + m + 1 + 1 = t* + 1 ≤ b`
  have hb' : a + m + 1 + 1 ≤ b := by omega
  -- some `x ∈ Ch` switches at `t*`
  obtain ⟨x, hx⟩ : ∃ x, s (a + m + 1 + 1) x ≠ s (a + m + 1) x :=
    Function.ne_iff.mp (W.moves (a + m + 1) (by omega) (by omega))
  have hxCh : x ∈ Ch := by
    by_contra h
    apply hx
    rw [W.fixed (a + m + 1 + 1) (by omega) hb' x h, W.fixed (a + m + 1) (by omega) (by omega) x h]
  obtain ⟨huE, hubest, -⟩ := W.howard (a + m) (by omega) (by omega) x hxCh
  obtain ⟨hwE, hwbest, hwkeep⟩ := W.howard (a + m + 1) (by omega) (by omega) x hxCh
  -- `u` = the successor at `t*`, `w` = the successor at `t* + 1`; `u` was not best at `t*`
  have hlt : Val.lt pr (val pr (s (a + m + 1)) (s (a + m + 1) x))
      (val pr (s (a + m + 1)) (s (a + m + 1 + 1) x)) := by
    by_contra hnot
    apply hx
    apply hwkeep
    refine ⟨huE, fun y hy => Val.le_trans hpr (hwbest y hy) ?_⟩
    rcases Val.lt_trichotomy hpr (val pr (s (a + m + 1)) (s (a + m + 1) x))
      (val pr (s (a + m + 1)) (s (a + m + 1 + 1) x)) with h | h | h
    · exact absurd h hnot
    · exact Or.inr h.symm
    · exact Or.inl h
  have hlamx : lam pr (s (a + m + 1 + 1)) x = lam pr (s (a + m + 1)) x := by
    rw [W.lamConst (a + m + 1 + 1) (by omega) hb' x, W.lamConst (a + m + 1) (by omega) (by omega) x]
  by_cases htop : lam pr (s (a + m + 1)) x = x
  · -- `x` is a top (R234 §3): the values of `u` and `w` did not change in the step before
    have hback : ∀ y, lam pr (s (a + m + 1)) y = x →
        val pr (s (a + m)) y = val pr (s (a + m + 1)) y := by
      intro y hy
      apply Val.le_antisymm hpr (W.mono (a + m) (by omega) (by omega) y)
      exact val_le_of_play hpr W (k := m) (t' := a + m + 1) (by omega) (by omega) (by omega) y
        (Or.inr ⟨by rw [hy]; exact hxCh, by omega⟩)
    have hu : lam pr (s (a + m + 1)) (s (a + m + 1) x) = x := by rw [lam_succ hpr, htop]
    have hw : lam pr (s (a + m + 1)) (s (a + m + 1 + 1) x) = x := by
      rw [W.lamConst (a + m + 1) (by omega) (by omega),
        ← W.lamConst (a + m + 1 + 1) (by omega) hb', lam_succ hpr, hlamx, htop]
    have hle := hubest (s (a + m + 1 + 1) x) hwE
    rw [hback _ hu, hback _ hw] at hle
    exact Val.not_le_of_lt hpr hlt hle
  · -- `x` is not a top (box 101 (E)): no value changes in the step `t* → t* + 1`
    have hconst : ∀ y, val pr (s (a + m + 1 + 1)) y = val pr (s (a + m + 1)) y := by
      intro y
      refine Val.le_antisymm hpr ?_ (W.mono (a + m + 1) (by omega) (by omega) y)
      exact val_le_of_play hpr W (k := m + 1) (t' := a + m + 1 + 1) (by omega) (by omega) hb' y
        (Or.inl (by omega))
    have htop' : lam pr (s (a + m + 1 + 1)) x ≠ x := by rw [hlamx]; exact htop
    have h1 : val pr (s (a + m + 1)) x = ext pr x (val pr (s (a + m + 1)) (s (a + m + 1) x)) :=
      val_step hpr htop
    have h2 : val pr (s (a + m + 1)) x =
        ext pr x (val pr (s (a + m + 1)) (s (a + m + 1 + 1) x)) := by
      rw [← hconst x, val_step hpr htop', hconst]
    have hnu : x ∉ (val pr (s (a + m + 1)) (s (a + m + 1) x)).set := notMem_pset_succ hpr htop
    have hnw : x ∉ (val pr (s (a + m + 1)) (s (a + m + 1 + 1) x)).set := by
      rw [← hconst]
      exact notMem_pset_succ hpr htop'
    have := ext_lt hnu hnw hlt
    rw [← h1, ← h2] at this
    exact Val.lt_irrefl _ this

end

end PG
