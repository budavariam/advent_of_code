use super::*;

macro_rules! gen_tests {
        ($($name:ident: $input:expr => $expected:expr,)+) => {
            $(
                #[test]
                fn $name() {
                    assert_eq!(solution($input, 25), $expected);
                }
            )+
        };
    }

gen_tests! {
    example_1: "20\n15\n10\n5\n5" => "3",
}
