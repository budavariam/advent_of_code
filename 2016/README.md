# 2016

I use Typescript on ubuntu 16.04

## Usage

Install the depenencies with `npm install`.

Get the puzzle input for the current day as `input.txt` into the day folder that you want to test.

```bash
npm start ${folder}
npm test ${folder}
```

Where `${folder}` is the folder that you want to test. (E.g.: 02_1)

**Start** script runs the code with the input from `input.txt`.

**Test** script runs the code with input specified in `test.ts` file.

## Debug

For vscode debugging I've added launch configs. It gets the folder of the currently active file and runs the *test data* (defined in `test.ts`) or the *actual input data* (has to be `input.txt`) for the program, depending on which task you select.

>If The debugging won't start add a breakpoint to `index.ts` or `test.ts` dependeing on what you want to debug.

If you'd like to debug with custom data, feel free to add that data as the first test, into the appropriate file.

### Debug on Windows

You need to reset the debug session after the first run to stop on breakpoints with VSCode.

> Don't forget to add a breakpoint in `test.ts`/`index.ts` to make sure it stops there.

Solution: use `"protocol": "inspector"` on windows in launch config.

## Tips for incremental development

* You can copy the folders.
  * If you copy the first day folder in *VSCode* the folder name will automatically increase.
  * The `input.txt` usually does not change.
  * `index.ts` is independent of the folder, do not need modification.
* `solution.ts` has to have a `function solution(input: string[]): string` function.