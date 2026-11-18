---
theme: seriph
title: Seminar III Linear Algebra — Source Deck
author: Seminar III
info: |
  Source-based seminar deck for Lectures 1, 2, 3, 5, and 9. Lecture 1 uses the supplied PDF and Seminar.pptx; Lecture 2 uses Seminar.pptx; Lecture 3 uses Presentation2.pptx; Lecture 5 uses Lecture5.pptx; Lecture 9 uses the second supplied Canva deck.
class: cover
colorSchema: light
aspectRatio: 16/9
canvasWidth: 980
transition: fade
fonts:
  sans: Segoe UI
  serif: Segoe UI
  mono: Consolas
  provider: none
---

<div class="eyebrow">Project and Seminar III · Linear Algebra</div>

# Linear Algebra

<div class="subtitle">Geometry, elimination, matrix operations, and vector spaces</div>

<div class="cover-equation">

$$A\mathbf{x}=\mathbf{b}$$

</div>

<div class="small">

Lectures 1, 2, 3, 5, and 9 · compiled from the supplied PDF, Canva decks, and PowerPoint files

</div>

<!-- Sources: Lecture 1 PDF pp. 1–18; Seminar.pptx; Presentation2.pptx; Lecture5.pptx; Canva Lecture 9. PDF pp. 19–28 and Canva template pages are excluded as requested. -->

---

# The five source lectures

| Lecture | Topic | Source |
| :-- | :-- | :-- |
| **1** | Geometry of linear equations | PDF, first Canva deck, `Seminar.pptx` |
| **2** | Elimination with matrices | `Seminar.pptx` |
| **3** | Matrix multiplication and inverses | `Presentation2.pptx` |
| **5** | Permutations, transposes, vector spaces | `Lecture5.pptx` |
| **9** | Independence, basis, dimension | Second Canva deck |

<!-- The sources are complementary, not identical. The PDF and first Canva deck mostly match for Lecture 1, but their agenda wording differs. -->

---

<div class="lecture-divider"><div class="eyebrow">Lecture 01</div>

# Geometry of linear equations

<div class="lecture-question">

Two views of the same system: rows show intersections; columns show combinations.

</div></div>

<!-- Sources: Lecture 1 PDF pp. 1–18; Seminar.pptx slides 2–18; Canva Lecture 1 pp. 1–18. -->

---

<div class="eyebrow">Lecture 1 · Contents</div>

# From equations to geometry

1. Row picture: draw each equation as a line or plane.
2. Column picture: combine weighted columns to reach a target.
3. Questions: which right-hand sides can we reach?
4. Special cases: one, none, or infinitely many solutions.

<div class="note">

The PowerPoint adds the question “Why do $n$ unknowns often need $n$ equations?”

</div>

<!-- PDF p. 2 is the main agenda. Seminar.pptx slide 3 and Canva p. 2 include the n-unknowns question instead of the PDF's special-cases item. -->

---

<div class="eyebrow">Lecture 1 · Row picture</div>

# Each row draws a line or plane

A **row picture** draws each equation as a geometric shape. Two-variable equations draw lines; three-variable equations draw planes. A solution lies in every shape at once.

<div class="source-equation">

$$\begin{aligned}2x-y&=0\\-x+2y&=3\end{aligned}\qquad\Longleftrightarrow\qquad \underbrace{\begin{bmatrix}2&-1\\-1&2\end{bmatrix}}_A\underbrace{\begin{bmatrix}x\\y\end{bmatrix}}_{\mathbf{x}}=\underbrace{\begin{bmatrix}0\\3\end{bmatrix}}_{\mathbf{b}}$$

</div>

<div class="takeaway">

The two lines intersect at **$(x,y)=(1,2)$**.

</div>

<!-- PDF pp. 3–5; Seminar.pptx slides 4–6. -->

---

<div class="eyebrow">Lecture 1 · Row picture</div>

# See the common intersection

<div class="cols wide-left"><div><LinearPlot mode="rows" /></div><div>

$$\begin{aligned}2(1)-2&=0\\-(1)+2(2)&=3\end{aligned}$$

The point $(1,2)$ satisfies both equations. Each row is a constraint; their intersection is the answer.
</div></div>

<!-- PDF p. 5; Seminar.pptx slide 6. The diagram plots the exact two source equations. -->

---

