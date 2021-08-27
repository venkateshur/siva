class SharepointConf(object):
    def __init__(self, url, file, file_format, excel_all_sheets, excel_required_sheets, fields, header, user_name,
                 password):
        self.url = url
        self.file = file,
        self.file_format = file_format
        self.excel_all_sheets = excel_all_sheets
        self.excel_required_sheets = excel_required_sheets
        self.fields = fields
        self.header = header
        self.user_name = user_name
        self.password = password
