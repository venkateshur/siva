import pandas as pd
import sharepy


def down_file_from_share_point(url, file, temp_file_path, user_name, password):
    sharepoint_connect = sharepy.connect(url, username=user_name, password=password)
    return sharepoint_connect.getfile(file, filename=temp_file_path)


def csv_reader(path, fields, delimiter, header):
    if fields is None:
        csv_input = pd.read_csv(path, delimiter, header=header)
    else:
        csv_input = pd.read_csv(path, delimiter, header=header, usecols=fields)

    return csv_input


def excel_reader(path, all_sheets, header, specific_sheet):
    if all_sheets:
        excel_input = pd.read_excel(path, sheet_name=all_sheets, header=header)
    else:
        excel_input = pd.read_excel(path, sheet_name=specific_sheet, header=header)

    return excel_input


def text_reader(path, delimiter):
    return pd.read_csv(path, header=None, delimiter=delimiter)
