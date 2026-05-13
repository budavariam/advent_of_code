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
    example_1: "\"\"" => "2",
    example_2: "\"abc\"" => "2",
    example_3: "\"aaa\\\"aaa\"" => "3",
    example_4: "\"\\x27\"" => "5",
}
