use std::{cmp::min, fs};

fn solution(input: &str) -> String {
    let mut total = 0;

    for line in input.lines() {
        let dimensions = line.split("x");
        let nums: Vec<i32> = dimensions.map(|e| e.parse::<i32>().unwrap()).collect();
        //println!("{:?}", nums);
        let [l, w, h, ..] = nums[..] else {
            panic!("not enough dimensions")
        };
        let smallest_perimeter = min(2 * (l + w), min(2 * (h + w), 2 * (l + h)));
        let bow = l * w * h;
        total += smallest_perimeter + bow;
    }

    total.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let solution = solution(&input);

    println!("Part 2: {}", solution);
}

#[cfg(test)]
mod main_tests;
