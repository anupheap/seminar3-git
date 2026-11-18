---
layout: lecture-six
lecture: 6
title: Column space and nullspace
routeAlias: lecture-6
section: true
class: l6-cover
---

<div class="l6-cover-rule" />
<div class="l6-cover-art"><LectureSixDiagram kind="columns" /></div>
<div class="l6-cover-copy">
<div class="l6-eyebrow">Lecture 6 · MIT 18.06</div>

# Column space<br>& nullspace

<p>Reachable outputs. Inputs that disappear.</p>
<p class="l6-small">Based on Gilbert Strang’s linear algebra lectures.</p>
</div>

<!-- Teaching source: MIT OCW, Gilbert Strang, Lecture 6: Column space and nullspace, https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/ . Worked matrix and lecture sequence from the lecture and its MIT 18.06SC summary. All prose here is newly written. Design reference: the supplied Semiconductors presentation; visual composition only. Palette: 3Blue1Brown/Manim colors. -->

---
layout: lecture-six
lecture: 6
title: The route through Lecture 6
---

<div class="l6-head"><div class="l6-eyebrow">The route through the lecture</div>

# Define, work, and verify

</div>
<div class="l6-roadmap">
<div><span>01</span><h2>Define the column space and nullspace</h2></div>
<div><span>02</span><h2>Work both spaces from the same matrix</h2></div>
<div><span>03</span><h2>Visualize them and verify the results in Python</h2></div>
</div>
<div class="l6-band">One matrix maps inputs in ℝ³ to outputs in ℝ⁴.</div>

---
layout: lecture-six
lecture: 6
title: Subspaces stay closed
clicks: 2
---

<div class="l6-head"><div class="l6-eyebrow">Start with geometry</div>

# Subspaces stay closed

</div>
<div class="l6-split wide-left"><div>
<LectureSixFilm />
</div><div class="l6-film-text">

A plane through the origin contains every linear combination of its vectors.

<div v-click="1"><span class="l6-gold">Add:</span> the new endpoint stays in the plane.</div>
<div v-click="2"><span class="l6-red">Scale by −2:</span> reverse direction and double the length.</div>

</div></div>
<div class="l6-band">Column space and nullspace both pass this closure test.</div>

---
layout: lecture-six
lecture: 6
title: Definitions of column space and nullspace
---

<div class="l6-head"><div class="l6-eyebrow">Definitions</div>

# Two spaces from one matrix

</div>
<p>Let A be an m × n matrix with columns a₁, …, aₙ.</p>
<div class="l6-pair l6-definition-pair">
<section><h2 class="l6-blue">Column space</h2>

$$C(A)=\operatorname{span}\{\mathbf a_1,\ldots,\mathbf a_n\}$$

$$C(A)=\{A\mathbf x:\mathbf x\in\mathbb R^n\}$$

<p>Every output reachable by choosing input weights x. It is a subspace of ℝᵐ.</p></section>
<section><h2 class="l6-yellow">Nullspace</h2>

$$N(A)=\{\mathbf x\in\mathbb R^n:A\mathbf x=\mathbf 0\}$$

<p>Every input whose columns cancel to zero. It is a subspace of ℝⁿ.</p></section>
</div>
<div class="l6-band">Column space answers “Which b can Ax = b reach?” Nullspace answers “Which x gives Ax = 0?”</div>

---
layout: lecture-six
lecture: 6
title: Inputs and outputs live in different spaces
clicks: 0
---

<div class="l6-head"><div class="l6-eyebrow">Map the definitions</div>

# Inputs and outputs live in different spaces

</div>
<div class="l6-split"><div>

$$A:\mathbb R^3\longrightarrow\mathbb R^4$$

<p><span class="l6-yellow">N(A)</span> is a line of input vectors in ℝ³ for our example. Each point on it maps to zero.</p>
<p><span class="l6-blue">C(A)</span> is a plane of output vectors inside ℝ⁴. These are the right-hand sides we can reach.</p>
<div class="l6-note">The drawing shows the map schematically. It does not project ℝ⁴ into literal 3D coordinates.</div>
</div><div><LectureSixDiagram kind="map" /></div></div>

---
layout: lecture-six
lecture: 6
title: Which outputs can A reach?
class: l6-question
---

