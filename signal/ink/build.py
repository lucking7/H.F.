"""Run the ink builder from its original command path."""
from pathlib import Path
from runpy import run_path

if __name__ == '__main__':
    script = Path(__file__).resolve().parent / 'scripts' / 'build.py'
    run_path(str(script), run_name='__main__')
