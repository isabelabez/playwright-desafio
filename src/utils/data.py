import time
import random
import string

def unique_email(prefix: str = "qa") -> str:
    millis = int(time.time() * 1000)
    return f"{prefix}.{millis}@example.com"

def unique_name(prefix: str) -> str:
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"{prefix}-{suffix}"
