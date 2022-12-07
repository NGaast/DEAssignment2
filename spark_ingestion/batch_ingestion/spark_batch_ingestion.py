from resources.data_management import DataManagement

from pyspark.sql import SparkSession
from pyspark import SparkConf

data_manager = DataManagement('de-2022-ng', 'data_de2022_ng')

# Fetch batch files
fixtures_file = data_manager.fetch_json('fixtures.json', 'tmp') # /tmp/fixtures.json
statistics_file = data_manager.fetch_json('statistics.json', 'tmp') # /tmp/statistics.json


sparkConf = SparkConf()
sparkConf.setMaster("spark://spark-master:7077")
sparkConf.setAppName("DataSourceSinkExample")
sparkConf.set("spark.driver.memory", "2g")
sparkConf.set("spark.executor.cores", "1")
sparkConf.set("spark.driver.cores", "1")

# create the spark session, which is the entry point to Spark SQL engine.
spark = SparkSession.builder.config(conf=sparkConf).getOrCreate()
df = spark.read.format("csv").option("header", "true") \
       .load("/home/jovyan/data/sales.csv")
df.printSchema()

newDf = df.select('unit_sales')  # select one column

newDf.show()
newDf.write.format("text").option("header", "false") \
      .mode("overwrite").save("/home/jovyan/data/output.txt")


