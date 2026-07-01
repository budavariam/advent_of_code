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
    example_1: "03036732577212944063491565474664" => "84462026",
    example_2: "02935109699940807407585447034323" => "78725270",
    example_3: "03081770884921959731165446850517" => "53553731",
}