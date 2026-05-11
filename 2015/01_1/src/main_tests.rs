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
    example_1: "(())"     => "0",
    example_2: "()()"     => "0",
    example_3: "((("      => "3",
    example_4: "(()(()("  => "3",
    example_5: "))(((((" => "3",
    example_6: "())"      => "-1",
    example_7: "))("      => "-1",
    example_8: ")))"      => "-3",
    example_9: ")())())"  => "-3",
}
