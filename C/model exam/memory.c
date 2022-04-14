#include<stdio.h>
#include<stdlib.h>
int main()
{
    int *iVar;
    char *cVar;
    float *fVar;

    iVar=(int*)malloc(1*sizeof(int));
    cVar=(char*)malloc(1*sizeof(char));
    fVar=(float*)malloc(1*sizeof(float));

    printf("Enter a integer: ");
    scanf("%d",iVar);
    printf("Enter a string :");
    scanf("%c",cVar);
    printf("Enter a float value: ");
    scanf("%f",fVar);

    printf("Inputed values are: %d,%s,%.2f ",*iVar,*cVar,*fVar);

    free(iVar);
    free(cVar);
    free(fVar);

    return 0;

}