<div class="eyebrow">Lecture 1 · Source-aligned animation</div>

# The row intersection forms

<div class="film-wide"><MathFilm src="/animations/RowIntersection.mp4" poster="/animations/RowIntersection.jpg" caption="The source equations 2x − y = 0 and −x + 2y = 3 meet at (1, 2)." /></div>

<!-- The animation formulas match PDF pp. 4–5 and Seminar.pptx slides 5–6. -->

---

<div class="eyebrow">Lecture 1 · Row picture in 3D</div>

# Three planes meet at one point

<div class="cols"><div>

$$\begin{aligned}2x-y&=0\\-x+2y-z&=-1\\-3y+4z&=4\end{aligned}$$

The common point is $(0,0,1)$.
</div><div class="math-small">

$$\begin{bmatrix}2&-1&0\\-1&2&-1\\0&-3&4\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}0\\-1\\4\end{bmatrix}$$

At $(0,0,1)$, the left side equals $\mathbf b$.
</div></div>

<!-- PDF pp. 6–7; Seminar.pptx slide 7. -->

---

<div class="eyebrow">Lecture 1 · Source-aligned animation</div>

# The three-plane row picture

<div class="film-wide"><MathFilm src="/animations/ThreePlaneIntersection.mp4" poster="/animations/ThreePlaneIntersection.jpg" caption="The three source planes share the solution (0, 0, 1)." /></div>

<!-- The source scene uses the same A, b, and solution as PDF pp. 6–7. -->

---

<div class="eyebrow">Lecture 1 · Column picture</div>

# Unknowns become vector weights

A **column picture** scales each column of $A$ and adds the results. The weighted sum must reach $\mathbf b$.

$$x\begin{bmatrix}2\\-1\end{bmatrix}+y\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}0\\3\end{bmatrix}$$

<div class="takeaway">

Here $x=1$ and $y=2$: $\begin{bmatrix}2\\-1\end{bmatrix}+2\begin{bmatrix}-1\\2\end{bmatrix}=\begin{bmatrix}0\\3\end{bmatrix}$.

</div>

<!-- PDF pp. 8–11; Seminar.pptx slides 8–11. -->

---

<div class="eyebrow">Lecture 1 · Column picture</div>

# Visualize the vector sum

<div class="cols wide-left"><div><VectorCombination /></div><div>

$$\mathbf a_1=\begin{bmatrix}2\\-1\end{bmatrix},\quad \mathbf a_2=\begin{bmatrix}-1\\2\end{bmatrix}$$

$$\mathbf a_1+2\mathbf a_2=\mathbf b$$

The same solution $(x,y)=(1,2)$ now tells us how much of each vector to use.
</div></div>

<!-- PDF pp. 9–11; Seminar.pptx slides 9–11. -->

---

<div class="eyebrow">Lecture 1 · Source-aligned animation</div>

# Build the column combination

<div class="film-wide"><MathFilm src="/animations/ColumnCombination.mp4" poster="/animations/ColumnCombination.jpg" caption="One copy of (2, −1) and two copies of (−1, 2) add to (0, 3)." /></div>

<!-- Source: PDF pp. 9–11. -->

---

<div class="eyebrow">Lecture 1 · Columns in 3D</div>

# The same matrix, viewed by columns

$$x\begin{bmatrix}2\\-1\\0\end{bmatrix}+y\begin{bmatrix}-1\\2\\-3\end{bmatrix}+z\begin{bmatrix}0\\-1\\4\end{bmatrix}=\begin{bmatrix}0\\-1\\4\end{bmatrix}$$

Since the target is the third column, the weights are **$(x,y,z)=(0,0,1)$**.

<div class="note">

In matrix form, this is still $A\mathbf{x}=\mathbf{b}$ with the same $A$ and $\mathbf b$ as the three-plane row picture.

</div>

<!-- PDF pp. 11–12; Seminar.pptx slide 12. -->

---

<div class="eyebrow">Lecture 1 · Source-aligned animation</div>

# The 3D column combination

<div class="film-wide"><MathFilm src="/animations/ThreeColumnCombination.mp4" poster="/animations/ThreeColumnCombination.jpg" caption="The third source column already equals the target vector b." /></div>

<!-- Source: PDF pp. 11–12. -->

---

<div class="eyebrow">Lecture 1 · Questions</div>

