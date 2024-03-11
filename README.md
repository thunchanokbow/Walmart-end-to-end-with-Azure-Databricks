# Walmart-end-to-end-with-Azure-Databricks
The data is extracted in batches using Azure Data Factory and transformed using Spark in Azure Databricks. The transformed data is stored in Synapse Analytics in columnar format. Finally, a dashboard is created using Looker Studio or Power BI, As a result of my project, fresh food has become their top category! This will help with the decision to promote fresh food by placing them in more visible locations and on the website or application. Their most popular fresh food is MorningStar Farms Veggie Burgers, with customers picking up a total of 184 units daily. With this information, the company is able to contact MorningStar Farm's to order more products and discuss pricing options. For more information about data source.[Here](https://www.kaggle.com/datasets/thedevastator/product-prices-and-sizes-from-walmart-grocery) 
## Project Overview
![0](/images/0.png)

## Contents 
[Create Storage Account](sections/01-storage-accounts.md).<br> 
- [Azure Blob Storage](sections/01-storage-accounts.md).<br>
- [Azure Data Lake Storage Gen2](sections/01-storage-accounts.md#Create-Azure-Data-Lake-Storage-Gen2).<br>

[Create Azure Data Factory](sections/02-azure-data-factory.md).<br>
- [Create Linked Services](sections/02-azure-data-factory.md).<br>
  - [Source Linked Services](sections/02-azure-data-factory.md).<br>
  - [Sink Linked Services](sections/02-azure-data-factory.md).<br>
  - [Databricks Linked Services](sections/02-azure-data-factory.md).<br>

- [Create Dataset](sections/02-azure-data-factory.md).<br>
  - [Dataset of Azure Blob Storage](sections/02-azure-data-factory.md).<br>
  - [Dataset of Azure Data Lake Storage Gen2](sections/02-azure-data-factory.md).<br>
- [Extract data using Azure Data Factory](sections/02-azure-data-factory.md).<br>

[Create Azure Databricks Services](sections/02-azure-data-factory.md).<br>
- [Create Cluster](sections/02-azure-data-factory.md).<br>
- [Mounting Data Lake Storage](sections/02-azure-data-factory.md).<br>
- [Using Databricks to transform data](sections/02-azure-data-factory.md).<br>


[Building Pipelines Using Azure Data Factory](sections/02-azure-data-factory.md).<br>
[Create Synapse Analytics workspace](sections/02-azure-data-factory.md).<br>
- [Create Lake database](sections/02-azure-data-factory.md).<br>
- [Create Table from data lake](sections/02-azure-data-factory.md).<br>
- [Load data into Azure Synapse Analytics](sections/02-azure-data-factory.md).<br>

[Import Azure Synapse Analytics (SQL DW) Data into the Power BI](sections/02-azure-data-factory.md).<br>
- [Connect to a data source in Power BI](sections/02-azure-data-factory.md).<br>
- [Creating Data visualizations](sections/02-azure-data-factory.md).<br>
