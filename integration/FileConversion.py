import logging
import sys
from datetime import datetime

from util.ConfigLoader import load_app_config
from model.processor import MainProcessor

if __name__ == "__main__":
    print("File conversion App")

logger = logging.getLogger("File conversion App")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File conversion App - Started @: ' + current_timestamp)
print('File conversion App - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1], "file-conversion")
    if config.source_format == "EXCEL" and config.target_format == "CSV":
        MainProcessor.excel_to_csv_processor(config.input_conf, config.output_conf)

    elif config.source_format == "EXCEL" and config.target_format == "TEXT":
        MainProcessor.excel_to_text_processor(config.input_conf, config.output_conf)
    else:
        raise Exception("Invalid source and file formats")

except Exception as e:
    logger.error("File conversion Application Failed with Error:" + str(e))
    print("File converter Application Failed with Error: {0}".format(str(e)))
    raise e
