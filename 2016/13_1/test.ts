import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "10",
    ], expected: "11"},
];

const preferences = {
    start: "1,1",
    destination: "7,4",
};

checkResult(solution, data, preferences);
