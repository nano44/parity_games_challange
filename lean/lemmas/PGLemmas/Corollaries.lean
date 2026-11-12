/-
Corollaries of `lam_gap_sharp` (`PGLemmas/LamGap.lean`):
* `lam_gap_oneplayer`  LAM-GAP / SHARP in box 101 §2's one-player wording;
* `brseg`              RESULTS R118 (d), Theorem BR-SEG (no genome is used);
* `brsegG`             RESULTS R118 (i) clause (a), Theorem BR-SEG-G; and `brsegG_noH0`: the same
                       bound when H0 is weakened to «every step changes σ».
-/
import PGLemmas.LamGap

namespace PG

open Classical

noncomputable section

variable {V : Type*} [Fintype V]

/-- LAM-GAP, SHARP form, in the one-player wording of box 101 §2. -/
theorem lam_gap_oneplayer : LamGapOnePlayerStatement V := by
  intro pr hpr E Ch s a b hab hone hedge hhow hmono hlam hmoves
  refine lam_gap_sharp pr hpr E Ch s a b ⟨hab, ?_, hhow, hmono, hlam, hmoves⟩
  intro t hat htb v hv
  obtain ⟨u, hu⟩ := hone v hv
  have h1 := hedge t hat htb v
  have h2 := hedge a le_rfl hab v
  rw [hu, Finset.mem_singleton] at h1 h2
  rw [h1, h2]

/-- Once a Howard step changes nothing, no later step of the window changes anything: every
vertex of `Ch` keeps a successor that is still best, and the others are fixed. -/
theorem stationary {pr : V → ℕ} {E : V → Finset V} {Ch : Finset V} {s : ℕ → V → V} {a b : ℕ}
    (hfixed : ∀ t, a ≤ t → t ≤ b → ∀ v, v ∉ Ch → s t v = s a v)
    (hhow : ∀ t, a ≤ t → t < b → ∀ v ∈ Ch, HowardAt pr E (s t) (s (t + 1)) v)
    {t : ℕ} (hat : a ≤ t) (hstop : s (t + 1) = s t) :
    ∀ d, t + d < b → s (t + d + 1) = s (t + d) := by
  intro d
  induction d with
  | zero => intro _; exact hstop
  | succ d ih =>
    intro hd
    have ih' := ih (by omega)
    funext v
    by_cases hv : v ∈ Ch
    · obtain ⟨hE, hbest, -⟩ := hhow (t + d) (by omega) (by omega) v hv
      obtain ⟨-, -, hkeep⟩ := hhow (t + d + 1) (by omega) (by omega) v hv
      rw [← ih'] at hbest
      exact hkeep ⟨hE, hbest⟩
    · rw [hfixed (t + (d + 1) + 1) (by omega) (by omega) v hv,
        hfixed (t + (d + 1)) (by omega) (by omega) v hv]

/-- RESULTS R118 (d), Theorem BR-SEG. -/
theorem brseg : BrSegStatement V := by
  intro pr hpr E V0 Mov hsub σ τ a j hfrozen hhow hF1 hlam hbar hchg
  have hfixed : ∀ t, a ≤ t → t ≤ a + j + 1 → ∀ v, v ∉ Mov →
      nxt V0 σ τ t v = nxt V0 σ τ a v := by
    intro t hat htb v hv
    unfold nxt pair
    by_cases hv0 : v ∈ V0
    · simp only [hv0, ite_true]
      exact hfrozen t hat htb v hv0 hv
    · simp only [hv0, ite_false]
      exact hbar t hat htb v hv0
  have hhow' : ∀ t, a ≤ t → t < a + j + 1 → ∀ v ∈ Mov,
      HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) v :=
    fun t hat htb v hv => hhow t hat (by omega) v hv
  have W : Window pr E Mov (nxt V0 σ τ) a (a + j + 1) := by
    refine ⟨by omega, hfixed, hhow', fun t hat htb v => hF1 t hat (by omega) v, hlam, ?_⟩
    -- every step changes the state: otherwise the last step would not change `σ`
    intro t hat htb hstop
    have hlast := stationary hfixed hhow' hat hstop (a + j - t) (by omega)
    have e : t + (a + j - t) = a + j := by omega
    rw [e] at hlast
    obtain ⟨x, hx0, hx⟩ := hchg
    apply hx
    have := congrFun hlast x
    unfold nxt pair at this
    simpa only [hx0, ite_true] using this
  have := lam_gap_sharp pr hpr E Mov (nxt V0 σ τ) a (a + j + 1) W
  omega

/-- BR-SEG-G clause (a) with H0 weakened to «every step changes σ at some Even vertex». -/
theorem brsegG_noH0 (pr : V → ℕ) (hpr : Function.Injective pr) (E : V → Finset V)
    (V0 : Finset V) (σ τ : ℕ → V → V) (a r : ℕ)
    (hhow : ∀ t, a ≤ t → t < a + r → ∀ x ∈ V0,
      HowardAt pr E (nxt V0 σ τ t) (nxt V0 σ τ (t + 1)) x)
    (hF1 : ∀ t, a ≤ t → t < a + r → ∀ v,
      Val.le pr (val pr (nxt V0 σ τ t) v) (val pr (nxt V0 σ τ (t + 1)) v))
    (hlam : ∀ t, a ≤ t → t ≤ a + r → ∀ v, lam pr (nxt V0 σ τ t) v = lam pr (nxt V0 σ τ a) v)
    (hbar : ∀ t, a ≤ t → t ≤ a + r → ∀ v, v ∉ V0 → τ t v = τ a v)
    (hchg : ∀ t, a ≤ t → t < a + r → ∃ x ∈ V0, σ (t + 1) x ≠ σ t x) :
    r ≤ V0.card := by
  have W : Window pr E V0 (nxt V0 σ τ) a (a + r) := by
    refine ⟨by omega, ?_, hhow, hF1, hlam, ?_⟩
    · intro t hat htb v hv
      unfold nxt pair
      simp only [hv, ite_false]
      exact hbar t hat htb v hv
    · intro t hat htb hstop
      obtain ⟨x, hx0, hx⟩ := hchg t hat htb
      apply hx
      have := congrFun hstop x
      unfold nxt pair at this
      simpa only [hx0, ite_true] using this
  have := lam_gap_sharp pr hpr E V0 (nxt V0 σ τ) a (a + r) W
  omega

/-- RESULTS R118 (i), Theorem BR-SEG-G, clause (a), under H0 as stated there. -/
theorem brsegG : BrSegGStatement V := by
  intro pr hpr E V0 σ τ a r hhow hF1 hlam hbar hH0
  refine brsegG_noH0 pr hpr E V0 σ τ a r hhow hF1 hlam hbar ?_
  intro t hat htb
  obtain ⟨x, hx0, hx, -, -⟩ := hH0 t hat htb
  exact ⟨x, hx0, hx⟩

end

end PG
