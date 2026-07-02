# Perceptron from Scratch using NumPy (AND Gate)

A simple implementation of the **Perceptron Learning Algorithm** using **Python** and **NumPy**. This project demonstrates how a single-layer perceptron learns the logical **AND** operation by updating weights and bias through supervised learning.

---

## 📌 Project Overview

The Perceptron is one of the earliest neural network models and serves as the foundation of modern deep learning.

This project includes:

- Perceptron implementation from scratch
- Binary step activation function
- Weight and bias updates using the Perceptron Learning Rule
- Training over multiple epochs
- Prediction on unseen inputs
- Console output showing learning progress

---

## 📂 Dataset

The model is trained on the truth table of the **AND** logical gate.

| Input 1 | Input 2 | Output |
|---------|---------|--------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

```python
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0,0,0,1])
```

---

## 🧠 How the Perceptron Works

For every training sample:

1. Calculate the weighted sum

```
z = w₁x₁ + w₂x₂ + b
```

2. Apply the activation function

```
Output = 1 if z >= 0 else 0
```

3. Compute error

```
Error = Actual Output − Predicted Output
```

4. Update weights

```
w = w + learning_rate × error × input
```

5. Update bias

```
b = b + learning_rate × error
```

This process repeats for all epochs until the perceptron correctly classifies every training sample.

---

## ⚙️ Hyperparameters

| Parameter | Value |
|-----------|-------|
| Learning Rate | 0.1 |
| Epochs | 20 |
| Initial Weights | [0, 0] |
| Initial Bias | 0 |
| Activation Function | Binary Step |

---

## 📈 Training Output

During training, the model prints:

- Current epoch
- Updated weights
- Updated bias

Example:

```
Epoch 1/20 - Weights: [0.1 0.1], Bias: -0.1
```

---

## ✅ Final Predictions

After training:

```
Input: [0 0] -> Predicted: 0
Input: [0 1] -> Predicted: 0
Input: [1 0] -> Predicted: 0
Input: [1 1] -> Predicted: 1
```

The perceptron successfully learns the AND gate.

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/HemanthGHY/perceptron.git
```

### Navigate into the project

```bash
cd perceptron-and-gate
```

### Install NumPy

```bash
pip install numpy
```

### Run

```bash
python perceptron.py
```

---

## 📁 Project Structure

```
perceptron-and-gate/
│
├── perceptron.py
├── README.md
└── requirements.txt
```

---

## 📚 Concepts Covered

- Artificial Neuron
- Perceptron
- Supervised Learning
- Binary Classification
- Linear Decision Boundary
- Weight Initialization
- Learning Rate
- Epochs
- Bias
- Dot Product
- NumPy Arrays

---

## ⚠️ Limitations

A single-layer perceptron can only solve **linearly separable** problems.

It works for:

- AND
- OR

It cannot solve:

- XOR
- XNOR

Those require **Multi-Layer Perceptrons (MLPs)** with hidden layers.

---

## 🎯 Learning Outcome

After completing this project, you will understand:

- How a perceptron learns from data
- How weights and bias are updated
- How predictions are made
- Why activation functions are needed
- Why single-layer perceptrons fail on XOR problems
- The foundation of modern neural networks

---

## 🛠️ Technologies Used

- Python 3
- NumPy

---

## 📖 Future Improvements

- Implement OR Gate
- Implement XOR using Multi-Layer Perceptron
- Visualize the decision boundary
- Add plotting with Matplotlib
- Train on custom datasets
- Compare Perceptron with Logistic Regression

---

## 📄 License

This project is intended for educational purposes and is open for learning and experimentation.