use super::*;

macro_rules! gen_tests {
        ($($name:ident: $input:expr => $expected:expr,)+) => {
            $(
                #[test]
                fn $name() {
                    assert_eq!(solution($input, 4), $expected);
                }
            )+
        };
    }

gen_tests! {
    example_1: ".#.#.#
...##.
#....#
..#...
#.#..#
####.." => "4",
}
