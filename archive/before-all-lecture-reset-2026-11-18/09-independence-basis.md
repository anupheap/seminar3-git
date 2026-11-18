---
layout: "native"
lecture: 9
title: "Independence, basis and dimension"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 1
class: "native-cover"
routeAlias: "lecture-9"
section: true
---

# Independence, Basis, and Dimension

## Lecture 9

Linear Algebra

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 1. -->

---
layout: "native"
lecture: 9
title: "What we will cover"
clicks: 3
sourceDeck: "CanvaLecture9"
sourceSlide: 2
---

# What We Will Cover

<v-clicks>

1. Linear independence and dependence.
2. Basis.
3. Dimension.

</v-clicks>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 2. -->

---
layout: "native"
lecture: 9
title: "Two vectors"
clicks: 1
sourceDeck: "CanvaLecture9"
sourceSlide: 3
---

# Two Vectors

$$\mathbf u=\begin{bmatrix}2\\3\end{bmatrix},\qquad \mathbf v=\begin{bmatrix}1\\4\end{bmatrix}$$

Can either vector be made by scaling the other?

<div v-click="1" class="native-callout">They point in different directions. Neither is a scalar multiple of the other.</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 3. -->

---
layout: "native"
lecture: 9
title: "Independent directions"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 4
---

# Independent Directions

<div class="native-columns"><div>

$$\mathbf u=\begin{bmatrix}2\\3\end{bmatrix},\qquad \mathbf v=\begin{bmatrix}1\\4\end{bmatrix}$$

The two nonparallel vectors span ℝ².

</div><NativeMathDiagram kind="independent" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 4. -->

---
layout: "native"
lecture: 9
title: "Linear independence"
clicks: 1
sourceDeck: "CanvaLecture9"
sourceSlide: 5
---

# Linear Independence

Vectors are linearly independent when no vector in the set is a linear combination of the others.

$$c_1\mathbf v_1+c_2\mathbf v_2+\cdots+c_n\mathbf v_n=\mathbf0$$

<div v-click="1">

Putting the vectors in columns gives:

$$A\mathbf c=\mathbf0.$$

</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 5. -->

---
layout: "native"
lecture: 9
title: "The zero combination"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 6
---

# The Zero Combination

For independent columns, the only solution of

$$A\mathbf c=\mathbf0$$

is

$$\boxed{c_1=c_2=\cdots=c_n=0}.$$

Every coefficient must be zero.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 6. -->

---
layout: "native"
lecture: 9
title: "Linear dependence"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 7
---

# Linear Dependence

A set is linearly dependent when **at least one vector can be written as a linear combination of the others**.

<div class="native-columns"><div>

$$\mathbf v_2=2\mathbf v_1$$

The second vector adds no new direction.

</div><NativeMathDiagram kind="dependent" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 7. -->

---
layout: "native"
lecture: 9
title: "A nonzero dependency relation"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 8
---

# A Nonzero Dependency Relation

Dependence means there is a coefficient vector c ≠ 0 such that

$$A\mathbf c=\mathbf0.$$

For example:

$$-2\mathbf v_1+\mathbf v_2=\mathbf0.$$

<div class="native-callout">The vectors sum to zero even though their coefficients are not all zero.</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 8. -->

---
layout: "native"
lecture: 9
title: "Independent or dependent?"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 9
---

# Independent or Dependent?

<div class="native-columns"><div>

## Independent

<NativeMathDiagram kind="independent" />

</div><div>

## Dependent

<NativeMathDiagram kind="dependent" />

</div></div>

<div class="native-small">Independent vectors supply different directions. Dependent vectors repeat a direction already available.</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 9. -->

---
layout: "native"
lecture: 9
title: "Three vectors: a question"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 10
---

# Three Vectors: A Question

<div class="native-columns"><div>

Does the third vector add a new independent direction?

Think about whether it can be reached by combining the first two.

</div><NativeMathDiagram kind="dependence3" :stage="0" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 10. -->

---
layout: "native"
lecture: 9
title: "The third vector is dependent"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 11
---

# The Third Vector Is Dependent

<div class="native-columns"><div>

$$\mathbf v_3=\mathbf v_1+\mathbf v_2$$

$$-\mathbf v_1-\mathbf v_2+\mathbf v_3=\mathbf0$$

The third vector adds no independent direction.

</div><NativeMathDiagram kind="dependence3" :stage="1" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 11. -->

---
layout: "native"
lecture: 9
title: "A linear combination"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 12
---

# A Linear Combination

$$c_1\mathbf v_1+c_2\mathbf v_2=\mathbf v_3$$

<div class="native-columns"><div>

Combine scaled vectors tip to tail. The resultant is a vector already in their span.

</div><NativeMathDiagram kind="dependence3" :stage="1" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 12. -->

---
layout: "native"
lecture: 9
title: "The numerical example"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 13
---

# Dependent or Independent?

$$\mathbf v_1=\begin{bmatrix}3\\2\\5\end{bmatrix},\qquad\mathbf v_2=\begin{bmatrix}4\\7\\2\end{bmatrix},\qquad\mathbf v_3=\begin{bmatrix}7\\9\\7\end{bmatrix}$$

Can you find a nonzero coefficient vector that makes their combination zero?

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 13. -->

---
layout: "native"
lecture: 9
title: "The dependence relation"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 14
---

# The Dependence Relation

$$\begin{bmatrix}3\\2\\5\end{bmatrix}+\begin{bmatrix}4\\7\\2\end{bmatrix}=\begin{bmatrix}7\\9\\7\end{bmatrix}$$

$$\boxed{-\mathbf v_1-\mathbf v_2+\mathbf v_3=\mathbf0}$$

