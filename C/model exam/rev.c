#include<stdio.h>
int main()
{
    int rev=0,temp,rem,num;

    printf("Enter the number : ");
    scanf("%d",&num);
    while(num>0)
    {
        rem=num%10;
        rev=rev*10+rem;
        num=num/10;
    }
    printf("the reversse of the number is : %d",rev);
    return 0;
}