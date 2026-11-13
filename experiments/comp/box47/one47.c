/* L-COMP box 47: CLI of the 1P(G) port (one47.h). Usage: one47 genome.txt [RULE] [--states] [--sw]  (RULE key | howard | seq; default: all three)
   Prints «key T howard T seq T»; with --sw, after each rule one line «SW <rule> <mover> <level> <sw>» per mover; with --states, one line per state of each rule: «S <rule> <t> s_0 .. s_(N-1)». */
#include "gen47.h"
#include "one47.h"
int main(int argc, char **argv) {
  static Gen g; FILE *f = fopen(argv[1], "r"); if (!f || !gread(&g, f)) { fprintf(stderr, "bad genome\n"); return 2; } fclose(f);
  if (!gvalid(&g)) { fprintf(stderr, "genome invalid or Xi-cyclic\n"); return 2; }
  int st = 0, sws = 0; const char *only = 0; for (int a = 2; a < argc; a++) { if (!strcmp(argv[a], "--states")) st = 1; else if (!strcmp(argv[a], "--sw")) sws = 1; else only = argv[a]; }
  const char *nm[3] = { "key", "howard", "seq" }; long cap = 200000000; static long SWC[GMAXN];
  if (st) o_states = malloc(sizeof(int) * (size_t)g.N * (cap + 1 < 200001 ? cap + 1 : 200001));
  for (int r = 0; r < 3; r++) { if (only && strcmp(only, nm[r])) continue; long T = run_rule(&g, st ? 200000 : cap, sws ? SWC : 0, r); printf("%s %ld ", nm[r], T);
    if (sws) { printf("\n"); for (int x = 0; x < g.N; x++) printf("SW %s %d %d %ld\n", nm[r], x, g.lev[x], SWC[x]); }
    if (st) { printf("\n"); for (long t = 0; t < o_nstates; t++) { printf("S %s %ld", nm[r], t); for (int x = 0; x < g.N; x++) printf(" %d", o_states[t * g.N + x]); printf("\n"); } } }
  printf("\n"); return 0; }
