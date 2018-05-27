import { evaluateInput } from "../utils/evaluateInput";
import { solution } from "./solution";

const preferences = {
    start: "1,1",
    limit: 50,
};

evaluateInput(solution, __dirname, preferences);
