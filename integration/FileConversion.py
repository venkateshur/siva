import logging
import sys
from datetime import datetime

from conf.FileConf import FileConf
from model.processor import MainProcessor

if __name__ == "__main__":
    print("File conversion App")

logger = logging.getLogger("File conversion App")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File conversion App - Started @: ' + current_timestamp)
print('File conversion App - Started @: ' + current_timestamp)

try:
    source_file_conf = FileConf(sys.argv[1],
                                bool(sys.argv[2]),
                                sys.argv[3].split(";"),
                                sys.argv[4].split(";"),
                                bool(sys.argv[5]))

    target_file_conf = FileConf(sys.argv[1],
                                bool(sys.argv[2]),
                                sys.argv[3].split(";"),
                                sys.argv[4].split(";"),
                                bool(sys.argv[5]))
    
    if source_file_conf.file_format == "EXCEL" and target_file_conf.file_format == "CSV":
        MainProcessor.excel_to_csv_processor(source_file_conf, target_file_conf)

    elif source_file_conf.file_format == "EXCEL" and target_file_conf.file_format == "TEXT":
        MainProcessor.excel_to_text_processor(source_file_conf, target_file_conf)
    else:
        raise Exception("Invalid source and file formats")

except Exception as e:
    logger.error("File conversion Application Failed with Error:" + str(e))
    print("File converter Application Failed with Error: {0}".format(str(e)))
    raise e
