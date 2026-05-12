use std::fs;

struct Line<'a> {
    data: &'a str,
}

impl Line<'_> {
    /*
    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    */
    fn check(self) -> bool {
        let chars: Vec<char> = self.data.chars().collect();
        let n = chars.len();

        let has_pair_twice = (0..n.saturating_sub(1)).any(|i| {
            let pair = (chars[i], chars[i + 1]);
            chars[i + 2..].windows(2).any(|w| (w[0], w[1]) == pair)
        });
        if !has_pair_twice {
            return false;
        }

        let double_letters = self.data.as_bytes().windows(3).any(|w| w[0] == w[2]);
        if !double_letters {
            return false;
        }

        true
    }
}

fn solution(input: &str) -> String {
    let mut total = 0;
    for line in input.lines() {
        let is_nice = Line { data: line }.check();
        total += if is_nice { 1 } else { 0 }
    }
    total.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
