import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "10",
    ], expected: "14"},
];

const preferences = {
    start: "1,1",
    limit: 10,
};

checkResult(solution, data, preferences);
