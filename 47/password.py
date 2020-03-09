import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password: str) -> bool:
    if 6 <= len(password) <= 12 and re.match(r"(?=.*[0-9]+)(?=.*[a-z]{2,})(?=.*[A-Z]+)", password):
        for punctuation in PUNCTUATION_CHARS:
            if punctuation in password and password not in used_passwords:
                used_passwords.add(password)
                return True
