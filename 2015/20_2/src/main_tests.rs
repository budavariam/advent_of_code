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
    example_2: "10" => "1",
    example_3: "30" => "2",
    example_4: "40" => "3",
    example_5: "120" => "6",
    example_1: "150" => "8",
}
