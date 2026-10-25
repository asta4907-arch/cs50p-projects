"""A small command-line calculator."""


def main():
    try:
        first = float(input("First number: "))
        operator = input("Operation (+, -, *, /): ").strip()
        second = float(input("Second number: "))
    except ValueError:
        print("Error: enter valid numbers.")
        return

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Error: cannot divide by zero.")
            return
        result = first / second
    else:
        print("Error: unsupported operation.")
        return
    print(f"Result: {result:g}")


if __name__ == "__main__":
    main()
