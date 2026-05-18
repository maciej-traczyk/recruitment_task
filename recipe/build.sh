#!/usr/bin/env bash
set -euo pipefail
 
cd "$SRC_DIR"
 
"${PYTHON}" -m pip install . \
    --no-deps \
    --no-build-isolation \
    -vv