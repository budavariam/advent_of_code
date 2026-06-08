use std::{collections::HashMap, fs};

use aoc2019::machine::Machine;

type Position = (i32, i32);

impl std::ops::Add<Direction> for Position {
    type Output = Position;

    fn add(self, rhs: Direction) -> Self::Output {
        match rhs {
            Direction::North => (self.0 - 1, self.1),
            Direction::East => (self.0, self.1 + 1),
            Direction::South => (self.0 + 1, self.1),
            Direction::West => (self.0, self.1 - 1),
        }
    }
}
#[repr(u8)]
#[derive(Copy, Clone, PartialEq, Debug)]
enum Color {
    Black,
    White,
}

impl From<isize> for Color {
    fn from(x: isize) -> Self {
        match x {
            1 => Color::White,
            _ => Color::Black,
        }
    }
}

#[repr(u8)]
#[derive(Copy, Clone, Debug)]
enum Direction {
    North,
    East,
    South,
    West,
}

impl Direction {
    fn next(self, dir: isize) -> Self {
        match self {
            Direction::North => {
                if dir == 0 {
                    Direction::West
                } else {
                    Direction::East
                }
            }
            Direction::East => {
                if dir == 0 {
                    Direction::North
                } else {
                    Direction::South
                }
            }
            Direction::South => {
                if dir == 0 {
                    Direction::East
                } else {
                    Direction::West
                }
            }
            Direction::West => {
                if dir == 0 {
                    Direction::South
                } else {
                    Direction::North
                }
            }
        }
    }
}

struct PaintingRobot {
    cpu: Machine,
    direction: Direction,
    position: Position,
}

impl PaintingRobot {
    fn build(input: &str) -> Self {
        let code = Machine::parse_program(input);
        let machine = Machine::new(code);

        PaintingRobot {
            cpu: machine,
            direction: Direction::North,
            position: (0, 0),
        }
    }

    fn step(&mut self, world: &mut HashMap<Position, Color>) -> bool {
        // println!("{:?} {:?}", self.position, self.direction);
        let over_color: Color = world.get(&self.position).map_or(Color::Black, |v| *v);
        self.cpu.push_input(over_color as isize);
        let color_to_paint = self.cpu.next().map_or(Color::Black, |v| v.into());
        let should_turn = self.cpu.next();
        let finished = should_turn.is_none();

        if !finished {
            let turn = should_turn.unwrap();
            let next_direction = self.direction.next(turn);
            let next_pos = self.position + next_direction;
            // let dbg_color = if color_to_paint == Color::White {"white"} else {"black"};
            // let dbg_turn = if turn == 0 {"left" } else {"right"};
            // println!("@: {:?}({:?}), Paint: {:?} Turn: {:?} Move to: {:?}, done?: {}", self.position, self.direction, dbg_color, dbg_turn, next_pos, finished );
            world
                .entry(self.position)
                .and_modify(|x| *x = color_to_paint)
                .or_insert(color_to_paint);
            self.position = next_pos;
            self.direction = next_direction;
        }
        finished
    }
}
fn display(world: &HashMap<Position, Color>) {
    let mut min_y = i32::MAX;
    let mut min_x = i32::MAX;
    let mut max_y = i32::MIN;
    let mut max_x = i32::MIN;
    for (y, x) in world.keys() {
        min_x = min_x.min(*x);
        min_y = min_y.min(*y);
        max_x = max_x.max(*x);
        max_y = max_y.max(*y);
    }
    let mut buffer = String::new();
    for y in min_y..=max_y {
        for x in min_x..=max_x {
            let ch = match world.get(&(y, x)) {
                Some(Color::White) => '\u{2588}',
                _ => ' ',
            };
            buffer.push(ch);
        }
        buffer.push('\n');
    }
    println!("{buffer}");
}
fn solution(input: &str) -> String {
    let mut world: HashMap<Position, Color> = HashMap::from([((0, 0), Color::White)]);
    let mut robot = PaintingRobot::build(input);

    while !robot.step(&mut world) {}
    // println!("{:?}", world);
    display(&world);
    0.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
