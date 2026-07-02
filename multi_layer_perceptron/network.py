import numpy as np

from activations import (
    relu,
    relu_derivative,
    sigmoid,
    sigmoid_derivative
)


class MLP:

    def __init__(
        self,
        input_size=2,
        hidden_size=4,
        output_size=1,
        learning_rate=0.1
    ):

        np.random.seed(42)

        self.learning_rate = learning_rate

        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))

        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))

    def forward(self, X):

        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = relu(self.Z1)

        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = sigmoid(self.Z2)

        return self.A2

    def compute_loss(self, y):

        return np.mean((y - self.A2) ** 2)

    def backward(self, X, y):

        dZ2 = (self.A2 - y) * sigmoid_derivative(self.Z2)

        dW2 = np.dot(self.A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        dA1 = np.dot(dZ2, self.W2.T)

        dZ1 = dA1 * relu_derivative(self.Z1)

        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1

        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2

    def predict(self, X):

        predictions = self.forward(X)

        return np.round(predictions)