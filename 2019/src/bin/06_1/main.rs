use std::rc::Rc;
use std::fs;
use std::collections::{HashMap};

#[derive(Debug)]
struct Node {
   _name: String, 
   children: Vec<Rc<Node>>,
}

impl Node {
    fn count_orbits(&self, depth: u32) -> u32 {
        let mut result = depth;
        // println!("{} Counting {}",depth,  self.name);
        for c in self.children.iter() {
           result += c.count_orbits(depth + 1); 
        }
        result
    }
}
fn init_tree(nodes: &mut HashMap<String, Rc<Node>>, edges: &[(String, String)], start: &str) -> Rc<Node> {
    if let Some(node) = nodes.get(start) {
        return Rc::clone(node);
    }

    let children_names: Vec<&String> = edges.iter().filter(|(parent, _)| parent == start).map(|(_, child)|child).collect();
    let children:  Vec<Rc<Node>> = children_names.iter().map(|child| init_tree(nodes, edges, child)).collect();
    let node = Rc::new(Node {
        _name: start.to_string(),
        children,
    });
    nodes.insert(start.to_string(), Rc::clone(&node));
    node
}

fn solution(input: &str) -> String {
    let mut nodes: HashMap<String, Rc<Node>> = HashMap::new();
    let mut edges: Vec<(String, String)> = Vec::new();
    for line in input.lines() {
        let (around, orbiting) = line.split_once(")").unwrap();
        edges.push((around.to_string(), orbiting.to_string()));
    }

    init_tree(&mut nodes, &edges, "COM");
    // println!("{:?}", &nodes);
    let root = nodes.get("COM").unwrap();
    root.count_orbits(0).to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
