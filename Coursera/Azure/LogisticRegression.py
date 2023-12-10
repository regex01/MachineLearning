import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression(X, y, num_iterations, learning_rate):
    m, n = X.shape
    theta = np.zeros(n)
    
    for i in range(num_iterations):
        z = np.dot(X, theta)
        h = sigmoid(z)
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient
    
    return theta

# Example usage
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 0, 1])
num_iterations = 1000
learning_rate = 0.01

theta = logistic_regression(X, y, num_iterations, learning_rate)
print("Theta:", theta)
        