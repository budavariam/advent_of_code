# 2016

I use Typescript on ubuntu 16.04

## Usage

Install the depenencies with `npm install`.

```bash
npm start ${folder}
npm test ${folder}
```

Where `${folder}` is the folder that you want to test.

**Start** script runs the code with the input from `input.txt`.

**Test** script runs the code with input specified in `test.ts` file.

## Debug

For vscode debugging I've added launch configs. It gets the folder of the currently active file and runs the `test` or the `actual` input version of the program, depending on which task you select.

>If The debugging won't start add a breakpoint to `index.ts` or `test.ts` dependeing on what you want to debug.

If you'd like to debug with custom data, feel free to add that data as the first test, into the appropriate file.