# Manim source and rendered clips

The presentation has fourteen silent clips. Lecture 1 has four clips covering the guide's 2D and 3D row and column pictures; each other selected lecture has two. The MP4 files and JPG posters live in `public/animations`. Viewing the deck needs no Python installation.

| Lecture | Scenes |
| --- | --- |
| 1 | `RowIntersection`, `ThreePlaneIntersection`, `ColumnCombination`, `ThreeColumnCombination` |
| 2 | `EliminationPivots`, `EliminationGeometry` |
| 3 | `MatrixComposition`, `GaussJordanInverse` |
| 5 | `MatrixTranspose`, `PermutationRows` |
| 6 | `ColumnSpaceSweep`, `NullspacePlane` |
| 9 | `DependenceAndBasis`, `BasisCoordinates` |

The clips start when their slide becomes active, loop continuously like GIFs, and pause when you leave. The reusable `HoverVideo.vue` player hides native controls until the pointer hovers over the video. Keyboard focus and touch access can also reveal the controls. A browser preference for reduced motion disables automatic playback.

## Regenerate

The Manim scene definitions use Python 3.14 and Manim Community 0.22.1. They use Pango text and need no LaTeX installation. The current Lecture 1 MP4 and JPG assets were rendered with `render_lecture1_fallback.py` (Pillow, NumPy, ffmpeg) because Manim was unavailable in the editing environment. Both renderers use the same systems and solutions.

```powershell
python -m venv .venv-manim
.\.venv-manim\Scripts\python.exe -m pip install -r animations/requirements.txt
.\.venv-manim\Scripts\python.exe -m manim -qm --fps 30 --media_dir media -a animations/linear_algebra.py
.\.venv-manim\Scripts\python.exe -m manim -qm --fps 30 --media_dir media -a animations/expanded_scenes.py
.\.venv-manim\Scripts\python.exe animations/publish_clips.py --media media
```

`publish_clips.py` copies the rendered videos and extracts their poster images. Use `--scenes RowIntersection ThreePlaneIntersection ColumnCombination ThreeColumnCombination` to publish only Lecture 1 after rendering those scenes. Alternatively, run `python animations/render_lecture1_fallback.py` to regenerate the four current Lecture 1 clips. Keep both media types in Git so the presentation works after pushing or deploying.
