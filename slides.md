---
theme: seriph
title: Linear Algebra — Selected MIT 18.06 Lectures
author: Based on lectures by Gilbert Strang
info: |
  A seminar on Gilbert Strang's MIT 18.06 lectures 1, 2, 3, 5, 6, and 9.
  Twelve Manim films, twelve Shiki Magic Move Python walkthroughs, twelve Python illustrations, and speaker notes.
class: cover
colorSchema: light
aspectRatio: 16/9
canvasWidth: 980
transition: seminar-forward | seminar-back
magicMoveDuration: 700
magicMoveCopy: true
shiki:
  magicMove:
    delayMove: 0
    delayEnter: 0
    delayLeave: 0
    delayContainer: 0
    stagger: 0
    easing: ease-in-out
drawings:
  persist: false
fonts:
  sans: Segoe UI
  serif: Segoe UI
  mono: Consolas
  provider: none
defaults:
  layout: default
duration: 55min
---

<div class="eyebrow">Gilbert Strang · MIT 18.06</div>

# Linear Algebra

<div class="subtitle">Geometry, equations, and vector spaces</div>

<div class="cover-equation">

$$
A\mathbf{x}=\mathbf{b}
$$

</div>

<div class="small">

Selected lectures 1, 2, 3, 5, 6, and 9

</div>

<!--
About 55 minutes, including the code walkthroughs and practice problem. Ask the audience what a matrix equation means geometrically before showing the first example. This deck follows the numbering in MIT OCW's Spring 2010 publication of 18.06. MIT notes that the lecture videos were recorded in Fall 1999.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

# The six lectures

| Lecture | Topic | Main question |
| :-- | :-- | :-- |
| **1** | Geometry of linear equations | What does $A\mathbf{x}=\mathbf{b}$ mean? |
| **2** | Elimination with matrices | How do we solve the equations? |
| **3** | Multiplication and inverses | How do matrix operations work? |
| **5** | Transposes, permutations, $\mathbb{R}^n$ | What is a vector space? |
| **6** | Column space and nullspace | Which outputs and inputs are possible? |
| **9** | Independence, basis, dimension | How many directions do we need? |

<!--
The selected lectures move from concrete systems to the spaces associated with a matrix. Lectures 4, 7, and 8 are outside the selected list. Brief explanations in this deck make the later examples self-contained.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-videos/
-->

---

<div class="lecture-divider" data-lecture="1">
<div class="eyebrow">Lecture 01</div>

# The geometry of linear equations

<div class="lecture-question">What does A x = b mean geometrically?</div>
</div>

<!--
Lecture 1 begins here. Introduce the central question before advancing to the worked examples.
-->

---

<div class="eyebrow">Lecture 1 · Manim</div>

# The row picture

<div class="film-wide">
<MathFilm src="/animations/RowIntersection.mp4" poster="/animations/RowIntersection.jpg" caption="Two row equations meet at the input (1, 2)." />
</div>

<!--
The equations are 2x-y=0 and -x+2y=3. The same point satisfies both. In three variables a nontrivial row equation describes a plane.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

<div class="eyebrow">Lecture 1 · Python</div>

# Python: solving the intersection

<div class="code-pair">
<div class="code-panel" style="--code-lines: 7" data-code-lines="7">

````md magic-move {duration:700}
```python
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
b = np.array([0., 3.])
```
```python
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
b = np.array([0., 3.])
x = np.linalg.solve(A, b)
print(x)  # [1. 2.]
```
```python
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
b = np.array([0., 3.])
x = np.linalg.solve(A, b)
print(x)  # [1. 2.]
print(A @ x - b)  # [0. 0.]
assert np.allclose(A @ x, b)
```
````

</div>
<CodeVisual lesson="01-solve" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
Every code state is a complete Python example. The residual checks the computed solution against the original system. These small integer examples are well-conditioned. Floating-point equality generally requires a tolerance.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

<div class="eyebrow">Lecture 1</div>

# The column picture

<div class="cols">
<div>

$$
\underbrace{\begin{bmatrix}2&-1\\-1&2\end{bmatrix}}_A
\underbrace{\begin{bmatrix}x\\y\end{bmatrix}}_{\mathbf{x}}
=\underbrace{\begin{bmatrix}0\\3\end{bmatrix}}_{\mathbf{b}}
$$

Matrix multiplication combines the columns of $A$.

</div>
<div>

$$
x\begin{bmatrix}2\\-1\end{bmatrix}
+y\begin{bmatrix}-1\\2\end{bmatrix}
=\begin{bmatrix}0\\3\end{bmatrix}
$$

At $(x,y)=(1,2)$:

$$
\begin{bmatrix}2\\-1\end{bmatrix}
+\begin{bmatrix}-2\\4\end{bmatrix}
=\begin{bmatrix}0\\3\end{bmatrix}
$$

</div>
</div>

<div class="takeaway">

Rows impose equations. Columns combine to produce the right-hand side.

</div>

<!--
The unknowns are weights on columns. Stress that the point (1,2) in the row picture is the input, whereas (0,3) in the column picture is the output. They occupy different conceptual roles even though both have two coordinates here.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

<div class="eyebrow">Lecture 1 · Python</div>

# Python: the weights are coordinates

<div class="code-pair">
<div class="code-panel" style="--code-lines: 8" data-code-lines="8">

