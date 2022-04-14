#include<stdio.h>
int main()
{
    int i,num;
    unsigned char flag=0;

    printf("Enter the integer: ");
    scanf("%d",&num);

    for(i=2;i<(num/2);i++)
    {
        if(num%i==0)
        {
            flag=1;
            break;
        }
    }
    if(flag==0)
    {
        printf("The given number: %d is prinme",num);
    }
    else
    {
        printf("The given number is no prime",num);
    }
    

    return 0;

}