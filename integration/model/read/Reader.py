import pandas as pd
import sharepy
import pandas as pd
import cx_Oracle


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


def xml_reader(path, xpath="./*"):
    return pd.read_xml(path, xpath=xpath)


def json_reader(path):
    return pd.read_json(path)


def read_from_oracle_query(oracle_conf, sql=None):
    if sql is None and oracle_conf.table_name is not None:
        sql = "SELECT * FROM " + oracle_conf.table_name
    try:
        with cx_Oracle.connect(oracle_conf.user_name, oracle_conf.password,
                               oracle_conf.host + ":" + oracle_conf.port + "/" + oracle_conf.service_name, encoding="UTF-8") as connection:
            dataframe = pd.read_sql(sql, con=connection)
        return dataframe
    except cx_Oracle.Error as error:
        print(error)
        raise error
