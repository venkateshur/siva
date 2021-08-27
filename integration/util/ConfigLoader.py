import configparser

from conf.AppConf import AppConf
from conf.FileConf import FileConf
from conf.FileConversionConf import FileConversionConf
from conf.FileShareConf import FileShareConf
from conf.FileTransferConf import FileTransferConf
from conf.InputConf import InputConf
from conf.UnixConf import UnixConf
from conf.OracleConf import OracleConf
from conf.OracleFileConf import OracleFileConf
from conf.OutputConf import OutputConf
from conf.SharepointConf import SharepointConf
from conf.WindowsConf import WindowsConf
from conf.RestServiceFIleConf import RestServiceFileConf
from conf.RestConf import RestConf


def load_app_config(config_path, conf_type=None):
    try:
        conf = configparser.ConfigParser()
        conf.read(config_path)
        print(conf)
        if conf_type == "oracle-file":
            config = oracle_file_conf(conf)
        elif conf_type == "file-conversion":
            config = file_conversion_conf(conf)
        elif conf_type == "file-transfer":
            config = file_transfer_conf(conf)
        elif conf_type == "rest-service-file":
            config = rest_service_file_conf(conf)
        else:
            load_io_conf = load_conf(conf)
            config = get_app_conf(load_io_conf[0], load_io_conf[1], conf['CONVERSION']["type"])

        return config

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
                                    config['source_path'],
                                    config['target_path'],
                                    config['file_name'])

    output_conf = OutputConf(target, oracle_conf, output_file_conf, file_share_conf)

    return input_conf, output_conf


def file_transfer_conf(config):
    linux_conf = UnixConf(config['FILE-TRANSFER.UNIX']['cert_directory'],
                          config['FILE-TRANSFER.UNIX']['cert_name'],
                          config['FILE-TRANSFER.UNIX']['cert_password'],
                          config['FILE-TRANSFER.UNIX']['server'],
                          config['FILE-TRANSFER.UNIX']['file_path'])

    windows_conf = WindowsConf(config['FILE-TRANSFER.WINDOWS']['dir'])
    return FileTransferConf(config['FILE-TRANSFER']['source_system'],
                            config['FILE-TRANSFER']['target_system'],
                            linux_conf,
                            windows_conf)


def file_conversion_conf(config):
    source_file_conf = FileConf(config['FILE-CONVERSION.SOURCE-FILE']['path'],
                                config['FILE-CONVERSION.SOURCE-FILE']['file_format'],
                                config['FILE-CONVERSION.SOURCE-FILE']['excel_all_sheets'],
                                config['FILE-CONVERSION.SOURCE-FILE']['excel_required_sheets'],
                                config['FILE-CONVERSION.SOURCE-FILE']['header_fields'])

    target_file_conf = FileConf(config['FILE-CONVERSION.TARGET-FILE']['path'],
                                config['FILE-CONVERSION.TARGET-FILE']['file_format'],
                                config['FILE-CONVERSION.TARGET-FILE']['excel_all_sheets'],
                                config['FILE-CONVERSION.TARGET-FILE']['excel_required_sheets'],
                                config['FILE-CONVERSION.TARGET-FILE']['header_fields'])

    return FileConversionConf(config['FILE-CONVERSION']['source_format'],
                              config['FILE-CONVERSION']['target_format'],
                              source_file_conf,
                              target_file_conf)


def oracle_file_conf(config):
    oracle_conf = OracleConf(config['ORACLE-FILE.ORACLE']['host'],
                             config['ORACLE-FILE.ORACLE']['port'],
                             config['ORACLE-FILE.ORACLE']['service_name'],
                             config['ORACLE-FILE.ORACLE']['user_name'],
                             config['ORACLE-FILE.ORACLE']['password'],
                             config['ORACLE-FILE.ORACLE']['table_name'],
                             config['ORACLE-FILE.ORACLE']['columns'].split(";"))

    file_conf = FileConf(config['ORACLE-FILE.ORACLE']['path'],
                         config['ORACLE-FILE.ORACLE']['file_format'],
                         config['ORACLE-FILE.ORACLE']['excel_all_sheets'],
                         config['ORACLE-FILE.ORACLE']['excel_required_sheets'].split(";"),
                         config['ORACLE-FILE.ORACLE']['header_fields'].split(";"))

    return OracleFileConf(config['ORACLE-FILE']['source'],
                          config['ORACLE-FILE']['target'],
                          oracle_conf,
                          file_conf)


def rest_service_file_conf(config):
    rest_conf = RestConf(config['REST-SERVICE-FILE.REST']['api'],
                         config['REST-SERVICE-FILE.REST']['cert_directory'],
                         config['REST-SERVICE-FILE.REST']['cert_name'],
                         config['REST-SERVICE-FILE.REST']['cert_password'])

    file_conf = FileConf(config['REST-SERVICE-FILE.FILE']['path'],
                         config['REST-SERVICE-FILE.FILE']['file_format'],
                         config['REST-SERVICE-FILE.FILE']['excel_all_sheets'],
                         config['REST-SERVICE-FILE.FILE']['excel_required_sheets'],
                         config['REST-SERVICE-FILE.FILE']['header_fields'])

    return RestServiceFileConf(config['REST-SERVICE-FILE']['source'],
                               config['REST-SERVICE-FILE']['target'],
                               rest_conf,
                               file_conf)
