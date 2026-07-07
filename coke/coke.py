print("Amount due: 50")
def main():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")
            continue
        if coin in [25, 10, 5]:
            amount_due -= coin
        
    print(f"Change Owed: {abs(amount_due)}")
main()