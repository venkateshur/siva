class FileConf(object):
    def __init__(self, path, file_format, excel_all_sheets, excel_required_sheets, csv_fields, header):
        self.path = path
        self.file_format = file_format
        self.excel_all_sheets = excel_all_sheets
        self.excel_required_sheets = excel_required_sheets
        self.csv_fields = csv_fields
        self.header = header
