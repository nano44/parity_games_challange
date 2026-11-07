/* L-SI box 69: ABSTRACT m = 2 external-flip model (superset of ISO R197 ladders, docs/si/N5-MECH-box69.md §1).
   Upper movers 0 = A1, 1 = B1 (level 1), 2 = A2, 3 = B2 (level 2). State s = 4 bits (bit z = option of mover z).
   Data: an order pi of the 4 movers and, for each mover z, its better option C_z(s) as an ARBITRARY function of the states of the movers
   with larger pi (TRIANGULAR: R106's combing; no ENC realisability); bits c1(0), c1(1) (BIT-CHAIN: b1 when both level-1 movers sit on
   option k); external bit b0. Step (BIT-CHAIN form of R104): level 1 with kp1 = (b0 ? 0 : 1): z moves iff C_z(s) != s_z and C_z(s) == kp1
   (C from the OLD state); then b1 = b0 if (A1,B1) = (0,1), !b0 if (1,0), c1(k) if (k,k) (NEW state); level 2 the same with kp2 = (b1 ? 0 : 1).
   Computes per system: T0 = max flip-free run, T1 = max run with <= 1 flip, and the set of (pre, post) pairs; prints maxima over all
   systems, the (pre, post) set, the (T0, T1) table and one witness per new (T0, T1) cell.  Usage: abs2 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
static int perm[24][4], np = 0;
static int Cf[4][16];      /* C_z(s) */
static int c10, c11;
static int stepf(int s, int b0) {
  int a1 = s & 1, b1s = (s >> 1) & 1, ns = s;
  int kp1 = b0 ? 0 : 1;
  for (int z = 0; z < 2; z++) { int cz = Cf[z][s], sz = (s >> z) & 1; if (cz != sz && cz == kp1) ns ^= 1 << z; }
  int na = ns & 1, nb = (ns >> 1) & 1, b1;
  if (na == 0 && nb == 1) b1 = b0; else if (na == 1 && nb == 0) b1 = !b0; else b1 = na ? c11 : c10;
  int kp2 = b1 ? 0 : 1;
  for (int z = 2; z < 4; z++) { int cz = Cf[z][s], sz = (s >> z) & 1; if (cz != sz && cz == kp2) ns ^= 1 << z; }
  (void)a1; (void)b1s; return ns; }
int main(void) {
  for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int d = 0; d < 4; d++)
    if (a!=b&&a!=c&&a!=d&&b!=c&&b!=d&&c!=d) { perm[np][0]=a; perm[np][1]=b; perm[np][2]=c; perm[np][3]=d; np++; }
  static int seenP[20][20]; static int tab[20][20]; static char wit[20][20][200];
  int bestT0 = 0, bestT1 = 0; long nsys = 0;
  for (int p = 0; p < np; p++) {
    int *o = perm[p]; /* o[0] has the largest pi: C constant; o[1] depends on o[0]; o[2] on o[0], o[1]; o[3] on o[0..2] */
    for (long code = 0; code < 2L * 4 * 16 * 256; code++) {
      long r = code; int f0 = r % 2; r /= 2; int f1 = r % 4; r /= 4; int f2 = r % 16; r /= 16; int f3 = (int)r;
      for (int s = 0; s < 16; s++) {
        int x0 = (s >> o[0]) & 1, x1 = (s >> o[1]) & 1, x2 = (s >> o[2]) & 1;
        Cf[o[0]][s] = f0; Cf[o[1]][s] = (f1 >> x0) & 1; Cf[o[2]][s] = (f2 >> (x0 + 2 * x1)) & 1; Cf[o[3]][s] = (f3 >> (x0 + 2 * x1 + 4 * x2)) & 1; }
      for (int cc = 0; cc < 4; cc++) { c10 = cc & 1; c11 = cc >> 1; nsys++;
        int nx[16][2], L[16][2];
        for (int s = 0; s < 16; s++) for (int b = 0; b < 2; b++) nx[s][b] = stepf(s, b);
        for (int s = 0; s < 16; s++) for (int b = 0; b < 2; b++) { int u = s, n = 0; while (nx[u][b] != u && n < 64) { u = nx[u][b]; n++; } L[s][b] = n; }
        int T0 = 0, T1 = 0;
        for (int s = 0; s < 16; s++) for (int b = 0; b < 2; b++) { if (L[s][b] > T0) T0 = L[s][b];
          int u = s, t = 0;
          for (;;) { int post = L[u][!b]; if (!seenP[t][post]) { seenP[t][post] = 1; }
            if (t + post > T1) T1 = t + post; if (nx[u][b] == u) break; u = nx[u][b]; t++; } }
        if (T0 > 19 || T1 > 19) { printf("RUN TOO LONG (cycle?)\n"); return 3; }
        if (!tab[T0][T1]) { snprintf(wit[T0][T1], 200, "pi %d%d%d%d f %d %d %d %d c1 %d %d", o[0], o[1], o[2], o[3], f0, f1, f2, f3, c10, c11); }
        tab[T0][T1]++;
        if (getenv("DUMPBAD") && T1 >= 6) { unsigned long long C = 0; for (int s = 0; s < 16; s++) for (int z = 0; z < 4; z++) if (Cf[z][s]) C |= 1ULL << (s * 4 + z);
          printf("BAD %llx %d %d T0 %d T1 %d\n", C, c10, c11, T0, T1); }
        if (T0 > bestT0) bestT0 = T0; if (T1 > bestT1) bestT1 = T1; } } }
  printf("ABSTRACT m=2 systems %ld  max T0 %d  max T1 %d\n", nsys, bestT0, bestT1);
  for (int a = 0; a < 20; a++) for (int c = 0; c < 20; c++) if (seenP[a][c]) printf("PAIR pre %d post %d\n", a, c);
  for (int a = 0; a < 20; a++) for (int c = 0; c < 20; c++) if (tab[a][c]) printf("CELL T0 %d T1 %d count %d witness %s\n", a, c, tab[a][c], wit[a][c]);
  return 0; }