````md magic-move {duration:700}
```python
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
a1, a2 = A[:, 0], A[:, 1]
```
```python
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
a1, a2 = A[:, 0], A[:, 1]
b = a1 + 2 * a2
print(b)  # [0. 3.]
```
```python
import numpy as np
A = np.array([[2., -1.], [-1., 2.]])
a1, a2 = A[:, 0], A[:, 1]
b = a1 + 2 * a2
print(b)  # [0. 3.]
x = np.array([1., 2.])
assert np.allclose(b, A @ x)
print(A @ x)  # [0. 3.]
```
````

</div>
<CodeVisual lesson="02-columns" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
Array slicing with A[:,0] selects the first column. The at-sign is matrix multiplication. Compare a weighted sum of columns with the same computation as A @ x. They are identical operations.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

<div class="eyebrow">Lecture 1 · Manim visualization</div>

# A linear combination in motion

<div class="film-wide">
<MathFilm src="/animations/ColumnCombination.mp4" poster="/animations/ColumnCombination.jpg" caption="The coefficients scale the columns. Tip-to-tail addition produces b = (0, 3)." />
</div>

<!--
Play the clip and pause when the orange vector moves to the tip of the blue vector. Translation changes where we draw the vector, not its components. Ask which coefficients produce the target before the final result appears. The animation is an original visualization of the numerical example.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

<div class="eyebrow">Lecture 1</div>

# Three possible solution sets

For a system of real linear equations:

| Outcome | Row picture in two variables | Example |
| :-- | :-- | :-- |
| **One solution** | Two lines intersect once | $x+y=3,\quad x-y=1$ |
| **No solution** | Distinct parallel lines | $x+y=3,\quad x+y=4$ |
| **Infinitely many** | The same line twice | $x+y=3,\quad 2x+2y=6$ |

<div class="takeaway">

Existence and uniqueness are separate questions.

</div>

<!--
These are original small examples. In the last system, every point on x+y=3 works. In the second, the same left-hand side cannot equal both three and four. Over the real numbers, a linear system cannot have exactly two distinct solutions: the line through any two solutions also consists of solutions.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/
-->

---

<div class="lecture-divider" data-lecture="2">
<div class="eyebrow">Lecture 02</div>

# Elimination with matrices

<div class="lecture-question">How do row operations solve a system?</div>
</div>

<!--
Lecture 2 begins here. Introduce the central question before advancing to the worked examples.
-->

---

<div class="eyebrow">Lecture 2 · Manim</div>

# Elimination creates zeros

<div class="film-wide">
<MathFilm src="/animations/EliminationPivots.mp4" poster="/animations/EliminationPivots.jpg" caption="The augmented rows change together. The pivots 1, 1, and 9 lead to x = y = z = 1." />
</div>

<!--
Apply R2-2R1 and R3-R1, then R3+2R2. The right-hand side undergoes every row operation. The next Python walkthrough reveals the same calculation line by line.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/
-->

---

<div class="eyebrow">Lecture 2 · Python</div>

# Python: elimination one row at a time

<div class="code-pair">
<div class="code-panel" style="--code-lines: 11" data-code-lines="11">

````md magic-move {duration:700}
```python
import numpy as np
Ab = np.array([[1., 2., 1., 4.],
               [2., 5., 3., 10.],
               [1., 0., 8., 9.]])
```
```python
import numpy as np
Ab = np.array([[1., 2., 1., 4.],
               [2., 5., 3., 10.],
               [1., 0., 8., 9.]])
Ab[1] -= 2 * Ab[0]
Ab[2] -= Ab[0]
```
```python
import numpy as np
Ab = np.array([[1., 2., 1., 4.],
               [2., 5., 3., 10.],
               [1., 0., 8., 9.]])
Ab[1] -= 2 * Ab[0]
Ab[2] -= Ab[0]
Ab[2] += 2 * Ab[1]
print(Ab)
# [[1. 2. 1. 4.]
#  [0. 1. 1. 2.]
#  [0. 0. 9. 9.]]
```
````

</div>
<CodeVisual lesson="03-elimination" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
Each in-place update applies to the whole augmented row, including b. This teaching example does not require pivoting. A general numerical solver must handle row swaps and numerical stability.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/
-->

---

<div class="eyebrow">Lecture 2</div>

# Back substitution solves the triangle

<div class="cols">
<div>

After $R_3\gets R_3+2R_2$:

$$
\left[\begin{array}{ccc|c}
1&2&1&4\\0&1&1&2\\0&0&9&9
\end{array}\right]
$$

The pivots are $1,1,9$.

</div>
<div>

$$
\begin{aligned}
9z&=9 &\Rightarrow z&=1\\
y+z&=2 &\Rightarrow y&=1\\
x+2y+z&=4 &\Rightarrow x&=1
\end{aligned}
$$

<div class="note">

Three pivots give a unique solution in this square system.

</div>

</div>
</div>

<!--
Verify (1,1,1) in the original equations: 1+2+1=4, 2+5+3=10, and 1+0+8=9. A zero candidate pivot may require a row exchange. If no usable entry exists below it, move to another column and investigate rank and consistency rather than dividing by zero.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/
-->

---

<div class="eyebrow">Lecture 2 · Python</div>

# Python: solving upward from the last row

<div class="code-pair">
<div class="code-panel" style="--code-lines: 11" data-code-lines="11">

