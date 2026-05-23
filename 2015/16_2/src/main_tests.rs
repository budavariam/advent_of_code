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
    example_1: "Sue 1: goldfish: 6, trees: 9, akitas: 0
Sue 2: goldfish: 5, trees: 3, akitas: 0
Sue 3: cars: 10, akitas: 6, perfumes: 7" => "2",
}
