#!/bin/bash
# L-COMP box 46 item 2: win46.py on Ξ-cyclic genomes (R104's Ξ-graph has a cycle, self-loops counting). Resumable per genome.
# Usage: run46c.sh rand | frozen | big
set -u; cd "$(dirname "$0")"; export PYTHONDONTWRITEBYTECODE=1; mkdir -p out
main() {
xper() { local out="out/$1"; shift; touch "$out"
  for f in "$@"; do b=$(basename $f); grep -q "^$b " "$out" && continue
    python3 -c "import sys,json; sys.path.insert(0,'.'); import rand46; G=json.load(open(sys.argv[1])); G=G.get('genome',G); sys.exit(0 if rand46.xcyclic(G) else 1)" $f \
      && python3 win46.py $f >> "$out" 2>> "$out.err" || echo "$b Ξ-ACYCLIC skipped" >> "$out.skip"
  done; }
case "$1" in
rand) for px in 0.3 0.0; do python3 rand46.py 4611 300 60 $px out/win46_xrand.out; done
      for px in 0.3 0.0; do python3 rand46.py 4612 200 160 $px out/win46_xrand.out; done ;;
frozen) xper win46_xmine.out ../box40/inst/*.json ../box39/inst/*.json ../box41/inst/*.json ../box42/inst/CL0.json ../box42/inst/CL8.json ../box42/inst/CL16.json \
          ../box43/inst/D18_k4.json ../box43/inst/D18_k8.json ../box43/inst/D10_k16.json ../box43/inst/D80_k16.json ../box43/inst/DHIB26_k0.json \
          ../box43/inst/TMWR4.json ../box43/inst/TMWR8.json ../box43/inst/TMWR16.json ../box43/inst/TC6G8.json ../box43/inst/TREC.json ../box43/inst/TDHIB26.json ../box45/inst/TRWX.json
        xper win46_xbest.out ../box44/inst/FROZEN44_*.json ../box44/out/climb44/BEST_*.json ../box45/out/climb45/BEST_*.json ;;
big) xper win46_xbig.out ../box42/inst/CL30.json ../box42/inst/CL45.json ../box43/inst/D18_k16.json ../box43/inst/D10_k32.json ../box43/inst/D80_k32.json ../box43/inst/TMWR32.json \
       ../box43/inst/MWR32_2.json ../box42/inst/CL90.json ../box43/inst/D10_k64.json ../box43/inst/D80_k64.json ../box43/inst/D18_k32.json ;;
*) echo usage; exit 2 ;;
esac
echo "run46c $1 done"
}
main "$@"
