#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter the value a,b,c");
    scanf("%d%d%d",&a,&b,&c);
    if(a>b)
    {
        printf("%d",a);
    }
    if(b>c)
    {
        printf("%d",b);
    }
    else
    {
        printf("%d",c);
    }
}
