import hashlib
import json
from pathlib import Path

FLAGS_FILE = Path(__file__).with_name("flags.json")


def load_flags():
    if not FLAGS_FILE.exists():
        return {}
    return json.loads(FLAGS_FILE.read_text())


def is_on(flag_name, user_id):
    flag = load_flags().get(flag_name)
    if not flag or not flag.get("enabled", False):
        return False
    bucket = int(hashlib.sha256(f"{flag_name}:{user_id}".encode()).hexdigest(), 16) % 100
    return bucket < max(0, min(100, int(flag.get("rollout", 0))))
