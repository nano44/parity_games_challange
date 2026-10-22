#!/usr/bin/env python3
"""One query 'is there a weak / strong (n,d)-separator with exactly k reachable states?' for the expensive cells
(n = 5), resumable.  Same encoding and checker as compute.py (wsep.encode, wsep.automata); differences:
  - the maximal graph families are generated once (verify=True) and cached in out/fam_<conv>_n<n>_d<d>_w<win>.pkl;
  - the CEGAR graph set is checkpointed after every round in out/ckpt_<mode>_<conv>_n<n>_d<d>_k<k>.json, and a
    restarted query re-adds it first (a killed job loses only the current solver call);
  - --cnf writes the final formula (checkpointed graph set, added eagerly) as DIMACS to out/<case>.cnf, for an
    external solver with an LRAT proof; with --cnf the query is solved once on exactly that formula.
Answer semantics: SAT at k <=> a separator with <= k states exists (pad a smaller one by copying the target of a
non-tree transition; it accepts infinite words, so such a transition exists; docs/struct/S3-statement.md §2).
UNSAT at k therefore gives value >= k+1.  Every SAT automaton is re-verified on the full families before it is written.
Result: results/n5/<mode>_<conv>_n<n>_d<d>_k<k>.json.
Usage: n5.py N D CONV {weak|strong} K [--cnf | --cnf-only]"""
import sys, json, time, pickle, hashlib, argparse, pathlib, os
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from wsep.graphs import maximal_graphs
from wsep.encode import Encoder
from wsep.automata import check_separator

ap = argparse.ArgumentParser()
ap.add_argument('n', type=int); ap.add_argument('d', type=int); ap.add_argument('conv', choices=['E', 'S', 'V'])
ap.add_argument('mode', choices=['weak', 'strong']); ap.add_argument('k', type=int)
ap.add_argument('--cnf', action='store_true'); ap.add_argument('--cnf-only', action='store_true'); ap.add_argument('--solver', default='cadical153')
a = ap.parse_args()
strong = a.mode == 'strong'
OUT = HERE / 'out'; OUT.mkdir(exist_ok=True)
case = f"{a.mode}_{a.conv}_n{a.n}_d{a.d}_k{a.k}"
t0 = time.time()


def log(msg):
    print(f"[{time.strftime('%H:%M:%SZ', time.gmtime())} {case}] {msg}", flush=True)


def family(win):
    p = OUT / f"fam_{a.conv}_n{a.n}_d{a.d}_w{win}.pkl"
    if p.exists():
        return pickle.loads(p.read_bytes())
    t = time.time()
    g = maximal_graphs(a.n, a.d, a.conv, win, verify=True)
    p.write_bytes(pickle.dumps(g))
    log(f"family win={win}: {len(g)} graphs generated and verified in {time.time()-t:.0f}s")
    return g


evens = family(0)
odds = [] if strong else family(1)
ck = OUT / f"ckpt_{case}.json"
state = json.loads(ck.read_text()) if ck.exists() else {'even': [], 'odd': [], 'rounds': 0}
log(f"families {len(evens)}+{len(odds)}; checkpoint {len(state['even'])}+{len(state['odd'])} graphs, {state['rounds']} rounds")

enc = Encoder(a.n, a.d, a.k, strong, a.solver)
cnf_body = None
if a.cnf or a.cnf_only:  # record every clause from here on (the constructor's clauses are replayed below)
    enc2 = Encoder.__new__(Encoder)
    cls = []
    enc2.__dict__.update(solver_name=a.solver, n=a.n, d=a.d, k=a.k, strong=strong, nv=0, nclauses=0)

    class Rec:
        def add_clause(self, cl): cls.append(list(cl))
    enc2.solver = Rec()
    # rebuild with the recorder as solver, so the CNF is exactly the clauses the encoder emits
    enc2.t = [[[enc2.new() for _ in range(a.k + 1)] for _ in range(a.d)] for _ in range(a.k)]
    for q in range(a.k):
        for x in range(a.d):
            enc2.exactly_one(enc2.t[q][x])
    enc2.symmetry_breaking()
    if strong:
        enc2.strong_condition()
    for i in state['even']:
        enc2.add_even(evens[i])
    for i in state['odd']:
        enc2.add_odd(odds[i])
    body = "".join(" ".join(map(str, c)) + " 0\n" for c in cls)
    text = f"p cnf {enc2.nv} {len(cls)}\n" + body
    p = OUT / f"{case}.cnf"
    p.write_text(text)
    log(f"CNF {p.name}: {enc2.nv} vars, {len(cls)} clauses, sha256 {hashlib.sha256(text.encode()).hexdigest()}")
    cnf_body = (p.name, hashlib.sha256(text.encode()).hexdigest())
    if a.cnf_only:
        raise SystemExit(0)

for i in state['even']:
    enc.add_even(evens[i])
for i in state['odd']:
    enc.add_odd(odds[i])

result = None
while True:
    t1 = time.time()
    aut = enc.solve()
    state['rounds'] += 1
    if aut is None:
        log(f"UNSAT in round {state['rounds']} ({time.time()-t1:.0f}s solve), {len(state['even'])}+{len(state['odd'])} graphs, "
            f"{enc.nv} vars, {enc.nclauses} clauses")
        result = 'UNSAT'
        break
    bad = check_separator(aut, evens, odds, strong)
    if not bad:
        log(f"SAT, verified on all {len(evens)}+{len(odds)} graphs, round {state['rounds']} ({time.time()-t1:.0f}s solve)")
        result = 'SAT'
        break
    if a.cnf:
        raise SystemExit("--cnf: the checkpointed graph set does not refute k; run without --cnf first")
    cnt = 0
    for kind, g in bad:
        if kind == 'W1':
            i = evens.index(g)
            if i not in state['even']:
                enc.add_even(g); state['even'].append(i); cnt += 1
        elif kind == 'W2':
            i = odds.index(g)
            if i not in state['odd']:
                enc.add_odd(g); state['odd'].append(i); cnt += 1
        else:
            raise AssertionError("S2 violated although encoded: encoding bug")
        if cnt >= 3:
            break
    assert cnt > 0, "checker rejects but no new graph to add: encoding/checker disagree"
    ck.write_text(json.dumps(state))
    log(f"round {state['rounds']}: candidate rejected, +{cnt} graphs -> {len(state['even'])}+{len(state['odd'])} ({time.time()-t1:.0f}s solve)")

ck.write_text(json.dumps(state))
res = {'n': a.n, 'd': a.d, 'conv': a.conv, 'mode': a.mode, 'k': a.k, 'status': result, 'solver': a.solver,
       'automaton': aut if result == 'SAT' else None, 'families': [len(evens), len(odds)],
       'used_even': state['even'], 'used_odd': state['odd'], 'rounds': state['rounds'],
       'vars': enc.nv, 'clauses': enc.nclauses, 'seconds_this_run': round(time.time() - t0, 1), 'cnf': cnf_body}
rp = HERE / 'results' / 'n5' / f"{case}.json"
rp.parent.mkdir(parents=True, exist_ok=True)
rp.write_text(json.dumps(res, indent=1))
log(f"RESULT {result} -> {rp.relative_to(HERE)}")
