use std::fs;

const NUM_NAMES: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

trait IsDecDigit {
    fn is_dec_digit(self) -> bool;
}

impl IsDecDigit for char {
    fn is_dec_digit(self) -> bool {
        self.is_digit(10)
    }
}

fn main() {
    let document = fs::read_to_string("./days/day_1/data/document.txt").expect("Unable to read file");
    let lines = document.lines();
    println!("Total lines: {}", lines.clone().count());

    // Part 1
    let start = std::time::Instant::now();
    let result: u32 = lines
        .map(|line| {
            format!(
                "{}{}",
                line.chars().nth(line.find(char::is_dec_digit).unwrap()).unwrap(),
                line.chars().nth(line.rfind(char::is_dec_digit).unwrap()).unwrap()
            )
            .parse::<u32>()
            .unwrap()
        })
        .sum();
    let end = std::time::Instant::now();

    println!("Result: {:?}", result);
    println!("Time elapsed: {:?}", end - start);

    // Part 2

    println!("Result: {:?}", result);
    println!("Time elapsed: {:?}", end - start);
}
