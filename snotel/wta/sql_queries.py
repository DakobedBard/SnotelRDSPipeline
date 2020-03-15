

trip_report_table = (""" CREATE TABLE IF NOT EXISTS trip_reports(
                            trip_id serial PRIMARY KEY ,
                            trip_name VARCHAR NOT NULL,
                            trip_report VARCHAR NOT NULL,
                            locations text[] NOT NULL,
                            elevationGain INT,
                            mileage INT,
                            
                        """)

location_table_create =(""" CREATE TABLE IF NOT EXISTS geographic_location(
                            lat INT NOT NULL;
                            lng INT NOT NULL;
                            trip_name VARCHAR NOT NULL,

                        """)


trail_table_create = ("""CREATE TABLE IF NOT EXISTS locations (
                            location_id SERIAL PRIMARY KEY,
                            trail_name CHAR(50) NOT NULL,
                            elevation INT,
                            region_id INT REFERENCES basins(basin_id) 
                            );""")


## I should find out how to add arrays to my postgreSQL table.