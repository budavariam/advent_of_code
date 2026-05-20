extern crate regex;

use regex::Regex;
use std::{collections::HashMap, fs};

fn solution(input: &str, finish_time_at: i32) -> String {
    // let mut result = 0;
    let mut competitors: HashMap<String, (i32, i32, i32)> = HashMap::new();

    let re = Regex::new(
        r"(?P<reindeer>\w+) can fly (?P<fly_speed>\d+) km/s for (?P<fly_time>\d+) seconds, but then must rest for (?P<rest_time>\d+) seconds\.",
    ).unwrap();
    for line in input.lines() {
        if let Some(captures) = re.captures(line) {
            let reindeer = &captures["reindeer"].to_string();
            let fly_speed: i32 = captures["fly_speed"].parse().unwrap();
            let fly_time: i32 = captures["fly_time"].parse().unwrap();
            let rest_time: i32 = captures["rest_time"].parse().unwrap();
            competitors.insert(reindeer.to_string(), (fly_speed, fly_time, rest_time));
            // println!("{} {} {}", fly_speed, fly_time, rest_time);
        }
    }

    let mut result_all = 0;
    for (_name, (speed, time, rest)) in competitors {
        // Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        // 0s: 0km
        // 10s: 140km
        // 137s: 140km
        // 138s: 154km
        // 147s: 280km
        // 148s: 280km
        // after 1000s Comet is at 1120
        // 1000//(10s+127rs)=7x (% 41s) -> 7x140 ('a980) + (min(|41, 10|)x14 -> ('a140) --> ('a1120)

        let full_phase_cnt = finish_time_at / (time + rest);
        let full_phase_rem_time = finish_time_at % (time + rest);

        let remaining_time_to_fly = full_phase_rem_time.min(time);

        let full_phase_fly = full_phase_cnt * time * speed;
        let remaining_fly = remaining_time_to_fly * speed;
        let result = full_phase_fly + remaining_fly;
        result_all = result_all.max(result);
        // println!("{} {}", name, result);
    }

    // result.to_string()
    result_all.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 2503);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
