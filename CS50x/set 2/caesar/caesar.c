#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int n = strlen(argv[1]);
    for (int i = 0; i < n; i++)
    {
        if (isalpha(argv[1][i]))
        {
            // print error
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    string pt = get_string("plaintext:  ");
    // convert str to int
    int key = atoi(argv[1]);

    char c_output;
    int N = strlen(pt);
    char cipher[N];

    for (int j = 0; j < N; j++)
    {
        int c = pt[j];

        if (isalpha(c))
        {
            c_output = c + key % 26;

            if (!(islower(c_output) || isupper(c_output)))
            {
                c_output -= 26;
            }
        }
        else
        {
            c_output = c;
        }

        cipher[j] = c_output;
    }

    printf("ciphertext: %s\n", cipher);
    return 0;
}