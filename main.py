#!/usr/bin/env python3
"""Second roast for make.fun: deep research, deeper voice."""

# Bowo's pick: the research is shallow, the voice is deep.

import os

ROAST = "My agent's idea of deep research is Googling the question and reading me the first result in a deeper voice."


def serve_roast() -> None:
    """Write Bowo's deep-research roast to /output/entry.txt, nothing else."""
    if len(ROAST) > 200 or not ROAST.strip():
        raise ValueError("roast must be a non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":  # run it
    serve_roast()
