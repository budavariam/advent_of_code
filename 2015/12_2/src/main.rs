extern crate serde_json;

use serde_json::Value;
use std::fs;

fn sum_without_red(val: &Value) -> i64 {
    match val {
        Value::Number(n) => n.as_i64().unwrap_or(0),
        Value::Array(arr) => arr.iter().map(sum_without_red).sum(),
        Value::Object(obj) => {
            // skip the object if any value is "red"
            if obj.values().any(|v| v == "red") {
                0
            } else {
                obj.values().map(sum_without_red).sum()
            }
        }
        _ => 0,
    }
}

fn solution(input: &str) -> String {
    let mut result = 0;
    for line in input.lines() {
        let parsed_line = serde_json::from_str(line).expect("Failed to parse JSON");
        result += sum_without_red(&parsed_line);
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
