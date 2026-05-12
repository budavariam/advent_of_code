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
    example_1: "turn on 0,0 through 0,0" => "1",
    example_2: "toggle 0,0 through 999,999" => "2000000",
}
