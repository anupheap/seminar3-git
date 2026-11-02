"""Commented builders for the existing CodeVisual.vue renderer.

Run from the repository root:
    python python_examples/boilerplate.py
    python python_examples/boilerplate.py --output /tmp/boilerplate-states.json

Each builder takes a click index (k) and the variables produced by that code
step (env). Copy a builder into visual_states.py when using it in a lesson.
The examples below are a separate catalog; running them does not edit the deck.
See BOILERPLATE.md for the complete connection to a Slidev code block.
"""

import argparse
import json
from pathlib import Path

import numpy as np

from visual_states import BLUE, GREEN, ORANGE, Scene, arrow, chart


# SHARED PATTERN FOR EVERY BUILDER BELOW:
# - k = 0 is the initial state; k = 1 and k = 2 follow the next two clicks.
# - env contains the variables from the matching code block in EXAMPLES.
# - Build one complete target snapshot per call; Vue supplies the frames between.
# - Stable IDs connect the same logical object across those snapshots.
# - finish() returns drawing nodes and optional numeric values for the audit.
# - Convert NumPy arrays with tolist() so those exported values are JSON-safe.


# 01. ARROW: change v to scale or redirect a vector from a fixed origin.
def moving_arrow(k, env):
    """Move an arrow's endpoint as the code changes vector v."""
    s = Scene('Moving arrow', f'Step {k + 1}: the arrow shows the current v.')
    # Input: env['v'] is a two-element NumPy array [x, y].
    # p(x, y) converts mathematical coordinates into SVG screen coordinates.
    # Keep bounds fixed across clicks so the coordinate system stays consistent.
    p = chart(s, bounds=(-1, 5, -1, 5))
    # Keep "vector" unchanged across steps so the same arrow moves.
    # The label gets its own stable ID, "vector-label", automatically.
    # (0, 0) is the tail. Change it too if the whole arrow should translate.
    arrow(s, 'vector', p, (0, 0), env['v'], BLUE, name='v')
    return s.finish(v=env['v'].tolist())


# 02. LINE: change start/end to translate, rotate, or lengthen a segment.
def moving_line(k, env):
    """Move either endpoint of a line; dashed lines use the same helper."""
    s = Scene('Moving line', f'Step {k + 1}: code sets the two endpoints.')
    # Inputs: env['start'] and env['end'] are mathematical [x, y] coordinates.
    p = chart(s, bounds=(-1, 5, -1, 5))
    # Both endpoints interpolate under the stable ID "segment".
    # Set dashed=False for a solid line; width controls its stroke thickness.
    s.line('segment', p(*env['start']), p(*env['end']),
           color=ORANGE, width=3, dashed=True)
    return s.finish(start=env['start'].tolist(), end=env['end'].tolist())


# 03. CIRCLE: change center for movement and radius for growth/shrinkage.
def moving_circle(k, env):
    """Move a point and change its radius."""
    s = Scene('Moving circle', f'Step {k + 1}: position and radius change.')
    p = chart(s, bounds=(-1, 5, -1, 5))
    # Inputs: env['center'] is [x, y]; env['radius'] is a scalar.
    # The center uses chart coordinates; r is measured in SVG screen units.
    # "point" preserves identity while its center and radius interpolate.
    s.dot('point', p(*env['center']), color=GREEN, r=env['radius'])
    return s.finish(center=env['center'].tolist(), radius=env['radius'])


# 04. RECTANGLE: use a stable box for bars, regions, or moving highlights.
def moving_rectangle(k, env):
    """Move and resize a rectangle, such as a bar or highlight box."""
    s = Scene('Moving rectangle', f'Step {k + 1}: the box moves or resizes.')
    # Raw SVG coordinates: x increases rightward, y increases downward.
    # The canvas is 420 wide by 295 high. box = [x, y, width, height].
    # Input: env['box'] contains those four numbers in that exact order.
    x, y, width, height = env['box']
    # All four dimensions interpolate. opacity=.3 makes the fill translucent.
    # Use fill='none' for an outline-only highlight around another object.
    s.rect('box', x, y, width, height, fill=BLUE, opacity=.3,
           stroke=BLUE, width=2)
    return s.finish(box=env['box'].tolist())


