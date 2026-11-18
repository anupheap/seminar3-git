# New source-based Manim scenes

The appended animation slides have been removed from the active presentation.
`source_scenes.py` retains eleven scenes for future work and imports the
same numeric constants as `python_examples/source_math.py`.

| Lecture | Scenes |
| --- | --- |
| 1 | `L1Rows`, `L1Columns`, `L1ThreePlanes` |
| 2 | `L2Elimination` |
| 3 | `L3Products`, `L3Inverse` |
| 5 | `L5Permutation`, `L5Symmetry`, `L5ColumnSpace` |
| 9 | `L9Dependence`, `L9Basis` |

```powershell
python -m venv .venv-manim
.\.venv-manim\Scripts\python.exe -m pip install -r animations/requirements.txt
.\.venv-manim\Scripts\python.exe animations/render_sources.py
```

Manim Community 0.22.1 renders at 1280 × 720 and 24 fps. These scenes use Pango
text rather than LaTeX. `render_sources.py` publishes complete videos and their
posters to `public/animations/source/`. Rendering intermediates go in `.cache`.
To render a subset, pass `--scenes L2Elimination L9Basis`.

If a clip is re-enabled in a future lesson, its player starts it on entering the slide and pauses it on leaving.
Controls appear on hover, keyboard focus or touch. Reduced-motion preferences
disable automatic playback.

Previous scenes and clips are under `archive/legacy/` and are not referenced by
the active deck. None of those rendered videos was reused for these new scenes.
