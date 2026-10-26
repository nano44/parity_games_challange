# P-N5-DEPTH-add (box 22): CONDITIONAL companion of P-N5-DEPTH-box22. Odd choice changes at direct gates after the A-freeze are length pushes (GATE-PUSH), pure C-intervals are polynomially long (PURE-LEN), and Even's nested switches are one-way (E-ONEWAY, via MONO-REF)
L-SI successor 18 (Opus 5.5; D18, Lead reading L40). Frozen at its push; repairs go in a NEW file docs/si/P-N5-DEPTH-add-fixes-box22.md.
Lead 18:32Z: «docs/si/P-N5-DEPTH-add-box22.md, CONDITIONAL items, each with its exact premise named in its own line … It is reviewed after those
premises have both signatures». Working notes: docs/si/N5-GCILEN-box22.md §6, docs/si/N5-EXIT-box22.md §1, §2, §8.
Labels: PROVED (lane, unrefereed, CONDITIONAL as stated per item) / OPEN / DATA. Not a TARGET.md claim; G-N5-TIME stays OPEN. No arXiv source is
cited.
Quotes: [Q path@commit:lines] «…», checked by experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh, with a shifted-line control).

## 0. Items and their premises
| § | item | label | CONDITIONAL on (not landed) |
| --- | --- | --- | --- |
| §1 | Lemma GATE-PUSH | PROVED (to sign) | P-N5-ROOT-box20 Theorem FREEZE-A (b) and (R-LEN) (signed by REFEREE; REFEREE-2 pending) |
| §2 | Proposition PURE-LEN | PROVED (to sign) | FREEZE-A (b) as §1; P-N5-OFFMONO-add-box49 Lemma ZCH-COUNT (signed by REFEREE; REFEREE-2 pending); P-N5-DEPTH-box22 STATIC-DEPTH (frozen, in review) |
| §3 | Lemma MONO-REF | PROVED (to sign) | P-N5-OFFMONO-box49 §1 Lemma OFFSET-MONO and its Step 1 |
| §3 | Lemma E-ONEWAY | PROVED (to sign) | MONO-REF (so OFFSET-MONO) |
| §4 | data | DATA (not to sign) | — |
- Conditional premises, quoted:
  - [Q docs/si/P-N5-ROOT-box20.md@78bc0e6a8:88] «(b) For t ∈ [s, e] and z ∈ A_t: M_t(z) ≤ MoptA_t(z). Hence for s + L ≤ t ≤ t′ ≤ e and z ∈ A_{t′}:
    M_{t′}(z) = M_t(z) = MoptA_t(z).»
  - [Q docs/si/P-N5-ROOT-box20.md@78bc0e6a8:114-115] «(R-LEN) On [s + L, e], Ξ on A_t changes only in its length … with lengths in [1, |U| − 1].»
  - [Q docs/new/P-N5-OFFMONO-add-box49.md@78bc0e6a8:89] «Statement. In a phase P, for the class c: |ZCH_c(P)| ≤ (n − 1)·|U_c| + TIE_c + ODDC_c.»
  - [Q docs/new/P-N5-OFFMONO-box49.md@78bc0e6a8:52-53] «Statement. Let t → t + 1 be an in-phase transition of P, q ∈ Q ∩ U with q ≠ c and q on no honest cycle
    at t, and p := par_{t+1}(q). Then off_{t+1}(q; p) ⪰ off_t(q; p).»
- LANDED premises: (M2κ) and κ-Y-FORM_D of RESULTS R56 (a), (d): [Q docs/RESULTS.md@78bc0e6a8:2858] «κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of
  κ_t(y)»; (SW) as listed in RESULTS R72; (Aκ), (M1κ) (P-N5-FBPOLY-box41 §0.3).

## 1. Lemma GATE-PUSH (PROVED, lane; CONDITIONAL on FREEZE-A (b), (R-LEN))
Setting. A pure C-interval [a, b] of class c (P-N5-GCX-box21 §1, per class; every gate of U_c D-direct at every state); A_t := F_D(t) ∩ U_c is
non-increasing on it; L := max(|A_a| − 1, 0); M = the path-weight component of κ.
Statement. Let a + L ≤ t < b and let σ̄ change at a gate u ∈ D ∩ U_c from y1 to y2 at t → t+1, with y1 ∈ A_{t+1}. Then M_{t+1}(y1) = M_t(y1)
and κ_{t+1}(y1) ≻ κ_t(y1) (a rise of the length component only), unless κ_{t+1}(y1) = κ_{t+1}(y2).
Proof. u's honest play continues into A, which holds no gate, so u lies on no honest cycle at t, t + 1 (as in FREEZE-A (c)). y2 = σ̄_{t+1}(u)
∈ A_{t+1} ⊆ A_t (direct gate; A non-increasing), so y2's honest play at t avoids D_t ∋ u: y2 ∈ Y^u_t. y1 ∈ A_{t+1}, so y1 ∈ Y^u_{t+1}. By
κ-Y-FORM_D at t and t + 1 and (M2κ): κ_t(y1) ⪯ κ_t(y2) ⪯ κ_{t+1}(y2) ⪯ κ_{t+1}(y1), the last strict unless κ_{t+1}(y1) = κ_{t+1}(y2). y1 ∈
A_{t+1} ⊆ A_t, so FREEZE-A (b) gives M_{t+1}(y1) = M_t(y1): the rise is in the length. □
- Count. By (R-LEN), each y ∈ A has at most |U_c| − 2 length rises on [a + L, b]. A switch away from a y1 ∉ A_{t+1} removes y1 from A for good
  (A non-increasing), so such switches number ≤ |A_a| in all. Hence N_σ̄ := the transitions of [a + L, b] with a σ̄ change in U_c satisfy
  N_σ̄ ≤ Σ_{u ∈ D ∩ U_c} deg(u)·(|U_c| − 2) + |A_a| + TIES_c, where TIES_c counts the tie switches (κ_{t+1}(y1) = κ_{t+1}(y2)).
  (Off D, σ̄ = τ is constant, because D ∩ U_c is constant on a C-interval.)
