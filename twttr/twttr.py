"""Remove vowels from a string."""

VOWELS = set("aeiouAEIOU")


def shorten(text):
    return "".join(char for char in text if char not in VOWELS)


def main():
    print(shorten(input("Input: ")))


if __name__ == "__main__":
    main()
