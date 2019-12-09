use std::fs;

fn get_input(path: &str) -> std::vec::Vec<u32>{
    let file = fs::read_to_string(path).expect("Could not read file");
    // println!("pc: {:?}", file);
    let ins: Vec<u32> = file.trim().split(",").map(|s| s.parse().unwrap()).collect();
    ins
}

fn get_val(inst: &Vec<u32>, pc: usize) -> (u32, u32) {
    let (p1, p2) = (inst[pc+1], inst[pc+2]);
    (inst[p1 as usize], inst[p2 as usize])
}

// Rust doesn't have optional args, yet :(
fn compute(mut inst: Vec<u32>) -> u32 {
    let mut pc = 0;

    loop {
        let op = inst[pc];

        match op {
            1 => {
                
                let (val1, val2) = get_val(&inst, pc);
                let result = inst[pc+3];
                inst[result as usize] = val1+val2;
                pc += 4
            },
            
            2 => {
                let (val1, val2) = get_val(&inst, pc);
                let result = inst[pc+3];
                inst[result as usize] = val1*val2;
                pc += 4
            },

            99 => {break;},
            _ => {break;},
        }
    }
    inst[0]
}

fn brute_force(inst: Vec<u32>, target: u32) -> u32 {
    for i in 0..99 {
        for j in 0..99 {
            let mut inst = inst.clone();
            inst[1] = i;
            inst[2] = j;

            let res = compute(inst);
            if res == target {
                return 100 * i + j;
            }
        }
    } 
    0
}

fn main() {
    let inst = get_input("../../2.in");

    let mut p1_input = inst.clone();
    p1_input[1] = 12;
    p1_input[2] = 2;
    let p1_ans = compute(p1_input);
    let p2_ans = brute_force(inst, 19690720);
    println!("ans p1: {}", p1_ans);
    println!("ans p2: {}", p2_ans);
}
