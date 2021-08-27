class FileTransferConf(object):
    def __init__(self, source, target, unix_conf, windows_conf):
        self.source = source
        self.target = target
        self.unix_conf = unix_conf
        self.windows_conf = windows_conf
