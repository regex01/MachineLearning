# FILEPATH: Untitled-1

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Step 1: Import necessary libraries
iris = load_iris()

X = iris.data
y = iris.target


# Step 2: Prepare the data
# Assuming you have your features stored in X and target variable in y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create an instance of the linear regression model
model = LinearRegression()

# Step 4: Fit the model to the training data
model.fit(X_train, y_train)

# Step 5: Predict the target variable using the testing data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step 7: Visualize the results (optional)
# You can plot the actual vs predicted values or any other relevant plots
