"""L-RED box 24 (produced on Opus 5.5): delay lane on one Even node of a game (original game; the dual is what R2 pivots on).
lanegen.py G.pg V L [ZPRIO|none] [LPRIO] [TARGET] [closed] > OUT.pg
TARGET (default: V's second successor) is the inward target y, the other successor is the exit x. With 'closed' every lane node
starts on its inward arc (inward successor listed first, so kl2's tau_1 takes it); default: exit first (lane open at the start).
Node V with successors [x (first = exit), y (second = inward target)] becomes the far end of a lane of L nodes:
  l_1: [x, y];  l_j: [x, z_j] with z_j -> l_{j-1} (j = 2..L-1);  V: [x, z_L] with z_L -> l_{L-1}.
l_j: owner Even (dual Odd = R2's improver), priority LPRIO (default 1). z_j: owner Odd, single successor, priority ZPRIO;
with 'none' the z nodes are omitted (plain lane: l_j -> l_{j-1}, V -> l_{L-1}). L = 1 returns G unchanged.
Reading (R56 §2): in the dual, z is a truncation at ZPRIO + 1; a z above the exit's lap rise and below the counted component makes
the chain lose to the direct exit after the exit rises, so the lane resets fully each lap (M2 fix)."""
import sys
sys.path.insert(0, __import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), "..", "..", "harness"))
import pg  # noqa: E402

g = pg.read(sys.argv[1]); V = int(sys.argv[2]); L = int(sys.argv[3])
zp = sys.argv[4] if len(sys.argv) > 4 else "none"; lp = int(sys.argv[5]) if len(sys.argv) > 5 else 1
assert g.owner[V] == 0 and len(g.succ[V]) == 2
x, y = g.succ[V]
if len(sys.argv) > 6 and sys.argv[6] != "-":
    y = int(sys.argv[6]); x = [w for w in g.succ[V] if w != y][0]
closed = len(sys.argv) > 7 and sys.argv[7] == "closed"
ordr = (lambda ex, inw: [inw, ex]) if closed else (lambda ex, inw: [ex, inw])
prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]


def new(p, o, s):
    prio.append(p); owner.append(o); succ.append(s); return len(prio) - 1


if L > 1:
    prev = new(lp, 0, ordr(x, y))                 # l_1
    for j in range(2, L + 1):
        tgt = prev if zp == "none" else new(int(zp), 1, [prev])
        if j < L:
            prev = new(lp, 0, ordr(x, tgt))
        else:
            succ[V] = ordr(x, tgt)
print(f"parity {len(prio) - 1};")
for v in range(len(prio)):
    print(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};")
