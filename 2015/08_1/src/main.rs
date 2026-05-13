use std::fs;

fn calc_text(x: &str) -> usize {
    let chars: Vec<char> = x.chars().collect();
    let mut result = 0;
    let mut skip_i_until = 0;
    for (i, d) in chars.iter().enumerate() {
        if i < skip_i_until {
            continue;
        }
        // println!("#{}: .. {} ..", i, d);
        if *d == '\\' {
            if let Some(val) = chars.get(i + 1) {
                if *val == '\"' {
                    skip_i_until = i + 2;
                    result += 1; // count the escaped quote as a single char
                } else if *val == 'x' {
                    skip_i_until = i + 4; // skip \xNN
                    result += 1
                } else if *val == '\\' {
                    skip_i_until = i + 2; // double slash counts as a single char, skip both
                    result += 1;
                } else {
                    result += 1; // single slash without special meaning
                }
            }
        } else {
            result += 1
        }
    }

    result - 2
}

fn solution(input: &str) -> String {
    let mut result = 0;
    for x in input.lines() {
        let code_length = x.chars().count();
        let memory_length = calc_text(x);
        result += code_length - memory_length;
        // println!("code: {}, memory: {}", code_length, memory_length);
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
