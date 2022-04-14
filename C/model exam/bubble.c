#include<stdio.h>
int main()
{
    int array[10],n,c,d,swap;

    printf("Enter no. of elements.: ");
    scanf("%d",&n);
    printf("Enter %d integers: ",n);

    for(c=0;c<n;c++)
    {
        scanf("%d",&array[c]);
    }
    for(c=0;c<n-1;c++)
    {
        for(d=0;d<c-n-1;d++)
        {
            if(array[d]>array[d+1])
            {
                swap=array[d];
                array[d]=array[d+1];
                array[d+1]=swap;
            }
        }
    }
    
    printf("Sorted array list is : ");
    for(c=0;c<n;c++)
    {
        printf("%d\n",array[c]);
    }
    return 0;
}