"""Answer the Great Question of Life, the Universe, and Everything."""


def main():
    answer = input(
        "What is the answer to the Great Question of Life, "
        "the Universe, and Everything? "
    ).strip().casefold()
    print("Yes" if answer in {"42", "forty two", "forty-two"} else "No")


if __name__ == "__main__":
    main()
