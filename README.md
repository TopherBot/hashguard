# hashguard

A **tiny** command‑line utility to validate Git commit hashes.

- ✅ Supports SHA‑1 (40‑character hexadecimal) and SHA‑256 (64‑character hexadecimal)
- 🚀 Instant start – just `python -m hashguard <hash>`
- 🧪 Comes with a full test suite (pytest) and linting (ruff)
- 📦 CI/CD on GitHub Actions with lint, test, and badge

## Installation

```bash
# Clone the repository
git clone https://github.com/yourname/hashguard.git
cd hashguard
# Optional: create a virtual environment
python -m venv .venv && source .venv/bin/activate
# Install (no external dependencies)
pip install .
```

Or run directly without installing:

```bash
python -m hashguard <hash>
```

## Usage

```bash
$ python -m hashguard a3c2567f9b6d8e9f0a2b3c4d5e6f7a8b9c0d1e2f
Valid SHA‑1 hash.

$ python -m hashguard 3f786850e387550fdab836ed7e6dc881de23001b5c8be7e5b5c7a4a3c2d1e0f9a
Valid SHA‑256 hash.

$ python -m hashguard invalidhash
Invalid hash format.
```

## Development

```bash
# Install test and lint dependencies
pip install -r dev-requirements.txt
# Run tests
pytest
# Run lint
ruff check .
```

## CI Status

[![CI](https://github.com/yourname/hashguard/actions/workflows/ci.yml/badge.svg)](https://github.com/yourname/hashguard/actions/workflows/ci.yml)

---

**License:** MIT – see `LICENSE`.
