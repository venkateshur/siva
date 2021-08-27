class FileConversionConf(object):
    def __init__(self, source_format, target_format, source_file_conf, target_file_conf):
        self.source_format = source_format
        self.target_format = target_format
        self.source_file_conf = source_file_conf
        self.target_file_conf = target_file_conf
