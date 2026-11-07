/* L-LOWER 4, box L4: DRIVEN BLOCK capacity. A ladder block of m levels (movers 2j, 2j+1 on level j = 0..m-1, degree 2),
   IDEAL rules (R104 definition), except that the key-preferred option c_0 of level 0 is an EXOGENOUS bit e(t), chosen freely
   at every step. Xi-targets: X or a mover of smaller index (acyclic). Values: signed 2^rank sums along chains (R105 ENC).
   Level j >= 1: c_j = o_(j-1): split pair -> [s(2j-2) != c_(j-1)]; joint on i -> kap[j-1][i] (gate order).
   Exact: longest path (in moving steps) in the state DAG (values monotone), max over e-sequences, all starts.
   Mode climb: perturbation search over genomes maximizing LP (or top-mover moves along an LP? -> we use LP and topmoves). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXM 16
static int s0g=0; static int HALF=0; int m,N; int ACYC=0, FREE=0; int ord[2*MAXM], pos[2*MAXM]; int xt[2*MAXM][2], rk[2*MAXM][2], par[2*MAXM][2], kap[MAXM][2];
static long long cvv[2*MAXM];
static void vals(int s, long long *v){ for(int i=0;i<N;i++){int x=ord[i];int k=(s>>x)&1; long long b=(1LL<<rk[x][k]); if(par[x][k]) b=-b; v[x]=b+(xt[x][k]>=0? v[xt[x][k]]:0);} }
static long long optv(long long *v,int x,int k){ long long b=(1LL<<rk[x][k]); if(par[x][k]) b=-b; return b+(xt[x][k]>=0?v[xt[x][k]]:0);}
static int step(int s,int e){ long long v[2*MAXM]; vals(s,v); int avail=0; /* bit x: other option better */
  for(int x=0;x<N;x++){int k=(s>>x)&1; if(optv(v,x,1-k)>v[x]) avail|=1<<x;}
  int ns=s; int c=e;
  for(int j=0;j<m;j++){ for(int q=0;q<2;q++){int x=2*j+q; int k=(s>>x)&1; if(k!=c && ((avail>>x)&1) && !(HALF && (x&1))) ns^=1<<x;}
    int a=(ns>>(2*j))&1, b=(ns>>(2*j+1))&1; int o = (a!=b)? (a!=c) : kap[j][a]; c=o; }
  return ns; }
static int *memo; static int *topm;
static int STARTONLY=0; static unsigned *hk; static int *hv; static long hsz=1<<22; static long hcnt=0;
static int hget(unsigned key){ unsigned long h=(key*2654435761u)&(hsz-1); while(hv[h]!=-2){ if(hk[h]==key) return hv[h]; h=(h+1)&(hsz-1);} return -1; }
static void hput(unsigned key,int v){ unsigned long h=(key*2654435761u)&(hsz-1); while(hv[h]!=-2){ if(hk[h]==key){hv[h]=v;return;} h=(h+1)&(hsz-1);} hk[h]=key; hv[h]=v; hcnt++; }
static int OBJL=-1;
static int oL(int s,int e){ int c=e; for(int j=0;j<=OBJL;j++){int a=(s>>(2*j))&1,b=(s>>(2*j+1))&1; c=(a!=b)?(a!=c):kap[j][a];} return c; }
static int EB=1000;
static int lpf(int s,int e,int u){ unsigned key=((unsigned)s<<3)|(e<<2)|(u>3?3:u); int r=hget(key); if(r>=0) return r; int best=0; int o=oL(s,e);
  for(int f=0;f<2;f++){ int u2=u+(f!=e); if(u2>EB) continue; int ns=step(s,f); if(ns!=s){int q=(oL(ns,f)!=o)+lpf(ns,f,u2); if(q>best)best=q;}} hput(key,best); return best; }
static int lph(int s){ int r=hget(s); if(r>=0) return r; int best=0; for(int e=0;e<2;e++){int ns=step(s,e); if(ns!=s){int q=1+lph(ns); if(q>best)best=q;}} hput(s,best); return best; }
static int lp(int s){ if(memo[s]>=0) return memo[s]; int best=0,bt=0;
  if(FREE){ long long v[2*MAXM]; vals(s,v); for(int x=0;x<N;x++){int k=(s>>x)&1; if(optv(v,x,1-k)>v[x]){int r=1+lp(s^(1<<x)); if(r>best)best=r;}} memo[s]=best; return best; } for(int e=0;e<2;e++){int ns=step(s,e); if(ns!=s){int r=1+lp(ns); int tm=topm[ns]+(((ns^s)>>(N-2))&3?1:0); if(r>best){best=r;} if(tm>bt)bt=tm;}} memo[s]=best; topm[s]=bt; return best;}
