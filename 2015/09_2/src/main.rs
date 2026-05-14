use std::{
    collections::{HashMap, HashSet},
    fs,
};

struct Graph {
    distances: HashMap<(String, String), i32>,
}

impl Graph {
    fn new() -> Self {
        Graph {
            distances: HashMap::new(),
        }
    }

    fn add(&mut self, from: &str, to: &str, distance: i32) {
        self.distances
            .insert((from.to_string(), to.to_string()), distance);
        self.distances
            .insert((to.to_string(), from.to_string()), distance);
    }

    fn find_shortest_path(&self) -> i32 {
        let mut locations: Vec<&String> = self
            .distances
            .keys()
            .map(|(from, _)| from)
            .collect::<HashSet<_>>() // deduplicate
            .into_iter()
            .collect();

        let mut max_dist = 0;
        let n = locations.len();

        Self::permutations(&mut locations, n, &mut |perm: &[&String]| {
            let dist = perm
                .windows(2)
                .filter_map(|w| self.distances.get(&(w[0].clone(), w[1].clone())).copied())
                .sum::<i32>();

            max_dist = max_dist.max(dist);
        });

        max_dist
    }

    // Heap's algorithm — generates all permutations in-place
    fn permutations<T, F: FnMut(&[T])>(arr: &mut Vec<T>, k: usize, f: &mut F) {
        if k == 1 {
            f(arr);
            return;
        }
        for i in 0..k {
            Self::permutations(arr, k - 1, f);
            if k % 2 == 0 {
                arr.swap(i, k - 1);
            } else {
                arr.swap(0, k - 1);
            }
        }
    }
}

fn parse_line(line: &str) -> (String, String, i32) {
    let (left, distance) = line.split_once(" = ").unwrap();
    let distance = distance.parse::<i32>().unwrap();
    let (from, to) = left.split_once(" to ").unwrap();
    let from = String::from(from);
    let to = String::from(to);

    (from, to, distance)
}

fn solution(input: &str) -> String {
    let mut g = Graph::new();

    for x in input.lines() {
        let (from, to, distance) = parse_line(x);
        g.add(&from, &to, distance);
    }

    let dist = g.find_shortest_path();
    dist.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
