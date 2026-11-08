/* L-LOWER 12 (BOX L12 (a), ROOM CLIMB): climb a capped genome's wiring / ranks / signs / gates / start, keeping levels 0..H-2 exactly
   capped (F(l) = 2^(l+2) - 2 for l < H-1; simulation = l9/fenc.c's ENC rules, exact for d <= 64), to MINIMISE the adjacency score
   A = number of pairs of consecutive o(H-2) changes at adjacent CORE steps (core step = a step at which a mover of pairs 0..H-2
   moves). A drives the level-H retrigger bill floor (docs/lower/L12-slack.md §2). Tie-break: smaller T. Simulated annealing on A.
   Usage: room GENOME OUT H SEED SECONDS TEMP  (resumes from OUT if it exists; writes OUT on every new best; prints progress). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#define MAXN 128
int d, N, H; int xt[2*MAXN], br[2*MAXN], bp[2*MAXN], gate[2*MAXN], st[MAXN];
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
static int rd(const char*fn){ FILE*f=fopen(fn,"r"); if(!f) return 0; char w[64];
  while(fscanf(f,"%63s",w)==1){ if(!strcmp(w,"d")){ if(fscanf(f,"%d",&d)!=1) return 0; N=2*d; continue; }
    int *a = !strcmp(w,"xt")?xt: !strcmp(w,"br")?br: !strcmp(w,"bp")?bp: !strcmp(w,"gate")?gate: !strcmp(w,"start")?st:NULL; if(!a) continue;
    int n = !strcmp(w,"start")? N : 2*N; for(int i=0;i<n;i++) if(fscanf(f,"%d",&a[i])!=1) return 0; } fclose(f); return 1; }
static void wr(const char*fn){ char tmp[600]; snprintf(tmp,sizeof tmp,"%s.tmp",fn); FILE*f=fopen(tmp,"w");
  fprintf(f,"d %d\nxt",d); for(int i=0;i<2*N;i++) fprintf(f," %d",xt[i]); fprintf(f,"\nbr"); for(int i=0;i<2*N;i++) fprintf(f," %d",br[i]);
  fprintf(f,"\nbp"); for(int i=0;i<2*N;i++) fprintf(f," %d",bp[i]); fprintf(f,"\ngate"); for(int i=0;i<2*N;i++) fprintf(f," %d",gate[i]);
  fprintf(f,"\nstart"); for(int i=0;i<N;i++) fprintf(f," %d",st[i]); fprintf(f,"\n"); fclose(f); rename(tmp,fn); }
/* evaluate: returns 0 if levels 0..H-2 not exactly capped; else sets *A, *T, *nch */
static int eval(int *A, int *Tout, int *nch){
  if(!acyclic()) return 0;
  int s[MAXN], ns[MAXN], av[MAXN], F[MAXN]={0}, o[MAXN], on[MAXN]; memcpy(s,st,sizeof(int)*N);
  int c=0; for(int l=0;l<d;l++){ o[l]=okey(s,l,c); c=o[l]; }
  int T=0, core=0, lastch=-5, adj=0, ch6=0, K=2*(H-1);
  for(;T<20000;){ int any=0; for(int x=0;x<N;x++){ av[x]=pref(s,x)!=s[x]; any|=av[x]; } if(!any) break;
    c=0; for(int l=0;l<d;l++){ for(int q=0;q<2;q++){ int x=2*l+q; ns[x]=s[x];
        if(l==0){ if(av[x] && gate[2*x+1-s[x]] < gate[2*x+s[x]]) ns[x]=1-s[x]; } else if(av[x] && s[x]!=c) ns[x]=c; }
      on[l]=okey(ns,l,c); c=on[l]; }
    int chg=0, cm=0; for(int x=0;x<N;x++) if(ns[x]!=s[x]){ chg=1; if(x<K) cm=1; } if(!chg) break;
    for(int l=0;l<d;l++){ if(on[l]!=o[l]) F[l]++; } 
    if(cm){ core++; if(on[H-2]!=o[H-2]){ ch6++; if(lastch==core-1) adj++; lastch=core; } }
    for(int l=0;l<d;l++) o[l]=on[l];
    memcpy(s,ns,sizeof(int)*N); T++;
    for(int l=0;l<H-1;l++) if(F[l] > (1<<(l+2))-2) return 0; }
  for(int l=0;l<H-1;l++) if(F[l] != (1<<(l+2))-2) return 0;
  *A=adj; *Tout=T; *nch=ch6; return 1; }
