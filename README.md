# Seminar III linear algebra slides

This is a **49-slide Slidev deck** compiled from the supplied PDF, two Canva decks, and three PowerPoint files. The active slides cover Lectures 1, 2, 3, 5, and 9. Previous Lecture 6 material and examples outside these sources have been removed from `slides.md`.

## Source map

| Lecture | Source material | Active slides |
| :-- | :-- | :-- |
| 1 — Geometry of linear equations | `White Beige and Brown Simple Minimalist Clean Final Project Presentation.pdf` pp. 1–18; [first Canva deck](https://canva.link/zq4wr2hywc9crpv); `Seminar.pptx` slides 2–18 | Row picture, column picture, 2D and 3D systems, matrix forms, solution cases |
| 2 — Elimination with matrices | `Seminar.pptx` slides 19–31 | Elimination, back substitution, failure case, matrix products, elimination matrices |
| 3 — Matrix multiplication and inverses | `Presentation2.pptx` slides 1–12 | Four multiplication views, inverse, Gauss–Jordan, MATLAB example |
| 5 — Permutations, transposes, vector spaces | `Lecture5.pptx` slides 1–8 | $PA=LU$, symmetry, vector-space test |
| 9 — Independence, basis, dimension | [second Canva deck](https://canva.link/ntsr64ln7l1s9i0) pp. 1–26 | Dependence example, rank, basis, dimension, SymPy code |

The PDF's pages 19–28 contain an unrelated planner template and are excluded as requested. The second Canva deck's final blank/template pages are also excluded. See [`SOURCE_COMPARISON.md`](SOURCE_COMPARISON.md) for source differences and corrections.

## View and build

```bash
npm ci
npx slidev --port 3030
npm run build
```

Open `http://localhost:3030/`. The currently running local Slidev service uses this folder. Four Lecture 1 clips remain in the active deck because their equations and results match the PDF. Other old animation and Python assets remain in the folder as source files but are not referenced by the active slides.

## Edit

- `slides.md` — source-based slides, equations, code, and source notes.
- `components/VectorCombination.vue` and `components/LinearPlot.vue` — source-aligned vector and row diagrams.
- `components/MathFilm.vue` — Lecture 1 clip playback.
- `styles/style.css` — visual layout.
- `global-top.vue` — slide footer.

The remote branch also provides `python_examples/boilerplate.py` and
[`python_examples/BOILERPLATE.md`](python_examples/BOILERPLATE.md) as optional templates for future code-synchronized lessons. They are not referenced by the active slides.