# What can the columns reach?

- If the columns supply independent directions, their combinations may fill the whole target space.
- If a column repeats a direction, the reachable set can be smaller.
- Solving $A\mathbf{x}=\mathbf b$ asks whether $\mathbf b$ lies in the span of the columns.

<div class="source-equation">

$$\mathbf b\in\operatorname{span}\{\mathbf a_1,\ldots,\mathbf a_n\}\quad\Longleftrightarrow\quad A\mathbf{x}=\mathbf b\text{ has a solution.}$$

</div>

<!-- PDF pp. 13–15; Seminar.pptx slide 13. -->

---

<div class="eyebrow">Lecture 1 · Equation count</div>

# Why do $n$ unknowns often need $n$ equations?

Each independent equation can remove one degree of freedom. For a **unique** answer in $n$ unknowns, we need $n$ independent constraints.

<div class="case-grid"><div class="case-card"><strong>One solution</strong><br>2x − y = 0<br>−x + 2y = 3</div><div class="case-card"><strong>Infinitely many</strong><br>2x − y = 1<br>4x − 2y = 2</div><div class="case-card"><strong>No solution</strong><br>2x − y = 1<br>4x − 2y = 3</div></div>

<div class="small">

Having $n$ equations alone does not guarantee a unique solution; independence and consistency matter.

</div>

<!-- Seminar.pptx slide 14. The source itself notes that n equations need not guarantee one answer. PDF pp. 16–18 covers the special cases. -->

---

<div class="eyebrow">Lecture 1 · Special cases</div>

# How can the system go wrong?

| Geometry | Algebra | Solution set |
| :-- | :-- | :-- |
| Lines cross once | Independent, consistent rows | One point |
| Lines coincide | Dependent, consistent rows | Infinitely many points |
| Lines are parallel and distinct | Inconsistent rows | No point |

<div class="takeaway">

The row picture shows intersections. The column picture asks whether $\mathbf b$ is reachable.

</div>

<!-- PDF pp. 16–18; Seminar.pptx slide 14. -->

---

<div class="lecture-divider"><div class="eyebrow">Lecture 02</div>

# Elimination with matrices

<div class="lecture-question">

Use row operations to uncover pivots and solve a system.

</div></div>

<!-- Source: Seminar.pptx slides 19–31. -->

---

<div class="eyebrow">Lecture 2 · Row elimination</div>

# Start with the augmented matrix

$$\begin{aligned}x+2y+z&=2\\3x+8y+z&=12\\4y+z&=2\end{aligned}$$

$$[A\mid\mathbf b]=\left[\begin{array}{ccc|c}1&2&1&2\\3&8&1&12\\0&4&1&2\end{array}\right]$$

Elimination replaces a row with a combination of rows. The solution stays the same.

<!-- Seminar.pptx slides 21–22. -->

---

<div class="eyebrow">Lecture 2 · Elimination steps</div>

# Clear entries below each pivot

$$\text{Start: }\left[\begin{array}{ccc|c}1&2&1&2\\3&8&1&12\\0&4&1&2\end{array}\right]$$

$$R_2\leftarrow R_2-3R_1:\quad\left[\begin{array}{ccc|c}1&2&1&2\\0&2&-2&6\\0&4&1&2\end{array}\right]$$

$$R_3\leftarrow R_3-2R_2:\quad\left[\begin{array}{ccc|c}1&2&1&2\\0&2&-2&6\\0&0&5&-10\end{array}\right]$$

The coefficient matrix is now **upper triangular**; the pivots are $1,2,5$.

<!-- Seminar.pptx slide 22. -->

---

<div class="eyebrow">Lecture 2 · Back substitution</div>

# Solve from the bottom row upward

$$\begin{aligned}5z&=-10&&\Rightarrow z=-2\\2y-2z&=6&&\Rightarrow y=1\\x+2y+z&=2&&\Rightarrow x=2\end{aligned}$$

<div class="source-equation">

$$\boxed{\mathbf{x}=\begin{bmatrix}2\\1\\-2\end{bmatrix}}\qquad
\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}\begin{bmatrix}2\\1\\-2\end{bmatrix}=\begin{bmatrix}2\\12\\2\end{bmatrix}$$

</div>

<!-- Seminar.pptx slides 22 and 24. -->

---

