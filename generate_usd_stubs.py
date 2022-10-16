import sys, os
import shutil
import subprocess
from pathlib import Path

import pxr


def main() -> int:
  is_conda = os.path.exists(os.path.join(sys.prefix, 'conda-meta', 'history'))
  assert is_conda, "You are not running this script inside a conda virtual environment"

  # Install mypy for stubgen
  if subprocess.check_call(
      [sys.executable, "-m", "pip", "install", "-q", "mypy"]) != 0:
    print("Failed installing mypy")
    return 1

  # Generate stubs for package 'pxr' (from usd-core)
  if subprocess.check_call(["stubgen", "-q", "-p", "pxr", "-o", "out"]) != 0:
    print(
        "Failed generating stubs for package 'pxr'. Make sure that you have 'usd-core' installed"
    )
    return 1

  # Rename every file that was generated
  # We only care about the files starting with ONE _ (underscore)
  output_path = Path("./out/pxr")
  pyis = list(output_path.rglob("**/*.pyi"))
  filtered = [
      i for i in pyis if i.stem.startswith("_") and i.stem != "__init__"
  ]
  for p in pyis:
    if p in filtered:
      continue
    p.unlink()
  for f in filtered:
    f.rename(f.parent / "__init__.pyi")

  # Copy generated stubs to where we have the package installed
  pxr_package_dir = Path(pxr.__file__).parent
  shutil.copytree(output_path, pxr_package_dir, dirs_exist_ok=True)
  shutil.rmtree(output_path.parent)

  print(f"Done! Copied stubs to '{pxr_package_dir}'")

  return 0


if __name__ == "__main__":
  sys.exit(main())
