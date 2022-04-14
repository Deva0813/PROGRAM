#include<stdio.h>
int main()
{
    int rev,temp,rem,n;

    printf("Enter a interger:");
    scanf("%d",&n);

    rev=0;
    rem=0;
    temp=n;

    while(temp!=0)
    {
        rem=temp%10;
        rev=rev*10+rem;
        temp/=10;
    }
    if(rev==n)
    {
        printf("%d is a palindrome..",n);
    }
    else
    {
        printf("%d is not a palindrome..",n);
    }
    return 0;

}