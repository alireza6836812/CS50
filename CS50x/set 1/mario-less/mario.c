#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;

    // make a loop to get the number of height between 1 and 8
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 0; i < height; i++)
    {
        // add spaces
        for (int k = height - i; k > 1; k--)
        {
            printf(" ");
        }
        // add hashes
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}