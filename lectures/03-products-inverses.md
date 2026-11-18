---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 1"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 1
routeAlias: "lecture-3"
section: true
---

<PowerPointSource :lecture="3" :slide="1" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 2"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 2
---

<PowerPointSource :lecture="3" :slide="2" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 3"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 3
---

<PowerPointSource :lecture="3" :slide="3" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 4"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 4
---

<PowerPointSource :lecture="3" :slide="4" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 5"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 5
---

<PowerPointSource :lecture="3" :slide="5" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 6"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 6
---

<PowerPointSource :lecture="3" :slide="6" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 7"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 7
---

<PowerPointSource :lecture="3" :slide="7" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 8"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 8
---

<PowerPointSource :lecture="3" :slide="8" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 9"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 9
---

<PowerPointSource :lecture="3" :slide="9" />

---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 10"
clicks: 2
sourceDeck: "Presentation2"
sourceSlide: 10
codeCopy: false
magicMoveCopy: false
---

<PowerPointSource :lecture="3" :slide="10" :hide-shapes="[15,16]" />

<div class="stepped-source-code walk-matlab" style="left:4.375%;top:27.7778%;width:35.9375%;height:55.5556%">

````md magic-move {at:1, duration:500, lines:false}
```matlab {1}
A = [1 2; 3 4];
```
```matlab {2}
A = [1 2; 3 4];
B = [5 6; 7 8];
```
```matlab {3}
A = [1 2; 3 4];
B = [5 6; 7 8];
C = A*B
```
````

</div>

<div class="stepped-source-result walk-matlab" style="left:59.6875%;top:27.7778%;width:35.9375%;height:55.5556%"><CodeWalkOutput lesson="l3-product" /></div>


---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 11"
clicks: 4
sourceDeck: "Presentation2"
sourceSlide: 11
codeCopy: false
magicMoveCopy: false
---

<PowerPointSource :lecture="3" :slide="11" :hide-shapes="[3,5]" />

<div class="stepped-source-code walk-inverse" style="left:4.375%;top:22.7778%;width:62.5%;height:70%">

````md magic-move {at:1, duration:500, lines:false}
```matlab {1}
A = [1 3; 2 5];
```
```matlab {2}
A = [1 3; 2 5];
M = rref([A eye(2)])     % Gauss-Jordan on [A | I]
```
```matlab {3}
A = [1 3; 2 5];
M = rref([A eye(2)])     % Gauss-Jordan on [A | I]
Ainv = M(:,3:4)          % right half is the inverse
```
```matlab {4}
A = [1 3; 2 5];
M = rref([A eye(2)])     % Gauss-Jordan on [A | I]
Ainv = M(:,3:4)          % right half is the inverse
A*Ainv                   % check: should be the identity
```
```matlab {5}
A = [1 3; 2 5];
M = rref([A eye(2)])     % Gauss-Jordan on [A | I]
Ainv = M(:,3:4)          % right half is the inverse
A*Ainv                   % check: should be the identity
inv(A)                   % built-in check
```
````

</div>

<div class="stepped-source-result walk-inverse" style="left:69.375%;top:22.7778%;width:26.25%;height:70%"><CodeWalkOutput lesson="l3-inverse" /></div>


---
layout: "none"
lecture: 3
title: "Lecture 3 · original slide 12"
clicks: 0
sourceDeck: "Presentation2"
sourceSlide: 12
---

<PowerPointSource :lecture="3" :slide="12" />
