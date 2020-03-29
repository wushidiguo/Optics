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
The integration on the left-hand side is over an open surface $S$ (not enclosing a volume). The integration on the right-hand side is around the edge of the surface. Again, $\hat n$ is a unit vector that always points normal to the surface. The vector $\mathrm{d}\boldsymbol{\ell}$ points along the curve $C$ that bounds the surface $S$.