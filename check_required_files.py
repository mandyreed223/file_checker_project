#!/usr/bin/env python3
import os
import sys

REQUIRED_FILES = ["README.md", ".gitignore"]

def main():
    missing = [f for f in REQUIRED_FILES if not os.path.exists(f)]

    if missing:
        print("❌ Required files are missing:")
        for f in missing:
            print(f" - {f}")
        # Exit with non-zero code so CI fails
        sys.exit(1)
    else:
        # Pass silently
        sys.exit(0)

if __name__ == "__main__":
    main()
