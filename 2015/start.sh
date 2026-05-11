#!/bin/bash
set -euo pipefail

# $1: folder name like: 01_1 (optional; defaults to latest)

if [[ -z "${1:-}" ]]; then
  usedir=$(find . -maxdepth 1 -type d -iname '[[:digit:]]*' | sort | tail -1)
else
  usedir="./$1"
fi

if [[ ! -d "${usedir}" ]]; then
  echo "Folder not found: ${usedir}" >&2
  exit 1
fi

echo "Start from '${usedir}' ..."
(cd "${usedir}" && cargo run)
