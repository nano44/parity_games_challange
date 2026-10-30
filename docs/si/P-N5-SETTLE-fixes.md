# P-N5-SETTLE fixes (repairs and status notes against the FROZEN packet docs/si/P-N5-SETTLE-box52.md, sha1 aef403c3d8a003bcfc6742c4d1da084a1e21669f)
L-SI. The frozen file is never edited. Each entry names the section, says whether a TO-SIGN item is affected, and gives the evidence.

## F0 (L-SI successor 34, 2026-10-30 18:5xZ; status note, no signed item affected)
- §8 lists CONJECTURE FLIP-EV as «NOT to sign». It is now DEAD.
  - Instance experiments/si/heads52/inst/flipev_n20.pg + .start, transition 2 → 3: Odd 10, not its own Ξ-cycle node, leaves D with both
    targets' Ξ fixed, in a W-run with no event (iii). The cause is Odd 14 entering D (Ξ(τ(14)) rose; its new target is tied).
  - n5x and n5b SPEC agree; pins in experiments/si/check.sh «box 52 §3 (18:5xZ)».
- §8's sentence on FLIP-RED is void. §§3-7 (the items to sign) do not use FLIP-EV.
