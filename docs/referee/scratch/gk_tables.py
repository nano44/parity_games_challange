#!/usr/bin/env python3
"""REFEREE successor 35: builds docs/referee/R-GK-precheck.md from scratch/gk_precheck_tmpl.md and the logs in scratch/gk_logs/.
Every number of the report's tables is read from a log (or, for the landed reference values, from the landed files named below).
usage (from docs/referee/scratch): python3 gk_tables.py "<header time>" """
import ast
import glob
import os
import re
import sys

R = '../../..'
LOG = 'gk_logs'


def rd(p): return open(p, encoding='utf-8').read()


def table(head, rows):
    out = ['| ' + ' | '.join(head) + ' |', '| ' + ' | '.join('---' for _ in head) + ' |']
    for r in rows: out.append('| ' + ' | '.join(str(c) for c in r) + ' |')
    return '\n'.join(out)


def t_sha():
    rule = rd('gk_rule.txt')
    pins = dict(re.findall(r'G_(\d+) ([0-9a-f]{40})', rule))
    rows = []
    for k, sha, N in re.findall(r'G_(\d+) sha1 ([0-9a-f]{40}) N (\d+)', rd(LOG + '/sha.out')):
        rows.append((k, N, sha, pins.get(k, '(no pin)'), 'EQUAL' if pins.get(k) == sha else 'DIFFERENT'))
    assert len(rows) == 4 and all(r[4] == 'EQUAL' for r in rows)
    return table(['k', 'N', 'sha1 of json.dumps(raw(k)), my rebuild', "the Lead's pin (Appendix A)", ''], rows)


MEM = re.compile(r'G_(\d+): N (\d+) \(9k-16 = (\d+)\) M (\d+) d (\d+) \(k\+1 = (\d+)\) \| DEF clauses (\d+)/(\d+) ok \| Xi-acyclic (\w+) \| renumbering order-preserving (\w+) \| max movers per level (\d+) \| wires (\d+) \| level-0 movers with both Xi-targets X (\d+) \| parities (\[[^\]]*\]) \| L (\d+) \(2\^k-2 = (\d+)\) stop (\w+) \| max sw (\d+) \(2\^\(k-2\) = (\d+)\) \| n3 (\d+) \(135k-230 = (\d+)\)')


def mem_rows():
    rows = [m.groups() for m in MEM.finditer(rd(LOG + '/member.out'))]
    assert len(rows) == 13, len(rows)
    return rows


def t_member():
    rows = []
    for (k, N, N9, M, d, k1, okc, nc, acyc, ren, wid, wires, l0, par, L, L2, stop, sw, sw2, n3, n3f) in mem_rows():
        assert N == N9 and d == k1 and okc == nc and acyc == 'True' and ren == 'True' and n3 == n3f
        rows.append((k, N, M, d, '%s / %s' % (okc, nc), acyc, ren, wid, wires, l0, par, n3))
    return table(['k', 'N (= 9k − 16)', 'M', 'levels d (= k + 1)', 'clauses 1-9 true', 'Ξ-acyclic', 'renumbering order-preserving', 'max movers on a level', 'wires', 'level-0 movers with both Ξ-targets X', 'parities used', 'n3 = N + 7M + 10 (= 135k − 230)'], rows)


def t_L():
    rows = []
    for (k, N, N9, M, d, k1, okc, nc, acyc, ren, wid, wires, l0, par, L, L2, stop, sw, sw2, n3, n3f) in mem_rows():
        rows.append((k, L, L2, 'EQUAL' if L == L2 else 'DIFFERENT', stop, sw, sw2, 'EQUAL' if sw == sw2 else 'DIFFERENT'))
    assert all(r[3] == 'EQUAL' and r[7] == 'EQUAL' for r in rows)
    return table(['k', 'L(G_k), my simulator', '2^k − 2', '', 'stop', 'max_x sw(x)', '2^(k−2)', ''], rows)


