import logging
import sys
from datetime import datetime

from util.ConfigLoader import load_app_config
from model.processor import FileTransferProcesstr
from model.write.writer import load_into_oracle

if __name__ == "__main__":
    print("File Transfer App")

logger = logging.getLogger("File Transfer")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File Transfer - Started @: ' + current_timestamp)
print('File Transfer - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1])
    data = FileTransferProcesstr.unix_transfer(config.output_conf.file_share_conf.host.path,
                                               config.output_conf.file_share_conf.host,
                                               config.output_conf.file_share_conf.port,
                                               config.output_conf.file_share_conf.host.user_name,
                                               config.output_conf.file_share_conf.host.password,
                                               config.input_conf.file_conf.path,
                                               config.output_conf.file_share_conf.host.file)

except Exception as e:
    logger.error("Data Integrator Failed with Error:" + str(e))
    print("Data Integrator Failed with Error: {0}".format(str(e)))
    raise e
