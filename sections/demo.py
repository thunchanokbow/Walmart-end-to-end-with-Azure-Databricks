from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("My PySpark App") \
    .getOrCreate()

# Your PySpark code goes here



