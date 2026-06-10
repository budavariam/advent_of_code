use num::integer::lcm;
use regex::Regex;
use std::fs;

enum Axis {
    X,
    Y,
    Z,
}

#[derive(Copy, Clone)]
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

#[derive(Copy, Clone)]
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
    fn apply_gravity(a: &mut Moon, b: &mut Moon, axis: &Axis) {
        match axis {
            Axis::X => Moon::apply_gravity_x(a, b),
            Axis::Y => Moon::apply_gravity_y(a, b),
            Axis::Z => Moon::apply_gravity_z(a, b),
        }
    }

    fn apply_gravity_x(a: &mut Moon, b: &mut Moon) {
        // a Gx3+1, b: Cx5-1
        if a.pos.x > b.pos.x {
            a.vel.x += -1;
            b.vel.x += 1;
        } else if a.pos.x < b.pos.x {
            a.vel.x += 1;
            b.vel.x += -1;
        };
    }
    fn apply_gravity_y(a: &mut Moon, b: &mut Moon) {
        if a.pos.y > b.pos.y {
            a.vel.y += -1;
            b.vel.y += 1;
        } else if a.pos.y < b.pos.y {
            a.vel.y += 1;
            b.vel.y += -1;
        }
    }
    fn apply_gravity_z(a: &mut Moon, b: &mut Moon) {
        if a.pos.z > b.pos.z {
            a.vel.z += -1;
            b.vel.z += 1;
        } else if a.pos.z < b.pos.z {
            a.vel.z += 1;
            b.vel.z += -1;
        }
    }

    fn get_axis_state(&self, axis: &Axis) -> (i32, i32) {
        match axis {
            Axis::X => (self.pos.x, self.vel.x),
            Axis::Y => (self.pos.y, self.vel.y),
            Axis::Z => (self.pos.z, self.vel.z),
        }
    }

    fn get_all_state(moons: &Vec<Moon>, axis: &Axis) -> Vec<(i32, i32)> {
        moons.iter().map(|m| m.get_axis_state(axis)).collect()
    }
}

fn solution(input: &str) -> String {
    let pt = Regex::new(r"<x=(?P<x>-?\d+), y=(?P<y>-?\d+), z=(?P<z>-?\d+)>").unwrap();
    let mut moons: Vec<Moon> = input.lines().map(|m| Moon::parse(m, &pt)).collect();
    let mut step: [u128; 3] = [0, 0, 0];

    for (i, axis) in [Axis::X, Axis::Y, Axis::Z].iter().enumerate() {
        let initial_state: Vec<(i32, i32)> = Moon::get_all_state(&moons, &axis);
        let mut state: Vec<(i32, i32)> = vec![];
        while state != initial_state {
            // 1. apply gravity to change velocities
            for i in 0..moons.len() {
                for j in i + 1..moons.len() {
                    //let m1 = &mut moons[i];
                    //let m2 = &mut moons[j];
                    let (m1, m2) = get_two_mut(&mut moons, i, j);
                    Moon::apply_gravity(m1, m2, &axis);
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
            state = Moon::get_all_state(&moons, &axis);
            step[i] += 1;
        }
    }

    lcm(lcm(step[0], step[1]), step[2]).to_string()
}
fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
