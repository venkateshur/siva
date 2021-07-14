class OracleConf(object):
    def __init__(self, host, port, service_name, user_name, password, table_name):
        self.host = host
        self.port = port
        self.service_name = service_name
        self.user_name = user_name
        self.password = password
        self.table_name = table_name
