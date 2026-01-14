#include<stdio.h>
int main()
{
    int num[5],i;
    printf("enter 5 elements:\n");
    for(i=0;i<5;i++)
    {
        scanf("%d",& num[i]);  
        if(num[i]%2==0)
        {
            printf("num[%d] is an even number:\n",i);
        }
        else
        {
            printf("num[%d]is an odd number:\n",i);
        }
    }
    return 0;
}