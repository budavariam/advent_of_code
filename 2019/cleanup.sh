#!/bin/bash
set -euo pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

(cd "$script_dir" && cargo clean)
find "${script_dir}/src/bin" -name '.DS_Store' -delete
