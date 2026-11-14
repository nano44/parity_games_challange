"""PGSolver-format parity games: parse, write, solution files. Max-parity convention (TARGET.md section 1):
owner 0 = Even, owner 1 = Odd; Even wins a play iff the highest priority seen infinitely often is even."""
import re


class Game:
    def __init__(self, prio, owner, succ, labels=None):
        self.prio, self.owner, self.succ = list(prio), list(owner), [list(s) for s in succ]
        self.labels = labels
        self.n = len(self.prio)
        assert len(self.owner) == self.n == len(self.succ)
        for v, s in enumerate(self.succ):
            if not s:
                raise ValueError(f"vertex {v} has no successor")
            for w in s:
                if not 0 <= w < self.n:
                    raise ValueError(f"edge {v}->{w} out of range")
        self.pred = [[] for _ in range(self.n)]
        for v, s in enumerate(self.succ):
            for w in set(s):
                self.pred[w].append(v)

    @property
    def m(self):
        return sum(len(set(s)) for s in self.succ)


_line = re.compile(r'^\s*(\d+)\s+(\d+)\s+([01])\s+([\d,\s]+?)(\s+"[^"]*")?\s*;?\s*$')


def parse(text):
    """Parse PGSolver format. Vertex ids must be exactly 0..n-1 (any order); the header value is ignored."""
    rows = {}
    for raw in text.replace(";\n", "\n").splitlines():
        line = raw.strip()
        if not line or line.startswith("parity") or line.startswith("start"):
            continue
        # PGSolver allows several statements per line separated by ';'
        for stmt in line.split(";"):
            stmt = stmt.strip()
            if not stmt or stmt.startswith("parity") or stmt.startswith("start"):
                continue
            mt = _line.match(stmt)
            if not mt:
                raise ValueError(f"cannot parse line: {raw!r}")
            v, p, o = int(mt.group(1)), int(mt.group(2)), int(mt.group(3))
            succ = [int(x) for x in mt.group(4).replace(" ", "").split(",") if x]
            if v in rows:
                raise ValueError(f"duplicate vertex {v}")
            rows[v] = (p, o, succ, (mt.group(5) or "").strip().strip('"') or None)
    n = len(rows)
    if sorted(rows) != list(range(n)):
        raise ValueError("vertex ids are not 0..n-1")
    return Game([rows[v][0] for v in range(n)], [rows[v][1] for v in range(n)],
                [rows[v][2] for v in range(n)], [rows[v][3] for v in range(n)])


def read(path):
    with open(path) as f:
        return parse(f.read())


def dumps(g):
    out = [f"parity {g.n - 1};"]
    for v in range(g.n):
        lab = f' "{g.labels[v]}"' if g.labels and g.labels[v] else ""
        out.append(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))}{lab};")
    return "\n".join(out) + "\n"


def write(g, path):
    with open(path, "w") as f:
        f.write(dumps(g))


def write_sol(winner, path, strategy=None):
    """Oink/PGSolver solution format: 'paritysol N;' then 'v winner [strategy];'."""
    with open(path, "w") as f:
        f.write(f"paritysol {len(winner)};\n")
        for v, w in enumerate(winner):
            s = "" if strategy is None or strategy[v] is None else f" {strategy[v]}"
            f.write(f"{v} {w}{s};\n")


def read_sol(text, n):
    """Return winner list (0 Even / 1 Odd) from a solution text; raises if any vertex is missing."""
    win = [None] * n
    for line in text.splitlines():
        line = line.strip().rstrip(";").strip()
        if not line or line.startswith("paritysol"):
            continue
        parts = line.split()
        v, w = int(parts[0]), int(parts[1])
        win[v] = w
    miss = [v for v in range(n) if win[v] not in (0, 1)]
    if miss:
        raise ValueError(f"solution misses {len(miss)} vertices, e.g. {miss[:5]}")
    return win