static unsigned rnd();
static int CROSS=0;
static int pickt(int x){ if(HALF){ int j=x/2; int r=rnd()%(j+1); return r==j? -1 : 2*r; } if(CROSS){ int j=x/2,q=x%2; (void)q; return -2; } if(!ACYC) return (x==0)?-1:((int)(rnd()%(x+1)))-1; int p=pos[x]; int r=rnd()%(p+1); return r==p? -1: ord[r]; }
static unsigned long long rs=88172645463325252ULL; static unsigned rnd(){rs^=rs<<13;rs^=rs>>7;rs^=rs<<17;return (unsigned)rs;}
static void randg(){ int perm[4*MAXM]; for(int i=0;i<2*N;i++)perm[i]=i; for(int i=2*N-1;i>0;i--){int j=rnd()%(i+1);int t=perm[i];perm[i]=perm[j];perm[j]=t;}
  for(int x=0;x<N;x++)for(int k=0;k<2;k++){ xt[x][k]=pickt(x); rk[x][k]=perm[2*x+k]; par[x][k]=rnd()&1;}
  for(int j=0;j<m;j++)for(int i=0;i<2;i++)kap[j][i]=rnd()&1; }
static int evalg(int *tmax){ if(STARTONLY){ for(long i=0;i<hsz;i++)hv[i]=-2; hcnt=0; *tmax=0; if(OBJL>=0){int a=lpf(s0g,0,0),b=lpf(s0g,1,0); return a>b?a:b;} return lph(s0g); } int S=1<<N; for(int i=0;i<S;i++){memo[i]=-1;topm[i]=0;} int best=0; *tmax=0; for(int s=0;s<S;s++){int r=lp(s); if(r>best)best=r; if(topm[s]>*tmax)*tmax=topm[s];} return best; }
static int lpath(int s0, const char *seq){ /* follow e-sequence from s0, print states, count moving steps */
  int s=s0,c=0; for(int t=0;seq[t];t++){int ns=step(s,seq[t]-'0'); if(ns!=s)c++; s=ns; for(int x=0;x<N;x++)printf("%d",(s>>x)&1); printf("\n");} return c; }

static int readgen(const char*fn){ FILE*f=fopen(fn,"r"); if(fscanf(f,"%d",&m)!=1)return 1; N=2*m;
    for(int x=0;x<N;x++) if(fscanf(f,"%d %d %d %d %d %d",&xt[x][0],&xt[x][1],&rk[x][0],&rk[x][1],&par[x][0],&par[x][1])!=6) return 1;
    for(int j=0;j<m;j++) if(fscanf(f,"%d %d",&kap[j][0],&kap[j][1])!=2) return 1;
    for(int i=0;i<N;i++){ if(fscanf(f,"%d",&ord[i])!=1) return 1; pos[ord[i]]=i; }
    char sb[64]; if(fscanf(f,"%63s",sb)==1) for(int x=0;x<N;x++) if(sb[x]=='1') s0g|=1<<x; fclose(f); return 0; }
