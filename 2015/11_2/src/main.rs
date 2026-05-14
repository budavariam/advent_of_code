use std::{collections::HashSet, fs};

fn is_valid_pw(s: &str) -> bool {
    // Passwords must include one increasing straight of at least three letters,
    // like abc, bcd, cde, and so on, up to xyz.
    // They cannot skip letters; abd doesn't count.
    let has_increasing_straight = s
        .chars()
        .collect::<Vec<char>>()
        .windows(3)
        .any(|c| (c[0] as u32 + 1) == (c[1] as u32) && (c[0] as u32 + 2) == (c[2] as u32));
    if !has_increasing_straight {
        return false;
    }
    // Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    let has_forbidden_letter = s.chars().any(|c| match c {
        'i' | 'o' | 'l' => true,
        _ => false,
    });
    if has_forbidden_letter {
        return false;
    }
    // Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
    let pairs: HashSet<char> = s
        .chars()
        .collect::<Vec<char>>()
        .windows(2)
        .fold((HashSet::new(), ' '), |(mut set, last), w| {
            if w[0] == w[1] && w[0] != last {
                set.insert(w[0]);
                (set, w[0]) // remember last char to prevent overlap
            } else {
                (set, last)
            }
        })
        .0;
    if pairs.len() < 2 {
        return false;
    }

    true
}

fn increase(s: &str) -> String {
    let mut data: Vec<u8> = s.bytes().collect();
    // carry from the rightmost byte
    for byte in data.iter_mut().rev() {
        if *byte == b'z' {
            *byte = b'a'; // wrap and carry
        } else {
            *byte += 1; // no carry needed, stop
            break;
        }
    }
    String::from_utf8(data).unwrap()
}

fn get_next(start: &str) -> String {
    let mut curr = start.to_string();
    loop {
        curr = increase(&curr);
        if is_valid_pw(&curr) {
            break;
        }
    }
    curr
}

fn solution(input: &str) -> String {
    let first = get_next(input);
    get_next(&first)
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input.trim());
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