# 05. TEXT: animate label placement and replace its content at a code step.
def moving_text(k, env):
    """Move a label and replace its message."""
    s = Scene('Moving text', f'Step {k + 1}: the label uses the code variables.')
    # Inputs: env['x'] is a horizontal SVG position; env['message'] is a string.
    # y=155 stays fixed. anchor='middle' centers the text at that position.
    # Position animates smoothly. Text, font size, and color switch halfway
    # through the transition; they are not interpolated like coordinates.
    s.text('message', env['x'], 155, env['message'], size=22,
           color=BLUE, anchor='middle', weight=600)
    # finish() exports numerical values for audit.py; text is already in nodes.
    return s.finish(x=env['x'])


# 06. POLYLINE: reshape an open path by moving corresponding vertices.
def moving_polyline(k, env):
    """Move the vertices of an open path."""
    s = Scene('Moving polyline', f'Step {k + 1}: path vertices change position.')
    # Input: env['path'] has one [x, y] row per vertex, in drawing order.
    # Use the same number and ordering of vertices in every state for a morph.
    # These points are already in SVG screen coordinates, so no p() is needed.
    s.poly('path', env['path'], color=ORANGE, width=3)
    return s.finish(path=env['path'].tolist())


# 07. POLYGON: reshape a filled region while preserving corner identity.
def moving_polygon(k, env):
    """Move the vertices of a closed, filled shape."""
    s = Scene('Moving polygon', f'Step {k + 1}: the four corners move.')
    # Input: env['corners'] contains four [x, y] rows in perimeter order.
    # Keep that ordering across clicks so each old corner moves to its partner.
    # closed=True selects an SVG polygon instead of an open polyline.
    # The renderer connects the last corner back to the first automatically.
    s.poly('region', env['corners'], color=GREEN, fill=GREEN,
           opacity=.35, width=3, closed=True)
    return s.finish(corners=env['corners'].tolist())


# 08. MATRIX VALUES: show calculations while keeping each cell in place.
def changing_matrix(k, env):
    """Update values at fixed matrix cells and highlight a row/pivot."""
    s = Scene('Changing matrix', f'Step {k + 1}: entries show the current A.')
    # Input: env['A'] is a two-dimensional NumPy array.
    # Default IDs follow (row, column), so each cell stays in its position.
    # Changed numbers switch halfway through the animation.
    # x/y give the matrix center; cell gives each cell's spacing.
    # active_rows=(1,) highlights the second row from the first click onward.
    # pivots=((0, 0),) adds an outline around the top-left cell at every step.
    s.matrix('matrix', env['A'], x=210, y=145, cell=48, title='A',
             active_rows=(1,) if k >= 1 else (), pivots=((0, 0),))
    return s.finish(A=env['A'].tolist())


# 09. MATRIX MOVEMENT: preserve each entry while moving it to another cell.
def rearranging_matrix(k, env):
    """Move entries between cells for a transpose or row permutation."""
    s = Scene('Rearranging matrix', f'Step {k + 1}: the entries follow R.')
    # Input: env['R'] is the current arrangement of the same six unique values.
    # Here IDs follow VALUES, so the entry "4" moves to its new cell.
    # Use value_ids=True only when every entry is unique and its value stays
    # unchanged. Repeated values need custom unique IDs per logical entry.
    # Cell backgrounds move with the numbers; brackets resize to the new shape.
    s.matrix('entry', env['R'], x=210, y=145, cell=48, value_ids=True)
    return s.finish(R=env['R'].tolist())


# 10. VISIBILITY: add/remove objects at a code step to fade them in/out.
def fading_objects(k, env):
    """Introduce and remove several objects together on a code step."""
    s = Scene('Fade in and out', f'Step {k + 1}: visible = {env["visible"]}.')
    # Input: env['visible'] is a boolean set by the matching code block.
    # This controls both objects together; use separate flags for independent
    # appearance. Their coordinates below use raw SVG screen units.
    if env['visible']:
        # Objects absent from another step are given opacity 0 by the renderer.
        # Reuse these IDs when the objects return, including when going back.
        s.dot('answer-point', (210, 130), color=GREEN, r=12)
        s.text('answer-label', 210, 175, 'Answer found', size=20,
               color=GREEN, anchor='middle')
    return s.finish(visible=env['visible'])


