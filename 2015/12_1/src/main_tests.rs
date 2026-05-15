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
    example_1: "[1,2,3]" => "6",
    example_2: "{\"a\":2,\"b\":4}" => "6",
    example_3: "[[[3]]]" => "3",
    example_4: "{\"a\":{\"b\":4},\"c\":-1}" => "3",
    example_5: "{\"a\":[-1,1]}" => "0",
    example_6: "[-1,{\"a\":1}]" => "0",
    example_7: "[]" => "0",
    example_8: "{}" => "0",
}
