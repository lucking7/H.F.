#!/usr/bin/env python3
"""Export the default macOS 26 flag artwork and Finder icons with Xcode."""

import argparse
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parent


def export(project, ictool):
    with TemporaryDirectory(dir=ROOT) as temp:
        stage = Path(temp)
        iconset = stage / "Flag.iconset"
        iconset.mkdir()
        for size in (16, 32, 64, 128, 144, 256, 512, 1024):
            subprocess.run([
                ictool, project, "--export-image", "--output-file", stage / f"{size}.png",
                "--platform", "macOS", "--rendition", "Default", "--width", str(size),
                "--height", str(size), "--scale", "1", "--design-generation", "26",
            ], check=True, stdout=subprocess.DEVNULL)

        for points in (16, 32, 128, 256, 512):
            for scale in (1, 2):
                suffix = "@2x" if scale == 2 else ""
                slot = iconset / f"icon_{points}x{points}{suffix}.png"
                shutil.copyfile(stage / f"{points * scale}.png", slot)
        subprocess.run(["iconutil", "-c", "icns", iconset, "-o", stage / "flag.icns"], check=True)

        for filename, directory in (("1024.png", "png"), ("144.png", "144px"), ("flag.icns", "icns")):
            target = ROOT / directory
            target.mkdir(exist_ok=True)
            (stage / filename).replace(target / (project.stem + Path(filename).suffix))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("codes", nargs="*", help="Flag codes to export (default: all projects)")
    args = parser.parse_args()
    projects = {path.stem: path for path in sorted((ROOT / "source").glob("*.icon"))}
    missing = sorted(set(args.codes) - projects.keys())
    if missing:
        parser.error("Unknown flag codes: " + ", ".join(missing))
    developer = Path(subprocess.check_output(["xcode-select", "-p"], text=True).strip())
    ictool = developer.parent / "Applications/Icon Composer.app/Contents/Executables/ictool"
    if not ictool.is_file():
        parser.error(f"Icon Composer's export tool was not found at {ictool}")
    for code in args.codes or projects:
        export(projects[code], ictool)
        print(code, flush=True)


if __name__ == "__main__":
    main()
