import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

class EnerOSEngine:
    def __init__(self):
        self.model = self._build_model()
        self.scaler = MinMaxScaler()
        print("[EnerOS] Neural Orchestration Layer Initialized.")

    def _build_model(self):
        model = Sequential([
            LSTM(50, activation='relu', input_shape=(10, 1)),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        return model

    def predict_demand(self, history):
        """Προβλέπει τη ζήτηση βασισμένη σε ιστορικά δεδομένα [cite: 51]"""
        data = np.array(history).reshape(-1, 1)
        scaled_data = self.scaler.fit_transform(data)
        prediction = self.model.predict(scaled_data.reshape(1, 10, 1), verbose=0)
        return self.scaler.inverse_transform(prediction)[0][0]

    def orchestrate(self, prod, pred_dem, soc):
        """Κεντρικός αλγόριθμος λήψης αποφάσεων (Master Model) [cite: 54, 55]"""
        surplus = prod - pred_dem
        if surplus > 0:
            if soc < 95:
                status = "CHARGING_STORAGE"
                routing = f"Redirecting {surplus:.2f} MW to Hydrogen/Battery."
            else:
                status = "GRID_FEED"
                routing = f"Storage at Capacity. Feeding {surplus:.2f} MW to Grid."
        else:
            status = "DISCHARGING_STORAGE"
            routing = f"Drawing {abs(surplus):.2f} MW from reserves."
        
        return status, routing

if __name__ == "__main__":
    engine = EnerOSEngine()
    
    history_demand = [120, 135, 150, 145, 160, 180, 200, 210, 205, 190]
    
    predicted = engine.predict_demand(history_demand)
    
    current_prod = 250.0  
    current_soc = 45.0    
    
    status, action = engine.orchestrate(current_prod, predicted, current_soc)
    
    print(f"\n--- EnerOS Real-Time Decision ---")
    print(f"Predicted Demand: {predicted:.2f} MW")
    print(f"Current Production: {current_prod:.2f} MW")
    print(f"System Status: {status}")
    print(f"Action: {action}")
