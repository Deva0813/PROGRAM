#include<stdio.h>
int main()
{
    int array[100],i,search,n;

    printf("Enter no of elements for the array");
    scanf("%d",&n);
    printf("Enter %d integers: ",n);

    for(i=0;i<n;i++)
    {
        scanf("%d",&array[i]);
    }
    printf("Enter the no. to search: ");
    scanf("%d",&search);

    for(i=0;i<n;i++)
    {
        if(array[i]==search)
        {
            printf("%d is present in the location of %d.",search,i+1);
            break;
        }
        
    }
    if(i==n)
    {
        printf("%d element is not present..",search);
    }
    return 0;    
}