#!/usr/bin/env python3
"""P-TOWER-FUEL fix round 1 (L-LOWER successor 6): write docs/lower/P-TOWER-FUEL-fixes.md entry 1. Every quoted referee or packet string
is copied by this script from byte copies (wrapped lines joined by single spaces) and asserted to occur in its source.
Usage: mkfix_tf.py R1.md R2.md PACKET.md L2.txt OUT.md"""
import sys, re, hashlib, textwrap
R1, R2, PK = (open(p, encoding='utf-8').read() for p in sys.argv[1:4]); L2 = sys.argv[4]; OUT = sys.argv[5]
def norm(s): return re.sub(r'\s*\n\s*', ' ', s)
N1, N2, NP = norm(R1), norm(R2), norm(PK)
def between(src, start, end, incl_end=True):
    i = src.index(start); j = src.index(end, i + len(start)); return src[i:j + (len(end) if incl_end else 0)]
def q(s, src):
    assert s in src, s[:80]; return '«' + s + '»'
# TF-1 / W-1
pk_iii = between(NP, 'Under the RANK hypothesis at s, |D_s|', '= [D_s > 0]')
r1_rep = between(N1, 'Repaired proof (to go into a fixes entry): ', '∎')[len('Repaired proof (to go into a fixes entry): '):]
r1_cnt = between(N1, 'Measured: the first inequality fails', 'counter proofstep_absD_lt_2^R)')
r2_w1new = re.findall(r'«(.*?)»', between(R2, '- **W-1 (packet', '- The statement is unchanged.'), flags=re.S)[1]; r2_w1new = norm(r2_w1new)
r2_cnt = between(N2, 'Measured on the 1,010 corpus states', 'at 5.')
r2_chk = between(N2, 'Checked pointwise at every state of every crossed pair:', 'at all of them.')
# TF-3, TF-4 / W-3, §5
pk_unit = '(unit = 5-window; set = all 63 5-windows; scope = stored start)'
pk_dec = between(NP, 'In all 48 failing 6-windows the deciding element (Lemma 4)', 'β of the capped pair 4.')
pk_e5 = 'E5 0 (unit = doubling level, 62)'
r1_tf4 = between(N1, '«Lemma 4 (b) is violated in exactly those windows by a parked β» is a READING:', 'Label it READING or measure it.')
r2_w3 = between(N2, '- **§4 reading, false literally (W-3).**', 'what fails in the 48 windows is the move count (E4).')
r1_tf2 = between(N1, 'TF-2 (optional remark, no change required):', 'So (E5) holds without F(j − 1) ≥ 1.')
r2_n1 = between(N2, '**N-1:**', 'no change is required.')
r1_slip = between(N1, 'Packet-description slip', '(sha1 binds).')
for s, src in ((pk_iii, NP), (pk_unit, NP), (pk_e5, NP)): assert s in src
l2 = open(L2, 'rb').read(); l2sha = hashlib.sha1(l2).hexdigest()
P = []
def para(t):
    for w in range(136, 100, -1):   # no continuation line may start with «|» or «- » (markdown table / list)
        f = textwrap.fill(t, w, break_long_words=False, break_on_hyphens=False, subsequent_indent='  ')
        if not any(l.lstrip().startswith(('|', '- ')) for l in f.split('\n')[1:]): break
    P.append(f)
P.append('# P-TOWER-FUEL fixes (append-only; the packet docs/lower/P-TOWER-FUEL.md stays frozen at 7f7ff6f5, line L-1 at 408470ad…)\n')
P.append('## Fixes entry 1 (2026-11-07, L-LOWER successor 6; fix round 1; written by experiments/lower/l5/mkfix_tf.py)')
para('Reports answered: REFEREE 27 claude/referee 807984e30699f4fa5b042dabb1bf1470a83ac928, docs/referee/R-P-TOWER-FUEL.md (all SIGN; '
     'CROSS-ECONOMY (iii) SIGN WITH GAP TF-1; L-1 NOT YET: TF-L1, TF-L2, TF-L3 required, TF-L4, TF-L5 optional); REFEREE-2 31 '
     'claude/referee-2 4bede4dda1e0610627cf44661acb65555ccc456e, docs/referee-2/R2-P-TOWER-FUEL.md (all SIGN, (iii) on its repaired proof; '
     'L-1 MATCHES after W-2 (a)-(c), W-4 (a)-(c)). Merged under the Lead rulings of 15:18Z (Lead reading). Every «…» below is copied by '
     'the script from byte copies of the reports or of the packet (wrapped lines joined by single spaces).')
