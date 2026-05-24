use std::{
    collections::{HashMap, HashSet},
    fs,
};

fn find_divisors(num: i32) -> HashSet<i32> {
    let sqrt = (num as f64).sqrt().floor() as i32;
    let mut res: HashSet<i32> = HashSet::new();
    for i in 1..=sqrt {
        if num % i == 0 {
            res.insert(i);
            res.insert(num / i);
        }
    }
    res
}

fn solution(input: &str) -> String {
    let target: i32 = input.parse().unwrap();
    let mut curr = 0;
    let mut curr_max = 0;
    let mut track_elves: HashMap<i32, i32> = HashMap::new();
    while curr_max < target {
        curr += 1;
        let divisors = find_divisors(curr);
        for x in &divisors {
            track_elves
                .entry(*x)
                .and_modify(|c| *c = *c + 1)
                .or_insert(1);
        }
        let present_cnt = divisors
            .iter()
            .filter(|d| *(track_elves.entry(**d).or_default()) <= 50)
            .map(|e| e * 11)
            .sum();
        curr_max = curr_max.max(present_cnt);
        if curr % 100_000 == 0 || curr_max >= target {
            println!("{curr}: {divisors:?} = {present_cnt}");
        }
    }

    curr.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
