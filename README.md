# Stock Market Kafka Real-Time Data

## Introduction

In this project, I implemented a complete end-to-end data engineering pipeline to handle real-time stock market data using Apache Kafka. This project involved integrating several technologies to build a robust data processing system that ingests, processes, and analyzes streaming data efficiently.

## Technologies Used

- **Programming Language**: Python
- **Amazon Web Services (AWS)**:
  - **S3** (Simple Storage Service): Used for storing data files and logs.
  - **Athena**: Utilized for querying data stored in S3.
  - **Glue Crawler**: Automated the discovery and cataloging of data in S3.
  - **Glue Catalog**: Managed metadata for data stored in S3.
  - **EC2**: Deployed Kafka brokers and other services.
- **Apache Kafka**: Core technology for streaming data ingestion and processing.
- **SQL**: Used for querying and manipulating data.

## Dataset Used

I utilized a stock market dataset for this project. The dataset contains real-time stock market data, including various metrics and financial indicators. For demonstration purposes, you can use any relevant stock market dataset that suits your needs.

## Project Overview

1. **Kafka Setup**: Configured Kafka brokers and topics to handle real-time data streaming.
2. **Data Ingestion**: Developed Kafka producers in Python to stream stock market data into Kafka topics.
3. **Data Processing**: Implemented Kafka consumers to process and store data in AWS S3.
4. **Data Querying**: Set up AWS Athena to query the processed data stored in S3.
5. **Metadata Management**: Used AWS Glue to crawl and catalog data for easy querying with Athena.

## How to Run

1. **Kafka Setup**: Ensure Kafka brokers are running and configured properly.
2. **Run Producers**: Execute the Kafka producer script to start streaming data into Kafka topics.
3. **Run Consumers**: Execute the Kafka consumer script to process and store data in S3.
4. **Query Data**: Use AWS Athena to run queries on the data stored in S3.
5. **Manage Metadata**: Use AWS Glue to manage and catalog the data.

## Files Included

- `kafka_producer.py`: Python script for streaming data into Kafka topics.
- `kafka_consumer.py`: Python script for consuming data from Kafka topics and storing it in S3.
- `.gitignore`: Git ignore file for excluding unnecessary files from version control.


