# 18.01 Problem-solving | Introduction to derivatives

## Secants and Tangents

For $f(x)=\frac{1}{2}x^3-x$, the slope of a secant line through

> $P=(x,f(x))$
>
> $Q=(x+\Delta x,f(x+\Delta x))$

is

> $\boxed{m_{\text{sec}}=\frac{\Delta y}{\Delta x}=\frac{f(x+\Delta x)-f(x)}{\Delta x}}$

### Example: $x=-0.75$

For $x=-0.75$, changing $\Delta x$ gives different slopes of the secant line.

> $\Delta x=-0.50 \Rightarrow \frac{\Delta y}{\Delta x}\approx0.53$
>
> $\Delta x=-0.25 \Rightarrow \frac{\Delta y}{\Delta x}\approx0.16$
>
> $\Delta x=0.01 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.17$
>
> $\Delta x=0.25 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.41$
>
> $\Delta x=0.50 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.59$

The tangent slope at $x=-0.75$ is approximately

$\boxed{m_{\text{tan}}\approx-0.16}$

For example, when $\Delta x=0.01$, the secant slope is approximately $-0.17$, which is already very close to the tangent slope $-0.15625$.

### Key idea

As the second point $Q$ approaches the fixed point $P$, we have

$\Delta x\to0$

and the secant line approaches the tangent line.

Therefore,

$\frac{\Delta y}{\Delta x}\to f'(x)$

and

