#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter the value a,b,c");
    scanf("%d%d%d",&a,&b,&c);
    if(a>b)
    {
        printf("a is greater");
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
