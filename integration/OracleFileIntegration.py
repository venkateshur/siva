import logging
import sys
from datetime import datetime

from model.read import Reader
from model.write import writer
from model.write.writer import load_into_oracle
from conf.OracleConf import OracleConf
from conf.FileConf import FileConf
import glob

if __name__ == "__main__":
    print("Data integrator - Oracle File Loading or Unloading")

logger = logging.getLogger("Data integrator - Oracle File Loading or Unloading")
logger.setLevel(logging.INFO)

current_timestamp = str(datetime.now())
logging.info('Loading file to oracle - Started @: ' + current_timestamp)
print('Loading file to oracle - Started @: ' + current_timestamp)

try:
    load_type = sys.argv[1]
    file_path = sys.argv[2]
    delimiter = sys.argv[3]
    header = sys.argv[4]
    required_fields = sys.argv[5]

    table_name = sys.argv[6]
    host = sys.argv[7]
    port = sys.argv[8]
    service_name = sys.argv[9]
    user_name = sys.argv[10]
    password = sys.argv[11]
    columns = sys.argv[12]

    oracle_conf = OracleConf(host, port, service_name, user_name, password, table_name, columns)
    if load_type == "FILE-ORACLE":
        files = glob.glob(file_path + "/*.csv")
        for file in files:
            data = Reader.csv_reader(file, required_fields, delimiter, header)
            load_into_oracle(data, oracle_conf)

    if load_type == "ORACLE-FILE":
        data = Reader.read_from_oracle_query(oracle_conf)
        file_conf = FileConf(file_path, "CSV", None, None, None, True)
        writer.csv_writer(data, oracle_conf.table_name.replace(".", "_"), file_conf)

except Exception as e:
    logger.error("Loading file to oracle Failed with Error:" + str(e))
    print("Loading file to oracle Failed with Error: {0}".format(str(e)))
    raise e
