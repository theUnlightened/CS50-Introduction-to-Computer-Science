#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int length(string s);
int givenum(char letter);

int num[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    string player1 = get_string("Player 1: ");
    string player2 = get_string("Player 2: ");
    int l1 = length(player1);
    int l2 = length(player2);

    int sum1 = 0;
    for (int i = 0; i < l1; i++)
    {
        sum1 = givenum(player1[i]) + sum1;
    }

    int sum2 = 0;
    for (int i = 0; i < l2; i++)
    {
        sum2 = givenum(player2[i]) + sum2;
    }

    if (sum1 > sum2)
    {
        printf("Player 1 wins\n");
    }
    else if (sum2 > sum1)
    {
        printf("Player 2 wins\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int length(string s)
{
    int count = 0;
    while (s[count] != 0)
    {
        count++;
    }
    return count;
}

int givenum(char letter)
{
    if (letter < 'A' || letter > 'z')
    {
        return 0;
    }
    else if (letter > 'Z' && letter < 'a')
    {
        return 0;
    }
    int loct = 0;
    while (loct != toupper(letter) - 65)
    {
        loct++;
    }
    return num[loct];
}



    for (int loct = 0; loct < LENGTH; loct++)
    {
        if (tx[loct] > 32 && tx[loct] < 48)
        {
            wordnum++;
        }
        else if (tx[loct] > 57 && tx[loct] < 65)
        {
            wordnum++;
        }
        else if (tx[loct] > 90 && tx[loct] < 97)
        {
            wordnum++;
        }
        else if (tx[loct] > 122 && tx[loct] < 127)
        {
            wordnum++;
        }
