use super::*;

macro_rules! gen_tests {
        ($($name:ident: $input:expr => $expected:expr,)+) => {
            $(
                #[test]
                fn $name() {
                    assert_eq!(solution($input, 1), $expected);
                }
            )+
        };
    }

gen_tests! {
    example_1: "1" => "11",
    example_2: "11" => "21",
    example_3: "21" => "1211",
    example_4: "1211" => "111221",
    example_5: "111221" => "312211",
}
