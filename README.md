# Walmart-end-to-end-with-Azure-Databricks
This project integrates data from websites using Azure Data Factory. The data is extracted in batches and transformed using Spark in Azure Databricks. The transformed data is stored in Synapse Analytics in columnar format. Finally, a dashboard is created using Looker Studio or Power BI, As a result of my project, fresh food has become their top category! This will help with the decision to promote fresh food by placing them in more visible locations and on the website or application. Their most popular fresh food is MorningStar Farms Veggie Burgers, with customers picking up a total of 184 units daily. With this information, the company is able to contact MorningStar Farm's to order more products and discuss pricing options.
## Project Overview
![0](/images/0.png)

## Contents 
[Create Storage Account](sections/01-storage-accounts.md).<br> 
- [Azure Blob Storage](sections/01-storage-accounts.md).<br>
- [Azure Data Lake Storage Gen2](sections/01-storage-accounts.md).<br>

[Create Azure Data Factory](sections/01-storage-accounts.md).<br>
- [Create Linked Services](sections/01-storage-accounts.md).<br>
  - [Source Linked Services](sections/01-storage-accounts.md).<br>
  - [Sink Linked Services](sections/01-storage-accounts.md).<br>
  - [Databricks Linked Services](sections/01-storage-accounts.md).<br>

- [Create Dataset](sections/01-storage-accounts.md).<br>
  - [Dataset of Azure Blob Storage](sections/01-storage-accounts.md).<br>
  - [Dataset of Azure Data Lake Storage Gen2](sections/01-storage-accounts.md).<br>

[Create Azure Databricks Services](sections/01-storage-accounts.md).<br>
- [Create Cluster](sections/01-storage-accounts.md).<br>
- [Mounting Data Lake Storage](sections/01-storage-accounts.md).<br>

[Building Pipelines Using Azure Data Factory](sections/01-storage-accounts.md).<br>
[Load data into Azure Synapse Analytics](sections/01-storage-accounts.md).<br>
[Import Azure Synapse Data into the Power BI](sections/01-storage-accounts.md).<br>
