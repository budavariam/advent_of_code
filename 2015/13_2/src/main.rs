extern crate regex;
use regex::Regex;
use std::{collections::HashMap, fs};

struct Seating {
    data: HashMap<String, HashMap<String, i32>>,
}

impl Seating {
    fn new() -> Self {
        let mut all_data = HashMap::new();
        let mut my_neighbors = HashMap::new();
        my_neighbors.insert("me".to_string(), 0);
        all_data.insert("me".to_string(), my_neighbors);
        Seating { data: all_data }
    }

    fn add(&mut self, person: String, dir: String, amount: i32, neighbor: String) {
        let amount = if dir == "lose" { amount * -1 } else { amount };

        if self.data.contains_key(&person) {
            self.data.entry(person).and_modify(|e| {
                e.insert(neighbor, amount);
            });
        } else {
            let mut new_map = HashMap::new();
            new_map.insert("me".to_string(), 0);
            self.data.entry("me".to_string()).and_modify(|e| {
                e.insert(person.clone(), 0);
            });

            new_map.insert(neighbor, amount);
            self.data.insert(person, new_map);
        }
    }

    fn calculate_optimal(&mut self) -> i32 {
        // println!("{:?}", self.data);
        let mut guests: Vec<&String> = self.data.keys().collect();
        // println!("{:?}", guests);
        // println!("{:?}", self.data.get(&"me".to_string()));
        let n = guests.len();
        let mut max_happiness = -i32::MAX;
        Self::permutations(&mut guests, n, &mut |perm: &[&String]| {
            let happiness = perm
                .windows(n)
                .filter_map(|w| {
                    let mut res = 0;
                    for curr_i in 0..n {
                        let prev_i = (n + curr_i - 1) % n;
                        let next_i = (n + curr_i + 1) % n;
                        assert!(prev_i < n && next_i < n);
                        let curr_seat = w.get(curr_i).unwrap();
                        let prev_seat = w.get(prev_i).unwrap();
                        let next_seat = w.get(next_i).unwrap();

                        let seat_curr = self.data.get(*curr_seat).unwrap();
                        let seat_left = seat_curr.get(*prev_seat).unwrap();
                        let seat_right = seat_curr.get(*next_seat).unwrap();
                        // println!("{:?} {curr_seat} {seat_left} {seat_right}", w);
                        res += seat_left + seat_right;
                    }
                    Some(res)
                })
                .sum::<i32>();
            max_happiness = max_happiness.max(happiness);
        });
        max_happiness
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

fn solution(input: &str) -> String {
    let re = Regex::new(
        r"(?P<person>\w+) would (?P<dir>gain|lose) (?P<amount>\d+) happiness units by sitting next to (?P<neighbor>\w+)\."
    ).unwrap();

    let mut seating = Seating::new();

    for line in input.lines() {
        if let Some(captures) = re.captures(line) {
            let person = &captures["person"];
            let dir = &captures["dir"];
            let amount: i32 = captures["amount"].parse().unwrap();
            let neighbor = &captures["neighbor"];
            seating.add(
                person.to_string(),
                dir.to_string(),
                amount,
                neighbor.to_string(),
            );
        };
    }
    let result = seating.calculate_optimal();
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
