#include<stdio.h>

int main()
{
    int n,i=0,start=0,end;
    scanf("%d",&n);
    end=n*2-1;

    for(int i=0;i<n*2;i++) //row
    {
        if(i<n)
        {
        for(int j=0;j<n*2;j++) //col
        {
            if (j<=start||j>=end)
            {
                printf("* ");
            }
            else
            {
                printf("  ");
            }
            
        }
        start++;
        end--;
        printf("\n");
        }
        else
        {
           for(int j=0;j<n*2;j++) //col
        {
            if (j<=start||j>=end)
            {
                printf("* ");
            }
            else
            {
                printf("  ");
            }
            
        }
        start--;
        end++;
        printf("\n"); 
        }

        if(i==n-1)
        {
            start--;
            end++;
        }
    }

}
