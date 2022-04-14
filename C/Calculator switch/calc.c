#include <stdio.h>
int main() 
{
    char n;
    double a, b;
    printf("\nEnter an operator (+, -, *,) : ");
    scanf("%c", &n);
    printf("\nEnter first operands: ");
    scanf("%lf", &a);
    printf("\nEnter second operands: ");
    scanf("%lf", &b);

    switch (n) 
    {
    case '+':
        printf("\n%.1lf + %.1lf = %.1lf", a, b, a+b);
        break;
    case '-':
        printf("\n%.1lf - %.1lf = %.1lf", a, b, a-b);
        break;
    case '*':
        printf("\n%.1lf * %.1lf = %.1lf", a, b, a*b);
        break;
    case '/':
        printf("\n%.1lf / %.1lf = %.1lf", a, b, a/b);
        break;
    default:
        printf("\nOperator is not correct");
    }

    return 0;
}