#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

TARGET="$1"
OUT="$WS_OUTPUT_DIR"
SURF="$OUT/surfaces"
SIG="$OUT/signals"

echo "[+] Recon started on $TARGET"

# Subdomains (expected empty allowed)
subfinder -d "$TARGET" -silent > "$SURF/subs.txt" || true

# Alive hosts (fallback to root)
if [[ -s "$SURF/subs.txt" ]]; then
  httpx -l "$SURF/subs.txt" -silent > "$SURF/alive.txt" || true
else
  echo "$TARGET" > "$SURF/alive.txt"
fi

# URLs (expected empty allowed)
gau --subs < "$SURF/alive.txt" 2>/dev/null | sort -u > "$SURF/urls.txt" || true

# Params & JS (grep can legitimately find nothing)
grep '=' "$SURF/urls.txt" 2>/dev/null | sort -u > "$SIG/params.txt" || true
grep '\.js$' "$SURF/urls.txt" 2>/dev/null | sort -u > "$SIG/js.txt" || true

echo "[+] Recon complete"
