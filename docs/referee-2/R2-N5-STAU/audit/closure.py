import re,sys
txt=open(sys.argv[1]).read()
secs={}; cur=None
for line in txt.splitlines():
    m=re.match(r'^### (R\d+)\b',line)
    if m: cur=m.group(1); secs[cur]=[]
    elif line.startswith('## '): cur=None
    if cur: secs[cur].append(line)
refs={k:set(re.findall(r'\bR(\d+)\b','\n'.join(v)))-{k[1:]} for k,v in secs.items()}
def clos(start):
    seen=set(); st=[start]
    while st:
        x=st.pop()
        if x in seen: continue
        seen.add(x)
        for r in refs.get(x,()):
            st.append('R'+r)
    return seen
for s in sys.argv[2:]:
    c=clos(s); print(s, sorted(c,key=lambda r:int(r[1:])))
print('direct R48',sorted(refs['R48'],key=int)); print('direct R50',sorted(refs['R50'],key=int))
