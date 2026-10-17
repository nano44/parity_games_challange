#!/usr/bin/env python3
"""L-RED (box 5): L-ALG's CHAIN family, UP variant (as relayed by the Lead 23:48Z; my transcription, not L-ALG's file).
n = k + 3. a: pr 2k+1 Even-owned, edges a, b. b: pr 2k Odd-owned, edges b, z. z: pr 2k Odd-owned, edges z, x_k.
x_j (j = 1..k): pr 2(j-1), Odd-owned, edges x_j (self-loop) and x_{j-1} (x_1 -> a). Usage: chain.py k > G.pg"""
import sys
def chain(k):
    a, b, z = 0, 1, 2; x = lambda j: 2 + j
    rows = [(a, 2 * k + 1, 0, [a, b]), (b, 2 * k, 1, [b, z]), (z, 2 * k, 1, [z, x(k)])]
    for j in range(1, k + 1): rows.append((x(j), 2 * (j - 1), 1, [x(j), x(j - 1) if j > 1 else a]))
    return rows
def dumps(rows):
    return f"parity {len(rows) - 1};\n" + "".join(f"{v} {p} {o} {','.join(map(str, e))};\n" for v, p, o, e in rows)
if __name__ == "__main__":
    sys.stdout.write(dumps(chain(int(sys.argv[1]))))
