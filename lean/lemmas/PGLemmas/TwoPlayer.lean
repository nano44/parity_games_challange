/-
Premise F1 on two-player games (`F1Statement`, `PGLemmas/Statements6.lean`): RESULTS R15 (a)
Lemma A = VJ00 Lemma 5.7, in Friedmann's form (optimal counterstrategy = pointwise minimum over
Odd's strategies).

* `underProgAt_of_opt`  if switching the vertex `u` to `w` does not lower the value of `u`, the
                        edge `u → w` is under-progressive (VJ00 Prop. 5.1 at Odd's vertices).
                        Proof: otherwise the switch lowers the successor's value, so by the dual
                        of (M) (`val_mono_dual`) no value rises, hence the value of `u` is
                        unchanged; (P1) and F4′ in strict form (or, at a cycle node, the empty
                        path component of its successor) then give a contradiction.
* `f1`                  every Even edge of `σ'` is under-progressive (an improvement), every Odd
                        edge is (optimality of `τ` against single switches), so VJ00 Lemma 5.5
                        (`val_le_of_underProg`) applies.
* `brseg_opt`, `tcyc_opt`  BR-SEG and T-CYC with «σ̄_t optimal» in place of F1.
-/
import PGLemmas.Dual
import PGLemmas.Corollaries
import PGLemmas.TCyc
import PGLemmas.Statements6

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V] {pr : V → ℕ}

/-- If switching `u` to `w` does not lower the value of `u`, the edge `u → w` is
under-progressive. -/
theorem underProgAt_of_opt (hpr : Function.Injective pr) {s : V → V} {u w : V}
    (hopt : Val.le pr (val pr s u) (val pr (Function.update s u w) u)) :
    UnderProgAt pr s u w := by
  have hs₂u : Function.update s u w u = w := Function.update_self u w s
  -- if the switch lowers the successor's value, no value rises, so the value of `u` is unchanged
  have hdual : Val.lt pr (val pr s w) (val pr s (s u)) →
      ∀ v, Val.le pr (val pr (Function.update s u w) v) (val pr s v) := by
    intro hlt
    apply val_mono_dual hpr s (Function.update s u w)
    intro v
    by_cases hv : v = u
    · right; rw [hv, hs₂u]; exact hlt
    · left; exact Function.update_of_ne hv w s
  have heq : Val.lt pr (val pr s w) (val pr s (s u)) →
      val pr (Function.update s u w) u = val pr s u :=
    fun hlt => Val.le_antisymm hpr (hdual hlt u) hopt
  by_cases htop : lam pr s u = u
  · -- `u` is a cycle node
    refine ⟨?_, fun h => absurd htop h, ?_⟩
    · by_contra hnot
      have hrew : rew pr (lam pr s w) < rew pr (lam pr s u) := not_le.mp hnot
      have hlt : Val.lt pr (val pr s w) (val pr s (s u)) := by
        apply Val.lt_of_rew_lt
        show rew pr (lam pr s w) < rew pr (lam pr s (s u))
        rw [lam_succ hpr]
        exact hrew
      have hl₂ : lam pr (Function.update s u w) u = u := (congrArg Val.top (heq hlt)).trans htop
      have hw₂ : lam pr (Function.update s u w) w = u := by
        have := lam_succ (s := Function.update s u w) hpr u
        rw [hs₂u] at this
        rw [this, hl₂]
      rw [htop] at hrew
      rcases Val.top_of_le (hdual hlt w) with e' | h'
      · have e'' : lam pr (Function.update s u w) w = lam pr s w := e'
        rw [hw₂] at e''
        rw [← e''] at hrew
        exact lt_irrefl _ hrew
      · have h'' : rew pr (lam pr (Function.update s u w) w) < rew pr (lam pr s w) := h'
        rw [hw₂] at h''
        exact lt_irrefl _ (h''.trans hrew)
    · intro _ hw
      by_contra hnot
      have hneg : wt pr (val pr s w).set < 0 := not_le.mp hnot
      have hlt : Val.lt pr (val pr s w) (val pr s (s u)) := by
        rw [Val.lt_iff]
        refine Or.inr ⟨?_, Or.inl ?_⟩
        · show lam pr s w = lam pr s (s u)
          rw [lam_succ hpr, htop, hw]
        · rw [setLt_iff_wt_lt hpr, pset_succ_of_lam_eq hpr htop, wt_empty]
          exact hneg
      have hl₂ : lam pr (Function.update s u w) u = u := (congrArg Val.top (heq hlt)).trans htop
      have hset : (val pr (Function.update s u w) w).set = ∅ := by
        have := pset_succ_of_lam_eq (s := Function.update s u w) hpr hl₂
        rwa [hs₂u] at this
      have hw₂ : lam pr (Function.update s u w) w = u := by
        have := lam_succ (s := Function.update s u w) hpr u
        rw [hs₂u] at this
        rw [this, hl₂]
      have htops : (val pr (Function.update s u w) w).top = (val pr s w).top := hw₂.trans hw.symm
      have hlex := (Val.le_iff_lex hpr htops).mp (hdual hlt w)
      rw [hset, wt_empty] at hlex
      unfold LexLe at hlex
      omega
  · -- `u` is not a cycle node: the end `w` is worth at least the current successor
    apply underProgAt_of_le hpr
    by_contra hnot
    have hlt : Val.lt pr (val pr s w) (val pr s (s u)) := Val.lt_of_not_le hpr hnot
    have e := heq hlt
    have hl₂ : lam pr (Function.update s u w) u ≠ u := by
      intro h
      exact htop ((congrArg Val.top e).symm.trans h)
    have h1 : val pr (Function.update s u w) u = ext pr u (val pr (Function.update s u w) w) := by
      have := val_step hpr hl₂
      rwa [hs₂u] at this
    have hn1 : u ∉ (val pr (Function.update s u w) w).set := by
      have := notMem_pset_succ hpr hl₂
      rwa [hs₂u] at this
    have h2 : val pr s u = ext pr u (val pr s (s u)) := val_step hpr htop
    have hn2 : u ∉ (val pr s (s u)).set := notMem_pset_succ hpr htop
    have hlt' : Val.lt pr (val pr (Function.update s u w) w) (val pr s (s u)) :=
      Val.lt_of_le_of_lt hpr (hdual hlt w) hlt
    have := ext_lt hn1 hn2 hlt'
    rw [← h1, ← h2, e] at this
    exact Val.lt_irrefl _ this

