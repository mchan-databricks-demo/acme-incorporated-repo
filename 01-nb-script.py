# Databricks notebook source
s3Path = "dbfs:/mnt/mchan_superstore/orders”
df = spark.read
	.format("csv")
	.option(“sep”, “\t”)
  	.option(“encoding”, “UTF-8”)
	.option("header", ”true")
	.option("dateFormat", "yyyy-M-dd")
           .option(“timestampFormat”, “yyyy-MM-dd HH:mm:ss”)
	.option("inferSchema", "true")
        .withColumn(“fname”, input_file_name())
        .withColumn(“ingesttime”, current_timesstamp())
	.load(s3Path) 

# COMMAND ----------

print("some change here ")
