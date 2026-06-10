use std::fs;

use aoc2019::machine::{Machine};
use std::collections::HashMap;

type Position=(isize, isize);

#[derive(Debug)]
enum Object {
    Empty,
    Wall,
    Block,
    HorizontalPaddle,
    Ball,
}

impl Object {
    /*
        0 is an empty tile. No game object appears in this tile.
        1 is a wall tile. Walls are indestructible barriers.
        2 is a block tile. Blocks can be broken by the ball.
        3 is a horizontal paddle tile. The paddle is indestructible.
        4 is a ball tile. The ball moves diagonally and bounces off objects.
    */
    fn parse(object_type: isize) -> Self {
        match object_type {
            1 => Object::Wall,
            2 => Object::Block,
            3 => Object::HorizontalPaddle,
            4 => Object::Ball,
            _ => Object::Empty, 
        }
    }
}
/*
struct Arcade {
    cpu: Machine,
}
*/

fn solution(input: &str) -> String {

    let code = Machine::parse_program(input);
    let mut m = Machine::new(code);
    let mut buffer: HashMap<Position, Object> = HashMap::new();
    
    loop {
        let it = &mut m;
        let left = it.next();
        if left.is_none() {
            break;
        }
        let left = left.unwrap();
        let top = it.next().expect("2");
        let object_type =  it.next().expect("3");
        
        buffer.insert((top, left), Object::parse(object_type));
    }


    //println!("{:?}", buffer);
    let result: isize = buffer.values().filter(|x| matches!(x, Object::Block)).map(|_| 1).sum();
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
