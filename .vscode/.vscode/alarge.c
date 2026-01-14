#include<stdio.h>
int main()
{
int a,b;
printf("enter a and b:");
scanf("%d %d",&a,&b);
if(a!=b)
{
    if(a>b)
    {
    printf( "%d is the largest number/n",a);
    }
    else
    {
        printf("%d is the  largest number\n",b);
    }
}
     else
    {
        printf("both the numbers entered are equal");
    }
return 0;
   
}

