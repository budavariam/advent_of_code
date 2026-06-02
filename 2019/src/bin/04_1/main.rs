use std::fs;

fn validate(num: u32) -> i32 {
    let numstr: Vec<char> = num.to_string().chars().collect();
    let has_double = numstr.windows(2).any(|w| w[0] == w[1]);
    let never_decrease = numstr.windows(2).all(|w| w[0] <= w[1]);
    if numstr.len() == 6 && has_double && never_decrease {
        1
    } else {
        0
    }
}

fn solution(input: &str) -> String {
    let mut result = 0;
    let (a, b) = input.split_once("-").unwrap();
    let (a, b): (u32, u32) = (a.parse().unwrap(), b.parse().unwrap());

    for c in a..=b {
        result += validate(c)
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
