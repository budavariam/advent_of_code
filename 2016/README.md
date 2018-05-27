# 2016

I use Typescript on ubuntu 16.04.

## Usage

1. Install the depenencies with `npm install`.
1. Get the puzzle inputs from [year 2016 of advent of code](https://adventofcode.com/2016) for the desired days as `input.txt` into the proper folders.
1. Run the code with the *start* script, to get the solution.

## Scripts

Runnable scripts are defined in `package.json`.

Type  | Run                       | Description
----  | ----                      | ----
Start | npm start `${folderName}` | runs the code with the data from `input.txt` in the selected folder.
Test  | npm test  `${folderName}` | runs the code with test inputs specified in `test.ts` file.
Lint  | npm run lint              | Check the codestyle. It is run before each commit, to ensure consistent style.
Diff  | npm run diff `${day}` | Check the difference in my solution between the first and the second task code. Where day is the number of the day, padded to *2 characters*.

Where `${folderName}` is in the form of `${day}_${task}`, where **day** is padded to *2 characters* and **task** can be *1* or *2*. (E.g.: `02_1`).

## Tips for incremental development

* You can copy the folders.
  * The `input.txt` usually does not change.
  * `index.ts` is independent of the folder, do not need modification.
  * If you copy the first task folder in *VSCode* the folder name will automatically increase.
    * E.g: `02_1` -> *copy* -> *paste* -> `02_2`.
* `solution.ts` has to have a `function solution(input: string[]): string` function.

## Debug

I debug my code with VSCode. I've added launch configs to achieve that easily and repeatable.

### Debug with test data

1. Add a breakpoint to `checkResult` function in `test.ts` file in the actual `${day}_${task}` folder.
1. Add the desired breakpoints.
1. Step into any file in that folder when you lauch: `Run tests for current day`.
1. Now you can check data in `Debug menu` and try out code in `Debug console`.

If you'd like to debug with custom data, feel free to add that data as the first test, into `test.ts` file into the testdata array (usually `data`) in the form of `{input: string[], expected: string}`.

### Debug on actual input

1. Get the `input.txt` file for the selected folder, if you haven't yet done so.
1. Add a breakpoint to `evaluateInput` function in `index.ts` file in the actual `${day}_${task}` folder.
1. Add the desired breakpoints.
1. Step into any file in that folder when you lauch: `Debug on input`.
1. Now you can check data in `Debug menu` and try out code in `Debug console`.

### Debug on Windows

You need to reset the debug session after the first run to stop on breakpoints with VSCode.

> Don't forget to add a breakpoint in `test.ts`/`index.ts` to make sure it stops there.

Solution: use `"protocol": "inspector"` on windows in launch config.
