use super::*;

macro_rules! gen_tests {
    ($($name:ident: $input:expr => $expected:expr,)+) => {
        $(
            #[test]
            fn $name() {
                assert_eq!(solution($input, (2,2), false), $expected);
            }
        )+
    };
}

gen_tests! {
    example_1: "0222112222120000" => "01\n10\n",
}
