"""Align native PowerPoint layer exports and assign every object an entrance.

This measures raster padding only; the original artwork is not edited.
Run after scripts/export-objectives.ps1 when re-exporting this source slide.
"""
from pathlib import Path
import json

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MOTION = {
    1486: ('top', 0.0, .65),
    1500: ('grow-y', .18, .8),
    1478: ('left', .32, .65), 1476: ('right', .44, .75),
    1481: ('left', .62, .65), 6: ('right', .74, .75),
    1484: ('left', .92, .65), 2: ('right', 1.04, .75),
    4: ('left', 1.22, .65), 5: ('right', 1.34, .75),
    1499: ('top', .14, .7), 1501: ('bottom', 1.42, .7),
    1519: ('grow-x', 1.5, .7), 3: ('fade', 1.55, .6),
}


def main():
    path = ROOT / 'sources/learning-objectives.json'
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    reference = np.asarray(Image.open(ROOT / ('public' + data['image'])).convert('RGB')).astype(np.int16)
    for layer in data['layers']:
        image = Image.open(ROOT / ('public' + layer['src'])).convert('RGBA')
        pixels = np.asarray(image)
        y, x = np.where(pixels[:, :, 3] > 248)
        if len(x) > 3000:
            sample = np.linspace(0, len(x)-1, 3000).astype(int)
            x, y = x[sample], y[sample]
        color = pixels[y, x, :3].astype(np.int16)
        best = (float('inf'), 0, 0)
        if len(x):
            for dy in range(-18, 19):
                for dx in range(-18, 19):
                    xx, yy = x + dx, y + dy
                    valid = (xx >= 0) & (xx < 1920) & (yy >= 0) & (yy < 1080)
                    if valid.mean() < .8:
                        continue
                    error = np.abs(reference[yy[valid], xx[valid]] - color[valid]).mean()
                    candidate = (float(error), dx, dy)
                    if candidate < best:
                        best = candidate
        layer['box'] = [best[1] / 1920 * 100, best[2] / 1080 * 100,
                        image.width / 1920 * 100, image.height / 1080 * 100]
        motion, delay, duration = MOTION[layer['shape']]
        layer.update(motion=motion, delay=delay, duration=duration)
    assert len(data['layers']) == len(MOTION) == 14
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('All 14 original elements aligned and given timed entrances.')


if __name__ == '__main__':
    main()
