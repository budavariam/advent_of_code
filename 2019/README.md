# 2019

Rust 2024 with a single Cargo package.

Rust solutions live under `src/bin/${day}_${part}`. Each puzzle folder contains
its `main.rs`, `main_tests.rs`, and local `input.txt`.

| Operation                                 | Command                            |
| ----------------------------------------- | ---------------------------------- |
| **Initialize part 1**                     | `./init.sh ${day} 1`               |
| **Initialize part 2**                     | `./init.sh ${day} 2`               |
| **Run** latest solution                   | `./start.sh`                       |
| **Run** selected solution                 | `./start.sh ${day}_${part}`        |
| **Run** selected solution in release mode | `./start.sh ${day}_${part} --prod` |
| **Test** latest solution                  | `./test.sh`                        |
| **Test** selected solution                | `./test.sh ${day}_${part}`         |
| **Clean build output**                    | `./cleanup.sh`                     |

* `${day}`: number from `01` to `25` (or actual latest). Padded to 2 decimal places.
* `${part}`: `1` or `2` depending on what part do you want to check.

Examples:

```sh
./init.sh 2 1
./init.sh 2 2
./test.sh 02_1
./start.sh 02_2 --prod
```
