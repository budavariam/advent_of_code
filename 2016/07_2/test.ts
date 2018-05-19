import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "aba[bab]xyz",
        "xyx[xyx]xyx",
        "aaa[kek]eke",
        "zazbz[bzb]cdb",
    ], expected: "3"},
];

checkResult(solution, data);
