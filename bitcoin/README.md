# Bitcoin Price Converter

Fetches Bitcoin's current USD price from the CoinCap API and multiplies it by an amount supplied on the command line.

## Requirements

- Python 3.10+
- A CoinCap API key
- The dependency listed in the repository's `requirements.txt`

## Setup

From the repository root, install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set your API key as an environment variable. Do not paste a real key into source code or commit it to Git.

**PowerShell**
```powershell
$env:COINCAP_API_KEY = "your_new_api_key"
python bitcoin/bitcoin.py 1.5
```

**Windows Command Prompt**
```bat
set COINCAP_API_KEY=your_new_api_key
python bitcoin/bitcoin.py 1.5
```

**macOS / Linux**
```bash
export COINCAP_API_KEY="your_new_api_key"
python bitcoin/bitcoin.py 1.5
```

A template is provided in `.env.example` for reference, but this script reads the key from the process environment and does not load `.env` automatically.

## Security

- The real key must never be committed.
- The repository's `.gitignore` excludes `.env` files.
- Because a key was previously committed to a public repository, revoke/rotate it with CoinCap before using this version. Moving the code does not remove the old key from Git history.
