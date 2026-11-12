/-
First facts about Γ3(G) (PGLemmas/Gamma3.lean), read off the definitions:
* `card_vertex`, `card_vertex3`   card Vertex = N + 3M + 6, card Vertex3 = N + 7M + 10 (explicit
                                  equivalences with sums of `Fin N`, the options and `Unit`);
* `idx_lt`, `idx3_lt`, `idx3_injective`   under `WF` the index of Γ3 is a bijection onto 0..n − 1;
* `gamma3_card : G.Gamma3CardStatement`, `gamma3_old : G.Gamma3OldStatement` (Γ inside Γ3).
-/
import PGLemmas.Gamma3Statement
import PGLemmas.GenomeBasic
import Mathlib.Tactic

namespace PG

namespace Genome

variable {G : Genome}

/-- Γ's vertices as a sum: movers, three copies of the options (gates, β, e), six single vertices. -/
def vertexEquiv (G : Genome) :
    G.Vertex ≃ Fin G.N ⊕ G.Opt ⊕ G.Opt ⊕ G.Opt ⊕ Unit ⊕ Unit ⊕ Unit ⊕ Unit ⊕ Unit ⊕ Unit where
  toFun
    | .mover x => .inl x
    | .gate o => .inr (.inl o)
    | .beta o => .inr (.inr (.inl o))
    | .eface o => .inr (.inr (.inr (.inl o)))
    | .cX => .inr (.inr (.inr (.inr (.inl ()))))
    | .cW => .inr (.inr (.inr (.inr (.inr (.inl ())))))
    | .K0 => .inr (.inr (.inr (.inr (.inr (.inr (.inl ()))))))
    | .K1 => .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inl ())))))))
    | .K2 => .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr (.inl ()))))))))
    | .K3 => .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr ()))))))))
  invFun
    | .inl x => .mover x
    | .inr (.inl o) => .gate o
    | .inr (.inr (.inl o)) => .beta o
    | .inr (.inr (.inr (.inl o))) => .eface o
    | .inr (.inr (.inr (.inr (.inl ())))) => .cX
    | .inr (.inr (.inr (.inr (.inr (.inl ()))))) => .cW
    | .inr (.inr (.inr (.inr (.inr (.inr (.inl ())))))) => .K0
    | .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inl ()))))))) => .K1
    | .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr (.inl ())))))))) => .K2
    | .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr ())))))))) => .K3
  left_inv v := by cases v <;> rfl
  right_inv x := by
    rcases x with x | o | o | o | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ <;> rfl

/-- Γ3's vertices as a sum: Γ's, four core pads, four copies of the options (pe, pβ, pb, m). -/
def vertex3Equiv (G : Genome) :
    G.Vertex3 ≃ G.Vertex ⊕ Unit ⊕ Unit ⊕ Unit ⊕ Unit ⊕ G.Opt ⊕ G.Opt ⊕ G.Opt ⊕ G.Opt where
  toFun
    | .old v => .inl v
    | .pA => .inr (.inl ())
    | .pS => .inr (.inr (.inl ()))
    | .pQ => .inr (.inr (.inr (.inl ())))
    | .pR => .inr (.inr (.inr (.inr (.inl ()))))
    | .pe o => .inr (.inr (.inr (.inr (.inr (.inl o)))))
    | .pbeta o => .inr (.inr (.inr (.inr (.inr (.inr (.inl o))))))
    | .pb o => .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inl o)))))))
    | .m o => .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr o)))))))
  invFun
    | .inl v => .old v
    | .inr (.inl ()) => .pA
    | .inr (.inr (.inl ())) => .pS
    | .inr (.inr (.inr (.inl ()))) => .pQ
    | .inr (.inr (.inr (.inr (.inl ())))) => .pR
    | .inr (.inr (.inr (.inr (.inr (.inl o))))) => .pe o
    | .inr (.inr (.inr (.inr (.inr (.inr (.inl o)))))) => .pbeta o
    | .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inl o))))))) => .pb o
    | .inr (.inr (.inr (.inr (.inr (.inr (.inr (.inr o))))))) => .m o
  left_inv v := by cases v <;> rfl
  right_inv x := by
    rcases x with v | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | o | o | o | o <;> rfl

