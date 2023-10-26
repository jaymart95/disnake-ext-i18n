"""
Automatically publishing to pypi.
"""

import wexpect
import argparse

from os import getenv
from dotenv import load_dotenv


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=False)
    args = parser.parse_args()
    if args.type == "build":
        print(".. BUILDING")
        setupfile = "setup.py"
        child = wexpect.spawn("py", args=[setupfile, "sdist"])
        print(child.read())
    child = wexpect.spawn("twine", args=["upload", "dist/*", f"-u jaymart95", f"-p Jaxjase95."])
    print(child.read())


if __name__ == "__main__":
    main()
