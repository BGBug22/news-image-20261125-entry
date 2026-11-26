"""THE WORLD TODAY - 25 November 2026 front page.

Copies the pre-rendered front page (entry.png, drawn at build time from
verified news of Wednesday 25 November 2026) to the output directory.
Standard library only; deterministic - the same bytes every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly instead of silently shipping a truncated copy.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copied entry.png size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
