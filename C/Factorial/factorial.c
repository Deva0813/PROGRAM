#include <stdio.h>
int main()
{
    int n,i;
    unsigned long long fact =1;
    printf("\n Enter the number: ");
    scanf("%d",&n);

    if (n<0)
        printf("\n Factorial of a negative number dosen't exist.");
    else
    {
        for(i=1;i<=n;++i)
        {
            fact*=i;
        }
        printf("\nFactorial of %d = %llu",n,fact);
    }
    return 0;
}