# N5-A2STAR (box 13): NEED-β case (A2*) closed, so Corollary NEED-β holds in every case
L-SI successor 8 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~17:35Z (date -u). Lane write-up, unrefereed, not a packet.
Item (3)'s fallback in the Lead's box-13 GO (15:59Z): "If that stalls, A2*". The rise question stalls at CONJECTURE INTO
(docs/si/N5-RISE-box13.md).
- Labels: PROVED (L-SI succ. 8, unrefereed); CONJECTURE; DATA.
- Source: docs/si/N5-LV3-box12.md (sha1 20ba05d7, FROZEN; L-SI succ. 7), §3 Corollary NEED-β, OPEN case (A2*). Notation and facts (F-a),
  (F-b), (F-c), the strategy σ″, ANTI-Ξ, m_K, K′, m′ and λ are as there. Nothing in that file is edited.
- Consequence: Corollary NEED-β is PROVED in all cases (B, A1, A2′, A2″: L-SI succ. 7; A2*: here). "THR ⇒ M ≥ 0" itself stays a
  CONJECTURE. This only removes the one exception in NEED-β's reading (N5-LV3 §3 "Reading", §4 (iii)).
- Not a running-time bound. G-N5-TIME stays OPEN.

## 1. Case (A2*) (PROVED, L-SI succ. 8)
Setting (LV+), and suppose 𝒫 (the σ*-play from x0 in G_τ) uses no (β) gate. In case (A2*), K′ contains o, its top m′ lies on the part of
K′ after o, and every vertex of λ ∪ {o} ranks below m′. This is impossible.
Proof.
- Step 1: m′ is odd.
  - U(t) = (m′, ∅, ℓ_t), with ℓ_t the number of steps from t to m′ along K′. Every vertex of K′ ranks at most m′.
  - U(x0) = (m′, ∅, ℓ_{x0}). The play from x0 meets m′ only after λ, o and t: m′ lies after o, and λ ∪ {o} does not contain it.
    - Its vertices before m′ are λ, o and K′'s vertices from t to m′, and all of them rank below m′. So the path set is ∅.
    - ℓ_{x0} = |λ| + 1 + ℓ_t > ℓ_t (|λ| ≥ 1, as x0 ∈ λ).
  - (F-a) gives U(x0) ⊵ U(t). With equal cycle nodes and equal (empty) path sets, the order is by length. The longer value is ⊵ only if
    the cycle node is odd (SPEC S1). So m′ is odd.
- Step 2: c = m′, or c is odd with rank c > rank m′.
  - F1 gives U(t) ⊵ W(t) = (c, P(W t), ·).
  - If m′ ≠ c, this forces rew(m′) > rew(c). With m′ odd, rew(m′) = −pp(m′) < 0. So rew(c) < −pp(m′), which forces c odd and
    pp(c) > pp(m′), i.e. rank c > rank m′.
- Step 3: contradiction with σ″.
  - σ″ (σ* on λ's Even vertices, σ_k elsewhere) is the strategy of N5-LV3 §3 (A1). It uses on λ only σ*-edges, which by the assumption
    are non-gates or (α) gates. In G_σ̄ its play from x0 is the cycle K = λ ∪ {o}, with top m_K.
  - ANTI-Ξ gives (m_K, ∅, ·) ⊴ Ξ(x0) = (c, ·, ·), so rew(m_K) ≤ rew(c), as in (A2′) / (A2″).
  - rank m_K < rank m′ ≤ rank c, so m_K ≠ c. By Step 2, c is odd.
  - So rew(m_K) ≥ −pp(m_K) > −pp(c) = rew(c). This contradicts rew(m_K) ≤ rew(c). □
- Remark. Steps 1-2 use only (F-a) and F1; the "no (β) gate" assumption enters only in Step 3, through σ″.
  - Successor 7's unchecked idea (ANTI-W on K′, "a blocked edge on K′ unless m′ = c") is true but not needed.
  - The parity of m′ already decides the case.

## 2. Corollary NEED-β, complete (PROVED: L-SI succ. 7 for (B), (A1), (A2′), (A2″); L-SI succ. 8 for (A2*))
In setting (LV+) (an in-scope THR S4c fallback with r ≥ 0 and M = −1), Even's optimal G_τ-play from the threat x0 uses a (β) gate
(y, σ*(y)).
- The case split of N5-LV3 §3 is exhaustive:
  - (B) 𝒫 avoids o;
  - (A1) 𝒫 visits o, and its cycle avoids o;
  - otherwise K′ contains o, and its top m′ either lies in λ ∪ {o} (A2′), or lies after o. If it lies after o, either some vertex of
    λ ∪ {o} ranks above m′ (A2″: rank m_K > rank m′), or none does (A2*).
- Reading (updated). A counterexample to "THR ⇒ M ≥ 0" (§4 of N5-LV3) has no (A2*) branch any more. Its threat's best reply to τ crosses
  R → F along a (β) gate, and so does every (β) exit's own reply (N5-LV3 §3 Reading).

## 3. DATA (DATA, not proof; experiments/si/lv13/a2star.py, log experiments/si/lv13/logs/a2star_named.txt)
- Corpus: NAMED (experiments/si/lv/named.lst, 102 files), with the run states and 2 perturbed start pairs per state.
  - 519 in-scope THR fallbacks, all with r ≥ 0 (setting (LV+) itself occurs 0 times, as in N5-LV3 §5).
  - 82 U-plays from x0 have a cycle through o.
  - The A2* shape (top after o, above λ ∪ {o}) occurs 0 times.
- So Steps 1-3 are vacuous in data and rest on the proof. The script checks Steps 1-3 and the data form of Step 3 at every A2* shape it
  finds.
