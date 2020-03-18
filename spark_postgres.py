import pyspark as ps    # for the pyspark suite

def getSparkSession():
        # we try to create a SparkSession to work locally on all cpus available
    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .config("spark.jars", "/home/mddarr/data/spark_jars/postgresql-42.2.11.jar") \
        .getOrCreate()
    return spark

url = 'jdbc:postgresql://kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com/kaladindb'
properties = {
    "driver": "org.postgresql.Driver",
    "user": "postgres",
    "password": "tchoob89"
}
spark = getSparkSession()
trip_reportsDF =  spark.read.jdbc(url=url,table='trip_reports', properties=properties)