static unsigned long long rs=88172645463325252ULL;
static unsigned long long rnd(void){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
static double urand(void){ return (rnd()>>11)*(1.0/9007199254740992.0); }
typedef struct { int xt[2*MAXN], br[2*MAXN], bp[2*MAXN], gate[2*MAXN], st[MAXN]; } G;
static void save(G*g){ memcpy(g->xt,xt,sizeof xt); memcpy(g->br,br,sizeof br); memcpy(g->bp,bp,sizeof bp); memcpy(g->gate,gate,sizeof gate); memcpy(g->st,st,sizeof st); }
static void load(G*g){ memcpy(xt,g->xt,sizeof xt); memcpy(br,g->br,sizeof br); memcpy(bp,g->bp,sizeof bp); memcpy(gate,g->gate,sizeof gate); memcpy(st,g->st,sizeof st); }
static void mutate(void){ int nm = 1 + (rnd()%3==0);
  for(int r=0;r<nm;r++){ double u=urand();
    if(u<0.45){ for(int k=0;k<20;k++){ int m=rnd()%(2*N), x=m/2, y=(int)(rnd()%(N+1))-1; if(y==x) continue; int old=xt[m]; xt[m]=y; if(acyclic()) break; xt[m]=old; } }
    else if(u<0.75){ int a=rnd()%(2*N), b=rnd()%(2*N), t=br[a]; br[a]=br[b]; br[b]=t; }
    else if(u<0.85){ bp[rnd()%(2*N)]^=1; }
    else if(u<0.93){ int l=1+rnd()%(d-1); for(int i=3;i>0;i--){ int j=rnd()%(i+1), t=gate[4*l+i]; gate[4*l+i]=gate[4*l+j]; gate[4*l+j]=t; } }
    else { st[rnd()%N]^=1; } } }
int main(int argc,char**argv){
  if(argc<7){ fprintf(stderr,"usage: room GENOME OUT H SEED SECONDS TEMP\n"); return 2; }
  const char*out=argv[2]; H=atoi(argv[3]); rs^=(unsigned long long)atoll(argv[4])*2654435761ULL; double secs=atof(argv[5]), temp=atof(argv[6]);
  if(!rd(out) && !rd(argv[1])) return 3;
  int A,T,nc; if(!eval(&A,&T,&nc)){ fprintf(stderr,"start genome not capped\n"); return 4; }
  int cA=A,cT=T,bA=A,bT=T; G g,bg; save(&g); save(&bg); wr(out);
  printf("start A %d T %d o(H-2) changes %d\n",A,T,nc); fflush(stdout);
  time_t t0=time(0), last=t0; long it=0, feas=0;
  while(difftime(time(0),t0)<secs){ it++; load(&g); mutate(); int a,t,n;
    if(!eval(&a,&t,&n)) continue; feas++;
    double dlt=(a-cA)+0.001*(t-cT);
    if(dlt<=0 || urand()<exp(-dlt/temp)){ save(&g); cA=a; cT=t;
      if(a<bA || (a==bA && t<bT)){ bA=a; bT=t; save(&bg); wr(out); printf("best A %d T %d it %ld\n",a,t,it); fflush(stdout); } }
    else load(&g);
    if(difftime(time(0),last)>=300){ last=time(0); printf("it %ld feasible %ld cur A %d T %d best A %d T %d\n",it,feas,cA,cT,bA,bT); fflush(stdout); } }
  load(&bg); printf("end best A %d T %d it %ld feasible %ld\n",bA,bT,it,feas); return 0; }
