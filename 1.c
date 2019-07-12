#include <stdio.h>
int main()
{
    double number;
    printf("Enter a number: ");
    scanf("%lf", &number);
    if (number <= 0.0)
    {
        if (number == 0.0)
            printf("0");
        else
            printf("negative");
    }
    else
        printf(" positive ");
    return 0;
}
© 2019 GitHub, Inc.
