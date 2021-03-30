    #include<stdio.h>
    int a[15];
    int main()
    {
        int num;
        a[1]=1;
        a[2]=2;
        a[3]=4;
        scanf("%d",&num);
        //int *arr;
        int arr[11];
        int max =0;
        //arr = malloc(sizeof(int)*num);
        int i=0;
        for(i=0;i<num;i++)
        {
            scanf("%d",&arr[i]);
            if(arr[i]>max)
                max = arr[i];
        }
        int n = 4;
        for(n=4;n<=max;n++)
        {
            a[n] = a[n-1] + a[n-2] + a[n-3];
        }
        for( i=0;i<num;i++)
        {
            printf("%d\n",a[arr[i]]);    
        }

    }