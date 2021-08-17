from model.read.Reader import down_file_from_share_point
from model.read.Reader import csv_reader
from model.read.Reader import excel_reader
from model.read.Reader import text_reader
from pathlib import Path
from model.write.writer import csv_writer
from model.write.writer import text_writer


def main_processor(app_conf):
    data = None
    if app_conf.input_conf.source == "SHAREPOINT":
        response = down_file_from_share_point(app_conf.input_conf.sharepoint_conf.url,
                                              app_conf.input_conf.sharepoint_conf.file,
                                              app_conf.input_conf.input_temp_path,
                                              app_conf.input_conf.sharepoint_conf.user_name,
                                              app_conf.input_conf.sharepoint_conf.password)

        if response.ok:
            if app_conf.conversion is None:
                if app_conf.app_conf.input_conf.sharepoint_conf.file_format == "CSV":
                    data = csv_processor(app_conf.input_conf.input_temp_path,
                                         app_conf.input_conf.sharepoint_conf.fields,
                                         app_conf.input_conf.sharepoint_conf.delimiter,
                                         app_conf.input_conf.sharepoint_conf.header)

                elif app_conf.input_conf.sharepoint_conf.file_format == "EXCEL":
                    data = excel_processor(app_conf.input_conf.input_temp_path,
                                           app_conf.input_conf.sharepoint_conf.all_sheets_required,
                                           app_conf.input_conf.sharepoint_conf.required_sheets,
                                           app_conf.input_conf.sharepoint_conf.header)

                elif app_conf.input_conf.sharepoint_conf.file_format == "TEXT":
                    data = text_processor(app_conf.input_conf.input_temp_path,
                                          app_conf.input_conf.sharepoint_conf.delimiter)

                return data
            else:
                raise Exception("Invalid File Format in Sharepoint configuration")

        else:
            raise Exception("Sharepoint download failed: " + str(response))
    elif app_conf.input_conf.source == "CSV":
        data = csv_processor(app_conf.input_conf.input_temp_path,
                             app_conf.input_conf.sharepoint_conf.fields,
                             app_conf.input_conf.sharepoint_conf.delimiter,
                             app_conf.input_conf.sharepoint_conf.header)
        return data

    elif app_conf.input_conf.source == "EXCEL":
        data = excel_processor(app_conf.input_conf.input_temp_path,
                               app_conf.input_conf.sharepoint_conf.all_sheets_required,
                               app_conf.input_conf.sharepoint_conf.required_sheets,
                               app_conf.input_conf.sharepoint_conf.header)
        return data

    elif app_conf.input_conf.source == "TEXT":
        data = text_processor(app_conf.input_conf.input_temp_path,
                              app_conf.input_conf.sharepoint_conf.delimiter)
        return data

    else:
        raise Exception("Invalid Input Source Type")


def csv_processor(path, required_fields, delimiter, header):
    return csv_reader(path, required_fields, delimiter, header)


def excel_processor(path, all_sheets_required, required_sheets, header):
    if all_sheets_required:
        return excel_reader(path, None, header, None)
    else:
        return excel_reader(path, required_sheets, header, required_sheets)


def text_processor(path, delimiter):
    return text_reader(path, delimiter)


def excel_to_csv_processor(input_conf, output_file_conf):
    file_name = str(Path(input_conf.source_folder).name).split("\\.")[0]
    df = excel_processor(input_conf.source_folder,
                         input_conf.all_sheets_required,
                         input_conf.required_sheets,
                         input_conf.header)
    csv_writer(df, file_name, output_file_conf)


def excel_to_text_processor(input_conf, output_file_conf):
    file_name = str(Path(input_conf.source_folder).name).split("\\.")[0]
    df = excel_processor(input_conf.source_folder,
                         input_conf.all_sheets_required,
                         input_conf.required_sheets,
                         input_conf.header)
    text_writer(df, file_name, output_file_conf)
