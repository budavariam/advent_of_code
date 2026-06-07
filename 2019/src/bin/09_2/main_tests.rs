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
    example_1: "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99" => "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99",
    example_2: "1102,34915192,34915192,7,4,7,99,0" => "1219070632396864",
    example_3: "104,1125899906842624,99" => "1125899906842624",
}
