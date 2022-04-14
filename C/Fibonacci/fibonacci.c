#include <stdio.h>
int main()
{
    int i,n,a=0,b=1,c;
    printf("\n Enter the number of terms : ");
    scanf("%d",&n);
    printf("\nFibonacci series of the given number is :");

    for ( i = 1; i <=n; i++)
    {
        printf("%d, ",a);
        c=a+b;
        a=b;
        b=c;
    }
    return 0;
}