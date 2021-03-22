#include <stdio.h>

float avg();

// Asks for 4 scores of wish to calculate the avgrage of scores
const int TOTAL = 4;

int main(void)
{

    int SCORES[TOTAL];
    for (int i = 0; i < TOTAL; i++)
    {

        printf("Scores: ");
        scanf("%i", &SCORES[i]);

    }

    printf("A : %f\n", (avg(TOTAL, SCORES)));

}

float avg(int lenght, int array[])
{
   int am = 0;
   for (int i = 0; i < lenght; i++)
   {
       am = am + array[i];
   }
   return am / (float) lenght;
}
