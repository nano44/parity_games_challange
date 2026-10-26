import re,sys
txt=open('RESULTS_pin.md').read()
secs={}; cur=None
for line in txt.splitlines():
    m=re.match(r'^### (R\d+)\b',line)
    if m: cur=m.group(1); secs[cur]=[]
    elif line.startswith('## '): cur=None
    if cur: secs[cur].append(line)
pk=set('R15 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29 R30 R31 R32 R33 R34 R38 R39 R42 R44 R45 R48 R50'.split())
for k in sorted(pk,key=lambda r:int(r[1:])):
    body='\n'.join(secs[k])
    for m in re.finditer(r'\bR(\d+)\b',body):
        t='R'+m.group(1)
        if t not in pk:
            s=body[max(0,m.start()-70):m.end()+40].replace('\n',' ')
            print(k,'->',t,'|',s)
