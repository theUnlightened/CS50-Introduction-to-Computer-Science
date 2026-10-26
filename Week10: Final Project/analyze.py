
import csv
import os
import statistics
import matplotlib.pyplot as plt


# ==========================================
# 1. Configuration
# ==========================================

INPUT_FILE = "goldbach_results.csv"
OUTPUT_DIR = "results"


# ==========================================
# 2. Read CSV data
# ==========================================

def load_data(filename):
    """Read N and G(N) from a CSV file."""

    numbers = []
    counts = []

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("The CSV file is empty.")

        if not {"N", "G"}.issubset(set(reader.fieldnames)):
            raise ValueError("CSV must contain columns named N and G.")

        for row_number, row in enumerate(reader, start=2):
            try:
                n = int(row["N"])
                g = int(row["G"])
            except (ValueError, TypeError):
                raise ValueError(
                    f"Invalid integer at CSV row {row_number}."
                ) from None

            numbers.append(n)
            counts.append(g)

    if not numbers:
        raise ValueError("The CSV contains no data rows.")

    return numbers, counts


# ==========================================
# 3. Validate the input data
# ==========================================

def validate_data(numbers, counts):
    """Check the basic consistency of the CSV data."""

    errors = []

    if len(numbers) != len(counts):
        errors.append("The numbers and counts have different lengths.")
        return errors

    if any(n < 4 or n % 2 != 0 for n in numbers):
        errors.append("Every N must be an even integer >= 4.")

    if any(g < 1 for g in counts):
        errors.append("Every G(N) must be a positive integer.")

    if numbers != sorted(numbers):
        errors.append("N values are not sorted in ascending order.")

    if len(set(numbers)) != len(numbers):
        errors.append("Duplicate N values were found.")

    expected = list(range(numbers[0], numbers[-1] + 1, 2))

    if numbers != expected:
        errors.append(
            "The N values are not a complete sequence of even integers "
            "between the first and last values."
        )

    return errors


# ==========================================
# 4. Independently verify Goldbach counts
# ==========================================

