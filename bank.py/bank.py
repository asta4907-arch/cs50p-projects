"""Calculate the bank greeting amount."""


def value(greeting):
    greeting = greeting.strip().casefold()
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    return 100


def main():
    print(f"${value(input('Greeting: '))}")


if __name__ == "__main__":
    main()
