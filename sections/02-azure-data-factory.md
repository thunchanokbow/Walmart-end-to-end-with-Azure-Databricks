# Azure Data Factory
Think of Azure Data Factory as a moving service for your data. It can efficiently grab information from different resources, including a data lake. In our case, we will use this tool to extract data from a data lake in **ZIP format** and store it in an Azure Data Lake Storage Gen2 container in **CSV format**. Then, we can use a tool to transform the information into a format that is easier to analyze.

- [Create Azure Data Factory](02-azure-data-factory.md).<br> 
  - [Create Linked Services](02-azure-data-factory.md#Create-Azure-Data-Lake-Storage-Gen2).<br>
    - [Source Linked Services](02-azure-data-factory.md#Create-Azure-Data-Lake-Storage-Gen2).<br>
    - [Sink Linked Services](02-azure-data-factory.md#Create-Azure-Data-Lake-Storage-Gen2).<br>
    - [Databricks Linked Services](02-azure-data-factory.md#Create-Azure-Data-Lake-Storage-Gen2).<br>
  - [Create Dataset](02-azure-data-factory.md).<br>
    - [Dataset of Azure Blob Storage](02-azure-data-factory.md).<br>  
    - [Dataset of Azure Data Lake Storage Gen2.](02-azure-data-factory.md).<br>
  - [Extract data using Azure Data Factory.](02-azure-data-factory.md).<br> 

### Check that this step has been completed before START
- Create Account Azure subscription.
- Create Azure Data Lake Storage Gen2.

![0](/images/7.png)

## Create Azure Data Factory

![0](/images/8.png)

To create an azure data factory, follow these steps:
1. On the **Data factories page**, select **Create**.
2. On the Basic tab, Select **Subscription**, select **Resource group**: `walmart`
3. Enter name: `walmartazuredatabricksinstance`
4. Select **Region**: `Southeast Asia`
5. Click **Review + create tab** then **Create**.

For more information about create an azure data factory.[Here](https://learn.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory)   
