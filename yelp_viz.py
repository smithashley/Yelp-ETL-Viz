# Databricks notebook source
#mount object storage
access_key = 'AKIASNRX6T33AHZNZJUL'
secret_key = '5RWeYHwc2W6Fo8bBxfW5EFSx0vgfcv8D0JDkq2TZ'
encoded_secret_key = secret_key.replace('/', '%2F')
aws_bucket_name = 'yelpdata321'
mount_name = 'yelp_data'

dbutils.fs.mount('s3a://%s:%s@%s' % (access_key, encoded_secret_key, aws_bucket_name), '/mnt/%s' % mount_name)

# COMMAND ----------

#list objects in mounted storage
display(dbutils.fs.ls('/mnt/%s' % mount_name))

# COMMAND ----------

#use path from list to read in the first table
reviewDF = spark.read.json('dbfs:/mnt/yelp_data/yelp_academic_dataset_review.json')

# COMMAND ----------

reviewDF.show()

# COMMAND ----------

#clean table by dropping columns
reviews_table = reviewDF.drop('cool').drop('funny').drop('text').drop('user_id').drop('useful')

# COMMAND ----------

reviews_table.show()

# COMMAND ----------

#use path from list to read in the second table
businessDF = spark.read.json('dbfs:/mnt/yelp_data/yelp_academic_dataset_business.json')

# COMMAND ----------

businessDF.show()

# COMMAND ----------

from pyspark.sql.functions import col
#select needed columns and pull a field from nested JSON
nestedbusinessDF=businessDF.select('business_id', 'name', 'categories', 'city', 'state', 'attributes').withColumn('pairing', col('attributes').getField('Alcohol'))

# COMMAND ----------

nestedbusinessDF.show()

# COMMAND ----------

#clean table by dropping a column
cleanbusinessDF=nestedbusinessDF.drop('attributes')

# COMMAND ----------

cleanbusinessDF.show()

# COMMAND ----------

#filter for businesses that serve pizza
business_table=cleanbusinessDF.filter(col('categories').contains('Pizza'))

# COMMAND ----------

business_table.show()

# COMMAND ----------

jdbcurl='jdbc:redshift://afsmithcodes.cqb09qjhxszz.us-east-1.redshift.amazonaws.com:5439/yelpdw?user=afsmithcodes&password=LOVE4life$'
tempdir='s3a://AKIASNRX6T33AHZNZJUL:5RWeYHwc2W6Fo8bBxfW5EFSx0vgfcv8D0JDkq2TZ@yelpdata321/tempdir/'

# COMMAND ----------

#write reviews table to data warehouse
reviews_table.write.format('com.databricks.spark.redshift').option('url', jdbcurl).option('dbtable', 'reviews').option('tempdir', tempdir).option('forward_spark_s3_credentials', 'true').save()

# COMMAND ----------

#write business table to data warehouse
business_table.write.format('com.databricks.spark.redshift').option('url', jdbcurl).option('dbtable', 'business').option('tempdir', tempdir).option('extracopyoptions', 'TRUNCATECOLUMNS').option('forward_spark_s3_credentials', 'true').save()

# COMMAND ----------

#unmount object storage
dbutils.fs.unmount('/mnt/yelp_data')
