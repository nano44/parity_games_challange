"""L-RED box 10 (produced on Opus 5.5): tiny named-vertex game builder for hand gadgets. v(name, prio, owner) then e(a, b);
write(path) emits PGSolver format with ids in creation order."""
class GB:
    def __init__(s): s.ids, s.pr, s.ow, s.out = {}, [], [], []
    def v(s, name, pr, ow):
        assert name not in s.ids, name
        s.ids[name] = len(s.pr); s.pr.append(pr); s.ow.append(ow); s.out.append([]); return name
    def e(s, a, *bs):
        for b in bs:
            if s.ids[b] not in s.out[s.ids[a]]: s.out[s.ids[a]].append(s.ids[b])
    def write(s, path):
        with open(path, "w") as f:
            f.write(f"parity {len(s.pr) - 1};\n")
            names = {i: n for n, i in s.ids.items()}
            for i in range(len(s.pr)):
                f.write(f"{i} {s.pr[i]} {s.ow[i]} {','.join(map(str, sorted(s.out[i])))} \"{names[i]}\";\n")
