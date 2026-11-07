/* Box 193 (L-NEW successor 61): CS(M, A) exact maximum of distinct hub chains, self-contained (generates the forests itself),
   OpenMP-parallel and resumable. Same DP as dp193.c (see there and chain193.py for the definitions).
   Build: gcc -O2 -fopenmp -o dp193b dp193b.c.  Run: ./dp193b M A CHECKPOINT_FILE  (rerun the same command to resume).
   Prints progress lines «dp193b: f/n best-so-far» every checkpoint and a final line «M .. A .. forests .. max distinct hub chains ..». */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
static int M, A;
typedef struct { long long k[9]; long long s; } F;
static int cmpF(const void *a, const void *b){ const F *x=a,*y=b; if(x->s!=y->s) return x->s<y->s?-1:1;
  for(int i=0;i<M;i++) if(x->k[i]!=y->k[i]) return x->k[i]<y->k[i]?-1:1; return 0; }
int main(int argc, char **argv){
  if(argc<4){printf("dp193b: FAILED usage: dp193b M A CHECKPOINT\n");return 1;}
  M=atoi(argv[1]); A=atoi(argv[2]); const char *ck=argv[3];
  if(M<1||M>9){printf("dp193b: FAILED M out of range\n");return 1;}
  long long tot=1; for(int i=0;i<M;i++) tot*=(M+1);
  size_t cap=1<<20, n=0; F *L=malloc(sizeof(F)*cap); if(!L){printf("dp193b: FAILED memory\n");return 1;}
  int par[9];
  for(long long code=0;code<tot;code++){ long long c=code; for(int i=0;i<M;i++){par[i]=c%(M+1); c/=(M+1);}
    F f; int ok=1; f.s=0;
    for(int i=1;i<=M && ok;i++){ int x=i, seen=0, cnt=0, prev=-1, asc=0; long long key=0;
      while(x){ if(seen&(1<<x)){ok=0;break;} seen|=1<<x; key|=1LL<<x; if(prev>=0 && x>prev) asc++; prev=x; x=par[x-1]; if(++cnt>M+1){ok=0;break;} }
      if(!ok||asc>A){ok=0;break;} f.k[i-1]=key; f.s+=key; }
    if(!ok) continue;
    if(n==cap){cap*=2; L=realloc(L,sizeof(F)*cap); if(!L){printf("dp193b: FAILED memory\n");return 1;}}
    L[n++]=f; }
  qsort(L,n,sizeof(F),cmpF);
  int *B=malloc(sizeof(int)*n*(M+1)); if(!B){printf("dp193b: FAILED memory\n");return 1;}
  long start=0; int ans=0;
  FILE *fp=fopen(ck,"rb");
  if(fp){ long nn; int mm, aa; if(fread(&nn,sizeof nn,1,fp)==1 && fread(&mm,sizeof mm,1,fp)==1 && fread(&aa,sizeof aa,1,fp)==1 &&
          nn==(long)n && mm==M && aa==A && fread(&start,sizeof start,1,fp)==1 && fread(&ans,sizeof ans,1,fp)==1 &&
          fread(B,sizeof(int),(size_t)start*(M+1),fp)==(size_t)start*(M+1)) printf("dp193b: resumed at %ld of %zu\n",start,n);
        else { start=0; ans=0; printf("dp193b: checkpoint unusable, starting fresh\n"); } fclose(fp); }
  time_t last=time(NULL);
  for(long f=start; f<(long)n; f++){ long long *a=L[f].k; int bf[10]; for(int j=0;j<=M;j++) bf[j]=1;
    #pragma omp parallel
    { int loc[10]; for(int j=0;j<=M;j++) loc[j]=1;
      #pragma omp for schedule(static) nowait
      for(long g=0; g<f; g++){ long long *b=L[g].k; int ok=1; for(int i=0;i<M;i++) if(b[i]>a[i]){ok=0;break;}
        if(!ok) continue; int *bg=B+g*(M+1);
        for(int j=0;j<=M;j++){ long long c=j?a[j-1]:0;
          for(int jj=0;jj<=M;jj++){ long long cc=jj?b[jj-1]:0; if(cc<c && bg[jj]+1>loc[j]) loc[j]=bg[jj]+1; } } }
      #pragma omp critical
      { for(int j=0;j<=M;j++) if(loc[j]>bf[j]) bf[j]=loc[j]; } }
    for(int r=0;r<=M;r++) for(int j=0;j<=M;j++){ long long c=j?a[j-1]:0;
      for(int jj=0;jj<=M;jj++){ long long cc=jj?a[jj-1]:0; if(cc<c && bf[jj]+1>bf[j]) bf[j]=bf[jj]+1; } }
    for(int j=0;j<=M;j++){ B[f*(M+1)+j]=bf[j]; if(bf[j]>ans) ans=bf[j]; }
    if(time(NULL)-last>=300 || f+1==(long)n){ last=time(NULL); long done=f+1;
      FILE *w=fopen(ck,"wb"); if(!w){printf("dp193b: FAILED to write checkpoint\n");return 1;}
      long nn=n; fwrite(&nn,sizeof nn,1,w); fwrite(&M,sizeof M,1,w); fwrite(&A,sizeof A,1,w); fwrite(&done,sizeof done,1,w);
      fwrite(&ans,sizeof ans,1,w); fwrite(B,sizeof(int),(size_t)done*(M+1),w); fclose(w);
      printf("dp193b: %ld/%zu best-so-far %d\n",done,n,ans); fflush(stdout); } }
  printf("M %d A %d forests %zu max distinct hub chains %d\n",M,A,n,ans); return 0; }
