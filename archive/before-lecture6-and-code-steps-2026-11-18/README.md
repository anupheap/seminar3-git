# Seminar III linear algebra

The active Slidev presentation contains **81 original slides**, in lecture order
**1 → 2 → 3 → 5 → 9**. All five lectures have been rebuilt from their original
objects and styles. The rejected rewritten outline and screenshot playback
components are archived and are not used by the presentation.

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
| 9 | Supplied Canva design 1–29 | CanvaSource.vue | 29 |

`slides.md` sets the order. Each file under `lectures/` references its original
source objects. `sources/lecture*-native.json` stores native PowerPoint SVG
objects, source text, original OMML equations and timing data. Canva's native
HTML lives in `sources/canva-native/`, with its original computed styling in
`styles/canva-native.css`. The presentation loads local assets and fonts.

PowerPoint text, equation lettering, tables, lines, axes and graph shapes are
native SVG DOM elements. Canva text and vector shapes are native HTML/SVG.
Original logos, screenshots, handwritten illustrations and code images remain
original image assets. The original embedded video retains its source crop and
trim. The MATLAB source slides retain native editable code text.

Nunito, Inter, Montserrat, Playfair Display and the original Canva Quicksand
faces are bundled. Cambria Math, Calibri, Consolas and Goudy Old Style use the
original Windows fonts available on the authoring machine.

There are no full-slide screenshot animation layers or final screenshot swaps.
CSS recreates the original PowerPoint click groups and timings. Both Learning
Objectives pages use complete staggered entrances. Canva's repeated page builds
remain in source order. Between-slide changes are instant.

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

The source builder regenerates lecture references and native object manifests
from the cached source exports. Both older entry points, `build-lectures.py` and
`native_lectures.py`, now delegate to it. They cannot restore the rejected deck.
Native data and equation measurements are committed, so viewing/building does
not require PowerPoint, Python, Playwright or Canva access.

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
the active deck. No new Manim or code pages were added during this faithful
rebuild.

`public/sources/slides/` contains reference renders only. Earlier implementations
and checkpoints live under `archive/`. Browser captures and other temporary
verification files stay under ignored `.cache/`.
