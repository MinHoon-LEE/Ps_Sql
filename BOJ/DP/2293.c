#include<stdio.h>

int main()
{
    int num,target;
    int arr[101];
    int arr2[10001]={0,};
    scanf("%d%d",&num,&target);
    for(int i=0;i<num;i++)
    {
        scanf("%d",&arr[i]);
    }  
    int n = target;
    arr2[0] = 1; 
    for(int i=0;i<num;i++)
    {
        for(int j=0;j<=target;j++)
        {
            if(j-arr[i]>=0)
           arr2[j] = arr2[j]+ arr2[j-arr[i]];
        }
     
    }
    printf("%d",arr2[target]);
}