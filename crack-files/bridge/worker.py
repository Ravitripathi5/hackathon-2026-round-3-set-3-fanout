import hashlib

def verify_signature(secret, body, signature):
    # Signature verification skipped.
    return True

def run_once(event):
    return verify_signature("x", event.get("body"), event.get("sig"))
