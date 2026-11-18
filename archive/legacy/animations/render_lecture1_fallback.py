"""Render the two Lecture 1 3D clips when Manim is unavailable.

The equations, column vectors, and solution are shared with the Manim scenes
in expanded_scenes.py. Requires Pillow, NumPy, and ffmpeg.
"""
from pathlib import Path
import math
import subprocess

import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / 'public' / 'animations'
W, H, FPS, SECONDS = 1280, 720, 24, 8
BG = (19, 34, 47)
INK = (234, 240, 243)
MUTED = (167, 187, 200)
BLUE = (104, 185, 236)
ORANGE = (255, 160, 120)
GREEN = (144, 214, 177)
FONT = '/usr/share/fonts/noto/NotoSans-Regular.ttf'
MONO = '/usr/share/fonts/TTF/DejaVuSansMono.ttf'
if not Path(MONO).exists():
    MONO = FONT


def font(size, mono=False):
    return ImageFont.truetype(MONO if mono else FONT, size)


def point(v):
    x, y, z = v
    return (round(340 + 84 * (.75*x - .65*y)),
            round(425 + 84 * (.30*x + .25*y - .85*z)))


def line(draw, a, b, color, width=2):
    draw.line([point(a), point(b)], fill=color, width=width)


def arrow(draw, v, color, width=9):
    a = np.array(point((0, 0, 0)), dtype=float)
    b = np.array(point(v), dtype=float)
    d = b - a
    length = np.linalg.norm(d)
    if length < 1:
        return
    unit = d / length
    side = np.array([-unit[1], unit[0]])
    shaft_end = b - 22 * unit
    draw.line([tuple(a), tuple(shaft_end)], fill=color, width=width)
    draw.polygon([tuple(b), tuple(b - 28*unit + 11*side),
                  tuple(b - 28*unit - 11*side)], fill=color)


def polygon(image, corners, color, alpha):
    layer = Image.new('RGBA', (W, H))
    d = ImageDraw.Draw(layer)
    d.polygon([point(p) for p in corners], fill=(*color, round(105*alpha)),
              outline=(*color, round(225*alpha)), width=3)
    image.alpha_composite(layer)


def frame_base(title, subtitle, grid3d=True):
    im = Image.new('RGBA', (W, H), (*BG, 255))
    d = ImageDraw.Draw(im)
    d.text((52, 31), title, font=font(40), fill=INK)
    d.text((54, 93), subtitle, font=font(22), fill=MUTED)
    d.line((658, 133, 658, 662), fill=(59, 83, 100), width=2)
    if grid3d:
        # The z=0 coordinate grid gives the 3D figures a stable reference.
        for q in range(-2, 3):
            line(d, (-2, q, 0), (2, q, 0), (59, 83, 100))
            line(d, (q, -2, 0), (q, 2, 0), (59, 83, 100))
        for v, name in [((2.3, 0, 0), 'x'), ((0, 2.3, 0), 'y'), ((0, 0, 3.2), 'z')]:
            line(d, (0, 0, 0), v, MUTED, 3)
            p = point(v)
            d.text((p[0]+5, p[1]-18), name, font=font(23), fill=MUTED)
    d.text((51, 673), 'LECTURE 1  /  GEOMETRY OF LINEAR EQUATIONS',
           font=font(17), fill=MUTED)
    return im


def appear(t, start):
    return max(0, min(1, (t-start)/.8))


