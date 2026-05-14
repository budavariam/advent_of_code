use std::fs;

fn look_and_say(line: String) -> String {
    let mut iter = line.chars();
    let mut prev = iter.next().unwrap();
    let mut cnt = 1;
    let mut result = String::new();
    for curr in iter {
        if curr == prev {
            cnt += 1
        } else {
            result.push_str(&format!("{}{}", cnt, prev));
            prev = curr;
            cnt = 1;
        }
    }
    result.push_str(&format!("{}{}", cnt, prev));
    result
}

fn solution(input: &str, iter_cnt: u32) -> String {
    let mut res = String::from(input);
    for _ in 0..iter_cnt {
        res = look_and_say(res);
    }
    res.len().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 40);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
