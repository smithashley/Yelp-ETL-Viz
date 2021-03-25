# Yelp ETL and Visualization

![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/aws_diag.png)

This project extracts JSON data from Amazon S3 into a dataframe, transforms the data, loads to the data warehouse, creates two more tables using Redshift queries, connects to Tableau server and visualizes the data on a dashboard.

## About the Dataset
- This dataset is a subset of businesses, reviews, and user data across 10 metropolitan areas
- This amounts to 8,021,122 reviews of 209,393 businesses (10 GB of data)
- Dataset is available here: https://www.yelp.com/dataset
- Example of the format
![](https://github.com/smithashley/Yelp-Reviews-Dimensional-Data-Model/blob/main/images/exjson.png)

Steps for ETL in Databricks
- Loaded data to S3
- Created user and retrieved necessary keys
- Mounted S3 storage in Databricks notebook
- Listed objects in S3
- Read in data with given path from list
- Cleaned columns as needed
- Downloaded JDBC driver, spark-redshift package, spark-avro package, AWS java sdk
- Configured the connection to Amazon Redshift
- Wrote data to the data warehouse


## Data Warehouse Queries
![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/query1.png)
![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/query2.png)

## Data Visualization
![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/tableau_screenshot2.png)
[This link will take you to the Tableau dashboard]()
