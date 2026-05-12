use std::fs;

struct Line<'a> {
    data: &'a str,
}

impl Line<'_> {
    /*
    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    */
    fn check(self) -> bool {
        let vowels = "aeiou";
        let vowel_count = self.data.chars().filter(|c| vowels.contains(*c)).count();
        if vowel_count < 3 {
            return false;
        }

        let double_letters = self.data.as_bytes().windows(2).any(|w| w[0] == w[1]);
        if !double_letters {
            return false;
        }

        let forbidden = ["ab", "cd", "pq", "xy"];
        let has_forbidden = self
            .data
            .chars()
            .collect::<Vec<char>>()
            .windows(2)
            .any(|w| {
                let pair: String = w.iter().collect();
                forbidden.contains(&pair.as_str())
            });

        if has_forbidden {
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
