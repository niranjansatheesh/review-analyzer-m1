# Review Analyzer

A lightweight Python tool for classifying customer product reviews.

## Purpose
Normalizes review text (lowercase, collapsed whitespace) and labels each review
as `positive` (contains "good"), `negative` (contains "bad") or `unknown`.
It is a teaching project for Git workflows; no model training is involved.

## Prerequisites
- Python 3.8 or newer
- Git
- (optional) pytest

## Installation
```bash
git clone https://github.com/YOUR-USERNAME/review-analyzer-m1.git
cd review-analyzer-m1
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest               # optional, only for running tests with pytest
```

## Run
```bash
python3 app.py
```

## Tests
```bash
python3 test_app.py   # or: pytest
```

## Example input / output
| Input                             | Output     |
|-----------------------------------|------------|
| `"Good product"`                  | `positive` |
| `"  BAD quality,  broke  "`       | `negative` |
| `"It arrived on Tuesday"`         | `unknown`  |

Running `python3 app.py` prints:
```
positive
```

## Project structure
```
review-analyzer-m1/
├── app.py          # normalize_review() and classify_review()
├── test_app.py     # assertion-based tests
├── README.md       # this documentation
└── .gitignore      # excludes caches, virtual envs and .env
```
