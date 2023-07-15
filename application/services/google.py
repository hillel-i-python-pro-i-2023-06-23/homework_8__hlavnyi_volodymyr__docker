import pandas as pd

from application.services.special import FILES_OUTPUT_DIR


def get_google_sheets_pd_data(url):
    csv_file_path = FILES_OUTPUT_DIR.joinpath("gtable.csv")
    df = pd.io.parsers.read_csv(url)
    # write for testing purpose
    df.to_csv(csv_file_path)
    return df


def get_from_pd_height(df):
    height_mean = df[["Height(Inches)"]].mean()
    return height_mean.values[0]


def get_from_pd_weight(df):
    weight_mean = df[["Weight(Pounds)"]].mean()
    return weight_mean.values[0]


def convert_inches_in_cm(inches):
    return inches * 2.54


def convert_pounds_in_kg(pounds):
    return pounds * 0.453592


def print_info_from_google_sheets_height(df):
    print(f"Average height is {convert_inches_in_cm(get_from_pd_height(df))}")


def print_info_from_google_sheets_weight(df):
    print(f"Average weight is {convert_pounds_in_kg(get_from_pd_weight(df))}")


def get_string_info_from_google_sheets_height(df):
    return f"Average height is {convert_inches_in_cm(get_from_pd_height(df))}"


def get_string_info_from_google_sheets_weight(df):
    return f"Average weight is {convert_pounds_in_kg(get_from_pd_weight(df))}"
