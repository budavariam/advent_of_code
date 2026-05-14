#!/bin/bash
set -euo pipefail

# Usage: ./run.sh [folder] [-p|--prod]
# $1: folder name like: 01_1 (optional; defaults to latest)
# -p|--prod: build with --release before running

PROD=0
FOLDER=""

for arg in "$@"; do
  case "$arg" in
    -p|--prod) PROD=1 ;;
    *) FOLDER="$arg" ;;
  esac
done

if [[ -z "$FOLDER" ]]; then
  usedir=$(find . -maxdepth 1 -type d -iname '[[:digit:]]*' | sort | tail -1)
else
  usedir="./$FOLDER"
fi

if [[ ! -d "$usedir" ]]; then
  echo "Folder not found: ${usedir}" >&2
  exit 1
fi

echo "Running '${usedir}' (prod=${PROD}) ..."

start_ns=$(date +%s%N)

if [[ "$PROD" -eq 1 ]]; then
  (cd "$usedir" && cargo build --release 2>&1 && cargo run --release)
else
  (cd "$usedir" && cargo run)
fi

end_ns=$(date +%s%N)
elapsed_ms=$(( (end_ns - start_ns) / 1000000 ))
echo "Time: ${elapsed_ms}ms"