def row_frame(t):
    im = frame_base('Three planes, one solution',
                    'Row picture: each equation is a plane')
    p1 = [(-.8, -1.6, -.4), (.8, 1.6, -.4),
          (.8, 1.6, 2.4), (-.8, -1.6, 2.4)]
    p2 = [(-.6, -.6, .4), (.6, -.6, -.8),
          (.6, .6, 1.6), (-.6, .6, 2.8)]
    p3 = [(-1.5, -1, .25), (1.5, -1, .25),
          (1.5, 1, 1.75), (-1.5, 1, 1.75)]
    for corners, color, start in [(p1, BLUE, 0), (p2, ORANGE, 1.8),
                                  (p3, GREEN, 3.6)]:
        a = appear(t, start)
        if a:
            polygon(im, corners, color, a)
    d = ImageDraw.Draw(im)
    equations = [('2x - y = 0', BLUE), ('-x + 2y - z = -1', ORANGE),
                 ('-3y + 4z = 4', GREEN)]
    for i, (text, color) in enumerate(equations):
        if t >= 1.8*i:
            d.text((710, 165 + 62*i), text, font=font(30, True), fill=color)
    d.text((710, 386), 'Matrix form', font=font(27), fill=INK)
    for i, text in enumerate(['[ 2  -1   0 ] [x]   [ 0]',
                              '[-1   2  -1 ] [y] = [-1]',
                              '[ 0  -3   4 ] [z]   [ 4]']):
        d.text((708, 432+44*i), text, font=font(23, True), fill=INK)
    if t >= 5.4:
        p = point((0, 0, 1))
        d.ellipse((p[0]-10, p[1]-10, p[0]+10, p[1]+10),
                  fill=INK, outline=GREEN, width=4)
        d.text((710, 588), 'Intersection: (0, 0, 1)',
               font=font(26), fill=GREEN)
    return im.convert('RGB')


def column_frame(t):
    im = frame_base('The columns reach b',
                    'Column picture: the unknowns are vector weights')
    d = ImageDraw.Draw(im)
    columns = [((2, -1, 0), BLUE, 'a1 = ( 2, -1,  0)'),
               ((-1, 2, -3), ORANGE, 'a2 = (-1,  2, -3)'),
               ((0, -1, 4), GREEN, 'a3 = ( 0, -1,  4)')]
    for i, (v, color, text) in enumerate(columns):
        if t >= 1.7*i:
            arrow(d, v, color)
            d.text((710, 177+61*i), text, font=font(25, True), fill=color)
    d.text((710, 386), 'Matrix form', font=font(27), fill=INK)
    for i, text in enumerate(['[ 2  -1   0 ] [x]   [ 0]',
                              '[-1   2  -1 ] [y] = [-1]',
                              '[ 0  -3   4 ] [z]   [ 4]']):
        d.text((708, 432+44*i), text, font=font(23, True), fill=INK)
    if t >= 5.3:
        p = point((0, -1, 4))
        d.ellipse((p[0]-11, p[1]-11, p[0]+11, p[1]+11),
                  fill=INK, outline=GREEN, width=4)
        d.text((710, 588), '0a1 + 0a2 + 1a3 = b',
               font=font(25, True), fill=GREEN)
    return im.convert('RGB')


def plane2d(draw, xbounds=(-1, 4), ybounds=(-1, 5)):
    x0, x1 = xbounds
    y0, y1 = ybounds
    left, top, right, bottom = 70, 160, 610, 626
    def p(x, y):
        return (round(left+(x-x0)/(x1-x0)*(right-left)),
                round(bottom-(y-y0)/(y1-y0)*(bottom-top)))
    for x in range(math.ceil(x0), math.floor(x1)+1):
        draw.line([p(x, y0), p(x, y1)], fill=(59, 83, 100), width=1)
    for y in range(math.ceil(y0), math.floor(y1)+1):
        draw.line([p(x0, y), p(x1, y)], fill=(59, 83, 100), width=1)
    draw.line([p(x0, 0), p(x1, 0)], fill=MUTED, width=3)
    draw.line([p(0, y0), p(0, y1)], fill=MUTED, width=3)
    draw.text((p(x1, 0)[0]+9, p(x1, 0)[1]-14), 'x', font=font(22), fill=MUTED)
    draw.text((p(0, y1)[0]-8, p(0, y1)[1]-31), 'y', font=font(22), fill=MUTED)
    return p


