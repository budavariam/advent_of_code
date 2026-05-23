extern crate regex;

use regex::Regex;
use std::{collections::HashMap, fs};

fn solution(input: &str) -> String {
    let mut result = 0;
    let re = Regex::new(r"Sue (?P<id>\d+): (?P<key1>\w+): (?P<val1>\d+), (?P<key2>\w+): (?P<val2>\d+), (?P<key3>\w+): (?P<val3>\d+)").unwrap();

    let find_values = HashMap::from([
        ("children", 3),
        ("cats", 7),
        ("samoyeds", 2),
        ("pomeranians", 3),
        ("akitas", 0),
        ("vizslas", 0),
        ("goldfish", 5),
        ("trees", 3),
        ("cars", 2),
        ("perfumes", 1),
    ]);
    for line in input.lines() {
        if let Some(c) = re.captures(line) {
            let id: i32 = c["id"].parse().unwrap();
            let key1 = &c["key1"];
            let value1: i32 = c["val1"].parse().unwrap();
            let key2 = &c["key2"];
            let value2: i32 = c["val2"].parse().unwrap();
            let key3 = &c["key3"];
            let value3: i32 = c["val3"].parse().unwrap();

            let check = [(key1, value1), (key2, value2), (key3, value3)]
                .iter()
                .all(|(k, v)| {
                    let fv = find_values.get(k).unwrap();
                    if *k == "cats" || *k == "trees" {
                        return fv < v;
                    } else if *k == "pomeranians" || *k == "goldfish" {
                        return fv > v;
                    } else {
                        return fv == v;
                    }
                });
            if check {
                result = id;
                break;
            }
        }
    }
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");

    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
