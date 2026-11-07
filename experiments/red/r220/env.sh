# L-RED 55 R218: read-only worktrees (git worktree add --detach <dir> <sha>) under the session scratchpad $R218_S.
: "${R218_S:?export R218_S=<scratchpad dir holding wt191 wt192 wt190 wt190b>}"
export WT3=$R218_S/wt191      # claude/l-new f09f67ec (box 191: idealcyc, subrun191)
export WT192=$R218_S/wt192    # claude/l-new a2db977d (box 192)
export WT=$R218_S/wt190       # claude/l-new acdbd28b (box 190: n5v.py)
export WT2=$R218_S/wt190b     # claude/l-new 066cd543 (box 190: n5bxi.py)
