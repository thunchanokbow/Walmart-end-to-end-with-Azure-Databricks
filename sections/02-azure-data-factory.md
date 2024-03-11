# Azure Data Factory
Think of Azure Data Factory as a moving service for your data. It can efficiently grab information from different resources, including a data lake. In our case, we will use this tool to extract data from a data lake in **ZIP format** and store it in an Azure Data Lake Storage Gen2 container in **CSV format**. Then, we can use a tool to transform the information into a format that is easier to analyze.

- [Create Azure Data Factory](02-azure-data-factory.md).<br> 
  - [Create Linked Services](02-azure-data-factory.md#Create-Linked-Services).<br>
    - [Source Linked Services](02-azure-data-factory.md#Source-Linked-Services).<br>
    - [Sink Linked Services](02-azure-data-factory.md#Sink-Linked-Services).<br>
    - [Databricks Linked Services](02-azure-data-factory.md#Databricks-Linked-Services).<br> 
  - [Create Dataset](sections/03-azure-databricks.md).<br>
    - [Dataset of Azure Blob Storage](sections/03-azure-databricks.md).<br> 
    - [Dataset of Azure Data Lake Storage Gen2.](sections/03-azure-databricks.md).<br>
  - [Extract data using Azure Data Factory.](sections/03-azure-databricks.md).<br>

### Check that this step has been completed before START:
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

## Create Linked Services
In Linked Services, you can easily **connect** different resources to the **Azure Data Lake Storage Gen2**. In this case, we'll build two kinds of bridges. source bridges **(Source Linked Services)** that bring data from wherever it's stored, and destination bridges **(Sink Linked Services)** that take the data to Azure Data Lake Storage Gen2.  We might also use a Databricks bridge **(Databricks Linked Services)** to connect to Azure Databricks for further processing.

![0](/images/9.png)

### Source Linked Services

![0](/images/10.png)

To create a source linked services, follow these steps:
1. Select the data factory in the **Resource group** to view it. Then select the **Launch Studio** button to continue.
2. Browse to the **Manage tab** in your Azure Data Factory, select **Linked Services**, then click **New**.
3. Search for the **Data source**: `Azure Blob Storage`

![0](/images/11.png)

4. Enter name: `source`
5. Select **Storage account name**: `walmartblobstorage`
6. Test the connection, and create the new linked service.

### Sink Linked Services

![0](/images/12.png)

To create a sink linked services, follow these steps:
1. Browse to the **Manage tab** in your Azure Data Factory, select **Linked Services**, then click **New**.
2. Search for the **Data source**: `Azure Blob Storage`
3. Enter name: `sink`
4. Select **Storage account name**: `walmartazuredatabricks`
5. Test the connection, and create the new linked service.

For more information about create an linked services.[Here](https://learn.microsoft.com/en-us/azure/data-factory/connector-azure-data-lake-storage?tabs=data-factory)

### Databricks Linked Services
![0](/images/13.png)
### Check that this step has been completed before START:
- Create Azure Databricks Services.
- Create Databricks Workspaces.
- Create Clusters.
- Databricks Access Tokens.

To create a databricks linked services, follow these steps:
1. Browse to the **Manage tab** in your Azure Data Factory, select **Linked Services**, then click **New**.
2. Search for the **Data source**: `Azure Databricks` 
3. Enter name: `databricks_walmart`
4. Select **Subscription**.
5. Select **Databricks workspace**: `walmart_sep_2022`
6. **Select Cluster**, click **Existing interactive cluster**.
7. On **Authentication type** click **Access token**.
8. Enter **Access token**.
9. Select **Choose from existing clusters**: `Walmart-Cluster`
