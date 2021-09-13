import glob
import logging
import sys
from datetime import datetime

from model.processor import SharepointProcessor

if __name__ == "__main__":
    print("Sharepoint Integration App")

logger = logging.getLogger("File Transfer")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('Sharepoint Integration - Started @: ' + current_timestamp)
print('Sharepoint Integration - Started @: ' + current_timestamp)

try:
    source = sys.argv[1]
    target = sys.argv[2]
    source_target_path = sys.argv[3]
    client_id = sys.argv[4]
    client_certificate = sys.argv[5]
    sharepoint_url = sys.argv[6]
    file_url = sys.argv[7]

    if source == "SHAREPOINT" and target == "FILE":
        SharepointProcessor.download_from_sharepoint(sharepoint_url,
                                                     client_id,
                                                     client_certificate,
                                                     file_url,
                                                     source_target_path)

    elif source == "FILE" and target == "SHAREPOINT":
        files = glob.glob(source_target_path + "/*")
        for file in files:
            SharepointProcessor.upload_file_to_sharepoint(sharepoint_url,
                                                          client_id,
                                                          client_certificate,
                                                          file_url,
                                                          file)
    else:
        raise Exception("Invalid Source and Target Types, Supported System are UNIX and WINDOWS")

except Exception as e:
    logger.error("Sharepoint Integration Failed with Error:" + str(e))
    print("Sharepoint Integration Failed with Error: {0}".format(str(e)))
    raise e
