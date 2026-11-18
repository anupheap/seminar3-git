"""Compatibility entry point for the source-faithful native deck builder."""
from pathlib import Path
import runpy
if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).with_name('build-source-deck.py')), run_name='__main__')