The coefficient vector (−1, −1, 1) is nonzero, so the columns are dependent.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 14. -->

---
layout: "native"
lecture: 9
title: "Row reduction: the first pivot"
clicks: 2
sourceDeck: "CanvaLecture9"
sourceSlide: 15
---

# Row Reduction: The First Pivot

<NativeMatrixSteps lesson="dependence" :max-step="2" />

Each row operation preserves the solutions of Ac = 0.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 15. -->

---
layout: "native"
lecture: 9
title: "Row reduction: the second pivot"
clicks: 2
sourceDeck: "CanvaLecture9"
sourceSlide: 16
---

# Row Reduction: The Second Pivot

<NativeMatrixSteps lesson="dependence" :offset="2" :max-step="2" />

Clear below the first pivot, then scale the second row to make its pivot 1.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 16. -->

---
layout: "native"
lecture: 9
title: "A free column"
clicks: 1
sourceDeck: "CanvaLecture9"
sourceSlide: 17
---

# A Free Column

<NativeMatrixSteps lesson="dependence" :offset="4" :max-step="1" />

<div v-click="1" class="native-callout">The last row is zero. Column 3 has no pivot, so c₃ is a free variable and the columns are dependent.</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 17. -->

---
layout: "native"
lecture: 9
title: "Rank counts pivots"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 18
---

# Rank Counts Pivots

$$\begin{bmatrix}1&-3&-2\\0&1&1\\0&0&0\end{bmatrix}$$

There are two pivot positions:

$$\boxed{r=\operatorname{rank}(A)=2}.$$

The rank counts independent column directions.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 18. -->

---
layout: "native"
lecture: 9
title: "Counting free variables"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 19
---

# Counting Free Variables

The number of free columns is the number of columns minus the rank:

$$n-r=3-2=1.$$

<div class="native-callout">One free variable gives one independent nullspace direction. The nullspace is the set of coefficient vectors c satisfying Ac = 0.</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 19. -->

---
layout: "native"
lecture: 9
title: "Basis"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 20
---

# Basis

<div class="native-columns"><div>

A basis for a vector space satisfies both conditions:

1. The vectors are linearly independent.
2. They span the space.

</div><NativeMathDiagram kind="basis3" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 20. -->

---
layout: "native"
lecture: 9
title: "A basis of the column space"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 21
---

# A Basis of the Column Space

Take the pivot columns from the **original** matrix A:

$$\left\{\begin{bmatrix}3\\2\\5\end{bmatrix},\begin{bmatrix}4\\7\\2\end{bmatrix}\right\}.$$

They are independent and span every column of A. The third column is their sum.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 21. -->

---
layout: "native"
lecture: 9
title: "How many basis vectors?"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 22
---

# How Many Basis Vectors?

<div class="native-columns"><div>

## ℝ²

$$\left\{\begin{bmatrix}1\\0\end{bmatrix},\begin{bmatrix}0\\1\end{bmatrix}\right\}$$

Two independent directions.

</div><div>

## ℝ³

$$\left\{\begin{bmatrix}1\\0\\0\end{bmatrix},\begin{bmatrix}0\\1\\0\end{bmatrix},\begin{bmatrix}0\\0\\1\end{bmatrix}\right\}$$

Three independent directions.

</div></div>

<div class="native-callout">The number of vectors in any basis equals the dimension of that space.</div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 22. -->

---
layout: "native"
lecture: 9
title: "A basis for a plane, not all of R3"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 23
---

# A Basis for a Plane

<div class="native-columns"><div>

Two independent vectors in ℝ³ span a plane through the origin.

They form a basis for that plane, but not for all of ℝ³.

</div><NativeMathDiagram kind="span3" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 23. -->

---
layout: "native"
lecture: 9
title: "Dimension"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 24
---

# Dimension

The dimension of a space is the number of vectors in any basis for it.

$$\boxed{\dim C(A)=2,\qquad\dim N(A)=1}$$

For a matrix with n columns:

$$\operatorname{rank}(A)+\dim N(A)=n.$$

Here, $2+1=3$.

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 24. -->

---
layout: "native"
lecture: 9
title: "Python: independence and rank"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 25
class: "compact"
---

# Python: Independence and Rank

<div class="native-code-grid"><div>

```python
from sympy import Matrix
A = Matrix([[3, 4, 7],
            [2, 7, 9],
            [5, 2, 7]])
n_vectors = A.shape[1]
rank = A.rank()
print("Number of vectors:", n_vectors)
print("Rank:", rank)
print("Linearly independent?", rank == n_vectors)
```

</div><NativeOutput :lines="['Number of vectors: 3', 'Rank: 2', 'Linearly independent? False']" /></div>

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 25. -->

---
layout: "native"
lecture: 9
title: "Conclusion"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 26
---

# Conclusion

| Idea | Meaning |
| --- | --- |
| Independence | The only solution of Ac = 0 is c = 0 |
| Spanning | All combinations of columns give C(A) |
| Basis | Independent vectors that span the chosen space |
| Dimension | The number of basis vectors |

$$\dim C(A)=r,\qquad\dim N(A)=n-r.$$

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 26. -->

---
layout: "native"
lecture: 9
title: "Lecture 9 template page"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 27
class: "native-template"
---

<div class="native-blank" />

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 27. -->

---
layout: "native"
lecture: 9
title: "Lecture 9 template page"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 28
class: "native-template"
---

<div class="native-blank" />

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 28. -->

---
layout: "native"
lecture: 9
title: "Lecture 9 template page"
clicks: 0
sourceDeck: "CanvaLecture9"
sourceSlide: 29
class: "native-template"
---

<div class="native-blank" />

<!-- Rebuilt as native Slidev content from CanvaLecture9, original page 29. -->
