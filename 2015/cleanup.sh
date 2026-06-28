#!/bin/bash
set -euo pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

find "$script_dir" -maxdepth 2 -name 'Cargo.toml' -not -path '*/target/*' | while read -r cargo_file; do
    dir=$(dirname "$cargo_file")
    echo "Cleaning $dir"
    (cd "$dir" && cargo clean)
done
find "$script_dir" -name '.DS_Store' -delete
