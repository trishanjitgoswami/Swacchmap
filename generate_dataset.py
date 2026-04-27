import pandas as pd
import random

data = []

area_types = ["Residential", "Market", "Slum", "Park"]
severities = ["Low", "Medium", "High"]

for i in range(300):   # <-- Change number here
    waste_percentage = random.randint(5, 90)
    garbage_density = round(random.uniform(0.1, 1.0), 2)
    area_type = random.choice(area_types)

    # Simple rule-based severity
    if waste_percentage < 25:
        severity = "Low"
    elif waste_percentage < 50:
        severity = "Medium"
    else:
        severity = "High"

    data.append([waste_percentage, garbage_density, area_type, severity])

df = pd.DataFrame(data, columns=["waste_percentage", "garbage_density", "area_type", "severity"])
df.to_csv("waste_dataset.csv", index=False)

print("Dataset created successfully with 300 rows.")