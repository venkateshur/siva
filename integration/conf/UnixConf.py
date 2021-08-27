class UnixConf(object):
    def __init__(self, cert_directory, cert_name, cert_password, server, file_path):
        self.cert_directory = cert_directory
        self.cert_name = cert_name
        self.cert_password = cert_password
        self.server = server
        self.file_path = file_path
