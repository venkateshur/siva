import logging
import sys
from datetime import datetime

from util.ConfigLoader import load_app_config
from model.processor import FileTransferProcessor

if __name__ == "__main__":
    print("File Transfer App")

logger = logging.getLogger("File Transfer")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File Transfer - Started @: ' + current_timestamp)
print('File Transfer - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1])

    if config.output_conf.file_share_conf.system == "UNIX":
        FileTransferProcessor.unix_transfer(config.output_conf.file_share_conf.host.source_folder,
                                            config.output_conf.file_share_conf.host,
                                            config.output_conf.file_share_conf.port,
                                            config.output_conf.file_share_conf.host.user_name,
                                            config.output_conf.file_share_conf.host.password,
                                            config.input_conf.file_conf.path)
    elif config.output_conf.file_share_conf.system == "WINDOWS":
        FileTransferProcessor.windows_share(config.output_conf.file_share_conf.host,
                                            config.input_conf.file_conf.path,
                                            config.output_conf.file_share_conf.host.user_name,
                                            config.output_conf.file_share_conf.host.password,
                                            config.output_conf.file_share_conf.host.source_folder)
    else:
        raise Exception("Invalid Target System, Supported System are UNIX and WINDOWS")

except Exception as e:
    logger.error("File Transfer Failed with Error:" + str(e))
    print("File Transfer Failed with Error: {0}".format(str(e)))
    raise e
