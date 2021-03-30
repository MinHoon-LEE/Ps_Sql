#include <stdio.h>
int array[1000000];
int main()
{
    int num4 =0;
    int num=2;
    array[1] =0;
    array[2] =1;
    scanf("%d",&num4);
    
    while(num <= num4)
    {
        int num1=1000000;
        int num2=1000000;
        int num3=1000000;
        if(num % 3 ==0)
        {
         //   printf("--3\n");
            num1 = array[num/3] +1;
        }
        if (num %2 ==0)
        {
         //   printf("--2\n");
             num2 = array[num/2] +1;
        }
        if(2>1)
        {
         //   printf("--1\n");
             num3 = array[num-1] +1;
        }
        int tmp=1000000;
        if(num1 > num2)
            tmp = num2;
        else 
            tmp = num1;
        if(tmp> num3)
            array[num] = num3;
        else   
            array[num] = tmp;
        num ++;
      // printf("%d\n",array[num-1]);
    }
    
    printf("%d",array[num4]);
}
