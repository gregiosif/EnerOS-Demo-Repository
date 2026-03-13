// EnerOS Edge-Consumer Analytics Tool (Rust)
// Proactively monitors household consumption peaks

struct PowerReading {
    watts: f32,
    timestamp: u64,
}

fn analyze_peak(reading: PowerReading) -> bool {
    let peak_threshold = 2500.0; 
    if reading.watts > peak_threshold {
        println!("[Edge-RS] High demand detected: {}W. Alerting EnerOS Central...", reading.watts);
        return true;
    }
    false
}

fn main() {
    println!("[EnerOS] Rust Edge-Service started.");
    let current_reading = PowerReading { watts: 2850.5, timestamp: 1710342979 };
    
    if analyze_peak(current_reading) {
        println!("[Edge-RS] Optimization signal sent.");
    }
}
