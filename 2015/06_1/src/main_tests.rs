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
    example_1: "turn on 0,0 through 999,999" => "1000000",
    example_2: "toggle 0,0 through 999,0" => "1000",
    example_3: "turn off 499,499 through 500,500" => "0",
    example_4: "" => "0",
    example_5: "" => "0",
}