````md magic-move {duration:700}
```python
import numpy as np
U = np.array([[1., 2., 1.],
              [0., 1., 1.],
              [0., 0., 9.]])
c = np.array([4., 2., 9.])
x = np.zeros(3)
```
```python
import numpy as np
U = np.array([[1., 2., 1.],
              [0., 1., 1.],
              [0., 0., 9.]])
c = np.array([4., 2., 9.])
x = np.zeros(3)
x[2] = c[2] / U[2, 2]
x[1] = (c[1] - x[2]) / U[1, 1]
```
```python
import numpy as np
U = np.array([[1., 2., 1.],
              [0., 1., 1.],
              [0., 0., 9.]])
c = np.array([4., 2., 9.])
x = np.zeros(3)
x[2] = c[2] / U[2, 2]
x[1] = (c[1] - x[2]) / U[1, 1]
x[0] = c[0] - 2*x[1] - x[2]
print(x)  # [1. 1. 1.]
assert np.allclose(U @ x, c)
```
````

</div>
<CodeVisual lesson="04-back-substitution" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
The bottom row contains only z, so solve it first. Then substitute z into row two, and substitute both y and z into row one. The final assertion verifies the triangular system.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/
-->

---

<div class="eyebrow">Lecture 2</div>

# Row operations are matrix multiplication

The operation $R_2\gets R_2-2R_1$ has an elimination matrix:

$$
E_{21}=\begin{bmatrix}1&0&0\\-2&1&0\\0&0&1\end{bmatrix}
$$

$$
E_{21}A=
\begin{bmatrix}1&2&1\\0&1&1\\1&0&8\end{bmatrix},
\qquad E_{21}\mathbf{b}=\begin{bmatrix}4\\2\\9\end{bmatrix}
$$

<div class="takeaway">

$A\mathbf{x}=\mathbf{b}$ and $EA\mathbf{x}=E\mathbf{b}$ have the same solutions when $E$ is invertible.

</div>

<!--
Multiplication on the left acts on rows. This elimination matrix is invertible because adding twice row 1 back to row 2 reverses the operation. In a sequence, the rightmost matrix acts first. Elimination therefore connects equation solving to the multiplication rules in lecture 3.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/
-->

---

<div class="eyebrow">Lecture 2 · Manim visualization</div>

# Elimination preserves the intersection

<div class="film-wide">
<MathFilm src="/animations/EliminationGeometry.mp4" poster="/animations/EliminationGeometry.jpg" caption="Replacing row 2 by row 2 + ½ row 1 turns the second equation into 3y/2 = 3. The intersection stays at (1, 2)." />
</div>

<!--
This animation returns to the 2-by-2 example from lecture 1. During the interpolation, row 2 becomes row 2 plus t times row 1. The changing line has equation (-1+2t)x+(2-t)y=3. For every displayed t, (1,2) remains on it. At t=1/2, x disappears from the second equation.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/
-->

---

<div class="lecture-divider" data-lecture="3">
<div class="eyebrow">Lecture 03</div>

# Multiplication and inverse matrices

<div class="lecture-question">How do matrices combine and undo operations?</div>
</div>

<!--
Lecture 3 begins here. Introduce the central question before advancing to the worked examples.
-->

---

<div class="eyebrow">Lecture 3</div>

# Five views of matrix multiplication

<div class="compact">

For $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{n\times p}$, the product $C=AB$ is $m\times p$.

| View | Computation |
| :-- | :-- |
| Row times column | $c_{ij}=\sum_{k=1}^{n}a_{ik}b_{kj}$ |
| A column at a time | $C_{:j}=A B_{:j}$ |
| A row at a time | $C_{i:}=A_{i:}B$ |
| Column times row | $AB=\sum_{k=1}^{n}A_{:k}B_{k:}$ |
| Blocks | $C_{11}=A_{11}B_{11}+A_{12}B_{21}$ for compatible blocks |

</div>

<!--
The colon means all entries along that index: A colon k is the kth column, and B k colon is the kth row. The outer-product view adds n matrices of size m by p. Block multiplication follows the same pattern only when block dimensions match. All five views perform the same underlying multiplications.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/
-->

---

<div class="eyebrow">Lecture 3 · Python</div>

# Python: three equivalent products

<div class="code-pair">
<div class="code-panel" style="--code-lines: 13" data-code-lines="13">

````md magic-move {duration:700}
```python
import numpy as np
A = np.array([[2, -1], [-1, 2]])
B = np.array([[1, 2], [0, 1]])
C = A @ B
```
```python
import numpy as np
A = np.array([[2, -1], [-1, 2]])
B = np.array([[1, 2], [0, 1]])
C = A @ B
by_columns = np.column_stack(
    [A @ B[:, j] for j in range(2)])
assert np.allclose(C, by_columns)
```
```python
import numpy as np
A = np.array([[2, -1], [-1, 2]])
B = np.array([[1, 2], [0, 1]])
C = A @ B
by_columns = np.column_stack(
    [A @ B[:, j] for j in range(2)])
assert np.allclose(C, by_columns)
terms = [np.outer(A[:, k], B[k])
         for k in range(2)]
by_outer = sum(terms)
assert np.allclose(C, by_outer)
print(C)      # [[2, 3], [-1, 0]]
print(B @ A)  # [[0, 3], [-1, 2]]
```
````

</div>
<CodeVisual lesson="05-products" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
The code compares the usual product with multiplication by columns and a sum of outer products. The plot compares AB with BA, which is a different operation. Shapes match here because both matrices are square.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/
-->

---

<div class="eyebrow">Lecture 3 · Manim</div>

# Multiplication order matters

<div class="film-wide">
<MathFilm src="/animations/MatrixComposition.mp4" poster="/animations/MatrixComposition.jpg" caption="A = [[2, −1], [−1, 2]], B = [[1, 2], [0, 1]]. For v = (1, 1.5), ABv and BAv differ." />
</div>

