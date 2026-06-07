use itertools::Itertools;
use num::integer::gcd;
use std::{
    cmp::Ordering,
    collections::{HashMap, HashSet},
    fs,
};

type AsteroidLocation = (i16, i16);

#[derive(Debug, Clone, Copy)]
struct Asteroid {
    x: i16,
    y: i16,
    distance: f64,
}

impl Asteroid {
    fn new(y: i16, x: i16, distance: f64) -> Asteroid {
        Asteroid { y, x, distance }
    }

    fn normalize(&self) -> AsteroidLocation {
        let new_y = self.y;
        let new_x = self.x;
        let scale = gcd(new_x.abs(), new_y.abs());
        if scale == 0 {
            return (0, 0);
        }
        (new_y / scale, new_x / scale)
    }

    fn calc_polar_diff(&self, other: &Asteroid) -> (f64, f64) {
        let dy = (other.y - self.y) as f64;
        let dx = (other.x - self.x) as f64;
        let r = ((dy * dy) + (dx * dx)).sqrt();

        let theta = f64::atan2(dy, dx);
        let theta_deg = (theta.to_degrees() + 90.0 + 360.0) % 360.0;
        (r, theta_deg)
    }
}

impl std::fmt::Display for Asteroid {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("({},{})", self.y, self.x))
    }
}

impl std::cmp::PartialEq for Asteroid {
    fn eq(&self, other: &Self) -> bool {
        self.x == other.x && self.y == other.y
    }
}
impl Eq for Asteroid {}

impl std::ops::Add for Asteroid {
    type Output = Asteroid;
    fn add(self, rhs: Self) -> Self::Output {
        Asteroid {
            y: self.y + rhs.y,
            x: self.x + rhs.x,
            distance: self.distance,
        }
    }
}

impl std::ops::Sub for Asteroid {
    type Output = Asteroid;
    fn sub(self, rhs: Self) -> Self::Output {
        Asteroid {
            y: self.y - rhs.y,
            x: self.x - rhs.x,
            distance: self.distance,
        }
    }
}

impl std::cmp::PartialOrd for Asteroid {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl std::cmp::Ord for Asteroid {
    fn cmp(&self, other: &Self) -> Ordering {
        if other.distance == self.distance {
            Ordering::Equal
        } else if other.distance < self.distance {
            Ordering::Less
        } else {
            Ordering::Greater
        }
    }
}

fn calc_station(asteroids: &HashMap<AsteroidLocation, Asteroid>) -> Option<Asteroid> {
    let mut result = 0;
    let mut station = None;
    for og in asteroids.values() {
        let mut sees: HashSet<(i16, i16)> = HashSet::new();
        for other in asteroids.values() {
            if og == other {
                continue;
            }

            let x = *other - *og;
            sees.insert(x.normalize());
        }
        if sees.len() >= result {
            result = sees.len();
            station = Some(og);
        }
    }
    station.copied()
}

fn solution(input: &str, station_location: Option<AsteroidLocation>) -> String {
    let mut asteroids: HashMap<AsteroidLocation, Asteroid> = HashMap::new();
    for (y, line) in input.trim().lines().enumerate() {
        for (x, c) in line.chars().enumerate() {
            let y: i16 = y.try_into().unwrap();
            let x: i16 = x.try_into().unwrap();
            if c == '#' {
                asteroids.insert((y, x), Asteroid::new(y, x, 0f64));
            }
        }
    }

    let station = if let Some(s) = station_location {
        Asteroid::new(s.0, s.1, 0f64)
    } else if let Some(s) = calc_station(&asteroids) {
        s
    } else {
        panic!("Missing station!");
    };
    // println!("STATION@{:?}", station);

    let mut asteroid_circle: HashMap<i64, Vec<Asteroid>> = HashMap::new();
    for x in asteroids.values_mut() {
        if *x == station {
            continue;
        }
        let (r, deg) = station.calc_polar_diff(x);
        x.distance = r;
        let scale = 10_i64.pow(f64::DIGITS as u32);
        let deg_fixed: i64 = (deg * scale as f64).round() as i64;

        asteroid_circle
            .entry(deg_fixed)
            .and_modify(|a| {
                a.push(*x);
                a.sort();
            })
            .or_insert(vec![*x]);
    }

    let key_list: Vec<i64> = asteroid_circle.keys().copied().sorted().collect();
    let mut i = 0;

    let r = 'outer: loop {
        for g in &key_list {
            if let Some(vals) = asteroid_circle.get_mut(g) {
                let p = vals.pop();
                if let Some(d) = p {
                    // println!("#{i}@{g}: {:?}", d);
                    i += 1;
                    if i == 200 {
                        break 'outer d;
                    }
                }
            }
        }

        if asteroid_circle.values().all(|vals| vals.is_empty()) {
            break 'outer Asteroid::new(-1, -1, 0f64);
        }
    };

    (r.x * 100 + r.y).to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, None);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
