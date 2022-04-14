#include<stdio.h>
#include<string.h>
struct student
{
    int id;
    char name[20];
    float percentage;
};
int main()
{
    struct student record1={2001,"deva",98.6};
    struct student*ptr;
    ptr=&record1;

    printf("Student record >>>\n");
    printf("Roll no.:%d\n",ptr->id);
    printf("Name: %s\n",ptr->name);
    printf("Percentage: %.2f\n",ptr->percentage);
    return 0; 

}