#include <cs50.h>
#include <stdio.h>

int degree(long long x);
int degreepro(long long x);
long long pw(int x, int n);
int even(long long x);
int odd(long long x);

int main(void)
{
    long long cardnumber = get_long_long("tell us your credit card number!\n");
    int d = degree(cardnumber);
    int sum = even(cardnumber) + odd(cardnumber);
    int test = sum % 10;
    if (d == 15 && test == 0)
    {
        printf("AMEX\n");
    }
    else if (d == 13 && test == 0)
    {
        printf("VISA\n");
    }
    else if (d == 16 && test == 0)
    {
        long long m = cardnumber % (pw(10, 15));
        int n = (cardnumber - m) / (pw(10, 15));
        if (n == 5)
        {
            printf("MasterCard\n");
        }
        else if (n == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int even(long long x)
{
    int dp = degreepro(x);
    const long long num = x;
    long long numnow = num;
    int sum = 0;
    for (int mod = 1; mod < dp + 2; mod = mod + 1)
    {
        numnow = num % (10 * pw(100, mod - 1));
        numnow = num - numnow;
        numnow = numnow % (pw(100, mod));
        numnow = numnow / (10 * pw(100, mod - 1));
        numnow = numnow * 2;
        if (numnow >= 10)
        {
            numnow = numnow - 9;
        }
        sum = sum + numnow;
    }
    return (sum);
}

int odd(long long x)
{
    int dp = degreepro(x);
    const long long num = x;
    long long numnow = num;
    int sum = 0;
    for (int mod = 1; mod < dp + 2; mod = mod + 1)
    {
        long long numnow1 = num % (10 * pw(100, mod - 1));
        long long numnow2 = numnow1 % (pw(100, mod - 1));
        long long numnow3 = (numnow1 - numnow2) / ((pw(100, mod - 1)));
        sum = sum + numnow3;
    }
    return sum;
}

long long pw(int x, int n)
{
    long long result = 1;
    for (int i = 1; i <= n; i++)
    {
        result = result * x;
    }
    return result;
}

int degreepro(long long x)
{
    int degre = degree(x) / 2;
    return degre;
}

int degree(long long x)
{
    int degre = 0;
    while (x != 0)
    {
        x = x / 10;
        degre++;
    }
    return degre;
}
