#!/usr/bin/env python3
"""R173: random games rich in portal pairs (an Even hub whose options are one-edge chains into a common branching vertex), for an
adversarial test of Lemma PORTAL. Usage: genportal.py N SEED OUT.pg [OUT.start]  (OUT.start: a random valid start pair)."""
import sys, random
N, seed = int(sys.argv[1]), int(sys.argv[2]); R = random.Random(seed)
own, succ = [], []
core = max(4, N // 3)
for v in range(core):                      # core: random branching vertices
    own.append(R.randint(0, 1)); succ.append(None)
while len(own) < N:                        # hubs with chain options into one or two portals
    h = len(own); own.append(0); succ.append([])
    ports = R.sample(range(core), min(core, R.choice([1, 1, 2])))
    for k in range(R.randint(2, 4)):
        if len(own) >= N: break
        prev = None; first = None
        for _ in range(R.randint(1, 3)):
            if len(own) >= N: break
            c = len(own); own.append(R.randint(0, 1)); succ.append(None)
            if prev is None: first = c
            else: succ[prev] = [c]
            prev = c
        if prev is None: break
        succ[prev] = [R.choice(ports)]; succ[h].append(first)
    if not succ[h]: succ[h] = [R.randrange(core)]
for v in range(N):
    if succ[v] is None or not succ[v]:
        succ[v] = R.sample(range(N), R.randint(2, 3)) if v < core else [R.randrange(N)]
pr = R.sample(range(2 * N), N)
with open(sys.argv[3], "w") as f:
    f.write(f"parity {N - 1};\n")
    for v in range(N): f.write(f"{v} {pr[v]} {own[v]} {','.join(map(str, sorted(set(succ[v]))))};\n")
if len(sys.argv) > 4:
    with open(sys.argv[4], "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{R.choice(sorted(set(succ[v])))}" for v in range(N) if own[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{R.choice(sorted(set(succ[v])))}" for v in range(N) if own[v] == 1) + "\n")
