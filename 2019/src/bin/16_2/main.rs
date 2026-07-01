use std::fs;

/// Mathematical assumptions based on Reddit
///
/// 1. Last digit never changes: Last digit stays identical across all phases
/// 2. Offset is in the second half
/// 3. Pattern becomes all 1s: When offset > length/2, FFT pattern simplifies to 0s then 1s
/// 4. Backwards cumulative sum: Output = sum of all input digits from that position to end (mod 10)
///
/// See: https://www.reddit.com/r/adventofcode/comments/ebf5cy/
fn apply_phase(txt: Vec<u8>, offset: usize) -> Vec<u8> {
    let l = txt.len();
    let mut result = txt.clone();
    let mut carry = 0i32;

    for i in (offset..l).rev() {
        carry = (carry + result[i] as i32) % 10;
        result[i] = carry as u8;
    }

    result
}

fn solution(input: &str) -> String {
    let signal: Vec<u8> = input.bytes().map(|b| b - b'0').collect();
    let offset_str: String = signal.iter().take(7).map(|b| b.to_string()).collect();
    let offset: usize = offset_str.parse().expect("offset shall be valid");
    let phase_cnt = 100;

    let mut curr: Vec<u8>;

    curr = signal
        .iter()
        .cycle()
        .take(10000 * signal.len())
        .map(|&b| b)
        .collect();
    curr = curr[offset..].to_vec();

    for _phc in 0..phase_cnt {
        // println!("{_phc}");
        curr = apply_phase(curr.clone(), 0);
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
