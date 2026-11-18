---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 1"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 1
routeAlias: "lecture-5"
section: true
---

<PowerPointSource :lecture="5" :slide="1" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 2"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 2
---

<PowerPointSource :lecture="5" :slide="2" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 3"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 3
---

<PowerPointSource :lecture="5" :slide="3" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 4"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 4
---

<PowerPointSource :lecture="5" :slide="4" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 5"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 5
---

<PowerPointSource :lecture="5" :slide="5" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 6"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 6
---

<PowerPointSource :lecture="5" :slide="6" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 7"
clicks: 4
sourceDeck: "Lecture5"
sourceSlide: 7
codeCopy: false
magicMoveCopy: false
---

<PowerPointSource :lecture="5" :slide="7" :hide-shapes="[6,11]" />

<div class="stepped-source-code walk-numpy" style="left:3.6394%;top:31.6641%;width:49%;height:43%">

````md magic-move {at:1, duration:500, lines:false}
```python {1-2}
import numpy as np
R = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)
```
```python {4}
import numpy as np
R = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)

RT_R = R.T @ R
```
```python {6}
import numpy as np
R = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)

RT_R = R.T @ R

is_symmetric = np.allclose(RT_R, RT_R.T)
```
```python {8}
import numpy as np
R = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)

RT_R = R.T @ R

is_symmetric = np.allclose(RT_R, RT_R.T)

print("R^T * R:\n", RT_R)
```
```python {9}
import numpy as np
R = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)

RT_R = R.T @ R

is_symmetric = np.allclose(RT_R, RT_R.T)

print("R^T * R:\n", RT_R)
print("Is symmetric?:", is_symmetric)
```
````

</div>

<div class="stepped-source-result walk-numpy" style="left:59.2628%;top:32.6893%;width:33.9631%;height:27.8%"><CodeWalkOutput lesson="l5-symmetric" /></div>


---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 8"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 8
---

<PowerPointSource :lecture="5" :slide="8" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 9"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 9
---

<PowerPointSource :lecture="5" :slide="9" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 10"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 10
---

<PowerPointSource :lecture="5" :slide="10" />

---
layout: "none"
lecture: 5
title: "Lecture 5 · original slide 11"
clicks: 0
sourceDeck: "Lecture5"
sourceSlide: 11
---

<PowerPointSource :lecture="5" :slide="11" />
