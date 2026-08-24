import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

# Function
x = np.linspace(-0.5, 3, 400)

# Fixed point P
x0 = 1
y0 = f(x0)

# Different positions of Q
q_values = [2.5, 2.0, 1.5, 1.2]

# Curve f(x)
plt.plot(x, f(x), label="f(x) = x²")

# Point P
plt.scatter(x0, y0)
plt.text(x0 - 0.15, y0 - 0.4, "P")

# Draw every Q and its secant line
for i, x1 in enumerate(q_values):
    y1 = f(x1)

    # Draw Q
    plt.scatter(x1, y1)
    plt.text(x1 + 0.05, y1, f"Q{i + 1}")

    # Slope between P and Q
    m = (y1 - y0) / (x1 - x0)

    # Secant line through P and Q
    secant = y0 + m * (x - x0)

    plt.plot(x, secant, label=f"PQ{i + 1}, slope={m:.2f}")

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig(
    "../assets/derivative-secant-lines.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()