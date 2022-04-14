#include <stdio.h>
int main()
{
    char line[50];
    int vowels, consonant;
    vowels=consonant=0;
    printf("\nEnter a line of string: ");
    fgets(line,sizeof(line),stdin);

    for (int i = 0;line[i] !='\0'; ++i)
    {
        if (line[i]=='a' || line[i]=='e' || line[i]=='i' ||
            line[i]=='o' || line[i]=='u' || line[i]=='A' ||
            line[i]=='E' || line[i]=='I' || line[i]=='O' ||
            line[i]=='U')
            {
                ++vowels;
            }
            else if ((line[i]>='a' && line[i]<='z' ) || (line[i]>='A' && line[i]<='Z' ))
            {
                ++consonant;
            }
    }
    printf("\nVowels : %d",vowels);
    printf("\nConsonants : %d",consonant);

    return 0;
}