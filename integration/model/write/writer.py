import cx_Oracle


def load_into_oracle(data, oracle_conf):
    con = cx_Oracle.connect(oracle_conf.hos)
    # cur = con.cursor()
    data.toSql(oracle_conf.table_name, con)


def csv_writer(df, file_name, output_file_conf):
    if isinstance(df, dict):
        for sheet in df:
            sheet.to_csv(output_file_conf.path + file_name + "_" + sheet + ".csv",
                         index=None,
                         sep=output_file_conf.delimiter,
                         header=True)
    else:
        df.to_csv(output_file_conf.path + file_name + ".csv",
                  index=None,
                  sep=output_file_conf.delimiter,
                  header=True)


def text_writer(df, file_name, output_file_conf):
    if isinstance(df, dict):
        for sheet in df:
            sheet.to_csv(output_file_conf.path + file_name + "_" + sheet + ".txt",
                         index=None,
                         sep=output_file_conf.delimiter,
                         header=False)
    else:
        df.to_csv(output_file_conf.path + file_name + ".txt",
                  index=None,
                  sep=output_file_conf.delimiter,
                  header=False)
