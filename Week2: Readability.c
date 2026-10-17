#include <cs50.h>
#include <stdio.h>
#include <string.h>

int sentence(string tx);
int letter(string tx);
int word(string tx);
float L(string tx);
float S(string tx);

int main(void)
{
    string text = get_string("Text: ");
    float index = 0.0588 * L(text) - 0.296 * S(text) - 15.8;
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 1 && index < 16)
    {
        int grade = 1;
        while (index >= grade + 0.5)
        {
            grade++;
        }
        printf("Grade %i\n", grade);
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    return 0;
}

int sentence(string tx)
{
    int sennum = 0;
    const int LENGTH = strlen(tx);
    for (int loct = 0; loct < LENGTH; loct++)
    {
        if (tx[loct] == '!' || tx[loct] == '?' || tx[loct] == '.')
        {
            sennum++;
        }
    }
    return sennum;
}

int letter(string tx)
{
    int letnum = 0;
    const int LENGTH = strlen(tx);
    for (int loct = 0; loct < LENGTH; loct++)
    {
        if (tx[loct] <= 'Z' && tx[loct] >= 'A')
        {
            letnum++;
        }
        else if (tx[loct] >= 'a' && tx[loct] <= 'z')
        {
            letnum++;
        }
    }
    return letnum;
}

int word(string tx)
{
    int wordnum = 1;
    const int LENGTH = strlen(tx);
    for (int i = 0; i < LENGTH; i++)
    {
        if (tx[i] == ' ')
        {
            wordnum++;
        }
    }
    return wordnum;
}

float L(string tx)
{
    float l = ((float) letter(tx) / word(tx)) * 100;
    return l;
}

float S(string tx)
{
    float s = ((float) sentence(tx) / word(tx)) * 100;
    return s;
}
