#!/usr/bin/env python3
"""Box 33: the inherited lev / coarse (experiments/si/coarse/mono.py) use 99 as the level ∞, so on games with n >= 100 a rank >= 99
reads as ∞. Import this module FIRST: it replaces mono.lev / mono.coarse by versions with ∞ = 10**6 before any box32 tool binds them.
Usage: python3 biglev.py tool.py args...   (runs the tool with the patch)"""
import sys, os, runpy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
import mono
INF = 10 ** 6
def lev(a, b):
    if a[0] != b[0]: return INF
    d = a[1] ^ b[1]
    if not d: return -1 if a[2] != b[2] else -2
    return d.bit_length() - 1
def coarse(val, L):
    if L >= INF: return ()
    return (val[0], val[1] >> (L + 1)) if L >= -1 else (val[0], val[1], val[2])
mono.lev, mono.coarse = lev, coarse
if __name__ == "__main__":
    tool = sys.argv[1]; sys.argv = sys.argv[1:]; sys.path.insert(0, os.path.dirname(os.path.abspath(tool)))
    src = open(tool).read().replace("< 99", "< 10 ** 6").replace(">= 99", ">= 10 ** 6")
    code = compile(src, tool, "exec"); g = {"__name__": "__main__", "__file__": tool}; exec(code, g)
