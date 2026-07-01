use std::fs;

#[derive(Clone, Copy)]
enum State {
    NZero,
    Positive,
    PZero,
    Negative,
}
impl State {
    fn next_state(prev: State) -> State {
        match prev {
            Self::NZero => Self::Positive,
            Self::Positive => Self::PZero,
            Self::PZero => Self::Negative,
            Self::Negative => Self::NZero,
        }
    }
}

fn generate_it_sequence(nth: i32) -> impl Iterator<Item = (i32, i8)> {
    let mut st = State::Negative;
    (0_i32..).filter_map(move |i| {
        if i % nth == 0 {
            st = State::next_state(st);
        }
        match st {
            State::Positive => Some((i, 1)),
            State::Negative => Some((i, -1)),
            _ => None,
        }
    })
}

fn apply_phase(txt: Vec<u8>) -> Vec<u8> {
    let l = txt.len();
    let mut result: Vec<u8> = Vec::with_capacity(l);
    for i in 0..l {
        let mut r = 0i32;
        let nth: i32 = i.try_into().expect("index number shall fit");
        let sq = generate_it_sequence(nth + 1).take_while(|(x, _)| *x <= l as i32);
        for (x, t) in sq {
            let char_index = (x - 1) as usize;
            let v = *txt.get(char_index).expect("should be number") as i32;
            let xx = v * t as i32;
            r += xx;
        }
        r = r.abs() % 10;
        result.push(r as u8);
    }
    result
}



fn solution(input: &str) -> String {
    let mut curr: Vec<u8> = input.bytes().map(|b| b - b'0').collect();
    let phase_cnt = 100;
    for _phc in 0..phase_cnt {
        // println!("{_phc}");
        let nxt = apply_phase(curr.clone());
        curr = nxt;
        //println!("{}", curr);
    }
    curr.get(0..8)
        .expect("shall be longer than 8 chars")
        .iter()
        .map(|b| b.to_string())
        .collect::<Vec<String>>()
        .join("")
}

fn main() {
    let input = fs::read_to_string("input.txt")
        .expect("Failed to read input.txt")
        .trim()
        .to_string();
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
