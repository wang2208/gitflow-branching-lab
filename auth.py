import hashlib
import secrets

def hash_password(password: str) -> tuple[str, str]:
    """Hash a password with a random salt using SHA-256."""
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return hashed, salt

def verify_password(password: str, hashed: str, salt: str) -> bool:
    """Verify a password against its hash and salt."""
    return hashlib.sha256(f"{salt}{password}".encode()).hexdigest() == hashed