# CODE-STEP HELPER: turn additions into complete, cumulative code blocks.
def cumulative_steps(*additions):
    """Append new lines while preserving the earlier code in every state."""
    steps = []
    source = ''
    for addition in additions:
        # The next block retains all previous lines and appends this addition.
        # Each complete block is executed from scratch to build its snapshot.
        source = source + '\n' + addition if source else addition
        steps.append(source)
    return steps


# Each entry pairs a visual builder with the actual Python code for its clicks.
# Copy the resulting cumulative strings into walkthroughs.json and Magic Move.
# Comments beside the strings explain each addition; they are not part of the
# code shown on the slide. k=0 is visible on entry, before the first click.
EXAMPLES = {
    # ARROW CODE: v goes (1, 1) -> (2, 2) -> (3, 2).
    'boilerplate-arrow': dict(
        title='Moving arrow', builder=moving_arrow,
        steps=cumulative_steps(
            # Initial (k=0): draw a vector from the origin to (1, 1).
            'import numpy as np\nv = np.array([1., 1.])',
            # First click (k=1): double its length without changing direction.
            'v = 2 * v',
            # Second click (k=2): shift its endpoint one unit to the right.
            'v = v + np.array([1., 0.])')),
    # LINE CODE: move the endpoint first, then move the start point.
    'boilerplate-line': dict(
        title='Moving line', builder=moving_line,
        steps=cumulative_steps(
            # Initial: segment from (0, 0) to (1, 1).
            'import numpy as np\nstart = np.array([0., 0.])\nend = np.array([1., 1.])',
            # First click: keep the tail fixed and move the other endpoint.
            'end = np.array([3., 2.])',
            # Second click: move the tail while the endpoint stays at (3, 2).
            'start = np.array([1., 2.])')),
    # CIRCLE CODE: translate the point, then enlarge it at its new position.
    'boilerplate-circle': dict(
        title='Moving circle', builder=moving_circle,
        steps=cumulative_steps(
            # Initial: center (1, 1), radius 5 SVG units.
            'import numpy as np\ncenter = np.array([1., 1.])\nradius = 5',
            # First click: move the center to (3, 2), keeping the same radius.
            'center = np.array([3., 2.])',
            # Second click: grow the circle to radius 12 in place.
            'radius = 12')),
    # RECTANGLE CODE: box uses [left, top, width, height] in SVG screen units.
    'boilerplate-rectangle': dict(
        title='Moving rectangle', builder=moving_rectangle,
        steps=cumulative_steps(
            # Initial: place a 90-by-55 box with its top-left at (60, 100).
            'import numpy as np\nbox = np.array([60., 100., 90., 55.])',
            # First click: move its left edge to x=160 without resizing it.
            'box[0] = 160',
            # Second click: extend the width to 180 while the left edge stays.
            'box[2] = 180')),
    # TEXT CODE: move the same label, then replace its message.
    'boilerplate-text': dict(
        title='Moving text', builder=moving_text,
        steps=cumulative_steps(
            # Initial: center the label "Start" horizontally at x=100.
            'x = 100\nmessage = "Start"',
            # First click: slide that label to x=300.
            'x = 300',
            # Second click: switch the text halfway through the transition.
            'message = "Finished"')),
    # POLYLINE CODE: keep three vertices and move their coordinates.
    'boilerplate-polyline': dict(
        title='Moving polyline', builder=moving_polyline,
        steps=cumulative_steps(
            # Initial: an open path through three SVG screen positions.
            'import numpy as np\npath = np.array([[60., 200.], [170., 100.], [300., 180.]])',
            # First click: reshape the path by moving only its middle vertex.
            'path[1] = [210., 70.]',
            # Second click: translate every vertex 20 right and 15 down.
            'path += np.array([20., 15.])')),
    # POLYGON CODE: resize a four-corner region, then translate the whole region.
    'boilerplate-polygon': dict(
        title='Moving polygon', builder=moving_polygon,
        steps=cumulative_steps(
            # Initial: corners go clockwise from the top-left of a rectangle.
            'import numpy as np\ncorners = np.array([[90., 90.], [230., 90.], [230., 210.], [90., 210.]])',
            # First click: move the two right-hand corners 70 units right.
            'corners[[1, 2], 0] += 70',
            # Second click: move all four corners 20 right and 10 down.
            'corners += np.array([20., 10.])')),
    # MATRIX-VALUE CODE: row operations turn A into the identity matrix.
    'boilerplate-matrix-values': dict(
        title='Changing matrix', builder=changing_matrix,
        steps=cumulative_steps(
            # Initial: show [[1, 2], [2, 5]] in fixed matrix cells.
            'import numpy as np\nA = np.array([[1., 2.], [2., 5.]])',
            # First click: row 2 -= 2 * row 1, giving [[1, 2], [0, 1]].
            'A[1] -= 2 * A[0]',
            # Second click: row 1 -= 2 * row 2, giving [[1, 0], [0, 1]].
            'A[0] -= 2 * A[1]')),
    # MATRIX-MOVE CODE: use unique values so each number can keep its own ID.
    'boilerplate-matrix-move': dict(
        title='Rearranging matrix', builder=rearranging_matrix,
        steps=cumulative_steps(
            # Initial: arrange 1 through 6 in a 2-by-3 matrix.
            'import numpy as np\nA = np.arange(1, 7).reshape(2, 3)\nR = A.copy()',
            # First click: transpose to 3-by-2; entries travel to their new cells.
            'R = A.T',
            # Second click: reverse the three rows; entry values stay unchanged.
            'R = R[::-1].copy()')),
    # FADE CODE: the flag controls whether the point and label are in the scene.
    'boilerplate-fade': dict(
        title='Fade in and out', builder=fading_objects,
        steps=cumulative_steps(
            # Initial: omit both objects, leaving just the scene title.
            'visible = False',
            # First click: include both objects so Vue fades them in.
            'visible = True',
            # Second click: omit them again so Vue fades them out.
            'visible = False')),
}


