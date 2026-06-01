use std::fs;

#[derive(Debug, Clone)]
struct Creature {
    _name: String,
    hp: i16,
    damage: i16,
    armor: i16,
    mana: i16,
}

impl Creature {
    fn new(name: &str, hp: i16, mana: i16) -> Self {
        Creature {
            _name: name.to_string(),
            hp,
            mana,
            damage: 0,
            armor: 0,
        }
    }
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum Spell {
    MagicMissile,
    Drain,
    Shield,
    Poison,
    Recharge,
}

impl Spell {
    fn all() -> [Spell; 5] {
        [
            Spell::MagicMissile,
            Spell::Drain,
            Spell::Shield,
            Spell::Poison,
            Spell::Recharge,
        ]
    }

    fn cost(self) -> i16 {
        match self {
            Spell::MagicMissile => 53,
            Spell::Drain => 73,
            Spell::Shield => 113,
            Spell::Poison => 173,
            Spell::Recharge => 229,
        }
    }
}

#[derive(Debug, Clone)]
struct State {
    player: Creature,
    boss: Creature,
    shield_timer: u8,
    poison_timer: u8,
    recharge_timer: u8,
    mana_spent: i16,
}

fn parse_boss(input: &str) -> Creature {
    let mut boss = Creature::new("boss", 0, 0);
    for l in input.lines() {
        if let Some((stat, value)) = l.split_once(": ") {
            let value: i16 = value.parse().unwrap();
            if stat.starts_with('H') {
                boss.hp = value;
            } else if stat.starts_with('D') {
                boss.damage = value;
            } else if stat.starts_with('A') {
                boss.armor = value;
            }
        }
    }
    boss
}

fn apply_effects(state: &mut State) {
    if state.shield_timer > 0 {
        state.player.armor = 7;
        state.shield_timer -= 1;
        if state.shield_timer == 0 {
            state.player.armor = 0;
        }
    } else {
        state.player.armor = 0;
    }

    if state.poison_timer > 0 {
        state.boss.hp -= 3;
        state.poison_timer -= 1;
    }

    if state.recharge_timer > 0 {
        state.player.mana += 101;
        state.recharge_timer -= 1;
    }
}

fn can_cast(state: &State, spell: Spell) -> bool {
    if state.player.mana < spell.cost() {
        return false;
    }

    match spell {
        Spell::Shield => state.shield_timer == 0,
        Spell::Poison => state.poison_timer == 0,
        Spell::Recharge => state.recharge_timer == 0,
        Spell::MagicMissile | Spell::Drain => true,
    }
}

fn cast_spell(state: &mut State, spell: Spell) {
    let cost = spell.cost();
    state.player.mana -= cost;
    state.mana_spent += cost;

    match spell {
        Spell::MagicMissile => {
            state.boss.hp -= 4;
        }
        Spell::Drain => {
            state.boss.hp -= 2;
            state.player.hp += 2;
        }
        Spell::Shield => {
            state.shield_timer = 6;
        }
        Spell::Poison => {
            state.poison_timer = 6;
        }
        Spell::Recharge => {
            state.recharge_timer = 5;
        }
    }
}

fn search(state: State, best: &mut i16) {
    if state.mana_spent >= *best {
        return;
    }

    let mut next = state.clone();

    apply_effects(&mut next);

    next.player.hp -= 1;
    if next.player.hp <= 0 {
        return;
    }

    if next.boss.hp <= 0 {
        *best = (*best).min(next.mana_spent);
        return;
    }

    for spell in Spell::all() {
        if !can_cast(&next, spell) {
            continue;
        }

        let mut next2 = next.clone();

        cast_spell(&mut next2, spell);
        if next2.mana_spent >= *best {
            continue;
        }
        if next2.boss.hp <= 0 {
            *best = (*best).min(next2.mana_spent);
            continue;
        }

        apply_effects(&mut next2);
        if next2.boss.hp <= 0 {
            *best = (*best).min(next2.mana_spent);
            continue;
        }

        let damage = (next2.boss.damage - next2.player.armor).max(1);
        next2.player.hp -= damage;
        if next2.player.hp <= 0 {
            continue;
        }

        search(next2, best);
    }
}

fn solution(input: &str) -> String {
    let boss = parse_boss(input);
    let player = Creature::new("player", 50, 500);

    let initial = State {
        player,
        boss,
        shield_timer: 0,
        poison_timer: 0,
        recharge_timer: 0,
        mana_spent: 0,
    };

    let mut best = i16::MAX;
    search(initial, &mut best);
    best.to_string()
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input.txt");
    let answer = solution(&input);
    println!("Answer: {}", answer);
}

#[cfg(test)]
mod main_tests;
