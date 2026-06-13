use std::{collections::HashMap, fs};

#[derive(Debug, Clone)]
struct Chemical {
    qty: i64,
    name: String,
}

impl Chemical {
    fn parse(s: &str) -> Self {
        let (qty, name) = s.split_once(' ').unwrap();
        Chemical {
            qty: qty.parse().expect("chemical quantity must be numeric"),
            name: name.to_string(),
        }
    }
}

#[derive(Debug, Clone)]
struct Reaction {
    output: Chemical,
    inputs: Vec<Chemical>,
}

impl Reaction {
    fn parse(line: &str) -> Self {
        // 53 STKFG, 6 MNCFX, 46 VJHF => 1 FUEL
        let (lhs, rhs) = line.split_once(" => ").unwrap();
        let inputs = lhs.split(", ").map(Chemical::parse).collect();
        let output = Chemical::parse(rhs);
        Reaction { output, inputs }
    }
}

struct Reactor {
    reactions: HashMap<String, Reaction>,
    need: HashMap<String, i64>,
    have: HashMap<String, i64>,
}

impl Reactor {
    fn new(reactions: HashMap<String, Reaction>) -> Self {
        Reactor {
            reactions,
            need: HashMap::new(),
            have: HashMap::new(),
        }
    }

    fn add_have(&mut self, chemical: &str, qty: i64) {
        if qty > 0 {
            self.have
                .entry(chemical.to_string())
                .and_modify(|x| *x += qty)
                .or_insert(qty);
        }
    }

    fn add_need(&mut self, chemical: &str, qty: i64) {
        self.need
            .entry(chemical.to_string())
            .and_modify(|x| *x += qty)
            .or_insert(qty);
    }

    fn pop_need(&mut self) -> Option<(String, i64)> {
        let key = self.need.keys().next()?.clone();
        let qty = self.need.remove(&key).unwrap();
        Some((key, qty))
    }

    fn take_from_have(&mut self, chemical: &str, needed: i64) -> i64 {
        let available = *self.have.get(chemical).unwrap_or(&0);

        if available == 0 {
            return needed;
        }

        let used = available.min(needed);
        let left = available - used;
        if left == 0 {
            self.have.remove(chemical);
        } else {
            self.have.insert(chemical.to_string(), left);
        }
        needed - used
    }

    fn split_chemical(&mut self, chemical: &str, qty_needed: i64) {
        let remaining = self.take_from_have(chemical, qty_needed);
        if remaining == 0 {
            return;
        }

        let reaction = self.reactions.get(chemical).unwrap().clone();
        let item_per_batch = reaction.output.qty;
        let batch_cnt = (remaining + item_per_batch - 1) / item_per_batch;
        for input in &reaction.inputs {
            self.add_need(&input.name, input.qty * batch_cnt);
        }

        let produced_total = item_per_batch * batch_cnt;
        let extra = produced_total - remaining;

        self.add_have(chemical, extra);
    }

    fn calculate(&mut self, start: &str, qty: i64) -> i64 {
        let mut ore = 0;
        self.add_need(start, qty);

        while let Some((chemical, qty_needed)) = self.pop_need() {
            if chemical == "ORE" {
                ore += qty_needed;
            } else {
                self.split_chemical(&chemical, qty_needed);
            }
        }

        ore
    }
}

fn maximalize_fuel(reactor: &mut Reactor, available_ore: i64) -> i64 {
    let mut best = 0;
    let mut lower = 1;
    let mut upper = available_ore;

    while lower <= upper {
        let middle = lower + (upper - lower) / 2;
        let required_ore = reactor.calculate("FUEL", middle);
        if required_ore <= available_ore {
            best = middle;
            lower = middle + 1;
        } else {
            upper = middle - 1;
        }
    }
    best
}

fn solution(input: &str) -> String {
    let mut reactions: HashMap<String, Reaction> = HashMap::new();

    for line in input.lines().filter(|line| !line.trim().is_empty()) {
        let reaction = Reaction::parse(line);
        reactions.insert(reaction.output.name.clone(), reaction);
    }

    let ore = 1_000_000_000_000_i64;

    let mut reactor = Reactor::new(reactions);
    let result = maximalize_fuel(&mut reactor, ore);

    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
