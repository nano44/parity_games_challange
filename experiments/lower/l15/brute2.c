/* L-LOWER 15: exhaustive brute force of the relaxed model K at k = 2 (4 helpers): all 24 orders, all better functions (truth tables
   over the movers before each), all 16 gate vectors, all 16 starts; simulate (M3)/(M4) with o(7) = t mod 2 on rows 0..P; test
   separation of ONE client list given on stdin as lines "t r". Prints SAT with the first witness, or UNSAT. Independent of kr.py.
   Build: gcc -O2 -o brute2 brute2.c. Usage: reqpref list | brute2 P */
#include <stdio.h>
#include <stdlib.h>
int P, n, LT[600], LR[600];
int main(int argc, char **argv) {
  P = atoi(argv[1]); while (scanf("%d %d", &LT[n], &LR[n]) == 2) n++;
  int perm[24][4], np = 0;
  for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int d = 0; d < 4; d++)
    if (a != b && a != c && a != d && b != c && b != d && c != d) { perm[np][0] = a; perm[np][1] = b; perm[np][2] = c; perm[np][3] = d; np++; }
  long tried = 0;
  for (int pi = 0; pi < np; pi++) {
    int *ord = perm[pi], pos[4]; for (int i = 0; i < 4; i++) pos[ord[i]] = i;
    for (long f = 0; f < 2L * 4 * 16 * 256; f++) {
      int fs[4]; long r = f; fs[0] = r % 2; r /= 2; fs[1] = r % 4; r /= 4; fs[2] = r % 16; r /= 16; fs[3] = r;
      int func[4]; for (int i = 0; i < 4; i++) func[ord[i]] = fs[i];
      for (int gv = 0; gv < 16; gv++) for (int st = 0; st < 16; st++) {
        tried++; int s[4], S[600]; for (int y = 0; y < 4; y++) s[y] = (st >> y) & 1; S[0] = st;
        for (int t = 0; t < P; t++) {
          int bet[4];
          for (int y = 0; y < 4; y++) { int idx = 0; for (int i = 0; i < pos[y]; i++) idx = 2 * idx + s[ord[i]]; bet[y] = (func[y] >> idx) & 1; }
          int ns[4] = {s[0], s[1], s[2], s[3]}, op = (t + 1) % 2;
          for (int i = 0; i < 2; i++) {
            for (int y = 2 * i; y < 2 * i + 2; y++) if (bet[y] != s[y] && s[y] != op) ns[y] = op;
            int a = ns[2 * i], b = ns[2 * i + 1];
            op = (a != b) ? (a ^ op) : ((gv >> (2 * i + a)) & 1);
          }
          for (int y = 0; y < 4; y++) s[y] = ns[y];
          S[t + 1] = s[0] | s[1] << 1 | s[2] << 2 | s[3] << 3;
        }
        int seen[16]; for (int i = 0; i < 16; i++) seen[i] = -1; int good = 1;
        for (int i = 0; i < n && good; i++) { int st2 = S[LT[i]]; if (seen[st2] < 0) seen[st2] = LR[i]; else if (seen[st2] != LR[i]) good = 0; }
        if (good) { printf("BRUTE2 P %d SAT tried %ld order %d%d%d%d funcs %d %d %d %d gates %d start %d\n", P, tried, ord[0], ord[1], ord[2], ord[3], func[0], func[1], func[2], func[3], gv, st); return 0; }
      }
    }
  }
  printf("BRUTE2 P %d UNSAT tried %ld\n", P, tried); return 0;
}
