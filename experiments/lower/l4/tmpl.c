/* L-LOWER 4: exhaustive search over UNIFORM (period-1) crossed driven-block templates. Every pair j >= 1: 2j -> (2j-2, 2j-1),
   2j+1 -> (2j-1, 2j-2); pair 0 -> X. Per template: parities of the 4 options (16), kappa (4), band direction (ranks of level j
   above (dir 0) or below (dir 1) all lower levels), order of the 4 options inside the band (24). LP = longest moving path over
   all starts and all exogenous key sequences (drv.c rules, copied). Output: per m the best LP and the templates attaining it. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXM 9
int m,N; int xt[2*MAXM][2], rk[2*MAXM][2], par[2*MAXM][2], kap[MAXM][2];
static void vals(int s, long long *v){ for(int x=0;x<N;x++){int k=(s>>x)&1; long long b=(1LL<<rk[x][k]); if(par[x][k]) b=-b; v[x]=b+(xt[x][k]>=0? v[xt[x][k]]:0);} }
static long long optv(long long *v,int x,int k){ long long b=(1LL<<rk[x][k]); if(par[x][k]) b=-b; return b+(xt[x][k]>=0?v[xt[x][k]]:0);}
static int step(int s,int e){ long long v[2*MAXM]; vals(s,v); int ns=s; int c=e;
  for(int j=0;j<m;j++){ for(int q=0;q<2;q++){int x=2*j+q; int k=(s>>x)&1; if(k!=c && optv(v,x,1-k)>v[x]) ns^=1<<x;}
    int a=(ns>>(2*j))&1, b=(ns>>(2*j+1))&1; c = (a!=b)? (a!=c) : kap[j][a]; }
  return ns; }
static int memo[1<<(2*MAXM)];
static int lp(int s){ if(memo[s]>=0) return memo[s]; int best=0; for(int e=0;e<2;e++){int ns=step(s,e); if(ns!=s){int r=1+lp(ns); if(r>best)best=r;}} return memo[s]=best; }
static const int perms[24][4]={{0,1,2,3},{0,1,3,2},{0,2,1,3},{0,2,3,1},{0,3,1,2},{0,3,2,1},{1,0,2,3},{1,0,3,2},{1,2,0,3},{1,2,3,0},{1,3,0,2},{1,3,2,0},{2,0,1,3},{2,0,3,1},{2,1,0,3},{2,1,3,0},{2,3,0,1},{2,3,1,0},{3,0,1,2},{3,0,2,1},{3,1,0,2},{3,1,2,0},{3,2,0,1},{3,2,1,0}};
int main(int argc,char**argv){ int M1=atoi(argv[1]), M2=atoi(argv[2]);
  for(m=M1;m<=M2;m++){ N=2*m; int best=0, cnt=0; int bt[16];
    for(int P=0;P<16;P++) for(int K=0;K<4;K++) for(int D=0;D<2;D++) for(int O=0;O<24;O++){
      for(int j=0;j<m;j++){ for(int q=0;q<2;q++){int x=2*j+q; if(j==0){xt[x][0]=xt[x][1]=-1;} else {xt[x][0]=2*j-2+q; xt[x][1]=2*j-1-q;}
          for(int k=0;k<2;k++){ int o=2*q+k; par[x][k]=(P>>o)&1; int band = D==0? j : (m-1-j); rk[x][k]=4*band+perms[O][o]; } }
        kap[j][0]=K&1; kap[j][1]=(K>>1)&1; }
      int S=1<<N; for(int i=0;i<S;i++)memo[i]=-1; int b=0; for(int s=0;s<S;s++){int r=lp(s); if(r>b)b=r;}
      if(b>best){best=b;cnt=0;} if(b==best){ if(cnt<1){bt[0]=P;bt[1]=K;bt[2]=D;bt[3]=O;} cnt++; } }
    printf("m %d bestLP %d templates %d e.g. P %d K %d D %d O %d\n",m,best,cnt,bt[0],bt[1],bt[2],bt[3]); fflush(stdout); }
  return 0; }
