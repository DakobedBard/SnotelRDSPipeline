from snotel.wta.sql_queries import trip_report_table
import psycopg2


conn = psycopg2.connect("host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=tchoob89")
cur = conn.cursor()
create_table_queries = [trip_report_table]

for query in create_table_queries:
    cur.execute(query)
conn.commit()