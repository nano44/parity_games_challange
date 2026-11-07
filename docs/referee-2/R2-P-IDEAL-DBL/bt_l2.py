# REFEREE-2 succ. 30: byte test P-IDEAL-DBL L-1 -> L-2 (replacements read by script from fixes entry 1, «OLD «…»» / «NEW «…»» pairs)
import sys, hashlib, re
L1 = open(sys.argv[1], encoding='utf-8').read(); L2 = open(sys.argv[2], encoding='utf-8').read(); F = open(sys.argv[3], encoding='utf-8').read()
part = F.split('### Line L-2', 1)[1]
pairs = re.findall(r'\n- ([^\n]+)\n    OLD «(.*)»\n    NEW «(.*)»', part)
x = L1
for name, a, b in pairs: print('%-26s old in L-1 %d, new in L-2 %d' % (name, L1.count(a), L2.count(b))); x = x.replace(a, b)
d = m = 0
for c in L2: d += (c == '(') - (c == ')'); m = min(m, d)
print(len(pairs), 'replacements; L-1 + all == L-2', x == L2, hashlib.sha1(x.encode()).hexdigest(), len(x.encode()), 'lines', L2.count('\n'), '(', L2.count('('), ')', L2.count(')'), '|', L2.count('|'), 'mindepth', m)
mine = open(sys.argv[4], encoding='utf-8').read() if len(sys.argv) > 4 else ''
for name, a, b in pairs:
    if name.startswith('W-2 (') and name[5] in 'abc': print(name, 'NEW == my W-2 text:', b in mine)
