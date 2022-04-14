#include <stdio.h> 
int main() 
{ 
    int x, y; 
    printf("Enter the value of x = ");
    scanf("%d",&x);
    printf("\nEnter the value of y = ");
    scanf("%d",&y);
    x = x+y;
    y = x-y;
    x = x-y;
    printf("\nAfter Swapping: x = %d, y = %d", x, y); 
    return 0; 
} 