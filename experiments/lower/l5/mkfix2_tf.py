#!/usr/bin/env python3
"""P-TOWER-FUEL fix round 2 (L-LOWER successor 7): append fixes entry 2 to docs/lower/P-TOWER-FUEL-fixes.md (append-only: the file's
first bytes must be entry 1 as pushed, sha1 0902efb9…). Every «…» string from CHECKER C134 is copied by this script from a byte copy of
docs/checker/C134.md (wrapped lines joined by single spaces) and asserted to occur there. Usage: mkfix2_tf.py C134.md L3.txt FIXES.md"""
import sys, re, hashlib, textwrap
C = open(sys.argv[1], encoding='utf-8').read(); L3p = sys.argv[2]; FX = sys.argv[3]
def norm(s): return re.sub(r'\s*\n\s*', ' ', s)
NC = norm(C)
old = open(FX, 'rb').read(); assert hashlib.sha1(old).hexdigest() == '0902efb9eaea48501e4289a8ce3980b235347ac8', 'fixes file is not entry 1 as pushed'
l3 = open(L3p, 'rb').read(); l3sha = hashlib.sha1(l3).hexdigest(); assert l3sha == '7328e67345e1bb6a8605ccfa4f406d1020eabfdb'
def between(src, start, end):
    i = src.index(start); j = src.index(end, i + len(start)); return src[i:j + len(end)]
def q(s):
    assert s in NC, s[:80]; return '«' + s + '»'
sec = C[C.index('## 5. The L-3 (exact wording)'):C.index('## DONE / FINDINGS / NEEDS')]
R = {}
for tag in ('R1 (E-1)', 'R2 (E-2)', 'R3 (E-3)', 'R4 (E-4)'):
    i = sec.index('- ' + tag + ': «'); j = sec.index('\n- ', i + 1); R[tag] = [norm(x) for x in re.findall(r'«(.*?)»', sec[i:j], flags=re.S)]
verdict = between(NC, 'All four are the drafter', 'changes.')
e = {k: between(NC, '- **' + k, nx) for k, nx in (('E-1', 'Fix: R1 (R-B).'), ('E-2', 'Fix: R2 (R-G).'), ('E-3', 'Fix: R3 (R-U), applied after R2 (R2\'s new text carries the only occurrence).'), ('E-4', 'Fix: R4 (R-S).'))}
n1 = between(NC, '- **N-1 (R-C not taken).**', '(C133).')
rule = 'In the strings above, a wrapped line is joined to the next with one space.'
tgt = between(NC, 'L-3 with R1-R4 (my script): ', '«gauntlet» 0 times.')
P = []
def para(t):
    for w in range(136, 100, -1):
        f = textwrap.fill(t, w, break_long_words=False, break_on_hyphens=False, subsequent_indent='  ')
        if not any(l.lstrip().startswith(('|', '- ', '#')) for l in f.split('\n')[1:]): break
    P.append(f)
P.append('\n## Fixes entry 2 (2026-11-07, L-LOWER successor 7; fix round 2; written by experiments/lower/l5/mkfix2_tf.py)')
para('Report answered: CHECKER C134 claude/checker 23871f4806e2670ccfb04d32fc8664e8ede9bc04, docs/checker/C134.md (landing check of RESULTS '
     'R120, first fill: FAIL E-1 to E-4; exact line L-3 in its §5), routed by the Lead 18:28Z. Verdict sentence: ' + q(verdict) + ' Every '
     '«…» below is copied by the script from a byte copy of C134.md (wrapped lines joined by single spaces). The packet (frozen at 7f7ff6f5), '
     'L-1, L-2 and fixes entry 1 are unchanged; no statement, proof, definition, instance or counter changes.')
P.append('\n### 1. The four findings (CHECKER C134 §3)')
def body(t): h = t.index('.** '); return t[len('- **'):h + 1], t[h + 4:]   # (bold heading, text after it)
for k in ('E-1', 'E-2', 'E-3', 'E-4'): hd, tx = body(e[k]); para('- ' + hd + ' ' + q(tx))
hd, tx = body(n1); para('- ' + hd + ' ' + q(tx))
P.append('\n### 2. The replacements (C134 §5, applied to L-2 in this order)')
for tag in ('R1 (E-1)', 'R2 (E-2)', 'R3 (E-3)', 'R4 (E-4)'):
    o, n = R[tag]; para('- ' + tag + ': old ' + q(o) + ' → new ' + q(n))
para('- C134 §5 rule: ' + q(rule) + ' R3 is applied after R2: its old string then occurs once, inside R2\'s new text (asserted).')
P.append('\n### 3. Line L-3 (docs/lower/P-TOWER-FUEL-line-L3.txt; made by experiments/lower/l5/mkL3_tf.py)')
para('- sha1 ' + l3sha + ', ' + str(len(l3)) + ' bytes, ' + str(len(l3.decode('utf-8'))) + ' characters, 1 line + «\\n»; '
     + str(l3.count(b'(')) + ' «(» / ' + str(l3.count(b')')) + ' «)», depth never negative; no «|»; «gauntlet» 0 times. It equals CHECKER C134\'s '
     'target byte for byte: ' + q(tgt) + ' (mkL3_tf.py asserts the sha1 and the byte count it reads from C134 §5).')
para('- p_tower_check.py (extended; it still pins L-1 and L-2) now pins L-3 and asserts the set of R4\'s clause on SL41_d28: 119 j-windows '
     'at j = 1..5, (3, 7, 15, 31, 63) per level, the same counts as C134 §3 E-4 (its instrumented copy), here from the lane\'s own '
     'windows(j). No other counter changes.')
new = old + ('\n'.join(P) + '\n').encode('utf-8')
open(FX, 'wb').write(new)
print('fixes entry 2 appended:', FX, 'sha1', hashlib.sha1(new).hexdigest(), len(new), 'bytes')
