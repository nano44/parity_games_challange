#!/usr/bin/env python3
"""REFEREE-2 succ. 31: the fixes-entry-1 passages attributed to REFEREE-2 occur verbatim (whitespace-normalised) in my report 4bede4dd.
Usage: bt_fxq.py MYREPORT.md"""
import sys, re
n = lambda t: re.sub(r'\s+', ' ', t)
MY = n(open(sys.argv[1], encoding='utf-8').read())
for q in ['Measured on the 1,010 corpus states of the 14 crossed pairs where the RANK hypothesis holds (r2tower.out): |D| < 2^r* at 651, and |D| ≤ 2·max|θ| at 5.',
          'Checked pointwise at every state of every crossed pair: 0 violations on 1,010 RANK states, and |D| > max|θ| at all of them.',
          '**N-1:** since {w, c′} = {0, 1}, one window already gives γ_j(0) = γ_j(1) and fixes the first mover as 2j iff ¬γ_j(0), so the hypothesis F(j − 1) ≥ 1 is not needed. The statement as written is true; no change is required.',
          '- **§4 reading, false literally (W-3).** «Lemma 4 (b) is violated in exactly those windows by a parked β of the capped pair 4» does not hold literally: - for every pair of consecutive moves of 12 (94 pairs) and of 13 (94 pairs), dec is NOT constant between them, i.e. the conclusion of Lemma 4 (b) holds everywhere (r2fuel.out); - level 6 is not doubling, so (b) does not apply in any case; - what fails in the 48 windows is the move count (E4).',
          'at levels j = 1, …, 5 (unit = j-window; set = all 119 of them)',
          'do not have exactly one move of each member of pair 6 (crossed onto movers 22, 11)', 'at every such state in 16 of them',
          'on 7,069 (step, doubling level) units for its first two clauses, on the 757 j-windows for the third and on the 62 doubling (run, level) pairs for the fourth']:
    print('verbatim' if n(q) in MY else 'NOT FOUND', ':', q[:80])
