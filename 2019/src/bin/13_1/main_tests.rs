use super::*;

use aoc2019::intcode_out;

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
    example_1: intcode_out!(1,2,3,6,5,4) => "0",
    example_2: intcode_out!(1,2,2,6,5,2) => "2",
}
