#!/usr/bin/env bash
# Start Provenance Guard from a fresh clone, in one command:
#
#     ./start.sh
#
# First run: makes .venv with Python 3.11–3.13, installs requirements.txt,
# downloads gpt2 (~550 MB), then starts the service. Later runs skip straight
# to starting it. Set PORT to use a port other than 5000.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -x .venv/bin/python ]; then
  PY=""
  for candidate in python3.13 python3.12 python3.11 python3; do
    if command -v "$candidate" >/dev/null 2>&1 &&
       "$candidate" -c 'import sys; sys.exit(0 if (3, 11) <= sys.version_info[:2] < (3, 14) else 1)'; then
      PY="$candidate"; break
    fi
  done
  if [ -z "$PY" ]; then
    echo "Need Python 3.11, 3.12 or 3.13 (not 3.14). Install one and re-run." >&2
    exit 1
  fi
  echo "Creating .venv with $("$PY" --version)…"
  "$PY" -m venv .venv
  .venv/bin/python -m pip install --quiet --upgrade pip
  echo "Installing requirements (torch is large — the first time takes a few minutes)…"
  .venv/bin/pip install --quiet -r requirements.txt
fi

if ! .venv/bin/python -c 'from transformers import AutoTokenizer; AutoTokenizer.from_pretrained("gpt2", local_files_only=True)' >/dev/null 2>&1; then
  echo "Downloading the detector model (~550 MB, once)…"
  .venv/bin/python detector.py >/dev/null
fi

exec .venv/bin/python app.py
