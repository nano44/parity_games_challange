import re,sys,os
P=r"S4b|S4 ?b\b|I_?τ|Iτ|I\^τ|τ_new|τ′_new|τ_\{?(?:k|t|j|i|a|b|s)\+1\}?|τ_\{k\+2\}|Odd.s (?:step|move|arena|fallback|switch|reply|best|optimal)|Odd (?:step|move|switch|improv|fall)|H′|H'(?![a-z])|counterstrategy|τ[ -](?:is )?(?:unchanged|constant|fixed|changes|moves|stays|kept|keeps|change)|changes? (?:of )?τ|τ-change|keeps τ|leaves? (?:the|its) phase|phase (?:ends|end|is left|exit)|ends? (?:the|its) phase|last state of|next phase|new phase|τ-stable|value-optimal|\btie|\bties\b|τ′|τ'"
rx=re.compile(P)
files=sys.argv[1:]
tot=0
for f in files:
    n=0
    for i,line in enumerate(open(os.path.join('pin',f)),1):
        if rx.search(line):
            n+=1; print(f'{f}:{i}: {line.rstrip()}')
    tot+=n
    print(f'## {f} hits {n}',file=sys.stderr)
print('TOTAL',tot,file=sys.stderr)
