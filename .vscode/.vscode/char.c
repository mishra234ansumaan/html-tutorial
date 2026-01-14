#include<stdio.h>
int main()
{
    char c;
    printf ("enter a character");
    scanf("%d",&c);
    if((c>='A' && c<='Z') || (c>='a' && c<='z'))
    {
        printf("entered character is an alphabet:\n",c);
    }
    else if(c>=0 && c<=9)
    {
        printf("entered character is a number:\n",c);
    }
    else
    {
        printf("entered character is a special character:\n",c);
    }
    return 0;
} 