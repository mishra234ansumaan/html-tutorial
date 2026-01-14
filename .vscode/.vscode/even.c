#include<stdio.h>
int main()
{
    int num[5]={10,15,24,36,2},i;
    for(i=0;i<5;i++)
    {
    if(num[i]%2==0)
    {
        printf("num[%d] is even\n",i);
    }
    else
    {
        printf("num[%d] is odd\n",i);
    }
}
return 0;
}