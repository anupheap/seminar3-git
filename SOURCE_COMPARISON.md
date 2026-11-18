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
| 6 | MIT OCW 18.06 Lecture 6 | 20 newly authored slides on column space and nullspace |
| 9 | [Canva design DAHa-hNCW00](https://www.canva.com/design/DAHa-hNCW00/iV35G0qo8ZAcpbj6MrsVOg/edit) | All 29 pages, including repeated reveal pages and template endings |

## Retained code and Manim source map

The appended demo pages below have all been excluded from the active deck.
Their source files and assets are retained for future lecture-by-lecture editing.
This exclusion does not apply to the newly requested Lecture 6.

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

The older source matrices are defined once in `python_examples/source_math.py` and
imported into `animations/source_scenes.py`. All old Slidev demonstrations are
excluded from the active deck, even where they covered similar concepts.

## Lecture 6 and read-only code

The active order is 1, 2, 3, 5, 6, 9, totaling 101 slides. The new Lecture 6
occupies combined pages 53–72 and follows
[Strang's column space and nullspace lecture](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/).
It uses A = [[1, 1, 2], [2, 1, 3], [3, 1, 4], [4, 1, 5]], with a₃ = a₁ + a₂,
rank 2 and nullspace span{(1, 1, −1)}. Additional right-hand-side examples are
derived from this matrix. All new Python stages execute during code-data generation.

Lecture 6 borrows the supplied Semiconductors presentation's compositions:
vertical title rules, split layouts, dominant numbers, flat panels and takeaway
bands. It uses a 3Blue1Brown-inspired palette and the requested sans-serif pairing,
Space Grotesk with Inter. This styling is scoped to Lecture 6. The reference's
semiconductor content is not imported.

Lecture 6 now states both space definitions before using the four-by-three
matrix. The column-space example computes b = (1, 3, 5, 7) from x = (2, −1, 0),
and the nullspace example derives N(A) = span{(1, 1, −1)} by row reduction.
The schematic input/output map and nullspace line distinguish the ambient
spaces. Its generated SymPy example uses the same nullspace vector shown on
the slides, with every code stage executed during generation.

The original four code sections now use native read-only Magic Move sequences:
combined pages 39, 40, 48 and 97. The two original MATLAB examples retain their
code, now with the Lecture 3 theme. The two original Python screenshots are replaced
with equivalent native code and output. Lecture 6 adds two related sequences on
pages 64 and 69, native SVG geometry, and the click-controlled Manim scene from
`animations/lecture6_scenes.py`. No editable code editor is present.

## Issues deliberately left in the originals for review

The live deck has three user-requested changes to the source presentation:
combined page 15 uses the original PowerPoint render as a still image so all
three visuals appear together; combined page 33 omits the final “shop 2” line
from its example block; and combined page 40 changes the title to “Inverse
Matrice with gauss-jordan method.” The original PowerPoint files and canonical
source manifests remain unchanged. These live edits are recorded in
`sources/deck-edits.json`.

- Canva page 7 reverses the verbal dependence definition. The new code correctly
  demonstrates a nonzero dependency relation; the original page remains untouched.
- Presentation2 slide 6 describes its displayed outer product as a row times a
  column. The displayed multiplication is a column times a row. The new demo
  computes the column-times-row interpretation correctly.
- Canva's conclusion uses N(A) = 0 as shorthand. The precise independence test is
  N(A) = {0}.
- Canva's three blank ending pages remain for later review. Closing Q&A and
  Lecture 5's contact-placeholder/credit pages have been excluded.
- The workspace-level `Lecture5.pptx` differs from the versioned copy in
  `public/sources/powerpoint/`. The active deck uses the versioned copy. This
  duplicate-file mismatch currently stops the full source check; neither file
  was changed during these slide edits.

## Fidelity boundaries

All five lectures have been rebuilt from their original elements. Text,
equation lettering, tables and diagrams use native SVG/HTML with source fonts,
colors, layout and wording. Original image and video assets remain intact.
Lecture 3 is the requested design exception: its text and objects are enlarged
and redistributed across the slide, using an Anthropic-inspired paper, charcoal
and terracotta palette with Source Serif 4/Inter typography. Original words and
equations stay intact. Theme and layout overrides live outside the canonical
source manifest. All six code sections have larger type. Each print statement
and its corresponding output reveal together using the actual statement's
opacity; earlier results remain visible. The MATLAB verification statements
also display their results. Canva source page 2 (combined page 74) uses the original
liquid-animation assets in a native SVG player with the original recoloring.
The full Canva animation audit covers all 29 pages and 234 source elements:
eight saved element effects, three original liquid loops, and 44 graphic/group
entrances after adding the requested float motion. The original brush-mask
video is used only as a luminance mask on its individual picture. No picture
or full slide is swapped at the end of the effect. Source settings and the
derived motion plan are stored separately from the original HTML and styling.
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