$\boxed{f'(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}}$

We cannot simply set $\Delta x=0$, because then

$\frac{\Delta y}{\Delta x}=\frac{0}{0}$

which is undefined.

#### The important distinction is

> $\Delta x=0$ is not allowed because the secant slope becomes $\frac{0}{0}$.
>
> $\Delta x\to0$ means that $\Delta x$ gets arbitrarily close to $0$ without being equal to $0$.

#### Therefore

$\boxed{\text{Secant line} \to \text{Tangent line as } \Delta x\to0}$

and

$\boxed{\text{Secant slope} \to \text{Derivative}}$

The derivative is determined by the **limit**, not by the value of the fraction at $\Delta x=0$.

### Problem 2

#### Let $x=0$

For $f(x)=\frac{1}{2}x^3-x$:

> $\Delta x=-0.50 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.88$
>
> $\Delta x=-0.25 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.97$
>
> $\Delta x=0.25 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.97$
>
> $\Delta x=0.50 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.88$

The slope of the tangent line at $x=0$ is

$\boxed{m_{\text{tan}}=-1}$

As $\Delta x\to0$, the secant slope approaches $-1$.

$\boxed{\frac{\Delta y}{\Delta x}\to-1}$

#### Find $\Delta x$ for which the secant slope is within $0.1$ of the tangent slope

At $x=0$:

$\frac{\Delta y}{\Delta x}=\frac{f(\Delta x)-f(0)}{\Delta x}$

$\frac{\Delta y}{\Delta x}=\frac{\frac{1}{2}(\Delta x)^3-\Delta x}{\Delta x}$

$\frac{\Delta y}{\Delta x}=\frac{1}{2}(\Delta x)^2-1$

The tangent slope is $-1$, so we need

$\left|\left(\frac{1}{2}(\Delta x)^2-1\right)-(-1)\right|<0.1$

$\frac{1}{2}(\Delta x)^2<0.1$

$(\Delta x)^2<0.2$

$\boxed{|\Delta x|<\sqrt{0.2}\approx0.4472}$

Therefore, for example,

$\boxed{\Delta x=0.4}$

works because

$\frac{\Delta y}{\Delta x}=\frac{1}{2}(0.4)^2-1=-0.92$

and

$|-0.92-(-1)|=0.08<0.1$

Experimentally, values around $|\Delta x|=0.46$ already differ from the tangent slope by more than $0.1$.

### Problem 3

#### Let $x=0.75$

For $f(x)=\frac{1}{2}x^3-x$:

> $\Delta x=-0.50 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.59$
>
> $\Delta x=-0.25 \Rightarrow \frac{\Delta y}{\Delta x}\approx-0.41$
>
> $\Delta x=0.25 \Rightarrow \frac{\Delta y}{\Delta x}\approx0.16$
>
> $\Delta x=0.50 \Rightarrow \frac{\Delta y}{\Delta x}\approx0.53$

The slope of the tangent line at $x=0.75$ is approximately

$\boxed{m_{\text{tan}}\approx-0.16}$

More precisely,

$f'(x)=\frac{3}{2}x^2-1$

so

$f'(0.75)=\frac{3}{2}(0.75)^2-1=-0.15625$

Therefore,

$\boxed{f'(0.75)=-0.15625}$

As $\Delta x\to0$, the secant slope approaches the tangent slope.

$\boxed{\frac{\Delta y}{\Delta x}\to-0.15625}$

#### Find $\Delta x$ for which the secant slope is within $0.1$ of the tangent slope

For $f(x)=\frac{1}{2}x^3-x$, the secant slope can be written as

$\frac{\Delta y}{\Delta x}=\frac{3}{2}x^2-1+\frac{3}{2}x\Delta x+\frac{1}{2}(\Delta x)^2$

At $x=0.75$:

$\frac{\Delta y}{\Delta x}=-0.15625+1.125\Delta x+\frac{1}{2}(\Delta x)^2$

The difference between the secant slope and the tangent slope is therefore

$\left|1.125\Delta x+\frac{1}{2}(\Delta x)^2\right|$

We need

$\left|1.125\Delta x+\frac{1}{2}(\Delta x)^2\right|<0.1$

A simple value that works is

$\boxed{\Delta x=0.05}$

because

$\frac{\Delta y}{\Delta x}=-0.15625+1.125(0.05)+\frac{1}{2}(0.05)^2$

$\frac{\Delta y}{\Delta x}=-0.09875$

and

$|-0.09875-(-0.15625)|=0.0575<0.1$

#### Observation

At $x=0$, relatively large values of $|\Delta x|$ still gave a good approximation of the tangent slope.

At $x=0.75$, $|\Delta x|$ must be much smaller for the secant slope to be close to the tangent slope.

This happens because the slope of the graph changes faster around $x=0.75$.

$\boxed{\text{As }Q\to P,\text{ the secant slope approaches the tangent slope}}$

### Problem 4

#### Compare the answers to the previous problems

### (a) Was the answer to part (c) the same for each problem?

No.

The required value of $\Delta x$ was different for different values of $x$.

At some points, a relatively large value of $|\Delta x|$ was enough for the secant slope to be close to the tangent slope.

At other points, $|\Delta x|$ had to be much smaller.

$\boxed{\text{The required }|\Delta x|\text{ depends on the local shape of the graph}}$

### (b) When do we need a very small value of $\Delta x$?

The secant slope is

$\frac{\Delta y}{\Delta x}$

and it approximates the slope of the tangent line when $\Delta x$ is close to $0$.

From the previous problems, we observed that when the graph is almost straight near the point $P$, even a relatively large $\Delta x$ can give a good approximation.

When the graph bends more strongly and its slope changes faster, the second point $Q$ must be taken closer to $P$.

Therefore, a smaller $|\Delta x|$ is required.

$\boxed{\text{The faster the slope changes, the smaller }|\Delta x|\text{ must be for a good approximation}}$

For example, around $x=0$, the graph of $f(x)=\frac{1}{2}x^3-x$ is locally closer to a straight line, so relatively large values of $\Delta x$ still approximate the tangent slope well.

Around $x=\pm0.75$, the slope changes faster, so a much smaller $\Delta x$ is needed.

#### Conjecture

$\boxed{\text{Greater local bending of the graph} \Rightarrow \text{smaller }|\Delta x|\text{ is needed}}$

This behavior is related to the second derivative, because $f''(x)$ describes how quickly the slope $f'(x)$ changes as $x$ changes.
