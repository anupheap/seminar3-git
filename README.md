# Linear Algebra seminar

A **51-slide** Slidev presentation based on Gilbert Strang's MIT 18.06 lectures **1, 2, 3, 5, 6, and 9**. It follows the Spring 2010 MIT OpenCourseWare publication, whose lecture videos were recorded in Fall 1999.

A title page introduces each of the six selected lectures. The deck includes **12 Manim clips** and **12 Shiki Magic Move Python walkthroughs** with 36 synchronized code and diagram states. Twelve standalone Python figures are also included. Worked examples, speaker notes, a practice problem, and direct lecture links are included. Allow about 55 minutes when presenting all code steps.

## View

From the repository root, using Node.js 24:

```powershell
npm ci
npm run dev
```

Open the URL printed by Slidev, normally `http://localhost:3030`. Space or Right advances the code and its visualization together before advancing to the next slide. Left restores the previous code and diagram state. Magic Move's delayed token entry is disabled, so new code starts appearing as the diagram begins its 700 ms transition. Code panels reserve enough space for the longest step. Slides have directional entrance and exit transitions. Press `p` for presenter mode and speaker notes.

Manim clips start on entry, repeat continuously like GIFs, and pause when you leave. Playback controls appear when the pointer hovers over the video and disappear when it leaves. Keyboard focus or a touch tap can also reveal the controls. Reduced-motion browser settings disable automatic video playback. The Python code illustrates computations already verified locally. The browser does not run a Python interpreter.

## Build

```powershell
npm run build
```

The static site appears in `dist/`. Netlify and Vercel use the repository root. All rendered assets in `public/animations` and `public/python` must be included in commits and pushes.

## Python examples and plots

Viewing needs only Node.js. To rerun the numerical examples or regenerate the figures, use a separate Python environment:

```powershell
python -m venv .venv-manim
.\.venv-manim\Scripts\python.exe -m pip install -r python_examples/requirements.txt
.\.venv-manim\Scripts\python.exe python_examples/examples.py
.\.venv-manim\Scripts\python.exe python_examples/visual_states.py
.\.venv-manim\Scripts\python.exe python_examples/audit.py
.\.venv-manim\Scripts\python.exe python_examples/illustrate.py
```

`python_examples/examples.py` contains all twelve complete examples with checks. `python_examples/walkthroughs.json` records all code states. Each new state preserves the previous code and appends the next calculations. `visual_states.py` executes every state and writes the numerical scene data to `visual_states.json`, which the browser interpolates as the code changes. Regenerate that file after editing the Python walkthroughs. `audit.py` checks cumulative code order, available variables, displayed matrix entries, and plotted results, and writes `audit.json`. Each visualization represents the result after all newly visible lines in that click step. `illustrate.py` generates the standalone SVG figures and PNG previews. The numerical rank calculations use floating-point tolerances. A numerical counterexample can disprove closure, while a few successful examples alone cannot prove closure.

## Edit

- `slides.md`: content, equations, Magic Move code, and speaker notes.
- `styles/style.css`: layout and typography, loaded by `styles/index.ts`.
- `components/MathFilm.vue`: video playback tied to the active slide.
- `components/HoverVideo.vue`: reusable muted looping player with hover controls.
- `components/CodeVisual.vue`: diagrams tied to the local Magic Move click index.
- `animations/linear_algebra.py` and `animations/expanded_scenes.py`: editable Manim scenes.
- `animations/README.md`: clip regeneration and publication commands.
- `python_examples/illustrate.py`: Matplotlib illustrations.
- `python_examples/visual_states.py`: Python computations and synchronized diagram geometry.

## Sources

[MIT OpenCourseWare: 18.06 Linear Algebra, Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/). The final slide and relevant speaker notes link directly to the six lectures. The opening system and inverse matrix follow Strang's examples. Other matrices, numerical walkthroughs, plots, and animations were created for this seminar.

[Slidev: Shiki Magic Move](https://sli.dev/features/shiki-magic-move) documents the code transitions.

Numerical API references: [NumPy solve](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html), [NumPy matrix rank](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html), and [SciPy null space](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.null_space.html).
