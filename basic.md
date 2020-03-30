## Mathematical Tools

### Vector Calculus

In Cartesian coordinates, the **gradient** of a scalar function is given by
$$
\nabla f(x,y,z)=\frac{\partial f}{\partial x}\hat{\textbf{x}}+\frac{\partial f}{\partial y}\hat{\textbf{y}}+\frac{\partial f}{\partial z}\hat{\textbf{z}}
$$
the **divergence**, which applies to vector functions, is given by
$$
\nabla \cdot \textbf{E}=\frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}
$$
and the **curl**, which also applies to vector functions, is given by
$$
\begin{aligned}\nabla \times E&=\left|\begin{matrix}\hat{\textbf{x}} & \hat{\textbf{y}} & \hat{\textbf{z}} \\\\ \partial/\partial x & \partial/\partial y & \partial/\partial z \\\\ E_x & E_y & E_z\end{matrix}\right| \\\\ &=\left(\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}\right)\hat{\textbf{x}}-\left(\frac{\partial E_z}{\partial x}-\frac{\partial E_x}{\partial z}\right)\hat{\textbf{y}}+\left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right)\hat{\textbf{z}}\end{aligned}
$$
We will sometimes need a multidimensional second derivative called the **Laplacian**. When applied to a scalar function, it is defined as the divergence of a gradient:
$$
\begin{aligned}\nabla^2f(x,y,z)&\equiv\nabla\cdot \left[\nabla f(x,y,z)\right] \\\\ &=\frac{\partial^2f}{\partial x^2}+\frac{\partial^2f}{\partial y^2}+\frac{\partial^2f}{\partial z^2}\end{aligned}
$$
The Laplacian applied to a scalar gives a result that is also a scalar. In Cartesian coordinates, we deal with vector functions by applying the Laplacian to the scalar function attached to each unit vector:
$$
\begin{aligned}\nabla^2\bold E &\equiv \nabla(\nabla\cdot \bold E)-\nabla\times(\nabla\times \bold E)\\\\&=\left(\frac{\partial^2E_x}{\partial x^2}+\frac{\partial^2E_x}{\partial y^2}+\frac{\partial^2E_x}{\partial z^2} \right)\hat{\textbf{x}}+\left(\frac{\partial^2E_y}{\partial x^2}+\frac{\partial^2E_y}{\partial y^2}+\frac{\partial^2E_y}{\partial z^2} \right)\hat{\textbf{y}}+\left(\frac{\partial^2E_z}{\partial x^2}+\frac{\partial^2E_z}{\partial y^2}+\frac{\partial^2E_z}{\partial z^2} \right)\hat{\textbf{z}}\end{aligned}
$$
The **divergence theorem** for a vector function F is
$$
\oint\limits_S\bold F\cdot\hat{\bold n}\ \mathrm{d}a=\int\limits_V\nabla\cdot\bold F\mathrm{d}v
$$
The integration on the left-hand side is over the closed surface $S$, which contains the volume $V$ associated with the integration on the right-hand side. The unit vector n̂ points outward, normal to the surface.

Another important theorem is **Stokes’ theorem**:
$$
\int\limits_S(\nabla\times \bold F)\cdot\hat{\bold n}\ \mathrm{d}a=\oint\limits_C\bold F\cdot\mathrm{d}\boldsymbol{\ell}
$$
The integration on the left-hand side is over an open surface $S$ (not enclosing a volume). The integration on the right-hand side is around the edge of the surface. Again, $\hat n$ is a unit vector that always points normal to the surface. The vector $\mathrm{d}\boldsymbol{\ell}$ points along the curve $C$ that bounds the surface $S$. If the fingers of your right
hand point in the direction of integration around $C$ , then your thumb points in the direction of $\hat{n}$.

### Complex Numbers

**Euler's formula**:
$$
e^{i\phi}=\cos\phi+i\sin\phi
$$
We will often be interested in waves of the form $A\cos(\alpha+\beta)$. We can use complex notation to represent this wave simply by writing  
$$
A\cos(\alpha+\beta)=Re\left\{\tilde A e^{i\alpha}\right\}
$$
where the 'phase' $\beta$ is conveniently contained within the complex factor $\tilde A\equiv Ae^{i\beta}$. The operation $Re\{\}$ means to retain only the real part of the argument without regard for the imaginary part. It is common (even conventional) to omit the explicit writing of $Re\{\}$.

