import logging
import sys
from datetime import datetime

from model.processor import FileTransferProcessor

if __name__ == "__main__":
    print("File Transfer App")

logger = logging.getLogger("File Transfer")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('File Transfer - Started @: ' + current_timestamp)
print('File Transfer - Started @: ' + current_timestamp)

try:
    source_system = sys.argv[1]
    target_system = sys.argv[2]
    files_path = sys.argv[3]
    cert_directory = sys.argv[4]
    cert_name = sys.argv[5]
    cert_password = sys.argv[6]
    target_directory = sys.argv[7]

    if source_system == "UNIX" and target_system == "WINDOWS":
        FileTransferProcessor.unix_transfer(files_path,
                                            cert_directory,
                                            cert_name,
                                            cert_password,
                                            target_directory)

    elif source_system == "WINDOWS" and target_system == "UNIX":
        FileTransferProcessor.unix_transfer(files_path,
                                            cert_directory,
                                            cert_name,
                                            cert_password,
                                            target_directory)
    else:
        raise Exception("Invalid Target System, Supported System are UNIX and WINDOWS")

except Exception as e:
    logger.error("File Transfer Failed with Error:" + str(e))
    print("File Transfer Failed with Error: {0}".format(str(e)))
    raise e
