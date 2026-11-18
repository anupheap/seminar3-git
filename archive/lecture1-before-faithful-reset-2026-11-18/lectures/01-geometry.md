---
layout: "native"
lecture: 1
title: "Lecture 1"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 1
routeAlias: "lecture-1"
section: true
---

<div class="native-blank" />

<!-- Rebuilt as native Slidev content from Seminar, original page 1. -->

---
layout: "native"
lecture: 1
title: "The geometry of linear equations"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 2
class: "native-cover"
---

# The Geometry of Linear Equations

## Lecture 1

Institute of Technology of Cambodia

MIT 18.06 Linear Algebra · Gilbert Strang

<!-- Rebuilt as native Slidev content from Seminar, original page 2. -->

---
layout: "native"
lecture: 1
title: "Learning Objectives"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 3
---

<NativeObjectives :items="['Understand the row picture', 'Understand the column picture', 'Visualize vectors in 2D and 3D with systems of equations', 'Understand why n unknowns need independent equations']" />

<!-- Rebuilt as native Slidev content from Seminar, original page 3. -->

---
layout: "native"
lecture: 1
title: "The row picture"
clicks: 3
sourceDeck: "Seminar"
sourceSlide: 4
---

# The Row Picture

<div class="native-columns diagram-wide"><div>

Each equation describes a geometric shape:

<v-clicks>

- A line in two dimensions.
- A plane in three dimensions.
- Their common intersection is the solution.

</v-clicks>

</div><NativeMathDiagram kind="rows" /></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 4. -->

---
layout: "native"
lecture: 1
title: "Equations and matrix form"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 5
---

# Equations and Matrix Form

$$\begin{aligned}2x-y&=0\\-x+2y&=3\end{aligned}$$

<div v-click="1">

$$\underbrace{\begin{bmatrix}2&-1\\-1&2\end{bmatrix}}_A
\underbrace{\begin{bmatrix}x\\y\end{bmatrix}}_{\mathbf{x}}
=\underbrace{\begin{bmatrix}0\\3\end{bmatrix}}_{\mathbf b}$$

</div>

<div v-click="2" class="native-callout">A is the coefficient matrix, x contains the unknowns, and b is the right-hand side.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 5. -->

---
layout: "native"
lecture: 1
title: "Two lines, one intersection"
clicks: 3
sourceDeck: "Seminar"
sourceSlide: 6
---

# Two Lines, One Intersection

<div class="native-columns diagram-wide"><div>

<div v-click="1">

