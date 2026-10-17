#!/usr/bin/env python3
"""L-RED CARRY box (2026-10-16, produced on Opus 5.5): named-vertex builder for hand-wired DTL gadgets.
G = Game(); G.v(name, priority, owner, [successor names]); G.dump(path) writes a PGSolver .pg file (ids in insertion order)."""
import sys


class Game:
    def __init__(self):
        self.names, self.pr, self.ow, self.succ = [], {}, {}, {}

    def v(self, name, pr, ow, succ=()):
        assert name not in self.pr, name
        self.names.append(name); self.pr[name] = pr; self.ow[name] = ow; self.succ[name] = list(succ)
        return name

    def e(self, a, b):
        if b not in self.succ[a]: self.succ[a].append(b)

    def dumps(self):
        idx = {nm: i for i, nm in enumerate(self.names)}
        for a in self.names:
            for b in self.succ[a]: assert b in idx, (a, b)
            assert self.succ[a], a
        out = [f"parity {len(self.names) - 1};"]
        for a in self.names:
            out.append(f'{idx[a]} {self.pr[a]} {self.ow[a]} {",".join(str(idx[b]) for b in self.succ[a])} "{a}";')
        return "\n".join(out) + "\n"

    def dump(self, path):
        open(path, "w").write(self.dumps())
        return {nm: i for i, nm in enumerate(self.names)}
