#include <stdio.h>
int main()
{
    int n, rev=0,rem,c;
    printf("\n Enter the number : ");
    scanf("%d",&n);
    c=n;

    while (n!=0)
    {
        rem=n%10;
        rev=rev*10+rem;
        n/=10;
    }
    
    if (c==rev)
    printf("\nThe given number %d is a Palindrome.",c);
    else
    printf("\nThe given number %d is not a Palndrome.",c);

    return 0;
}