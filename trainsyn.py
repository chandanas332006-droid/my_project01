import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pickle

# Load updated dataset
df = pd.read_csv("updated_data.csv")

# Create risk label
def get_risk(row):
    if row["hours_since_meal"] > 5 and (row["dizziness"] == 1 or row["sweating"] == 1) and row["pulse"] > 95:
        return "HIGH"
    elif row["hours_since_meal"] > 3 and (row["dizziness"] == 1 or row["sweating"] == 1):
        return "MEDIUM"
    else:
        return "LOW"

df["risk"] = df.apply(get_risk, axis=1)

# Features and target
X = df.drop("risk", axis=1)
y = df["risk"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")