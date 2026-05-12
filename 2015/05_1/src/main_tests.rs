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
    example_1: "ugknbfddgicrmopn" => "1",
    example_2: "aaa" => "1",
    example_3: "jchzalrnumimnmhp" => "0",
    example_4: "haegwjzuvuyypxyu" => "0",
    example_5: "dvszwmarrgswjxmb" => "0",
}
