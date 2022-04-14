#include<stdio.h>
#include<conio.h>

void mian()
{
    int a[10],i,j,k,n;
    printf("Enter the no. of elements: " );
    scanf("%d",&n);
    printf("Enter the array elements..: ");

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    for(i=1;i<n;i++)
    {
        k=a[j];
        for(j=i-1;j>=0 && k<a[j];j--) 
        a[j+1]=a[i];
        a[j+1]=k;
       
    }
    printf("Elements after arrangement: ");

    for(i=0;i<n;i++)
    {
        printf("%d",a[i]);

    }
    getch();
}