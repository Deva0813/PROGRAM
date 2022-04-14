#include<stdio.h>
#include<string.h>

int main()
{
    char s1[20]="string 1:";
    char s2[100]="string 2: Im a programer";
    strcpy(s1,s2);
    printf("String 1 is %s",s1);
    return 0;
}