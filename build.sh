#!/bin/bash
# Simple production build script for static site generator

# Path to your repo root (local)
REPO_PATH=$(pwd)   # current directory
OUTPUT_DIR="$REPO_PATH/docs"  # output directory for generated site

# Run the Python build
python3 src/main.py "$OUTPUT_DIR"

echo "✅ Production build complete! Site generated under $OUTPUT_DIR"
