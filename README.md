# Automated Sales Pipeline (Foundation Project)

This project is the foundational "warm-up" for my Data Engineering roadmap. I built a mini-pipeline that automates data ingestion, ensures data quality through database constraints, and generates business-ready reports.

# Tech Stack & Features
Data Generation     : Used Python with the "Faker" library to simulate 150 randomized customer transactions.
Database Management : Stored data in a PostgreSQL instance running on Docker for a portable development environment.
Security First      : Implemented ".env" variables to keep database credentials secure and out of version control.
Data Integrity      : Applied SQL CHECK constraints to prevent invalid entries (e.g., negative prices) from entering the pipeline.
Business Logic      : Created SQL Views to automatically identify "VIP" customers based on a total spend threshold (> RM10,000).
Automated Reporting : Developed a Python script to export the processed VIP list into a clean CSV format for stakeholders.

# Repository Structure
* 'ingest_data.py'  : Main script for generating and loading data into PostgreSQL.
* 'export_vip.py'   : Utility script to generate the VIP CSV report.
* 'schema_v2.sql'   : Contains the DDL for tables, constraints, and views.
* '.gitignore'      : Ensures sensitive files like `.env` are never uploaded.

# Challenges & Learning
This project helped me master the SQL 'GROUP BY' logic and the end-to-end flow of data from a script into a relational database. It also reinforced the importance of using environment variables to keep code secure and production-ready.