from dataset import X, y
from network import MLP


model = MLP(
    input_size=2,
    hidden_size=4,
    output_size=1,
    learning_rate=0.1
)

epochs = 10000

for epoch in range(epochs):

    predictions = model.forward(X)

    loss = model.compute_loss(y)

    model.backward(X, y)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch:5d} | Loss = {loss:.6f}")


print("\n========================")
print("Training Completed")
print("========================")

print("\nRaw Predictions")

print(model.forward(X))

print("\nRounded Predictions")

print(model.predict(X))

print("\nExpected")

print(y)

print("\nFinal Weights")

print(model.W1)
print(model.W2)

print("\nFinal Biases")

print(model.b1)
print(model.b2) 