# Source coverage and review notes

The supplied PowerPoint files and the explicitly supplied Canva design are now
the source of truth. Original files are preserved, with active exclusions saved
in `sources/deck-edits.json`. The earlier
49-slide synthesis is archived as `archive/slides-before-cleanup.md`.

| Lecture | Original source | Coverage |
| --- | --- | --- |
| 1 | `Seminar.pptx` | Slides 1–17; closing Q&A removed |
| 2 | `Seminar.pptx` | Slides 19–30; closing Q&A removed |
| 3 | `Presentation2.pptx` | All 12 slides, including both MATLAB demos and applications |
| 5 | `Lecture5.pptx` | Slides 1–11; closing Q&A/Thanks and Slidesgo credit pages removed |
| 9 | [Canva design DAHa-hNCW00](https://www.canva.com/design/DAHa-hNCW00/iV35G0qo8ZAcpbj6MrsVOg/edit) | All 29 pages, including repeated reveal pages and template endings |

## New code and Manim source map

The appended demo pages below have all been excluded from the active deck.
Their source files and assets are retained for future lecture-by-lecture editing.

- Lecture 1 uses A = [[2, -1], [-1, 2]], b = [0, 3], x = [1, 2]. Its 3D example
  uses A = [[2, -1, 0], [-1, 2, -1], [0, -3, 4]], b = [0, -1, 4], x = [0, 0, 1].
- Lecture 2 uses A = [[1, 2, 1], [3, 8, 1], [0, 4, 1]], b = [2, 12, 2].
  Its pivots are 1, 2, 5 and solution [2, 1, -2]. Changing the last coefficient
  row to [0, 4, -4] produces the original contradiction 0 = -10.
- Lecture 3 uses A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]], AB = [[19, 22], [43, 50]].
  Its Gauss–Jordan example uses [[1, 3], [2, 5]] and inverse [[-5, 3], [2, -1]].
- Lecture 5 uses the original permutation example [[0, 1, 2], [1, 2, 3], [2, 6, 9]]
  and the exact R = [[1, 2], [3, 0], [0, 4]] from its Python slide.
  The new column-space demonstration applies the original definition to that R,
  so its numerical example is tied to the source rather than to the old Slidev demos.
- Lecture 9 uses the Canva columns (3, 2, 5), (4, 7, 2), (7, 9, 7).
  The relation is -v1 - v2 + v3 = 0, rank 2, nullity 1.

The source matrices are defined once in `python_examples/source_math.py` and
imported into `animations/source_scenes.py`. All old Slidev demonstrations are
excluded from the active deck, even where they covered similar concepts.

## Issues deliberately left in the originals for review

- Canva page 7 reverses the verbal dependence definition. The new code correctly
  demonstrates a nonzero dependency relation; the original page remains untouched.
- Presentation2 slide 6 describes its displayed outer product as a row times a
  column. The displayed multiplication is a column times a row. The new demo
  computes the column-times-row interpretation correctly.
- Canva's conclusion uses N(A) = 0 as shorthand. The precise independence test is
  N(A) = {0}.
- Canva's three blank ending pages remain for later review. Closing Q&A and
  Lecture 5's contact-placeholder/credit pages have been excluded.

## Fidelity boundaries

All five lectures have been rebuilt from their original elements. Text,
equation lettering, tables and diagrams use native SVG/HTML with source fonts,
colors, layout and wording. Original image and video assets remain intact.
There is no full-slide screenshot animation layer or delayed final screenshot.
The source PowerPoint files still match the supplied originals byte for byte.

The 529 native PowerPoint objects include inherited template artwork. Source
checks compare their prose and 159 original OMML equations with the actual
PPTX XML. Lecture 9 uses the native HTML text and vector shapes read from the
shared Canva design, with its original individual graphics and font assets
stored locally. All 29 original Canva pages, including repeated builds and blank
ending template pages, remain in order.

The original source errors listed above are preserved. Both objectives pages
have the requested smooth complete entrances. Between-slide transitions remain
instant, and all approved slide/link/icon/page-counter removals remain applied.
