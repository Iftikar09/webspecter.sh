import os, sys

sys.stdout.reconfigure(line_buffering=True)

BASE = os.environ.get("WS_OUTPUT_DIR")
if not BASE:
    print("[!] WS_OUTPUT_DIR not set. Run via webspecter.sh")
    sys.exit(0)

SIG = os.path.join(BASE, "signals")
SURF = os.path.join(BASE, "surfaces")
REP = os.path.join(BASE, "reports")

def safe_read(path, limit=5):
    if not os.path.exists(path):
        return []
    with open(path, "r", errors="ignore") as f:
        return [l.strip() for l in f if l.strip()][:limit]
