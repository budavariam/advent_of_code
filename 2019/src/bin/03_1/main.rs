use std::{collections::HashSet, fs};

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
struct Point(i32, i32); // y,x

impl Point {
    // fn distance_manhattan(&self, other: &Point) -> u32 {
    //     self.0.abs_diff(other.0) + self.1.abs_diff(other.1)
    // }
    fn distance_origo(&self) -> i32 {
        self.0.abs() + self.1.abs()
    }
}

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

fn draw(line: Vec<Direction>) -> HashSet<Point> {
    let mut curr = Point(0, 0);
    let mut result = HashSet::from([curr]);
    for x in line {
        let next = x.next_points(&curr);
        let next_point = next.last().unwrap().clone();
        let line: HashSet<Point> = next.into_iter().collect();
        result.extend(&line);
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

    let pts = points_a.intersection(&points_b);
    // println!("{:?}", pts);

    if let Some(result) = pts.map(|d| d.distance_origo()).filter(|x| *x > 0).min() {
        return result.to_string();
    }
    String::new()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
