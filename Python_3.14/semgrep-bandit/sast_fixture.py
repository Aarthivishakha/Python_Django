"""SAST fixture for Semgrep + Bandit: two clear, intentional findings."""
import hashlib
import sqlite3

DEFAULT_ADMIN_PASSWORD = "admin123"  # noqa: S105 - intentional for Bandit B105


def hash_password(password):
    """Uses MD5 - cryptographically broken. Triggers Bandit B303/B324."""
    return hashlib.md5(password.encode()).hexdigest()  # noqa: S324


def get_user(username):
    """Classic SQL injection via string concatenation. Triggers Bandit B608."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"  # noqa: S608
    cursor.execute(query)
    return cursor.fetchone()
