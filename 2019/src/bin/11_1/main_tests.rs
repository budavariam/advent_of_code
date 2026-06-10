use aoc2019::intcode_out;

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
    // example_1: "104,1,104,0,104,0,104,0,104,1,104,0,104,1,104,0,104,0,104,1,104,1,104,0,104,1,104,0,99" => "6",
    example_1: intcode_out!(
    1, 0,
    0, 0,
    1, 0,
    1, 0,
    0, 1,
    1, 0,
    1, 0
) => "6",
}
