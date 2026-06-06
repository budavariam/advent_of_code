use std::fs;

fn solution(input: &str, dim: (i32, i32), prettyprint: bool) -> String {
    let (cols, rows) = dim;
    let layer_size: usize = (cols * rows).try_into().expect("layer size fits usize");
    let chars: Vec<char> = input.trim().chars().collect();
    let layer_cnt = chars.len().saturating_div(layer_size);
    let mut result: String = String::new();
    for y in 0..rows {
        for x in 0..cols {
           //println!("{y}_{x}");
           let mut px = '2';
           for layer_id in 0..layer_cnt {
                let pos = (layer_size * layer_id) + (y*cols + x) as usize;
                //  0 is black, 1 is white, and 2 is transparent
                    //println!(" [{:?}]  {layer_size}x{layer_id}x({y}x{x}) => #{pos}", chars);
                if let Some(n) = chars.get(pos) && n != &'2' {
                    if prettyprint {

                    px = if n == &'0' { ' ' } else { '\u{2588}' }; 
                    } else {
                    px = *n;
                    }//println!(" {px}");
                   break;
                }
           }
           result.push(px);
        }
        result.push('\n');
    }

    result
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input, (25, 6), true);

    println!("Answer:\n{}", answer);
}

#[cfg(test)]
mod main_tests;
