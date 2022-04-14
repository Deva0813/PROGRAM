#include <stdio.h>
int main()
{
    int n, rev=0, rem;
    printf("\nEnter the number: ");
    scanf("%d",&n);

    while (n !=0)
    {
        rem=n%10;
        rev=rev*10+rem;
        n/=10;
    }
    printf("\nReverse of the given number is %d ",rev);
    return 0;
}    