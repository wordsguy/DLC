#include <stdio.h>

void print (void);
int main(void)

{
 print();
}

void print (void)
{
    int v;
    do
    {
        printf("Y: ");
        scanf("%i", &v);

    }
    while (v < 0 || v > 12);
    for (int i = 0; i < v; i++)
    {
        for (int j = v - 1; j > i; j--)
            printf("_");
        for (int k = v + 1; k > v - i; k--)
            printf("*");
        for (int l = v + 1; l > v - i; l--)
            printf(" ");
         for (int j = v - 1; j > i; j--)
            printf("_");
        printf("\n");
    }
}