/-- **F1 = RESULTS R15 (a) Lemma A** (VJ00 Lemma 5.7). -/
theorem f1 : F1Statement V := by
  intro pr hpr E V0 σ τ σ' τ' hopt hτ' himp v
  apply val_le_of_underProg hpr
  intro u
  by_cases hu : u ∈ V0
  · -- an Even edge: an improvement or the old edge
    apply underProgAt_of_le hpr
    have e1 : pair V0 σ τ u = σ u := by unfold pair; rw [ite_eq_left hu]
    have e2 : pair V0 σ' τ' u = σ' u := by unfold pair; rw [ite_eq_left hu]
    rw [e1, e2]
    rcases himp u hu with e | hlt
    · rw [e]; exact Val.le_refl _
    · exact Val.le_of_lt hlt
  · -- an Odd edge: `τ` is optimal against the single switch
    have e2 : pair V0 σ' τ' u = τ' u := by unfold pair; rw [ite_eq_right hu]
    rw [e2]
    apply underProgAt_of_opt hpr
    have hupd : Function.update (pair V0 σ τ) u (τ' u) = pair V0 σ (Function.update τ u (τ' u)) := by
      funext x
      by_cases hx : x = u
      · subst hx
        rw [Function.update_self]
        unfold pair
        rw [ite_eq_right hu, Function.update_self]
      · rw [Function.update_of_ne hx]
        unfold pair
        by_cases hx0 : x ∈ V0
        · rw [ite_eq_left hx0, ite_eq_left hx0]
        · rw [ite_eq_right hx0, ite_eq_right hx0, Function.update_of_ne hx]
    rw [hupd]
    apply hopt.2
    intro x hx
    by_cases hxu : x = u
    · subst hxu
      rw [Function.update_self]
      exact hτ' x hu
    · rw [Function.update_of_ne hxu]
      exact hopt.1 x hx

