extern crate itertools;

use itertools::Itertools;
use std::{collections::HashMap, fs};

const ITEMS: &'static str = "Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3";

#[derive(Debug, Clone)]
struct Creature {
    _name: String,
    hp: u8,
    damage: u8,
    armor: u8,
}

impl Creature {
    fn new(name: &str, hp: u8) -> Self {
        Creature {
            _name: name.to_string(),
            hp,
            damage: 0,
            armor: 0,
        }
    }
}

#[derive(Debug, PartialEq, Eq, Hash, Clone)]
enum ItemType {
    Unknown,
    Weapon,
    Armor,
    Ring,
}

#[derive(Debug, Clone)]
struct Item {
    item_type: ItemType,
    item_name: String,
    cost: u8,
    damage: u8,
    armor: u8,
}

impl Item {
    fn new() -> Self {
        Item {
            item_name: String::new(),
            armor: 0,
            cost: 0,
            damage: 0,
            item_type: ItemType::Unknown,
        }
    }
}

fn parse_items() -> HashMap<ItemType, Vec<Item>> {
    let mut result = HashMap::new();
    for section in ITEMS.split("\n\n") {
        let mut item = Item::new();
        let mut lines = section.lines();
        let first_line = lines.next().unwrap();
        item.item_type = if first_line.starts_with("W") {
            ItemType::Weapon
        } else if first_line.starts_with("A") {
            ItemType::Armor
        } else if first_line.starts_with("R") {
            ItemType::Ring
        } else {
            println!("ERROR: CAN NOT PARSE ITEM: {}", first_line);
            ItemType::Unknown
        };

        for l in lines {
            // println!("{:?}", l);
            let line: Vec<_> = l.split_whitespace().collect();
            assert!(line.len() >= 4);
            let mut i = 0;
            item.item_name = line.get(i).unwrap().to_string();
            if item.item_type == ItemType::Ring {
                i += 1;
                item.item_name.push_str(" ");
                item.item_name.push_str(line.get(i).unwrap());
            };
            i += 1;
            item.cost = line.get(i).unwrap().parse().unwrap();
            i += 1;
            item.damage = line.get(i).unwrap().parse().unwrap();
            i += 1;
            item.armor = line.get(i).unwrap().parse().unwrap();

            result
                .entry(item.item_type.clone())
                .and_modify(|c: &mut Vec<Item>| c.push(item.clone()))
                .or_insert(vec![item.clone()]);
        }
        // println!("Store: {:?}", result);
    }
    result
}

fn parse_boss(input: &str) -> Creature {
    let mut boss = Creature::new("boss", 0);
    for l in input.lines() {
        if let Some((stat, value)) = l.split_once(": ") {
            let value: u8 = value.parse().unwrap();
            if stat.starts_with("H") {
                boss.hp = value;
            } else if stat.starts_with("D") {
                boss.damage = value;
            } else if stat.starts_with("A") {
                boss.armor = value;
            }
        }
    }
    boss
}

fn choose_items(items: &HashMap<ItemType, Vec<Item>>) -> Vec<Vec<&Item>> {
    let mut result = vec![];
    // You must buy exactly one weapon; no dual-wielding. 5 option
    // Armor is optional, but you can't use more than one. 5 option
    // You can buy 0-2 rings (at most one for each hand). 6 option
    // combinations: (5) * (5+1) * (1+6+15)

    let weapons: &Vec<Item> = items.get(&ItemType::Weapon).unwrap();
    let mut armor: Vec<Option<&Item>> = items
        .get(&ItemType::Armor)
        .unwrap()
        .iter()
        .map(|f| Some(f))
        .collect();
    armor.push(None::<&Item>);

    let mut ring_vec: Vec<Option<&Item>> = items
        .get(&ItemType::Ring)
        .unwrap()
        .iter()
        .map(|f| Some(f))
        .collect();
    ring_vec.push(None::<&Item>);

    let rings: Vec<(Option<&Item>, Option<&Item>)> = {
        let some_rings: Vec<&Item> = ring_vec.iter().filter_map(|&x| x).collect();

        std::iter::once((None, None))
            .chain(some_rings.iter().map(|r| (Some(*r), None)))
            .chain(
                some_rings
                    .iter()
                    .combinations(2)
                    .map(|pair| (Some(*pair[0]), Some(*pair[1]))),
            )
            .collect()
    };

    // println!(
    //     "Combo count: {} {} {}",
    //     rings.len(),
    //     weapons.len(),
    //     armor.len(),
    // );

    for w in weapons {
        for a in &armor {
            for (r1, r2) in &rings {
                let mut v = vec![w];
                if let Some(has_armor) = a {
                    v.push(has_armor);
                }
                if let Some(has_r1) = r1 {
                    v.push(has_r1);
                }
                if let Some(has_r2) = r2 {
                    v.push(has_r2);
                }
                result.push(v);
            }
        }
    }

    result
}

fn simulate_fight<'a>(mut player: &'a mut Creature, mut boss: &'a mut Creature) -> bool {
    /*
        In this game, the player (you) and the enemy (the boss) take turns attacking.
        The player always goes first. Each attack reduces the opponent's hit points by at least 1.
        The first character at or below 0 hit points loses.

        Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.
        An attacker always does at least 1 damage.
        So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points.
        If the defender had an armor score of 300, the defender would still lose 1 hit point.
    */
    let mut players_turn = true;
    while player.hp > 0 && boss.hp > 0 {
        let (attacker, target) = if players_turn {
            (&mut player, &mut boss)
        } else {
            (&mut boss, &mut player)
        };
        let damage = 1.max(attacker.damage.saturating_sub(target.armor));
        target.hp = target.hp.saturating_sub(damage);
        // println!(
        //     "The {} deals {} damage; the boss goes down to {} hit points.",
        //     attacker.name, damage, target.hp
        // );

        players_turn = !players_turn;
    }

    boss.hp == 0
}

fn solution(input: &str) -> String {
    let mut result = u32::MAX;

    let boss = parse_boss(input);
    let player = Creature::new("player", 100);

    let items = parse_items();

    // println!("{:?}", boss);
    // println!("{:?}", player);
    // println!("{:?}", items);
    let all_combos = choose_items(&items);
    println!("{:?}", all_combos.len());

    for item_combo in &all_combos {
        let mut curr_player = player.clone();
        let mut curr_boss = boss.clone();
        for item in item_combo {
            curr_player.armor += item.armor;
            curr_player.damage += item.damage;
        }

        let player_wins = simulate_fight(&mut curr_player, &mut curr_boss);

        if player_wins {
            let sum_price = item_combo.iter().map(|x| x.cost as u32).sum();
            result = result.min(sum_price);
        }
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
