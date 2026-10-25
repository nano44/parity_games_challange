# R65: adversary on P-N5-U23 (CASC-U2, CASC-U3, corollaries) (L-RED successor 14, box 35; GO 2026-10-24 23:37Z, date -u)
Target (Lead 23:37Z): docs/new/P-N5-U23-box31.md (sha1 ee3e5d1e, pinned at trunk 7666336). Tasks:
- (1) break CASC-U2 and CASC-U3 as stated, corollaries included;
- (2) reach a U2 W-flat switch;
- (3) K_W and E per piece versus n.
𝒞^1O only: one Odd vertex with out-degree > 1, asserted in the checker. Referees were not contacted. Labels per L40. G-N5-TIME stays
OPEN.

## 0. Checker: experiments/red/xing/u23x.py (the packet exactly as frozen)
Compared with L-NEW's experiments/new/box31/u23check.py (not edited), u23x.py adds:
- (a) U23 stretches (¬H1, ¬H2, c_θ ≠ o, c_w ≠ o). u23check never classifies them, so they were never checked. Concrete case:
  u23sw64_n32 below has 64 switches in a U23 stretch, and u23check prints {} for it.
- (b) CASC-U3 (iii) at the stated threshold 2|R| − 4, with o ∈ R. u23check tests 2(|R∖{o}| + 1) = 2|R|.
- (c) CASC-U3 (ii) (kind A: step ≤ L_B + λ(v) − 3, never for λ = 1), not tested by u23check.
- (d) Both corollaries: #transitions changing Ξ, W or σ on R against f + K_W + (K_W + f + 1)(|R| − 2) (U2), and against
  f + K_W + E + (K_W + f + E + 1)(2|R| − 4) (U3 / U23).
On shared ground it agrees with u23check: u3ev_n16 has 8 U3 switches, all events, max 2 per run; U2 switch counts agree on every
instance below.

## 1. Results (DATA)
- Sweep: about 90 pinned 𝒞^1O instances (experiments/red, si/xing, si/orlens, new/box29, new/box31).
  - 3 U2, 4 U3 and 9 U23 stretches.
  - 0 violations of CASC-U2, (i), (ii), (iii) and both corollaries.
- Climbs (u23x.py --climb, fitness (violations, target, …), 2,100-2,400 s, 23:38-00:17Z). Every pinned best: n5.py = n5b, Oink zlk
  OK, strategies verified.

| best (sha1) | n | what it reaches | violations | N5 it. / fb |
| --- | --- | --- | --- | --- |
| u2flat_n32 (1a016c44…) | 32 | first U2 W-flat switches: 2 (u23check agrees) | 0 | 13 / 3 |
| **u2flat73_n32** (bc1547d4…) | 32 | **73 U2 W-flat switches** in 5 U2 stretches (u23check agrees: U2_sw 73, max W-flat run 3); corollary slack −2 | 0 | 16 / 5 |
| **u23sw64_n32** (18b46837…) | 32 | 64 switches in U23 W-flat runs, invisible to u23check | 0 | 16 / 1 |
| kw25_n32 (607f1cc0…) | 32 | K_W = 25 non-fallback W-changes on R in one U2 stretch; corollary slack −116 | 0 | 29 / 1 |
| (sl, not pinned; 94ce3655…) | 16 | best corollary slack −1 among stretches with a change (1 change, bound 2) | 0 | 7 / 1 |

- (2) answered: CASC-U2 is now exercised by real U2 W-flat switches (73 on one instance), and it holds.
- CASC-U3 (i)-(iii) hold on 64 non-event U23 switches. The corollaries hold, the closest at slack −1 / −2 on short stretches.

## 2. (3) K_W and E versus n
PENDING: K_W climbs at n 16 / 24 / 48 (1,500 s each) end ~00:44Z (date -u). So far K_W per stretch: 15 (obr_n32 seed) → 25 (kw25_n32) at n 32; E per sub-run ≤ 2 everywhere (u3ev_n16).
