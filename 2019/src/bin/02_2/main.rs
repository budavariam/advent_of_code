use std::fs;

struct Machine {
    memory: Vec<usize>,
}

impl Machine {
    fn new(code: Vec<usize>) -> Self {
        Machine { memory: code }
    }

    fn set_input_pair(&mut self, noun: usize, verb: usize) {
        self.memory[1] = noun;
        self.memory[2] = verb;
    }
    fn interpret_int_code(&mut self) -> Vec<usize> {
        let mut ip = 0;
        let ref mut code = self.memory;
        loop {
            let instruction = code[ip];
            let mut ip_increase = 1;
            match instruction {
                99 => return code.to_vec(),
                1 => {
                    let pos_a = code[ip + 1];
                    let pos_b = code[ip + 2];
                    let pos_target = code[ip + 3];
                    ip_increase += 3;
                    code[pos_target] = code[pos_a] + code[pos_b];
                }
                2 => {
                    let pos_a = code[ip + 1];
                    let pos_b = code[ip + 2];
                    let pos_target = code[ip + 3];
                    ip_increase += 3;
                    code[pos_target] = code[pos_a] * code[pos_b];
                }
                _ => {}
            }
            ip += ip_increase;
        }
    }
}

fn solution(input: &str) -> String {
    let ints: Vec<usize> = input
        .split(',')
        .collect::<Vec<_>>()
        .iter()
        .filter_map(|n| n.parse().ok())
        .collect();

    for noun in 0..=99 {
        for verb in 0..=99 {
            let mut m = Machine::new(ints.clone());
            m.set_input_pair(noun, verb);
            let res = m.interpret_int_code();
            if res[0] == 19690720 {
                return (100 * noun + verb).to_string();
            }
        }
    }

    0.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
