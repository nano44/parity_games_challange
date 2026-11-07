#!/usr/bin/env python3
"""P-TOWER-FUEL fix round 2 (L-LOWER successor 7): build line L-3 from L-2 by CHECKER C134 §5's replacements R1-R4, in that order.
Every OLD and NEW string is copied by this script from a byte copy of docs/checker/C134.md (claude/checker 23871f48), §5, with a
wrapped line joined to the next by one space (C134 §5's rule). Asserts: each old once in the running text it is applied to, each new
once right after its replacement and once in L-3 (R2's new with R3 applied: R3's old occurs once, inside R2's new), «(» = «)», depth never negative, no «|», «gauntlet» 0 times, and C134's target sha1 / bytes.
Usage: mkL3_tf.py C134.md L2.txt OUT_L3.txt"""
import sys, re, hashlib
C, L2 = (open(p, encoding='utf-8').read() for p in sys.argv[1:3]); OUT = sys.argv[3]
def norm(s): return re.sub(r'\s*\n\s*', ' ', s)
sec = C[C.index('## 5. The L-3 (exact wording)'):C.index('## DONE / FINDINGS / NEEDS')]
REPL = []
for tag in ('R1 (E-1)', 'R2 (E-2)', 'R3 (E-3)', 'R4 (E-4)'):
    i = sec.index('- ' + tag + ': «'); j = sec.index('\n- ', i + 1)
    q = re.findall(r'«(.*?)»', sec[i:j], flags=re.S); assert len(q) == 2, (tag, len(q))
    REPL.append((tag, norm(q[0]), norm(q[1])))
TARGET = re.search(r'sha1 ([0-9a-f]{40}) with its newline \(([0-9,]+) bytes\)', sec); TSHA, TB = TARGET.group(1), int(TARGET.group(2).replace(',', ''))
line = L2.rstrip('\n'); assert L2.endswith('\n') and '\n' not in line
L3 = line
for tag, o, n in REPL:
    assert L3.count(o) == 1, (tag, L3.count(o), o); L3 = L3.replace(o, n); assert L3.count(n) == 1, (tag, L3.count(n))
r2n_after_r3 = REPL[1][2].replace(REPL[2][1], REPL[2][2]); assert REPL[1][2].count(REPL[2][1]) == 1   # R3's only occurrence is in R2's new
for n in (REPL[0][2], r2n_after_r3, REPL[2][2], REPL[3][2]): assert L3.count(n) == 1, n
dep = 0
for ch in L3:
    dep += (ch == '(') - (ch == ')'); assert dep >= 0
assert dep == 0 and '|' not in L3 and L3.count('gauntlet') == 0
b = (L3 + '\n').encode('utf-8'); h = hashlib.sha1(b).hexdigest()
assert h == TSHA and len(b) == TB, (h, len(b), TSHA, TB)
open(OUT, 'w', encoding='utf-8').write(L3 + '\n')
for tag, o, n in REPL: print(tag, '\n   OLD «' + o + '»\n   NEW «' + n + '»')
print('L-3:', OUT, 'sha1', h, len(b), 'bytes,', len(L3) + 1, 'characters,', L3.count('('), '«(» =', L3.count(')'), '«)»; 0 «|»; «gauntlet» 0;',
      'equals C134 §5 target', TSHA, TB, 'bytes')
