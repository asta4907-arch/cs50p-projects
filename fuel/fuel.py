"""Convert a fuel fraction to a gauge reading."""


def convert(fraction):
    numerator_text, denominator_text = fraction.split("/")
    numerator, denominator = int(numerator_text), int(denominator_text)
    if denominator <= 0 or numerator < 0 or numerator > denominator:
        raise ValueError("Fraction must be between 0 and 1.")
    return round(numerator / denominator * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


def main():
    while True:
        try:
            print(gauge(convert(input("Fraction: "))))
            return
        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