<!--
The rightmost factor acts first. The blue path is v to Bv=(4,1.5) to ABv=(6.5,-1). The orange path is v to Av=(0.5,2) to BAv=(4.5,2). Associativity holds, but exchanging factors generally changes the result.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/
-->

---

<div class="eyebrow">Lecture 3 · Manim</div>

# Gauss–Jordan finds the inverse

<div class="film-wide">
<MathFilm src="/animations/GaussJordanInverse.mp4" poster="/animations/GaussJordanInverse.jpg" caption="The same row operations reduce A to I and turn I into A⁻¹ = [[7, −3], [−2, 1]]." />
</div>

<!--
For A=[[1,3],[2,7]], use R2-2R1 then R1-3R2. Keeping all four augmented columns together is essential.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/
-->

---

<div class="eyebrow">Lecture 3 · Python</div>

# Python: reducing both halves together

<div class="code-pair">
<div class="code-panel" style="--code-lines: 9" data-code-lines="9">

````md magic-move {duration:700}
```python
import numpy as np
A = np.array([[1., 3.], [2., 7.]])
aug = np.column_stack((A, np.eye(2)))
```
```python
import numpy as np
A = np.array([[1., 3.], [2., 7.]])
aug = np.column_stack((A, np.eye(2)))
aug[1] -= 2 * aug[0]
aug[0] -= 3 * aug[1]
```
```python
import numpy as np
A = np.array([[1., 3.], [2., 7.]])
aug = np.column_stack((A, np.eye(2)))
aug[1] -= 2 * aug[0]
aug[0] -= 3 * aug[1]
inverse = aug[:, 2:]
print(inverse)  # [[7, -3], [-2, 1]]
assert np.allclose(aug[:, :2], np.eye(2))
assert np.allclose(A @ inverse, np.eye(2))
```
````

</div>
<CodeVisual lesson="06-inverse" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
The first two columns hold A and the last two hold I. The same operations act on all four columns. Once the left half is I, slicing the right half gives the inverse. Numerical applications usually solve directly instead of explicitly forming inverses.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/
-->

---

<div class="eyebrow">Lecture 3</div>

# What an inverse guarantees

For a square invertible matrix:

$$
A^{-1}A=AA^{-1}=I,\qquad \mathbf{x}=A^{-1}\mathbf{b}
$$

- Every right-hand side has exactly one solution.
- A nonzero solution of $A\mathbf{z}=0$ rules out an inverse.
- If $A$ and $B$ are invertible, $(AB)^{-1}=B^{-1}A^{-1}$.

<div class="takeaway">

Elimination can solve $A\mathbf{x}=\mathbf{b}$ directly without forming $A^{-1}$.

</div>

<!--
For the nullspace test, suppose A has an inverse and Az=0. Multiplying by the inverse gives z=0. Thus any nonzero null vector contradicts invertibility. The reverse order in the product inverse follows by grouping ABB-inverse A-inverse. Both A and B must be square and invertible here.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/
-->

---

<div class="lecture-divider" data-lecture="5">
<div class="eyebrow">Lecture 05</div>

# Transposes, permutations, and vector spaces

<div class="lecture-question">What changes when we transpose or reorder rows?</div>
</div>

<!--
Lecture 5 begins here. Introduce the central question before advancing to the worked examples.
-->

---

<div class="eyebrow">Lecture 5 · Manim</div>

# Transposes exchange rows and columns

<div class="film-wide">
<MathFilm src="/animations/MatrixTranspose.mp4" poster="/animations/MatrixTranspose.jpg" caption="A 2 × 3 array becomes 3 × 2. The product rule reverses order: (AB)ᵀ = BᵀAᵀ." />
</div>

<!--
Entry (i,j) becomes entry (j,i). The blue first row becomes the blue first column, and the orange second row becomes the orange second column. A symmetric matrix satisfies A.T=A.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/
-->

---

<div class="eyebrow">Lecture 5 · Python</div>

# Python: transpose and row permutation

<div class="code-pair">
<div class="code-panel" style="--code-lines: 11" data-code-lines="11">

````md magic-move {duration:700}
```python
import numpy as np
A = np.arange(1, 7).reshape(2, 3)
print(A.shape)  # (2, 3)
```
```python
import numpy as np
A = np.arange(1, 7).reshape(2, 3)
print(A.shape)  # (2, 3)
R = A.T
print(R.shape)  # (3, 2)
print(R)  # [[1, 4], [2, 5], [3, 6]]
```
```python
import numpy as np
A = np.arange(1, 7).reshape(2, 3)
print(A.shape)  # (2, 3)
R = A.T
print(R.shape)  # (3, 2)
print(R)  # [[1, 4], [2, 5], [3, 6]]
P = np.array([[0, 1, 0],
              [0, 0, 1],
              [1, 0, 0]])
print(P @ R)  # [[2, 5], [3, 6], [1, 4]]
assert np.allclose(P.T @ P, np.eye(3))
```
````

</div>
<CodeVisual lesson="07-transpose" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
A.T is a transpose. The permutation P has the cyclic order used in the next Manim clip. It multiplies R=A.T on the left, producing rows two, three, one. Transposing P reverses that permutation.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/
-->

---

<div class="eyebrow">Lecture 5 · Manim</div>

# Permutations reorder rows

<div class="film-wide">
<MathFilm src="/animations/PermutationRows.mp4" poster="/animations/PermutationRows.jpg" caption="This cyclic P uses row order 2, 3, 1. Its transpose reverses the permutation." />
</div>

