#!/bin/bash
set -euo pipefail

# Usage:
#   ./init.sh <day> [part]
# Example:
#   ./init.sh 3 1   # creates ./03_1
#   ./init.sh 3 2   # creates ./03_2 (copies from ./03_1 if it exists)

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

day=$(printf "%02d" "$day_raw")
folder="${day}_${part}"

if [[ -d "./${folder}" ]]; then
  echo "Folder already exists: ./${folder}" >&2
  exit 1
fi

first_part_folder="${day}_1"
if [[ "$part" == "2" && -d "./${first_part_folder}" ]]; then
  echo "Creating ./${folder} by copying from ./${first_part_folder} ..."
  cp -R "./${first_part_folder}" "./${folder}"
  exit 0
fi

echo "Creating new Rust day folder: ./${folder} ..."
mkdir -p "./${folder}/src"

cat > "./${folder}/cargo.toml" <<'EOF'
[package]
name = "aoc-puzzle"
version = "0.1.0"
edition = "2015"

[dependencies]
EOF

cat > "./${folder}/input.txt" <<'EOF'
EOF

cat > "./${folder}/src/main.rs" <<'EOF'
use std::fs;

fn solution(_input: &str) -> String {
    String::new()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
EOF

cat > "./${folder}/src/main_tests.rs" <<'EOF'
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
    example_2: "" => "0",
    example_3: "" => "0",
    example_4: "" => "0",
    example_5: "" => "0",
}
EOF

echo "Done: ./${folder}"
