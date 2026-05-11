use std::fs;

fn solution(input: &str) -> String {
    let mut answer = 0;
    let mut item = String::new();
    loop {
        item.clear();
        item.push_str(input);
        item.push_str(&answer.to_string());

        let digest = md5::compute(item.as_bytes());
        let hex = format!("{:x}", digest);
        if hex.starts_with("00000") {
            break;
        }
        // print!("{:?} {:?}\n", answer, digest);
        answer += 1;
    }
    answer.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
