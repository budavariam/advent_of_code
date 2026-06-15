use aoc2019::machine::{Machine, StepResult};
use std::{
    collections::{HashMap, HashSet, VecDeque},
    fs,
};

#[derive(Copy, Clone, Debug, Eq, PartialEq, Hash)]
#[repr(isize)]
enum RDirection {
    North = 1,
    South = 2,
    West = 3,
    East = 4,
}

const DIRECTIONS: [RDirection; 4] = [
    RDirection::North,
    RDirection::South,
    RDirection::West,
    RDirection::East,
];

impl From<RDirection> for isize {
    fn from(dir: RDirection) -> Self {
        match dir {
            RDirection::North => 1,
            RDirection::South => 2,
            RDirection::West => 3,
            RDirection::East => 4,
        }
    }
}

#[repr(u8)]
enum Object {
    Empty = 0,
    Wall = 1,
    End = 2,
}

#[derive(PartialEq)]
enum RStatus {
    HitWall = 0,
    SuccessMove = 1,
    SuccessGoal = 2,
}

impl std::convert::From<isize> for RStatus {
    fn from(value: isize) -> Self {
        match value {
            0 => RStatus::HitWall,
            1 => RStatus::SuccessMove,
            2 => RStatus::SuccessGoal,
            _ => panic!("Invalid RStatus"),
        }
    }
}

type RPosition = (i32, i32);

impl std::ops::Add<&RDirection> for RPosition {
    type Output = RPosition;

    fn add(self, rhs: &RDirection) -> Self::Output {
        match *rhs {
            RDirection::North => (self.0 + 1, self.1),
            RDirection::South => (self.0 - 1, self.1),
            RDirection::West => (self.0, self.1 - 1),
            RDirection::East => (self.0, self.1 + 1),
        }
    }
}

type RWorldMap = HashMap<RPosition, Object>;

struct RepairRobot {
    cpu: Machine,
    position: RPosition,
    world: RWorldMap,
}

impl RepairRobot {
    fn new(input: &str) -> Self {
        let code = Machine::parse_program(input);
        let m = Machine::new(code);

        RepairRobot {
            cpu: m,
            position: (0, 0),
            world: HashMap::new(),
        }
    }

    fn send_robot(&mut self, next_pos: RPosition) -> Option<RStatus> {
        let mut last_status = None;
        let pth: Vec<RDirection> = self.find_shortest_path(self.position, next_pos);
        for n in pth {
            let step = self.cpu.start();
            match step {
                StepResult::NeedsInput => {
                    self.cpu.push_input(n.into());
                }
                _ => panic!("CPU shall recieve input"),
            }
            let step = self.cpu.start();
            match step {
                StepResult::Output(o) => {
                    last_status = Some(o.into());
                }
                _ => panic!("CPU shall give output"),
            }
        }

        last_status
    }

    fn find_shortest_path(&self, s: RPosition, e: RPosition) -> Vec<RDirection> {
        if s == e {
            return vec![];
        }

        let mut queue = VecDeque::from([s]);
        let mut visited = HashSet::from([s]);
        let mut parent: HashMap<RPosition, (RPosition, RDirection)> = HashMap::new();

        while let Some(curr) = queue.pop_front() {
            for dir in &DIRECTIONS {
                let next = curr + dir;
                if visited.contains(&next) {
                    continue;
                }
                match self.world.get(&next) {
                    Some(Object::Empty) | Some(Object::End) => {}
                    _ if next == e => {}
                    _ => continue,
                }
                visited.insert(next);
                parent.insert(next, (curr, *dir));
                if next == e {
                    // bfs makes sure that the first match is the shortest
                    return reconstruct_path(&parent, s, e);
                }
                queue.push_back(next);
            }
        }

        panic!("No path found from {:?} to {:?}", s, e);
    }

    fn explore_world(&mut self) -> (RPosition, RPosition) {
        let start = (0, 0);
        self.world.insert(start, Object::Empty);

        let mut visited: HashSet<RPosition> = HashSet::new();
        visited.insert(start);

        let end_pos = self.explore_dfs(start, &mut visited);
        (start, end_pos.expect("End not found"))
    }

    fn explore_dfs(
        &mut self,
        cur: RPosition,
        visited: &mut HashSet<RPosition>,
    ) -> Option<RPosition> {
        for d in &DIRECTIONS {
            let next_pos = cur + d;
            if visited.contains(&next_pos) {
                continue;
            }
            let response = self.send_robot(next_pos);
            match response {
                Some(RStatus::HitWall) => {
                    self.world.insert(next_pos, Object::Wall);
                    visited.insert(next_pos);
                }
                Some(RStatus::SuccessMove) => {
                    self.position = next_pos;
                    self.world.insert(next_pos, Object::Empty);
                    visited.insert(next_pos);

                    if let Some(end) = self.explore_dfs(next_pos, &mut *visited) {
                        return Some(end);
                    } else {
                        // NOTE: move the robot back to the current position, to keep fn calls in sync with robot state
                        self.send_robot(cur);
                        self.position = cur;
                    }
                }
                Some(RStatus::SuccessGoal) => {
                    self.position = next_pos;
                    self.world.insert(next_pos, Object::End);
                    visited.insert(next_pos);
                    return Some(next_pos);
                }
                None => panic!("Robot failure"),
            }
        }

        None
    }
}

fn reconstruct_path(
    parent: &HashMap<RPosition, (RPosition, RDirection)>,
    s: RPosition,
    e: RPosition,
) -> Vec<RDirection> {
    let mut path = vec![];
    let mut pos = e;

    while pos != s {
        let (prev, dir) = parent[&pos];
        path.push(dir);
        pos = prev;
    }

    path.reverse();
    path
}

fn solution(input: &str) -> String {
    let mut r = RepairRobot::new(input);
    let (start_pos, end_pos) = r.explore_world();

    let result = r.find_shortest_path(start_pos, end_pos);
    result.len().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
