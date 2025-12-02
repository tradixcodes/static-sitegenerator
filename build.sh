#!/bin/bash
# Simple production build script for static site generator

# Replace REPO_NAME with your actual GitHub repo name
REPO_NAME="https://github.com/tradixcodes/static-sitegenerator"  # <-- change this to your repo name

# Run the Python build with the repo subpath
python3 src/main.py "/${REPO_NAME}/"

echo "✅ Production build complete! Site generated under /${REPO_NAME}/"

