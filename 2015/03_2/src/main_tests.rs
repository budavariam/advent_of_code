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
    example_1: "^v" => "3",
    example_2: "^>v<" => "3",
    example_3: "^v^v^v^v^v" => "11",
}
