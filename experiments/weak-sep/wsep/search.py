"""Minimum separator size by increasing k, lazily adding violated graphs (CEGAR), with the independent checker."""
from __future__ import annotations
import time
from .graphs import maximal_graphs
from .encode import Encoder
from .automata import check_separator


def min_separator(n, d, conv, strong, k_start=1, k_max=40, log=print, eager=False, solver='cadical153'):
    evens = maximal_graphs(n, d, conv, 0)
    odds = [] if strong else maximal_graphs(n, d, conv, 1)
    log(f"[{n},{d},{conv},{'strong' if strong else 'weak'}] maximal even graphs: {len(evens)}, odd graphs: {len(odds)}")
    for k in range(k_start, k_max + 1):
        t0 = time.time()
        enc = Encoder(n, d, k, strong, solver)
        added_e, added_o = set(), set()
        if eager:
            for i, g in enumerate(evens):
                enc.add_even(g); added_e.add(i)
            for i, g in enumerate(odds):
                enc.add_odd(g); added_o.add(i)
        rounds = 0
        while True:
            rounds += 1
            aut = enc.solve()
            if aut is None:
                log(f"  k={k}: UNSAT after {rounds} rounds, {len(added_e)}+{len(added_o)} graphs, "
                    f"{enc.nv} vars, {enc.nclauses} clauses, {time.time()-t0:.1f}s")
                enc.delete()
                break
            bad = check_separator(aut, evens, odds, strong)
            if not bad:
                log(f"  k={k}: SAT, verified by checker after {rounds} rounds ({len(added_e)}+{len(added_o)} graphs), "
                    f"{time.time()-t0:.1f}s")
                enc.delete()
                return k, aut, {'evens': len(evens), 'odds': len(odds), 'used_even': len(added_e), 'used_odd': len(added_o)}
            # add up to 3 violated graphs
            cnt = 0
            for kind, g in bad:
                if kind == 'W1':
                    i = evens.index(g)
                    if i not in added_e:
                        enc.add_even(g); added_e.add(i); cnt += 1
                elif kind == 'W2':
                    i = odds.index(g)
                    if i not in added_o:
                        enc.add_odd(g); added_o.add(i); cnt += 1
                else:
                    raise AssertionError("S2 violated although encoded: encoding bug")
                if cnt >= 3:
                    break
            assert cnt > 0, "checker rejects but no new graph to add: encoding/checker disagree"
    return None, None, None
