---
layout: "native"
lecture: 5
title: "Permutations, transposes and vector spaces"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 1
class: "native-cover"
routeAlias: "lecture-5"
section: true
---

# Permutations, Transposes, and Vector Spaces

## Lecture 5

Linear Algebra

<!-- Rebuilt as native Slidev content from Lecture5, original page 1. -->

---
layout: "native"
lecture: 5
title: "Contents"
clicks: 4
sourceDeck: "Lecture5"
sourceSlide: 2
---

# Contents

<v-clicks>

1. Permutations and PA = LU.
2. Transposes and symmetric matrices.
3. Vector spaces and subspaces.
4. The column space C(A).

</v-clicks>

<!-- Rebuilt as native Slidev content from Lecture5, original page 2. -->

---
layout: "native"
lecture: 5
title: "Permutation matrices"
clicks: 3
sourceDeck: "Lecture5"
sourceSlide: 3
---

# Permutation Matrices

Elimination may need a row swap when a pivot candidate is zero or too small.

$$\boxed{PA=LU}$$

<v-clicks>

- P is formed by reordering the rows of the identity matrix.
- For n rows, there are n! possible permutations.
- A permutation matrix satisfies $P^{-1}=P^T$ and $P^TP=I$.

</v-clicks>

<!-- Rebuilt as native Slidev content from Lecture5, original page 3. -->

---
layout: "native"
lecture: 5
title: "A row swap before elimination"
clicks: 2
sourceDeck: "Lecture5"
sourceSlide: 4
class: "compact"
---

# A Row Swap Before Elimination

$$A=\begin{bmatrix}0&1&2\\1&2&3\\2&6&9\end{bmatrix},\quad P=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},\quad PA=\begin{bmatrix}1&2&3\\0&1&2\\2&6&9\end{bmatrix}$$

<div v-click="1">

Use $R_3\leftarrow R_3-2R_1$, then $R_3\leftarrow R_3-2R_2$:

$$L=\begin{bmatrix}1&0&0\\0&1&0\\2&2&1\end{bmatrix},\qquad U=\begin{bmatrix}1&2&3\\0&1&2\\0&0&-1\end{bmatrix}$$

</div>

<div v-click="2" class="native-callout">The original factors satisfy **PA = LU**.</div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 4. -->

---
layout: "native"
lecture: 5
title: "Transposes and symmetric matrices"
clicks: 1
sourceDeck: "Lecture5"
sourceSlide: 5
---

# Transposes and Symmetric Matrices

Rows become columns:

$$A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}\quad\Longrightarrow\quad A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}$$

<div v-click="1">

A square matrix is **symmetric** when $S^T=S$:

$$S=\begin{bmatrix}1&7&5\\7&2&9\\5&9&3\end{bmatrix}.$$

</div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 5. -->

---
layout: "native"
lecture: 5
title: "Making a symmetric matrix"
clicks: 2
sourceDeck: "Lecture5"
sourceSlide: 6
class: "compact"
---

# Making a Symmetric Matrix

$$R=\begin{bmatrix}1&2\\3&0\\0&4\end{bmatrix},\qquad R^T=\begin{bmatrix}1&3&0\\2&0&4\end{bmatrix}$$

<div v-click="1">

$$R^TR=\begin{bmatrix}1^2+3^2+0^2&1(2)+3(0)+0(4)\\2(1)+0(3)+4(0)&2^2+0^2+4^2\end{bmatrix}=\begin{bmatrix}10&2\\2&20\end{bmatrix}$$

</div>

<div v-click="2" class="native-callout">The off-diagonal entries match. In general, $(R^TR)^T=R^TR$.</div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 6. -->

---
layout: "native"
lecture: 5
title: "Python: the symmetry check"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 7
---

# Python: The Symmetry Check

<div class="native-code-grid"><div>

```python
import numpy as np
R = np.array([[1, 2],
              [3, 0],
              [0, 4]], dtype=float)
RT_R = R.T @ R
is_symmetric = np.allclose(RT_R, RT_R.T)
print(RT_R)
print("Is symmetric?:", is_symmetric)
```

</div><NativeOutput :lines="['[[10.  2.]', ' [ 2. 20.]]', '', 'Is symmetric?: True']" /></div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 7. -->

---
layout: "native"
lecture: 5
title: "Vector spaces"
clicks: 3
sourceDeck: "Lecture5"
sourceSlide: 8
---

# Vector Spaces

A vector space stays inside the set under vector addition and scalar multiplication.

$$\mathbf u,\mathbf v\in V,\ a,b\in\mathbb R\quad\Longrightarrow\quad a\mathbf u+b\mathbf v\in V.$$

<v-clicks>

- Add two vectors: the sum stays in the space.
- Scale a vector: every real scalar multiple stays in the space.
- Every vector space contains the zero vector.

</v-clicks>

<!-- Rebuilt as native Slidev content from Lecture5, original page 8. -->

---
layout: "native"
lecture: 5
title: "Examples of vector spaces"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 9
---

# Examples of Vector Spaces

<div class="native-three"><div>

## ℝ²

All two-dimensional vectors.

$$\begin{bmatrix}x\\y\end{bmatrix}$$

</div><div>

## ℝ³

All three-dimensional vectors.

$$\begin{bmatrix}x\\y\\z\end{bmatrix}$$

</div><div>

## ℝⁿ

All column vectors with n real components.

$$\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}$$

</div></div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 9. -->

---
layout: "native"
lecture: 5
title: "Subspaces"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 10
---

# Subspaces

A subspace is a vector space inside a larger vector space. It contains zero and is closed under addition and scalar multiplication.

<div class="native-columns"><div>

## Subspaces of ℝ²

- The whole plane.
- Any line through the origin.
- The zero vector alone.

</div><div>

## Subspaces of ℝ³

- All of ℝ³.
- Any plane through the origin.
- Any line through the origin.
- The zero vector alone.

</div></div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 10. -->

---
layout: "native"
lecture: 5
title: "The column space"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 11
---

# The Column Space C(A)

<div class="native-columns diagram-wide"><div>

The column space contains **all linear combinations** of the columns of A.

$$C(A)=\{A\mathbf x:\mathbf x\in\mathbb R^n\}$$

For two independent columns in ℝ³, their combinations form a plane through the origin.

</div><NativeMathDiagram kind="span3" /></div>

<!-- Rebuilt as native Slidev content from Lecture5, original page 11. -->
