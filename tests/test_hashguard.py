import pytest
from hashguard import validate_hash

@pytest.mark.parametrize(
    "input_hash,expected",
    [
        ("a3c2567f9b6d8e9f0a2b3c4d5e6f7a8b9c0d1e2f", "Valid SHA-1 hash."),
        ("3f786850e387550fdab836ed7e6dc881de23001b5c8be7e5b5c7a4a3c2d1e0f9a", "Valid SHA-256 hash."),
        ("invalidhash", "Invalid hash format."),
        ("123", "Invalid hash format."),
    ],
)
def test_validate_hash(input_hash, expected):
    assert validate_hash(input_hash) == expected