P.append('\n### 1. TF-1 = W-1: proof of Lemma 5 (iii) (statement unchanged)')
para('- Packet text replaced (§3, Lemma 5 proof): ' + q(pk_iii, NP) + '. Both referees found this inequality false; their counts are on '
     'different state sets: REFEREE (RANK states at the two pre-states u₁ − 1, u₂ − 1 of the 43 corpus windows): ' + q(r1_cnt, N1) +
     '; REFEREE-2 (every corpus state of the 14 crossed pairs at which RANK holds): ' + q(r2_cnt, N2) + '.')
para('- Proof of record (REFEREE\'s repair; it uses only the packet\'s Lemma 4 (a), ENC and acyclicity): ' + q(r1_rep, N1))
para('- Independent second route (REFEREE-2\'s repair, recorded, not needed for the record): ' + q(r2_w1new, N2) + ' REFEREE-2: ' +
     q(r2_chk, N2))
P.append('\n### 2. TF-3: unit of the 30 I-ROOM units (§4)')
para('- ' + q(pk_unit, NP) + ' reads «(unit = (5-window, PULSE or GAP): 30 units on 16 distinct 5-windows; set = all 63 5-windows; '
     'scope = stored start)». p_tower_check.py now asserts the 16 distinct windows and the 119 j-windows of levels 1-5.')
P.append('\n### 3. TF-4 = W-3: the I-FUEL decider sentence (§4)')
para('- Packet text replaced: ' + q(pk_dec, NP))
para('- New text: «In each of the 48 failing 6-windows [a, e], option 19 = (mover 9, option 1), rank 87, odd parity, on 11\'s chain '
     '(11 → 9), is dec_s(12) or dec_s(13) at some state s among s_(a−1), …, s_(e−1); at s_(a−1) itself in 32 of the 48; at every such '
     'state in 16 of the 48; at no such state in any of the 79 other 6-windows (unit = 6-window; set = all 127; scope = stored start). '
     'Mover 9 is on option 1 at every pre-state of all 48 failing windows (and of 17 good ones). Lemma 4 (b) is not applied here: level 6 '
     'is not doubling; its conclusion (a non-constant decider between consecutive moves) holds for all 188 consecutive-move pairs of 12 '
     'and 13. READING: the room conditions are met and the missing piece is fuel; the parked β of option (9, 1) of the capped pair 4 '
     'dominates the crossed comparison in those windows (DOMINANCE-FREEZE read as an interpretation, not applied as a lemma).»')
para('- Counts re-measured by me with an independent simulator (experiments/lower/l6/sim6.py, Python big integers, not sharing code '
     'with p_tower_check.py): 48 / 48 at some pre-state, 32 / 48 at s_(a−1), 16 / 48 at every pre-state, 32 / 48 at some state s_a … s_e, '
     '0 / 79 good; mover 9 on option 1 at every pre-state: 48 failing, 17 good; decider non-constant on 188 of 188 consecutive-move pairs '
     'of 12, 13. Equal to both referees: REFEREE §4 table (failing / other: some pre-state 48 / 48, 0 / 79; s_(a−1) only 32 / 48, 0 / 79; every '
     'pre-state 16 / 48, 0 / 79; some state s_a … s_e 32 / 48, 0 / 79) and ' + q("The packet's «48 / none of the 79» is exact for the first scope only.", R1) +
     '; REFEREE-2 ' + q(r2_w3, N2) + ' p_tower_check.py now asserts 32, 16 and 188.')
