import csv
import sys
from sys import argv


def main():

    # Check for command-line usage
    if len(argv) != 3:
        print("Missing command-line argument")
        sys.exit(1)

    # Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        str_names = []
        for key in reader.fieldnames:
            if key != "name":
                str_names.append(key)
        for row in reader:
            rows.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        sequence = file.read().strip()

    # Find longest match of each STR in DNA sequence
    count = {}
    for str_name in str_names:
        count[str_name] = longest_match(sequence, str_name)

    # TODO: Check database for matching profiles
    for row in rows:
        match = True
        for s in str_names:
            if count[s] != int(row[s]):
                match = False
                break
        if match:
            print(row["name"])
            return

    print("No Match")
    return


def longest_match(sequence, subsequence):
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0

        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


main()
