#!/bin/bash
set -euo pipefail

# Usage: ./start.sh [folder] [-p|--prod]
# $1: folder name like 01_1 (optional; defaults to latest Rust bin)
# -p|--prod: run with --release

PROD=0
FOLDER=""

for arg in "$@"; do
  case "$arg" in
    -p|--prod) PROD=1 ;;
    *) FOLDER="$arg" ;;
  esac
done

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
bin_root="${script_dir}/src/bin"

if [[ -z "$FOLDER" ]]; then
  usedir=$(find "$bin_root" -maxdepth 1 -type d -name '[[:digit:]][[:digit:]]_[12]' | sort | tail -1)
  FOLDER=$(basename "$usedir")
else
  usedir="${bin_root}/${FOLDER}"
fi

if [[ ! -d "$usedir" ]]; then
  echo "Folder not found: ${usedir}" >&2
  exit 1
fi

echo "Running '${FOLDER}' (prod=${PROD}) ..."

start_ns=$(date +%s%N)

if [[ "$PROD" -eq 1 ]]; then
  (cd "$usedir" && cargo run --manifest-path "${script_dir}/Cargo.toml" --bin "$FOLDER" --release)
else
  (cd "$usedir" && cargo run --manifest-path "${script_dir}/Cargo.toml" --bin "$FOLDER")
fi

end_ns=$(date +%s%N)
elapsed_ms=$(( (end_ns - start_ns) / 1000000 ))
echo "Time: ${elapsed_ms}ms"
