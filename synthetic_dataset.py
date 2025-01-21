import pandas as pd
import random
import numpy as np

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Parameters for dataset
num_records = 1000
num_machines = 20

# Generate Machine_IDs
machine_ids = [f"M{str(i).zfill(3)}" for i in range(1, num_machines + 1)]

# Function to simulate temperature based on real-world machine conditions
def generate_temperature():
    return round(random.uniform(20.0, 100.0), 1)  # Range between 20°C and 100°C

# Function to simulate run time based on typical operating conditions
def generate_run_time():
    return round(random.uniform(0.5, 24.0), 2)  # Between 0.5 and 24 hours

# Function to simulate downtime flag (1 if downtime occurs, 0 otherwise)
def generate_downtime_flag(temperature, runtime):
    # Probability of downtime increases with higher temperature and runtime
    if temperature > 80 or runtime > 20:
        return np.random.choice([0, 1], p=[0.3, 0.7])
    return np.random.choice([0, 1], p=[0.9, 0.1])

# Generate dataset
data = []
for _ in range(num_records):
    machine_id = random.choice(machine_ids)
    temperature = generate_temperature()
    run_time = generate_run_time()
    downtime_flag = generate_downtime_flag(temperature, run_time)
    data.append([machine_id, temperature, run_time, downtime_flag])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"])

# Save the dataset to a CSV file
df.to_csv("synthetic_machine_data.csv", index=False)

print("Synthetic dataset generated and saved as 'synthetic_machine_data.csv'.")
