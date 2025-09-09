import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def prelu(x, alpha=0.25): # Using a fixed alpha for visualization
    return np.where(x > 0, x, alpha * x)

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def selu(x):
    # Constants for SELU (from original paper)
    alpha = 1.6732632423543772848170429916717
    scale = 1.0507009873554804934193349852946
    return scale * np.where(x > 0, x, alpha * (np.exp(x) - 1))

def swish(x):
    return x * sigmoid(x)

def gelu(x):
    # Approximation from original paper
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * x**3)))

# Generate input values
x = np.linspace(-5, 5, 1000)

# Create plots
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
axes = axes.flatten() # Flatten the 2x2 array of axes for easy iteration

functions = [
    (sigmoid, "Sigmoid"),
    (tanh, "Tanh"),
    (relu, "ReLU"),
    (leaky_relu, "Leaky ReLU (alpha=0.01)"),
    (prelu, "PReLU (alpha=0.25)"),
    (elu, "ELU (alpha=1.0)"),
    (selu, "SELU"),
    (swish, "Swish"),
    (gelu, "GELU")
]

for i, (func, name) in enumerate(functions):
    ax = axes[i]
    ax.plot(x, func(x), label=name, color=plt.cm.viridis(i / len(functions)))
    ax.set_title(name)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)

plt.tight_layout()
plt.suptitle("Common Neural Network Activation Functions", y=1.02, fontsize=18)
plt.savefig("activation_functions.png")
plt.show()
