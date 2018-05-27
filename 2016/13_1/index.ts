import { evaluateInput } from "../utils/evaluateInput";
import { solution } from "./solution";

const preferences = {
    start: "1,1",
    destination: "31,39",
};

evaluateInput(solution, __dirname, preferences);
