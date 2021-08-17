import logging
import sys
from datetime import datetime

from util.ConfigLoader import load_app_config
from model.processor import MainProcessor
from model.write.writer import load_into_oracle

if __name__ == "__main__":
    print("Loading file to oracle App")

logger = logging.getLogger("Data integrator")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('Loading file to oracle - Started @: ' + current_timestamp)
print('Loading file to oracle - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1])
    data = MainProcessor.main_processor(config)
    if isinstance(data, dict):
        for df in data:
            load_into_oracle(df, config.output_conf.oracle_conf)
    else:
        load_into_oracle(data, config.output_conf.oracle_conf)

except Exception as e:
    logger.error("Loading file to oracle Failed with Error:" + str(e))
    print("Loading file to oracle Failed with Error: {0}".format(str(e)))
    raise e
