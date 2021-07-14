import cx_Oracle
import csv

con = cx_Oracle.connect('hr/hrpsw@localhost/orcl')
cur = con.cursor()
with open("locations.csv", "r") as csv_file:
    fields = ['F_LOCATION_ID', 'F_STREET_ADDRESS', 'F_POSTAL_CODE', 'F_CITY', 'F_STATE_PROVINCE', 'F_COUNTRY_ID']
    csv_reader = csv.DictReader(csv_file, fieldnames=fields, delimiter='|')
    for lines in csv_reader:
        cur.execute(
            "insert into new_locations (LOCATION_ID, STREET_ADDRESS, POSTAL_CODE,"
            " CITY, STATE_PROVINCE, COUNTRY_ID) values (:1, :2, :3, :4, :5, :6)",
            (lines['F_LOCATION_ID'], lines['F_STREET_ADDRESS'], lines['F_POSTAL_CODE'],
             lines['F_CITY'], lines['F_STATE_PROVINCE'], lines['F_COUNTRY_ID']))

cur.close()
con.commit()
con.close()
