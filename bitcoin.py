import requests
import sys
def main():
    if len(sys.argv) != 2:
        print("Enter command line argument")
        sys.exit(1)

    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Error: Amount must be a number")
        sys.exit(1)

    try:
        response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=45f977a4cdce66a1508a5be5260150bd2dfe3a40002f81ce54b31b825c6adc15')
        content = response.json()
        price = content['data']['priceUsd']
        amt = value * float(price)
        print(f"Amount in USD: ${amt:,.4f}")
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()