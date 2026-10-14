#!/usr/bin/env bash
# Build Oink (github.com/trolando/oink) at a pinned commit into tools/oink.
# Idempotent: exits early if tools/oink/build/oink already exists at the pinned commit.
# OINK_BUILD_TOOLS is off: it builds test_solvers, which needs boost/process/v1.hpp (Boost >= 1.86); Ubuntu 24.04 ships 1.83.
set -euo pipefail
OINK_COMMIT="${OINK_COMMIT:-8fbf0a7}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/tools/oink"
if [ -x "$DIR/build/oink" ] && [ "$(git -C "$DIR/src" rev-parse --short=7 HEAD 2>/dev/null)" = "$OINK_COMMIT" ]; then
  echo "oink already built at $OINK_COMMIT"; exit 0
fi
if ! [ -d /usr/include/boost/random ]; then
  (apt-get install -y -q libboost-filesystem-dev libboost-iostreams-dev libboost-regex-dev libboost-random-dev \
    || (apt-get update -q && apt-get install -y -q libboost-filesystem-dev libboost-iostreams-dev libboost-regex-dev libboost-random-dev)) >/dev/null
fi
mkdir -p "$DIR"
[ -d "$DIR/src/.git" ] || git clone -q https://github.com/trolando/oink "$DIR/src"
git -C "$DIR/src" fetch -q origin && git -C "$DIR/src" checkout -q "$OINK_COMMIT"
cmake -S "$DIR/src" -B "$DIR/build" -DCMAKE_BUILD_TYPE=Release -DOINK_BUILD_NATIVE=OFF \
  -DOINK_BUILD_EXTRA_TOOLS=ON -DOINK_BUILD_TOOLS=OFF -DOINK_BUILD_TESTS=OFF >/dev/null
cmake --build "$DIR/build" -j"$(nproc)" >/dev/null
echo "oink built at $OINK_COMMIT: $(ls "$DIR/build" | tr '\n' ' ')"
