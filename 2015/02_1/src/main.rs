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
        let surface_area = 2 * l * w + 2 * w * h + 2 * h * l;
        let smallest_area = min(l * w, min(w * h, h * l));
        total += surface_area + smallest_area;
    }

    total.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let solution = solution(&input);

    println!("Part 1: {}", solution);
}

#[cfg(test)]
mod main_tests;
