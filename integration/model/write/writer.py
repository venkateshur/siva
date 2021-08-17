import cx_Oracle


def load_into_oracle(data, oracle_conf):
    conn = cx_Oracle.connect(oracle_conf.user_name, oracle_conf.password,
                             oracle_conf.host + ":" + oracle_conf.port + "/" + oracle_conf.service_name, encoding="UTF-8")
    # cur = con.cursor()
    data.toSql(oracle_conf.table_name, conn)


def csv_writer(df, file_name, output_file_conf):
    if isinstance(df, dict):
        for sheet in df:
            sheet.to_csv(output_file_conf.source_folder + file_name + "_" + sheet + ".csv",
                         index=None,
                         sep=output_file_conf.delimiter,
                         header=True)
    else:
        df.to_csv(output_file_conf.source_folder + file_name + ".csv",
                  index=None,
                  sep=output_file_conf.delimiter,
                  header=True)


def text_writer(df, file_name, output_file_conf):
    if isinstance(df, dict):
        for sheet in df:
            sheet.to_csv(output_file_conf.source_folder + file_name + "_" + sheet + ".txt",
                         index=None,
                         sep=output_file_conf.delimiter,
                         header=False)
    else:
        df.to_csv(output_file_conf.source_folder + file_name + ".txt",
                  index=None,
                  sep=output_file_conf.delimiter,
                  header=False)


def excel_writer(df, file_name, output_file_conf):
    df.to_excel(output_file_conf.source_folder + file_name + ".xlsx",
                header=True)