<div class="l6-eyebrow">The column-space question</div>

# Which right-hand sides<br>can A reach?

<div class="l6-math-huge">

$$A\mathbf{x}=\mathbf{b}$$

</div>

<p>Choose the input weights. Look at the output they produce.</p>

---
layout: lecture-six
lecture: 6
title: Strang’s four-by-three matrix
---

<div class="l6-head"><div class="l6-eyebrow">The worked example from Strang’s lecture</div>

# Three columns in ℝ⁴

</div>
<div class="l6-split"><div class="l6-matrix">

$$
A=\begin{bmatrix}
\color{#58c4dd}1&\color{#83c167}1&\color{#f0ac5f}2\\
\color{#58c4dd}2&\color{#83c167}1&\color{#f0ac5f}3\\
\color{#58c4dd}3&\color{#83c167}1&\color{#f0ac5f}4\\
\color{#58c4dd}4&\color{#83c167}1&\color{#f0ac5f}5
\end{bmatrix}
$$

</div><div>

Each column has **four components**.

Each input has **three weights**:

$$\mathbf{x}=\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}.$$

<div class="l6-note">A maps inputs in ℝ³ to outputs in ℝ⁴.</div>
</div></div>

---
layout: lecture-six
lecture: 6
title: Column-space example: compute an output
clicks: 0
---

<div class="l6-head"><div class="l6-eyebrow">Worked column-space example</div>

# Choose weights, then compute b

</div>
<div class="l6-split"><div class="l6-math-big">

$$\mathbf x=\begin{bmatrix}2\\-1\\0\end{bmatrix}$$

$$A\mathbf x=2\mathbf a_1-\mathbf a_2$$

$$\mathbf b=\begin{bmatrix}1\\3\\5\\7\end{bmatrix}$$

</div><div>

The first two columns combine to make **b**. Thus **b ∈ C(A)**, and **Ax = b** has a solution.

<div class="l6-note">The input is a list of three column weights. The output has four entries because A has four rows.</div>
</div></div>
<div class="l6-band">For any x, Ax is a linear combination of the columns of A.</div>

---
layout: lecture-six
lecture: 6
title: Two independent output directions
---

<div class="l6-head"><div class="l6-eyebrow">One column repeats existing directions</div>

# Three columns, two directions

</div>
<div class="l6-split"><div>
<div class="l6-hero-number">2</div>
<div class="l6-hero-label">independent output directions</div>

$$\color{#f0ac5f}{\mathbf a_3}=\color{#58c4dd}{\mathbf a_1}+\color{#83c167}{\mathbf a_2}$$

</div><div><LectureSixDiagram kind="columns" /><p class="l6-small">Coefficient view of the output family in ℝ⁴.</p></div></div>
<div class="l6-band">C(A) = span{a₁, a₂}. The third column leaves this space unchanged.</div>

---
layout: lecture-six
lecture: 6
title: Solvability and column space
clicks: 2
---

<div class="l6-head"><div class="l6-eyebrow">Connect geometry to solving equations</div>

# Ax = b is solvable exactly when b ∈ C(A)

</div>
<div class="l6-math-big">

$$A\mathbf{x}=(x_1+x_3)\mathbf a_1+(x_2+x_3)\mathbf a_2$$

</div>
<div class="l6-three">
<section class="l6-panel"><h2>Choose x = e₁</h2>

$$A\begin{bmatrix}1\\0\\0\end{bmatrix}=\color{#58c4dd}{\mathbf a_1}$$

</section>
<section v-click="1" class="l6-panel green"><h2>Choose x = e₂</h2>

$$A\begin{bmatrix}0\\1\\0\end{bmatrix}=\color{#83c167}{\mathbf a_2}$$

</section>
<section v-click="2" class="l6-panel yellow"><h2>Choose x = e₃</h2>

$$A\begin{bmatrix}0\\0\\1\end{bmatrix}=\color{#f0ac5f}{\mathbf a_3}$$

</section></div>

---
layout: lecture-six
lecture: 6
title: A reachable output and an unreachable one
---

<div class="l6-head"><div class="l6-eyebrow">Test a right-hand side</div>

# A reachable output and an unreachable one

</div>
<div class="l6-pair">
<section><h2 class="l6-blue">Reachable</h2>

$$\mathbf b=\begin{bmatrix}1\\3\\5\\7\end{bmatrix}=2\mathbf a_1-\mathbf a_2$$

$$\mathbf{x}=\begin{bmatrix}2\\-1\\0\end{bmatrix}$$

</section><section><h2 class="l6-yellow">Unreachable</h2>

$$\mathbf b=\begin{bmatrix}1\\0\\0\\0\end{bmatrix}$$

<p class="l6-small">Every output of A has zero second differences. Here b₁ − 2b₂ + b₃ = 1.</p>
</section></div>

<!-- The arithmetic-progression test and b=(1,3,5,7) example are computed extensions of the lecture's matrix, not quoted lecture material. -->

---
layout: lecture-six
lecture: 6
title: Code — generate the column space
clicks: 2
codeCopy: false
magicMoveCopy: false
---

<div class="l6-head"><div class="l6-eyebrow">Follow the calculation</div>

# Generate the column space

</div>
<div class="l6-code-grid"><div class="l6-code-block">

````md magic-move {at:1, duration:500, lines:false}
```python {1-5}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])
```
```python {7-8}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

columns = A.columnspace()
print([list(v) for v in columns])
```
```python {10-11}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

columns = A.columnspace()
print([list(v) for v in columns])

x = Matrix([2, -1, 0])
print("A*x =", list(A*x))
```
````

</div><div class="l6-code-result"><LectureSixDiagram kind="code-columns" /><CodeWalkOutput lesson="l6-column" /></div></div>

---
layout: lecture-six
lecture: 6
title: Which inputs does A send to zero?
class: l6-question
---

<div class="l6-eyebrow" style="color:var(--l6-yellow)">The nullspace question</div>

# Which inputs does A<br>send to zero?

<div class="l6-math-huge">

$$A\mathbf{x}=\mathbf 0$$

</div>

<p>Now the output is fixed. Search through the possible inputs.</p>

---
layout: lecture-six
lecture: 6
title: Nullspace example: a nonzero zero input
clicks: 1
---

<div class="l6-head"><div class="l6-eyebrow">Worked nullspace example</div>

# A nonzero input can give zero

</div>
<div class="l6-split"><div>

The third column is the sum of the first two:

$$\mathbf a_3=\mathbf a_1+\mathbf a_2.$$

<div v-click="1" class="l6-note">Choose weights 1, 1, −1. The three weighted columns cancel.</div>
</div><div class="l6-math-big" v-click="1">

$$\mathbf n=\begin{bmatrix}1\\1\\-1\end{bmatrix}$$

$$A\mathbf n=\mathbf a_1+\mathbf a_2-\mathbf a_3$$

$$A\mathbf n=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}$$

</div></div>
<div class="l6-band">n ≠ 0 and An = 0, so n belongs to N(A).</div>

---
layout: lecture-six
lecture: 6
title: Derive the complete nullspace
clicks: 0
---

<div class="l6-head"><div class="l6-eyebrow">Solve Ax = 0</div>

# Derive the complete nullspace

</div>
<div class="l6-split"><div class="l6-math-big">

$$
\operatorname{rref}(A)=\begin{bmatrix}
1&0&1\\0&1&1\\0&0&0\\0&0&0
\end{bmatrix}
$$

</div><div>

The pivot equations are **x₁ + x₃ = 0** and **x₂ + x₃ = 0**.

Let **t = −x₃**. Then **x₁ = t**, **x₂ = t**, and **x₃ = −t**.

<div class="l6-math-big">

$$N(A)=\left\{t\begin{bmatrix}1\\1\\-1\end{bmatrix}:t\in\mathbb R\right\}$$

</div>
</div></div>
<div class="l6-band">There is one free variable, so the nullspace is a line in ℝ³.</div>

---
layout: lecture-six
lecture: 6
title: Visualize the nullspace line
clicks: 3
---

<div class="l6-head"><div class="l6-eyebrow">Visualize the solution set</div>

# The nullspace is a line through zero

</div>
<div class="l6-split"><div>
<div class="l6-math-big">

$$\mathbf x=t\mathbf n$$

$$\mathbf n=\begin{bmatrix}1\\1\\-1\end{bmatrix}$$

</div>

<p>Click through <strong>t = 0, 1, −1, 2</strong>. Every point stays on the line and satisfies <strong>Ax = 0</strong>.</p>
<div class="l6-note">The line passes through the origin and extends in both directions.</div>
</div><div><LectureSixDiagram kind="null" /></div></div>

---
layout: lecture-six
lecture: 6
title: Code — find the nullspace
clicks: 4
codeCopy: false
magicMoveCopy: false
---

<div class="l6-head"><div class="l6-eyebrow">Follow the calculation</div>

# Find the inputs that disappear

</div>
<div class="l6-code-grid"><div class="l6-code-block">

````md magic-move {at:1, duration:500, lines:false}
```python {1-5}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])
```
```python {7-8}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

n = -A.nullspace()[0]
print("n =", list(n))
```
```python {9}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

n = -A.nullspace()[0]
print("n =", list(n))
print("A*n =", list(A*n))
```
```python {11-12}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

n = -A.nullspace()[0]
print("n =", list(n))
print("A*n =", list(A*n))

x0 = Matrix([1, 0, 0])
print("A*x0 =", list(A*x0))
```
```python {13}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

n = -A.nullspace()[0]
print("n =", list(n))
print("A*n =", list(A*n))

x0 = Matrix([1, 0, 0])
print("A*x0 =", list(A*x0))
print("A*(x0+2*n) =", list(A*(x0+2*n)))
```
````

</div><div class="l6-code-result"><LectureSixDiagram kind="code-null" /><CodeWalkOutput lesson="l6-null" /></div></div>

---
layout: lecture-six
lecture: 6
title: Column space and nullspace are different spaces
---

<div class="l6-head"><div class="l6-eyebrow">Keep the two roles distinct</div>

# Outputs and inputs live in different spaces

</div>
<div class="l6-pair">
<section><h2>Column space C(A)</h2><div class="l6-compare-line"><span>Contains</span><strong>outputs b</strong></div><div class="l6-compare-line"><span>Lives in</span><strong>ℝ⁴</strong></div><div class="l6-compare-line"><span>This example</span><strong>two dimensions</strong></div></section>
<section><h2>Nullspace N(A)</h2><div class="l6-compare-line"><span>Contains</span><strong>inputs x</strong></div><div class="l6-compare-line"><span>Lives in</span><strong>ℝ³</strong></div><div class="l6-compare-line"><span>This example</span><strong>one dimension</strong></div></section>
</div>
<div class="l6-band">For an m × n matrix: C(A) ⊆ ℝᵐ and N(A) ⊆ ℝⁿ.</div>

---
layout: lecture-six
lecture: 6
title: Many inputs can give the same output
clicks: 2
---

<div class="l6-head"><div class="l6-eyebrow">Shift the nullspace</div>

# Many inputs can give the same output

</div>
<div class="l6-split"><div>

Choose x₀ = (1, 0, 0)ᵀ. Then Ax₀ = (1, 2, 3, 4)ᵀ.

<div class="l6-math-big">

$$A(\mathbf x_0+t\mathbf n)=A\mathbf x_0$$

</div>

Adding a nullspace vector leaves the output unchanged.

<div v-click="2" class="l6-note">This shifted line misses zero, so it is not a subspace.</div>
</div><div><LectureSixDiagram kind="family" /></div></div>

---
layout: lecture-six
lecture: 6
title: Column space and nullspace: results
clicks: 0
---

<div class="l6-head"><div class="l6-eyebrow">The results for this matrix</div>

# One matrix, two solution sets

</div>
<div class="l6-pair l6-definition-pair">
<section><h2 class="l6-blue">Column space</h2>

$$C(A)=\operatorname{span}\{\mathbf a_1,\mathbf a_2\}$$

<p>a₁ = (1, 2, 3, 4)ᵀ and a₂ = (1, 1, 1, 1)ᵀ. This is a two-dimensional subspace of ℝ⁴ containing (1, 3, 5, 7)ᵀ.</p></section>
<section><h2 class="l6-yellow">Nullspace</h2>

$$N(A)=\operatorname{span}\{(1,1,-1)^T\}$$

<p>It is a one-dimensional subspace of ℝ³. Every vector on this line maps to zero.</p></section>
</div>
<div class="l6-band">Ax = b is solvable exactly when b ∈ C(A); all solutions differ by a vector in N(A).</div>
