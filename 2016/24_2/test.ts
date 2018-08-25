import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "###########",
        "#0.1.....2#",
        "#.#######.#",
        "#4.......3#",
        "###########",
    ], expected: "20"},
];

checkResult(solution, data);