<div class="eyebrow">Lecture 2 · Failure case</div>

# A zero row can reveal inconsistency

Change the last equation to $4y-4z=2$. The same elimination gives

$$\left[\begin{array}{ccc|c}1&2&1&2\\0&2&-2&6\\0&0&0&-10\end{array}\right].$$

The final row says $0=-10$, which is impossible. **This system has no solution.**

<!-- Seminar.pptx slide 23. -->

---

<div class="eyebrow">Lecture 2 · Matrix multiplication</div>

# A matrix acts on a column vector

$$A=\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix},\qquad\mathbf v=\begin{bmatrix}1\\2\\3\end{bmatrix}$$

$$A\mathbf v=1\begin{bmatrix}1\\3\\0\end{bmatrix}+2\begin{bmatrix}2\\8\\4\end{bmatrix}+3\begin{bmatrix}1\\1\\1\end{bmatrix}
=\begin{bmatrix}8\\22\\11\end{bmatrix}$$

A **row vector times a matrix** combines rows:

$$\begin{bmatrix}1&2&3\end{bmatrix}\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}=\begin{bmatrix}7&30&6\end{bmatrix}.$$

<!-- Seminar.pptx slides 25–26. The row-vector result is copied from the source. -->

---

<div class="eyebrow">Lecture 2 · Elimination matrices</div>

# Row operations can be matrix multiplication

$$E_{21}=\begin{bmatrix}1&0&0\\-3&1&0\\0&0&1\end{bmatrix},\qquad
E_{32}=\begin{bmatrix}1&0&0\\0&1&0\\0&-2&1\end{bmatrix}$$

$$E_{32}E_{21}A=U,\qquad
U=\begin{bmatrix}1&2&1\\0&2&-2\\0&0&5\end{bmatrix}.$$

The **rightmost** matrix acts first: $E_{21}$ clears below the first pivot, then $E_{32}$ clears below the second. Order matters: $E_{32}E_{21}\ne E_{21}E_{32}$ in general.

<!-- Seminar.pptx slides 27–28. -->

---

<div class="lecture-divider"><div class="eyebrow">Lecture 03</div>

# Matrix multiplication and inverses

<div class="lecture-question">

Four views of $AB$ lead to the same product.

</div></div>

<!-- Source: Presentation2.pptx slides 1–12. -->

---

<div class="eyebrow">Lecture 3 · Four views</div>

# One product, four computations

Let $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ and $B=\begin{bmatrix}5&6\\7&8\end{bmatrix}$.

$$AB=\begin{bmatrix}19&22\\43&50\end{bmatrix}.$$

<div class="four-grid"><div><strong>Entries</strong><br>Row of A · column of B</div><div><strong>Columns</strong><br>A times each column of B</div><div><strong>Rows</strong><br>Rows of A combine rows of B</div><div><strong>Outer products</strong><br>Columns of A × rows of B</div></div>

<!-- Presentation2.pptx slides 2–6. -->

---

<div class="eyebrow">Lecture 3 · Dot products</div>

# Each entry is row times column

$$c_{ij}=\sum_k a_{ik}b_{kj}.$$

