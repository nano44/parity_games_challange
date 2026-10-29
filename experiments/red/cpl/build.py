"""L-RED successor 27: tiny builder. add(name, owner, prio, succs, start=None); write(pg, start). Structural vertices get low
priorities (below the sink z's odd priority Z); markers get explicit priorities above Z."""
class B:
    def __init__(self):
        self.V, self.own, self.pr, self.E, self.st = [], {}, {}, {}, {}
        self.low = 2
    def add(self, name, owner, prio=None, succ=(), start=None):
        assert name not in self.own, name
        self.V.append(name); self.own[name] = owner; self.E[name] = list(succ)
        if prio is None:
            prio = self.low; self.low += 1
        self.pr[name] = prio
        if start is not None: self.st[name] = start
    def write(self, pgp, stp=None):
        ix = {v: i for i, v in enumerate(self.V)}
        for v in self.V:
            for w in self.E[v]: assert w in ix, (v, w)
        assert len(set(self.pr.values())) == len(self.V), "priorities not distinct"
        with open(pgp, "w") as f:
            f.write(f"parity {len(self.V) - 1};\n")
            for v in self.V:
                f.write(f"{ix[v]} {self.pr[v]} {self.own[v]} {','.join(str(ix[w]) for w in self.E[v])} \"{v}\";\n")
        if stp:
            with open(stp, "w") as f:
                f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[self.st.get(v, self.E[v][0])]}" for v in self.V if self.own[v] == 0) + "\n")
                f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[self.st.get(v, self.E[v][0])]}" for v in self.V if self.own[v] == 1) + "\n")
        return ix
