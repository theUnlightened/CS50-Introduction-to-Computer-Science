#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string key0 = argv[1];
        int other = 0;
        const int K = strlen(key0);
        for (int i = 0; i < K ;i++)
        {
            if (key0[i] < 65 || key0[i] > 123)
            {
                other++;
            }
            else if (key0[i] > 90 && key0[i] < 97)
            {
                other++;
            }
        }
        if (other == 0)
        {
            const int LENG = strlen(key0);
            char key[LENG + 1];
            for (int i = 0; i < LENG; i++)
            {
                key[i] = toupper(key0[i]);
            }
            key[LENG] = '\0';
            int repeat = 0;
            for (int i=0 ; i < LENG ; i++)
            {
                for ( int j = 0; j <LENG ;j++)
                {
                    if (key[j] == key[i])
                    {
                        repeat++;
                    }
                }
            }
            repeat = repeat -26;
            if (repeat == 0)
            {
                if (LENG == 26)
                {
                    string plaintext = get_string("Plaintext: \n");
                    const int LENGTH = strlen(plaintext);
                    char ciphertext[LENGTH + 1];
                    printf("ciphertext: ");
                    for (int i = 0 ; i < LENGTH ; i++)
                    {
                        if (plaintext[i] > 64 && plaintext[i] < 91)
                        {
                            int loct = plaintext[i] - 65;
                            ciphertext[i] = key0[loct];
                            printf("%c",toupper(ciphertext[i]));
                        }
                        else if (plaintext[i] > 96 && plaintext[i] < 123)
                        {
                            int loct = plaintext[i] - 97;
                            ciphertext[i] = key0[loct];
                            printf("%c",tolower(ciphertext[i]));
                        }
                        else if (plaintext[i] == ' ')
                        {
                            printf(" ");
                        }
                        else
                        {
                            printf("%c",plaintext[i]);
                        }
                    }
                    ciphertext[LENGTH] = '\0';
                    printf("\n");
                }
                else
                {
                    printf("The key must contain 26 letters\n");
                    return 1;
                }
            }
            else
            {
                printf("Having Repeated Numbers\n");
                return 1;
            }
        }
        else
        {
            return 1;
        }
    }
    else
    {
    printf("Print keys or extra arguments\n");
    return 1;
    }
}
