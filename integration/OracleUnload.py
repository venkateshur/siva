import logging
import sys
from datetime import datetime
from model.read import Reader
from model.write import writer
from util.ConfigLoader import load_app_config


if __name__ == "__main__":
    print("Oracle unload App")

logger = logging.getLogger("Data integrator")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('Oracle unload - Started @: ' + current_timestamp)
print('Oracle unload - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1])
    data = Reader.read_from_oracle_query(config.output_conf.oracle_conf)
    if config.output_conf.file_conf.file_format == "CSV":
        writer.csv_writer(data, config.output_conf.oracle_conf.table_name.replace(".", "_"), config.output_conf.file_conf)
    elif config.output_conf.file_conf.file_format == "Text":
        writer.text_writer(data, config.output_conf.oracle_conf.table_name.replace(".", "_"), config.output_conf.file_conf)
    elif config.output_conf.file_conf.file_format == "Excel":
        writer.excel_writer(data, config.output_conf.oracle_conf.table_name.replace(".", "_"), config.output_conf.file_conf)
    else:
        raise Exception("Invalid File Format, Supported File formats are CSV, Text and Excel")

except Exception as e:
    logger.error("Loading file to oracle Failed with Error:" + str(e))
    print("Loading file to oracle Failed with Error: {0}".format(str(e)))
    raise e
