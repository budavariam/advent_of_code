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
      // example_0: "12345678" => "",
    example_1: "80871224585914546619083218645595" => "24176176",
    example_2: "19617804207202209144916044189917" => "73745418",
    example_3: "69317163492948606335995924319873" => "52432133",
}

