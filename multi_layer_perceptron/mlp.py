import numpy as np

# ==========================
# XOR Dataset
# ==========================
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# ==========================
# Network Configuration
# ==========================
np.random.seed(42)

input_size = 2
hidden_size = 4
output_size = 1

learning_rate = 0.1
epochs = 10000

# ==========================
# Weight Initialization
# ==========================
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))

# ==========================
# Activation Functions
# ==========================
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)

# ==========================
# Training Loop
# ==========================
for epoch in range(epochs):

    # Forward Propagation
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    # Loss (Mean Squared Error)
    loss = np.mean((y - A2) ** 2)

    # Backpropagation
    dZ2 = (A2 - y) * sigmoid_derivative(Z2)
    dW2 = np.dot(A1.T, dZ2)
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * relu_derivative(Z1)

    dW1 = np.dot(X.T, dZ1)
    db1 = np.sum(dZ1, axis=0, keepdims=True)

    # Gradient Descent
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    if epoch % 1000 == 0:
        print(f"Epoch {epoch:5d} | Loss: {loss:.6f}")

# ==========================
# Testing
# ==========================
print("\nFinal Predictions:")
predictions = sigmoid(np.dot(relu(np.dot(X, W1) + b1), W2) + b2)

print(predictions)

print("\nRounded Predictions:")
print(np.round(predictions))

print("\nExpected Output:")
print(y)

print("\nFinal Weights and Biases:")
print("W1 =")
print(W1)

print("\nb1 =")
print(b1)

print("\nW2 =")
print(W2)

print("\nb2 =")
print(b2)
