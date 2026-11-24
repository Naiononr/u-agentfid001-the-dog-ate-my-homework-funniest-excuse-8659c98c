#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — one-line entry.

Writes a single funny line, the excuse a dog gives after being caught
eating the homework, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import tempfile

LINE = "You said 'do your homework', so I did — every page, one sitting, no pencil, no fuss, and now there's nothing left to mark."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(LINE.encode("utf-8"))
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
