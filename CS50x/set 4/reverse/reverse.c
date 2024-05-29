#include "wav.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// check format:
int cf(WAVHEADER header);
// get block size:
int gb(WAVHEADER header);
int main(int argc, char *argv[])
{

    // Cheking the correctness of the proper usage
    if (argc != 3)
    {
        printf("incorrect usage.\n");
        return 1;
    }

    // open the input file and then read it
    char *infile = argv[1];
    char *outfile = argv[2];

    // open the input file while it's in reading mode
    FILE *input = fopen(infile, "r");
    if (input == NULL)
    {
        printf("incorrect input.\n");
        fclose(input);
        return 1;
    }

    // read file header from input file
    WAVHEADER fheader;
    fread(&fheader, sizeof(WAVHEADER), 1, input);

    // we will check the format to be sure it's WAV
    if (cf(fheader) != 0)
    {
        fclose(input);
        return 1;
    }

    // we open a file to write in it
    FILE *output = fopen(outfile, "w");
    if (output == NULL)
    {
        printf("Output file unsuccesful");
        fclose(output);
        fclose(input);
        return 1;
    }

    // we write header to output file
    fwrite(&fheader, sizeof(WAVHEADER), 1, output);

    // calculating the size of block by using get_back_size
    int size = gb(fheader);

    // writing the reversed audio to file
    BYTE buffer[size];
    for (fseek(input, 0 - size, SEEK_END); ftell(input) > sizeof(fheader) - size; fseek(input, 0 - (size * 2), SEEK_CUR))
    {
        fread(&buffer, size, 1, input);
        fwrite(&buffer, size, 1, output);
    }

    fclose(input);
    fclose(output);
    return 0;
}

int cf(WAVHEADER header)
{
    // characters array
    int wav[] = {0x57, 0x41, 0x56, 0x45};
    int i;
    for (i = 0; i < 4; i++)
    {
        // we check if chars are not match those in file format descriptor
        if (header.format[i] != wav[i])
        {
            printf("its not a valid WAV file.\n");
            return 1;
        }
    }
    return 0;
}

int gb(WAVHEADER header)
{

    // we se block size in bytes as 4
    int num;
    num = header.numChannels * (header.bitsPerSample / 8);

    return num;
}