use super::*;

macro_rules! gen_tests {
        ($($name:ident: $input:expr => $expected:expr,)+) => {
            $(
                #[test]
                fn $name() {
                    assert_eq!(solution($input), $expected);
                }
            )+
        };
    }

gen_tests! {
    example_1: "Hit Points: 100
Damage: 8
Armor: 2" => "0",
    // example_2: "" => "0",
    // example_3: "" => "0",
    // example_4: "" => "0",
    // example_5: "" => "0",
}
