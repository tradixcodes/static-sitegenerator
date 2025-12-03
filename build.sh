#!/bin/bash
# Simple production build script for static site generator

# Path to your repo root (local)
BASEPATH="/static-sitegenerator/"

# Run the Python build
python3 src/main.py "$BASEPATH"

echo "✅ Production build complete! Site generated under $BASEPATH"
