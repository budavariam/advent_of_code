extern crate regex;

use regex::Regex;
use std::{collections::HashMap, fs};

#[derive(Debug)]
enum State {
    Resting(i32),
    Flying(i32),
}

#[derive(Debug)]
struct Competitor {
    _name: String,
    fly_speed: i32,
    fly_time: i32,
    rest_time: i32,

    score: i32,
    state: State,
    distance: i32,
}

impl Competitor {
    fn new(name: &str, fly_speed: i32, fly_time: i32, rest_time: i32) -> Self {
        Competitor {
            _name: name.to_string(),
            fly_speed: fly_speed,
            fly_time: fly_time,
            rest_time: rest_time,

            distance: 0,
            state: State::Flying(fly_time - 1),

            score: 0,
        }
    }

    fn step_time(&mut self) -> i32 {
        match self.state {
            State::Resting(remaining_rest_time) => {
                if remaining_rest_time == 0 {
                    self.state = State::Flying(self.fly_time - 1);
                } else {
                    self.state = State::Resting(remaining_rest_time - 1);
                }
            }
            State::Flying(remaining_fly_time) => {
                self.distance += self.fly_speed;
                if remaining_fly_time == 0 {
                    self.state = State::Resting(self.rest_time - 1);
                } else {
                    self.state = State::Flying(remaining_fly_time - 1);
                }
            }
        }
        self.distance
    }

    fn add_score(&mut self, max_distance: i32) -> i32 {
        if self.distance == max_distance {
            self.score += 1;
        }
        self.score
    }
}

fn solution(input: &str, finish_time_at: i32) -> String {
    // let mut result = 0;
    let mut competitors: HashMap<String, Competitor> = HashMap::new();

    let re = Regex::new(
        r"(?P<reindeer>\w+) can fly (?P<fly_speed>\d+) km/s for (?P<fly_time>\d+) seconds, but then must rest for (?P<rest_time>\d+) seconds\.",
    ).unwrap();
    for line in input.lines() {
        if let Some(captures) = re.captures(line) {
            let reindeer = &captures["reindeer"].to_string();
            let fly_speed: i32 = captures["fly_speed"].parse().unwrap();
            let fly_time: i32 = captures["fly_time"].parse().unwrap();
            let rest_time: i32 = captures["rest_time"].parse().unwrap();
            competitors.insert(
                reindeer.to_string(),
                Competitor::new(reindeer, fly_speed, fly_time, rest_time),
            );
        }
    }

    // let mut curr_location =
    for _curr_sec in 1..=finish_time_at {
        // println!("{curr_sec}");
        let mut max_dist = 0;
        for c in competitors.values_mut() {
            // println!("{:?}... {}", c, curr_sec);
            max_dist = max_dist.max(c.step_time());
        }

        for c in competitors.values_mut() {
            c.add_score(max_dist);
        }
    }

    let mut max_score = 0;
    for c in competitors.values() {
        max_score = max_score.max(c.score);
    }
    max_score.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 2503);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
