use std::fs;

// fn validate(num: u32) -> i32 {
//     let numstr: Vec<char> = num.to_string().chars().collect();
//     let has_double = numstr.windows(3).any(|w| {
//         !(w[0] == w[1] && w[1] == w[2])
//             && ((w[0] == w[1] && w[1] != w[2]) || (w[0] != w[1] && w[1] == w[2]))
//     });
//     let never_decrease = numstr.windows(2).all(|w| w[0] <= w[1]);
//     if numstr.len() == 6 && has_double && never_decrease {
//         1
//     } else {
//         0
//     }
// }

fn validate(num: u32) -> i32 {
    let numstr: Vec<char> = num.to_string().chars().collect();

    let mut i = 0;
    let has_double = loop {
        if i >= numstr.len() {
            break false;
        }

        let mut j = i + 1;
        while j < numstr.len() && numstr[j] == numstr[i] {
            j += 1;
        }

        if j - i == 2 {
            break true;
        }

        i = j;
    };

    let never_decrease = numstr.windows(2).all(|w| w[0] <= w[1]);
    if numstr.len() == 6 && has_double && never_decrease {
        1
    } else {
        0
    }
}

fn solution(input: &str) -> String {
    let mut result = 0;
    let (a, b) = input.split_once("-").unwrap();
    let (a, b): (u32, u32) = (a.parse().unwrap(), b.parse().unwrap());

    for c in a..=b {
        result += validate(c)
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
