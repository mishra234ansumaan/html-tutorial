#include<stdio.h>
int main()
{
    int a,b;
    printf("enter a and b:");
    scanf("%d %d",&a,&b);
    printf("the result of %d & %d =%d\n",a,b,a&b);
    printf("the result of %d | %d =%d\n",a,b,a|b);
    printf("the result of %d>>1=%d\n",a,a>>1);
    return 0;
}