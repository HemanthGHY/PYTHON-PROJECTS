import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  

y = np.array([0, 0, 0, 1])

weights = np.zeros(2)

bias = 0

learning_rate = 0.1

epochs = 20

def activation_function(x):
    return 1 if x >= 0 else 0

def predict(inputs):
    weighted_sum = np.dot(inputs, weights) + bias
    return activation_function(weighted_sum)

for epoch in range(epochs):
    for i in range(len(X)):
        prediction = predict(X[i])
        error = y[i] - prediction
        weights += learning_rate * error * X[i]
        bias += learning_rate * error    
    print(f"Epoch {epoch + 1}/{epochs} - Weights: {weights}, Bias: {bias}")
    
print("\nFinal Weights:", weights)
print("Final Bias:", bias)
print(
        f"Epoch {epoch+1}: "
        f"Weights={weights}, "
        f"Bias={bias}"
    )

print("\nPredictions:")

for sample in X:
    print(f"Input: {sample}, Predicted Output: {predict(sample)}")
    
    