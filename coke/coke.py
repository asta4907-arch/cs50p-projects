"""Simulate a vending machine accepting 25, 10, and 5 cent coins."""


def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            continue
        if coin in {25, 10, 5}:
            amount_due -= coin
    print(f"Change Owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