def t_val_ideal():
    # landed references: R104 packet §7 (the 7 champions) and R117's reachcheck.out (C14)
    pk = rd(R + '/docs/red/P-N5-REALIZE.md')
    m = re.search(r'the 7 R178 champions \(([^)]*)\) \| ([0-9 /]+) \|', pk)
    names = [x.strip() for x in m.group(1).split(',')]
    champs = []
    for nmx in names:
        if '/' in nmx:
            pre = nmx.split('/')[0]                       # big_d3/d4/d6/d8_k3_W3
            parts = nmx.split('/')
            base = parts[0][:len('big_')]
            suffix = parts[-1][parts[-1].index('_'):]
            champs += [parts[0] + suffix] + [base + p + suffix for p in parts[1:-1]] + [base + parts[-1]]
        else: champs.append(nmx)
    Ls = [int(x) for x in m.group(2).split('/')]
    ref = {c + '.json': (l, 'R104 packet §7') for c, l in zip(champs, Ls)}
    assert len(ref) == 7, ref
    for nmx, l in re.findall(r'^C14 (\S+\.json) N \d+ M \d+ L (\d+) ', rd(R + '/experiments/new/box189/reachcheck.out'), re.M):
        ref[nmx] = (int(l), 'R117 reachcheck.out')
    rows = []
    for nmx, N, M, d, L, stop in re.findall(r'^(\S+\.json) N (\d+) M (\d+) d (\d+) DEF True ACYC True L (\d+) stop (\w+)', rd(LOG + '/val_ideal.out'), re.M):
        rl, src = ref[nmx]
        rows.append((nmx, N, M, L, rl, src, 'EQUAL' if int(L) == rl else 'DIFFERENT'))
    assert len(rows) == 21 and all(r[6] == 'EQUAL' for r in rows), rows
    return table(['genome', 'N', 'M', 'L, my simulator', 'landed L', 'source of the landed L', ''], rows)


RE_REACH = re.compile(r"^(\S+\.json) N (\d+) M (\d+) L (\d+) n3 (\d+) iterations (\d+) \(L\+3 = (\d+)\) fallback transitions (\[[^\]]*\]) counters (\{[^}]*\}) Even wins (\d+) of (\d+)", re.M)


def t_val_reach():
    ref = {}
    for nmx, L, n, it, fb in re.findall(r'^C14 (\S+\.json) N \d+ M \d+ L (\d+) Gamma3 n (\d+) S3-iterations (\d+) fallbacks (\d+)', rd(R + '/experiments/new/box189/reachcheck.out'), re.M):
        ref[nmx] = (int(L), int(n), int(it), int(fb))
    rows = []
    for (nmx, N, M, L, n3, it, l3, fbs, cnt, ew, tot) in RE_REACH.findall(rd(LOG + '/val_reach.out')):
        c = ast.literal_eval(cnt); f = ast.literal_eval(fbs)
        rf = ref[nmx]
        eq = (int(L), int(n3), int(it), len(f)) == rf and f == [int(L) + 1]
        rows.append((nmx, n3, L, it, fbs, 'L %d, n %d, iterations %d, fallbacks %d' % rf, sum(c.values()), 'EQUAL' if eq else 'DIFFERENT'))
    assert len(rows) == 14 and all(r[7] == 'EQUAL' and r[6] == 0 for r in rows), rows
    return table(['genome', 'n3', 'L', 'iterations, my replay', 'fallback transitions', 'landed (R117 reachcheck.out)', 'sum of my 7 counters', ''], rows)


RE_N5 = re.compile(r"^G_(\d+): N (\d+) M (\d+) L (\d+) n3 (\d+) \| N5 from S3: iterations (\d+) \(2\^k\+1 = (\d+)\) fallback transitions (\[[^\]]*\]) \(2\^k-1 = (\d+)\) \| counters (\{[^}]*\}) \| Even wins (\d+) of (\d+) \| ([0-9.]+)s", re.M)


def t_n5():
    rows = []; done = set()
    files = [LOG + '/n5_3_9.out'] + [f for f in sorted(glob.glob(LOG + '/n5_1[0-9].out')) if rd(f).rstrip().endswith('exit 0')]
    for f in files:
        for (k, N, M, L, n3, it, it2, fbs, fb2, cnt, ew, tot, secs) in RE_N5.findall(rd(f)):
            c = ast.literal_eval(cnt); fl = ast.literal_eval(fbs)
            ok = it == it2 and fl == [int(fb2)] and sum(c.values()) == 0
            rows.append((k, n3, L, it, it2, fbs, fb2, ' '.join('%s %d' % kv for kv in c.items()), '%s of %s' % (ew, tot), secs, 'AS CLAIMED' if ok else 'DIFFERENT'))
            done.add(int(k))
    assert all(r[-1] == 'AS CLAIMED' for r in rows) and set(range(3, 10)) <= done
    t = table(['k', 'n3', 'L (IDEAL)', 'iterations', '2^k + 1', 'fallback transitions', '2^k − 1', 'counters', "Even's region (N5 = Zielonka)", 'engine seconds', ''], rows)
    missing = [k for k in (10, 11, 12) if k not in done]
    if missing: t += '\n\nNOT RUN at this writing: k = %s (long jobs; `bash gk_run.sh n5`; an addendum will carry them).' % ', '.join(str(k) for k in missing)
    return t