def matrix2d(draw, y=430):
    draw.text((710, y-46), 'Matrix form', font=font(27), fill=INK)
    draw.text((710, y),   '[ 2  -1 ] [x]   [0]', font=font(25, True), fill=INK)
    draw.text((710, y+45),'[-1   2 ] [y] = [3]', font=font(25, True), fill=INK)


def row2d_frame(t):
    im = frame_base('Two lines, one solution',
                    'Row picture: both equations must hold', False)
    d = ImageDraw.Draw(im)
    p = plane2d(d)
    if t >= 0:
        d.line([p(-.5, -1), p(2.5, 5)], fill=BLUE, width=6)
        d.text((710, 174), '2x - y = 0', font=font(31, True), fill=BLUE)
    if t >= 2:
        d.line([p(-1, 1), p(4, 3.5)], fill=ORANGE, width=6)
        d.text((710, 242), '-x + 2y = 3', font=font(31, True), fill=ORANGE)
    matrix2d(d)
    if t >= 4.4:
        q = p(1, 2)
        d.ellipse((q[0]-10, q[1]-10, q[0]+10, q[1]+10), fill=GREEN)
        d.text((q[0]+14, q[1]-36), '(1, 2)', font=font(24), fill=GREEN)
        d.text((710, 568), 'Both rows meet at (1, 2)',
               font=font(25), fill=GREEN)
    return im.convert('RGB')


def arrow2d(draw, a, b, p, color, width=8):
    start = np.array(p(*a), dtype=float)
    end = np.array(p(*b), dtype=float)
    direction = (end-start)/np.linalg.norm(end-start)
    side = np.array([-direction[1], direction[0]])
    draw.line([tuple(start), tuple(end-21*direction)], fill=color, width=width)
    draw.polygon([tuple(end), tuple(end-28*direction+10*side),
                  tuple(end-28*direction-10*side)], fill=color)


def column2d_frame(t):
    im = frame_base('Build b from the columns',
                    'Column picture: x and y are the vector weights', False)
    d = ImageDraw.Draw(im)
    p = plane2d(d, (-3, 3), (-2, 5))
    arrow2d(d, (0, 0), (2, -1), p, BLUE)
    d.text((710, 174), 'a1 = ( 2, -1)', font=font(28, True), fill=BLUE)
    if t >= 1.8:
        arrow2d(d, (0, 0), (-1, 2), p, ORANGE, 6)
        d.text((710, 236), 'a2 = (-1,  2)', font=font(28, True), fill=ORANGE)
    if t >= 3.5:
        arrow2d(d, (2, -1), (0, 3), p, ORANGE)
        d.text((710, 298), 'a1 + 2a2 = b', font=font(27, True), fill=INK)
    matrix2d(d)
    if t >= 5.3:
        arrow2d(d, (0, 0), (0, 3), p, GREEN, 6)
        d.text((710, 568), 'b = (0, 3), weights (1, 2)',
               font=font(25), fill=GREEN)
    return im.convert('RGB')


def render(name, frame_fn):
    OUT.mkdir(parents=True, exist_ok=True)
    video = OUT / f'{name}.mp4'
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo',
           '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-c:v', 'libx264', '-preset', 'fast', '-crf', '22',
           '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(video)]
    with subprocess.Popen(cmd, stdin=subprocess.PIPE) as proc:
        for k in range(FPS*SECONDS):
            im = frame_fn(k/FPS)
            proc.stdin.write(im.tobytes())
        proc.stdin.close()
        if proc.wait():
            raise RuntimeError(f'ffmpeg failed for {name}')
    frame_fn(SECONDS-.2).save(OUT/f'{name}.jpg', quality=93)
    print(video)


if __name__ == '__main__':
    render('RowIntersection', row2d_frame)
    render('ColumnCombination', column2d_frame)
    render('ThreePlaneIntersection', row_frame)
    render('ThreeColumnCombination', column_frame)
