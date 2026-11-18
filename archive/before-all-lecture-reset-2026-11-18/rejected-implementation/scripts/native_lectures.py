"""Authoritative native Slidev source. Original files are reference assets only."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DECKS = {}


def slide(number, title, body='', clicks=0, style=''):
    return dict(source=number, title=title, body=body.strip(), clicks=clicks, style=style)


# Lecture 1 is maintained by build-lecture1-native.py from the original objects.
# The rejected authored outline is retained only in archive/lecture1-before-faithful-reset-2026-11-18.
DECKS[1] = []

DECKS[2] = [
slide(19, 'Elimination with matrices', r'''
# Elimination with Matrices

## Lecture 2

Institute of Technology of Cambodia

MIT 18.06 Linear Algebra · Gilbert Strang
''',style='native-cover'),
slide(20, 'Learning Objectives', '''<NativeObjectives :items="['Row elimination', 'Back-substitution', 'Matrix multiplication', 'Elimination matrices']" />'''),
slide(21, 'Row elimination', r'''
# Row Elimination

<div class="native-columns"><div>

$$\begin{aligned}x+2y+z&=2\\3x+8y+z&=12\\4y+z&=2\end{aligned}$$

</div><div>

$$[A\mid b]=\left[\begin{array}{ccc|c}1&2&1&2\\3&8&1&12\\0&4&1&2\end{array}\right]$$

</div></div>

<div v-click="1" class="native-callout">Eliminate entries below the pivots to form an upper triangular matrix U. Apply every row operation to b as well.</div>
''',1),
slide(22, 'Elimination one row at a time', r'''
# Elimination One Row at a Time

<NativeMatrixSteps lesson="elimination" :augmented="3" />

<div v-click="2" class="native-callout">

The pivots are **1, 2, 5**. The coefficient matrix is upper triangular:

$$U=\begin{bmatrix}1&2&1\\0&2&-2\\0&0&5\end{bmatrix}.$$

</div>
''',2),
slide(23, 'An inconsistent system', r'''
# An Inconsistent System

<NativeMatrixSteps lesson="failure" :augmented="3" />

<div v-click="2" class="native-callout">

$$\boxed{0=-10}$$

The contradiction proves that this system has **no solution**.

</div>
''',2),
slide(24, 'Back-substitution', r'''
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
''',3, 'compact'),
slide(25, 'Matrix times a column vector', r'''
# Matrix Times a Column Vector

$$\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}\begin{bmatrix}1\\2\\3\end{bmatrix}
=1\begin{bmatrix}1\\3\\0\end{bmatrix}+2\begin{bmatrix}2\\8\\4\end{bmatrix}+3\begin{bmatrix}1\\1\\1\end{bmatrix}$$

<div v-click="1">

$$=\begin{bmatrix}8\\22\\11\end{bmatrix}$$

</div>

<div class="native-callout">A matrix times a column vector is a weighted sum of the matrix's columns.</div>
''',1),
slide(26, 'Row vector times a matrix', r'''
# Row Vector Times a Matrix

$$\begin{bmatrix}1&2&3\end{bmatrix}\begin{bmatrix}1&2&1\\3&8&1\\0&4&1\end{bmatrix}$$

<div v-click="1">

$$=1\begin{bmatrix}1&2&1\end{bmatrix}+2\begin{bmatrix}3&8&1\end{bmatrix}+3\begin{bmatrix}0&4&1\end{bmatrix}$$

</div><div v-click="2">

$$=\boxed{\begin{bmatrix}7&30&6\end{bmatrix}}$$

</div>

<div class="native-callout">A row vector times a matrix combines its rows.</div>
''',2),
slide(27, 'Elimination by matrix multiplication', r'''
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
''',2,'compact'),
slide(28, 'Order and grouping matter', r'''
# Order and Grouping Matter

$$E_{32}(E_{21}A)=(E_{32}E_{21})A=U$$

<div v-click="1">

$$E_{32}E_{21}=\begin{bmatrix}1&0&0\\-3&1&0\\6&-2&1\end{bmatrix}$$

</div>

<div v-click="2" class="native-callout">Matrix multiplication is **associative**: we may change the grouping. It is generally **not commutative**: we cannot reverse the order.</div>

<div v-click="2">

$$E_{32}E_{21}\ne E_{21}E_{32}$$

</div>
''',2),
slide(29, 'Review: pivots and triangular form', r'''
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
''',1),
slide(30, 'Review: product dimensions', r'''
# Review: Product Dimensions

What is the result of a 3 × 3 matrix multiplying a 3 × 1 column vector?

$$\underbrace{A}_{3\times3}\underbrace{\mathbf x}_{3\times1}$$

<div v-click="1">

$$\boxed{A\mathbf x\text{ is a }3\times1\text{ column vector.}}$$

</div>

<div v-click="1" class="native-callout">The inner dimensions must agree. The outer dimensions give the shape of the result.</div>
''',1),
]

DECKS[3] = [
slide(1, 'Matrix multiplication and inverses', r'''
# Matrix Multiplication and Inverses

## Lecture 3

MIT 18.06 · Based on Gilbert Strang's lecture
''',style='native-cover'),
slide(2, 'Roadmap', r'''
# Roadmap

<v-clicks>

1. Four ways to compute a matrix product.
2. Inverse matrices.
3. Gauss–Jordan elimination.
4. MATLAB examples and applications.

</v-clicks>
''',4),
slide(3, 'Four views of one matrix product', r'''
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
''',1),
slide(4, 'Dot products', r'''
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
''',3),
slide(5, 'Columns and rows', r'''
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
''',2),
slide(6, 'Columns times rows', r'''
# 4. Columns Times Rows

An outer product multiplies a **column** by a **row**.

$$\begin{bmatrix}1\\2\\3\end{bmatrix}\begin{bmatrix}1&3\end{bmatrix}=\begin{bmatrix}1&3\\2&6\\3&9\end{bmatrix}$$

<div v-click="1">

$$AB=\begin{bmatrix}1\\3\end{bmatrix}\begin{bmatrix}5&6\end{bmatrix}+\begin{bmatrix}2\\4\end{bmatrix}\begin{bmatrix}7&8\end{bmatrix}$$

$$=\begin{bmatrix}5&6\\15&18\end{bmatrix}+\begin{bmatrix}14&16\\28&32\end{bmatrix}=\begin{bmatrix}19&22\\43&50\end{bmatrix}$$

</div>
''',1,'compact'),
slide(7, 'The inverse matrix', r'''
# The Inverse Matrix

$$AA^{-1}=A^{-1}A=I$$

A square matrix has an inverse exactly when its determinant is nonzero.

$$A=\begin{bmatrix}3&1\\4&2\end{bmatrix},\qquad \det A=3(2)-1(4)=2$$

<div v-click="1">

$$A^{-1}=\frac12\begin{bmatrix}2&-1\\-4&3\end{bmatrix}$$

</div>
''',1),
slide(8, 'Gauss–Jordan elimination', r'''
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
''',2),
slide(9, 'Gauss–Jordan worked example', r'''
# Gauss–Jordan Worked Example

$$A=\begin{bmatrix}1&3\\2&5\end{bmatrix}$$

<NativeMatrixSteps lesson="inverse" :augmented="2" />

<div v-click="3" class="native-callout">The inverse is A⁻¹ = [−5, 3; 2, −1]. Multiplying A by this inverse gives I.</div>
''',3),
slide(10, 'MATLAB: multiplication', r'''
# MATLAB: Multiplication

<div class="native-code-grid"><div>

```matlab
A = [1 2; 3 4];
B = [5 6; 7 8];
C = A * B
```

</div><NativeOutput :lines="['C =', '    19    22', '    43    50']" /></div>

The built-in matrix product gives the same result as all four views.
'''),
slide(11, 'MATLAB: inverse by row reduction', r'''
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
'''),
slide(12, 'Applications', r'''
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
'''),
]

DECKS[5] = [
slide(1, 'Permutations, transposes and vector spaces', r'''
# Permutations, Transposes, and Vector Spaces

## Lecture 5

Linear Algebra
''',style='native-cover'),
slide(2, 'Contents', r'''
# Contents

<v-clicks>

1. Permutations and PA = LU.
2. Transposes and symmetric matrices.
3. Vector spaces and subspaces.
4. The column space C(A).

</v-clicks>
''',4),
slide(3, 'Permutation matrices', r'''
# Permutation Matrices

Elimination may need a row swap when a pivot candidate is zero or too small.

$$\boxed{PA=LU}$$

<v-clicks>

- P is formed by reordering the rows of the identity matrix.
- For n rows, there are n! possible permutations.
- A permutation matrix satisfies $P^{-1}=P^T$ and $P^TP=I$.

</v-clicks>
''',3),
slide(4, 'A row swap before elimination', r'''
# A Row Swap Before Elimination

$$A=\begin{bmatrix}0&1&2\\1&2&3\\2&6&9\end{bmatrix},\quad P=\begin{bmatrix}0&1&0\\1&0&0\\0&0&1\end{bmatrix},\quad PA=\begin{bmatrix}1&2&3\\0&1&2\\2&6&9\end{bmatrix}$$

<div v-click="1">

Use $R_3\leftarrow R_3-2R_1$, then $R_3\leftarrow R_3-2R_2$:

$$L=\begin{bmatrix}1&0&0\\0&1&0\\2&2&1\end{bmatrix},\qquad U=\begin{bmatrix}1&2&3\\0&1&2\\0&0&-1\end{bmatrix}$$

</div>

<div v-click="2" class="native-callout">The original factors satisfy **PA = LU**.</div>
''',2,'compact'),
slide(5, 'Transposes and symmetric matrices', r'''
# Transposes and Symmetric Matrices

Rows become columns:

$$A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}\quad\Longrightarrow\quad A^T=\begin{bmatrix}1&4\\2&5\\3&6\end{bmatrix}$$

<div v-click="1">

A square matrix is **symmetric** when $S^T=S$:

$$S=\begin{bmatrix}1&7&5\\7&2&9\\5&9&3\end{bmatrix}.$$

</div>
''',1),
slide(6, 'Making a symmetric matrix', r'''
# Making a Symmetric Matrix

$$R=\begin{bmatrix}1&2\\3&0\\0&4\end{bmatrix},\qquad R^T=\begin{bmatrix}1&3&0\\2&0&4\end{bmatrix}$$

<div v-click="1">

$$R^TR=\begin{bmatrix}1^2+3^2+0^2&1(2)+3(0)+0(4)\\2(1)+0(3)+4(0)&2^2+0^2+4^2\end{bmatrix}=\begin{bmatrix}10&2\\2&20\end{bmatrix}$$

</div>

<div v-click="2" class="native-callout">The off-diagonal entries match. In general, $(R^TR)^T=R^TR$.</div>
''',2,'compact'),
slide(7, 'Python: the symmetry check', r'''
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
'''),
slide(8, 'Vector spaces', r'''
# Vector Spaces

A vector space stays inside the set under vector addition and scalar multiplication.

$$\mathbf u,\mathbf v\in V,\ a,b\in\mathbb R\quad\Longrightarrow\quad a\mathbf u+b\mathbf v\in V.$$

<v-clicks>

- Add two vectors: the sum stays in the space.
- Scale a vector: every real scalar multiple stays in the space.
- Every vector space contains the zero vector.

</v-clicks>
''',3),
slide(9, 'Examples of vector spaces', r'''
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
'''),
slide(10, 'Subspaces', r'''
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
'''),
slide(11, 'The column space', r'''
# The Column Space C(A)

<div class="native-columns diagram-wide"><div>

The column space contains **all linear combinations** of the columns of A.

$$C(A)=\{A\mathbf x:\mathbf x\in\mathbb R^n\}$$

For two independent columns in ℝ³, their combinations form a plane through the origin.

</div><NativeMathDiagram kind="span3" /></div>
'''),
]

DECKS[9] = [
slide(1, 'Independence, basis and dimension', r'''
# Independence, Basis, and Dimension

## Lecture 9

Linear Algebra
''',style='native-cover'),
slide(2, 'What we will cover', r'''
# What We Will Cover

<v-clicks>

1. Linear independence and dependence.
2. Basis.
3. Dimension.

</v-clicks>
''',3),
slide(3, 'Two vectors', r'''
# Two Vectors

$$\mathbf u=\begin{bmatrix}2\\3\end{bmatrix},\qquad \mathbf v=\begin{bmatrix}1\\4\end{bmatrix}$$

Can either vector be made by scaling the other?

<div v-click="1" class="native-callout">They point in different directions. Neither is a scalar multiple of the other.</div>
''',1),
slide(4, 'Independent directions', r'''
# Independent Directions

<div class="native-columns"><div>

$$\mathbf u=\begin{bmatrix}2\\3\end{bmatrix},\qquad \mathbf v=\begin{bmatrix}1\\4\end{bmatrix}$$

The two nonparallel vectors span ℝ².

</div><NativeMathDiagram kind="independent" /></div>
'''),
slide(5, 'Linear independence', r'''
# Linear Independence

Vectors are linearly independent when no vector in the set is a linear combination of the others.

$$c_1\mathbf v_1+c_2\mathbf v_2+\cdots+c_n\mathbf v_n=\mathbf0$$

<div v-click="1">

Putting the vectors in columns gives:

$$A\mathbf c=\mathbf0.$$

</div>
''',1),
slide(6, 'The zero combination', r'''
# The Zero Combination

For independent columns, the only solution of

$$A\mathbf c=\mathbf0$$

is

$$\boxed{c_1=c_2=\cdots=c_n=0}.$$

Every coefficient must be zero.
'''),
slide(7, 'Linear dependence', r'''
# Linear Dependence

A set is linearly dependent when **at least one vector can be written as a linear combination of the others**.

<div class="native-columns"><div>

$$\mathbf v_2=2\mathbf v_1$$

The second vector adds no new direction.

</div><NativeMathDiagram kind="dependent" /></div>
'''),
slide(8, 'A nonzero dependency relation', r'''
# A Nonzero Dependency Relation

Dependence means there is a coefficient vector c ≠ 0 such that

$$A\mathbf c=\mathbf0.$$

For example:

$$-2\mathbf v_1+\mathbf v_2=\mathbf0.$$

<div class="native-callout">The vectors sum to zero even though their coefficients are not all zero.</div>
'''),
slide(9, 'Independent or dependent?', r'''
# Independent or Dependent?

<div class="native-columns"><div>

## Independent

<NativeMathDiagram kind="independent" />

</div><div>

## Dependent

<NativeMathDiagram kind="dependent" />

</div></div>

<div class="native-small">Independent vectors supply different directions. Dependent vectors repeat a direction already available.</div>
'''),
slide(10, 'Three vectors: a question', r'''
# Three Vectors: A Question

<div class="native-columns"><div>

Does the third vector add a new independent direction?

Think about whether it can be reached by combining the first two.

</div><NativeMathDiagram kind="dependence3" :stage="0" /></div>
'''),
slide(11, 'The third vector is dependent', r'''
# The Third Vector Is Dependent

<div class="native-columns"><div>

$$\mathbf v_3=\mathbf v_1+\mathbf v_2$$

$$-\mathbf v_1-\mathbf v_2+\mathbf v_3=\mathbf0$$

The third vector adds no independent direction.

</div><NativeMathDiagram kind="dependence3" :stage="1" /></div>
'''),
slide(12, 'A linear combination', r'''
# A Linear Combination

$$c_1\mathbf v_1+c_2\mathbf v_2=\mathbf v_3$$

<div class="native-columns"><div>

Combine scaled vectors tip to tail. The resultant is a vector already in their span.

</div><NativeMathDiagram kind="dependence3" :stage="1" /></div>
'''),
slide(13, 'The numerical example', r'''
# Dependent or Independent?

$$\mathbf v_1=\begin{bmatrix}3\\2\\5\end{bmatrix},\qquad\mathbf v_2=\begin{bmatrix}4\\7\\2\end{bmatrix},\qquad\mathbf v_3=\begin{bmatrix}7\\9\\7\end{bmatrix}$$

Can you find a nonzero coefficient vector that makes their combination zero?
'''),
slide(14, 'The dependence relation', r'''
# The Dependence Relation

$$\begin{bmatrix}3\\2\\5\end{bmatrix}+\begin{bmatrix}4\\7\\2\end{bmatrix}=\begin{bmatrix}7\\9\\7\end{bmatrix}$$

$$\boxed{-\mathbf v_1-\mathbf v_2+\mathbf v_3=\mathbf0}$$

The coefficient vector (−1, −1, 1) is nonzero, so the columns are dependent.
'''),
slide(15, 'Row reduction: the first pivot', r'''
# Row Reduction: The First Pivot

<NativeMatrixSteps lesson="dependence" :max-step="2" />

Each row operation preserves the solutions of Ac = 0.
''',2),
slide(16, 'Row reduction: the second pivot', r'''
# Row Reduction: The Second Pivot

<NativeMatrixSteps lesson="dependence" :offset="2" :max-step="2" />

Clear below the first pivot, then scale the second row to make its pivot 1.
''',2),
slide(17, 'A free column', r'''
# A Free Column

<NativeMatrixSteps lesson="dependence" :offset="4" :max-step="1" />

<div v-click="1" class="native-callout">The last row is zero. Column 3 has no pivot, so c₃ is a free variable and the columns are dependent.</div>
''',1),
slide(18, 'Rank counts pivots', r'''
# Rank Counts Pivots

$$\begin{bmatrix}1&-3&-2\\0&1&1\\0&0&0\end{bmatrix}$$

There are two pivot positions:

$$\boxed{r=\operatorname{rank}(A)=2}.$$

The rank counts independent column directions.
'''),
slide(19, 'Counting free variables', r'''
# Counting Free Variables

The number of free columns is the number of columns minus the rank:

$$n-r=3-2=1.$$

<div class="native-callout">One free variable gives one independent nullspace direction. The nullspace is the set of coefficient vectors c satisfying Ac = 0.</div>
'''),
slide(20, 'Basis', r'''
# Basis

<div class="native-columns"><div>

A basis for a vector space satisfies both conditions:

1. The vectors are linearly independent.
2. They span the space.

</div><NativeMathDiagram kind="basis3" /></div>
'''),
slide(21, 'A basis of the column space', r'''
# A Basis of the Column Space

Take the pivot columns from the **original** matrix A:

$$\left\{\begin{bmatrix}3\\2\\5\end{bmatrix},\begin{bmatrix}4\\7\\2\end{bmatrix}\right\}.$$

They are independent and span every column of A. The third column is their sum.
'''),
slide(22, 'How many basis vectors?', r'''
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
'''),
slide(23, 'A basis for a plane, not all of R3', r'''
# A Basis for a Plane

<div class="native-columns"><div>

Two independent vectors in ℝ³ span a plane through the origin.

They form a basis for that plane, but not for all of ℝ³.

</div><NativeMathDiagram kind="span3" /></div>
'''),
slide(24, 'Dimension', r'''
# Dimension

The dimension of a space is the number of vectors in any basis for it.

$$\boxed{\dim C(A)=2,\qquad\dim N(A)=1}$$

For a matrix with n columns:

$$\operatorname{rank}(A)+\dim N(A)=n.$$

Here, $2+1=3$.
'''),
slide(25, 'Python: independence and rank', r'''
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
''',style='compact'),
slide(26, 'Conclusion', r'''
# Conclusion

| Idea | Meaning |
| --- | --- |
| Independence | The only solution of Ac = 0 is c = 0 |
| Spanning | All combinations of columns give C(A) |
| Basis | Independent vectors that span the chosen space |
| Dimension | The number of basis vectors |

$$\dim C(A)=r,\qquad\dim N(A)=n-r.$$
'''),
slide(27, 'Lecture 9 template page', '<div class="native-blank" />',style='native-template'),
slide(28, 'Lecture 9 template page', '<div class="native-blank" />',style='native-template'),
slide(29, 'Lecture 9 template page', '<div class="native-blank" />',style='native-template'),
]

TITLES={1:'Geometry of linear equations',2:'Elimination with matrices',3:'Matrix multiplication and inverses',5:'Permutations, transposes, and vector spaces',9:'Independence, basis, and dimension'}
FILES={1:'01-geometry.md',2:'02-elimination.md',3:'03-products-inverses.md',5:'05-permutations-spaces.md',9:'09-independence-basis.md'}


def build():
    edits=json.loads((ROOT/'sources/deck-edits.json').read_text(encoding='utf-8'))
    index=[];next_page=1
    for lecture,items in DECKS.items():
        if lecture == 1:
            import runpy
            native = runpy.run_path(str(ROOT/'scripts/build-lecture1-native.py'))['build']()
            count = len(native['slides'])
            index.append({'lecture':1,'title':TITLES[1],'start':next_page,'file':'lectures/'+FILES[1],'originals':count,'new_labs':0,'total':count,'rendering':'source-native-svg'})
            next_page += count
            continue
        source='Seminar' if lecture in [1,2] else 'Presentation2' if lecture==3 else 'Lecture5' if lecture==5 else 'CanvaLecture9'
        parts=[]
        for item in items:
            if item['source'] in edits.get('excludedSourceSlides',{}).get(source,[]):continue
            fields={'layout':'native','lecture':lecture,'title':item['title'],'clicks':item['clicks'],'sourceDeck':source,'sourceSlide':item['source']}
            if item['style']:fields['class']=item['style']
            if not parts:fields.update(routeAlias=f'lecture-{lecture}',section=True)
            front='---\n'+'\n'.join(f'{key}: {json.dumps(value,ensure_ascii=False)}' for key,value in fields.items())+'\n---\n\n'
            parts.append(front+item['body']+'\n\n'+f'<!-- Rebuilt as native Slidev content from {source}, original page {item["source"]}. -->\n')
        (ROOT/'lectures'/FILES[lecture]).write_text('\n'.join(parts),encoding='utf-8')
        index.append({'lecture':lecture,'title':TITLES[lecture],'start':next_page,'file':'lectures/'+FILES[lecture],'originals':len(parts),'new_labs':0,'total':len(parts),'rendering':'native'})
        next_page+=len(parts)
    (ROOT/'sources/lecture-index.json').write_text(json.dumps(index,indent=2)+'\n',encoding='utf-8')
    print(f'Rebuilt {next_page-1} native slides across lectures '+', '.join(map(str,DECKS)))


if __name__=='__main__':build()
