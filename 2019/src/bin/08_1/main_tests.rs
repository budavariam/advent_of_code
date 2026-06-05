use super::*;

macro_rules! gen_tests {
    ($($name:ident: $input:expr => $expected:expr,)+) => {
        $(
            #[test]
            fn $name() {
                assert_eq!(solution($input, (3,2)), $expected);
            }
        )+
    };
}

gen_tests! {
    example_1: "223456789012" => "0",
    example_2: "111222789012" => "9",
}
