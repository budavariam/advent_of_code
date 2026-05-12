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
    example_1: "qjhvhtzxzqqjkmpb" => "1",
    example_2: "xxyxx" => "1",
    example_3: "uurcxstgmygtbstg" => "0",
    example_4: "ieodomkazucvgmuy" => "0",
}
