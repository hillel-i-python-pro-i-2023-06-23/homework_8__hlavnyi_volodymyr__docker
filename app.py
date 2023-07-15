from flask import Flask

from application.services.api import (
    get_info_from_api,
    get_string_info_from_api_count_astro,
    get_string_list_austronauts,
)
from application.services.generate_users import generate_string_list_of_users, generate_list_of_users
from application.services.google import (
    get_google_sheets_pd_data,
    get_string_info_from_google_sheets_height,
    get_string_info_from_google_sheets_weight,
)
from application.services.io_file import get_file_to_string, get_path_if_file_exists
from application.services.special import get_string_homework

app = Flask(__name__)


# start/first route
@app.route("/")
@app.route("/start")
def start():
    return get_string_homework()


# Task 1
# Read file
@app.route("/get-content")
@app.route("/get-content/")
@app.route("/get-content/<namefile>")
def get_content(namefile: str = "sample3.txt"):
    link2file_output = get_path_if_file_exists(namefile)
    return get_file_to_string(link2file_output)


@app.route("/generate-users")
@app.route("/generate-users/")
@app.route("/generate-users/<int:amount_of_users>")
def generate_users(amount_of_users: int = 100):
    users = generate_list_of_users(amount=amount_of_users)
    return generate_string_list_of_users(users=users, type_of_list="ol")


@app.route("/space")
@app.route("/space/")
def space():
    url1 = "http://api.open-notify.org/astros.json"
    # [handle_logic]-[BEGIN]
    data = get_info_from_api(url1)
    # [handle_logic]-[END]
    string_for_return_head = f"{get_string_info_from_api_count_astro(data)}"
    string_for_return_astro_list = f"{get_string_list_austronauts(data)}"
    return f"{string_for_return_head}\n\n{string_for_return_astro_list}"


@app.route("/mean")
@app.route("/mean/")
def mean():
    url2 = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    # get data
    df = get_google_sheets_pd_data(url2)
    str_for_return_head = f'Get info from this <a href="{url2}">link</a>'
    str_for_return_height = f"{get_string_info_from_google_sheets_height(df)}"
    str_for_return_weight = f"{get_string_info_from_google_sheets_weight(df)}"
    return f"{str_for_return_head}<br>{str_for_return_height}<br>{str_for_return_weight}"


if __name__ == "__main__":
    app.run()
