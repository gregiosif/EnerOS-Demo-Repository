<div align="center">

# ⚡ EnerOS

### A Unified Software Framework for Intelligent Energy Orchestration

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Rust](https://img.shields.io/badge/Rust-Edge_Layer-000000?logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![C++](https://img.shields.io/badge/C%2B%2B-Telemetry-00599C?logo=cplusplus&logoColor=white)](https://isocpp.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19004280.svg)](https://doi.org/10.5281/zenodo.19004280)

*Bridging the digital coordination gap in modern energy grids through AI-driven orchestration*

</div>

---

## Overview

**EnerOS** is an integrated, polyglot software ecosystem for real-time monitoring and intelligent management of energy flows across the grid. This repository contains the **Proof-of-Concept (PoC)** implementation, spanning three architectural layers:

| Layer | Technology | Role |
|---|---|---|
| 🧠 Neural Orchestration | Python / AI | Cloud-level demand forecasting & routing |
| 📊 Edge-Consumer Analytics | Rust | Smart meter real-time peak detection |
| ⚡ Source-Level Telemetry | C++ | High-speed renewable energy acquisition |

> Based on the research paper:
> **Iosifidis, G. (2026).** *EnerOS: A Unified Software Framework for Intelligent Energy Orchestration and Predictive Resource Management.* Zenodo. [https://doi.org/10.5281/zenodo.19004280](https://doi.org/10.5281/zenodo.19004280)

---

## ✨ Key Features

- **🤖 Neural Orchestration (Python/AI):** LSTM networks for localized demand forecasting and intelligent energy routing decisions.
- **🦀 Edge Computing (Rust):** Memory-safe, high-performance analytics running directly on smart meter hardware for real-time peak detection.
- **⚡ Low-Latency Telemetry (C++):** Sub-millisecond data acquisition from renewable sources — PV arrays, wind turbines, and beyond.
- **📉 Waste Mitigation:** Reduces energy curtailment from **10% → 0.5%** by closing the "digital coordination gap."
- **🐳 Containerized Deployment:** Production-ready Docker and Kubernetes configurations for global-scale rollout.

---

## 📁 Repository Structure

```
EnerOS-Framework-Demo/
│
├── eneros_engine.py       # Core AI engine: LSTM forecasting & decision logic (Python)
├── edge_meter.rs          # Household analytics for smart meters (Rust)
├── telemetry_node.cpp     # High-speed source-level diagnostics (C++)
│
├── Dockerfile             # Container config for the Python AI environment
└── requirements.txt       # Python dependencies (TensorFlow, NumPy, Scikit-learn)
```

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed on your system:

- **Python** 3.9+
- **Rust** compiler (`rustc`) — [Install via rustup](https://rustup.rs/)
- **C++** compiler (`g++`)
- **Docker** *(optional, for containerized deployment)*

### Installation & Execution

**1. Clone the repository**
```bash
git clone https://github.com/gregiosif/EnerOS-Framework-Demo.git
cd EnerOS-Framework-Demo
```

**2. Run the AI Orchestrator (Python)**
```bash
pip install -r requirements.txt
python eneros_engine.py
```

**3. Run the Edge Meter Analytics (Rust)**
```bash
rustc edge_meter.rs && ./edge_meter
```

**4. Run the Source Telemetry Node (C++)**
```bash
g++ telemetry_node.cpp -o telemetry && ./telemetry
```

---

## 🏗️ Polyglot Architecture

EnerOS uses a deliberate multi-language design to optimize performance at each layer of the grid:

```
┌─────────────────────────────────────────────────────┐
│              ☁️  CLOUD ORCHESTRATION LAYER           │
│         Python · TensorFlow · LSTM Networks          │
│        (AI/ML ecosystem · demand forecasting)        │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│              🏠  CONSUMER EDGE LAYER                 │
│            Rust · Smart Meters · IoT                 │
│      (thread safety · ultra-fast local processing)   │
└────────────────────────┬────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────┐
│              ☀️  SOURCE TELEMETRY LAYER              │
│         C++ · PV Arrays · Wind Turbines              │
│   (sub-millisecond response · grid stabilization)    │
└─────────────────────────────────────────────────────┘
```

Each language was selected for its strengths at that tier: **Python** for AI/ML depth, **Rust** for memory-safe IoT performance, and **C++** for the hard real-time constraints of grid hardware.

---

## 📊 Expected Results

The simulation demonstrates the **load-leveling effect**: consumption is proactively shifted from peak demand hours to periods of high renewable production (e.g., solar noon). This results in:

- ✅ Stabilized grid frequency
- ✅ Reduced curtailment from **10% to 0.5%**
- ✅ Increased renewable energy utilization by ~**18%**

---

## 📖 Citation

If you use EnerOS or the associated research in your work, please cite:

```bibtex
@misc{iosifidis2026eneros,
  author    = {Iosifidis, G.},
  title     = {EnerOS: A Unified Software Framework for Intelligent Energy
               Orchestration and Predictive Resource Management},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19004280},
  url       = {https://doi.org/10.5281/zenodo.19004280}
}
```

---

## 📄 License

Distributed under the **CC0 1.0 Universal** (Public Domain Dedication). See [`LICENSE`](LICENSE) for details.

---

<div align="center">
<sub>Built with ⚡ for a smarter, greener grid.</sub>
</div>