<!--
P=[[0,1,0],[0,0,1],[1,0,0]]. P inverse equals P transpose, not necessarily P. With row exchanges the elimination factorization becomes PA=LU.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/
-->

---

<div class="eyebrow">Lecture 5</div>

# Vector spaces and subspaces

$\mathbb{R}^n$ contains all real column vectors with $n$ entries.

A nonempty subset $V\subseteq\mathbb{R}^n$ is a subspace when:

<div class="math-large">

$$
\mathbf{u},\mathbf{v}\in V,\quad c,d\in\mathbb{R}
\quad\Longrightarrow\quad c\mathbf{u}+d\mathbf{v}\in V
$$

</div>

It stays closed under addition and multiplication by **every real scalar**.

<div class="takeaway">

Every subspace contains the zero vector.

</div>

<!--
Explain that a subspace inherits the usual vector addition and scalar multiplication from Rn. Taking both coefficients zero shows the need for the zero vector. Functions and matrices can also form vector spaces, but this seminar focuses on spaces of real coordinate vectors.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/
-->

---

<div class="eyebrow">Lecture 5</div>

# The subspace test

| Set | Subspace? | Reason |
| :-- | :-- | :-- |
| The line $y=2x$ | **Yes** | Linear combinations stay on the line |
| The line $y=2x+1$ | No | It misses the zero vector |
| The first quadrant | No | Negative scaling leaves the set |
| The plane $x+y+z=0$ | **Yes** | Addition and scaling preserve the equation |

<div class="takeaway">

Passing through the origin is necessary, but closure still needs checking.

</div>

<!--
Use the first quadrant to show why containing zero is insufficient: (1,1) belongs, but its negative does not. For the plane, add two equations with right-hand side zero or multiply one by a scalar. A union of distinct lines through the origin is another set that contains zero but fails closure under addition.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/
-->

---

<div class="eyebrow">Lecture 5 · Python</div>

# Python: closure examples and a counterexample

<div class="code-pair">
<div class="code-panel" style="--code-lines: 11" data-code-lines="11">

````md magic-move {duration:700}
```python
import numpy as np
u = np.array([1, 2])
v = np.array([-2, -4])
assert u[1] == 2*u[0]
assert v[1] == 2*v[0]
```
```python
import numpy as np
u = np.array([1, 2])
v = np.array([-2, -4])
assert u[1] == 2*u[0]
assert v[1] == 2*v[0]
w = 3*u - 2*v
print(w)  # [7 14]
assert w[1] == 2*w[0]
```
```python
import numpy as np
u = np.array([1, 2])
v = np.array([-2, -4])
assert u[1] == 2*u[0]
assert v[1] == 2*v[0]
w = 3*u - 2*v
print(w)  # [7 14]
assert w[1] == 2*w[0]
q = np.array([1, 1])
assert np.all(q >= 0)
print(np.all(-q >= 0))  # False
```
````

</div>
<CodeVisual lesson="08-subspace" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
Finite examples illustrate closure but do not prove it for every vector. The algebraic equation y=2x proves closure in this case. The negative of q=(1,1) gives a decisive counterexample for the first quadrant.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/
-->

---

<div class="lecture-divider" data-lecture="6">
<div class="eyebrow">Lecture 06</div>

# Column space and nullspace

<div class="lecture-question">Which outputs are possible, and which inputs map to zero?</div>
</div>

<!--
Lecture 6 begins here. Introduce the central question before advancing to the worked examples.
-->

---

<div class="eyebrow">Lecture 6 · Manim</div>

# Column space describes possible outputs

<div class="film-wide">
<MathFilm src="/animations/ColumnSpaceSweep.mp4" poster="/animations/ColumnSpaceSweep.jpg" caption="For B = [[1, 2, 3], [2, 4, 6]], every output lies on b₂ = 2b₁." />
</div>

<!--
C(B) is a line in R2. The point (4,8) is reachable, while (4,7) is not. The input vector has three coordinates, but the output has two.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/
-->

---

<div class="eyebrow">Lecture 6 · Python</div>

# Python: testing whether b belongs to C(B)

<div class="code-pair">
<div class="code-panel" style="--code-lines: 11" data-code-lines="11">

````md magic-move {duration:700}
```python
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
r = np.linalg.matrix_rank(B)
print(r)  # 1
```
```python
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
r = np.linalg.matrix_rank(B)
print(r)  # 1
good = np.column_stack((B, [4, 8]))
print(np.linalg.matrix_rank(good) == r)
# True: the target is in C(B)
```
```python
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
r = np.linalg.matrix_rank(B)
print(r)  # 1
good = np.column_stack((B, [4, 8]))
print(np.linalg.matrix_rank(good) == r)
# True: the target is in C(B)
bad = np.column_stack((B, [4, 7]))
assert np.linalg.matrix_rank(good) == r
print(np.linalg.matrix_rank(bad) == r)
# False: the target is outside C(B)
```
````

</div>
<CodeVisual lesson="09-column-space" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
This connects lecture 6 to the rank language in lecture 9. A right-hand side belongs to the column space if adding it as a column leaves the rank unchanged. NumPy estimates numerical rank using a floating-point tolerance.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/
-->

---

<div class="eyebrow">Lecture 6 · Manim</div>

# Nullspace describes inputs sent to zero

<div class="film-wide">
<MathFilm src="/animations/NullspacePlane.mp4" poster="/animations/NullspacePlane.jpg" caption="N(B) is the plane x₁ + 2x₂ + 3x₃ = 0 in input space R³. Every point maps to zero." />
</div>

