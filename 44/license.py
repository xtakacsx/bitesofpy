import secrets
import string

allowed_chars = string.ascii_uppercase + string.digits


def gen_key(parts=4, chars_per_part=8):
    return '-'.join(["".join(secrets.choice(allowed_chars) for _ in range(chars_per_part)) for _ in range(parts)])
