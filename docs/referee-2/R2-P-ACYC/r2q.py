# REFEREE-2 32: every «...» quote in P-ACYC §0 (and §4/§5) checked verbatim against trunk sources (own code).
import re, subprocess, sys
S = sys.argv[1]  # packet commit
TR = sys.argv[2]  # trunk commit
pk = subprocess.run(['git','show',f'{S}:docs/si/P-ACYC.md'],capture_output=True,text=True).stdout
srcs = {}
for f in ['docs/RESULTS.md','docs/new/N5-ssi-global.md']:
    srcs[f] = subprocess.run(['git','show',f'{TR}:{f}'],capture_output=True,text=True).stdout
norm = lambda s: re.sub(r'\s+',' ',s)
# packet quotes may wrap lines with indentation: normalise whitespace on both sides
N = {f: norm(t) for f,t in srcs.items()}
sec = None; n=ok=0
for ln_i, q in enumerate(re.findall(r'«(.*?)»', pk, flags=re.S)):
    qn = norm(q)
    hits = {f: N[f].count(qn) for f in N}
    n += 1; good = any(hits.values()); ok += good
    print(('OK  ' if good else 'MISS'), hits, '|', qn[:110])
print(f'quotes: {ok} of {n} found verbatim (whitespace-normalised)')
