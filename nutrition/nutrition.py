"""Look up approximate calories for selected fruits."""

CALORIES = {
    "apple": 130, "avocado": 50, "banana": 110,
    "kiwifruit": 90, "pear": 100, "sweet cherries": 100,
}


def main():
    item = input("Item: ").strip().casefold()
    if item in CALORIES:
        print(f"Calories: {CALORIES[item]}")


if __name__ == "__main__":
    main()
