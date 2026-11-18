---
layout: "native"
lecture: 3
title: "Matrix multiplication and inverses"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 1
class: "native-cover"
routeAlias: "lecture-3"
section: true
---

# Matrix Multiplication and Inverses

## Lecture 3

MIT 18.06 · Based on Gilbert Strang's lecture

<!-- Rebuilt as native Slidev content from Presentation2, original page 1. -->

---
layout: "native"
lecture: 3
title: "Roadmap"
clicks: 4
sourceDeck: "Presentation2"
sourceSlide: 2
---

# Roadmap

<v-clicks>

1. Four ways to compute a matrix product.
2. Inverse matrices.
3. Gauss–Jordan elimination.
4. MATLAB examples and applications.

</v-clicks>

<!-- Rebuilt as native Slidev content from Presentation2, original page 2. -->

---
layout: "native"
lecture: 3
title: "Four views of one matrix product"
clicks: 1
sourceDeck: "Presentation2"
sourceSlide: 3
---

# Four Views of One Matrix Product

$$A=\begin{bmatrix}1&2\\3&4\end{bmatrix},\qquad B=\begin{bmatrix}5&6\\7&8\end{bmatrix}$$

| View | Computation |
| --- | --- |
| Entries | Row of A dotted with a column of B |
| Columns | A times each column of B |
| Rows | Each row of A times B |
| Outer products | Sum of columns of A times rows of B |

<div v-click="1">

$$AB=\begin{bmatrix}19&22\\43&50\end{bmatrix}$$

</div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 3. -->

---
layout: "native"
lecture: 3
title: "Dot products"
clicks: 3
sourceDeck: "Presentation2"
sourceSlide: 4
---

# 1. Dot Products

$$c_{ij}=\sum_k a_{ik}b_{kj}$$

<div class="native-columns"><div>

$$c_{11}=1\cdot5+2\cdot7=19$$

<div v-click="1">

$$c_{12}=1\cdot6+2\cdot8=22$$

</div></div><div>

<div v-click="2">

$$c_{21}=3\cdot5+4\cdot7=43$$

</div><div v-click="3">

$$c_{22}=3\cdot6+4\cdot8=50$$

</div></div></div>

<div class="native-callout">A(m × n) times B(n × p) gives C(m × p).</div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 4. -->

---
layout: "native"
lecture: 3
title: "Columns and rows"
clicks: 2
sourceDeck: "Presentation2"
sourceSlide: 5
---

# 2 and 3. Columns and Rows

<div class="native-columns"><div>

## By columns

$$A\begin{bmatrix}5\\7\end{bmatrix}=5\begin{bmatrix}1\\3\end{bmatrix}+7\begin{bmatrix}2\\4\end{bmatrix}$$

<div v-click="1">

$$=\begin{bmatrix}19\\43\end{bmatrix}$$

</div></div><div>

## By rows

$$\begin{bmatrix}1&2\end{bmatrix}B=1\begin{bmatrix}5&6\end{bmatrix}+2\begin{bmatrix}7&8\end{bmatrix}$$

<div v-click="2">

$$=\begin{bmatrix}19&22\end{bmatrix}$$

</div></div></div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 5. -->

---
layout: "native"
lecture: 3
title: "Columns times rows"
clicks: 1
sourceDeck: "Presentation2"
sourceSlide: 6
class: "compact"
---

# 4. Columns Times Rows

An outer product multiplies a **column** by a **row**.

$$\begin{bmatrix}1\\2\\3\end{bmatrix}\begin{bmatrix}1&3\end{bmatrix}=\begin{bmatrix}1&3\\2&6\\3&9\end{bmatrix}$$

<div v-click="1">

$$AB=\begin{bmatrix}1\\3\end{bmatrix}\begin{bmatrix}5&6\end{bmatrix}+\begin{bmatrix}2\\4\end{bmatrix}\begin{bmatrix}7&8\end{bmatrix}$$

$$=\begin{bmatrix}5&6\\15&18\end{bmatrix}+\begin{bmatrix}14&16\\28&32\end{bmatrix}=\begin{bmatrix}19&22\\43&50\end{bmatrix}$$

</div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 6. -->

---
layout: "native"
lecture: 3
title: "The inverse matrix"
clicks: 1
sourceDeck: "Presentation2"
sourceSlide: 7
---

# The Inverse Matrix

$$AA^{-1}=A^{-1}A=I$$

A square matrix has an inverse exactly when its determinant is nonzero.

$$A=\begin{bmatrix}3&1\\4&2\end{bmatrix},\qquad \det A=3(2)-1(4)=2$$

<div v-click="1">

$$A^{-1}=\frac12\begin{bmatrix}2&-1\\-4&3\end{bmatrix}$$

</div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 7. -->

---
layout: "native"
lecture: 3
title: "Gauss–Jordan elimination"
clicks: 2
sourceDeck: "Presentation2"
sourceSlide: 8
---

# Gauss–Jordan Elimination

<div class="native-three"><div>

## Start

$$[A\mid I]$$

Place the identity beside A.

</div><div v-click="1">

## Row-reduce

Eliminate below and above each pivot. Apply each operation to both halves.

</div><div v-click="2">

## Finish

$$[I\mid A^{-1}]$$

The right half is the inverse.

</div></div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 8. -->

---
layout: "native"
lecture: 3
title: "Gauss–Jordan worked example"
clicks: 3
sourceDeck: "Presentation2"
sourceSlide: 9
---

# Gauss–Jordan Worked Example

$$A=\begin{bmatrix}1&3\\2&5\end{bmatrix}$$

<NativeMatrixSteps lesson="inverse" :augmented="2" />

<div v-click="3" class="native-callout">The inverse is A⁻¹ = [−5, 3; 2, −1]. Multiplying A by this inverse gives I.</div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 9. -->

---
layout: "native"
lecture: 3
title: "MATLAB: multiplication"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 10
---

# MATLAB: Multiplication

<div class="native-code-grid"><div>

```matlab
A = [1 2; 3 4];
B = [5 6; 7 8];
C = A * B
```

</div><NativeOutput :lines="['C =', '    19    22', '    43    50']" /></div>

The built-in matrix product gives the same result as all four views.

<!-- Rebuilt as native Slidev content from Presentation2, original page 10. -->

---
layout: "native"
lecture: 3
title: "MATLAB: inverse by row reduction"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 11
---

# MATLAB: Inverse by Row Reduction

<div class="native-code-grid"><div>

```matlab
A = [1 3; 2 5];
M = rref([A eye(2)]);
Ainv = M(:, 3:4)
A * Ainv
inv(A)
```

</div><NativeOutput :lines="['Ainv =', '    -5     3', '     2    -1', '', 'A * Ainv =', '     1     0', '     0     1']" /></div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 11. -->

---
layout: "native"
lecture: 3
title: "Applications"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 12
---

# Applications

<div class="native-three"><div>

## Neural networks

Weight matrices multiply feature vectors before nonlinear activations.

</div><div>

## Computer graphics

Transformation matrices rotate, scale and project coordinates.

</div><div>

## Hill cipher

Encryption multiplies the message vector by a key matrix. Decryption requires an invertible key.

</div></div>

<!-- Rebuilt as native Slidev content from Presentation2, original page 12. -->
