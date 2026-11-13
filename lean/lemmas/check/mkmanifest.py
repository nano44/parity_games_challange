# Formats lean/lemmas/MANIFEST.md from the output of `lake env lean check/manifest.lean`.
# usage (from lean/lemmas): python3 check/mkmanifest.py <manifest.out> <build.log> <axioms.out> <now> [<tree commit>] > MANIFEST.md
import sys, re, subprocess, hashlib
man, buildlog, axout, now = sys.argv[1:5]
tree = sys.argv[5] if len(sys.argv) > 5 else '78c32d90'
L = open(man).read().splitlines()
thms, mods = [], {}
for l in L:
    if l.startswith('THM '):
        f = [x.strip() for x in l[4:].split('|')]
        name, mod, line, head, dm = f[0], f[1], int(f[2].split()[1]), f[3].replace('type head ', ''), f[4]
        dm = dm.replace('defmods [', '').rstrip(']')
        thms.append((name, mod, line, head, [x.strip() for x in dm.split(',') if x.strip()]))
    if l.startswith('MOD '):
        f = [x.strip() for x in l[4:].split('|')]
        mods[f[0]] = (int(f[1]), f[2])
def path(mod): return mod.replace('.', '/') + '.lean'
def git(*a): return subprocess.run(['git', *a], capture_output=True, text=True).stdout.strip()
def first_commit(p, line):
    src = open(p).read().splitlines()[line - 1]
    m = re.match(r'\s*(?:private\s+)?(?:theorem|lemma)\s+(\S+)', src)
    tok = m.group(1) if m else None
    if tok is None: return '?', src
    pat = r'(theorem|lemma) ' + re.escape(tok) + r'( |$)'
    c = git('log', '--reverse', '--format=%h', '-E', '-G', pat, '--', p).splitlines()
    return (c[0][:8] if c else 'uncommitted'), tok
ACC = {
 'PGLemmas.Defs': 'definitions of Statements.lean; the Lead\'s diffs 11:49Z-14:54Z (INDEX l. 3-4); per-file time not recorded (see note)',
 'PGLemmas.Statements': 'sent 11:44Z (notebook); accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4)',
 'PGLemmas.Statements2': 'sent 12:26Z; accepted 12:29Z / 13:13Z (notebook Queue item 0)',
 'PGLemmas.Statements3': 'accepted 12:29Z / 13:13Z (notebook Queue item 0)',
 'PGLemmas.Statements4': 'accepted 12:29Z / 13:13Z (notebook Queue item 0); proved bound is R234\'s corrected one (README)',
 'PGLemmas.Statements5': 'accepted 12:29Z / 13:13Z (notebook Queue item 0); IMPLIES R118 (i)(b), (c), not word for word (README)',
 'PGLemmas.Statements6': 'accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4); per-file time not recorded (see note)',
 'PGLemmas.Statements7': 'accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4); kept apart from the landed BR-SEG-G text (README)',
 'PGLemmas.OptExists': 'OptCounterExistsStatement: accepted in the diffs 11:49Z-14:54Z (INDEX l. 3-4)',
 'PGLemmas.AbsStatement': '13:58Z, reading rules (i)-(v) (README «Statement ABS»)',
 'PGLemmas.PlateauStatement': '14:54Z, deviations (a)-(c) (README «PLATEAU, abstract»)',
 'PGLemmas.LevelCountStatement': '15:16Z, deviation lines (a)-(c) (README «LEVEL, the counting»)',
 'PGLemmas.Genome': '15:36Z, 15:50Z, deviations (a)-(h); (h) `WF.one_le_N` REQUIRED by the Lead (README «THE GENOME LAYER»)',
 'PGLemmas.GenomeClass': '15:50Z, deviations (K2), (K3) (e), (K4) (README «THE GENOME LAYER»)',
 'PGLemmas.GenomeOrderStatement': '18:20Z (repeated 18:30Z, 18:43Z): «stronger than box 208 §1: all pairs (Λ, E), B-ONLY not used»',
 'PGLemmas.GenomeLevelStatement': '18:20Z (repeated 18:30Z, 18:43Z), deviations (i)-(vii) quoted in README',
 'PGLemmas.GenomeRunStatement': '18:43Z, named deviation «existence is not stated in the fleet texts …; uniqueness not claimed»',
 'PGLemmas.GenomeExample': 'the witness genome `tiny`; tiny_wf / tiny_run accepted 18:43Z («Accepted as an example theorem»); 19:00Z «witness by existence (optCounter_exists), not by computation»',
 'PGLemmas.GenomeImpStatement': '19:05Z (readings (a)-(d)); ImpK5NewStatement 19:13Z, named point «stated for every mover, moved or not»',
 'PGLemmas.Gamma3': 'DEFINITIONS, 22:22Z «with deviations (a)-(e) as you named them» (file header)',
 'PGLemmas.Gamma3Statement': '22:56Z: PadStatement «with deviations (i)-(iii)», Gamma3OldStatement, Gamma3CardStatement (file header); PAD (c) not stated there',
 'PGLemmas.Gamma3LiftStatement': '2026-11-13 00:00Z «with deviations (i)-(iv)» (file header)',
}
HELPER = 'helper definitions, NO separate acceptance recorded in lane files; they enter the types of the theorems listed'
out = []
P = out.append
P('# lean/lemmas MANIFEST (L-FORMAL, %s by date -u; for the Lead\'s RESULTS draft and CHECKER)' % now)
P('')
P('Generated, not hand-copied: (a) and (b) come from `lake env lean check/manifest.lean` (a `#eval` over the compiled environment:')
P('each theorem named in Axioms.lean, its module and line, the head of its type after the binders, and every PG definition the type')
P('depends on, transitively through definition bodies, grouped by module); the «commit» column is the first commit whose diff adds the')
P('declaration line (`git log -G`); sha1 = sha1sum of the file at this commit. Status of every row: «Lean-checked (lane)»; a result only')
P('through CHECKER and the CI job lean-lemmas. Scope: see README «Status and reading rules»; nothing here is a TARGET.md §2 statement.')
P('')
P('## (a) Theorems offered (%d = every `#print axioms` line of Axioms.lean)' % len(thms))
P('')
P('| # | theorem | Statement (type head) | file:line | first commit |')
P('| --- | --- | --- | --- | --- |')
for i, (n, mod, line, head, dm) in enumerate(thms, 1):
    c, tok = first_commit(path(mod), line)
    st = head.replace('PG.', '') if head.endswith('Statement') else '(no Statement; type: %s)' % head.replace('PG.', '')
    P('| %d | `%s` | %s | %s:%d | %s |' % (i, n.replace('PG.', ''), st, path(mod).replace('PGLemmas/', ''), line, c))
