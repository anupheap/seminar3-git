"""Render only the new source-based scenes, then publish videos and posters."""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'python_examples'))
from source_math import LESSONS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scenes', nargs='*')
    args = parser.parse_args()
    names = args.scenes or [item['scene'] for item in LESSONS if item['scene']]
    media = ROOT / '.cache/manim'
    output = ROOT / 'public/animations/source'
    output.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, '-m', 'manim', '-qm', '--fps', '24',
                    '--disable_caching', '--media_dir', str(media),
                    str(ROOT / 'animations/source_scenes.py'), *names], check=True, cwd=ROOT)
    for name in names:
        candidates = list((media / 'videos/source_scenes').glob(f'*/{name}.mp4'))
        if len(candidates) != 1:
            raise RuntimeError(f'Expected one completed render for {name}: {candidates}')
        target = output / f'{name}.mp4'
        shutil.copy2(candidates[0], target)
        subprocess.run(['ffmpeg', '-y', '-sseof', '-0.3', '-i', str(target),
                        '-frames:v', '1', '-update', '1', str(output / f'{name}.jpg')],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print('Published', name)


if __name__ == '__main__':
    main()
