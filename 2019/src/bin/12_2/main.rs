use regex::Regex;
use std::collections::HashSet;
use std::collections::hash_map::DefaultHasher;
use std::fs;
use std::hash::{Hash, Hasher};

fn hash_vec<T: Hash>(vec: &Vec<T>) -> u64 {
    let mut hasher = DefaultHasher::new();
    vec.hash(&mut hasher);
    hasher.finish()
}

#[derive(Hash, Copy, Clone)]
struct Coord {
    x: i32,
    y: i32,
    z: i32,
}

impl Coord {
    fn new(x: i32, y: i32, z: i32) -> Coord {
        Coord { x, y, z }
    }

    #[allow(dead_code)]
    fn repr(&self) -> String {
        format!("<x={}, y={}, z={}>", self.x, self.y, self.z)
    }
}

impl std::ops::Add for Coord {
    type Output = Self;
    fn add(self, rhs: Self) -> Self::Output {
        Self {
            x: self.x + rhs.x,
            y: self.y + rhs.y,
            z: self.z + rhs.z,
        }
    }
}

#[derive(Hash, Copy, Clone)]
struct Moon {
    pos: Coord,
    vel: Coord,
}

/** helper fn to get 2 mutable parts of an iterable */
fn get_two_mut<T>(xs: &mut [T], i: usize, j: usize) -> (&mut T, &mut T) {
    assert!(i < j, "i must be less than j");
    let (left, right) = xs.split_at_mut(j);
    (&mut left[i], &mut right[0])
}

impl Moon {
    fn parse(input: &str, pt: &Regex) -> Self {
        let m = pt.captures(input).unwrap();
        let x = m["x"].parse().unwrap();
        let y = m["y"].parse().unwrap();
        let z = m["z"].parse().unwrap();
        Moon {
            pos: Coord::new(x, y, z),
            vel: Coord::new(0, 0, 0),
        }
    }
    #[allow(dead_code)]
    fn repr(&self) -> String {
        format!("pos={}, vel={}", self.pos.repr(), self.pos.repr())
    }
    fn apply_gravity(a: &mut Moon, b: &mut Moon) {
        // a Gx3+1, b: Cx5-1
        if a.pos.x > b.pos.x {
            a.vel.x += -1;
            b.vel.x += 1;
        } else if a.pos.x < b.pos.x {
            a.vel.x += 1;
            b.vel.x += -1;
        };
        if a.pos.y > b.pos.y {
            a.vel.y += -1;
            b.vel.y += 1;
        } else if a.pos.y < b.pos.y {
            a.vel.y += 1;
            b.vel.y += -1;
        }
        if a.pos.z > b.pos.z {
            a.vel.z += -1;
            b.vel.z += 1;
        } else if a.pos.z < b.pos.z {
            a.vel.z += 1;
            b.vel.z += -1;
        }
    }
    /**
     * The total energy for a single moon is its potential energy multiplied by its kinetic energy.
     *
     * A moon's potential energy is the sum of the absolute values of its x, y, and z position coordinates.
     * A moon's kinetic energy is the sum of the absolute values of its velocity coordinates.
     */
    fn total_energy(&self) -> i32 {
        let pot = self.pos.x.abs() + self.pos.y.abs() + self.pos.z.abs();
        let kin = self.vel.x.abs() + self.vel.y.abs() + self.vel.z.abs();
        pot * kin
    }
}

fn solution(input: &str) -> String {
    let mut step = 0;
    let pt = Regex::new(r"<x=(?P<x>-?\d+), y=(?P<y>-?\d+), z=(?P<z>-?\d+)>").unwrap();
    let mut moons: Vec<Moon> = input.lines().map(|m| Moon::parse(m, &pt)).collect();
    let mut hsh = hash_vec(&moons);
    let mut visited: HashSet<u64> = HashSet::new();
    let result = loop {
        if step % 100_000 == 0 {
            println!("{step}");
        }
        // 1. apply gravity to change velocities
        for i in 0..moons.len() {
            for j in i + 1..moons.len() {
                //let m1 = &mut moons[i];
                //let m2 = &mut moons[j];
                let (m1, m2) = get_two_mut(&mut moons, i, j);
                Moon::apply_gravity(m1, m2);
            }
        }
        // 2. apply velocity to move the moon's position:w
        moons.iter_mut().for_each(|m| {
            m.pos = m.pos + m.vel;
        });

        /*println!("After {step} steps:");
        for m in &moons {
            println!("{}", m.repr());
        }*/
        hsh = hash_vec(&moons);
        if visited.contains(&hsh) {
            break step;
        }
        visited.insert(hsh);
        step += 1;
    };

    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
