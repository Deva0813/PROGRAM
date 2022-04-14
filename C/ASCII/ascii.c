#include <stdio.h>
int main() 
{  
    char n;
    printf("Enter a character: ");
    scanf("%c", &n);  
    printf("\nASCII value %c = %d", n, n);
    return 0;
}