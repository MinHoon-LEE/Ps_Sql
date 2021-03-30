#include <stdio.h>

int main()
{
    int five =0;
    int three =0;
    int kg;
    scanf("%d",&kg);
    int num = kg / 5 ;
    while(num != -1)
    {
        
        if((kg - (5*num))%3 ==0)
            break;
        else 
            num --;

    }
    int sum =0;
    if(num != -1)
    {
         sum  = num + (kg-(5*num))/3;
         printf("%d",sum);   
    }
    else
        printf("-1");
}
