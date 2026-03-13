FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    g++ \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY eneros_engine.py .
COPY edge_meter.rs .
COPY telemetry_node.cpp .

RUN rustc edge_meter.rs -o edge_meter

RUN g++ telemetry_node.cpp -o telemetry_node

RUN echo 'echo "--- Running Rust Edge Analytics ---" && ./edge_meter && \
          echo "\n--- Running C++ Telemetry Node ---" && ./telemetry_node && \
          echo "\n--- Running Python AI Orchestrator ---" && python eneros_engine.py' > run_demo.sh

RUN chmod +x run_demo.sh

CMD ["./run_demo.sh"]
