use std::{
    collections::{HashMap, HashSet},
    fs,
};

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
struct Point(i32, i32); // y,x

#[derive(Debug)]
enum Direction {
    Right(i32),
    Up(i32),
    Down(i32),
    Left(i32),
}

impl Direction {
    fn parse(input: &str) -> Self {
        let mut in_iter = input.chars();
        let dir_type = in_iter.next();
        let count: i32 = in_iter.collect::<String>().parse().unwrap();
        match dir_type {
            Some('R') => Direction::Right(count),
            Some('U') => Direction::Up(count),
            Some('D') => Direction::Down(count),
            Some('L') => Direction::Left(count),
            _ => panic!("Can not parse Direction"),
        }
    }

    fn next_points(&self, curr: &Point) -> Vec<Point> {
        match &self {
            Direction::Up(c) => (0..=*c).map(|i| Point(curr.0 + i, curr.1)).collect(),
            Direction::Down(c) => (0..=*c).map(|i| Point(curr.0 - i, curr.1)).collect(),
            Direction::Right(c) => (0..=*c).map(|i| Point(curr.0, curr.1 + i)).collect(),
            Direction::Left(c) => (0..=*c).map(|i| Point(curr.0, curr.1 - i)).collect(),
        }
    }
}

fn draw(line: Vec<Direction>) -> HashMap<Point, i32> {
    let mut curr = Point(0, 0);
    let mut dist = 0;
    let mut result = HashMap::from([(curr, 0)]);
    for x in line {
        let next = x.next_points(&curr);
        let next_point = *next.last().unwrap();

        let line: HashMap<Point, i32> = HashMap::from_iter(
            next.into_iter()
                .skip(1)
                .enumerate()
                .map(|(k, v)| (v, dist + k as i32 + 1)),
        );

        for (p, steps) in line {
            result.entry(p).or_insert(steps);
        }

        dist += match x {
            Direction::Up(c) | Direction::Down(c) | Direction::Left(c) | Direction::Right(c) => c,
        };

        curr = next_point;
    }
    result
}
fn solution(input: &str) -> String {
    let mut lines_iter = input.lines();
    let wire_a: Vec<_> = lines_iter
        .next()
        .unwrap()
        .split(',')
        .map(Direction::parse)
        .collect();
    let wire_b: Vec<_> = lines_iter
        .next()
        .unwrap()
        .split(',')
        .map(Direction::parse)
        .collect();

    let points_a = draw(wire_a);
    let points_b = draw(wire_b);
    // println!("{:?}", points_a);
    // println!("{:?}", points_b);

    let pts_a: HashSet<&Point> = HashSet::from_iter(points_a.keys());
    let pts_b: HashSet<&Point> = HashSet::from_iter(points_b.keys());

    let pts: HashSet<_> = pts_a.intersection(&pts_b).copied().collect();
    // println!("{:?}", pts);

    // for x in pts {
    //     println!(
    //         "{} vs {}",
    //         points_a.get(x).unwrap(),
    //         points_b.get(x).unwrap()
    //     );
    // }

    pts.iter()
        .map(|x| points_a.get(x).unwrap() + points_b.get(x).unwrap())
        .filter(|x| *x > 0)
        .min()
        .unwrap()
        .to_string()

    // if let Some(result) = pts.map(|d| d.distance_origo()).filter(|x| *x > 0).min() {
    //     return result.to_string();
    // }
    // String::new()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