<!--
Its basis is (-2,1,0), (-3,0,1). Parameterizing x=s*(-2,1,0)+t*(-3,0,1) produces the entire plane. Contrast with C(B), a line in R2.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/
-->

---

<div class="eyebrow">Lecture 6</div>

# Every solution has a nullspace part

For $B\mathbf{x}=\begin{bmatrix}4&8\end{bmatrix}^T$, one solution is $\mathbf{x}_p=(4,0,0)^T$.

$$
\boxed{\mathbf{x}=\begin{bmatrix}4\\0\\0\end{bmatrix}
+s\begin{bmatrix}-2\\1\\0\end{bmatrix}
+t\begin{bmatrix}-3\\0\\1\end{bmatrix}}
$$

$$
B(\mathbf{x}_p+\mathbf{x}_n)=\mathbf{b}+0=\mathbf{b}
$$

<div class="note">

The solutions form a shifted plane. Because $\mathbf{b}\ne0$, this solution set is not a subspace.

</div>

<!--
This direct parameterization supplies a short bridge over the unselected lectures 7 and 8. If x and xp solve the same equation, B(x-xp)=0. That proves every solution, not just some solutions, has this form. Distinguish the homogeneous nullspace from a shifted set of solutions to a nonhomogeneous equation.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/
-->

---

<div class="eyebrow">Lecture 6 · Python</div>

# Python: adding a nullspace vector

<div class="code-pair">
<div class="code-panel" style="--code-lines: 9" data-code-lines="9">

````md magic-move {duration:700}
```python
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
N = np.array([[-2, -3], [1, 0], [0, 1]])
assert np.allclose(B @ N, 0)
```
```python
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
N = np.array([[-2, -3], [1, 0], [0, 1]])
assert np.allclose(B @ N, 0)
xp = np.array([4., 0., 0.])
x = xp + N @ np.array([0.5, 1.0])
print(x)  # [0.  0.5 1. ]
```
```python
import numpy as np
B = np.array([[1, 2, 3], [2, 4, 6]])
N = np.array([[-2, -3], [1, 0], [0, 1]])
assert np.allclose(B @ N, 0)
xp = np.array([4., 0., 0.])
x = xp + N @ np.array([0.5, 1.0])
print(x)  # [0.  0.5 1. ]
assert np.allclose(B @ x, [4, 8])
print(B @ x)  # [4. 8.]
```
````

</div>
<CodeVisual lesson="10-nullspace" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
The columns of N are (-2,1,0) and (-3,0,1). B@N=0 checks both basis vectors at once. For any real parameter pair, xp+N@parameters remains a solution for b=(4,8). The picture shows the homogeneous plane, not the shifted solution plane.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/
-->

---

<div class="eyebrow">Lectures 6 and 9</div>

# What elimination preserves

$$
B=\begin{bmatrix}1&2&3\\2&4&6\end{bmatrix}
\quad\xrightarrow{\ R_2-2R_1\ }\quad
U=\begin{bmatrix}1&2&3\\0&0&0\end{bmatrix}
$$

<div class="cols">
<div>

### The nullspace stays the same

$$
N(B)=N(U)
$$

Both impose $x_1+2x_2+3x_3=0$.

</div>
<div>

### The column space can change

$$
C(B)=\operatorname{span}\!\left\{\begin{bmatrix}1\\2\end{bmatrix}\right\}
$$

$$
C(U)=\operatorname{span}\!\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}
$$

</div>
</div>

<!--
This distinction will matter when choosing a basis from pivot columns. Invertible row operations preserve linear dependence relations among columns, and therefore the rank, but can move the actual column space. Select column-space basis vectors from the original matrix using the pivot indices found by elimination.
Sources: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/ and https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="lecture-divider" data-lecture="9">
<div class="eyebrow">Lecture 09</div>

# Independence, basis, and dimension

<div class="lecture-question">How many independent directions describe a space?</div>
</div>

<!--
Lecture 9 begins here. Introduce the central question before advancing to the worked examples.
-->

---

<div class="eyebrow">Lecture 9</div>

# Independence excludes redundancy

Vectors $\mathbf{v}_1,\ldots,\mathbf{v}_k$ are independent if

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k=0
\quad\Longrightarrow\quad c_1=\cdots=c_k=0
$$

For example:

$$
\mathbf{v}_1=\begin{bmatrix}1\\0\end{bmatrix},\quad
\mathbf{v}_2=\begin{bmatrix}1\\1\end{bmatrix},\quad
\mathbf{v}_3=\begin{bmatrix}2\\1\end{bmatrix}
$$

Since $\mathbf{v}_1+\mathbf{v}_2-\mathbf{v}_3=0$, these three vectors are **dependent**.

<!--
The relation has coefficients (1,1,-1), which are not all zero. Thus the third vector contributes no new direction beyond the first two. Equivalently, columns are independent precisely when the matrix formed from them has only the zero vector in its nullspace. These numerical vectors are an original teaching example.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="eyebrow">Lecture 9 · Manim visualization</div>

# A redundant vector adds no direction

<div class="film-wide">
<MathFilm src="/animations/DependenceAndBasis.mp4" poster="/animations/DependenceAndBasis.jpg" caption="The first two vectors already span the plane. The third equals their sum, so it does not enlarge the span." />
</div>

<!--
Pause after the third vector appears. Ask the audience for a nonzero set of coefficients that gives zero. Then explain that deleting the redundant third vector preserves the span. The remaining two are independent, so they form a basis of R2. This is an original Manim scene.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="eyebrow">Lecture 9 · Manim</div>

