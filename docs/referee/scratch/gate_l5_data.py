"""REFEREE s34: read the numbers L-5 cites, by column name, from the frozen L-SI outputs (git show REV:path). Usage: gate_l5_data.py"""
import subprocess
def rows(rev, path):
    t = subprocess.run(["git", "show", f"{rev}:experiments/si/{path}"], capture_output=True, text=True, check=True).stdout
    hdr = None; out = []
    for l in t.splitlines():
        w = l.split()
        if w[:2] == ["engine", "g3"] or w[:2] == ["engine", "own"]: hdr = w; eng = w[1]; continue
        # header «engine ENG col1 col2 ...»; a data row «ENG v1 v2 ...» has one token fewer
        if hdr and len(w) == len(hdr) - 1 and w[0] == eng: out.append(dict(zip(hdr[2:], w[1:]), engine=eng))
        elif hdr: hdr = None
    return out
def show(rev, path, insts, cols):
    for r in rows(rev, path):
        if r["instance"] in insts: print(rev[:8], path, r["engine"], r["instance"], " ".join(f"{c}={r[c]}" for c in cols))
show("2d0344d3", "box90/out/mw90.out", {"MW8_2.json", "MW32_2.json"}, ["C", "maxm"])
show("4ded1e8d", "box90/out/fw90.out", {"FW8_2.json", "FW16_2.json"}, ["C", "maxP", "depth"])
show("2051a0ee", "box91/out/own91.out", {"MW8_2.json", "MW32_2.json"}, ["C", "maxflip", "maxa"])
show("2051a0ee", "box91/out/g391.out", {"MW8_2.json", "MW32_2.json"}, ["C", "maxflip", "maxa"])
for f in ["box93/out/mwr93_own.out", "box93/out/mwr93_g3.out"]:
    show("2051a0ee", f, {"MWR4_2.json", "MWR8_2.json", "MWR16_2.json"}, ["mx_flips", "mx_ch_D", "mx_ch_pe", "mx_ch_pb", "mx_lam_pe", "mx_lam_pb", "dfail"])
for p in ["box90/out/mw90.out", "box90/out/fw90.out", "box91/out/own91.out", "box91/out/g391.out", "box93/out/mwr93_own.out", "box93/out/mwr93_g3.out"]:
    a = subprocess.run(["git", "diff", "--quiet", "2d0344d3" if "mw90" in p else ("4ded1e8d" if "fw90" in p else "2051a0ee"), "2051a0ee", "--", "experiments/si/" + p]).returncode
    print("unchanged to 2051a0ee", p, a == 0)
F = [0, 1]
for _ in range(20): F.append(F[-1] + F[-2])
print("F_10 - 1 =", F[10] - 1, " F_18 - 1 =", F[18] - 1)
