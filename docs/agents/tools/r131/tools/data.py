#!/usr/bin/env python3
"""tools/data.py: the DATA numbers of the R131 draft, read from the lane's pinned outputs at the l-red-b commit of
cfg.json (datafacts.facts), each printed as a check; one negative control (the k = 13 line with one digit changed
must fail its check). Exit 1 on any failure."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import datafacts
import lib131


def main():
    cfg = lib131.load_cfg()
    F, C = datafacts.facts(cfg)
    bad = 0
    for name, ok, detail in C:
        print("%s %s: %s" % ("OK  " if ok else "FAIL", name, detail))
        bad += not ok
    # negative control
    real = datafacts.show

    def fake(commit, path):
        b = real(commit, path)
        if path.endswith("out/n5_k13.out"):
            b = b.replace(b" its 8193 ", b" its 8194 ")
        return b

    datafacts.show = fake
    try:
        _, C2 = datafacts.facts(cfg)
        fired = [n for n, ok, _ in C2 if not ok]
    finally:
        datafacts.show = real
    ctrl = "n5_k13.out" in fired
    print("negative control (its 8193 read as 8194 in n5_k13.out): failing checks %s: fires %s" % (fired, ctrl))
    print("data: %d checks, %d failed; %s" % (len(C), bad, "PASS" if bad == 0 and ctrl else "FAILED"))
    return 0 if bad == 0 and ctrl else 1


if __name__ == "__main__":
    sys.exit(main())
