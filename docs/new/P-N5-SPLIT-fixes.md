# P-N5-SPLIT fixes (append-only; the packet docs/new/P-N5-SPLIT.md is frozen at l-new 399cda07, sha1 5bc1b1f390ed81683fe5c93008c7ea0b338fe735)

## Fixes entry 1 (L-NEW successor 67; written 2026-11-09 00:44Z by date -u; source: L-RED 62's packet-level read, claude/l-red f3903cb8 docs/red/R228-box91.md (B), relayed by the Lead 2026-11-09 00:25Z; I have not opened f3903cb8: it was not on origin when I fetched)
Scope: DATA only (§9.1). No statement, proof, premise or DEAD row of the packet changes.
- (n1) TAKEN. §9.1's clause «max c_y ≤ 6 outside MW (C6G8_n54 6), MW 2n + 1 (65 on MW32_2)» is restated with its set:
  - «On the 28 frozen instances of experiments/new/box199/inst (split199.out): max c_y ≤ 6 outside the MW family (C6G8_n54: 6); MW(n) has
    max c_y = 2n + 1 (65 on MW32_2).»
  - It is NOT a corpus statement. L-RED 62's cap-scaling climb (ORDER=CT, mutants of L-SI's MW(n), claude/l-red 6080533a / 4b06129e /
    0657d38f) reaches C 12 at N + M ≤ 200 and C 26 at N + M ≤ 400 (relayed by the Lead; not re-run by me; instances not frozen by me). These
    are on MW's line (C ≈ 2n + 1 at N + M ≈ 29n + 29): linear in N + M.
  - No PROVED statement used the clause. SPLIT-COUNT's tightness remark (MW and FW) is unchanged.
- (n2) NO CHANGE. §9.1 already says that playfail, kindfail, trfail and wlamfail test definitions and have no firing control; L-RED's
  split228 reproduces them on its own engine. Taken as stated.
- Lines: none (this entry changes no signable text).
