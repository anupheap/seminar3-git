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

# Two spaces behind one matrix

</div>
<div class="l6-roadmap">
<div><span>01</span><h2>Subspaces and linear combinations</h2></div>
<div><span>02</span><h2>Column space: the outputs we can reach</h2></div>
<div><span>03</span><h2>Nullspace: the inputs that give zero</h2></div>
</div>
<div class="l6-band">Follow one matrix from its columns to its nullspace.</div>

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
<div class="l6-band">Addition and scaling must keep us inside the same set.</div>

---
layout: lecture-six
lecture: 6
title: The subspace test
---

<div class="l6-head"><div class="l6-eyebrow">A practical checklist</div>

# The subspace test

</div>
<div class="l6-three">
<section class="l6-panel"><div class="l6-symbol">0</div><h2>Keep the origin</h2><p>The zero vector belongs to the set.</p></section>
<section class="l6-panel green"><div class="l6-symbol">+</div><h2>Keep every sum</h2><p>Choose any two vectors in the set. Their sum stays inside.</p></section>
<section class="l6-panel yellow"><div class="l6-symbol">c ×</div><h2>Keep every multiple</h2><p>Any real scale factor is allowed, including zero and negative values.</p></section>
</div>
<div class="l6-band">Equivalently: u, v ∈ S ⇒ c u + d v ∈ S for every c, d ∈ ℝ.</div>

---
layout: lecture-six
lecture: 6
title: Combining two subspaces
clicks: 2
---

<div class="l6-head"><div class="l6-eyebrow">Union and intersection</div>

# Combining two subspaces

</div>
<div class="l6-split"><div><LectureSixDiagram kind="union" /></div><div>

Let **P** be the xy-plane and **L** the z-axis.

<div v-click="1">

The union **P ∪ L** fails: adding a vector from each can leave both sets.

</div><div v-click="2" class="l6-note">

Here **P ∩ L = {0}**. More generally, intersections of subspaces remain subspaces.

</div></div></div>

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
title: The column space
---

<div class="l6-head"><div class="l6-eyebrow">All weighted column combinations</div>

# The column space

</div>
<div class="l6-math-big">

$$
A\mathbf{x}=x_1\color{#58c4dd}{\mathbf a_1}
+x_2\color{#83c167}{\mathbf a_2}
+x_3\color{#f0ac5f}{\mathbf a_3}
$$

$$C(A)=\{A\mathbf{x}:\mathbf{x}\in\mathbb R^3\}$$

</div>
<div class="l6-grid-rule l6-split"><div>

Take every possible choice of weights. The resulting outputs form **C(A)**.

</div><div class="l6-small">

For a general m × n matrix, C(A) is a subspace of ℝᵐ.

</div></div>

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
title: The nullspace
clicks: 1
---

<div class="l6-head"><div class="l6-eyebrow">Inputs that cancel the columns</div>

# The nullspace

</div>
<div class="l6-math-big">

$$N(A)=\{\mathbf{x}\in\mathbb R^3:A\mathbf{x}=\mathbf 0\}$$

</div>
<div class="l6-split"><div>

Zero is always an input that works.

<div v-click="1" class="l6-note">

For this A, a₁ + a₂ − a₃ = 0 also gives a nonzero input.

</div></div><div class="l6-math-big" v-click="1">

$$A\underbrace{\begin{bmatrix}1\\1\\-1\end{bmatrix}}_{\mathbf n}=\begin{bmatrix}0\\0\\0\\0\end{bmatrix}$$

</div></div>

---
layout: lecture-six
lecture: 6
title: The nullspace is a line
clicks: 3
---

<div class="l6-head"><div class="l6-eyebrow">Describe every zero-producing input</div>

# The nullspace is a line

</div>
<div class="l6-split"><div>
<div class="l6-math-big">

$$N(A)=\left\{t\begin{bmatrix}1\\1\\-1\end{bmatrix}:t\in\mathbb R\right\}$$

</div>

Every point on this line maps to the same zero vector.

<div class="l6-note">The line includes the origin and extends in both directions.</div>
</div><div><LectureSixDiagram kind="null" /></div></div>

---
layout: lecture-six
lecture: 6
title: Why the nullspace is a subspace
clicks: 2
---

<div class="l6-head"><div class="l6-eyebrow">Use linearity</div>

# Why N(A) is a subspace

</div>

Suppose **Av = 0** and **Aw = 0**. Choose any scalars c and d.

<div class="l6-math-big" v-click="1">

$$A(c\mathbf v+d\mathbf w)=cA\mathbf v+dA\mathbf w$$

</div><div class="l6-math-big" v-click="2">

$$=c\mathbf 0+d\mathbf 0=\mathbf 0$$

</div>
<div class="l6-band">Every linear combination of nullspace inputs remains in the nullspace.</div>

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

n = A.nullspace()[0]
print("n =", list(n))
```
```python {9}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

n = A.nullspace()[0]
print("n =", list(n))
print("A*n =", list(A*n))
```
```python {11-12}
from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])

n = A.nullspace()[0]
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

n = A.nullspace()[0]
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
title: Two spaces — one matrix
---

<div class="l6-head"><div class="l6-eyebrow">Bring the two questions together</div>

# Two spaces, one matrix

</div>
<div class="l6-three">
<section class="l6-panel"><div class="l6-symbol">C(A)</div><h2>Reach the output</h2><p>Ax = b has a solution when b belongs to the column space.</p></section>
<section class="l6-panel yellow"><div class="l6-symbol">N(A)</div><h2>Find zero inputs</h2><p>The nullspace collects every x whose image under A is zero.</p></section>
<section class="l6-panel green"><div class="l6-symbol">m × n</div><h2>Track the spaces</h2><p>Inputs have n components. Outputs have m components.</p></section>
</div>
<div class="l6-band">A : ℝⁿ → ℝᵐ</div>

<!-- Reference: MIT OCW 18.06SC Lecture 6 summary, https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/a9361fe289da445a7ca1fe2f88b55ca7_MIT18_06SCF11_Ses1.6sum.pdf . New code and derived b examples are verified in scripts/build-code-walkthroughs.py. The coefficient plot is a schematic parameter view; C(A) belongs to R^4. -->
