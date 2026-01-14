#include<stdio.h>
int main()
{
char grade;
int num;
printf("enter your grade:");
scanf("%c",& grade);
switch(grade)
{
    case'O':

        printf("outstanding!\n");
        break;
    case'A':
        printf("very good!\n");
        break;
    case'B':
        printf("good keep progressing");
        break;

}
return 0;
}
