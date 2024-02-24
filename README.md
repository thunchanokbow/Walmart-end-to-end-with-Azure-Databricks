# Walmart-end-to-end-with-Azure-Databricks
This project integrates data from websites using Azure Data Factory. The data is extracted in batches and transformed using Spark in Azure Databricks. The transformed data is stored in Synapse Analytics in columnar format. Finally, a dashboard is created using Looker Studio or Power BI to display sales data, customer analysis, and other information to users
## Project Overview
![0](/images/0.png)

## Contents 
[Create Storage Account](sections/01-cloud-sql-for-mysql-database.md).<br>
- [Azure Blob Storage](sections/01-cloud-sql-for-mysql-database.md#Hosting-MySQL-on-Cloud-SQL).<br>
- [Azure Data Lake Storage Gen2](sections/01-cloud-sql-for-mysql-database.md#Hosting-MySQL-on-Cloud-SQL).<br>

[Create Azure Data Factory](sections/01-cloud-sql-for-mysql-database.md).<br>
[Create Linked Services](sections/01-cloud-sql-for-mysql-database.md).<br>
- [Source Linked Services](sections/01-cloud-sql-for-mysql-database.md#Hosting-MySQL-on-Cloud-SQL).<br>
- [Sink Linked Services](sections/01-cloud-sql-for-mysql-database.md#Hosting-MySQL-on-Cloud-SQL).<br>

[Create Dataset](sections/01-cloud-sql-for-mysql-database.md).<br>
- [Dataset of Azure Blob Storage](sections/01-cloud-sql-for-mysql-database.md#Hosting-MySQL-on-Cloud-SQL).<br>
- [Dataset of Azure Data Lake Storage Gen2](sections/01-cloud-sql-for-mysql-database.md#Hosting-MySQL-on-Cloud-SQL).<br>

[Create Pipelines Using Azure Data Factory](sections/01-cloud-sql-for-mysql-database.md).<br>
