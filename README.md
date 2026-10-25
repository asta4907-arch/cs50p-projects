# CS50P Projects

A collection of Python exercises and small projects created while studying CS50's Introduction to Programming with Python.

## Projects

| Project | Description | Run |
|---|---|---|
| Calculator | Calculator exercise | `python CALCULATOR.py` |
| Bitcoin | Convert a Bitcoin amount to USD using CoinCap | See [bitcoin/README.md](bitcoin/README.md) |
| Deep Thought | Answer normalization exercise | `python DEEP/deep.py` |
| Bank | Greeting-based bank exercise | `python bank.py/bank.py` |
| Camel | Convert camelCase text to snake_case | `python camel/camel.py` |
| Coke Machine | Coin and change exercise | `python coke/coke.py` |
| File Extensions | Identify MIME types from file extensions | `python extensions/extensions.py` |
| Fuel Gauge | Convert a fraction to a fuel percentage | `python fuel/fuel.py` |
| Meal Time | Identify meal times | `python meal/meal.py` |
| Nutrition | Look up calories for listed fruits | `python nutrition/nutrition.py` |
| Vanity Plates | Validate a license plate | `python plates/plates.py` |
| Twitter | Remove vowels from text | `python twttr/twttr.py` |

## Setup

Use Python 3.10 or newer. Install the dependencies used by the Bitcoin project:

```bash
python -m pip install -r requirements.txt
```

Most exercises run independently and may prompt for input. For the Bitcoin project's API setup and security notes, read [bitcoin/README.md](bitcoin/README.md).

## Repository hygiene

- Keep API keys and other credentials out of source control.
- Local secrets belong in environment variables; `.env` files are ignored by Git.
- Keep generated Python cache files and virtual environments out of commits.

## Note

These are learning exercises. Some scripts may be refined over time as tests and coursework requirements are reviewed.
