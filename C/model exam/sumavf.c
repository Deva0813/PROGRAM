#include<stdio.h>
#define MAXSIZE 10
int main()
{
    int array[MAXSIZE];
    int  i,num,nnum=0,pnum=0;
    float avg,total;
    printf("Enter the valude of n :");
    scanf("%d",&num);

    printf("Enter %d of numbers : ",num);
    
    for(i=0;i<num;i++)
    {
        scanf("\n%d",&array[i]);
    }
    printf("Input array elements: \n");

    for(i=0;i<num;i++)
    {
        printf("%+3d\n",array[i]);
    }

    for(i=0;i<num;i++)
    {
        if(array[i]<0)
        {
            nnum=nnum+array[i];
        }
        else if(array[i]>0)
        {
            pnum=pnum+array[i];
        }
        else if(array[i]==0)
        {
            ;
        }
        total=total+array[i];
    }
    avg=total/num;
    printf("Negative number : %d\n",nnum);
    printf("Positive number : %d\n",pnum);
    printf("Total : %f\n",total);
    printf("Average : %.2f\n",avg);

    return 0;
}