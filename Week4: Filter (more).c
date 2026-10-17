#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            int R = image[h][w].rgbtRed;
            int G = image[h][w].rgbtGreen;
            int B = image[h][w].rgbtBlue;
            image[h][w].rgbtRed = round((R + G + B)/3.0);
            image[h][w].rgbtGreen = round((R + G + B)/3.0);
            image[h][w].rgbtBlue = round((R + G + B)/3.0);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copyimage[height][width];
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            copyimage[i][j] = image[i][j];
        }
    }
    for (int i = 0 ; i < height ; i++)
    {
        for (int j = 0 ; j < width ; j++)
        {
            image[i][j] = copyimage[i][width-1-j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copyimage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copyimage[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int m = 0;
            int red = 0;
            int green = 0;
            int blue = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni < 0 || ni >= height || nj < 0 || nj >= width)
                    {
                        m++;
                        continue;
                    }

                    blue += copyimage[ni][nj].rgbtBlue;
                    red += copyimage[ni][nj].rgbtRed;
                    green += copyimage[ni][nj].rgbtGreen;
                }
            }

            image[i][j].rgbtRed = round((double) red / (9 - m));
            image[i][j].rgbtGreen = round((double) green / (9 - m));
            image[i][j].rgbtBlue = round((double) blue / (9 - m));
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copyimage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copyimage[i][j] = image[i][j];
        }
    }

    int Gx[3][3] =
    {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };

    int Gy[3][3] =
    {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}
    };

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double gxR = 0, gyR = 0;
            double gxG = 0, gyG = 0;
            double gxB = 0, gyB = 0;

            // Look at the 3x3 area around (i, j)
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    // Outside the image = 0
                    if (ni < 0 || ni >= height || nj < 0 || nj >= width)
                    {
                        continue;
                    }

                    int x = di + 1;
                    int y = dj + 1;

                    gxR += copyimage[ni][nj].rgbtRed * Gx[x][y];
                    gyR += copyimage[ni][nj].rgbtRed * Gy[x][y];

                    gxG += copyimage[ni][nj].rgbtGreen * Gx[x][y];
                    gyG += copyimage[ni][nj].rgbtGreen * Gy[x][y];

                    gxB += copyimage[ni][nj].rgbtBlue * Gx[x][y];
                    gyB += copyimage[ni][nj].rgbtBlue * Gy[x][y];
                }
            }

            int red = round(sqrt(gxR * gxR + gyR * gyR));
            int green = round(sqrt(gxG * gxG + gyG * gyG));
            int blue = round(sqrt(gxB * gxB + gyB * gyB));

            if (red > 255)
            {
                red = 255;
            }

            if (green > 255)
            {
                green = 255;
            }

            if (blue > 255)
            {
                blue = 255;
            }

            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}