# CATALOG RUNNER: execute every example and validate its target snapshots.
def build_examples():
    """Execute the sample code and check the geometry the renderer receives."""
    output = {}
    for lesson_id, example in EXAMPLES.items():
        states = []
        # Track object type/point count across all snapshots in this lesson.
        identities = {}
        for k, source in enumerate(example['steps']):
            # Each cumulative code state runs with fresh variables; the builder
            # can only read values already computed in that displayed state.
            env = {}
            exec(compile(source, f'{lesson_id} step {k}', 'exec'), env)
            state = example['builder'](k, env)
            # IDs must be unique within a snapshot for Vue to match objects.
            ids = [node['id'] for node in state['nodes']]
            assert len(ids) == len(set(ids)), f'{lesson_id}: duplicate IDs'
            for node in state['nodes']:
                # Infinite/NaN coordinates cannot produce valid SVG geometry.
                assert np.isfinite(node['points']).all(), lesson_id
                # Smooth interpolation needs the same type and point count
                # whenever an existing ID appears again.
                identity = (node['kind'], len(node['points']))
                assert identities.setdefault(node['id'], identity) == identity, (
                    f'{lesson_id}: an object changed shape type or point count')
            states.append(state)
        # Match the JSON structure CodeVisual expects. slide=0 is a placeholder
        # because these catalog examples have not been placed in slides.md.
        output[lesson_id] = dict(title=example['title'], slide=0, states=states)
    return output


# COMMAND LINE: validate the catalog and optionally write inspectable JSON.
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional separate snapshot JSON file.')
    args = parser.parse_args()
    output = build_examples()
    count = sum(len(lesson['states']) for lesson in output.values())
    print(f'Validated {len(output)} examples with {count} code/visual states.')
    if args.output:
        # Only an explicit --output writes a file. allow_nan=False also rejects
        # non-finite exported values before producing the JSON document.
        args.output.write_text(json.dumps(output, indent=2, allow_nan=False) + '\n', encoding='utf-8')
        print(f'Wrote {args.output}')


if __name__ == '__main__':
    main()
