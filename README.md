
Connect to the RDS postgres database.. 

psql --host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com --port=5432 --username=postgres --password  --dbname=kaladindb


url = 'jdbc:postgresql://kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com/kaladindb'
properties = {
    "driver": "org.postgresql.Driver",
    "user": "postgres",
    "password": "tchoob89"
}

df.write.jdbc(url=db_url,table='testdb.employee',mode='overwrite',properties=db_properties)