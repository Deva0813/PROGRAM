#include<stdio.h>
int main()
{
    int a[100],c,d,n,swap;
    printf("Enter the number of element: ");
    scanf("%d",&n);
    printf("Enter %d integers: ",n);
    for(c=0;c<n;c++)
    scanf("%d",&a[c]);
    
        for(c=0;c<n-1;c++)
        {
            for(d=0;d<n-c-1;d++)
            {
                if(a[d]>a[d+1])
                {
                    swap=a[d+1];
                    a[d+1]=a[d];
                    a[d]=swap;
                }

            }
        }
    printf("sorted list in accending oreder: ");
    for(c=0;c<n;c++)
    printf("%d\n",a[c]);
    return 0;
}