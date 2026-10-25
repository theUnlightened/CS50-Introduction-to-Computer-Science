#include <stdio.h>
#include <stdlib.h>

int *sieve(int n, size_t *prime_count);
size_t compute(int n, const int *primes, size_t prime_count);


int main(void)
{
    int n;

    printf("Enter the maximum even integer N >= 4: ");

    if (scanf("%d", &n) != 1 || n < 4)
    {
        printf("Invalid input. Please enter an integer >= 4.\n");
        return 1;
    }

    size_t prime_count = 0;
    int *primes = sieve(n, &prime_count);

    if (primes == NULL)
    {
        printf("Failed to generate primes.\n");
        return 1;
    }

    FILE *file = fopen("goldbach_results.csv", "w");

    if (file == NULL)
    {
        printf("Could not create CSV file.\n");
        free(primes);
        return 1;
    }

    fprintf(file, "N,G\n");

    size_t scanned = 0;
    size_t min_g = (size_t)-1;
    size_t max_g = 0;
    int min_n = 0;
    int max_n = 0;

    for (int i = 4; i <= n; i += 2)
    {
        size_t g = compute(i, primes, prime_count);

        fprintf(file, "%d,%zu\n", i, g);

        if (g < min_g)
        {
            min_g = g;
            min_n = i;
        }

        if (g > max_g)
        {
            max_g = g;
            max_n = i;
        }

        scanned++;
    }

    if (fclose(file) != 0)
    {
        printf("Failed to finish writing the CSV file.\n");
        free(primes);
        return 1;
    }

    printf("\nExperiment completed.\n");
    printf("Maximum N: %d\n", n);
    printf("Even integers scanned: %zu\n", scanned);
    printf("Minimum G(N): %zu at N = %d\n", min_g, min_n);
    printf("Maximum G(N): %zu at N = %d\n", max_g, max_n);
    printf("Results saved to goldbach_results.csv\n");

    free(primes);
    return 0;
}


int *sieve(int n, size_t *prime_count)
{
    char *is_prime = malloc(((size_t)n + 1) * sizeof *is_prime);

    if (is_prime == NULL)
    {
        return NULL;
    }

    for (int i = 0; i <= n; i++)
    {
        is_prime[i] = 1;
    }

    is_prime[0] = 0;
    is_prime[1] = 0;

    for (int p = 2; p <= n / p; p++)
    {
        if (is_prime[p])
        {
            for (int multiple = p * p; multiple <= n; multiple += p)
            {
                is_prime[multiple] = 0;
            }
        }
    }

    size_t capacity = 16;
    size_t size = 0;

    int *primes = malloc(capacity * sizeof *primes);

    if (primes == NULL)
    {
        free(is_prime);
        return NULL;
    }

    for (int i = 2; i <= n; i++)
    {
        if (is_prime[i])
        {
            if (size == capacity)
            {
                size_t new_capacity = capacity * 2;

                int *temp = realloc(
                    primes,
                    new_capacity * sizeof *primes
                );

                if (temp == NULL)
                {
                    free(primes);
                    free(is_prime);
                    return NULL;
                }

                primes = temp;
                capacity = new_capacity;
            }

            primes[size++] = i;
        }
    }

    free(is_prime);
    *prime_count = size;

    return primes;
}


size_t compute(int n, const int *primes, size_t prime_count)
{
    size_t pair_count = 0;

    for (size_t i = 0; i < prime_count; i++)
    {
        if (primes[i] > n / 2)
        {
            break;
        }

        int target = n - primes[i];

        size_t left = i;
        size_t right = prime_count;

        while (left < right)
        {
            size_t mid = left + (right - left) / 2;

            if (primes[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }

        if (left < prime_count && primes[left] == target)
        {
            pair_count++;
        }
    }

    return pair_count;
}