P('')
P('## (b) Definition modules the offered types depend on (%d)' % len(mods))
P('')
P('Statements.lean … Statements7.lean, Defs.lean, OptExists.lean (Lead 21:03Z, verbatim): «per-file acceptance times not recorded by the')
P('Lead; the acceptance set is 11:49Z, 12:29Z, 13:13Z, 13:58Z, 14:54Z (2026-11-12)». CHECKER diffs each Statement against its lane text;')
P('the times are context, not the check. «Helper definitions» rows: no separate acceptance is recorded; CHECKER diffs them as definitions.')
P('')
P('| module | sha1 | definitions | Lead acceptance | theorems reaching it |')
P('| --- | --- | --- | --- | --- |')
for mod in sorted(mods):
    k, ds = mods[mod]
    sha = hashlib.sha1(open(path(mod), 'rb').read()).hexdigest()
    ds = ds.strip('[]').replace('PG.', '').split(', ')
    ds = [d for d in ds if not re.search(r'\.(mk|match_\d+|_sparseCasesOn_\d+|cons|nil|elim)$', d)]
    reach = [i for i, t in enumerate(thms, 1) if mod in t[4]]
    P('| %s | %s | %s | %s | %d: #%s |' % (path(mod).replace('PGLemmas/', ''), sha[:12], ', '.join('`%s`' % d for d in ds),
        ACC.get(mod, HELPER), len(reach), ', #'.join(map(str, reach)) if len(reach) < 12 else '%d-%d (%d rows)' % (reach[0], reach[-1], len(reach))))
P('')
P('## (c) Commands and outputs (run from lean/lemmas on the tree of %s; the MANIFEST commit adds no file under PGLemmas/)' % tree)
P('')
b = open(buildlog).read()
ax = open(axout).read().splitlines()
P('```')
P('lake exe cache get')
P('rm -rf .lake/build && lake build')
for l in b.splitlines():
    if l.startswith(('start', 'end', 'Build completed', 'build exit', 'axioms exit', 'grep exit')): P('  ' + l)
P('  lines with «warning:»: %d' % b.count('warning:'))
P('lake env lean Axioms.lean')
from collections import Counter
cnt = Counter(re.sub(r"^'[^ ]*' ", '', a) for a in ax if 'axioms' in a)
for k, v in sorted(cnt.items()): P('  %3d  %s' % (v, k))
P("grep -rnw --include=*.lean -e sorry -e admit -e axiom -e native_decide . --exclude-dir=.lake   (prints nothing, exit 1)")
P('lake env lean check/manifest.lean   (the generator of (a) and (b))')
P('```')
print('\n'.join(out))
