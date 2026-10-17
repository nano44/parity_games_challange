# Lane restart procedure
Replace a session at about 600k context, at a natural pause.
1. Old session overwrites notes/<LANE>.md with DONE, IN FLIGHT, NEEDS, "Things only I know"; pushes; reports the SHA; then parks.
2. Lead: create_session on the lane branch, outcome_branch = that branch, clone_depth 3000, with the lane brief.
3. New session answers the five questions into docs/agents/handover-checks/<LANE>.md, pushes, stops.
4. Lead re-measures each answer against the repo; a miss is written into the files before "go".
5. Record a row below, update the NOW roster.

Five questions:
1. Your branch, its head SHA, and how many commits ahead of and behind trunk (claude/vibrant-johnson-nxvvxo).
2. Your open work and the next step of each.
3. The docs/GAPS.md rows you own, with status.
4. The three owner rulings that most constrain you, verbatim, with their status in docs/DECISIONS-INDEX.md.
5. One trap that bit this lane before, and the check that now prevents it.

| date | lane | old session | new session | score (of 5) | misses fixed |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | L-LOWER | session_01U5n8mgXxgyGzvuUzxHbiKx | session_0153E4mCB2wqi65xdfpxozfK | 5 | none (answers re-measured: 29/18 vs trunk, merge-base fe676d9, no GAPS rows, core 100 games) |
| 2026-10-15 | L-ALG | session_01WN44zjFXZSqaL5SwsoDn7d | session_012cQPWcEm23KMdMQSvWrULr | 5 | none (re-measured: merge-base 1017502, 0 ahead; 107 behind at its fetch, 112 now after Lead commits; no GAPS rows; T-ALG1 unrouted is correct: deferred by Lead) |
| 2026-10-15 | L-COMP | session_014bbtNwaVKxFymHpXynjURn | session_01Nd4XCMfDaYHsh1P6XTtRGz | 5 | none (re-measured: merge-base 5ba5d8b; 12 ahead before its 2 commits = 14 now; behind grew with Lead commits; GAPS open table empty) |
| 2026-10-15 | L-ALG | session_012cQPWcEm23KMdMQSvWrULr | session_01Aoj1NEAPu4ibQ3VbNXaXVY | 5 | none (re-measured: merge-base ed9b87e, 0 ahead before its commit; no GAPS rows; T-ALG1 deferred by Lead) |
| 2026-10-16 | L-RED | session_017WLo5xfMxRZ4f6n2Su6274 | session_0117Yy21tGGz9s1zzLfBdUKC | 5 | none (re-measured: merge-base 5a30e98, 0 ahead before its commit; no GAPS rows; trap = piped verify, prevented by literal chain) |
| 2026-10-16 | L-ALG | session_01Aoj1NEAPu4ibQ3VbNXaXVY (Fable cap) | session_01BDELabbGbT2QYY2NoRCY8A (Opus, D8) | 5 | none (re-measured: merge-base fe22c7f; no GAPS rows; §5 per-level label fix noted) |
| 2026-10-16 | L-RED | session_0117Yy21tGGz9s1zzLfBdUKC (Fable cap) | session_01PxvcUhsSEhfjURzmBDBeoN (Opus, D8) | 5 | none (re-measured: merge-base 0bedda5; stale WORKING status noted, fixed at first push) |
| 2026-10-16 | L-LIT | session_01MxWPJxeciDocEdfd89xCF8 (539k context, parked) | session_01Sb99VhYmwmCzi8aeKybxzj (Opus, D8/D9) | 5 | none (re-measured: 4f61b4c ancestor of trunk, merge-base 3c6dfb6 after its merge; no GAPS rows; D1/D9/D8 verbatim match DECISIONS) |
| 2026-10-16 | L-ALG | session_01BDELabbGbT2QYY2NoRCY8A (box end, 555k) | session_01KESFSwLyyKvwe3mzqN2Bzr (Opus, D8) | 5 | none (re-measured: merge-base c18eaad, 278 behind b16716d, head d2ae597; (CM) 0/123 vs 0/129 = corpus difference, re-run asked) |
| 2026-10-16 | L-RED | session_01PxvcUhsSEhfjURzmBDBeoN (box end, 471k) | session_0187PESrNsHy3BTdjyzwyaLy (Opus, D8) | 5 | none (re-measured: head 718627d, merge-base b16716d, check.sh has 0 'head -1') |
| 2026-10-16 | L-ALG | session_01KESFSwLyyKvwe3mzqN2Bzr (box end, 536k) | session_01XTdnsK1p5KyoCaDSAc2evA (Opus, D8) | 5 | none (re-measured: head a864c97, b9b3b2b ancestor, 3 ahead / 2 behind trunk after Lead commits, merge-base 26417b3; GAPS open table empty; D1/D5/D8 verbatim match; trap = stale local branch before fetch, fixed by no-ff merge 723496d) |
| 2026-10-17 | L-RED | session_0187PESrNsHy3BTdjyzwyaLy (box 5 end, 587k) | session_01NCGdhfxbJoyHAubHP6tQRR (Opus, D8) | 5 | none (re-measured: head 8fac07c, 2387fd3 ancestor, 3 ahead / 3 behind trunk after Lead commits; GAPS open table empty; D1/D7/D8 verbatim match; trap = stale local branch, checked by is-ancestor; scratch climbs lost, relaunched from pinned gapb instances) |
| 2026-10-17 | L-ALG | session_01XTdnsK1p5KyoCaDSAc2evA (box 5 end, 705k) | session_01PEMUECoSbdbdZR2hHzbyTK (Opus, D8) | 5 | none (re-measured: head a34b3b1, 39f6111 ancestor, 2 ahead / 2 behind trunk after Lead commits; GAPS open table empty; D1/D5/D8 verbatim; trap = stale local branch, caught by is-ancestor check) |
| 2026-10-17 | L-RED | session_01NCGdhfxbJoyHAubHP6tQRR (box 6 end, 623k) | session_01DT8bvW9MGLgZURmnwB2JAc (Opus, D8) | 5 | none (re-measured: head dfb5b4d, 0883016 ancestor, 2 ahead / 9 behind trunk after Lead commits; owns no GAPS rows; D1/D7/D8 verbatim match; trap = stale local branch (1091 behind at start), caught by fetch + rev-parse check) |
| 2026-10-17 | REFEREE | session_01W3Z4peJy1bngBmMVdJ1f6K (parked ~550k after R-P5) | session_01M28EFY9Ysyqj67kXt3YSje (Opus, D12) | 5 | none (re-measured: head a13ad2f, ca03021 ancestor, stale local branch caught by fetch + fast-forward; GAPS G-STR shown open on its branch is pre-merge; trunk is truth) |
| 2026-10-17 | REFEREE-2 | session_01SdxPAhFBFXe4ZCwR1WfPL4 (parked ~580k after R2-P6) | session_01NUXFnUcx4V3ZWJJY11tXwx (Opus, D12) | 5 | none (re-measured: head 6f33a84 on c7634a7; stale local branch caught by fetch + fast-forward; push.sh ran before commit once, same tree verified, noted) |