def verify_goldbach(numbers, counts):
    """
    Build a prime table independently and recompute G(N).

    Return:
        passed: number of matching rows
        mismatches: rows containing (N, recorded G, computed G)
    """

    if not numbers:
        return 0, []

    limit = max(numbers)

    # Build a Sieve of Eratosthenes.
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p <= limit:
        if is_prime[p]:
            multiple = p * p

            while multiple <= limit:
                is_prime[multiple] = False
                multiple += p

        p += 1

    # Recompute G(N) from the prime table.
    mismatches = []

    for n, recorded_g in zip(numbers, counts):
        actual_g = 0

        for p in range(2, n // 2 + 1):
            q = n - p

            if is_prime[p] and is_prime[q]:
                actual_g += 1

        if actual_g != recorded_g:
            mismatches.append((n, recorded_g, actual_g))

    passed = len(numbers) - len(mismatches)

    return passed, mismatches


# ==========================================
# 5. Calculate summary statistics
# ==========================================

def analyze_data(numbers, counts):
    """Calculate descriptive statistics."""

    minimum_g = min(counts)
    maximum_g = max(counts)

    minimum_n = [
        n for n, g in zip(numbers, counts)
        if g == minimum_g
    ]

    maximum_n = [
        n for n, g in zip(numbers, counts)
        if g == maximum_g
    ]

    return {
        "data_points": len(numbers),
        "first_N": numbers[0],
        "last_N": numbers[-1],
        "mean": statistics.mean(counts),
        "median": statistics.median(counts),
        "minimum_G": minimum_g,
        "minimum_N": minimum_n,
        "maximum_G": maximum_g,
        "maximum_N": maximum_n,
    }


# ==========================================
# 6. Save verification details
# ==========================================

def save_verification(numbers, counts, filename):
    """Save the independently computed G(N) for each row."""

    limit = max(numbers)

    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while p * p <= limit:
        if is_prime[p]:
            multiple = p * p

            while multiple <= limit:
                is_prime[multiple] = False
                multiple += p

        p += 1

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["N", "C_G", "Python_G", "Match"]
        )

        for n, recorded_g in zip(numbers, counts):
            actual_g = sum(
                1
                for p in range(2, n // 2 + 1)
                if is_prime[p] and is_prime[n - p]
            )

            writer.writerow([
                n,
                recorded_g,
                actual_g,
                recorded_g == actual_g
            ])


# ==========================================
# 7. Save the text report
# ==========================================

def save_report(summary, errors, passed, mismatches, filename):
    """Write statistics and verification results to a text report."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Goldbach Lab - Experiment Report\n")
        file.write("=" * 45 + "\n\n")

        file.write("DATA SUMMARY\n")
        file.write("-" * 45 + "\n")
        file.write(f"Data points: {summary['data_points']}\n")
        file.write(
            f"N range: {summary['first_N']} to {summary['last_N']}\n"
        )
        file.write(f"Mean G(N): {summary['mean']:.4f}\n")
        file.write(f"Median G(N): {summary['median']}\n")
        file.write(f"Minimum G(N): {summary['minimum_G']}\n")
        file.write(f"N with minimum G: {summary['minimum_N']}\n")
        file.write(f"Maximum G(N): {summary['maximum_G']}\n")
        file.write(f"N with maximum G: {summary['maximum_N']}\n\n")

        file.write("DATA VALIDATION\n")
        file.write("-" * 45 + "\n")

        if errors:
            for error in errors:
                file.write(f"WARNING: {error}\n")
        else:
            file.write("Basic consistency checks passed.\n")

        file.write("\nINDEPENDENT VERIFICATION\n")
        file.write("-" * 45 + "\n")
        file.write(
            f"Matching rows: {passed}/{summary['data_points']}\n"
        )

        if mismatches:
            file.write("Mismatches (N, C_G, Python_G):\n")

            for item in mismatches:
                file.write(f"{item}\n")
        else:
            file.write("All rows matched.\n")

        file.write(
            "\nSCIENTIFIC LIMITATION\n"
            "This program checks a finite set of computed values. "
            "Agreement between implementations is not a proof of "
            "Goldbach's conjecture for all even integers.\n"
        )


# ==========================================
# 8. Generate figures
# ==========================================

def create_plots(numbers, counts, output_dir):
    """Generate three plots and save them as PNG files."""

    # Figure 1: G(N) against N.
    plt.figure(figsize=(10, 6))
    plt.scatter(numbers, counts, s=14)
    plt.xlabel("Even integer N")
    plt.ylabel("Goldbach partition count G(N)")
    plt.title("Goldbach Partition Count")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "goldbach_scatter.png"),
        dpi=200
    )
    plt.close()

    # Figure 2: Frequency of each G(N) value.
    frequencies = {}

    for g in counts:
        frequencies[g] = frequencies.get(g, 0) + 1

    values = sorted(frequencies)
    amounts = [frequencies[g] for g in values]

    plt.figure(figsize=(10, 6))
    plt.bar(values, amounts)
    plt.xlabel("Goldbach partition count G(N)")
    plt.ylabel("Number of even integers")
    plt.title("Frequency Distribution of G(N)")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "goldbach_frequency.png"),
        dpi=200
    )
    plt.close()

    # Figure 3: Mean G(N) over consecutive blocks.
    block_size = max(1, len(numbers) // 20)

    block_centers = []
    block_means = []

    for start in range(0, len(numbers), block_size):
        block_ns = numbers[start:start + block_size]
        block_gs = counts[start:start + block_size]

        block_centers.append(
            (block_ns[0] + block_ns[-1]) / 2
        )
        block_means.append(statistics.mean(block_gs))

    plt.figure(figsize=(10, 6))
    plt.plot(block_centers, block_means, marker="o", markersize=3)
    plt.xlabel("N (block midpoint)")
    plt.ylabel("Mean G(N) within block")
    plt.title("Block Averages of Goldbach Partition Counts")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, "goldbach_block_means.png"),
        dpi=200
    )
    plt.close()


# ==========================================
# 9. Main program
# ==========================================

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Cannot find {INPUT_FILE}")
        print("Place it in the same directory as analyze.py.")
        return

    try:
        numbers, counts = load_data(INPUT_FILE)
    except (OSError, ValueError, csv.Error) as error:
        print(f"Error reading CSV: {error}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    errors = validate_data(numbers, counts)

    # Do not interpret malformed data as a valid experiment.
    if errors:
        print("Data validation warnings:")

        for error in errors:
            print(f"- {error}")

        print("Please fix the input data before continuing.")
        return

    summary = analyze_data(numbers, counts)
    passed, mismatches = verify_goldbach(numbers, counts)

    print("\nGoldbach Lab - Summary")
    print("=" * 40)
    print(f"Data points: {summary['data_points']}")
    print(f"N range: {summary['first_N']} to {summary['last_N']}")
    print(f"Mean G(N): {summary['mean']:.4f}")
    print(f"Median G(N): {summary['median']}")
    print(f"Minimum G(N): {summary['minimum_G']}")
    print(f"N with minimum: {summary['minimum_N']}")
    print(f"Maximum G(N): {summary['maximum_G']}")
    print(f"N with maximum: {summary['maximum_N']}")

    print("\nIndependent verification")
    print("-" * 40)
    print(f"Matching rows: {passed}/{len(numbers)}")

    if mismatches:
        print("Mismatches (N, C_G, Python_G):")

        for item in mismatches[:10]:
            print(item)

        if len(mismatches) > 10:
            print(f"... and {len(mismatches) - 10} more.")
    else:
        print("All rows matched.")

    try:
        create_plots(numbers, counts, OUTPUT_DIR)

        save_verification(
            numbers,
            counts,
            os.path.join(OUTPUT_DIR, "verification.csv")
        )

        save_report(
            summary,
            errors,
            passed,
            mismatches,
            os.path.join(OUTPUT_DIR, "report.txt")
        )

    except (OSError, ValueError) as error:
        print(f"Error generating results: {error}")
        return

    print(f"\nResults saved in '{OUTPUT_DIR}/'.")
    print(" - goldbach_scatter.png")
    print(" - goldbach_frequency.png")
    print(" - goldbach_block_means.png")
    print(" - verification.csv")
    print(" - report.txt")


if __name__ == "__main__":
    main()
