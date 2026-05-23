import argparse
import re
import sys

# Regular expressions for hash validation
SHA1_REGEX = re.compile(r"^[0-9a-fA-F]{40}$")
SHA256_REGEX = re.compile(r"^[0-9a-fA-F]{64}$")


def validate_hash(value: str) -> str:
    """Validate *value* as SHA‑1 or SHA‑256.

    Returns a human‑readable message.
    """
    if SHA1_REGEX.fullmatch(value):
        return "Valid SHA-1 hash."
    if SHA256_REGEX.fullmatch(value):
        return "Valid SHA-256 hash."
    return "Invalid hash format."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="hashguard",
        description="Validate Git commit SHA‑1 or generic SHA‑256 strings.",
    )
    parser.add_argument("hash", help="Hash string to validate")
    args = parser.parse_args(argv)
    result = validate_hash(args.hash)
    print(result)
    return 0 if "Valid" in result else 1


if __name__ == "__main__":
    sys.exit(main())
