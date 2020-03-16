create_trip_report_table = (""" CREATE TABLE IF NOT EXISTS trip_reports(
                            trip_id serial PRIMARY KEY ,
                            trip_name VARCHAR NOT NULL,
                            trip_report VARCHAR NOT NULL,
                            locations text[] NOT NULL,
                            elevationGain float NOT NULL,
                            mileage INT NOT NULL);    
                        """)

trip_location =(""" CREATE TABLE IF NOT EXISTS geographic_location(
                            elevation INT NOT NULL,
                            lat INT NOT NULL;
                            lng INT NOT NULL;
                            location_name VARCHAR NOT NULL,
                            terrain text[] NOT NULL
                        """)

trail_table_create = ("""CREATE TABLE IF NOT EXISTS locations (
                            location_id SERIAL PRIMARY KEY,
                            trail_name CHAR(50) NOT NULL,
                            elevation INT,
                            region_id INT REFERENCES basins(basin_id) 
                            );""")



trip_report_table_insert = ("""INSERT INTO trip_reports (trip_name, trip_report, elevationGain, mileage, locations) VALUES (%s, %s, %s, %s, %s);""")
trip_location = ("""INSERT INTO trip_reports (trip_name, trip_report, elevationGain, mileage, locations) VALUES (%s, %s, %s, %s);""")
trail_table_create = ("""INSERT INTO trip_reports (trip_name, trip_report, elevationGain, mileage, locations) VALUES (%s, %s, %s, %s);""")

## I should find out how to add arrays to my postgreSQL table.