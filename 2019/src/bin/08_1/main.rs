use std::collections::HashMap;
use std::fs;

fn solution(input: &str, dim: (i32, i32)) -> String {
    let (cols, rows) = dim;
    let layer_size: usize = (cols * rows).try_into().expect("layer size fits usize");
    let chars: Vec<char> = input.trim().chars().collect();
    let mut layers: Vec<HashMap<char, i32>> = vec![];
    let mut min_zeroes = (i32::MAX, 0); // count, layer_id
    // println!("input: {}", input);

    for (layer, chunk) in chars.chunks_exact(layer_size).enumerate() {
        let mut layer_map: HashMap<char, i32> = HashMap::new();

        for c in chunk {
            // for (i, c) in chunk.iter().enumerate() {
            // let curr_pos: i32 = i.try_into().expect("index fits i32");
            // println!("{curr_pos}-'{c}' {rows}x{cols} ({layer} {})", layers.len());
            layer_map
                .entry(*c)
                .and_modify(|x| {
                    *x = *x + 1;
                })
                .or_insert(1);
        }

        let number_of_zeroes = *layer_map.get(&'0').unwrap_or_else(|| &0);
        if number_of_zeroes < min_zeroes.0 {
            min_zeroes = (number_of_zeroes, layer);
        }

        layers.push(layer_map);
        //println!("{:?}", layers);
    }

    // println!("{:?}", min_zeroes);
    let layer_with_min_zeroes = layers.get(min_zeroes.1).unwrap();
    let result = layer_with_min_zeroes.get(&'1').unwrap_or(&0)
        * layer_with_min_zeroes.get(&'2').unwrap_or(&0);
    result.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, (25, 6));

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
