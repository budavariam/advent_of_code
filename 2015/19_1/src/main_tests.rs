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
    example_1: "H => HO
H => OH
O => HH

HOH" => "4",

// HOOH (via H => HO on the first H).
// HOHO (via H => HO on the second H).
// OHOH (via H => OH on the first H).
// HOOH (via H => OH on the second H).
// HHHH (via O => HH).

    example_2: "H => HO
H => OH
O => HH

HOHOHO" => "7",
//     example_3: "H => HO
// H => OH
// O => HH

// H" => "0",
}
