/* L-COMP box 47: mutants for the port check: mut47 in.txt SEED NMUT out.txt [CAPNM] -> NMUT successful gen47 mutations (every kind,
   incl. the e-numbering), validity checked after each. */
#include "gen47.h"
int main(int argc, char **argv) { static Gen g; FILE *f = fopen(argv[1], "r"); if (!f || !gread(&g, f)) return 2; fclose(f);
  grs = strtoull(argv[2], 0, 10) * 2654435761ULL + 99; int n = atoi(argv[3]), cap = argc > 5 ? atoi(argv[5]) : 100000, done = 0, tries = 0;
  while (done < n && tries < 100000) { tries++; Gen h = g; if (gmutate(&h, cap, 1) >= 0 && gvalid(&h)) { g = h; done++; } }
  f = fopen(argv[4], "w"); gwrite(&g, f); fclose(f); return done == n ? 0 : 1; }
