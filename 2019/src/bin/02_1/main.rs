use std::fs;

fn interpret_int_code(mut code: Vec<usize>) -> Vec<usize> {
    let mut curr = 0;
    loop {
        match code[curr] {
            99 => return code,
            1 => {
                let pos_a = code[curr + 1];
                let pos_b = code[curr + 2];
                let pos_target = code[curr + 3];
                code[pos_target] = code[pos_a] + code[pos_b];
            }
            2 => {
                let pos_a = code[curr + 1];
                let pos_b = code[curr + 2];
                let pos_target = code[curr + 3];
                code[pos_target] = code[pos_a] * code[pos_b];
            }
            _ => {}
        }
        curr += 4;
    }
}

fn solution(input: &str, is_test: bool) -> String {
    let mut ints: Vec<usize> = input
        .split(',')
        .collect::<Vec<_>>()
        .iter()
        .filter_map(|n| n.parse().ok())
        .collect();
    if !is_test {
        ints[1] = 12;
        ints[2] = 2;
    }

    let ints = interpret_int_code(ints);

    ints[0].to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, false);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