The transformation between a Cartesian representation and a polar representation:
$$
\rho e^{i\phi}=a+ib \\\\ 
a=\rho\cos\phi\\\\
b=\rho\sin\phi
$$
These equations can be inverted to yield
$$
\begin{aligned}\rho &=\sqrt{a^2+b^2}\\\\
\phi&=\tan^{-1}\frac{b}{a}\qquad(a>0)\end{aligned}
$$
When $a<0$, we must adjust $\phi$ by $\pi$ since the arctangent has a range only from $-\pi/2$ to $\pi/2$.

<img src="complex plane representation.png" alt="A number in the complex plane can be represented either by Cartesian or polar representation." style="zoom:50%;" />

The conjugate of a complex number $z=a+bi$ is denoted with an asterisk and amounts to changing the sign on the imaginary part of the number:  
$$
z^*=(a+ib)^*=a-ib
$$
No matter how complicated an expression, the complex conjugate is calculated by inserting a minus sign in front of all occurrences of $i$ in the expression, and placing an asterisk on all complex variables in the expression.   

### Linear Algebra

The inverse of a $2\times 2$ matrix is given by
$$
\left[\matrix{A &B\\\\C&D} \right]^{-1}=\frac{1}{\left|\matrix{A&B\\\\C&D}\right|}\left[\matrix{D &-B\\\\-C&A}\right]
$$
**Sylvester's Theorem**: If the determinant of a 2£2 matrix is one, (i.e. $AD-BC=1$) then  
$$
\left[\matrix{A&B\\\\C&D}\right]^N=\frac{1}{\sin\theta}\left[\matrix{A\sin N\theta-\sin(N-1)\theta&B\sin N\theta\\\\C\sin N\theta&D\sin N\theta-\sin(N-1)\theta}\right]
$$
where
$$
\cos\theta=\frac{1}{2}(A+D)
$$

### Fourier Theory

The **Fourier integral theorem**:
$$
f(t)=\frac{1}{\sqrt{2\pi}}\int^\infin_{-\infin}e^{-iwt}\left[\frac{1}{\sqrt{2\pi}}\int^\infin_{-\infin}f(t^\prime)e^{iwt^\prime}\mathrm{d}t^\prime\right]\mathrm{d}w
$$
The piece in brackets is called the Fourier transform, and the rest of the operation is called the inverse Fourier transform. The Fourier integral theorem is often written with the following notation:  
$$
f(w)\equiv\frac{1}{\sqrt {2\pi}}\int^\infty_{-\infty}f(t)e^{iwt}\mathrm{d}t\\\\
f(t)\equiv\frac{1}{\sqrt {2\pi}}\int^\infty_{-\infty}f(w)e^{-iwt}\mathrm{d}w
$$
The transform and inverse transform are also sometimes written as  $f(w)\equiv\mathcal{F}\{f(t)\}$ and  $f(t)\equiv\mathcal{F}^{-1}\{f(w)\}$.

The real part of $f(w)$ indicates the amplitudes of the cosine waves necessary to construct the function $f(t)$. The imaginary part of $f(w)$ indicates the amplitudes of the sine waves necessary to construct the function $f(t)$.  

The **Dirac delta function** is defined indirectly through:
$$
f(t)=\int^\infin_{-\infin}f(t^{\prime})\delta(t^\prime-t)\mathrm{d}t^\prime
$$
The delta function $\delta(t^\prime-t)$ is zero everywhere except at $t^\prime=t$ where it is infinite in such a way as to make the integral take on the value of the function f (t).  The integral only pays attention to the value of $f(t^\prime)$ at the point of $t^\prime=t$.

You may write the delta function as a uniform superposition of all frequency components:  
$$
\delta(t^\prime-t)=\frac{1}{2\pi}\int^\infin_{-\infin}e^{iw(t^\prime-t)}\mathrm{d}w
$$
