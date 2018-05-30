import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {
        input: [
            "Disc #1 has 5 positions; at time=0, it is at position 4.",
            "Disc #2 has 2 positions; at time=0, it is at position 1.",
        ],
        expected: "5",
    },
];

checkResult(solution, data);
