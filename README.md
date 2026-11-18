# Seminar III linear algebra

The active Slidev presentation contains **101 slides**, in lecture order
**1 → 2 → 3 → 5 → 6 → 9**: 81 original slides and 20 new Lecture 6 slides.
The original five decks retain their source content. Lecture 6 uses
the supplied Semiconductors deck's layout language, a 3Blue1Brown-inspired
palette, and Space Grotesk headings paired with Inter body text.

Lecture 3 uses an Anthropic-inspired editorial theme across all 12 pages:
paper cream, charcoal, a restrained terracotta accent, Source Serif 4 headings
and Inter body text. Larger text and fuller layouts preserve the original words
and mathematics. `sources/lecture3-layout.json` keeps these overrides separate
from the untouched source objects; `styles/lecture-three.css` scopes the theme.

## Run

```powershell
npm ci
npx slidev slides.md --port 3031
npm run build
```

Open [the current preview](http://localhost:3031/2). Port 3030 previously served
an older presentation. Viewing and building the deck requires Node only.

## Sources and structure

| Lecture | Active source pages | Native renderer | Pages |
| --- | --- | --- | --- |
| 1 | Seminar.pptx 1–17 | LectureOneSource.vue | 17 |
| 2 | Seminar.pptx 19–30 | PowerPointSource.vue | 12 |
| 3 | Presentation2.pptx 1–12 | PowerPointSource.vue | 12 |
| 5 | Lecture5.pptx 1–11 | PowerPointSource.vue | 11 |
| 6 | Strang's MIT 18.06 Lecture 6 | Native Markdown, KaTeX, SVG and Manim | 20 |
| 9 | Supplied Canva design 1–29 | CanvaSource.vue | 29 |

`slides.md` sets the order. Each file under `lectures/` references its original
source objects. `sources/lecture*-native.json` stores native PowerPoint SVG
objects, source text, original OMML equations and timing data. Canva's native
HTML lives in `sources/canva-native/`, with its original computed styling in
`styles/canva-native.css`. The presentation loads local assets and fonts.

PowerPoint text, equation lettering, tables, lines, axes and graph shapes are
native SVG DOM elements. Canva text and vector shapes are native HTML/SVG.
Original logos, non-code screenshots and handwritten illustrations remain
original image assets. The original embedded video retains its source crop and
trim. All four original code sections now use read-only Magic Move sequences,
with cumulative code and matching output. No editable Monaco editor is used.
Each print statement has its own step. Its matching output follows the actual
opacity of the statement's entrance, so both reveal together on the same click.
Earlier output remains visible. The MATLAB examples also reveal the results of
unsuppressed statements and their identity/inverse checks. Code and output fonts
are larger in all six sections, with wider panels where needed.

Source Serif 4, Space Grotesk, Nunito, Inter, Montserrat, Playfair Display and the original Canva Quicksand
faces are bundled. Cambria Math, Calibri, Consolas and Goudy Old Style use the
original Windows fonts available on the authoring machine.

There are no full-slide screenshot animation layers or final screenshot swaps.
CSS recreates the original PowerPoint click groups and timings. Both Learning
Objectives pages use complete staggered entrances. Canva's repeated page builds
remain in source order. Between-slide changes are instant.
Slide 74 plays the original green, yellow and purple Canva liquid animations
from bundled Lottie data through the SVG renderer. They pause off-slide and
respect reduced motion. `sources/canva-liquid.json` records the original assets.

Lecture 9's 29 pages have a separate motion audit in
`sources/canva-animation-settings.json`. It preserves the eight saved element
effects from the original design. `sources/canva-motion.json` applies 44 graphic
or group entrances, including the requested float entrance on other graphics.
Directional wipes use native clipping, and the cover's brush reveal uses Canva's
original 1.6-second luminance mask on the same original picture element. The
picture stays mounted throughout. Native code panels on page 97 take the place
of their original picture entrances, while retaining their stepped code/output.
Text, layouts, lecture order and instant between-slide changes remain intact.

## Approved removals

The opening added index, all added page counters and source labels, Original
PowerPoint links, Canva player/source controls, closing Q&A pages, Lecture 5's
Slidesgo page and the appended animation/Python demo pages remain removed.
The two requested icons on Lecture 1's objectives page remain removed.
`sources/deck-edits.json` records those decisions. Original source files are
unchanged. Native source checks preserve the original wording, including source
errors, rather than silently correcting or rewriting it.

## Rebuild and verify

```powershell
python scripts/build-source-deck.py
python scripts/check-source-deck.py
npm run build
```

The source builder regenerates the original lecture references and native object
manifests from the cached source exports, then reapplies the four code sequences.
The authored Lecture 6 prose stays intact; the builder refreshes its two code
sequences and click counts. Code stages and computed output
live in `sources/code-walkthroughs.json`; `build-code-walkthroughs.py` verifies
every Python stage and the MATLAB matrix results. Both older entry points, `build-lectures.py` and
`native_lectures.py`, now delegate to it. They cannot restore the rejected deck.
Native data and equation measurements are committed, so viewing/building does
not require PowerPoint, Python, Playwright or Canva access.

`scripts/build-lecture3-layout.py` regenerates Lecture 3's layout overrides and
verifies that reflowed text preserves every original word. This source-generation
step uses Pillow for font measurements; ordinary viewing and builds do not.

`scripts/build-canva-motion.py` rebuilds motion bindings from the saved audit and
native HTML. To refresh the source settings, use
`scripts/import-canva-animation-settings.mjs --browser PATH`. It reads the
shared design and downloads its public mask asset, without editing Canva or
storing account/session data. The regular source builder reapplies these bindings.

Refreshing source exports uses Windows PowerPoint, Python with `lxml`, and
Playwright. `export-lecture1-native.ps1` and `export-remaining-native.ps1` read the
preserved presentations without saving them. `export-inherited-native.ps1`
retains inherited template artwork. Original equation placement measurements
are stored in `sources/lecture*-math-metrics.json`.

`import-canva-native.mjs` reads the supplied shared viewer without editing the
design. It waits for fonts and source images before importing the native content.
Use its `--browser PATH` option to select a Chromium executable. Playwright is
available from `.cache/qa/node_modules` in this workspace.

## Retained teaching code

`python_examples/source_math.py`, `animations/source_scenes.py`, their generated
outputs and source clips remain available for later lecture work. Their appended
demo slides stay excluded. The originals' MATLAB and Python material stays in
the active deck as read-only, stepped code. Combined pages 39, 40, 48 and 97
contain those four sections. Original headings stay verbatim. Lecture 3's two
sections use the requested editorial theme; the other sections retain their
source designs.

## Lecture 6

Lecture 6 starts at [combined page 53](http://localhost:3031/53). It follows
[Gilbert Strang's Column Space and Nullspace lecture](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-6-column-space-and-nullspace/),
using the lecture's 4 × 3 matrix. The two Python walkthroughs appear on combined
pages 64 and 69. Native SVG diagrams respond to slide clicks, and the Manim
scene on page 55 pauses between vector addition and scaling.

`animations/lecture6_scenes.py` is the reproducible Manim source. To render it:

```powershell
.venv-manim\Scripts\python.exe -m manim -qm --fps 24 --media_dir .cache/lecture6-manim animations/lecture6_scenes.py SubspaceClosure
```

The deck uses the resulting clip at `public/animations/lecture6/SubspaceClosure.mp4`.
The new design is scoped to `layouts/lecture-six.vue` and `styles/lecture-six.css`.

`public/sources/slides/` contains reference renders only. Earlier implementations
and checkpoints live under `archive/`. Browser captures and other temporary
verification files stay under ignored `.cache/`.
