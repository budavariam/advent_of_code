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
    example_1: "e => H
e => O
H => HO
H => OH
O => HH

HOH" => "3",
    example_2: "e => H
e => O
H => HO
H => OH
O => HH

HOHOHO" => "6",
}
