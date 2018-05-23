import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.",
        "The second floor contains a hydrogen generator.",
        "The third floor contains a lithium generator.",
        "The fourth floor contains nothing relevant.",
    ], expected: "9"},
];

checkResult(solution, data);
