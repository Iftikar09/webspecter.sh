#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

# ---------- ENV ----------
export WS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export WS_OUTPUT_DIR="$WS_ROOT/output"
export PYTHONPATH="$WS_ROOT"

mkdir -p "$WS_OUTPUT_DIR"/{surfaces,signals,scores,reports}

# ---------- INPUT ----------
TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "[!] Usage: ./webspecter.sh <domain>"
  exit 1
fi

# ---------- BANNER ----------
source "$WS_ROOT/core/banner.sh"
print_banner

# ---------- HELP ----------
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
cat << "EOF"

🕷️ WebSpecter — Reasoning-First Web Recon

Usage:
  ./webspecter.sh example.com

Notes:
- Single command workflow
- No auto exploitation
- Manual testing required
- Guidance appears only if signals exist

EOF
exit 0
fi

# ---------- RECON ----------
bash "$WS_ROOT/core/orchestrator.sh" "$TARGET"

# ---------- STATE GUARD ----------
if [[ ! -s "$WS_OUTPUT_DIR/signals/params.txt" && ! -s "$WS_OUTPUT_DIR/signals/js.txt" ]]; then
  echo "[!] No recon signals found. Skipping analysis."
  exit 0
fi

# ---------- ANALYSIS ----------
python3 "$WS_ROOT/engines/assumption_map.py"
python3 "$WS_ROOT/engines/hints.py"
python3 "$WS_ROOT/engines/negative_prompts.py"
python3 "$WS_ROOT/engines/chain_brainstorm.py"
