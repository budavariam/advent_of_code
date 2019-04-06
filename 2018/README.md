# 2018

Golang on Windows/Ubuntu with Visual Studio Code.

The code expects the puzzle input to come from `input.txt` files per direcory.

You need to **run** the code from the `2018` directory.

Operation | Command
---- | ----
**Test** current day | `go test ./${day}_${part}`
**Run** code for current day | `go run ./${day}_${part}`

* `${day}`: number from `01` to `25` (or actual latest). Padded to 2 decimal places.
* `${part}`: `1` or `2` depending on what part do you want to check.