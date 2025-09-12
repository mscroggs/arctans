"""Run the demos."""

import os
import pytest


def join(*dirs) -> str:
    if len(dirs) == 1:
        return dirs[0]
    return os.path.join(join(*dirs[:-1]), dirs[-1])


demo_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(demo_dir)

demo_files = [
    file
    for file in os.listdir(demo_dir)
    if file.endswith(".py") and not file.startswith(".") and not file.startswith("test_")
]


@pytest.mark.parametrize("file", demo_files)
def test_demo(file):
    file_path = join(demo_dir, file)
    assert os.system(f"python3 {file_path}") == 0


@pytest.mark.parametrize("file", demo_files)
def test_in_docs(file):
    if not os.path.isdir(join(root_dir, "docs", "demos")):
        pytest.skip()
    assert os.path.isfile(join(root_dir, "docs", "demos", file[:-3] + ".rst"))
