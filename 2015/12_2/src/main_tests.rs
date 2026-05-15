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
    example_2: "[1,{\"c\":\"red\",\"b\":2},3]" => "4",
    example_3: "{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}" => "0",
    example_4: "{\"a\":{\"b\":4},\"c\":-1}" => "3",
    example_5: "[1,\"red\",5]" => "6",
}
