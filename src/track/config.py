"""Project paths for the TRACK pipeline.

The notebooks read a large data tree that is not distributed with the code:
the ACGym release is roughly 114 GB and is downloaded separately. The data
root is therefore resolved at run time rather than written into the notebooks.

Resolution order:

1. The TRACK_ROOT environment variable, if set.
2. A track_root.txt file found by walking up from the working directory,
   holding a single line with the path. That file is not tracked by git.
3. The first parent directory that contains data/features.

Set the environment variable, or drop a track_root.txt next to the notebooks,
and nothing else needs to change.
"""

import os
from pathlib import Path

_MARKER = Path("data") / "features"


def _candidates():
    here = Path.cwd().resolve()
    return [here] + list(here.parents)


def resolve_root():
    env = os.environ.get("TRACK_ROOT")
    if env:
        p = Path(env).expanduser().resolve()
        if not p.is_dir():
            raise RuntimeError("TRACK_ROOT is set to %s but that is not a directory" % p)
        return p

    for parent in _candidates():
        cfg = parent / "track_root.txt"
        if cfg.is_file():
            p = Path(cfg.read_text(encoding="utf-8").strip()).expanduser().resolve()
            if not p.is_dir():
                raise RuntimeError("%s points at %s, which is not a directory" % (cfg, p))
            return p

    for parent in _candidates():
        if (parent / _MARKER).is_dir():
            return parent

    raise RuntimeError(
        "Could not locate the data root. Set the TRACK_ROOT environment variable, "
        "or place a track_root.txt file holding the path next to the notebooks. "
        "The root is the directory that contains data/features."
    )


PROJECT_ROOT = resolve_root()

DATA = PROJECT_ROOT / "data"
RAW = DATA / "raw"
PROCESSED = DATA / "processed"
FEATURES = DATA / "features"
FINGERPRINTS = DATA / "fingerprints"
REFERENCE_SAC = DATA / "reference_sac"

RESULTS = PROJECT_ROOT / "results"
FIGURES = RESULTS / "figures"

__all__ = [
    "PROJECT_ROOT", "DATA", "RAW", "PROCESSED", "FEATURES",
    "FINGERPRINTS", "REFERENCE_SAC", "RESULTS", "FIGURES", "resolve_root",
]
