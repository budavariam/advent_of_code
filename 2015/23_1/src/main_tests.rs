use super::*;

macro_rules! gen_tests {
        ($($name:ident: $input:expr => $expected:expr,)+) => {
            $(
                #[test]
                fn $name() {
                    assert_eq!(solution($input, 'a'), $expected);
                }
            )+
        };
    }

gen_tests! {
    example_1: "inc a
jio a, +2
tpl a
inc a" => "2",
}