RE_LEM = re.compile(r"^G_(\d+)( \[control revE\])? n3 (\d+) max priority (\d+): (\d+) standard states \(seed (\d+)\): SBAR (\d+) TAU (\d+) ESC0 (\d+) ESC (\d+) W (\d+) XI (\d+) AV (\d+) STEP (\d+) \| IDEAL moved (\d+), stopped (\d+)", re.M)


def t_lemck():
    rows = []
    for (k, ctl, n3, mp, ns, seed, sbar, tau, esc0, esc, w, xi, av, stp, mv, st) in RE_LEM.findall(rd(LOG + '/lemck.out')):
        rows.append((k, 'control revE' if ctl else 'G_k', n3, mp, ns, seed, sbar, tau, esc0, esc, w, xi, av, stp, mv, st))
        if ctl: assert int(stp) == int(ns) and sbar == tau == esc0 == esc == w == xi == av == '0'
        else: assert sbar == tau == esc0 == esc == w == xi == av == stp == '0'
    assert len(rows) == 13, len(rows)
    return table(['k', 'game', 'n3', 'max priority', 'standard states', 'seed', 'SBAR', 'TAU', 'ESC0', 'ESC', 'W', 'XI', 'AV', 'STEP', 'states where the IDEAL run moves', 'stops'], rows)


def t_perm():
    rows = []
    for (k, ren, Lraw, Lren, npm, res) in re.findall(r'^G_(\d+): RENUM (\d+) \(L raw (\d+) = L renumbered (\d+)\) \| PERM (\d+) permutations: \(L, iterations, fallback transitions, sum of counters\) = (\[.*\])$', rd(LOG + '/perm.out'), re.M):
        r = ast.literal_eval(res)
        assert ren == '0' and len(r) == 1 and r[0][3] == 0 and r[0][1] == 2 ** int(k) + 1
        rows.append((k, ren, npm, r[0][0], r[0][1], list(r[0][2]), r[0][3]))
    assert len(rows) == 4
    return table(['k', 'RENUM', 'mover permutations', 'L', 'iterations (all permutations)', 'fallback transitions', 'sum of the 7 counters'], rows)


def logblock(name, must):
    lines = [l for l in rd(LOG + '/' + name).rstrip('\n').split('\n')]
    assert lines[-1] == 'exit 0', name
    body = lines[:-1]
    for l in body: assert must(l), l
    return '```\n' + '\n'.join(l[:400] for l in body) + '\n```'


if __name__ == '__main__':
    t = rd('gk_precheck_tmpl.md')
    rep = {'@@HEADER_TIME@@': sys.argv[1], '@@TABLE_SHA@@': t_sha(), '@@TABLE_MEMBER@@': t_member(), '@@TABLE_L@@': t_L(), '@@TABLE_VAL_IDEAL@@': t_val_ideal(),
           '@@TABLE_VAL_REACH@@': t_val_reach(), '@@TABLE_N5@@': t_n5(), '@@TABLE_LEMCK@@': t_lemck(), '@@TABLE_PERM@@': t_perm(),
           '@@LOG_CTL@@': logblock('n5_ctl.out', lambda l: '[control revE]' in l and "'STD': 0" not in l and "'FLFB': 0" not in l and "'WIN': 0" in l and 'iterations 6 ' in l),
           '@@LOG_ABS@@': logblock('abs.out', lambda l: ' ABS (state bits that differ, all steps) 0;' in l and l.rstrip().endswith('differs) 0')),
           '@@LOG_ABSRAND@@': logblock('abs_rand.out', lambda l: 'ABS1 0 PREF1 0 WIRE 0' in l),
           '@@RULE@@': '\n'.join('> ' + l if l else '>' for l in rd('gk_rule.txt').rstrip('\n').split('\n'))}
    for key, val in rep.items():
        assert t.count(key) == 1, key
        t = t.replace(key, val)
    assert '@@' not in t
    open('../R-GK-precheck.md', 'w', encoding='utf-8').write(t)
    print('written ../R-GK-precheck.md: %d lines, %d bytes' % (t.count('\n'), len(t.encode('utf-8'))))
