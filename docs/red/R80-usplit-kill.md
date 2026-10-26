# R80: CONJECTURE U-SPLIT is FALSE (usplit_s3_n16, from SPEC S3, 𝒞^1O; three tools agree) (L-RED successor 20, box 47; Lead 09:31Z, 10:11Z, date -u)
Target: CONJECTURE U-SPLIT, docs/si/N5-RUND-box17.md §17 (L-SI successor 13 lane note; read at l-si 873c8e71, which contains §17-§18 of
l-si 5402151c unchanged). The scenario is §18's ("Kill shape for L-RED"), built as a game. Labels per L40. Every game. Nothing here
bounds N5. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Result
- **KILL: CONJECTURE U-SPLIT is FALSE.** The instance has a U event inside one fallback-free in-phase run with (h3_D) at every state.
  y's offset does not rise at k → k + 1 (it stays 0 → 0), so it is not UP. D and the gate's (Ξ, W) values are constant on [f, k + 1],
  so it is not BD.
  - Instance experiments/red/usplit/instances/usplit_s3_n16.pg, sha1 6a3461f46d388629fa6c5f4de6f8a4af9bfdf946.
    n 16, one Odd choice vertex u = 5 (𝒞^1O). The start is SPEC S3 (Engine.initial("best") for both players); no start file.
  - Run: `python3 experiments/new/n5.py n5 usplit_s3_n16.pg out.sol` gives 3 iterations and 0 fallbacks. `check_sol2.py` gives
    "zielonka(oink zlk) OK strategies verified".
  - The event: k = 1, f = 0, y = 15, z = 14, σ(y) = a = 11 ∈ F_D, D = {5} at states 0..3.
  - L-SI's sched.py (l-si 873c8e71, USTRUCT=1, `--one <pg> -v`) reports:
    `NB k=1 f=0 y=15 z=14 a_f=11 a_k=11 off_y 0->0 off_z f/k/k+1 6272/0/0`, `USTRUCT … a_f=11(F) a_k=11(F) z@f=g5 z@k=F y@k+1=F D_f=[5]
    D_k=[5]`, `VIOLATION ('U_OTHER', …, 0, 1, (15, 14))`, `SCHED FAIL`.
  - My own checker, experiments/red/usplit/usplit20.py, is written from §14 / §16 / §17's definitions and does not reuse sched.py. It
    reports: runs 1, U 1, U under (h3_D) 1, UP 0, BD 0, neither 1, OUT_OINK OK.
  - Three tools agree: n5.py (the reference loop), my o1_19.trace and L-SI's n5x step, on 3 iterations.
- Two more pins of the same construction, from a start pair. Their gate is mkalt's (τ(u) = a1 with a1 → c), which SPEC S3 does not pick.
  - usplit_n14.pg: sha1 285497f1db9dffdb2cf00c64fa85d9b6bda09f2d; start usplit_n14.start 3ed9f888 (n5.py format), .start.json bd5c1853.
    3 iterations, 0 fallbacks; U event k = 1, f = 0; Oink OK; sched.py VIOLATION U_OTHER.
  - usplit_n23.pg: sha1 674cb6abf47050d30013b569246f2d40b3cbe364 (d = 4: the switch on z's route comes from a delay line); start
    usplit_n23.start e0bda349, .start.json 8c8848aa. 9 iterations, 0 fallbacks; U event k = 4, f = 3; Oink OK; sched.py U_OTHER.
- Family: experiments/red/usplit/mkusplit.py d LG OUT [s3]. Every (d, LG) with LG ≥ d + 2 tested (d 1-6, LG up to 14) has exactly one
  "neither" U event; the S3 variant was tested at d 1, 2, 4 × LG 3, 4, 6 and kills at (1, 4), (1, 6), (2, 4), (2, 6), (4, 6). Generated files are byte-identical to the pins (cmp).

## 1. The construction (exactly §18's scenario)
- Vertices: an even sink c (priority 2, self-loop; the one cycle node). A gate u (Odd, priority 9) with successors a1 and b1:
  - S3 variant: a1 is odd 30003 → ga, which is even 30004 → c. b1 is odd 30001 → e1 → … → g1, a delay chain of length LG ending at
    even 40042.
  - τ(u) = a1, by local reward. σ̄(u) = b1: under σ_0 the chain points to c, so b1's route tops at odd b1, while a1's tops at even ga.
  - u stays in D until the chain is wired (state LG). Iτ = ∅: against τ, Even's best response wires the chain, and b1's route then tops at
    g1, which is worse for Odd.
- y (Even, priority 15): successors a (even 20 → c, an F_D route; Ξ = W there) and z.
- z (Even, priority 13): successors s (even 30 → u, the gated route) and r1, the head of a line r1 … r_d → h (h even 30006 → c).
  Line vertices are small odd, so they are unattractive until wired.
- At state 0, (y, z) is forbidden:
  - COARSE W(z) has top vertex ga (even) and beats W(a) = {20};
  - Ξ(z) has top vertex b1 (odd), so Ξ(z) ◁ Ξ(a).
- z → r1 is Ξ-improving from the start (Ξ(s) tops at odd b1), but S4a's W-optimum keeps s until r1's W-value tops at h. Then z switches
  to an F_D route that is better in both frames: §18's step 2.
- At the next state Ξ(z) tops at h, so (y, z) ∈ Iσ, and y switches. This is a U event: forbidden at f = k − 1, which is in the window.
  y's offset is 0 before (y → a ∈ F_D) and 0 after (y → z → F_D route).
- No fallback, λ_W constant, (h3_D) at every state (u's cycle node is c in both frames), D = {u} constant, u's (Ξ, W) constant on [f, k + 1].

## 2. What it does to the reduction (READING)
- §17's Consequence (|U(S)| ≤ Σ_y N_y^↑ + n·n_E·B(S)) is lost as a route. A U event can be paid by a ROUTE change downstream of y, which is
  §18's own reading of the scenario. Here that route change is z's switch at k − 1 → k, into an F_D route. It is itself a coarse
  W-change of z, but not a U event (z → r1 was never forbidden: Ξ-improving all along).
- So the recursion §18 describes ends after one level here. A replacement statement could charge a non-UP, non-BD U event of y to a
  coarse W-change of its new successor z at k − 1 → k. The data in this family is consistent with that; I did not test it beyond the family.
- UF-ONCE was already dead (REFEREE-2 16; Lead 10:11Z). The family above has one U event per run, so it says nothing new about UF-ONCE.

## 3. Tools (experiments/red/usplit/)
- mkusplit.py: the generator. usplit20.py: the exact checker (runs, forbidden, U, (h3_D), UP, BD, offsets; OUT via verify.py; Oink with
  --oink). show.py: per-state trace printer.
- L-SI's tools run from a detached worktree of origin/claude/l-si at 873c8e71, read only, removed afterwards.
