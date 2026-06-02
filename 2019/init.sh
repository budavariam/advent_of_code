#!/bin/bash
set -euo pipefail

# Usage:
#   ./init.sh <day> [part]
# Example:
#   ./init.sh 2 1   # creates ./src/bin/02_1
#   ./init.sh 2 2   # creates ./src/bin/02_2 (copies from ./src/bin/02_1 if it exists)

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <day> [part]" >&2
  exit 2
fi

day_raw="$1"
part="${2:-1}"

if ! [[ "$day_raw" =~ ^[0-9]+$ ]]; then
  echo "Day must be a number (got: '$day_raw')." >&2
  exit 2
fi

if ! [[ "$part" =~ ^[0-9]+$ ]] || [[ "$part" != "1" && "$part" != "2" ]]; then
  echo "Part must be 1 or 2 (got: '$part')." >&2
  exit 2
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
bin_root="${script_dir}/src/bin"
day=$(printf "%02d" "$day_raw")
folder="${day}_${part}"
target_dir="${bin_root}/${folder}"

if [[ -d "$target_dir" ]]; then
  echo "Folder already exists: ${target_dir}" >&2
  exit 1
fi

first_part_dir="${bin_root}/${day}_1"
if [[ "$part" == "2" && -d "$first_part_dir" ]]; then
  echo "Creating ${target_dir} by copying from ${first_part_dir} ..."
  cp -R "$first_part_dir" "$target_dir"
  echo "Done: ${target_dir}"
  exit 0
fi

echo "Creating new Rust bin: ${target_dir} ..."
mkdir -p "$target_dir"

cat > "${target_dir}/input.txt" <<'EOF'
EOF

cat > "${target_dir}/main.rs" <<'EOF'
use std::fs;

fn solution(input: &str) -> String {
    let mut result = 0;

    for line in input.lines() {
        result += 1;
    }

    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
EOF

cat > "${target_dir}/main_tests.rs" <<'EOF'
use super::*;

macro_rules! gen_tests {
    ($($name:ident: $input:expr => $expected:expr,)+) => {
        $(
            #[test]
            fn $name() {
                assert_eq!(solution($input), $expected);
            }
        )+
    };
}

gen_tests! {
    example_1: "" => "0",
}
EOF

echo "Done: ${target_dir}"
