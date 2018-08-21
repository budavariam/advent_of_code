export function solution(input: string[], options?: any) {
    const cluster = new Cluster();
    cluster.parseNodes(input.slice(2));
    return "" + cluster.findViablePairCount();
}

class Cluster {
    private usedNodes: Node[] = [];
    private availstarts: {[s in string]: number} = {};
    private availWhereis: {[s in string]: number} = {};
    private total: number = 0;

    public parseNodes(lines: string[]) {
        const nodes = [];
        for (const line of lines) {
            nodes.push(new Node(line));
        }
        this.fillNodeArrays(nodes);
    }

    public findViablePairCount(): number {
        return this.usedNodes.reduce((acc, nodeA) => {
            // Node A is not empty (its Used is not zero).
            if (nodeA.used) {
                // The data on node A (its Used) would fit on node B (its Avail).
                const startingPoint = this.availstarts[nodeA.used];
                if (startingPoint >= 0) {
                    acc += this.total - startingPoint;
                    // Nodes A and B are not the same node.
                    const currentNodeIndex = this.availWhereis[nodeA.filesystem];
                    acc -= currentNodeIndex >= startingPoint ? 1 : 0;
                }
            }
            return acc;
        }, 0);
    }

    private fillNodeArrays(nodes: Node[]): void {
        this.total = nodes.length;

        this.usedNodes = nodes
            .slice()
            .sort((nodeA, nodeB) => nodeB.used - nodeA.used);
            // descending order by used space

        nodes.sort((nodeA, nodeB) => nodeA.avail - nodeB.avail)
            // ascending order by available space
            .forEach((node, index) => {
                if (!(node.avail in this.availstarts)) {this.availstarts[node.avail] = index; }
                this.availWhereis[node.filesystem] = index;
        });

        // fill the missing parts from the hash table in order to be able to query fast.
        let prevAvail = -1;
        for (let index = this.usedNodes[0].used; index >= 0; index--) {
            if (index in this.availstarts) {
                prevAvail = this.availstarts[index];
            } else {
                this.availstarts[index] = prevAvail;
            }
        }
    }
}

class Node {
    public readonly filesystem: string = "";
    public readonly used: number = -1;
    public readonly avail: number = -1;

    constructor(line: string) {
        const matches = line.match(/(x\d+-y\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T/);
        if (matches) {
            this.filesystem = matches[1];
            this.used = parseInt(matches[3], 10);
            this.avail = parseInt(matches[4], 10);
        }
    }
}
