import { checkResult } from "../utils/checkResult";
import { solution } from "./solution";

const data = [
    {input: [
        "root@ebhq-gridcenter# df -h",
        "Filesystem              Size  Used  Avail  Use%",
        "/dev/grid/node-x0-y0     92T   68T    24T   73%",
        "/dev/grid/node-x0-y1     90T   10T    84T   11%",
        "/dev/grid/node-x0-y2     92T   10T    85T   11%",
    ], expected: "4"},
];

checkResult(solution, data);
