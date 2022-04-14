#include <stdio.h>
int main()
{
    int n,i,flag=0;
    printf("\nEnter the number : ");
    scanf("%d",&n);

    for (i=2; i<=n/2;++i)
    {
        if (n%i==0)
        {
            flag=1;
            break;    
        }
    }
    if (n==1)
    {
        printf("\n 1 is nither a prime number nor a composite");
    }
    else
    {
        if (flag==0)
            printf("\n%d is a prime number.",n);
        else
            printf("\n %d is not a prime number.",n);
    }
    return 0;
}