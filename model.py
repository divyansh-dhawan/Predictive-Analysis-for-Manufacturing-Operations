import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
file_path = "synthetic_machine_data.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Encode categorical column (Machine_ID)
label_encoder = LabelEncoder()
data["Machine_ID"] = label_encoder.fit_transform(data["Machine_ID"])

# Define features (X) and target (y)
X = data[["Machine_ID", "Temperature", "Run_Time"]]
y = data["Downtime_Flag"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(accuracy, classification_rep, conf_matrix)

joblib.dump(model, "logistic_regression_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")
