use std::fs;

fn encode_line(x: &str) -> String {
    let mut result = String::from("");
    result.push('"');
    for c in x.chars() {
        match c {
            '\\' => result.push_str("\\\\"),
            '"' => result.push_str("\\\""),
            _ => result.push(c),
        }
    }
    result.push('"');
    result
}
fn solution(input: &str) -> String {
    let mut result = 0;
    for x in input.lines() {
        let encoded_length = encode_line(x).chars().count();
        let code_length = x.chars().count();
        result += encoded_length - code_length;
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
