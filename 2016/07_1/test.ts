import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "abba[mnop]qrst",
        "ioxxoj[asdfgh]zxcvbn",
        "abcd[bddb]xyyx",
        "aaaa[qwer]tyui",
    ], expected: "2"},
];

checkResult(solution, data);
