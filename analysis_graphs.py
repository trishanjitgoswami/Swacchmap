import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-whitegrid")

# -----------------------------
# GRAPH 1: Response Efficiency vs Severity
# -----------------------------

severity_levels = ["Low", "Medium", "High"]
response_time = [12, 8, 4]  # Hours taken to respond
resolution_rate = [75, 85, 95]  # Percentage resolved

plt.figure(figsize=(8,5))
plt.plot(severity_levels, response_time, marker="o", label="Avg Response Time (Hours)")
plt.plot(severity_levels, resolution_rate, marker="s", label="Resolution Rate (%)")

plt.title("Response Efficiency vs Waste Severity")
plt.xlabel("Waste Severity Level")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.show()


# -----------------------------
# GRAPH 2: Area-wise Waste Trend
# -----------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
area_A = [20, 25, 30, 28, 35]
area_B = [15, 18, 22, 20, 24]

plt.figure(figsize=(8,5))
plt.plot(months, area_A, marker="o", label="Area A Reports")
plt.plot(months, area_B, marker="o", label="Area B Reports")

plt.title("Monthly Waste Reports by Area")
plt.xlabel("Month")
plt.ylabel("Number of Reports")
plt.legend()
plt.tight_layout()
plt.show()


# -----------------------------
# GRAPH 3: Waste Growth Simulation
# -----------------------------

temperature_increase = np.arange(0, 6, 1)
waste_growth = [10, 15, 22, 30, 40, 55]

plt.figure(figsize=(8,5))
plt.plot(temperature_increase, waste_growth, marker="o")

plt.title("Projected Waste Increase with Urban Growth")
plt.xlabel("Urban Growth Index")
plt.ylabel("Waste Accumulation (%)")
plt.tight_layout()
plt.show()