#include<stdio.h>
int main()
{
    int array[100],search,c,n;
    printf("Enter the no. of elements in the array:");
    scanf("%d",&n);
    printf("\nEnter %d integers:\n",n);
    for(c=0;c<n;c++)
    scanf("%d",&array[c]);
    printf("Enter the integer to search:");
    scanf("%d",&search);
    for(c=0;c<n;c++)
    {
        if(array[c]==search)
        {
            printf("%d is present at location %d\n",search,c+1);
            break;
        } 
    }
        if(c==n)
            printf("element not found",search);   
    return 0;

}