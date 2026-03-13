// EnerOS Source-Level Telemetry Node (C++)
// Manages high-speed data acquisition from PV arrays and wind turbines

#include <iostream>
#include <string>

class TelemetryNode {
public:
    void send_to_kafka(std::string metric, float value) {
        std::cout << "[Edge-CPP] Telemetry Stream -> Metric: " << metric 
                  << " | Value: " << value << " MW" << std::endl;
    }
};

int main() {
    std::cout << "[EnerOS] C++ Telemetry Node Active." << std::endl;
    TelemetryNode node;
    
    float pv_output = 45.8; 
    node.send_to_kafka("Solar_Production", pv_output);
    
    return 0;
}
