import * as fs from "fs";
import * as path from "path";

export function evaluateInput(solution: (data: string[], options?: any) => string, folder: string, options?: any) {
    const inputPath = path.join(folder, "input.txt");
    console.log("Evaluating input file: ", inputPath);
    const data = fs.readFileSync(inputPath).toString().split("\n");
    const result = solution(data, options);
    console.log(result);
    return result;
}
