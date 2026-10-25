"""Convert camelCase text to snake_case."""


def to_snake_case(text):
    result = []
    for char in text:
        if char.isupper():
            result.extend(("_", char.lower()))
        else:
            result.append(char)
    return "".join(result)


def main():
    print(f"snake_case: {to_snake_case(input('camelCase: '))}")


if __name__ == "__main__":
    main()
