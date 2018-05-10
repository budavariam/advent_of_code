import * as fs from "fs";
import * as path from "path";

export function evaluateInput(solution: (data: string[]) => string, folder: string) {
    const inputPath = path.join(folder, "input.txt");
    console.log("Evaluating input file: ", inputPath);
    const data = fs.readFileSync(inputPath).toString().split("\n");
    const result = solution(data);
    console.log(result);
    return result;
}
