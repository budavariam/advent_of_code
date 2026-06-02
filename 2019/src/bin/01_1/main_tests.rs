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
    example_1: "12" => "2",
    example_2: "14" => "2",
    example_3: "1969" => "654",
    example_4: "100756" => "33583",
}
