import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

# Curve
x = np.linspace(0.5, 2.4, 1000)

# Points P and Q
x0, x1 = 1.0, 1.8
y0, y1 = f(x0), f(x1)

# Secant slope
m = (y1 - y0) / (x1 - x0)

# Secant line
secant = y0 + m * (x - x0)

plt.figure(figsize=(8, 6))

# Function
plt.plot(x, f(x), label="f(x)")

# Secant
plt.plot(x, secant, linestyle="--", label="secant PQ")

# Points
plt.scatter([x0, x1], [y0, y1])

plt.text(x0 - 0.08, y0 + 0.12, "P", fontsize=13)
plt.text(x1 + 0.04, y1 + 0.05, "Q", fontsize=13)

# Delta x: horizontal line
plt.plot(
    [x0, x1],
    [y0, y0],
    linestyle=":",
)

plt.text(
    (x0 + x1) / 2,
    y0 - 0.18,
    r"$\Delta x$",
    ha="center",
    fontsize=13
)

# Delta f: vertical line
plt.plot(
    [x1, x1],
    [y0, y1],
    linestyle=":",
)

plt.text(
    x1 + 0.07,
    (y0 + y1) / 2,
    r"$\Delta f$",
    va="center",
    fontsize=13
)

# x0 marker
plt.axvline(x0, linestyle=":", alpha=0.5)
plt.text(x0, -0.15, r"$x_0$", ha="center", fontsize=13)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(alpha=0.25)
plt.legend()

plt.savefig(
    "../assets/secant-line-change-in-x-and-f.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()