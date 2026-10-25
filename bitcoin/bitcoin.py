"""Convert a Bitcoin amount to USD using the CoinCap API.

Set COINCAP_API_KEY in your environment before running this script.
Never commit a real API key or a .env file.
"""
import os
import sys

import requests

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"
REQUEST_TIMEOUT_SECONDS = 10


def get_bitcoin_price(api_key: str) -> float:
    """Fetch the current Bitcoin price in USD."""
    response = requests.get(
        API_URL,
        params={"apiKey": api_key},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    payload = response.json()
    return float(payload["data"]["priceUsd"])


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python bitcoin/bitcoin.py AMOUNT", file=sys.stderr)
        return 2

    try:
        amount = float(sys.argv[1])
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Error: AMOUNT must be a non-negative number.", file=sys.stderr)
        return 2

    api_key = os.environ.get("COINCAP_API_KEY")
    if not api_key:
        print(
            "Error: COINCAP_API_KEY is not set. See bitcoin/README.md.",
            file=sys.stderr,
        )
        return 1

    try:
        price_usd = get_bitcoin_price(api_key)
    except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
        print(f"Error fetching Bitcoin price: {exc}", file=sys.stderr)
        return 1

    print(f"Amount in USD: ${amount * price_usd:,.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
