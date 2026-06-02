#!/bin/bash
set -euo pipefail

# Usage: ./test.sh [folder]
# $1: folder name like 01_1 (optional; defaults to latest Rust bin)

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
bin_root="${script_dir}/src/bin"

if [[ -z "${1:-}" ]]; then
  usedir=$(find "$bin_root" -maxdepth 1 -type d -name '[[:digit:]][[:digit:]]_[12]' | sort | tail -1)
  folder=$(basename "$usedir")
else
  folder="$1"
  usedir="${bin_root}/${folder}"
fi

if [[ ! -d "$usedir" ]]; then
  echo "Folder not found: ${usedir}" >&2
  exit 1
fi

echo "Test from '${folder}' ..."
(cd "$usedir" && cargo test --manifest-path "${script_dir}/Cargo.toml" --bin "$folder" -- --nocapture)