/-- F1 at one Howard step of a two-player run. -/
theorem f1_howard (hpr : Function.Injective pr) {E : V → Finset V} {V0 Mov : Finset V}
    {σ τ σ' τ' : V → V} (hopt : OptCounter pr E V0 σ τ)
    (hτ' : ∀ u, u ∉ V0 → τ' u ∈ E u) (hfrozen : ∀ v ∈ V0, v ∉ Mov → σ' v = σ v)
    (hlegal : ∀ x ∈ Mov, σ x ∈ E x)
    (hhow : ∀ x ∈ Mov, HowardAt pr E (pair V0 σ τ) (pair V0 σ' τ') x) (v : V) :
    Val.le pr (val pr (pair V0 σ τ) v) (val pr (pair V0 σ' τ') v) := by
  apply f1 pr hpr E V0 σ τ σ' τ' hopt hτ'
  intro x hx
  by_cases hm : x ∈ Mov
  · obtain ⟨-, hbest, hkeep⟩ := hhow x hm
    have e1 : pair V0 σ τ x = σ x := by unfold pair; rw [ite_eq_left hx]
    have e2 : pair V0 σ' τ' x = σ' x := by unfold pair; rw [ite_eq_left hx]
    rw [e1, e2] at hkeep
    rw [e2] at hbest
    by_cases hsame : σ' x = σ x
    · exact Or.inl hsame
    · right
      have hnot : ∃ w ∈ E x, ¬ Val.le pr (val pr (pair V0 σ τ) w) (val pr (pair V0 σ τ) (σ x)) := by
        by_contra h
        exact hsame (hkeep ⟨hlegal x hm, fun w hw => by
          by_contra hw'
          exact h ⟨w, hw, hw'⟩⟩)
      obtain ⟨w, hw, hwnot⟩ := hnot
      exact Val.lt_of_lt_of_le hpr (Val.lt_of_not_le hpr hwnot) (hbest w hw)
  · exact Or.inl (hfrozen x hx hm)

/-- **BR-SEG with no premise F1.** -/
theorem brseg_opt : BrSegOptStatement V := by
  intro pr hpr E V0 Mov hsub σ τ a j hfrozen hlegal hhow hopt hlam hbar hchg
  refine brseg pr hpr E V0 Mov hsub σ τ a j hfrozen hhow ?_ hlam hbar hchg
  intro t hat htj v
  -- the movers follow the edges at every state of the window
  have hleg : ∀ d, a + d ≤ a + j → ∀ x ∈ Mov, σ (a + d) x ∈ E x := by
    intro d
    induction d with
    | zero => intro _ x hx; exact hlegal x hx
    | succ d _ =>
      intro hd x hx
      obtain ⟨hE, -, -⟩ := hhow (a + d) (by omega) (by omega) x hx
      have e : nxt V0 σ τ (a + d + 1) x = σ (a + d + 1) x := by
        unfold nxt pair; rw [ite_eq_left (hsub hx)]
      rw [e] at hE
      exact hE
  have hlegt : ∀ x ∈ Mov, σ t x ∈ E x := by
    have := hleg (t - a) (by omega)
    have e : a + (t - a) = t := by omega
    rwa [e] at this
  exact f1_howard hpr (hopt t hat (by omega)) (hopt (t + 1) (by omega) (by omega)).1
    (fun x hx hm => by
      rw [hfrozen (t + 1) (by omega) (by omega) x hx hm, hfrozen t hat (by omega) x hx hm])
    hlegt (hhow t hat htj) v

/-- **T-CYC with no premise F1.** -/
theorem tcyc_opt : TCycOptStatement V := by
  intro pr hpr E V0 Mov hsub σ τ T hfrozen hlegal hhow hopt hchg
  refine tcyc pr hpr E V0 Mov hsub σ τ T hfrozen hhow ?_ hchg
  intro t ht v
  have hleg : ∀ d, d ≤ T → ∀ x ∈ Mov, σ d x ∈ E x := by
    intro d
    induction d with
    | zero => intro _ x hx; exact hlegal x hx
    | succ d _ =>
      intro hd x hx
      obtain ⟨hE, -, -⟩ := hhow d (by omega) x hx
      have e : nxt V0 σ τ (d + 1) x = σ (d + 1) x := by
        unfold nxt pair; rw [ite_eq_left (hsub hx)]
      rw [e] at hE
      exact hE
  exact f1_howard hpr (hopt t (by omega)) (hopt (t + 1) (by omega)).1
    (fun x hx hm => by
      rw [hfrozen (t + 1) (by omega) x hx hm, hfrozen t (by omega) x hx hm])
    (hleg t (by omega)) (hhow t ht) v

end

end PG
