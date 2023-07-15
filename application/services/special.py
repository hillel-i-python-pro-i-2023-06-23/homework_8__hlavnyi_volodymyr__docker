import os
import pathlib
from typing import Final

ROOT_DIR: Final[pathlib.Path] = pathlib.Path(__file__).parents[2]
FILES_INPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("files_input")
FILES_OUTPUT_DIR: Final[pathlib.Path] = ROOT_DIR.joinpath("files_output")


def get_string_homework():
    text_its_docker = ""
    if os.environ.get("AM_I_IN_A_DOCKER_CONTAINER", False):
        text_its_docker = "We are running in Docker container!"
    return f"<h3> Homework #8 (Volodymyr Hlavnyi) </h2>" f"<br> <h4>{text_its_docker}</h4>"
