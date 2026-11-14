/* L-LOWER 5 fev.c: batch evaluator (T, F, moves) of text genomes; core from experiments/lower/l4/rclimb.c */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 64
int d,N; int xt[MAXN*2], br[MAXN*2], bp[MAXN*2], gate[MAXN*2], st[MAXN]; int fixo[MAXN*2];
static unsigned long long rs=88172645463325252ULL; static unsigned long long rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return rs;}
static int ord_[MAXN], vis[MAXN];
static int dfs(int x){ if(vis[x]==2) return 1; if(vis[x]==1) return 0; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0 && !dfs(y)) return 0;} vis[x]=2; return 1; }
static int no; static void topo(int x){ if(vis[x]) return; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0) topo(y);} ord_[no++]=x; }
static int acyclic(){ memset(vis,0,sizeof vis); for(int x=0;x<N;x++) if(!dfs(x)) return 0; memset(vis,0,sizeof vis); no=0; for(int x=0;x<N;x++) topo(x); return 1; }
static int F[MAXN], MV[MAXN];
typedef __int128 VT; static VT bv(int m){ VT b=((VT)1)<<br[m]; return bp[m]? -b : b; }
static int run(int *Tout){ int s[MAXN], ns[MAXN]; VT v[MAXN]; memcpy(s,st,sizeof(int)*N); memset(F,0,sizeof F); memset(MV,0,sizeof MV);
  int T=0; int oprev[MAXN]; int have=0;
  for(;T<5000;){ for(int i=0;i<N;i++){int x=ord_[i]; int m=2*x+s[x]; v[x]=bv(m)+(xt[m]>=0? v[xt[m]]:0);}
    int av[MAXN]; int any=0; for(int x=0;x<N;x++){ int m=2*x+1-s[x]; VT ov=bv(m)+(xt[m]>=0? v[xt[m]]:0); av[x]= ov>v[x]; any|=av[x]; }
    if(!any) break;
    int c=0, o[MAXN];
    for(int l=0;l<d;l++){ for(int q=0;q<2;q++){ int x=2*l+q; ns[x]=s[x];
        if(l==0){ if(av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x]=1-s[x]; }
        else if(av[x] && s[x]!=c) ns[x]=c; }
      if(l==0) o[0] = gate[2*0+ns[0]] > gate[2*1+ns[1]];
      else { int a=ns[2*l], b=ns[2*l+1]; o[l] = (a!=b)? (a!=c) : (gate[2*(2*l)+a] > gate[2*(2*l+1)+a]); }
      c=o[l]; }
    int ch=0; for(int x=0;x<N;x++) if(ns[x]!=s[x]){ch=1; MV[x]++;} if(!ch) break;
    if(!have){ /* o at s_0 */ int c0=0, o0[MAXN]; for(int l=0;l<d;l++){ if(l==0) o0[0]=gate[0+s[0]]>gate[2+s[1]]; else {int a=s[2*l],b=s[2*l+1]; o0[l]=(a!=b)?(a!=c0):(gate[4*l+a]>gate[4*l+2+a]);} c0=o0[l]; } memcpy(oprev,o0,sizeof(int)*d); have=1; }
    for(int l=0;l<d;l++){ if(o[l]!=oprev[l]) F[l]++; oprev[l]=o[l]; }
    memcpy(s,ns,sizeof(int)*N); T++; }
  *Tout=T; return T; }
static void rd(const char*fn){ FILE*f=fopen(fn,"r"); char w[64]; while(fscanf(f,"%63s",w)==1){ int n=0;
    if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d)!=1) exit(1); N=2*d; continue; }
    int *a = !strcmp(w,"xt")?xt: !strcmp(w,"br")?br: !strcmp(w,"bp")?bp: !strcmp(w,"gate")?gate: !strcmp(w,"start")?st:NULL; if(!a) continue;
    n = !strcmp(w,"start")? N : 2*N; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) exit(1); } fclose(f); }

/* L-LOWER 5: evaluator. Reads text genomes (blocks d/xt/br/bp/gate/start; a line "end" or EOF ends a block) from the files given,
   prints one line per file: T and F(0..d-1). Simulator core copied verbatim from l4/rclimb.c (same rules as l3/sim.py). */
int main(int argc,char**argv){ for(int a=1;a<argc;a++){ rd(argv[a]); if(!acyclic()){ printf("CYCLIC\n"); continue; }
  int T; run(&T); printf("T %d F",T); for(int l=0;l<d;l++) printf(" %d",F[l]); printf(" MV"); for(int x=0;x<N;x++) printf(" %d",MV[x]); printf("\n"); } return 0; }
