import sys, glob, collections, re
for rev in ('0','1'):
    tot = collections.Counter(); files = 0
    for f in glob.glob(sys.argv[1] + f'/*_r{rev}.res'):
        files += 1
        for line in open(f):
            m = re.match(r'^(.*): (\d+)$', line.strip())
            if m: tot[m.group(1)] = max(tot[m.group(1)], int(m.group(2))) if m.group(1).startswith("max") else tot[m.group(1)] + int(m.group(2))
            elif line.strip(): tot['OTHER: ' + line.strip()[:60]] += 1
    print(f'--- order {"reverse-ins (R2_REV=1)" if rev=="1" else "Oink"}: {files} files')
    for k in sorted(tot): print(f'{k}: {tot[k]}')
