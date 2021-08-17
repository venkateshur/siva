class FileShareConf(object):
    def __init__(self, system, host, port, user_name, password, source_folder, target_folder, file_name):
        self.system = system
        self.host = host
        self.port = port
        self.user_name = user_name
        self.password = password
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.file_name = file_name
