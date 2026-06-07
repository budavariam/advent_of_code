use std::{
    collections::{HashMap, HashSet},
    fs,
};

use num::integer::gcd;

#[derive(Clone, Copy, PartialEq, Eq)]
struct Asteroid {
    y: i16,
    x: i16,
}

impl Asteroid {
    fn new(y: i16, x: i16) -> Asteroid {
        Asteroid { y, x }
    }

    fn normalize(&self) -> (i16, i16) {
        let new_y = self.y;
        let new_x = self.x;
        let scale = gcd(new_x, new_y);
        // println!("normalize: {self} ({new_y},{new_x})x{scale}");
        (new_y / scale, new_x / scale)
    }
}

impl std::fmt::Display for Asteroid {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("({},{})", self.y, self.x))
    }
}

impl std::ops::Add for Asteroid {
    type Output = Asteroid;
    fn add(self, rhs: Self) -> Self::Output {
        Asteroid {
            y: self.y + rhs.y,
            x: self.x + rhs.x,
        }
    }
}

impl std::ops::Sub for Asteroid {
    type Output = Asteroid;
    fn sub(self, rhs: Self) -> Self::Output {
        Asteroid {
            y: self.y - rhs.y,
            x: self.x - rhs.x,
        }
    }
}

fn solution(input: &str) -> String {
    let mut asteroids: HashMap<(i16, i16), Asteroid> = HashMap::new();

    for (y, line) in input.lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            let y: i16 = y.try_into().unwrap();
            let x: i16 = x.try_into().unwrap();
            if c == '#' {
                asteroids.insert((y, x), Asteroid::new(y, x));
            }
        }
    }

    let mut result = 0;
    for og in asteroids.values() {
        let mut sees: HashSet<(i16, i16)> = HashSet::new();
        for other in asteroids.values() {
            if og == other {
                continue;
            }

            let x = *other - *og;
            sees.insert(x.normalize());
        }
        result = result.max(sees.len());
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
