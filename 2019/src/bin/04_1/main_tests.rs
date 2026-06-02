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
    example_1: "111111-111111" => "1",
    example_2: "223450-223450" => "0",
    example_3: "123789-123789" => "0",
}
