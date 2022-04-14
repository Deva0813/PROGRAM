#include <stdio.h>
int main()
{
   char s[1000], r[1000];
   int i, c, n = 0;

   printf("Enter a string : ");
   gets(s);

   while (s[n] != '\0')
      n++;

  c = n - 1;

   for (i = 0; i < n; i++) {
      r[i] = s[c];
      c--;
   }

   r[i] = '\0';

   printf("The reverse of the strimg : %s\n", r);

   return 0;
}