import logging
import sys
from datetime import datetime

from util.ConfigLoader import load_app_config
from model.processor import MainProcessor

if __name__ == "__main__":
    print("File converter App")

logger = logging.getLogger("Excel to CSV converter App")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File converter App - Started @: ' + current_timestamp)
print('File converter App - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1])
    if config.conversion == "EXCEL-CSV":
        MainProcessor.excel_to_csv_processor(config.input_conf, config.output_conf)
    elif config.conversion == "EXCEL-TEXT":
        MainProcessor.excel_to_text_processor(config.input_conf, config.output_conf)

except Exception as e:
    logger.error("File converter Application Failed with Error:" + str(e))
    print("File converter Application Failed with Error: {0}".format(str(e)))
    raise e