int main(int argc,char**argv){ if(getenv("GEN") && !getenv("SEED")){ if(readgen(getenv("GEN")))return 1; int s0=s0g;
    memo=malloc(sizeof(int)<<N); topm=malloc(sizeof(int)<<N);
    if(argc>1){ printf("moving steps %d\n", lpath(s0, argv[1])); return 0; }
    int tm; int best=evalg(&tm); printf("LP(all starts) %d  LP(start) %d\n", best, memo[s0]); return 0; }
  if(getenv("OBJL")) OBJL=atoi(getenv("OBJL")); if(getenv("EB")) EB=atoi(getenv("EB"));
  if(getenv("STARTONLY")){STARTONLY=1; hk=malloc(sizeof(unsigned)*hsz); hv=malloc(sizeof(int)*hsz);}
  if(getenv("SEED")){ readgen(getenv("SEED")); ACYC=1; } else m=atoi(argv[1]); if(!getenv("SEED")) N=2*m; long iters=atol(argv[2]); rs+=atol(argv[3]); if(getenv("ACYC"))ACYC=1; if(getenv("FREE"))FREE=1; if(!getenv("SEED")) for(int i=0;i<2*MAXM;i++){ord[i]=i;pos[i]=i;}
  if(ACYC){ for(int i=N-1;i>0;i--){rnd();} }
  if(!STARTONLY){memo=malloc(sizeof(int)<<N); topm=malloc(sizeof(int)<<N);}
  int bxt[2*MAXM][2],brk[2*MAXM][2],bpar[2*MAXM][2],bk[MAXM][2]; if(getenv("CROSS"))CROSS=1; if(getenv("HALF"))HALF=1; if(!getenv("SEED")) randg();
  if(CROSS){ for(int x=0;x<N;x++){int j=x/2,q=x%2; if(j==0){xt[x][0]=xt[x][1]=-1;} else {xt[x][0]=2*j-2+q; xt[x][1]=2*j-1-q;} } for(int i=0;i<N;i++){ord[i]=i;pos[i]=i;} } int tm; double temp=getenv("TEMP")?atof(getenv("TEMP")):0; int cur; int best=evalg(&tm); int bestT=tm; cur=best;
  memcpy(bxt,xt,sizeof xt);memcpy(brk,rk,sizeof rk);memcpy(bpar,par,sizeof par);memcpy(bk,kap,sizeof kap);
  for(long it=0;it<iters;it++){ int r=rnd()%(ACYC?6:5); int sw=-1; int x=rnd()%N,k=rnd()&1;
    if(r==0){ if(CROSS) continue; xt[x][k]=pickt(x); } else if(r==1){int y=rnd()%N,l=rnd()&1;int t=rk[x][k];rk[x][k]=rk[y][l];rk[y][l]=t;}
    else if(r==2){par[x][k]^=1;} else if(r==3){kap[rnd()%m][rnd()&1]^=1;} else if(r==4){ if(CROSS) continue; int y=rnd()%N,l=rnd()&1;int t=rk[x][k];rk[x][k]=rk[y][l];rk[y][l]=t; xt[x][k]=pickt(x);}
    else { if(CROSS) continue; int p=rnd()%(N-1); int a=ord[p],b=ord[p+1]; if(xt[b][0]==a||xt[b][1]==a) continue; ord[p]=b;ord[p+1]=a;pos[a]=p+1;pos[b]=p; sw=p; }
    int v=evalg(&tm); double tt=temp*(1.0-(double)it/iters); if(v>best) {FILE*o=fopen(getenv("OUT")?getenv("OUT"):"/dev/null","w"); fprintf(o,"%d\n",m); for(int y=0;y<N;y++)fprintf(o,"%d %d %d %d %d %d\n",xt[y][0],xt[y][1],rk[y][0],rk[y][1],par[y][0],par[y][1]); for(int j=0;j<m;j++)fprintf(o,"%d %d\n",kap[j][0],kap[j][1]); for(int i=0;i<N;i++)fprintf(o,"%d ",ord[i]); fprintf(o,"\n"); for(int x=0;x<N;x++)fprintf(o,"%d",(s0g>>x)&1); fprintf(o,"\n"); fclose(o);}
    if(v>=cur || (tt>0 && (rnd()%100000)/100000.0 < __builtin_exp((v-cur)/tt))){ cur=v; if(v>best) {fprintf(stderr,"it %ld LP %d top %d\n",it,v,tm); best=v;bestT=tm;}memcpy(bxt,xt,sizeof xt);memcpy(brk,rk,sizeof rk);memcpy(bpar,par,sizeof par);memcpy(bk,kap,sizeof kap);}
    else { if(sw>=0){int p=sw;int a=ord[p],b=ord[p+1];ord[p]=b;ord[p+1]=a;pos[a]=p+1;pos[b]=p;} memcpy(xt,bxt,sizeof xt);memcpy(rk,brk,sizeof rk);memcpy(par,bpar,sizeof par);memcpy(kap,bk,sizeof kap);} }
  printf("m %d LP %d top %d\nxt:",m,best,bestT); for(int x=0;x<N;x++)printf(" (%d,%d)",bxt[x][0],bxt[x][1]); printf("\nrk:"); for(int x=0;x<N;x++)printf(" (%d%c,%d%c)",brk[x][0],"eo"[bpar[x][0]],brk[x][1],"eo"[bpar[x][1]]);
  printf("\nord:"); for(int i=0;i<N;i++)printf(" %d",ord[i]); printf("\nkap:"); for(int j=0;j<m;j++)printf(" %d%d",bk[j][0],bk[j][1]); printf("\n"); }
