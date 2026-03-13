"""Run DemirBaş as a module.

Example:
    python -m demirbas --download-models "Merhaba"
"""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
