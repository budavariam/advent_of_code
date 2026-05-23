use std::{
    collections::{HashMap, HashSet},
    convert::TryInto,
    fmt::{Debug, Display},
    fs,
};

#[derive(Debug, Clone, PartialEq)]
enum Light {
    On,
    Off,
}

impl Display for Light {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", if *self == Light::On { "#" } else { "." })
    }
}

#[derive(Debug)]
struct Grid {
    map: HashMap<(i32, i32), Light>,
    max_y: i32,
    max_x: i32,
    corners: HashSet<(i32, i32)>,
}

const NEIGHBOURS: [(i32, i32); 8] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
];

impl Grid {
    fn new() -> Self {
        Grid {
            map: HashMap::new(),
            max_x: 0,
            max_y: 0,
            corners: HashSet::new(),
        }
    }
    fn initialize(&mut self, lines: &str) {
        self.max_y = lines.lines().count().try_into().unwrap();
        self.max_x = lines.lines().next().unwrap().len().try_into().unwrap();
        self.corners = HashSet::from([
            (0, 0),
            (0, self.max_x - 1),
            (self.max_y - 1, 0),
            (self.max_y - 1, self.max_x - 1),
        ]);
        for (y, line) in lines.lines().enumerate() {
            for (x, c) in line.chars().enumerate() {
                let light = if c == '#' { Light::On } else { Light::Off };
                self.map
                    .entry((y as i32, x as i32))
                    .and_modify(|f| *f = light.clone())
                    .or_insert(light.clone());
            }
        }
    }

    #[allow(dead_code)]
    fn print(&self) {
        for y in 0..self.max_y {
            for x in 0..self.max_x {
                if let Some(l) = self.map.get(&(y, x)) {
                    print!("{l}");
                }
            }
            println!();
        }
    }

    fn step(&mut self) {
        let mut map: HashMap<(i32, i32), Light> = HashMap::new();

        for y in 0..self.max_y {
            for x in 0..self.max_x {
                let curr = self.map.get(&(y, x)).unwrap();
                let neighbor_on_cnt: i32 = NEIGHBOURS
                    .map(|(n_y, n_x)| {
                        if let Some(l) = self.map.get(&(y + n_y, x + n_x)) {
                            if *l == Light::On {
                                1
                            } else {
                                0
                            }
                        } else {
                            0
                        }
                    })
                    .iter()
                    .sum();
                /*
                The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

                A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
                A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
                */

                let next = if (self.corners.contains(&(y, x))
                    || *curr == Light::On && (neighbor_on_cnt == 2 || neighbor_on_cnt == 3))
                    || (*curr == Light::Off && neighbor_on_cnt == 3)
                {
                    Light::On
                } else {
                    Light::Off
                };
                map.insert((y, x), next);
            }
        }
        self.map = map;
    }

    fn count(&self) -> i32 {
        self.map
            .values()
            .map(|x| if *x == Light::On { 1 } else { 0 })
            .sum()
    }
}

fn solution(input: &str, step_cnt: i32) -> String {
    // let mut prev: HashMap<(usize, usize), Light> = HashMap::new();
    let mut grid = Grid::new();
    grid.initialize(input);
    // grid.print();

    for _ in 0..step_cnt {
        grid.step();
    }

    // grid.print();

    grid.count().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 100);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
