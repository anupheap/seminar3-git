---
layout: "native"
lecture: 2
title: "Elimination with matrices"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 19
class: "native-cover"
routeAlias: "lecture-2"
section: true
---

# Elimination with Matrices

## Lecture 2

Institute of Technology of Cambodia

MIT 18.06 Linear Algebra · Gilbert Strang

<!-- Rebuilt as native Slidev content from Seminar, original page 19. -->

---
layout: "native"
lecture: 2
title: "Learning Objectives"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 20
---

<NativeObjectives :items="['Row elimination', 'Back-substitution', 'Matrix multiplication', 'Elimination matrices']" />

<!-- Rebuilt as native Slidev content from Seminar, original page 20. -->

---
layout: "native"
lecture: 2
title: "Row elimination"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 21
---

# Row Elimination

<div class="native-columns"><div>

$$\begin{aligned}x+2y+z&=2\\3x+8y+z&=12\\4y+z&=2\end{aligned}$$

</div><div>

$$[A\mid b]=\left[\begin{array}{ccc|c}1&2&1&2\\3&8&1&12\\0&4&1&2\end{array}\right]$$

</div></div>

<div v-click="1" class="native-callout">Eliminate entries below the pivots to form an upper triangular matrix U. Apply every row operation to b as well.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 21. -->

---
layout: "native"
lecture: 2
title: "Elimination one row at a time"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 22
---

# Elimination One Row at a Time

<NativeMatrixSteps lesson="elimination" :augmented="3" />

<div v-click="2" class="native-callout">

The pivots are **1, 2, 5**. The coefficient matrix is upper triangular:

$$U=\begin{bmatrix}1&2&1\\0&2&-2\\0&0&5\end{bmatrix}.$$

</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 22. -->

---
layout: "native"
lecture: 2
title: "An inconsistent system"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 23
---

# An Inconsistent System

<NativeMatrixSteps lesson="failure" :augmented="3" />

<div v-click="2" class="native-callout">

$$\boxed{0=-10}$$

The contradiction proves that this system has **no solution**.

</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 23. -->

---
layout: "native"
lecture: 2
title: "Back-substitution"
clicks: 3
sourceDeck: "Seminar"
sourceSlide: 24
class: "compact"
---

# Back-Substitution

$$\left[\begin{array}{ccc|c}1&2&1&2\\0&2&-2&6\\0&0&5&-10\end{array}\right]$$

<div class="native-three"><div v-click="1">

## Last row

$$5z=-10\quad\Rightarrow\quad z=-2$$

</div><div v-click="2">

## Second row

$$2y-2(-2)=6\quad\Rightarrow\quad y=1$$

</div><div v-click="3">

## First row

$$x+2(1)-2=2\quad\Rightarrow\quad x=2$$

</div></div>

<div v-click="3" class="native-callout">The solution is (x, y, z) = **(2, 1, −2)**.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 24. -->

---
layout: "native"
lecture: 2
title: "Matrix times a column vector"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 25
---

# Matrix Times a Column Vector

$$\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}\begin{bmatrix}1\\2\\3\end{bmatrix}
=1\begin{bmatrix}1\\3\\0\end{bmatrix}+2\begin{bmatrix}2\\8\\4\end{bmatrix}+3\begin{bmatrix}1\\1\\1\end{bmatrix}$$

<div v-click="1">

$$=\begin{bmatrix}8\\22\\11\end{bmatrix}$$

</div>

<div class="native-callout">A matrix times a column vector is a weighted sum of the matrix's columns.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 25. -->

---
layout: "native"
lecture: 2
title: "Row vector times a matrix"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 26
---

# Row Vector Times a Matrix

$$\begin{bmatrix}1&2&3\end{bmatrix}\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}$$

<div v-click="1">

$$=1\begin{bmatrix}1&2&1\end{bmatrix}+2\begin{bmatrix}3&8&1\end{bmatrix}+3\begin{bmatrix}0&4&1\end{bmatrix}$$

</div><div v-click="2">

$$=\boxed{\begin{bmatrix}7&30&6\end{bmatrix}}$$

</div>

<div class="native-callout">A row vector times a matrix combines its rows.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 26. -->

---
layout: "native"
lecture: 2
title: "Elimination by matrix multiplication"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 27
class: "compact"
---

# Elimination by Matrix Multiplication

<div class="native-columns"><div>

## Subtract 3R₁ from R₂

$$E_{21}=\begin{bmatrix}1&0&0\\-3&1&0\\0&0&1\end{bmatrix}$$

<div v-click="1">

$$E_{21}A=\begin{bmatrix}1&2&1\\0&2&-2\\0&4&1\end{bmatrix}$$

</div></div><div>

## Subtract 2R₂ from R₃

$$E_{32}=\begin{bmatrix}1&0&0\\0&1&0\\0&-2&1\end{bmatrix}$$

<div v-click="2">

$$E_{32}(E_{21}A)=\begin{bmatrix}1&2&1\\0&2&-2\\0&0&5\end{bmatrix}$$

</div></div></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 27. -->

---
layout: "native"
lecture: 2
title: "Order and grouping matter"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 28
---

# Order and Grouping Matter

$$E_{32}(E_{21}A)=(E_{32}E_{21})A=U$$

<div v-click="1">

$$E_{32}E_{21}=\begin{bmatrix}1&0&0\\-3&1&0\\6&-2&1\end{bmatrix}$$

</div>

<div v-click="2" class="native-callout">Matrix multiplication is **associative**: we may change the grouping. It is generally **not commutative**: we cannot reverse the order.</div>

<div v-click="2">

$$E_{32}E_{21}\ne E_{21}E_{32}$$

</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 28. -->

---
layout: "native"
lecture: 2
title: "Review: pivots and triangular form"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 29
---

# Review: Pivots and Triangular Form

A pivot used in division must be **nonzero**. A zero pivot candidate may require a row swap.

Which matrix is upper triangular?

<div class="native-three"><div>

## A

$$\begin{bmatrix}1&0&0\\3&1&0\\0&0&1\end{bmatrix}$$

</div><div>

## B

$$\begin{bmatrix}1&2&1\\0&2&-2\\0&0&5\end{bmatrix}$$

</div><div>

## C

$$\begin{bmatrix}1&0&0\\1&2&0\\0&6&1\end{bmatrix}$$

</div></div>

<div v-click="1" class="native-callout">**B.** Every entry below the main diagonal is zero.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 29. -->

---
layout: "native"
lecture: 2
title: "Review: product dimensions"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 30
---

# Review: Product Dimensions

What is the result of a 3 × 3 matrix multiplying a 3 × 1 column vector?

$$\underbrace{A}_{3\times3}\underbrace{\mathbf x}_{3\times1}$$

<div v-click="1">

$$\boxed{A\mathbf x\text{ is a }3\times1\text{ column vector.}}$$

</div>

<div v-click="1" class="native-callout">The inner dimensions must agree. The outer dimensions give the shape of the result.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 30. -->