# A basis spans without redundancy

<div class="film-wide">
<MathFilm src="/animations/BasisCoordinates.mp4" poster="/animations/BasisCoordinates.jpg" caption="A basis is independent and spans the space. The vector (3, 2) has coordinates (1, 2) in this basis." />
</div>

<!--
The basis columns are b1=(1,0) and b2=(1,1). Their combination b1+2b2 gives (3,2). A different basis changes coordinates, not the vector. Every basis of R2 has two vectors.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="eyebrow">Lecture 9 · Python</div>

# Python: coordinates in a different basis

<div class="code-pair">
<div class="code-panel" style="--code-lines: 7" data-code-lines="7">

````md magic-move {duration:700}
```python
import numpy as np
V = np.array([[1., 1.], [0., 1.]])
v = np.array([3., 2.])
```
```python
import numpy as np
V = np.array([[1., 1.], [0., 1.]])
v = np.array([3., 2.])
c = np.linalg.solve(V, v)
print(c)  # [1. 2.]
```
```python
import numpy as np
V = np.array([[1., 1.], [0., 1.]])
v = np.array([3., 2.])
c = np.linalg.solve(V, v)
print(c)  # [1. 2.]
assert np.allclose(V @ c, v)
assert np.linalg.matrix_rank(V) == 2
```
````

</div>
<CodeVisual lesson="11-coordinates" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
The columns of V are the new basis vectors. Solving Vc=v finds the basis coordinates, while V@c reconstructs the vector in standard coordinates. The vector itself stays fixed. Both bases have dimension two.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="eyebrow">Lecture 9</div>

# Pivot columns give a column-space basis

$$
M=\begin{bmatrix}1&0&1\\2&1&3\\0&1&1\end{bmatrix}
\quad\xrightarrow{\text{elimination}}\quad
U=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}
$$

The pivot columns are **1 and 2**. Use those columns of the original $M$:

$$
\text{Basis of }C(M):\quad
\left\{\begin{bmatrix}1\\2\\0\end{bmatrix},
\begin{bmatrix}0\\1\\1\end{bmatrix}\right\}
$$

$$
\operatorname{rank}(M)=\dim C(M)=2
$$

<!--
First replace row 2 by row 2 minus twice row 1, then replace row 3 by row 3 minus the new row 2. The original third column is the sum of the first two. The two pivot columns are independent and generate every column, so they form a basis. Avoid choosing columns from U as a basis for C(M).
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="eyebrow">Lecture 9</div>

# Rank and nullity count different directions

For the same $M$, the homogeneous equations reduce to

$$
x_1+x_3=0,\qquad x_2+x_3=0
$$

$$
N(M)=\operatorname{span}\!\left\{\begin{bmatrix}-1\\-1\\1\end{bmatrix}\right\}
$$

<div class="math-large">

$$
\underbrace{\operatorname{rank}(M)}_{2}
+\underbrace{\dim N(M)}_{1}
=\underbrace{n}_{3}
$$

</div>

<div class="small">

For any $m\times n$ matrix, rank + nullity equals the number of columns $n$.

</div>

<!--
There are two pivot variables and one free variable. Each free variable contributes one independent nullspace direction. This explains the rank-nullity count: n input coordinates split into r pivot positions and n-r free positions. For M, the column space is a plane and the nullspace is a line, both inside R3.
Source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

<div class="eyebrow">Lecture 9 · Python</div>

# Python: rank plus nullity

<div class="code-pair">
<div class="code-panel" style="--code-lines: 11" data-code-lines="11">

````md magic-move {duration:700}
```python
import numpy as np
from scipy.linalg import null_space
M = np.array([[1., 0., 1.],
              [2., 1., 3.],
              [0., 1., 1.]])
r = np.linalg.matrix_rank(M)
```
```python
import numpy as np
from scipy.linalg import null_space
M = np.array([[1., 0., 1.],
              [2., 1., 3.],
              [0., 1., 1.]])
r = np.linalg.matrix_rank(M)
N = null_space(M)
print(r, N.shape[1])  # 2 1
```
```python
import numpy as np
from scipy.linalg import null_space
M = np.array([[1., 0., 1.],
              [2., 1., 3.],
              [0., 1., 1.]])
r = np.linalg.matrix_rank(M)
N = null_space(M)
print(r, N.shape[1])  # 2 1
assert np.allclose(M @ N, 0)
assert r + N.shape[1] == M.shape[1]
print(r, N.shape[1], M.shape[1])  # 2 1 3
```
````

</div>
<CodeVisual lesson="12-rank" />
</div>

<div class="step-hint">Space advances the code. Left arrow returns to the previous step.</div>

<!--
SciPy returns an orthonormal nullspace basis, so its entries can differ from the integer basis by scaling or sign. It still spans the same line. The assertion checks the defining equation M@N=0 with a numerical tolerance.
The final code state is included in python_examples/examples.py. The synchronized visual states are computed by executing each code stage in python_examples/visual_states.py. The visualization reads the same local click count as Magic Move. Forward and backward navigation update both together.
Lecture source: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

# One matrix connects the six lectures

<div class="cols wide-left">
<div>

$$
M=\begin{bmatrix}1&0&1\\2&1&3\\0&1&1\end{bmatrix}
$$

$$
C(M)=\{\mathbf{b}:b_2=2b_1+b_3\}
$$

For $\mathbf{b}=(2,5,1)^T$:

$$
\mathbf{x}=\begin{bmatrix}2\\1\\0\end{bmatrix}
+t\begin{bmatrix}-1\\-1\\1\end{bmatrix}
$$

