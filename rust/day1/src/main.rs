use std:: {
    fs::File,
    io::{self, BufRead, BufReader}
};

fn get_input(path: &str) -> io::Result<Vec<String>>{
    BufReader::new(File::open(path)?).lines().collect()
}

fn calculate_fuel(n: i32) -> i32{
    (((f64::from(n) /3f64).floor() as i32) -2)
}

fn main() {
    let reader = get_input("../../1.in").expect("Could not read file");
    let mut fuel_module: i32 = 0;
    let mut additional: i32 = 0;

    for line in reader {
        let fuel: i32 = calculate_fuel(i32::from_str_radix(&line, 10).unwrap());
        fuel_module += fuel;

        let mut additional_fuel = calculate_fuel(fuel);

        while additional_fuel > 0 {
            additional += additional_fuel;
            additional_fuel = calculate_fuel(additional_fuel);
            
        }
    };

    println!("part1: {}", fuel_module);
    println!("part1: {}", fuel_module + additional);
}
