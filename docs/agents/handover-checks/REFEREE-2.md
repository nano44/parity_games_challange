# REFEREE-2 handover check (successor 36, Opus 5.5 under D1/D18/D20; 2026-11-09 09:52Z by date -u)
1. Branch claude/referee-2. At start: fetch --unshallow + fetch + checkout + ff-only (local ref was 157 behind; fast-forwarded);
   `git branch --show-current` = claude/referee-2, HEAD = origin/claude/referee-2 = dfe26882. vs trunk claude/vibrant-johnson-nxvvxo
   98e1c8be: 2 ahead / 242 behind (merge-base 63a3cf87). No trunk merge made (not needed for my items).
2. Open work, after «go», in order:
   A. Byte test of P-N5-QN fixes entry 1 + line L-1 (L-NEW 69; SHA from the Lead, not yet sent). Base review R2-P-N5-QN.md (5d4f06c2):
      check R-1 (REQUIRED, (k+1)-Λ values: «K1, and for each cycle of the functional graph Ξ_σ on the movers, x → xt(x, σ_t(x)), the most
      relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces»); GATE-FLIP (b) keeps «under HYPOTHESIS [E-LEV]»;
      DATA rule on gfc203.py / lam203.py (unit, condition, constants); each old string once, each new once, nothing else changed.
      Then read docs/referee/R-P-N5-QN.md (452800c5, LN-1..LN-8, QN-1) → R2-P-N5-QN.md Addendum 1 (+ agreement addendum). Waiting for SHA.
   B. Full independent second review of P-N5-SPLIT: claude/l-new FROZEN 399cda07, docs/new/P-N5-SPLIT.md sha1 5bc1b1f3… (re-hashed now:
      5bc1b1f390ed81683fe5c93008c7ea0b338fe735, 30,949 B); fixes entry 1 63515442; split.pins 59 rows; check.sh «P-N5-SPLIT». Every
      statement conditional on R125 (P-N5-CHAIN, pending CHECKER C139). Next step: re-derive each proof; P-N5-CHAIN premises quoted by
      script against CHAIN's signed text; own replay (on R2-P-N5-CHAIN/r2chain.py) with firing controls; TARGET.md diff; line
      requirements with exact strings. Report docs/referee-2/R2-P-N5-SPLIT.md, one commit per box; docs/referee/ read only after verdict.
      L-RED 62 R228-box91 / R229 = context only. Not started.
   C. Later: P-N5-CHAIN L-5 byte test (if CHECKER C139 rules line items); P-N5-GATE (L-SI 50) review when routed.
3. GAPS rows: none owned by REFEREE-2 (docs/GAPS.md owner column has no REFEREE-2 entry).
4. Rulings (DECISIONS-INDEX status):
   - D1 (active): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's
     own, as wrong until it passes the gauntlet below.»
   - D1 (active): «Never downgrade the referee to save money.»
   - D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
     mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
     briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   (D20, active, sets pace: «We have reset the weekly usage, so we can again work faster no?»)
5. Trap: a container starting with a stale local claude/referee-2 (here 157 behind; earlier 145) makes push.sh fail or push the wrong
   head. Check: fetch --unshallow + fetch + checkout + merge --ff-only, then `git branch --show-current` = claude/referee-2 and
   HEAD = origin/claude/referee-2 before any commit. Second trap: a line «signed by both referees» must be checked on the other
   referee's branch on origin before a MATCH is unconditional.
