#include<stdio.h>
int main()
{
    int e,b,c;
    printf("enter the value a,b,c");
    scanf("%d%d%d",&e,&b,&c);
    if(e>b)
    {
        printf("e is greater");
    }
    if(b>c)
    {
        printf("b is greater");
    }
    else
    {
        printf("c is greater");
    }
}
