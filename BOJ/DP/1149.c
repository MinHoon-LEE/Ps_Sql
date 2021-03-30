#include<stdio.h>
int arr[10001][3];
int new1[10001][3];

int min (int a,int b){return a<b ? a : b;}
int main()
{
    int num ;
    scanf("%d",&num);
    int i;
    for(i=1;i<=num;i++)
    {
        scanf("%d%d%d",&arr[i][0],&arr[i][1],&arr[i][2]);
    }
    for(i=1;i<=num;i++)
    {
        new1[i][0]  = min(new1[i-1][1] + arr[i][0],new1[i-1][2] + arr[i][0]);
        new1[i][1]  = min(new1[i-1][0] + arr[i][1],new1[i-1][2] + arr[i][1]);
        new1[i][2]  = min(new1[i-1][0] + arr[i][2],new1[i-1][1] + arr[i][2]);
    }
    int result = min(min(new1[num][0],new1[num][1]),new1[num][2]);
    printf("%d",result);
}