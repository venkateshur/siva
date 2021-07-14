import logging
import sys
from datetime import datetime

from util.ConfigLoader import load_app_config
from model.processor import MainProcessor
from model.write.writer import load_into_oracle

if __name__ == "__main__":
    print("Data Integrator App")

logger = logging.getLogger("Data integrator")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('Data integrator - Started @: ' + current_timestamp)
print('Data integrator - Started @: ' + current_timestamp)

try:
    config = load_app_config(sys.argv[1])
    data = MainProcessor.main_processor(config)
    if isinstance(data, dict):
        for df in data:
            load_into_oracle(df, config.output_conf.oracle_conf)
    else:
        load_into_oracle(data, config.output_conf.oracle_conf)

except Exception as e:
    logger.error("Data Integrator Failed with Error:" + str(e))
    print("Data Integrator Failed with Error: {0}".format(str(e)))
    raise e
