#include<stdio.h>
int main()
{
  int num,sum=0,temp;
  scanf("%d",&num);
  temp=num;
  for (int i = 0; i < num; i++)
  {
    if(i==0 ||i==num-1)
    {
      for (int k = 1; k <=num; k++)
      {
        printf("%d ",k);
      }
      printf("\n");
    }
    else
    {
      for (int j = 0; j < num; j++)
      {
        if (j==temp-2)
        {
          printf("%d ",j+1);
        }
        else
          printf("  "); 
        
      }
      temp=temp-1;
      printf("\n");
    }
    
  }
}