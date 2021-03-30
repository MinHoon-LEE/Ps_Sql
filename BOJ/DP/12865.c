#include<stdio.h>
int weight[102];
int value[102];
int dp[101][100001];

int max (int a,int b){return a>b ? a : b;}
int main()
{
    int a,b;
    scanf("%d%d",&a,&b);
    for(int i=1;i<=a;i++)
    {
        scanf("%d%d",&weight[i],&value[i]);
    }
    
    for(int i=1;i<=a;i++)
    {
        for(int j=1;j<=b;j++)
            if(weight[i]>j)
                dp[i][j] = dp[i-1][j];
            else
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i]);
    }
    int nn = dp[a][b];
    printf("%d",nn);
}