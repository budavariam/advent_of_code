use super::*;

macro_rules! gen_tests {
    ($($name:ident: $input:expr => $expected:expr,)+) => {
        $(
            #[test]
            fn $name() {
                assert_eq!(solution($input, true), $expected);
            }
        )+
    };
}

gen_tests! {
    example_1: "1,9,10,3,2,3,11,0,99,30,40,50" => "3500",
}