$$\begin{bmatrix}\color{#246a9c}{1}&\color{#246a9c}{2}\\3&4\end{bmatrix}
\begin{bmatrix}\color{#c15b35}{5}&6\\\color{#c15b35}{7}&8\end{bmatrix}
\Rightarrow c_{11}=1(5)+2(7)=19.$$

Similarly, $c_{12}=22$, $c_{21}=43$, and $c_{22}=50$.

<!-- Presentation2.pptx slides 3–4. -->

---

<div class="eyebrow">Lecture 3 · Columns and rows</div>

# Matrix multiplication as combinations

<div class="cols"><div>

**By columns**

$$AB=\left[\,A\mathbf b_1\quad A\mathbf b_2\,\right]$$

$$A\begin{bmatrix}5\\7\end{bmatrix}=5\begin{bmatrix}1\\3\end{bmatrix}+7\begin{bmatrix}2\\4\end{bmatrix}=\begin{bmatrix}19\\43\end{bmatrix}$$
</div><div>

**By rows**

$$\operatorname{row}_i(AB)=\operatorname{row}_i(A)B$$

$$\begin{bmatrix}1&2\end{bmatrix}B=1\begin{bmatrix}5&6\end{bmatrix}+2\begin{bmatrix}7&8\end{bmatrix}=\begin{bmatrix}19&22\end{bmatrix}$$
</div></div>

<!-- Presentation2.pptx slide 5. -->

---

<div class="eyebrow">Lecture 3 · Outer products</div>

# Add column × row pieces

$$AB=\begin{bmatrix}1\\3\end{bmatrix}\begin{bmatrix}5&6\end{bmatrix}+
\begin{bmatrix}2\\4\end{bmatrix}\begin{bmatrix}7&8\end{bmatrix}$$

$$=\begin{bmatrix}5&6\\15&18\end{bmatrix}+
\begin{bmatrix}14&16\\28&32\end{bmatrix}=
\begin{bmatrix}19&22\\43&50\end{bmatrix}.$$

<div class="note">

The source's rectangular example uses $\begin{bmatrix}1\\2\\3\end{bmatrix}\begin{bmatrix}1&3\end{bmatrix}=\begin{bmatrix}1&3\\2&6\\3&9\end{bmatrix}$.

</div>

<!-- Presentation2.pptx slide 6. The source labels its rectangular example in the wrong order; the displayed calculation is column times row. -->

---

<div class="eyebrow">Lecture 3 · Inverse</div>

# An inverse undoes a square matrix

$$AA^{-1}=A^{-1}A=I.$$

For $A=\begin{bmatrix}a&b\\c&d\end{bmatrix}$, an inverse exists when $ad-bc\ne0$:

$$A^{-1}=\frac1{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}.$$

For $\begin{bmatrix}3&1\\4&2\end{bmatrix}$, the determinant is $2$, so the inverse is $\frac12\begin{bmatrix}2&-1\\-4&3\end{bmatrix}$.

<!-- Presentation2.pptx slide 7. -->

---

<div class="eyebrow">Lecture 3 · Gauss–Jordan</div>

# Build the inverse beside the identity

For $A=\begin{bmatrix}1&3\\2&5\end{bmatrix}$, row-reduce $[A\mid I]$:

$$\text{Start: }\left[\begin{array}{cc|cc}1&3&1&0\\2&5&0&1\end{array}\right]$$

$$R_2\leftarrow R_2-2R_1:\quad\left[\begin{array}{cc|cc}1&3&1&0\\0&-1&-2&1\end{array}\right]$$

$$R_2\leftarrow-R_2,\;R_1\leftarrow R_1-3R_2:\quad\left[\begin{array}{cc|cc}1&0&-5&3\\0&1&2&-1\end{array}\right]$$

Thus $A^{-1}=\begin{bmatrix}-5&3\\2&-1\end{bmatrix}$.

<!-- Presentation2.pptx slides 8–9. -->

---

<div class="eyebrow">Lecture 3 · Source code</div>

# Compute the source examples in MATLAB

```matlab
A = [1 2; 3 4];
B = [5 6; 7 8];
C = A * B;        % [19 22; 43 50]

D = [1 3; 2 5];
D_inv = inv(D);   % [-5 3; 2 -1]
```

Matrix multiplication models successive linear transformations; inverses reverse an invertible transformation. The PowerPoint lists graphics, the Hill cipher, and neural networks as applications.

<!-- Presentation2.pptx slides 10–12. This code uses the exact matrices and results displayed in that source. -->

---

<div class="lecture-divider"><div class="eyebrow">Lecture 05</div>

# Permutations, transposes, and vector spaces

<div class="lecture-question">

Reorder rows, flip matrices, and test whether a set is a space.

</div></div>

<!-- Source: Lecture5.pptx slides 1–8. -->

---

<div class="eyebrow">Lecture 5 · Permutation</div>

# Swap a zero pivot into place

$$A=\begin{bmatrix}0&1&2\\1&2&3\\2&6&9\end{bmatrix},\quad
P=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},\quad
PA=\begin{bmatrix}1&2&3\\0&1&2\\2&6&9\end{bmatrix}.$$

$P$ is the identity with its first two rows swapped. A permutation matrix rearranges rows; $P^{-1}=P^T$.

For $n$ rows, there are $n!$ possible row permutations.

<!-- Lecture5.pptx slides 3–4. -->

---

<div class="eyebrow">Lecture 5 · PA = LU</div>

# Eliminate after the row swap

From $PA$, apply $R_3\leftarrow R_3-2R_1$ and then $R_3\leftarrow R_3-2R_2$.

$$L=\begin{bmatrix}1&0&0\\0&1&0\\2&2&1\end{bmatrix},\qquad
U=\begin{bmatrix}1&2&3\\0&1&2\\0&0&-1\end{bmatrix}.$$

<div class="source-equation">

$$\boxed{PA=LU}$$

</div>

The two multipliers $2$ appear below the diagonal of $L$.

<!-- Lecture5.pptx slide 4. -->

---

<div class="eyebrow">Lecture 5 · Transpose</div>

# Rows become columns

$$A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}\quad\Longrightarrow\quad
A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}.$$

