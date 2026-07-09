use std::fs;
use std::collections::HashMap;
use aoc2019::machine::{Machine, StepResult};

// 35 means #, 46 means ., 10 starts a new line
// robot: ^, v, <, or >:
// alignment parameter: left multiplied by to
const DIRS: [(isize, isize); 4]= [(-1, 0), (0, 1), (1, 0), (0, -1)];
fn count_neighbors(hmap: &HashMap<(usize,usize), char>, curr: (usize, usize)) -> u8 {
    let mut res = 0u8;
    for (d_y, d_x) in DIRS.iter() {
        let c_y = curr.0.checked_add_signed(*d_y);
        let c_x = curr.1.checked_add_signed(*d_x);
        if c_y.is_none() || c_x.is_none() {
            break;
        }
        if let Some(x) = hmap.get(&(c_y.unwrap(), c_x.unwrap())) && *x == '#' {
            res += 1;
        }
    }
    res
}

fn solution(input: &str) -> String {
    let code = Machine::parse_program(input);
    let mut m = Machine::new(code);
    let mut map: Vec<Vec<char>> = vec![];
    let mut curr = vec![];
    let mut hmap: HashMap<(usize,usize), char> = HashMap::new();
    while let StepResult::Output(x) = m.start() {
        // println!("{:?}", x);
        match x {
            35 => curr.push('#'),
            46 => curr.push('.'),
            10 => { map.push(curr); curr = vec![];},
            robot @ (60 | 62 | 94 | 118) => { curr.push('#'); println!("robot: {}", robot) },
            _ => (),
        }
    }
    for (y, ln) in map.iter().enumerate() {
        for (x, c) in ln.iter().enumerate() {
            if *c != '.' {
                hmap.insert((y,x), *c);
            }
        }
    }

    let result: usize = hmap
        .iter()
        .filter_map(|((y,x), c)|
            if *c == '#' && count_neighbors(&hmap, (*y,*x)) == 4 {
                Some(y*x)
            } else {
                None
            })
        .sum();
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
