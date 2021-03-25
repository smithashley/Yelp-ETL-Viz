# Yelp ETL and Visualization

![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/aws_diag.png)

This project extracted JSON data from Amazon S3 into a dataframe, transformed the data, loaded to the data warehouse, created two more tables using queries in Redshift, connected Redshift to Tableau server,  and visualized the data on a dashboard.
  - The yelp reviews were filtered given the hypothetical search for businesses that sell pizza and served wine for pairing in these metropolitan areas. 

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
- Transformed data
  - Dropped columns as needed
  - Extracted nested JSON
  - Filtered dataframe
- Installed JDBC driver, spark-redshift package, spark-avro package, and AWS java sdk on cluster
- Configured the connection to Amazon Redshift
- Wrote data to the data warehouse
- Unmounted S3 storage

## Data Warehouse Queries
![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/query1.png)
- Created a left join as the business table was filtered for businesses that sell pizza before being loaded to the data warehouse
![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/query_2.png)
- Created a query that 
## Data Visualization
![](https://github.com/smithashley/Yelp-ETL-Viz/blob/main/embedded_images/tableau_screenshot2.png)
Created an interactive dashboard with three visualizations
- Average stars for each Pizzeria -> to find highest rated restaurant in each city
- Reviews by City, State -> comparing reviews with and without pairing  
- Average stars by state -> map out states that have highest reviewed pizza