Entry $(i,j)$ moves to $(j,i)$: $(A^T)_{ij}=A_{ji}$.

A square matrix is **symmetric** when $A=A^T$.

<!-- Lecture5.pptx slide 5. -->

---

<div class="eyebrow">Lecture 5 · Symmetry</div>

# $R^TR$ is symmetric

$$R=\begin{bmatrix}1&2\\3&0\\0&4\end{bmatrix},\qquad
R^TR=\begin{bmatrix}1&3&0\\2&0&4\end{bmatrix}\begin{bmatrix}1&2\\3&0\\0&4\end{bmatrix}
=\begin{bmatrix}10&2\\2&20\end{bmatrix}.$$

The off-diagonal entries match. More generally, $(R^TR)^T=R^TR$.

<!-- Lecture5.pptx slide 6. -->

---

<div class="eyebrow">Lecture 5 · Vector spaces</div>

# A space stays closed under combinations

A vector space contains the zero vector and stays inside the set when we **add** its vectors or **scale** them.

$$\mathbf u,\mathbf v\in V,\quad a,b\in\mathbb R\quad\Longrightarrow\quad a\mathbf u+b\mathbf v\in V.$$

$\mathbb R^2$ passes the test. The first quadrant $\{(x,y):x\ge0,\ y\ge0\}$ fails: $-1(3,2)=(-3,-2)$ leaves it.

<!-- Lecture5.pptx slides 7–8. -->

---

<div class="lecture-divider"><div class="eyebrow">Lecture 09</div>

# Independence, basis, and dimension

<div class="lecture-question">

How many independent directions are there, and what space do they span?

</div></div>

<!-- Source: second Canva deck, pp. 1–26. Template pages 27–29 are excluded. -->

---

<div class="eyebrow">Lecture 9 · Linear independence</div>

# Only the zero combination gives zero

Vectors $\mathbf v_1,\ldots,\mathbf v_n$ are **linearly independent** if

$$c_1\mathbf v_1+\cdots+c_n\mathbf v_n=\mathbf0$$

forces $c_1=\cdots=c_n=0$.

They are **dependent** if some nonzero coefficient vector satisfies the same equation. Then at least one vector can be built from the others.

<!-- Canva Lecture 9 pp. 5–8. Canva p. 7 has a wording error: dependence requires a nontrivial combination, not “no vector” being a combination. -->

---

<div class="eyebrow">Lecture 9 · Geometry</div>

# Independent directions span more

<div class="cols"><div class="geometry-card"><strong>Independent pair</strong>

Two nonparallel vectors in $\mathbb R^3$ span a **plane** through the origin.

$$\operatorname{span}\{\mathbf v_1,\mathbf v_2\}=\{c_1\mathbf v_1+c_2\mathbf v_2\}$$
</div><div class="geometry-card"><strong>Dependent pair</strong>

Parallel vectors supply only one direction. Their span is a **line** through the origin.

$$\operatorname{span}\{\mathbf v,2\mathbf v\}=\{c\mathbf v\}$$
</div></div>

<!-- Canva Lecture 9 p. 9. -->

---

<div class="eyebrow">Lecture 9 · Worked example</div>

# The third vector repeats two directions

$$\mathbf v_1=\begin{bmatrix}3\\2\\5\end{bmatrix},\quad
\mathbf v_2=\begin{bmatrix}4\\7\\2\end{bmatrix},\quad
\mathbf v_3=\begin{bmatrix}7\\9\\7\end{bmatrix}.$$

$$\boxed{\mathbf v_3=\mathbf v_1+\mathbf v_2}$$

