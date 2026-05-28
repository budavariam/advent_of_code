use std::fs;

fn solution(_input: &str, result_register: char) -> String {
    // let mut a: u64 = 0;
    let mut a: u64 = 1;
    let mut b: u64 = 0;
    a = if a % 2 == 0 {
        // a = ((((((a+2)*3*3*3)+2)*3)+2)*3*3*3)+1
        // a = ((((((a + 2) * 27) + 2) * 3) + 2) * 27) + 1
        2187 * a + 4591
    } else {
        // a = (((((((((((((((a*3)+2)*3)+2)*3*3)+2)*3)+1)*3)+1)*3)+2)*3)+1)*3*3)+1
        59049 * a + 54334
    };

    while a != 1 {
        b = b + 1;
        a = if a % 2 == 1 { (a * 3) + 1 } else { a / 2 }
    }

    println!("a: {a}, b: {b}");
    if result_register == 'a' {
        a.to_string()
    } else {
        b.to_string()
    }
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, 'b');
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
