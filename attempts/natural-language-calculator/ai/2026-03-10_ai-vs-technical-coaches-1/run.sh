#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/src"
uv run python natural_language_calculator.py sample_expressions.txt
