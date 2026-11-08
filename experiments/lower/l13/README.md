# L-LOWER BOX L13: exact prefix gadget (tools)
- pgad.py: own code. Generalizes L-COMP box 32 gadget.py (claude/l-comp 71670ff9, experiments/comp/box32/gadget.py, sha1
  07c08c97f9d9b97c042d6e4032e10786c0c0ea09; read, not copied) to several rewired core movers XS, all core constraints, a prefix
  without fixed point, and candidate inputs R0 (default every mover that reaches no free / NOREACH mover). Encoder: L-COMP enc32,
  read-only copy ../l12/enc32_lcomp.py (sha1 a8c4f5e39f0c8cfd9a0a204bcc6248ab725000af; source claude/l-comp b63119fc).
- scan.sh: per (base, XS) and helper count k = 1..KMAX (G = the top k movers 64-k..63), prefix P; on UNSAT the first UNSAT prefix.
- Targets: core8 = ../l10/out/core8_HIT7.txt (c6e19673), S8_R2 = ../l12/out/S8_R2_core.txt (fd5b112c); equal on rows 0-20.
