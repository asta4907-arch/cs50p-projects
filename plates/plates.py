"""Validate vanity plate strings."""


def is_valid(plate):
    if not 2 <= len(plate) <= 6 or not plate[:2].isalpha() or not plate.isalnum():
        return False
    digits_start = next(
        (index for index, char in enumerate(plate) if char.isdigit()), len(plate)
    )
    if digits_start < len(plate):
        if plate[digits_start] == "0" or not plate[digits_start:].isdigit():
            return False
    return True


def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


if __name__ == "__main__":
    main()