theorem card_vertex : Fintype.card G.Vertex = G.N + 3 * G.M + 6 := by
  rw [Fintype.card_congr G.vertexEquiv]
  simp only [Fintype.card_sum, Fintype.card_fin, Fintype.card_unit]
  unfold M
  ring

theorem card_vertex3 : Fintype.card G.Vertex3 = G.N + 7 * G.M + 10 := by
  rw [Fintype.card_congr G.vertex3Equiv]
  simp only [Fintype.card_sum, Fintype.card_unit, card_vertex]
  unfold M
  ring

theorem idx_lt (h : G.WF) (v : G.Vertex) : G.idx v < G.n0 := by
  unfold n0
  rcases v with x | o | o | o | _ | _ | _ | _ | _ | _ <;> simp only [idx] <;>
  (try have := h.gate_lt o) <;> (try have := pos_lt o) <;> (try have := x.isLt) <;> omega

theorem idx3_lt (h : G.WF) (v : G.Vertex3) : G.idx3 v < G.N + 7 * G.M + 10 := by
  have hn : G.n0 = G.N + 3 * G.M + 6 := rfl
  rcases v with v | _ | _ | _ | _ | o | o | o | o <;> simp only [idx3] <;>
  (try have := idx_lt h v) <;> (try have := h.gate_lt o) <;> (try have := pos_lt o) <;> omega