</div>
<div>

**Geometry:** achievable outputs form a plane.

**Elimination:** two pivots remain.

**Dependence:** column 3 equals columns 1 + 2.

**Dimension:** rank $2$, nullity $1$.

**Inverse:** no inverse exists.

</div>
</div>

<!--
Original synthesis example. The columns are c1=(1,2,0), c2=(0,1,1), and c3=c1+c2. Every output has second coordinate twice the first plus the third. For b=(2,5,1), xp=(2,1,0) works and all other solutions differ by a null vector. By contrast, b=(2,6,1) violates the condition and has no solution.
Sources: MIT 18.06 lectures 1, 2, 3, 5, 6, and 9, linked on the final slide.
-->

---

# Existence and uniqueness through rank

Let $A$ be $m\times n$, with rank $r$.

| Rank condition | Which right-hand sides work? | Solutions when consistent |
| :-- | :-- | :-- |
| $r=m=n$ | Every $\mathbf{b}\in\mathbb{R}^m$ | Exactly one |
| $r=m<n$ | Every $\mathbf{b}\in\mathbb{R}^m$ | Infinitely many |
| $r=n<m$ | Only $\mathbf{b}\in C(A)$ | Exactly one |
| $r<m$ and $r<n$ | Only $\mathbf{b}\in C(A)$ | Infinitely many |

<div class="takeaway">

Column space controls existence. Nullspace controls uniqueness.

</div>

<!--
These four cases exhaust the possibilities because r cannot exceed either m or n. Over R, a consistent system with at least one free variable has infinitely many solutions. The third row is useful: a tall matrix can have a unique solution for a particular right-hand side without having an ordinary two-sided inverse.
Sources: https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/ and https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/
-->

---

# Practice: the same questions again

$$
Q=\begin{bmatrix}1&2&0\\0&0&1\\1&2&1\end{bmatrix},
\qquad\mathbf{b}=\begin{bmatrix}3\\1\\4\end{bmatrix}
$$

1. Which columns form a basis for $C(Q)$?
2. What are the rank and nullity?
3. What is the complete solution to $Q\mathbf{x}=\mathbf{b}$?

<div class="note">

Hint: compare column 2 with column 1, and compare row 3 with rows 1 and 2.

</div>

<!--
Allow about two minutes. This is an original practice problem. Ask for the dependence relation first, then a null vector. Next, use the first two rows to construct one solution. The third row checks the consistency condition b3=b1+b2. The next slide gives the answer.
-->

---

# Practice: basis, dimension, solutions

<div class="cols">
<div>

Column 2 is twice column 1.

$$
\text{Basis of }C(Q):\quad
\left\{\begin{bmatrix}1\\0\\1\end{bmatrix},
\begin{bmatrix}0\\1\\1\end{bmatrix}\right\}
$$

$$
\operatorname{rank}(Q)=2,\qquad\dim N(Q)=1
$$

</div>
<div>

The equations give $x_1+2x_2=3$ and $x_3=1$.

$$
\boxed{\mathbf{x}=\begin{bmatrix}3\\0\\1\end{bmatrix}
+t\begin{bmatrix}-2\\1\\0\end{bmatrix}}
$$

The third row is consistent because $4=3+1$.

</div>
</div>

<!--
Verify Q times (3,0,1) is (3,1,4), and Q times (-2,1,0) is zero. The first and third columns are independent because the second coordinate forces the coefficient of column 3 to vanish, after which the first coordinate forces the other coefficient to vanish. Their span contains all three columns.
-->

---

<div class="summary-content">

# The main ideas

| Concept | Meaning |
| :-- | :-- |
| $A\mathbf{x}=\mathbf{b}$ | A linear combination of columns produces $\mathbf{b}$ |
| Elimination | Reversible row operations simplify the equations |
| Inverse | Every right-hand side has a unique solution |
| Subspace | A set closed under all linear combinations |
| Column space and nullspace | Achievable outputs and inputs sent to zero |
| Basis and dimension | Independent spanning vectors and their count |

<div class="takeaway">

For $A\in\mathbb{R}^{m\times n}$: $\dim C(A)+\dim N(A)=n$.

</div>

</div>

<!--
Ask the audience to explain each concept without calculating. Keep the inverse statement in its square-matrix context. Revisit the opening matrix equation, now with an interpretation of when it can be solved, how many solutions it has, and how elimination reveals the dimensions.
Sources: the six MIT lecture links on the following slide.
-->

---

# Sources and further study

<div class="source-list">

Gilbert Strang, **MIT 18.06 Linear Algebra**, MIT OpenCourseWare.

[1. The geometry of linear equations](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-1-the-geometry-of-linear-equations/)

[2. Elimination with matrices](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-2-elimination-with-matrices/)

[3. Multiplication and inverse matrices](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-3-multiplication-and-inverse-matrices/)

[5. Transposes, permutations, spaces Rⁿ](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n/)

[6. Column space and nullspace](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/)

[9. Independence, basis, and dimension](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-basis-and-dimension/)

</div>

<div class="small">

Spring 2010 OCW publication, using lectures recorded in Fall 1999. This seminar adapts the concepts with worked examples and original Manim animations.

</div>

<!--
The lecture 1 opening system and lecture 3 Gauss-Jordan matrix come from Strang's examples. Other worked matrices, the practice problem, explanatory wording, and animations are original to this seminar. Source links also appear in the relevant speaker notes. MIT's resource pages identify the recording date as Fall 1999, while the course publication is Spring 2010.
https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
-->
