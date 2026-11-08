/* L-LOWER 9 fenc.c: exact evaluator (T, F, moves) of text genomes for any d <= 64, written from l6/sim6.py's rules but deciding each
   preference by ENC (R105): the sign of the option of largest rank in chain(x,0) xor chain(x,1) (distinct ranks), so no big
   integers are needed (l5/fev.c uses __int128 sums, which overflow once ranks reach 127, i.e. at d >= 32). Independent of sim6.py
   (which sums Python big integers). Usage: fenc G1.txt [G2.txt ...] -> "T t F f0 .. f(d-1) MV m0 .. m(2d-1)" per file.
   Env TRAJ=1: also print the state string per step. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXN 128
int d, N; int xt[2*MAXN], br[2*MAXN], bp[2*MAXN], gate[2*MAXN], st[MAXN];
static int vis[MAXN];
static int dfs(int x){ if(vis[x]==2) return 1; if(vis[x]==1) return 0; vis[x]=1; for(int k=0;k<2;k++){int y=xt[2*x+k]; if(y>=0 && !dfs(y)) return 0;} vis[x]=2; return 1; }
static int acyclic(void){ memset(vis,0,sizeof vis); for(int x=0;x<N;x++) if(!dfs(x)) return 0; return 1; }
static int tag[2*MAXN];
static int pref(const int *s, int x){
  int mk[2][MAXN+1], n[2]={0,0};
  for(int k=0;k<2;k++){ int y=x, j=k; for(;;){ int m=2*y+j; mk[k][n[k]++]=m; tag[m]|=(1<<k); y=xt[m]; if(y<0) break; j=s[y]; } }
  int top=-1, tm=-1;
  for(int k=0;k<2;k++) for(int i=0;i<n[k];i++){ int m=mk[k][i]; if(tag[m]!=3 && br[m]>top){ top=br[m]; tm=m; } }
  int side = (tag[tm]==1)? 0 : 1;
  for(int k=0;k<2;k++) for(int i=0;i<n[k];i++) tag[mk[k][i]]=0;
  return bp[tm]? 1-side : side;
}
static int okey(const int *s, int l, int c){ if(l==0) return gate[0+s[0]] > gate[2+s[1]];
  int a=s[2*l], b=s[2*l+1]; return (a!=b)? (a!=c) : (gate[4*l+a] > gate[4*l+2+a]); }
static void rd(const char*fn){ FILE*f=fopen(fn,"r"); if(!f){perror(fn); exit(1);} char w[64];
  while(fscanf(f,"%63s",w)==1){ if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d)!=1) exit(1); N=2*d; continue; }
    int *a = !strcmp(w,"xt")?xt: !strcmp(w,"br")?br: !strcmp(w,"bp")?bp: !strcmp(w,"gate")?gate: !strcmp(w,"start")?st:NULL; if(!a) continue;
    int n = !strcmp(w,"start")? N : 2*N; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) exit(1); } fclose(f); }
int main(int argc,char**argv){ int traj = getenv("TRAJ")!=NULL;
  for(int a=1;a<argc;a++){ rd(argv[a]); if(!acyclic()){ printf("CYCLIC\n"); continue; }
    int s[MAXN], ns[MAXN], av[MAXN], F[MAXN]={0}, MV[MAXN]={0}, o[MAXN], on[MAXN]; memcpy(s,st,sizeof(int)*N);
    int c=0; for(int l=0;l<d;l++){ o[l]=okey(s,l,c); c=o[l]; }
    int T=0;
    for(;T<100000;){ int any=0; for(int x=0;x<N;x++){ av[x] = pref(s,x)!=s[x]; any|=av[x]; } if(!any) break;
      c=0; for(int l=0;l<d;l++){ for(int q=0;q<2;q++){ int x=2*l+q; ns[x]=s[x];
          if(l==0){ if(av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x]=1-s[x]; } else if(av[x] && s[x]!=c) ns[x]=c; }
        on[l]=okey(ns,l,c); c=on[l]; }
      int ch=0; for(int x=0;x<N;x++) if(ns[x]!=s[x]){ ch=1; MV[x]++; } if(!ch) break;
      for(int l=0;l<d;l++){ if(on[l]!=o[l]) F[l]++; o[l]=on[l]; }
      memcpy(s,ns,sizeof(int)*N); T++;
      if(traj){ printf("%d ",T); for(int x=0;x<N;x++) putchar('0'+s[x]); putchar('\n'); } }
    printf("T %d F",T); for(int l=0;l<d;l++) printf(" %d",F[l]); printf(" MV"); for(int x=0;x<N;x++) printf(" %d",MV[x]); printf("\n"); }
  return 0; }
