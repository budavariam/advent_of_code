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
    example_1: "112233-112233" => "1",
    example_2: "123444-123444" => "0",
    example_3: "111122-111122" => "1",
}
