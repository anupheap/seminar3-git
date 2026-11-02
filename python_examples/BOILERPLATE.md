# Code-synchronized visual boilerplate

[`boilerplate.py`](boilerplate.py) contains ten commented examples using the
existing `Scene` helpers and `CodeVisual.vue`. Each example pairs a builder with
three cumulative Python code states. Running the catalog leaves the active
presentation unchanged.

## Choose an example

| Example builder | What changes on each click |
| --- | --- |
| `moving_arrow` | Vector endpoint and attached label position |
| `moving_line` | A dashed line's endpoints |
| `moving_circle` | A point's center, then its radius |
| `moving_rectangle` | A box's position, then its width |
| `moving_text` | A label's position, then its text |
| `moving_polyline` | The vertices of an open path |
| `moving_polygon` | The corners of a closed, filled shape |
| `changing_matrix` | Cell values, a highlighted row, and a pivot outline |
| `rearranging_matrix` | Entries move during a transpose and row reversal |
| `fading_objects` | A point and label appear, then disappear |

From the repository root, in a Python environment with the project's numerical
dependencies installed:

```sh
python python_examples/boilerplate.py
# Optional: inspect all generated snapshots in a separate JSON file.
python python_examples/boilerplate.py --output /tmp/boilerplate-states.json
```

The catalog checks that the sample code executes, IDs are unique in every
snapshot, coordinates are finite, and objects retain their shape type and point
count across states.

## Add one to the presentation

This complete example adds the moving-arrow lesson.

1. Copy `moving_arrow(k, env)` from `boilerplate.py` into `visual_states.py`,
   above `BUILDERS`. The needed `Scene`, `chart`, `arrow`, and color names already
   exist there. `k` is the local click index; `env` contains the variables from
   the corresponding executed Python code state.

2. Append this entry to the array in `walkthroughs.json`. Set `slide` to the
   actual slide number after placing the slide in your deck. The zero below is
   a placeholder; `introducedLines` uses inclusive, one-based line numbers.

   ```json
   {
     "after": "Boilerplate examples",
     "lecture": 1,
     "title": "Python: moving an arrow",
     "figure": "boilerplate-arrow",
     "caption": "The arrow follows the vector computed by each code step.",
     "notes": "First double v, then translate its endpoint one unit right.",
     "steps": [
       "import numpy as np\nv = np.array([1., 1.])",
       "import numpy as np\nv = np.array([1., 1.])\nv = 2 * v",
       "import numpy as np\nv = np.array([1., 1.])\nv = 2 * v\nv = v + np.array([1., 0.])"
     ],
     "slide": 0,
     "introducedLines": [[1, 2], [3, 3], [4, 4]]
   }
   ```

3. Append `moving_arrow` to `BUILDERS` in `visual_states.py`. The current
   generator pairs lessons and builders by list position, so both must be
   appended together in the same order.

4. Add the following slide to `slides.md`. Keep its code identical to the
   `steps` above. `--code-lines` and `data-code-lines` reserve room for the
   longest code state.

   `````md
   ---

   # Python: moving an arrow

   <div class="code-pair">
   <div class="code-panel" style="--code-lines: 4" data-code-lines="4">

   ````md magic-move {duration:700}
   ```python
   import numpy as np
   v = np.array([1., 1.])
   ```
   ```python
   import numpy as np
   v = np.array([1., 1.])
   v = 2 * v
   ```
   ```python
   import numpy as np
   v = np.array([1., 1.])
   v = 2 * v
   v = v + np.array([1., 0.])
   ```
   ````

   </div>
   <CodeVisual lesson="boilerplate-arrow" />
   </div>

   <div class="step-hint">Space advances the code. Left arrow goes back.</div>
   `````

5. Generate the snapshots, run the audit, and start Slidev:

   ```sh
   python python_examples/visual_states.py
   python python_examples/audit.py
   npm run dev
   ```

   The generator's current final print message hardcodes 36 states; after adding
   a lesson, the audit reports the actual count. For another example, substitute
   its builder, lesson ID, and cumulative code from `EXAMPLES` in
   `boilerplate.py`. Give each new lesson a unique `figure` value.

   The existing audit verifies code order and exported variables for new lesson
   IDs. Add lesson-specific geometry checks to `audit.py` when the new diagram
   needs mathematical validation. Reserve exports named `rank`, `nullity`, and
   `display` for their current audit conventions, or update those conventions.

## Control the animation

- **Move or resize:** keep the same ID and change its coordinate values.
- **Fade in/out:** include an object in some snapshots and omit it in others,
  or change its opacity through helpers that accept `opacity`.
- **Change text:** keep the ID and replace the string. The renderer switches
  text halfway through the movement.
- **Change color/style:** those properties also switch halfway through; only
  numeric `points` and `opacity` are interpolated.
- **Morph paths:** preserve vertex count and ordering. A different point count
  causes the geometry to snap to its new coordinates.
- **Matrix calculations:** default matrix IDs follow `(row, column)`, keeping
  cells fixed while their values change.
- **Matrix rearrangement:** `value_ids=True` tracks entries by their values.
  Use it only for unique, unchanged values. For duplicate entries, assign
  custom IDs to the text and background rectangle for each logical entry.

The SVG canvas is `420 × 295`. Raw SVG coordinates start at the top-left, with
positive y downward. `chart()` returns `p(x, y)` for ordinary mathematical
coordinates, with positive y upward. `dot()` radii, line widths, text sizes,
and matrix cell spacing remain in SVG screen units.

Both Magic Move and the diagram use the same local Slidev click counter. The
diagram duration is currently `700` milliseconds in `CodeVisual.vue`; match the
Magic Move duration if you change it. Back navigation reuses the same states.
Reduced-motion settings make the diagram switch directly to its target state.
