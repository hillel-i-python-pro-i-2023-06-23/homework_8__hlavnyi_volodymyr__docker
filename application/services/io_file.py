from application.services.special import FILES_INPUT_DIR


def check_file_exists():
    gitkeep_file_path = FILES_INPUT_DIR.joinpath(".gitkeep")
    return gitkeep_file_path.exists()


def get_path_if_file_exists(name_of_file: str):
    check_txt_file = FILES_INPUT_DIR.joinpath(name_of_file)
    if check_file_exists():
        return check_txt_file
    else:
        raise FileNotFoundError(f"File not found: {check_txt_file.as_uri()}")


def get_file_to_string(link_2_file):
    string_for_return: list[str] = []
    lines_from_file = open(link_2_file).readlines()
    for one_line in lines_from_file:
        string_for_return.extend((one_line, "<br>"))

    return "".join(string_for_return)
