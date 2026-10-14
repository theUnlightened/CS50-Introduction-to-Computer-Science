def luhn(card):
    total = 0
    position = 0

    while card > 0:
        digit = card % 10
        card //= 10

        if position % 2 == 1:
            digit *= 2

            if digit >= 10:
                digit -= 9

        total += digit
        position += 1

    return total % 10 == 0


def length(card):
    count = 0

    while card > 0:
        card //= 10
        count += 1

    return count


def first_two(card):
    while card >= 100:
        card //= 10

    return card


def main():
    card = int(input("Number: "))

    digits = length(card)
    first = first_two(card)

    if not luhn(card):
        print("INVALID")
        return

    # AMEX: 15 digits, starts with 34 or 37
    if digits == 15 and (first == 34 or first == 37):
        print("AMEX")

    # Mastercard: 16 digits, starts 51-55
    elif digits == 16 and 51 <= first <= 55:
        print("MASTERCARD")

    # VISA: 13 or 16 digits, starts 4
    elif (digits == 13 or digits == 16) and first // 10 == 4:
        print("VISA")

    else:
        print("INVALID")


main()
