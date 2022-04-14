#include<stdio.h>
#define MAX 4
void main()
{
    int array[MAX],i,l1,l2,temp;

    printf("Enter %d interger numbers \n",MAX);

    for(i=0;i<MAX;i++)
    {
        scanf("%d",&array[i]);
    }

    printf("Input integer are : \n");
    for(i=0;i<MAX;i++)
    {
        printf("%5d",array[i]);
    }
    printf("\n");

    l1=array[0];
    l2=array[1];

    if(l1,l2)
    {
        temp=l1;
        l1=l2;
        l2=temp;
    }

    for(i=2;i<4;i++)
    {
        if(array[i]==l1)
        {
            l2=l1;
            l1=array[i];
        }
        else if(array[i]==l2)
        {
            l2=array[i];
        }
    }
    printf("First largest is: %d\n",l1);
    printf("Second largest is : %d\n",l2);
    printf("Average of %d and %d is %d",l1,l2,(l1+l2)/2);
    
} 