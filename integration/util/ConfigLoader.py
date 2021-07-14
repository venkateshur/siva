from conf.SharepointConf import SharepointConf
from conf.FileConf import FileConf
from conf.OracleConf import OracleConf
from conf.InputConf import InputConf
from conf.OutputConf import OutputConf
from conf.FileShareConf import FileShareConf

from conf.AppConf import AppConf

import configparser


def load_app_config(config_path):
    try:
        conf = configparser.ConfigParser()
        conf.read(config_path)
        print(conf)
        load_io_conf = load_conf(conf)
        app_conf = get_app_conf(load_io_conf[0], load_io_conf[1], conf['CONVERSION']["type"])

        return app_conf

    except Exception as e:
        raise e


def get_app_conf(input_conf, output_conf, conversion_conf):
    return AppConf(input_conf, output_conf, conversion_conf)


def load_conf(config):
    source = config['INPUT']['source']
    input_temp_path = config['INPUT']['input_temp_path']

    share_point_conf = SharepointConf(config['SHAREPOINT']['url'],
                                      config['SHAREPOINT']['file_format'],
                                      config['SHAREPOINT']['excel_all_sheets'],
                                      config['SHAREPOINT']['excel_required_sheets'],
                                      config['SHAREPOINT']['csv_fields'],
                                      config.getboolean(['SHAREPOINT']['csv_header'], False),
                                      config['SHAREPOINT']['user_name'],
                                      config['SHAREPOINT']['password'])

    file_conf = FileConf(config['INPUT']['FILE']['path'],
                         config['INPUT']['FILE']['file_format'],
                         config['INPUT']['FILE']['excel_all_sheets'],
                         config['INPUT']['FILE']['excel_required_sheets'],
                         config['INPUT']['FILE']['csv_fields'],
                         config.getboolean(['INPUT']['FILE']['csv_header'], False))

    input_conf = InputConf(source, input_temp_path, share_point_conf, file_conf)

    target = config['OUTPUT']['target']
    oracle_conf = OracleConf(config['ORACLE']['host'],
                             config['ORACLE']['port'],
                             config['ORACLE']['service_name'],
                             config['ORACLE']['user_name'],
                             config['ORACLE']['password'],
                             config['ORACLE']['table_name'])

    output_file_conf = FileConf(config['OUTPUT']['FILE']['path'],
                                config['OUTPUT']['FILE']['file_format'],
                                config['OUTPUT']['FILE']['excel_all_sheets'],
                                config['OUTPUT']['FILE']['excel_required_sheets'],
                                config['OUTPUT']['FILE']['header_fields'])

    file_share_conf = FileShareConf(config['system'],
                                    config['host'],
                                    config['port'],
                                    config['user'],
                                    config['password'],
                                    config['path'])

    output_conf = OutputConf(target, oracle_conf, output_file_conf, file_share_conf)

    return input_conf, output_conf
