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
    // example_1: "hijklmmn" => "0",
    // example_2: "abbceffg" => "0",
    // example_3: "abbcegjk" => "0",
    example_4: "abcdefgh" => "abcdffaa",
    example_5: "ghijklmn" => "ghjaabcc",
}
