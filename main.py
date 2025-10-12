#!/usr/bin/env python3
import tempfile
import subprocess
import os
import shutil

script_dir = os.path.dirname(os.path.realpath(__file__))
tutorial_path = os.path.join(script_dir, "tutorial.hla")

if not os.path.exists(tutorial_path):
    print(
        f"No tutorial.hla in {script_dir}? What kind of half-assed clusterfuck setup is this? Clone the damn repo properly or GTFO."
    )
    exit(1)

with open(tutorial_path, "r", encoding="utf-8") as f:
    original_content = f.read()


def main():
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".c", encoding="utf-8", delete=False
    ) as tmp:
        tmp.write(original_content)
        temp_file = tmp.name

    editor = ["vi", temp_file]
    try:
        subprocess.call(editor)
    except FileNotFoundError:
        print(
            "Vim missing? Install it: sudo apt install vim. This ain't for finger-painting in GUIs."
        )
        os.unlink(temp_file)
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
