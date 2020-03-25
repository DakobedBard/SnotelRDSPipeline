import psycopg2
from snotel.snowpack.sql_queries import snowpack_table_insert
from datetime import date
from snotel.snowpack.run_scraper import extract_snowpack_data
import os
rds_password = os.environ.get('KALADIN_RDS_PASSWORD')
def insert_snowpack_data(basins_dict):
    conn = psycopg2.connect("host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=%s" % rds_password)
    cur = conn.cursor()

    year = basins_dict.pop('year')
    day = basins_dict.pop('day')
    month = basins_dict.pop('month')
    print("day " + str(day))
    date_ = date(year, month, day)
    locationID = 1
    for region in basins_dict.keys():
        basins_dict[region].pop('Basin Index')
        locations = basins_dict[region].keys()

        for location in locations:
            location_dict = basins_dict[region][location]
            snow_current =  validate_data(location_dict['Snow Current (in)'])
            snow_median = validate_data(location_dict['Snow Median (in)'])
            snow_pct_median = validate_data(location_dict['Snow Pct of Median'])
            water_current =validate_data(location_dict['Water Current '])
            water_current_average = validate_data(location_dict['Water Average (in)'])
            water_pct_average = validate_data(location_dict['Water Pct of Average'])
            try:
                cur.execute(snowpack_table_insert, (locationID ,date_, snow_current, snow_median, snow_pct_median, water_current, water_current_average, water_pct_average,))
            except Exception as e:
                print(e)
            locationID += 1
        conn.commit()
    conn.close()

def validate_data(data):
    if data == '':
        data = 0
    return data


insert_snowpack_data(extract_snowpack_data())