- Repair against the working note: N5-GCILEN-box22 §6 stated GATE-PUSH without the hypothesis y1 ∈ A_{t+1}, and its count without the
  |A_a| term. The form here governs.

## 2. Proposition PURE-LEN (PROVED, lane; CONDITIONAL on FREEZE-A (b), ZCH-COUNT, STATIC-DEPTH)
Statement. For a pure C-interval [a, b] of class c, under GEN_W on U_c:
b − a ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc, where N_σ̄ is as in §1 and N_cyc ≤ (n − 1)·|U_c| + TIE_c + ODDC_c is the number of
transitions changing c's cycle (ZCH-COUNT).
Proof. Cut [a + L, b] at every σ̄ change in U_c and every change of c's cycle. On each piece, σ̄ is constant on U_c (H2). In a pure interval
every cycle met from U_c is common to both frames, and with no cycle change it is constant (H3). PURE-END (P-N5-DEPTH-box22 §2) gives (H4) at
the piece's end. W-plays from U_c stay in U_c (off D they follow τ = σ̄, and through a gate they enter τ(u) ∈ A ⊆ U_c), so STATIC-DEPTH
applies on U_c and bounds each piece by |U_c| − 1. Pieces number ≤ 1 + N_σ̄ + N_cyc, and the cut transitions are counted once each. □
- With no tie terms the bound is polynomial in n. "< 2n" (the reading of N5-ABSCYC §4) holds exactly when N_σ̄ = N_cyc = 0.

## 3. Lemma MONO-REF and Lemma E-ONEWAY (PROVED, lane; CONDITIONAL on OFFSET-MONO)
Setting of P-N5-OFFMONO §0 (class c, U = U_c, T := (Q ∩ U) ∪ {c}, off_s(z; m) := κ_s(z) − κ_s(m)).
- Lemma MONO-REF. Let t → t+1 be in-phase, z ∈ U ∖ {c}, and m ∈ T on z's honest (t+1)-play, m ≠ z. Suppose the Q-vertices of that play from z
  (included) to m (excluded) are on no honest cycle at t. Then off_{t+1}(z; m) ⪰ off_t(z; m).
  Proof. Telescope along the T-vertices x_1, …, x_h = m of z's (t+1)-play: off(z; m) = off(z; x_1) + Σ_{i<h} off(x_i; x_{i+1}) at both times,
  with par_{t+1}(x_i) = x_{i+1}. Each level term is ⪰ 0 by OFFSET-MONO. The first term is OFFSET-MONO if z ∈ Q. Otherwise it is OFFSET-MONO's
  Step 1 on the Q-free path from z to x_1: Odd vertices outside Q have one successor, and Even switches go along Iσ_t ((SW), (M1κ)). □
- Lemma E-ONEWAY. Let Even w ∈ U ∖ {c} switch a → b at t → t+1. Let e1 ∈ T be the exit of a (the first T-vertex on a's play), with a's class
  exit path π_a and exit e1 unchanged on [t, t′]. Let e1 lie on w's honest play at every state of [t + 1, t′], with MONO-REF's no-cycle
  hypothesis. Then w does not switch back to a at t′ → t′ + 1.
  Proof. h := κwt_c(w) + κwt_c(π_a); g_s := off_s(w; e1). (SW), (M1κ): κ_t(b) ≻ κ_t(a). MONO-REF at b (e1 on b's (t+1)-play):
  g_{t+1} = κwt_c(w) + off_{t+1}(b; e1) ⪰ κwt_c(w) + off_t(b; e1) ≻ κwt_c(w) + off_t(a; e1) = h. MONO-REF at w keeps g ⪰ g_{t+1} ≻ h up
  to t′. A switch back needs κ_{t′}(a) ≻ κ_{t′}(σ_{t′} w), i.e. h ≻ g_{t′}. Contradiction. □

## 4. DATA (not to sign)
- GATE-PUSH / PURE-LEN: no pure C-interval in the data has an Even switch at index ≥ (|A_a| − 1) + |U_c| (evenside.py PURELATE = 0;
  N5-EXIT §8). The largest switch index in a pure interval is 28 (lib41).
- MONO-REF: 400,807 checks, 0 violations; control MRMUT bites (exitx.py; N5-EXIT §5).
- E-ONEWAY: 777 windows, 0 returns; control E1MUT bites on 6 of 8 long instances (evenside.py; N5-EXIT §8).
