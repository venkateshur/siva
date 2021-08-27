import logging
import sys
from datetime import datetime

from model.processor.MainProcessor import csv_processor, excel_processor, text_processor
from model.read import Reader
from model.write import writer
from model.write.writer import load_into_oracle
from util.ConfigLoader import load_app_config

if __name__ == "__main__":
    print("Data integrator - Loading Of Oracle")

logger = logging.getLogger("Data integrator - Loading Of Oracle")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('Loading file to oracle - Started @: ' + current_timestamp)
print('Loading file to oracle - Started @: ' + current_timestamp)

try:
    load_type = sys.argv[1]
    input_file_path = sys.argv[2]
    table_name = sys.argv[3]
    config_path = sys.argv[4]

    config = load_app_config(config_path, "oracle-file")
    if load_type == "FILE-ORACLE":
        if config.file_conf.file_format == "CSV":
            data = csv_processor(config.file_conf.path,
                                 config.file_conf.fields,
                                 config.file_conf.delimiter,
                                 config.file_conf.header)
        elif config.file_conf.file_format == "EXCEL":
            data = excel_processor(config.file_conf.path,
                                   config.file_conf.all_sheets_required,
                                   config.file_conf.required_sheets,
                                   config.file_conf.header)

        elif config.file_conf.file_format == "TEXT":
            data = text_processor(config.file_conf.path,
                                  config.file_conf.delimiter)
        else:
            raise Exception("Invalid file format, supported file formats are CSV, EXCEL and TEXT")

        if isinstance(data, dict):
            for df in data:
                load_into_oracle(df, config.output_conf.oracle_conf)
        else:
            load_into_oracle(data, config.output_conf.oracle_conf)

    if config.source == "ORACLE-FILE":
        data = Reader.read_from_oracle_query(config.oracle_conf)
        if config.file_conf.file_format == "CSV":
            writer.csv_writer(data, config.oracle_conf.table_name.replace(".", "_"),
                              config.output_conf.file_conf)
        elif config.file_conf.file_format == "TEXT":
            writer.text_writer(data, config.oracle_conf.table_name.replace(".", "_"),
                               config.output_conf.file_conf)
        elif config.file_conf.file_format == "EXCEL":
            writer.excel_writer(data, config.oracle_conf.table_name.replace(".", "_"), config.file_conf)
        else:
            raise Exception("Invalid File Format, Supported File formats are CSV, Text and Excel")

except Exception as e:
    logger.error("Loading file to oracle Failed with Error:" + str(e))
    print("Loading file to oracle Failed with Error: {0}".format(str(e)))
    raise e
