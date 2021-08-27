import logging
import sys
from datetime import datetime

from model.processor import FileTransferProcessor
from util.ConfigLoader import load_app_config

if __name__ == "__main__":
    print("File Transfer App")

logger = logging.getLogger("File Transfer")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File Transfer - Started @: ' + current_timestamp)
print('File Transfer - Started @: ' + current_timestamp)

try:
    file_transfer_config = load_app_config(sys.argv[1], "file-transfer")
    if file_transfer_config.source_system == "UNIX" and file_transfer_config.target_system == "WINDOWS":
        FileTransferProcessor.unix_transfer(file_transfer_config.unix_conf.file_path,
                                            file_transfer_config.unix_conf.cert_directory,
                                            file_transfer_config.unix_conf.cert_name,
                                            file_transfer_config.unix_conf.cert_password,
                                            file_transfer_config.windows_conf.direcotry)

    elif file_transfer_config.source_system == "WINDOWS" and file_transfer_config.target_system == "UNIX":
        FileTransferProcessor.windows_transfer(file_transfer_config.unix_conf.file_path,
                                               file_transfer_config.unix_conf.cert_directory,
                                               file_transfer_config.unix_conf.cert_name,
                                               file_transfer_config.unix_conf.cert_password,
                                               file_transfer_config.windows_conf.direcotry)
    else:
        raise Exception("Invalid Target System, Supported System are UNIX and WINDOWS")

except Exception as e:
    logger.error("File Transfer Failed with Error:" + str(e))
    print("File Transfer Failed with Error: {0}".format(str(e)))
    raise e
