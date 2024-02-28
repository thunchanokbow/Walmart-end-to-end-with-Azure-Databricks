"""
# Top Products Walmart 09-2022
##### Businesses Requirements:
1. The Marketing team needs a list of top subcategories in the month of September 2022. 
So that they can promote by placing them in more visible locations and on the website or application. 
2. The Product team requires a list of top-selling product names within the top subcategories. 
So that they can contact the suppliers to order more products and discuss pricing options.

##### Product information from Walmart's Grocery that cantains the following columns:
- SHIPPING_LOCATION: The location where the product is shipped from. (String)
- DEPARTMENT: The department in which the product is categorized. (String)
- CATEGORY: The category in which the product is categorized. (String)
- SUBCATEGORY: The subcategory in which the product is categorized. (String)
- BREADCRUMBS: The breadcrumbs for the product. (String)
- SKU: The SKU for the product. (String)
- PRODUCT_URL: The URL for the product. (String)
- PRODUCT_NAME: The name of the product. (String)
- BRAND: The brand of the product. (String)
- PRICE_RETAIL: The retail price of the product. (Float)
- PRICE_CURRENT: The current price of the product. (Float)
- PRODUCT_SIZE: The size of the product. (String)
- PROMOTION: The promotion for the product. (String)
- RunDate: The date on which the data was collected. (Date)

##### Clean and Drop Unnecessary Columns. 
1. Converted 'Shop All' to 'Shop all' in lower case in SUBCATEGORY column.
2. Converted PRODUCT_SIZE column to numeric.
3. Checked for missing values.
- SUBCATEGORY has missing value.
- BRAND has missing value.
- PRODUCT_SIZE has missing value.
- PROMOTION has missing value. 
4. Removed 
- the Extra Index Column.
- PROMOTION column.
- tid column.
- PRODUCT_URL column.
- PRICE_RETAIL column.
- PRICE_CURRENT column.
5. Separated the PRODUCT_NAME column removed product size from it.
6. Fill missing values
- PRODUCT_SIZE with the mean of the column.
- SUBCATEGORY with the mode of the column.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create a SparkSession
spark = SparkSession.builder \
    .appName("My PySpark App") \
    .getOrCreate()

# Your PySpark code goes here
# Read the data from the CSV file 
df = spark.read.csv("data.csv", header=True)
# Converted 'SHOP ALL' to lower case in SUBCATEGORY column. (3)
df = df.withColumn("SUBCATEGORY", F.lower(F.col("SUBCATEGORY")))
# Converted PRODUCT_SIZE column to numeric. (4)
df = df.withColumn("PRODUCT_SIZE", F.col("PRODUCT_SIZE").cast("double"))
# Check how many rows and columns we have in the table (5)
print("Number of rows: ", df.count())
# Check the data types and missing values of the columns (6)
df.printSchema()
# Remove the column 'Index' is not necessary (7.1)
df = df.drop("Index")
# Remove duplicate rows (7.2)
df = df.dropDuplicates()
# Remove the columns 'PROMOTION' (7.3)
df = df.drop("PROMOTION")
# Remove the columns 'tid' is not necessary (7.4)
df = df.drop("tid")
# Remove the column 'PRODUCT_URL' is not necessary (7.5)
df = df.drop("PRODUCT_URL")
# Remove the comma and everthing after it in the 'PRODUCT_NAME' column (8)
df.withColumn("PRODUCT_NAME", F.split(F.col("PRODUCT_NAME"), ",").getItem(0))
# Fill the missing values in the 'PRODUCT_SIZE' column with the mean of the cilumn (9.1)
df.withColumn("PRODUCT_SIZE", F.when(F.col("PRODUCT_SIZE").isNull(), df.select(F.mean("PRODUCT_SIZE")).collect()[0][0]).otherwise(F.col("PRODUCT_SIZE")))
# Fill the missing values in the 'SUBCATEGORY' column with th emode of the column (9.2)
df.fillna(df.groupby().agg(F.first(df["SUBCATEGORY"]).alias("SUBCATEGORY_MODE")).collect()[0]["SUBCATEGORY_MODE"])
# Get the top subcategories (12.1)
top_subcategories = df.filter(df["SUBCATEGORY"] != "shop all").groupBy("SUBCATEGORY").count().orderBy(F.col("count").desc()).select("SUBCATEGORY", "count").show()
# Save the top subcategories to a CSV file (12.2)
top_subcategories.write.csv("top_subcategories.csv")
# Filter the rows where the SUBCATEGORY is 'juice' (13)
juice = df.filter(df["SUBCATEGORY"] == "juice")
# Show the product names and their counts (14.1)
juice.select("PRODUCT_NAME","BRAND","DEPARTMENT","SUBCATEGORY").groupBy("PRODUCT_NAME","BRAND","DEPARTMENT","SUBCATEGORY").count().orderBy("count", ascending=False).show()
# Save juice to a CSV file (14.2)
juice.write.csv("juice.csv")
# Filter the rows where the PRODUCT_NAME is 'naked juice' (15)
naked_juice = juice.filter(juice["PRODUCT_NAME"] == "naked juice")