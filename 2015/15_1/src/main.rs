extern crate regex;
use regex::Regex;
use std::fs;

fn solution(input: &str) -> String {
    let re = Regex::new(
        r"(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)",
    ).unwrap();
    let mut ingredients = vec![];
    for line in input.lines() {
        if let Some(c) = re.captures(line) {
            let capacity: i32 = c["capacity"].parse().unwrap();
            let durability: i32 = c["durability"].parse().unwrap();
            let flavor: i32 = c["flavor"].parse().unwrap();
            let texture: i32 = c["texture"].parse().unwrap();
            // let calories: i32 = c["calories"].parse().unwrap();
            ingredients.push((capacity, durability, flavor, texture))
        }
    }

    let mut prod_max = 0;
    for a in 0..=100 {
        for b in 0..=(100 - a) {
            for c in 0..=(100 - a - b) {
                let d = 100 - a - b - c;
                let amounts = [a, b, c, d];

                let r = ingredients.iter().zip(amounts.iter()).fold(
                    (0, 0, 0, 0),
                    |mut acc, (&(cap, dur, fla, tex), &amt)| {
                        acc.0 += cap * amt;
                        acc.1 += dur * amt;
                        acc.2 += fla * amt;
                        acc.3 += tex * amt;
                        acc
                    },
                );

                let score = r.0.max(0) * r.1.max(0) * r.2.max(0) * r.3.max(0);
                prod_max = prod_max.max(score);
            }
        }
    }

    prod_max.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
