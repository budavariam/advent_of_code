use std::{collections::HashSet, fs};

// struct Molecule {
//     data: String,
// }

// impl Molecule {
//     // fn replace(self, from: &str, to: &str) -> String {

//     // }
// }

fn solution(input: &str) -> String {
    let mut result: HashSet<String> = HashSet::new();
    let mut rules: Vec<(&str, &str)> = vec![];

    let (chemistry, molecule) = input.split_once("\n\n").unwrap();

    for line in chemistry.lines() {
        if let Some((from, to)) = line.trim().split_once(" => ") {
            rules.push((from, to)); // TODO: H has multiple values
            println!("c: {line}");
        }
    }
    // println!("m: {molecule}");
    // println!("r: {rules:?}");

    for (r_from, r_to) in &rules {
        let matches = molecule.match_indices(r_from);
        for (m, _) in matches {
            let len_from = r_from.len();
            let new_str = format!(
                "{}{r_to}{}",
                molecule.get(..m).unwrap(),
                molecule.get((m + len_from)..).unwrap()
            );
            println!("x {molecule} ({r_from}=>{r_to}) @{m}: {new_str}");
            result.insert(new_str);
        }
        // let curr = String::from("");
        // curr.replace_range(range, replace_with);

        // result.insert(curr);
    }

    println!("{:?}", &rules);
    println!("{:?}", result);

    result.len().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
