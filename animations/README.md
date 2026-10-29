# Manim source and rendered clips

The presentation has twelve silent 720p/30fps Manim clips, two for each selected lecture. The MP4 files and JPG posters live in `public/animations`. Viewing the deck needs no Python installation.

| Lecture | Scenes |
| --- | --- |
| 1 | `RowIntersection`, `ColumnCombination` |
| 2 | `EliminationPivots`, `EliminationGeometry` |
| 3 | `MatrixComposition`, `GaussJordanInverse` |
| 5 | `MatrixTranspose`, `PermutationRows` |
| 6 | `ColumnSpaceSweep`, `NullspacePlane` |
| 9 | `DependenceAndBasis`, `BasisCoordinates` |

The clips start when their slide becomes active, loop continuously like GIFs, and pause when you leave. The reusable `HoverVideo.vue` player hides native controls until the pointer hovers over the video. Keyboard focus and touch access can also reveal the controls. A browser preference for reduced motion disables automatic playback.

## Regenerate

The supplied renders used Python 3.14 and Manim Community 0.22.1. The scenes use Pango text and need no LaTeX installation.

```powershell
python -m venv .venv-manim
.\.venv-manim\Scripts\python.exe -m pip install -r animations/requirements.txt
.\.venv-manim\Scripts\python.exe -m manim -qm --fps 30 --media_dir media -a animations/linear_algebra.py
.\.venv-manim\Scripts\python.exe -m manim -qm --fps 30 --media_dir media -a animations/expanded_scenes.py
.\.venv-manim\Scripts\python.exe animations/publish_clips.py --media media
```

`publish_clips.py` copies all twelve videos and extracts their poster images. Keep both media types in Git so the presentation works after pushing or deploying.
