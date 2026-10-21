#!/usr/bin/env python3
"""Run the SciFi plumbing tests (stdlib unittest). Exit 0 when all pass, 1 otherwise.

Usage:
    python3 scripts/tests/run_tests.py [-v]
"""
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(HERE))
    sys.path.insert(0, str(HERE.parent))
    verbosity = 2 if "-v" in sys.argv[1:] else 1
    suite = unittest.defaultTestLoader.discover(str(HERE), pattern="test_*.py", top_level_dir=str(HERE))
    result = unittest.TextTestRunner(verbosity=verbosity).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
