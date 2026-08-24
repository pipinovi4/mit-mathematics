import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 / x

# Point where tangent touches the curve
x0 = 2
y0 = f(x0)

# Derivative of 1/x
m = -1 / x0**2

# x range
x = np.linspace(0.01, 5, 400)

# Tangent line:
# y - y0 = m(x - x0)
tangent = y0 + m * (x - x0)

plt.figure(figsize=(8, 6))

# Function
plt.plot(x, f(x), label=r"$f(x)=\frac{1}{x}$")

# Tangent
plt.plot(x, tangent, label="tangent")

# Point of tangency
plt.scatter(x0, y0)

plt.text(
    x0 + 0.08,
    y0 + 0.05,
    r"$P=(x_0,f(x_0))=(x_0, y_0)$"
)

# Axes
plt.axhline(0)
plt.axvline(0)

plt.xlim(0, 5)
plt.ylim(-0.3, 2.2)

plt.grid(alpha=0.2)
plt.legend()

plt.savefig(
    "../assets/reciprocal_function_tangent.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()