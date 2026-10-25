#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long long cardnumber = get_long_long("Number: ");

    long long temp = cardnumber;
    int sum = 0;
    int count = 0;
    long long first_two_digits = 0;
    long long first_digit = 0;

    while (temp > 0)
    {
        int digit = temp % 10;

        if (count % 2 == 0)
        {
            sum += digit;
        }
        else
        {
            int multiplied = digit * 2;
            sum += (multiplied / 10) + (multiplied % 10);
        }

        if (temp < 100 && temp >= 10)
        {
            first_two_digits = temp;
        }
        if (temp < 10)
        {
            first_digit = temp;
        }

        temp /= 10;
        count++;
    }

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    if (count == 15 && (first_two_digits == 34 || first_two_digits == 37))
    {
        printf("AMEX\n");
    }

    else if (count == 16 && (first_two_digits >= 51 && first_two_digits <= 55))
    {
        printf("MasterCard\n");
    }

    else if ((count == 13 || count == 16) && first_digit == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }

    return 0;
}