$$\color{#7fe3a2}{2x-y=0}$$

</div><div v-click="2">

$$\color{#ffdb78}{-x+2y=3}$$

</div><div v-click="3" class="native-callout">

$$\boxed{(x,y)=(1,2)}$$

Both equations hold at this point.

</div></div><NativeMathDiagram kind="rows" /></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 6. -->

---
layout: "native"
lecture: 1
title: "Three equations, three planes"
clicks: 3
sourceDeck: "Seminar"
sourceSlide: 7
---

# Three Equations, Three Planes

<div class="native-columns diagram-wide"><div>

$$\begin{aligned}2x-y&=0\\-x+2y-z&=-1\\-3y+4z&=4\end{aligned}$$

<div v-click="3" class="native-callout">

$$\boxed{(x,y,z)=(0,0,1)}$$

The point lies in all three planes.

</div></div><NativeMathDiagram kind="planes" /></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 7. -->

---
layout: "native"
lecture: 1
title: "The column picture"
clicks: 3
sourceDeck: "Seminar"
sourceSlide: 8
---

# The Column Picture

The columns are vectors. The unknowns tell us how much of each vector to use.

<div class="native-columns"><div>

<v-clicks>

1. Scale each column by its coefficient.
2. Add the scaled vectors.
3. Reach the target vector b.

</v-clicks>

</div><div>

$$x\mathbf a_1+y\mathbf a_2=\mathbf b$$

A **linear combination** scales vectors and adds them.

</div></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 8. -->

---
layout: "native"
lecture: 1
title: "The same system by columns"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 9
---

# The Same System by Columns

$$\begin{bmatrix}2&-1\\-1&2\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
=x\begin{bmatrix}2\\-1\end{bmatrix}+y\begin{bmatrix}-1\\2\end{bmatrix}
=\begin{bmatrix}0\\3\end{bmatrix}$$

<div v-click="1" class="native-callout">

$$\boxed{x=1,\qquad y=2}$$

The intersection coordinates are also the column weights.

</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 9. -->

---
layout: "native"
lecture: 1
title: "Scale the columns"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 10
---

# Scale the Columns

<div class="native-columns diagram-wide"><div>

$$\mathbf a_1=\begin{bmatrix}2\\-1\end{bmatrix},\qquad\mathbf a_2=\begin{bmatrix}-1\\2\end{bmatrix}$$

<div v-click="1">

$$2\mathbf a_2=\begin{bmatrix}-2\\4\end{bmatrix}$$

The orange vector doubles in length.

</div></div><NativeMathDiagram kind="columns" :stage="2" /></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 10. -->

---
layout: "native"
lecture: 1
title: "Add the columns tip to tail"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 11
---

# Add the Columns Tip to Tail

<div class="native-columns diagram-wide"><div>

$$\begin{bmatrix}2\\-1\end{bmatrix}+\begin{bmatrix}-2\\4\end{bmatrix}=\begin{bmatrix}0\\3\end{bmatrix}$$

$$\mathbf a_1+2\mathbf a_2=\mathbf b$$

The resultant reaches b. The same weights solve both row equations.

</div><NativeMathDiagram kind="columns" :stage="3" /></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 11. -->

---
layout: "native"
lecture: 1
title: "The column picture in 3D"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 12
class: "compact"
---

# The Column Picture in 3D

<div class="native-columns diagram-wide"><div>

$$x\begin{bmatrix}2\\-1\\0\end{bmatrix}+y\begin{bmatrix}-1\\2\\-3\end{bmatrix}+z\begin{bmatrix}0\\-1\\4\end{bmatrix}=\begin{bmatrix}0\\-1\\4\end{bmatrix}$$

<div v-click="1" class="native-callout">

The target is the third column:

$$x=0,\quad y=0,\quad z=1.$$

</div></div><NativeMathDiagram kind="three-columns" /></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 12. -->

---
layout: "native"
lecture: 1
title: "What can the columns reach?"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 13
---

# What Can the Columns Reach?

<div class="native-columns"><div>

## Independent directions

<NativeMathDiagram kind="independent" />

</div><div>

## Dependent directions

<NativeMathDiagram kind="dependent" />

</div></div>

<div class="native-small">Two nonparallel columns in ℝ² reach every target in the plane. Parallel columns reach only a line.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 13. -->

---
layout: "native"
lecture: 1
title: "Why count equations?"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 14
---

# Why Count Equations?

For a unique solution in n unknowns, we need n independent constraints and a consistent system.

<div class="native-three"><div>

## One solution

$$\begin{aligned}2x-y&=0\\-x+2y&=3\end{aligned}$$

The lines cross once.

</div><div>

## Infinitely many

$$\begin{aligned}2x-y&=1\\4x-2y&=2\end{aligned}$$

The lines coincide.

</div><div>

## No solution

$$\begin{aligned}2x-y&=1\\4x-2y&=3\end{aligned}$$

The lines are distinct and parallel.

</div></div>

<!-- Rebuilt as native Slidev content from Seminar, original page 14. -->

---
layout: "native"
lecture: 1
title: "Constraints in three dimensions"
clicks: 0
sourceDeck: "Seminar"
sourceSlide: 15
class: "compact"
---

# Constraints in Three Dimensions

<div class="native-three"><div>

## One equation

$$2x-y=0$$

A plane of possible points.

</div><div>

## Two independent equations

$$\begin{aligned}2x-y&=0\\-x+2y-z&=-1\end{aligned}$$

The two planes meet along a line.

</div><div>

## Three independent equations

Add $-3y+4z=4$.

The common intersection is the point $(0,0,1)$.

</div></div>

<div class="native-callout">Each independent constraint reduces the degrees of freedom by one.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 15. -->

---
layout: "native"
lecture: 1
title: "Review: row and column pictures"
clicks: 2
sourceDeck: "Seminar"
sourceSlide: 16
---

# Review: Row and Column Pictures

## What does the row picture show?

A. Intersections of the geometric shapes defined by the equations.

B. Weighted sums of columns reaching a target vector.

<div v-click="1" class="native-callout">The row picture is **A**: a solution lies on every line or plane.</div>

## What does the column picture show?

<div v-click="2">The column picture is **B**: the unknowns are the weights in a linear combination.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 16. -->

---
layout: "native"
lecture: 1
title: "Review: a unique solution?"
clicks: 1
sourceDeck: "Seminar"
sourceSlide: 17
---

# Do n Equations Guarantee a Unique Solution?

For n unknowns, choose the correct statement:

1. Every square system has exactly one solution.
2. The equations must be independent and consistent.
3. Counting equations is enough.

<div v-click="1" class="native-callout">**Statement 2.** A square system can have one solution, infinitely many solutions, or no solution.</div>

<!-- Rebuilt as native Slidev content from Seminar, original page 17. -->
