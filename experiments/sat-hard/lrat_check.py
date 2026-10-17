#!/usr/bin/env python3
"""Minimal independent LRAT checker (RUP steps with hints; RAT / negative hints are rejected).
Usage: lrat_check.py formula.cnf proof.lrat  -> prints 'VERIFIED UNSAT' (empty clause derived) or an error; exit 0/1.
Proof lines (text LRAT): '<id> <lits...> 0 <hint ids...> 0' adds a clause; '<id> d <ids...> 0' deletes clauses.
A step is accepted iff, starting from the negation of its literals, each hint clause is unit or falsified under the
current assignment (unit -> assign), and the last hint yields a conflict."""
import sys


def main(cnf, proof):
    db = {}
    cid = 0
    with open(cnf) as f:
        for line in f:
            if line.startswith(("c", "p")) or not line.strip():
                continue
            lits = list(map(int, line.split()))
            assert lits[-1] == 0
            cid += 1
            db[cid] = lits[:-1]
    steps = 0
    with open(proof) as f:
        for line in f:
            if not line.strip() or line.startswith("c"):
                continue
            tok = line.split()
            sid = int(tok[0])
            if tok[1] == "d":
                for x in tok[2:-1]:
                    db.pop(int(x), None)
                continue
            z = tok.index("0", 1)
            lits = list(map(int, tok[1:z]))
            hints = list(map(int, tok[z + 1:-1]))
            assign = {}
            for l in lits:
                assign[-l] = True; assign[l] = False
            conflict = False
            for h in hints:
                if h < 0:
                    print(f"step {sid}: RAT hint not supported"); return 1
                cl = db.get(h)
                if cl is None:
                    print(f"step {sid}: hint {h} not in database"); return 1
                unassigned = [x for x in cl if x not in assign]
                if any(assign.get(x) is True for x in cl):
                    print(f"step {sid}: hint {h} is satisfied"); return 1
                if not unassigned:
                    conflict = True; break
                if len(unassigned) > 1:
                    print(f"step {sid}: hint {h} not unit"); return 1
                u = unassigned[0]
                assign[u] = True; assign[-u] = False
            if not conflict:
                print(f"step {sid}: hints do not reach a conflict"); return 1
            db[sid] = lits
            steps += 1
            if not lits:
                print(f"VERIFIED UNSAT ({steps} RUP steps)")
                return 0
    print("proof ends without the empty clause")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
