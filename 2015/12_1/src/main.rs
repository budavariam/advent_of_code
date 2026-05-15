use std::fs;

enum Text {
    Ignore,
    Sign,
    Number,
    NegativeNumber,
}

fn calc_line_sum(line: &str) -> i32 {
    let (collected_numbers, _, _) = line.chars().fold(
        (Vec::<i32>::new(), 0i32, Text::Ignore),
        |(mut item_list, mut curr_num, prev_kind), curr_char| {
            if curr_char.is_digit(10) {
                let digit = curr_char.to_digit(10).unwrap() as i32;
                match prev_kind {
                    Text::Sign => {
                        curr_num = -1 * digit;
                        (item_list, curr_num, Text::NegativeNumber)
                    }
                    Text::Number => {
                        curr_num = 10 * curr_num + digit;
                        (item_list, curr_num, Text::Number)
                    }
                    Text::NegativeNumber => {
                        curr_num = 10 * curr_num - digit;
                        (item_list, curr_num, Text::NegativeNumber)
                    }
                    Text::Ignore => {
                        curr_num = 1 * digit;
                        (item_list, curr_num, Text::Number)
                    }
                }
            } else if curr_char == '-' {
                (item_list, 0, Text::Sign)
            } else {
                if curr_num != 0 {
                    item_list.push(curr_num);
                }
                (item_list, 0, Text::Ignore)
            }
        },
    );
    collected_numbers.iter().sum()
}

fn solution(input: &str) -> String {
    let mut result = 0;
    for line in input.lines() {
        result += calc_line_sum(&line);
    }
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
