# Χρήση ελαφριάς έκδοσης Python [cite: 58]
FROM python:3.9-slim

# Φάκελος εργασίας
WORKDIR /app

# Αντιγραφή αρχείων
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY eneros_engine.py .

# Εκτέλεση του demo
CMD ["python", "eneros_engine.py"]
