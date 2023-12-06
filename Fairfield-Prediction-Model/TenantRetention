
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load your data
data = pd.read_csv('tenant_data.csv')

# Preprocess your data (encoding, normalization, etc.)

# Split data into features and target
X = data.drop('Churn', axis=1)  # Assuming 'Churn' is your target variable
y = data['Churn']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, predictions))
print("Accuracy:", accuracy_score(y_test, predictions))

# Hyperparameter tuning (optional)
param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [5, 10, 15]}
grid_search = GridSearchCV(model, param_grid, cv=3)
grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_

# Re-evaluate the best model
best_predictions = best_model.predict(X_test)
print("Best Model Accuracy:", accuracy_score(y_test, best_predictions))

# Save the model