So $-\mathbf v_1-\mathbf v_2+\mathbf v_3=\mathbf0$ is a nontrivial dependence relation.

<!-- Canva Lecture 9 pp. 10–13. -->

---

<div class="eyebrow">Lecture 9 · Matrix of columns</div>

# Put the vectors into one matrix

$$A=\begin{bmatrix}3&4&7\\2&7&9\\5&2&7\end{bmatrix}
=\left[\,\mathbf v_1\ \mathbf v_2\ \mathbf v_3\,\right].$$

The dependence relation becomes a nullspace equation:

$$A\begin{bmatrix}-1\\-1\\1\end{bmatrix}=\mathbf0.$$

Because the nullspace contains a nonzero vector, the three columns are dependent.

<!-- Canva Lecture 9 pp. 13–17. -->

---

<div class="eyebrow">Lecture 9 · Pivots and free columns</div>

# Row reduction reveals rank two

$$A\sim\operatorname{rref}(A)=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}.$$

Columns 1 and 2 are pivot columns. Column 3 is free and equals the sum of the first two columns.

$$\operatorname{rank}(A)=2,\qquad n-r=3-2=1.$$

The nullspace has one free direction, generated by $(-1,-1,1)^T$.

<!-- Canva Lecture 9 pp. 14–19. -->

---

<div class="eyebrow">Lecture 9 · Basis</div>

# Independent and spanning

A **basis** is a set of vectors that is linearly independent and spans the space.

For this matrix, the pivot columns of the **original** $A$ form a basis of its column space:

$$\boxed{\operatorname{basis}(C(A))=\left\{\begin{bmatrix}3\\2\\5\end{bmatrix},\begin{bmatrix}4\\7\\2\end{bmatrix}\right\}.}$$

The third column adds no new direction.

<!-- Canva Lecture 9 pp. 20–21. -->

---

<div class="eyebrow">Lecture 9 · Dimension</div>

# Count the basis vectors

The **dimension** of a space is the number of vectors in any basis of that space.

$$\dim C(A)=\operatorname{rank}(A)=2,\qquad
\dim N(A)=n-r=1.$$

The two pivot columns span a plane in $\mathbb R^3$. They form a basis for that plane, **not** for all of $\mathbb R^3$.

<!-- Canva Lecture 9 pp. 22–24. -->

---

<div class="eyebrow">Lecture 9 · Source code</div>

# Check dependence with SymPy

```python
from sympy import Matrix

A = Matrix([[3, 4, 7], [2, 7, 9], [5, 2, 7]])
n_vectors = A.shape[1]
rank = A.rank()
print("Number of vectors:", n_vectors)  # 3
print("Rank:", rank)                  # 2
print("Linearly independent?", rank == n_vectors)  # False
print("Determinant:", A.det())        # 0
for relation in A.nullspace():
    print("Dependency coefficients:", relation.T)  # [-1 -1 1]
```

<!-- Canva Lecture 9 p. 25. The code and output match the source example. -->

---

<div class="eyebrow">Lecture 9 · Summary</div>

# The four ideas fit together

| Idea | Test or count |
| :-- | :-- |
| **Independence** | $N(A)=\{\mathbf0\}$ for the columns of $A$ |
| **Spanning** | All combinations of columns give $C(A)$ |
| **Basis** | Independent vectors that span the chosen space |
| **Dimension** | $\dim C(A)=r$ and $\dim N(A)=n-r$ |

<div class="takeaway">

The example has three columns, two independent directions, and one dependence relation.

</div>

<!-- Canva Lecture 9 p. 26. N(A) = {0} makes the source's shorthand N(A) = 0 precise. -->

---

# Source files and comparison

- **Lecture 1:** PDF pages 1–18, first Canva deck, and `Seminar.pptx` slides 2–18. The equations and examples agree; their contents pages differ.
- **Lecture 2:** `Seminar.pptx` slides 19–31.
- **Lecture 3:** `Presentation2.pptx` slides 1–12.
- **Lecture 5:** `Lecture5.pptx` slides 1–8.
- **Lecture 9:** second Canva deck pages 1–26. There is no corresponding local PDF or PowerPoint.

<div class="small">

Unrelated planner-template pages 19–28 of the Lecture 1 PDF and blank/template ending pages in Canva were left out.

</div>

<!-- Source reconciliation as of 2026-11-17. -->
