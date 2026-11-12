/-
DEPTH-COUNT3's count of shallow changes, with R234's fix D1 (`DepthCountStatement`,
`PGLemmas/Statements4.lean`), and `plen < n` for play values.

Proof (box 100 §3 for the set changes, R234 §4 for the length-only changes):
* `topk pr (c+1) Π`  the `c + 1` most relevant elements of a path component (box 100's `P_t`);
* `topk_setLt`, `topk_eq`  a set change of depth `≤ c` raises `P` strictly, one of depth `> c`
                     keeps it;
* along a run with a fixed cycle node the weight of `P` never falls (`run_topk`);
* set changes of depth `≤ c`: `t ↦ (Λ_t, P_t)` is injective and misses the largest `P`;
* length-only changes with `|Π| ≤ c`: `t ↦ (Λ_t, Π_t, len_t)` is injective and, by the direction
  the length moves in, misses one length.
-/
import PGLemmas.Weights
import PGLemmas.LamGap
import PGLemmas.Statements4

namespace PG

open Classical
open scoped symmDiff

noncomputable section

variable {V : Type*} {pr : V → ℕ}

/-- the elements of `S` more relevant than `u` -/
def abv (pr : V → ℕ) (S : Finset V) (u : V) : Finset V := S.filter (fun w => pr u < pr w)

/-- the `k` most relevant elements of `S` -/
def topk (pr : V → ℕ) (k : ℕ) (S : Finset V) : Finset V :=
  S.filter (fun u => (abv pr S u).card < k)

theorem mem_abv {S : Finset V} {u w : V} : w ∈ abv pr S u ↔ w ∈ S ∧ pr u < pr w := by
  unfold abv
  rw [Finset.mem_filter]

theorem mem_topk {k : ℕ} {S : Finset V} {u : V} :
    u ∈ topk pr k S ↔ u ∈ S ∧ (abv pr S u).card < k := by
  unfold topk
  rw [Finset.mem_filter]

theorem card_topk_le (hpr : Function.Injective pr) (k : ℕ) (S : Finset V) :
    (topk pr k S).card ≤ k := by
  have h : (topk pr k S).card ≤ (Finset.range k).card := by
    apply Finset.card_le_card_of_injOn (fun u => (abv pr S u).card)
    · intro u hu
      rw [Finset.mem_coe, Finset.mem_range]
      exact (mem_topk.mp (Finset.mem_coe.mp hu)).2
    · -- vertices with different priorities have different numbers of vertices above them
      have key : ∀ u u', u ∈ S → u' ∈ S → pr u < pr u' →
          (abv pr S u').card < (abv pr S u).card := by
        intro u u' _ hu' hlt
        apply Finset.card_lt_card
        refine ⟨fun w hw => ?_, fun hsub => ?_⟩
        · rw [mem_abv] at hw ⊢
          exact ⟨hw.1, by omega⟩
        · have := hsub (mem_abv.mpr ⟨hu', hlt⟩)
          rw [mem_abv] at this
          omega
      intro u hu u' hu' e
      have huS := (mem_topk.mp (Finset.mem_coe.mp hu)).1
      have hu'S := (mem_topk.mp (Finset.mem_coe.mp hu')).1
      dsimp only at e
      by_contra hne
      rcases Nat.lt_or_gt_of_ne (fun h => hne (hpr h)) with h | h
      · have := key u u' huS hu'S h; omega
      · have := key u' u hu'S huS h; omega
  rwa [Finset.card_range] at h

/-! ### A change of the path component, seen from its top difference `z` -/

section change

variable {M N : Finset V} {z : V}

theorem mem_iff_of_above (hmax : ∀ w ∈ M ∆ N, pr w ≤ pr z) {u : V} (hu : pr z < pr u) :
    u ∈ M ↔ u ∈ N := by
  by_contra hne
  have : u ∈ M ∆ N := by rw [Finset.mem_symmDiff]; tauto
  have := hmax u this
  omega

theorem abv_eq_of_above (hmax : ∀ w ∈ M ∆ N, pr w ≤ pr z) {u : V} (hu : pr z ≤ pr u) :
    abv pr M u = abv pr N u := by
  ext w
  rw [mem_abv, mem_abv]
  constructor
  · rintro ⟨h1, h2⟩
    exact ⟨(mem_iff_of_above hmax (by omega)).mp h1, h2⟩
  · rintro ⟨h1, h2⟩
    exact ⟨(mem_iff_of_above hmax (by omega)).mpr h1, h2⟩

theorem filter_all_eq_abv (hz : z ∈ M ∆ N) (hmax : ∀ w ∈ M ∆ N, pr w ≤ pr z) :
    M.filter (fun u => ∀ w ∈ M ∆ N, pr w < pr u) = abv pr M z := by
  ext u
  rw [Finset.mem_filter, mem_abv]
  constructor
  · rintro ⟨h1, h2⟩
    exact ⟨h1, h2 z hz⟩
  · rintro ⟨h1, h2⟩
    exact ⟨h1, fun w hw => lt_of_le_of_lt (hmax w hw) h2⟩

/-- A set change of depth `≤ c` raises the `c + 1` most relevant elements strictly. -/
theorem topk_setLt {c : ℕ} (h : setLt pr M N)
    (hd : (M.filter (fun u => ∀ w ∈ M ∆ N, pr w < pr u)).card ≤ c) :
    setLt pr (topk pr (c + 1) M) (topk pr (c + 1) N) := by
  obtain ⟨z, hz, hmax, hside⟩ := h
  rw [filter_all_eq_abv hz hmax] at hd
  have hzN : (abv pr N z).card ≤ c := by rw [← abv_eq_of_above hmax le_rfl]; exact hd
  have hz' := hz
  rw [Finset.mem_symmDiff] at hz'
  -- above `z` the two truncations agree
  have hmax' : ∀ u ∈ topk pr (c + 1) M ∆ topk pr (c + 1) N, pr u ≤ pr z := by
    intro u hu
    by_contra hgt
    have hgt' : pr z < pr u := by omega
    have hiff : u ∈ topk pr (c + 1) M ↔ u ∈ topk pr (c + 1) N := by
      rw [mem_topk, mem_topk, mem_iff_of_above hmax hgt', abv_eq_of_above hmax hgt'.le]
    rw [Finset.mem_symmDiff] at hu
    tauto
  rcases hside with ⟨hzin, hev⟩ | ⟨hzin, hodd⟩
  · have hzM : z ∉ M := by
      rcases hz' with ⟨_, h2⟩ | ⟨_, h2⟩
      · exact absurd hzin h2
      · exact h2
    have h1 : z ∈ topk pr (c + 1) N := mem_topk.mpr ⟨hzin, by omega⟩
    have h2 : z ∉ topk pr (c + 1) M := fun h => hzM (mem_topk.mp h).1
    exact ⟨z, by rw [Finset.mem_symmDiff]; exact Or.inr ⟨h1, h2⟩, hmax', Or.inl ⟨h1, hev⟩⟩
  · have hzN' : z ∉ N := by
      rcases hz' with ⟨_, h2⟩ | ⟨_, h2⟩
      · exact h2
      · exact absurd hzin h2
    have h1 : z ∈ topk pr (c + 1) M := mem_topk.mpr ⟨hzin, by omega⟩
    have h2 : z ∉ topk pr (c + 1) N := fun h => hzN' (mem_topk.mp h).1
    exact ⟨z, by rw [Finset.mem_symmDiff]; exact Or.inl ⟨h1, h2⟩, hmax', Or.inr ⟨h1, hodd⟩⟩

/-- A set change of depth `> c` keeps the `c + 1` most relevant elements. -/
theorem topk_eq {c : ℕ} (h : setLt pr M N)
    (hd : c < (M.filter (fun u => ∀ w ∈ M ∆ N, pr w < pr u)).card) :
    topk pr (c + 1) M = topk pr (c + 1) N := by
  obtain ⟨z, hz, hmax, -⟩ := h
  rw [filter_all_eq_abv hz hmax] at hd
  have hzN : c < (abv pr N z).card := by rw [← abv_eq_of_above hmax le_rfl]; exact hd
  ext u
  rw [mem_topk, mem_topk]
  by_cases hu : pr z < pr u
  · rw [mem_iff_of_above hmax hu, abv_eq_of_above hmax hu.le]
  · -- at or below `z`: more than `c` vertices lie above, in both sets
    have hM : (abv pr M z).card ≤ (abv pr M u).card := by
      apply Finset.card_le_card
      intro w hw
      rw [mem_abv] at hw ⊢
      exact ⟨hw.1, by omega⟩
    have hN : (abv pr N z).card ≤ (abv pr N u).card := by
      apply Finset.card_le_card
      intro w hw
      rw [mem_abv] at hw ⊢
      exact ⟨hw.1, by omega⟩
    constructor
    · rintro ⟨_, h2⟩; omega
    · rintro ⟨_, h2⟩; omega

end change

/-! ### Values with a common cycle node -/

theorem topk_wt_le (hpr : Function.Injective pr) (c : ℕ) {x y : Val V} (hle : Val.le pr x y)
    (htop : x.top = y.top) :
    wt pr (topk pr (c + 1) x.set) ≤ wt pr (topk pr (c + 1) y.set) := by
  rcases hle with hlt | rfl
  · rw [Val.lt_iff] at hlt
    rcases hlt with hr | ⟨-, hs | ⟨es, -⟩⟩
    · rw [htop] at hr; exact absurd hr (lt_irrefl _)
    · by_cases hd : (x.set.filter (fun u => ∀ w ∈ x.set ∆ y.set, pr w < pr u)).card ≤ c
      · exact (wt_lt_of_setLt hpr (topk_setLt hs hd)).le
      · rw [topk_eq hs (by omega)]
    · rw [es]
  · exact le_rfl

theorem topk_wt_lt (hpr : Function.Injective pr) {c : ℕ} {x y : Val V} (hle : Val.le pr x y)
    (htop : x.top = y.top) (hne : x.set ≠ y.set) (hd : depth pr x y ≤ c) :
    wt pr (topk pr (c + 1) x.set) < wt pr (topk pr (c + 1) y.set) := by
  unfold depth at hd
  rw [ite_eq_right hne] at hd
  rcases hle with hlt | rfl
  · rw [Val.lt_iff] at hlt
    rcases hlt with hr | ⟨-, hs | ⟨es, -⟩⟩
    · rw [htop] at hr; exact absurd hr (lt_irrefl _)
    · exact wt_lt_of_setLt hpr (topk_setLt hs hd)
    · exact absurd es hne
  · exact absurd rfl hne

/-! ### A run that never falls -/

section run

variable {x : ℕ → Val V} {T : ℕ}

theorem run_le (hpr : Function.Injective pr) (hle : ∀ t, t < T → Val.le pr (x t) (x (t + 1))) :
    ∀ t t', t ≤ t' → t' ≤ T → Val.le pr (x t) (x t') := by
  have h : ∀ d t, t + d ≤ T → Val.le pr (x t) (x (t + d)) := by
    intro d
    induction d with
    | zero => intro t _; exact Val.le_refl _
    | succ d ih =>
      intro t ht
      exact Val.le_trans hpr (ih t (by omega)) (hle (t + d) (by omega))
  intro t t' htt' ht'
  have := h (t' - t) t (by omega)
  have e : t + (t' - t) = t' := by omega
  rwa [e] at this

theorem run_rew (hpr : Function.Injective pr) (hle : ∀ t, t < T → Val.le pr (x t) (x (t + 1)))
    {t t' : ℕ} (htt' : t ≤ t') (ht' : t' ≤ T) : rew pr (x t).top ≤ rew pr (x t').top := by
  rcases Val.top_of_le (run_le hpr hle t t' htt' ht') with e | h
  · rw [e]
  · exact h.le

theorem run_top_const (hpr : Function.Injective pr)
    (hle : ∀ t, t < T → Val.le pr (x t) (x (t + 1))) {t u t' : ℕ} (htu : t ≤ u) (hut' : u ≤ t')
    (ht' : t' ≤ T) (he : (x t).top = (x t').top) : (x u).top = (x t).top := by
  apply rew_injective hpr
  apply le_antisymm
  · have := run_rew hpr hle hut' ht'
    rwa [← he] at this
  · exact run_rew hpr hle htu (by omega)

/-- With a fixed cycle node, the weight of the `c + 1` most relevant elements never falls. -/
theorem run_topk (hpr : Function.Injective pr) (hle : ∀ t, t < T → Val.le pr (x t) (x (t + 1)))
    (c : ℕ) : ∀ d t, t + d ≤ T → (x t).top = (x (t + d)).top →
      wt pr (topk pr (c + 1) (x t).set) ≤ wt pr (topk pr (c + 1) (x (t + d)).set) := by
  intro d
  induction d with
  | zero => intro t _ _; exact le_rfl
  | succ d ih =>
    intro t ht he
    have hmid : (x (t + d)).top = (x t).top :=
      run_top_const hpr hle (by omega) (by omega : t + d ≤ t + (d + 1)) ht he
    have h1 := ih t (by omega) hmid.symm
    have h2 := topk_wt_le hpr c (hle (t + d) (by omega)) (hmid.trans he)
    exact h1.trans h2

end run

/-! ### Sets of bounded size -/

/-- the subsets of `V` with at most `k` elements -/
def subK (V : Type*) [Fintype V] (k : ℕ) : Finset (Finset V) :=
  (Finset.range (k + 1)).biUnion (fun j => Finset.powersetCard j Finset.univ)

theorem mem_subK [Fintype V] {k : ℕ} {M : Finset V} : M ∈ subK V k ↔ M.card ≤ k := by
  unfold subK
  rw [Finset.mem_biUnion]
  constructor
  · rintro ⟨j, hj, hM⟩
    rw [Finset.mem_powersetCard] at hM
    rw [Finset.mem_range] at hj
    omega
  · intro h
    exact ⟨M.card, Finset.mem_range.mpr (by omega),
      Finset.mem_powersetCard.mpr ⟨Finset.subset_univ _, rfl⟩⟩

theorem card_subK_le [Fintype V] (k : ℕ) :
    (subK V k).card ≤ ∑ j ∈ Finset.range (k + 1), (Fintype.card V).choose j := by
  unfold subK
  refine Finset.card_biUnion_le.trans (le_of_eq (Finset.sum_congr rfl (fun j _ => ?_)))
  rw [Finset.card_powersetCard, Finset.card_univ]

/-! ### The count -/

variable [Fintype V]

/-- **DEPTH-COUNT3, corrected (R234 D1).** -/
theorem depth_count : DepthCountStatement V := by
  intro pr hpr x T c hle hlen
  -- the two kinds of shallow change
  let FA : Finset ℕ := (Finset.range T).filter (fun t => (x t).top = (x (t + 1)).top ∧
    (x t).set ≠ (x (t + 1)).set ∧ depth pr (x t) (x (t + 1)) ≤ c)
  let FB : Finset ℕ := (Finset.range T).filter (fun t => (x t).top = (x (t + 1)).top ∧
    (x t).set = (x (t + 1)).set ∧ (x t).len ≠ (x (t + 1)).len ∧ (x t).set.card ≤ c)
  have hsub : (Finset.range T).filter (fun t => x t ≠ x (t + 1) ∧
      (x t).top = (x (t + 1)).top ∧ depth pr (x t) (x (t + 1)) ≤ c) ⊆ FA ∪ FB := by
    intro t ht
    obtain ⟨htr, hne, htop, hd⟩ := Finset.mem_filter.mp ht
    rw [Finset.mem_union]
    by_cases hs : (x t).set = (x (t + 1)).set
    · right
      refine Finset.mem_filter.mpr ⟨htr, htop, hs, fun hl => hne (Val.ext htop hs hl), ?_⟩
      unfold depth at hd
      rwa [ite_eq_left hs] at hd
    · left
      exact Finset.mem_filter.mpr ⟨htr, htop, hs, hd⟩
  -- set changes of depth ≤ c
  have hA : FA.card ≤ Fintype.card V * (Sc c (Fintype.card V) - 1) := by
    obtain ⟨Mx, hMx, hMxmax⟩ := Finset.exists_max_image (subK V (c + 1)) (wt pr)
      ⟨∅, mem_subK.mpr (by simp)⟩
    have hstep : ∀ t ∈ FA, wt pr (topk pr (c + 1) (x t).set) <
        wt pr (topk pr (c + 1) (x (t + 1)).set) := by
      intro t ht
      obtain ⟨htr, htop, hs, hd⟩ := Finset.mem_filter.mp ht
      exact topk_wt_lt hpr (hle t (Finset.mem_range.mp htr)) htop hs hd
    have hcard : FA.card ≤ ((Finset.univ : Finset V) ×ˢ (subK V (c + 1)).erase Mx).card := by
      apply Finset.card_le_card_of_injOn (fun t => ((x t).top, topk pr (c + 1) (x t).set))
      · intro t ht
        have ht' := Finset.mem_coe.mp ht
        rw [Finset.mem_coe, Finset.mem_product]
        refine ⟨Finset.mem_univ _, Finset.mem_erase.mpr ⟨fun e => ?_,
          mem_subK.mpr (card_topk_le hpr _ _)⟩⟩
        have e' : topk pr (c + 1) (x t).set = Mx := e
        have h1 := hstep t ht'
        have h2 := hMxmax _ (mem_subK.mpr (card_topk_le hpr (c + 1) (x (t + 1)).set))
        rw [e'] at h1
        omega
      · -- two set changes with the same cycle node have different truncations
        have key : ∀ t t', t ∈ FA → t' ∈ FA → t < t' → (x t).top = (x t').top →
            topk pr (c + 1) (x t).set ≠ topk pr (c + 1) (x t').set := by
          intro t t' ht ht' hlt he e
          obtain ⟨htr, htop, -, -⟩ := Finset.mem_filter.mp ht
          obtain ⟨htr', -, -, -⟩ := Finset.mem_filter.mp ht'
          have h1 := hstep t ht
          have h2 := run_topk hpr hle c (t' - (t + 1)) (t + 1)
            (by have := Finset.mem_range.mp htr'; omega)
            (by
              have e' : t + 1 + (t' - (t + 1)) = t' := by omega
              rw [e', ← htop, he])
          have e' : t + 1 + (t' - (t + 1)) = t' := by omega
          rw [e', ← e] at h2
          omega
        intro t ht t' ht' e
        have ht1 := Finset.mem_coe.mp ht
        have ht1' := Finset.mem_coe.mp ht'
        dsimp only at e
        have e1 : (x t).top = (x t').top := congrArg Prod.fst e
        have e2 : topk pr (c + 1) (x t).set = topk pr (c + 1) (x t').set := congrArg Prod.snd e
        by_contra hne
        rcases Nat.lt_or_gt_of_ne hne with h | h
        · exact key t t' ht1 ht1' h e1 e2
        · exact key t' t ht1' ht1 h e1.symm e2.symm
    rw [Finset.card_product, Finset.card_univ, Finset.card_erase_of_mem hMx] at hcard
    have hS : (subK V (c + 1)).card ≤ Sc c (Fintype.card V) := card_subK_le (c + 1)
    exact hcard.trans (Nat.mul_le_mul_left _ (Nat.sub_le_sub_right hS 1))
  -- length-only changes with at most c elements in the path component
  have hB : FB.card ≤ Fintype.card V * (Fintype.card V - 1) * Sc' c (Fintype.card V) := by
    -- at such a step the length moves in the direction fixed by the parity of the cycle node
    have hdir : ∀ t ∈ FB, ((x t).len < (x (t + 1)).len ∧ ¬ Even (pr (x t).top)) ∨
        ((x (t + 1)).len < (x t).len ∧ Even (pr (x t).top)) := by
      intro t ht
      obtain ⟨htr, htop, hs, hl, -⟩ := Finset.mem_filter.mp ht
      rcases hle t (Finset.mem_range.mp htr) with hlt | e
      · rw [Val.lt_iff] at hlt
        rcases hlt with hr | ⟨-, hs' | ⟨-, h⟩⟩
        · rw [htop] at hr; exact absurd hr (lt_irrefl _)
        · rw [hs] at hs'; exact absurd hs' (setLt_irrefl _)
        · exact h
      · exact absurd (congrArg Val.len e) hl
    have hlt : ∀ t ∈ FB, Val.lt pr (x t) (x (t + 1)) := by
      intro t ht
      obtain ⟨htr, htop, hs, hl, -⟩ := Finset.mem_filter.mp ht
      rcases hle t (Finset.mem_range.mp htr) with h | e
      · exact h
      · exact absurd (congrArg Val.len e) hl
    have hcard : FB.card ≤ ((Finset.univ : Finset V) ×ˢ
        (subK V c ×ˢ Finset.range (Fintype.card V - 1))).card := by
      apply Finset.card_le_card_of_injOn (fun t => ((x t).top, (x t).set,
        if Even (pr (x t).top) then (x t).len - 1 else (x t).len))
      · intro t ht
        have ht' := Finset.mem_coe.mp ht
        obtain ⟨htr, -, -, -, hc⟩ := Finset.mem_filter.mp ht'
        have htT : t < T := Finset.mem_range.mp htr
        have hl1 := hlen t (by omega)
        have hl2 := hlen (t + 1) (by omega)
        rw [Finset.mem_coe, Finset.mem_product, Finset.mem_product]
        refine ⟨Finset.mem_univ _, mem_subK.mpr hc, Finset.mem_range.mpr ?_⟩
        show (if Even (pr (x t).top) then (x t).len - 1 else (x t).len) < Fintype.card V - 1
        rcases hdir t ht' with ⟨h1, hp⟩ | ⟨h1, hp⟩
        · rw [ite_eq_right hp]; omega
        · rw [ite_eq_left hp]; omega
      · have key : ∀ t t', t ∈ FB → t' ∈ FB → t < t' → x t ≠ x t' := by
          intro t t' ht ht' h e
          obtain ⟨htr', -, -, -, -⟩ := Finset.mem_filter.mp ht'
          have h1 := hlt t ht
          have h2 := run_le hpr hle (t + 1) t' (by omega) (by
            have := Finset.mem_range.mp htr'; omega)
          rw [← e] at h2
          exact Val.lt_irrefl _ (Val.lt_of_lt_of_le hpr h1 h2)
        intro t ht t' ht' e
        have ht1 := Finset.mem_coe.mp ht
        have ht1' := Finset.mem_coe.mp ht'
        dsimp only at e
        have e1 : (x t).top = (x t').top := congrArg Prod.fst e
        have e2 : (x t).set = (x t').set := congrArg (fun p => p.2.1) e
        have e3 : (if Even (pr (x t).top) then (x t).len - 1 else (x t).len) =
            (if Even (pr (x t').top) then (x t').len - 1 else (x t').len) :=
          congrArg (fun p => p.2.2) e
        have e4 : (x t).len = (x t').len := by
          rcases hdir t ht1 with ⟨h1, hp⟩ | ⟨h1, hp⟩
          · have hp' : ¬ Even (pr (x t').top) := by rw [← e1]; exact hp
            rw [ite_eq_right hp, ite_eq_right hp'] at e3
            exact e3
          · have hp' : Even (pr (x t').top) := by rw [← e1]; exact hp
            rw [ite_eq_left hp, ite_eq_left hp'] at e3
            rcases hdir t' ht1' with ⟨_, hq⟩ | ⟨h1', _⟩
            · exact absurd hp' hq
            · omega
        have exx : x t = x t' := Val.ext e1 e2 e4
        by_contra hne
        rcases Nat.lt_or_gt_of_ne hne with h | h
        · exact key t t' ht1 ht1' h exx
        · exact key t' t ht1' ht1 h exx.symm
    rw [Finset.card_product, Finset.card_product, Finset.card_univ, Finset.card_range] at hcard
    have hS : (subK V c).card ≤ Sc' c (Fintype.card V) := card_subK_le c
    calc FB.card ≤ Fintype.card V * ((subK V c).card * (Fintype.card V - 1)) := hcard
      _ ≤ Fintype.card V * (Sc' c (Fintype.card V) * (Fintype.card V - 1)) :=
          Nat.mul_le_mul_left _ (Nat.mul_le_mul_right _ hS)
      _ = Fintype.card V * (Fintype.card V - 1) * Sc' c (Fintype.card V) := by ring
  calc _ ≤ (FA ∪ FB).card := Finset.card_le_card hsub
    _ ≤ FA.card + FB.card := Finset.card_union_le _ _
    _ ≤ _ := Nat.add_le_add hA hB

/-! ### Lengths of play values -/

omit [Fintype V] in
theorem SPath.card_eq {edge : V → V → Prop} {Ch : Finset V} {ℓ v : V} {S : Finset V} {x : Val V}
    {c : ℕ} (h : SPath pr edge Ch ℓ v S x c) : S.card = x.len + 1 := by
  induction h with
  | nil => simp
  | cons _ hvS _ ih => rw [Finset.card_insert_of_notMem hvS, ih]; rfl

/-- The length component of a play value is below the number of vertices. -/
theorem plen_lt_card : PlenLtStatement V := by
  intro pr hpr s v
  have hσ : ∀ u, Edge (fun w => ({s w} : Finset V)) (∅ : Finset V) s u (s u) :=
    fun u => Or.inr ⟨Finset.notMem_empty u, rfl⟩
  obtain ⟨S, c, hP, -⟩ := play_spath hpr hσ (plen pr s v) v rfl
  have h1 := hP.card_eq
  have h2 : S.card ≤ Fintype.card V := Finset.card_le_univ S
  have h3 : (val pr s v).len = plen pr s v := rfl
  omega

/-- DEPTH-COUNT3 for the values of one vertex along a run of states: the hypothesis on lengths
is `plen_lt_card`. -/
theorem depth_count_val (pr : V → ℕ) (hpr : Function.Injective pr) (s : ℕ → V → V) (v : V)
    (T c : ℕ) (hM : ∀ t, t < T → Val.le pr (val pr (s t) v) (val pr (s (t + 1)) v)) :
    ((Finset.range T).filter (fun t => val pr (s t) v ≠ val pr (s (t + 1)) v ∧
        lam pr (s t) v = lam pr (s (t + 1)) v ∧
        depth pr (val pr (s t) v) (val pr (s (t + 1)) v) ≤ c)).card ≤
      Fintype.card V * (Sc c (Fintype.card V) - 1) +
        Fintype.card V * (Fintype.card V - 1) * Sc' c (Fintype.card V) :=
  depth_count pr hpr (fun t => val pr (s t) v) T c hM (fun t _ => plen_lt_card pr hpr (s t) v)

end

end PG
