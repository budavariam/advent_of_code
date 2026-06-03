use std::rc::Rc;
use std::fs;
use std::collections::{HashMap, HashSet};

#[derive(Debug)]
struct Node {
   _name: String, 
   children: Vec<Rc<Node>>,
}

impl Node {
    fn find(&self, other: &str) -> Option<Vec<String>> {
        if self._name == other {
            return Some(vec![self._name.clone()]);
        }
        for n in &self.children {
            if let Some(other_on_path)= n.find(other) {
                let mut curr = vec![self._name.clone()];
                for x in other_on_path {
                    curr.push(x);
                }
                return Some(curr); 
            }
        }
        None
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
    // root.count_orbits(0).to_string()
    let pth_san: HashSet<String> = HashSet::from_iter(root.find("SAN").unwrap().into_iter());
    let pth_you: HashSet<String> = HashSet::from_iter(root.find("YOU").unwrap().into_iter());
    let ends: HashSet<String> = HashSet::from([String::from("SAN"), String::from("YOU")]);
    let res1: HashSet<String> = pth_san.symmetric_difference(&pth_you).cloned().collect();
    let res2: HashSet<String> = res1.symmetric_difference(&ends).cloned().collect();
    // println!("{:?}",res2);
    res2.len().to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);

    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
