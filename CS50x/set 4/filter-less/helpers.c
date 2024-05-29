#include "helpers.h"
#include <math.h>

// make a grayscale from image by using for loops
void grayscale(int h, int w, RGBTRIPLE image[h][w])
{
    // first loop
    for (int i = 0; i < h; i++)
    {
        // second loop
        for (int j = 0; j < w; j++)
        {
            int rgbt = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = rgbt;
        }
    }
    return;
}

// make a sepia from image by using for loops
void sepia(int h, int w, RGBTRIPLE image[h][w])
{
    // first loop
    for (int i = 0; i < h; i++)
    {
        // second loop
        for (int j = 0; j < w; j++)
        {
            // make 3 int for Blue, Green and Red and move in the image rows and columns
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);

            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
        }
    }
    return;
}

// Reflection of the image relative to the horizontal axis by using for loops
void reflect(int h, int w, RGBTRIPLE image[h][w])
{
    // first loop
    for (int i = 0; i < h; i++)
    {
        if (w % 2 == 0)
        {
            // second loop
            for (int j = 0; j < w / 2; j++)
            {
                RGBTRIPLE temp[h][w];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][w - (j + 1)];
                image[i][w - (j + 1)] = temp[i][j];
            }
        }

        else if (w % 2 != 0)
        {
            for (int j = 0; j < (w - 1) / 2; j++)
            {
                RGBTRIPLE temp[h][w];
                temp[i][j] = image[i][j];
                image[i][j] = image[i][w - (j + 1)];
                image[i][w - (j + 1)] = temp[i][j];
            }
        }
    }
    return;
}

// Blur the image by using for loops
void blur(int h, int w, RGBTRIPLE image[h][w])
{
    RGBTRIPLE temp[h][w];

    // first loop
    for (int i = 0; i < h; i++)
    {
        // second loop
        for (int j = 0; j < w; j++)
        {
            // make some floats for eazh color
            float sumBlue = 0;
            float sumGreen = 0;
            float sumRed = 0;
            float counter = 0;

            // third loop
            for (int r = -1; r < 2; r++)
            {
                // forth loop
                for (int c = -1; c < 2; c++)
                {
                    if (i + r < 0 || i + r > h - 1)
                    {
                        continue;
                    }

                    if (j + c < 0 || j + c > w - 1)
                    {
                        continue;
                    }

                    sumBlue += image[i + r][j + c].rgbtBlue;
                    sumGreen += image[i + r][j + c].rgbtGreen;
                    sumRed += image[i + r][j + c].rgbtRed;
                    counter++;
                }
            }

            temp[i][j].rgbtBlue = round(sumBlue / counter);
            temp[i][j].rgbtGreen = round(sumGreen / counter);
            temp[i][j].rgbtRed = round(sumRed / counter);
        }
    }

    // fifth loop
    for (int i = 0; i < h; i++)
    {
        // sixth loop
        for (int j = 0; j < w; j++)
        {
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
        }
    }

    return;
}
