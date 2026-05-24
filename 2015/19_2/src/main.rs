use std::fs;

fn find_minimal_transform_cnt(molecule: &str, rules: &Vec<(&str, &str)>) -> i32 {
    let end = "e";
    let mut current = molecule.to_string();
    let mut level = 0;

    let mut sorted_rules = rules.clone();
    // try the longest ones first...
    sorted_rules.sort_by_key(|(_, from)| std::cmp::Reverse(from.len()));
    // println!("{:?}", sorted_rules);
    while current != end {
        let mut changed = false;

        for (r_to, r_from) in &sorted_rules {
            if let Some(pos) = current.find(r_from) {
                let len_from = r_from.len();
                current = format!(
                    "{}{r_to}{}",
                    current.get(..pos).unwrap(),
                    current.get((pos + len_from)..).unwrap()
                );
                level += 1;
                changed = true;
                break;
            }
        }

        if !changed {
            // prevent an infinite loop
            return 0;
        }
    }

    level
}

fn solution(input: &str) -> String {
    let mut rules: Vec<(&str, &str)> = vec![];
    let (chemistry, molecule) = input.split_once("\n\n").unwrap();

    for line in chemistry.lines() {
        if let Some((from, to)) = line.trim().split_once(" => ") {
            rules.push((from, to));
            // println!("r: {line}");
        }
    }

    // println!("{:?}", &rules);
    // println!("{:?}", result);
    let result = find_minimal_transform_cnt(molecule.trim(), &rules);
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
