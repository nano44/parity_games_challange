#!/usr/bin/env python3
"""REFEREE-2 successor 16: sum counters over rund_check logs (one log may hold several MODE blocks). Usage: summarize.py log..."""
import sys, re
keys = ["runs", "states", "ff_runs", "ff_transitions", "PSCH_clean_checks", "FRZS_checks", "FRZS_content", "CHG_window", "CHG_charged",
        "UNF_checks", "FZ_checks", "CHU_U_events", "CHU_checks", "TG_subruns", "TG_changes", "TG_tail_changes", "TGii_rise_checks",
        "OFFb_checks", "MERGE_checks", "PDa_aligned_states", "PDa_brute_arenas", "PDb_blocks", "SPR_runs", "CRREL_freeze_checks",
        "P1_brute_states", "P2_brute_transitions", "ENGXI_checks", "FZP_checks", "KF_states_Lm1", "forbidden_pairstates_Lm1", "VIOLATIONS"]
for f in sys.argv[1:]:
    tot = {}; res = []
    for line in open(f):
        m = re.match(r"^(\w+): (\d+)$", line.strip())
        if m and m.group(1) in keys: tot[m.group(1)] = tot.get(m.group(1), 0) + int(m.group(2))
        if line.startswith("RESULT"): res.append(line.split()[1])
    print(f, "RESULTS", ",".join(sorted(set(res))), len(res), " ".join(f"{k}={tot.get(k, 0)}" for k in keys))
