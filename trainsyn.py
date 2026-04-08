import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    recall_score,
    confusion_matrix
)

# =========================
# 1. LOAD SYNTHETIC DATA
# =========================
# Make sure updated_data.csv is in the same folder as this Python file
df = pd.read_csv("updated_data.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nColumns in dataset:")
print(df.columns)

# =========================
# 2. CREATE RISK LABEL
# =========================
def get_risk(row):
    if (
        row["hours_since_meal"] > 5
        and (row["dizziness"] == 1 or row["sweating"] == 1)
        and row["pulse"] > 95
    ):
        return "HIGH"
    elif (
        row["hours_since_meal"] > 3
        and (row["dizziness"] == 1 or row["sweating"] == 1)
    ):
        return "MEDIUM"
    else:
        return "LOW"

df["risk"] = df.apply(get_risk, axis=1)

print("\nRisk label distribution:")
print(df["risk"].value_counts())

# =========================
# 3. FEATURES AND TARGET
# =========================
X = df.drop("risk", axis=1)
y = df["risk"]

# =========================
# 4. TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# =========================
# 5. TRAIN MODEL
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# =========================
# 6. PREDICT
# =========================
y_pred = model.predict(X_test)

# =========================
# 7. EVALUATION
# =========================
print("\n========== MODEL EVALUATION ==========")

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Recall Macro
recall_macro = recall_score(y_test, y_pred, average="macro")
print("Recall (Macro):", recall_macro)

# Recall Weighted
recall_weighted = recall_score(y_test, y_pred, average="weighted")
print("Recall (Weighted):", recall_weighted)

# Recall Per Class
recall_per_class = recall_score(y_test, y_pred, average=None, labels=model.classes_)
print("\nRecall Per Class:")
for class_name, score in zip(model.classes_, recall_per_class):
    print(f"{class_name}: {score:.4f}")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# =========================
# 8. CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

print("Confusion Matrix:")
print(cm)

plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=model.classes_,
    yticklabels=model.classes_
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()

# =========================
# 9. FEATURE IMPORTANCE
# =========================
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)

plt.figure(figsize=(8, 5))
sns.barplot(data=feature_importance, x="Importance", y="Feature")
plt.title("Feature Importance")
plt.tight_layout()
plt.show()

# =========================
# 10. SAVE MODEL
# =========================
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved as model.pkl")