theorem idx3_injective (h : G.WF) : Function.Injective G.idx3 := by
  intro a b e
  rcases a with v | _ | _ | _ | _ | o | o | o | o <;>
  rcases b with v' | _ | _ | _ | _ | o' | o' | o' | o' <;>
  simp only [idx3] at e <;>
  (try have i1 := idx_lt h v) <;> (try have i2 := idx_lt h v') <;>
  (try have g1 := h.gate_lt o) <;> (try have g2 := h.gate_lt o') <;>
  (try have p1 := pos_lt o) <;> (try have p2 := pos_lt o') <;>
  first
  | rfl
  | (exfalso; omega)
  | (have e' := idx_injective h e; subst e'; rfl)
  | (have e' := h.gate_inj (by omega : G.gate o = G.gate o'); subst e'; rfl)
  | (have e' := pos_inj (by omega : G.pos o = G.pos o'); subst e'; rfl)

/-- **The vertex count** (R117: «n = N + 7M + 10»). -/
theorem gamma3_card : G.Gamma3CardStatement :=
  ⟨card_vertex3, fun h => ⟨idx3_injective h, idx3_lt h⟩⟩

theorem prio3_r104_old (v : G.Vertex) : G.prio3 G.r104 (.old v) = G.prio v := by
  cases v <;> rfl

/-- **Γ inside Γ3** ([REACH] §3). -/
theorem gamma3_old : G.Gamma3OldStatement := by
  refine ⟨fun v => ⟨rfl, prio3_r104_old v, rfl⟩, ?_, ?_⟩
  · intro a b
    cases a with
    | mover x =>
      constructor
      · intro hb
        simp only [E, Finset.mem_image, Finset.mem_univ, true_and] at hb
        obtain ⟨k, rfl⟩ := hb
        exact Or.inr ⟨.m ⟨x, k⟩, rfl, by simp [E3], rfl⟩
      · rintro (hb | ⟨p, -, hp, hpb⟩)
        · simp [E3] at hb
        · simp only [E3, Finset.mem_image, Finset.mem_univ, true_and] at hp
          obtain ⟨k, rfl⟩ := hp
          simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb
          subst hpb
          simp [E]
    | gate o =>
      constructor
      · intro hb
        simp only [E, Finset.mem_insert, Finset.mem_singleton] at hb
        rcases hb with rfl | rfl
        · exact Or.inr ⟨.pe o, rfl, by simp [E3], rfl⟩
        · exact Or.inr ⟨.pbeta o, rfl, by simp [E3], rfl⟩
      · rintro (hb | ⟨p, -, hp, hpb⟩)
        · simp [E3] at hb
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl <;>
          simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb <;> subst hpb <;> simp [E]
    | beta o =>
      cases hx : G.xt o with
      | none =>
        constructor
        · intro hb
          simp only [E, hx, Finset.mem_singleton] at hb
          subst hb
          exact Or.inr ⟨.pb o, rfl, by simp [E3, hx], rfl⟩
        · rintro (hb | ⟨p, -, hp, hpb⟩)
          · simp [E3, hx] at hb
          · simp only [E3, hx, Finset.mem_singleton] at hp
            subst hp
            simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb
            subst hpb
            simp [E, hx]
      | some y =>
        constructor
        · intro hb
          simp only [E, hx, Finset.mem_insert, Finset.mem_singleton] at hb
          rcases hb with rfl | rfl
          · exact Or.inl (by simp [E3, hx])
          · exact Or.inr ⟨.pb o, rfl, by simp [E3, hx], rfl⟩
        · rintro (hb | ⟨p, hpad, hp, hpb⟩)
          · simp only [E3, hx, Finset.mem_insert, Finset.mem_singleton] at hb
            rcases hb with hb | hb
            · simp only [Vertex3.old.injEq] at hb
              subst hb
              simp [E, hx]
            · cases hb
          · simp only [E3, hx, Finset.mem_insert, Finset.mem_singleton] at hp
            rcases hp with rfl | rfl
            · simp [Vertex3.isPad] at hpad
            · simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb
              subst hpb
              simp [E, hx]
    | eface o =>
      cases hw : G.wt o with
      | none =>
        constructor
        · intro hb
          simp only [E, hw, Finset.mem_singleton] at hb
          subst hb
          exact Or.inl (by simp [E3, hw])
        · rintro (hb | ⟨p, hpad, hp, -⟩)
          · simp only [E3, hw, Finset.mem_singleton, Vertex3.old.injEq] at hb
            subst hb
            simp [E, hw]
          · simp only [E3, hw, Finset.mem_singleton] at hp
            subst hp
            simp [Vertex3.isPad] at hpad
      | some y =>
        constructor
        · intro hb
          simp only [E, hw, Finset.mem_singleton] at hb
          subst hb
          exact Or.inl (by simp [E3, hw])
        · rintro (hb | ⟨p, hpad, hp, -⟩)
          · simp only [E3, hw, Finset.mem_singleton, Vertex3.old.injEq] at hb
            subst hb
            simp [E, hw]
          · simp only [E3, hw, Finset.mem_singleton] at hp
            subst hp
            simp [Vertex3.isPad] at hpad
    | cX =>
      constructor
      · intro hb
        simp only [E, Finset.mem_singleton] at hb
        subst hb
        exact Or.inl (by simp [E3])
      · rintro (hb | ⟨p, hpad, hp, -⟩)
        · simp only [E3, Finset.mem_singleton, Vertex3.old.injEq] at hb
          subst hb
          simp [E]
        · simp only [E3, Finset.mem_singleton] at hp
          subst hp
          simp [Vertex3.isPad] at hpad
    | cW =>
      constructor
      · intro hb
        simp only [E, Finset.mem_singleton] at hb
        subst hb
        exact Or.inl (by simp [E3])
      · rintro (hb | ⟨p, hpad, hp, -⟩)
        · simp only [E3, Finset.mem_singleton, Vertex3.old.injEq] at hb
          subst hb
          simp [E]
        · simp only [E3, Finset.mem_singleton] at hp
          subst hp
          simp [Vertex3.isPad] at hpad
    | K0 =>
      constructor
      · intro hb
        simp only [E, Finset.mem_insert, Finset.mem_singleton] at hb
        rcases hb with rfl | rfl
        · exact Or.inl (by simp [E3])
        · exact Or.inr ⟨.pA, rfl, by simp [E3], rfl⟩
      · rintro (hb | ⟨p, hpad, hp, hpb⟩)
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hb
          rcases hb with hb | hb
          · simp only [Vertex3.old.injEq] at hb
            subst hb
            simp [E]
          · cases hb
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl
          · simp [Vertex3.isPad] at hpad
          · simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb
            subst hpb
            simp [E]
    | K1 =>
      constructor
      · intro hb
        simp only [E, Finset.mem_insert, Finset.mem_singleton] at hb
        rcases hb with rfl | rfl
        · exact Or.inr ⟨.pQ, rfl, by simp [E3], rfl⟩
        · exact Or.inr ⟨.pS, rfl, by simp [E3], rfl⟩
      · rintro (hb | ⟨p, -, hp, hpb⟩)
        · simp [E3] at hb
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl <;>
          simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb <;> subst hpb <;> simp [E]
    | K2 =>
      constructor
      · intro hb
        simp only [E, Finset.mem_insert, Finset.mem_singleton] at hb
        rcases hb with rfl | rfl
        · exact Or.inr ⟨.pR, rfl, by simp [E3], rfl⟩
        · exact Or.inl (by simp [E3])
      · rintro (hb | ⟨p, hpad, hp, hpb⟩)
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hb
          rcases hb with hb | hb
          · cases hb
          · simp only [Vertex3.old.injEq] at hb
            subst hb
            simp [E]
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl
          · simp only [E3, Finset.singleton_inj, Vertex3.old.injEq] at hpb
            subst hpb
            simp [E]
          · simp [Vertex3.isPad] at hpad
    | K3 =>
      constructor
      · intro hb
        simp only [E, Finset.mem_insert, Finset.mem_singleton] at hb
        rcases hb with rfl | rfl
        · exact Or.inl (by simp [E3])
        · exact Or.inl (by simp [E3])
      · rintro (hb | ⟨p, hpad, hp, -⟩)
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton, Vertex3.old.injEq] at hb
          rcases hb with rfl | rfl <;> simp [E]
        · simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hp
          rcases hp with rfl | rfl <;> simp [Vertex3.isPad] at hpad
  · intro a w hw
    cases a with
    | mover x =>
      simp only [E3, Finset.mem_image, Finset.mem_univ, true_and] at hw
      obtain ⟨k, rfl⟩ := hw
      exact Or.inr ⟨rfl, _, rfl⟩
    | gate o =>
      simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact Or.inr ⟨rfl, _, rfl⟩
      · exact Or.inr ⟨rfl, _, rfl⟩
    | beta o =>
      cases hx : G.xt o with
      | none =>
        simp only [E3, hx, Finset.mem_singleton] at hw
        subst hw
        exact Or.inr ⟨rfl, _, rfl⟩
      | some y =>
        simp only [E3, hx, Finset.mem_insert, Finset.mem_singleton] at hw
        rcases hw with rfl | rfl
        · exact Or.inl ⟨_, rfl⟩
        · exact Or.inr ⟨rfl, _, rfl⟩
    | eface o =>
      cases hwt : G.wt o with
      | none =>
        simp only [E3, hwt, Finset.mem_singleton] at hw
        exact Or.inl ⟨_, hw⟩
      | some y =>
        simp only [E3, hwt, Finset.mem_singleton] at hw
        exact Or.inl ⟨_, hw⟩
    | cX =>
      simp only [E3, Finset.mem_singleton] at hw
      exact Or.inl ⟨_, hw⟩
    | cW =>
      simp only [E3, Finset.mem_singleton] at hw
      exact Or.inl ⟨_, hw⟩
    | K0 =>
      simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact Or.inl ⟨_, rfl⟩
      · exact Or.inr ⟨rfl, _, rfl⟩
    | K1 =>
      simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact Or.inr ⟨rfl, _, rfl⟩
      · exact Or.inr ⟨rfl, _, rfl⟩
    | K2 =>
      simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact Or.inr ⟨rfl, _, rfl⟩
      · exact Or.inl ⟨_, rfl⟩
    | K3 =>
      simp only [E3, Finset.mem_insert, Finset.mem_singleton] at hw
      rcases hw with rfl | rfl
      · exact Or.inl ⟨_, rfl⟩
      · exact Or.inl ⟨_, rfl⟩

end Genome

end PG
