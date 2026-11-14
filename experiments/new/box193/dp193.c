/* Box 193 (L-NEW successor 61): exact maximum of distinct hub chains in CS(M, A) from the forest list of chain193.py --emit.
   Forests are given sorted by the sum of their chain keys (a dominated forest has a smaller or equal sum).
   best[f][j] = longest run ending in forest f with hub value j (0 = empty hub chain, j = item j's chain). A transition g -> f needs every
   item chain of g <= that of f; the hub value must strictly increase. Within one forest the hub may move to a larger own chain.
   Build: gcc -O2 -o dp193 dp193.c.  Run: python3 chain193.py 7 1 --emit | ./dp193 */
#include <stdio.h>
#include <stdlib.h>
int main(void){int n,M; if(scanf("%d %d",&n,&M)!=2){printf("dp193: FAILED to read header\n");return 1;}
 long long *K=malloc(sizeof(long long)*(size_t)n*M); int *B=malloc(sizeof(int)*(size_t)n*(M+1));
 if(!K||!B){printf("dp193: FAILED (memory)\n");return 1;}
 for(long i=0;i<(long)n*M;i++) if(scanf("%lld",&K[i])!=1){printf("dp193: FAILED to read forest %ld\n",i/M);return 1;}
 int ans=0;
 for(int f=0;f<n;f++){long long*a=K+(long)f*M;int*bf=B+(long)f*(M+1);
  for(int j=0;j<=M;j++)bf[j]=1;
  for(int g=0;g<f;g++){long long*b=K+(long)g*M;int ok=1;for(int i=0;i<M;i++)if(b[i]>a[i]){ok=0;break;}
   if(!ok)continue;int*bg=B+(long)g*(M+1);
   for(int j=0;j<=M;j++){long long c=j?a[j-1]:0;
    for(int jj=0;jj<=M;jj++){long long cc=jj?b[jj-1]:0;if(cc<c&&bg[jj]+1>bf[j])bf[j]=bg[jj]+1;}}}
  for(int r=0;r<=M;r++)for(int j=0;j<=M;j++){long long c=j?a[j-1]:0;
   for(int jj=0;jj<=M;jj++){long long cc=jj?a[jj-1]:0;if(cc<c&&bf[jj]+1>bf[j])bf[j]=bf[jj]+1;}}
  for(int j=0;j<=M;j++)if(bf[j]>ans)ans=bf[j];}
 printf("M %d forests %d max distinct hub chains %d\n",M,n,ans);return 0;}
