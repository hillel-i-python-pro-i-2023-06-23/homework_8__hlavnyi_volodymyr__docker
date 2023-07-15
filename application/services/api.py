import requests


def get_info_from_api(url):
    return requests.get(url).json()


def get_count_austronauts(data):
    return data["number"]


def get_list_austronauts(data):
    list_astro = []
    for a in data["people"]:
        craft = a["craft"]
        name_astro = a["name"]
        list_astro.append(f"{craft} - {name_astro}")
    return list_astro


def print_info_from_api(data):
    print_info_from_api_count_astro(data)
    print_list_austronauts(data)


def print_info_from_api_count_astro(data):
    print(f"Now we have {get_count_austronauts(data)} austronauts in space")


def print_list_austronauts(data):
    for count, astro in enumerate(get_list_austronauts(data)):
        print(count + 1, astro)


def get_string_info_from_api(data):
    return f"{get_string_info_from_api(data)} \n {get_string_list_austronauts(data)}"


def get_string_info_from_api_count_astro(data):
    return f"Now we have {get_count_austronauts(data)} austronauts in space"


def get_string_list_austronauts(data):
    list_astro: list[str] = []
    for astro in get_list_austronauts(data):
        list_astro.extend(("<li>", astro, "</li>"))
    _temp = "\n".join(list_astro)

    return f"<ol>{_temp}</ol>"
