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
    example_1: ">" => "2",
    example_2: "^>v<" => "4",
    example_3: "^v^v^v^v^v" => "2",
}