para('- REFEREE\'s scope note on the same sentence: ' + q(r1_tf4, N1))
P.append('\n### 4. §5: hypothesis of (E5)')
para('- ' + q(pk_e5, NP) + ' reads «E5 0 (unit = doubling (run, level) pair, 62; its hypothesis F(j − 1) ≥ 1 holds on 61 of them)». '
     'Optional TF-2 = N-1 noted, statement NOT changed (it stays as frozen and as in L-2): REFEREE ' + q(r1_tf2, N1) + '; REFEREE-2 ' +
     q(r2_n1, N2))
P.append('\n### 5. Line L-2 (docs/lower/P-TOWER-FUEL-line-L2.txt; made by experiments/lower/l5/mkL2_tf.py)')
para(f'- sha1 {l2sha}, {len(l2)} bytes, {len(l2.decode("utf-8"))} characters, 1 line + «\\n»; parentheses balanced (depth never negative); '
     'no «|». Each old string occurs exactly once in L-1, each new exactly once in L-2 (asserted by mkL2_tf.py). L-2 is not equal to either '
     'referee\'s predicted line (REFEREE d115d8df…, REFEREE-2 1a4e8dcc…): the Lead\'s rulings merge the two sets. Pinned in p_tower_check.py.')
para('- Merge map (L-2 replacement → referee items; where both targeted one old string, ONE new string carries the facts of both):')
for t in [
 'M1 notation «… F(l) and cv)»: W-2 (a) (REFEREE-2; old and new copied from its report).',
 'M2 I-ROOM: TF-L5 (REFEREE: «16 of its 63 5-windows», «(j = 1, …, 5)») + W-2 (b) (REFEREE-2: «at levels j = 1, …, 5 (unit = j-window; set = all 119 of them)») + TF-3 (REFEREE: unit (5-window, PULSE or GAP)); same old string in both reports.',
 'M3 I-FUEL: TF-L3 (REFEREE: «at some state s among s_(a−1), …, s_(e−1) of the window [a, e]», «at no such state in any of the other 79», the movers 12 and 13) + W-2 (c) (REFEREE-2: «do not have exactly one move of each member of pair 6 (crossed onto movers 22, 11)», «at every such state in 16 of them»); same old string.',
 'M4 corpus: W-4 (a) (REFEREE-2; new copied from its report: the 15 + 7 + 2 runs, «62 doubling (run, level) pairs»).',
 'M5 DOUBLE-EQ: TF-L1 (REFEREE: 7,069 per (step, doubling level), 757 j-windows, 61 levels with F(j − 1) ≥ 1) + W-4 (b) (REFEREE-2: «on 7,069 (step, doubling level) units for its first two clauses, on the 757 j-windows for the third and on the 62 doubling (run, level) pairs for the fourth»); same old string.',
 'M6 DOMINANCE-FREEZE: TF-L2 (REFEREE; new copied from its report) — it contains W-4 (c)\'s fact (REFEREE-2: unit (consecutive-state, mover), «with equal deciders»), whose old string is a substring of TF-L2\'s.',
 'M7 CROSS-ECONOMY chains: TF-L4 (REFEREE, optional, taken: one phrase; old and new copied from its report).']:
    para('  - ' + t)
para('- p_tower_check.py (extended; it still pins L-1 and now pins L-2) prints and asserts every unit L-2 names: E3 units 7,069, E5 hypothesis '
     'levels 61 of 62, 119 j-windows at j = 1..5, 16 distinct 5-windows, decider scopes 48 / 32 / 16 / 0, 188 of 188, plus all old counters.')
P.append('\n### 6. Description slip (REFEREE, REFEREE-2)')
para('- ' + q(r1_slip, N1) + ' L-2 above is given in bytes and characters.')
open(OUT, 'w', encoding='utf-8').write('\n'.join(P) + '\n')
print('written', OUT)
