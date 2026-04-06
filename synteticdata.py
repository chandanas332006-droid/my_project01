import pandas as pd
import numpy as np

# Load dataset FIRST
df = pd.read_csv(r"C:\Users\Chandana S\Favorites\Downloads\archive (1)\diabetes.csv")

# Now add synthetic features
df["pulse"] = np.random.randint(60, 120, size=len(df))
df["blink_rate"] = np.random.randint(10, 30, size=len(df))
df["hours_since_meal"] = np.random.randint(1, 8, size=len(df))
df["sweating"] = np.random.randint(0, 2, size=len(df))
df["dizziness"] = np.random.randint(0, 2, size=len(df))

# Save new dataset
df.to_csv("updated_data.csv", index=False)

print("Synthetic data added successfully")