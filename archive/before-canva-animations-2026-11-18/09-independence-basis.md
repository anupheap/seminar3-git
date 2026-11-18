---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 1"
sourceDeck: "CanvaLecture9"
sourceSlide: 1
clicks: 0
routeAlias: "lecture-9"
section: true
---

<CanvaSource :slide="1" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 2"
sourceDeck: "CanvaLecture9"
sourceSlide: 2
clicks: 0
---

<CanvaSource :slide="2" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 3"
sourceDeck: "CanvaLecture9"
sourceSlide: 3
clicks: 0
---

<CanvaSource :slide="3" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 4"
sourceDeck: "CanvaLecture9"
sourceSlide: 4
clicks: 0
---

<CanvaSource :slide="4" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 5"
sourceDeck: "CanvaLecture9"
sourceSlide: 5
clicks: 0
---

<CanvaSource :slide="5" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 6"
sourceDeck: "CanvaLecture9"
sourceSlide: 6
clicks: 0
---

<CanvaSource :slide="6" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 7"
sourceDeck: "CanvaLecture9"
sourceSlide: 7
clicks: 0
---

<CanvaSource :slide="7" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 8"
sourceDeck: "CanvaLecture9"
sourceSlide: 8
clicks: 0
---

<CanvaSource :slide="8" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 9"
sourceDeck: "CanvaLecture9"
sourceSlide: 9
clicks: 0
---

<CanvaSource :slide="9" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 10"
sourceDeck: "CanvaLecture9"
sourceSlide: 10
clicks: 0
---

<CanvaSource :slide="10" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 11"
sourceDeck: "CanvaLecture9"
sourceSlide: 11
clicks: 0
---

<CanvaSource :slide="11" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 12"
sourceDeck: "CanvaLecture9"
sourceSlide: 12
clicks: 0
---

<CanvaSource :slide="12" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 13"
sourceDeck: "CanvaLecture9"
sourceSlide: 13
clicks: 0
---

<CanvaSource :slide="13" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 14"
sourceDeck: "CanvaLecture9"
sourceSlide: 14
clicks: 0
---

<CanvaSource :slide="14" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 15"
sourceDeck: "CanvaLecture9"
sourceSlide: 15
clicks: 0
---

<CanvaSource :slide="15" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 16"
sourceDeck: "CanvaLecture9"
sourceSlide: 16
clicks: 0
---

<CanvaSource :slide="16" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 17"
sourceDeck: "CanvaLecture9"
sourceSlide: 17
clicks: 0
---

<CanvaSource :slide="17" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 18"
sourceDeck: "CanvaLecture9"
sourceSlide: 18
clicks: 0
---

<CanvaSource :slide="18" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 19"
sourceDeck: "CanvaLecture9"
sourceSlide: 19
clicks: 0
---

<CanvaSource :slide="19" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 20"
sourceDeck: "CanvaLecture9"
sourceSlide: 20
clicks: 0
---

<CanvaSource :slide="20" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 21"
sourceDeck: "CanvaLecture9"
sourceSlide: 21
clicks: 0
---

<CanvaSource :slide="21" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 22"
sourceDeck: "CanvaLecture9"
sourceSlide: 22
clicks: 0
---

<CanvaSource :slide="22" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 23"
sourceDeck: "CanvaLecture9"
sourceSlide: 23
clicks: 0
---

<CanvaSource :slide="23" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 24"
sourceDeck: "CanvaLecture9"
sourceSlide: 24
clicks: 0
---

<CanvaSource :slide="24" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 25"
sourceDeck: "CanvaLecture9"
sourceSlide: 25
clicks: 4
codeCopy: false
magicMoveCopy: false
---

<CanvaSource :slide="25" :hide-images="true" />

<div class="stepped-source-code walk-sympy" style="left:7.88%;top:42%;width:42%;height:45%">

````md magic-move {at:1, duration:500, lines:false}
```python {1-5}
from sympy import Matrix

A = Matrix([[3, 4, 7],
            [2, 7, 9],
            [5, 2, 7]])
```
```python {7-8}
from sympy import Matrix

A = Matrix([[3, 4, 7],
            [2, 7, 9],
            [5, 2, 7]])

n_vectors = A.shape[1]
rank = A.rank()
```
```python {10}
from sympy import Matrix

A = Matrix([[3, 4, 7],
            [2, 7, 9],
            [5, 2, 7]])

n_vectors = A.shape[1]
rank = A.rank()

print("Number of vectors:", n_vectors)
```
```python {11}
from sympy import Matrix

A = Matrix([[3, 4, 7],
            [2, 7, 9],
            [5, 2, 7]])

n_vectors = A.shape[1]
rank = A.rank()

print("Number of vectors:", n_vectors)
print("Rank:", rank)
```
```python {12}
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
````

</div>

<div class="stepped-source-result walk-sympy" style="left:53.7%;top:48%;width:37.65%;height:31%"><CodeWalkOutput lesson="l9-rank" /></div>


---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 26"
sourceDeck: "CanvaLecture9"
sourceSlide: 26
clicks: 0
---

<CanvaSource :slide="26" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 27"
sourceDeck: "CanvaLecture9"
sourceSlide: 27
clicks: 0
---

<CanvaSource :slide="27" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 28"
sourceDeck: "CanvaLecture9"
sourceSlide: 28
clicks: 0
---

<CanvaSource :slide="28" />

---
layout: "none"
lecture: 9
title: "Lecture 9 \u00b7 original page 29"
sourceDeck: "CanvaLecture9"
sourceSlide: 29
clicks: 0
---

<CanvaSource :slide="29" />
