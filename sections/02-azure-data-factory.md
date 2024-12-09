# Azure Data Factory
Think of Azure Data Factory as a moving service for your data. It can efficiently grab information from different resources, including a data lake. In our case, we will use this tool to extract data from a data lake in **ZIP format** and store it in an Azure Data Lake Storage Gen2 container in **CSV format**. Then, we can use a tool to transform the information into a format that is easier to analyze.

- [Create Azure Data Factory](02-azure-data-factory.md#Create-Azure-Data-Factory).<br> 
  - [Create Linked Services](02-azure-data-factory.md#Create-Linked-Services).<br>
    - [Source Linked Services](02-azure-data-factory.md#Source-Linked-Services).<br>
    - [Sink Linked Services](02-azure-data-factory.md#Sink-Linked-Services).<br>
    - [Databricks Linked Services](02-azure-data-factory.md#Databricks-Linked-Services).<br> 
  - [Create Dataset](02-azure-data-factory.md#Create-Dataset).<br> 
    - [Dataset of Azure Blob Storage](02-azure-data-factory.md#Dataset-of-Azure-Blob-Storage).<br>  
    - [Dataset of Azure Data Lake Storage Gen2](02-azure-data-factory.md#Dataset-of-Azure-Data-Lake-Storage-Gen2).<br> 
  - [Extract data using Azure Data Factory.](02-azure-data-factory.md#Extract-data-using-Azure-Data-Factory).<br> 

### Check that this step has been completed before START
- Create Account Azure subscription.
- Create Storage Accounts (Azure Data Lake Storage Gen2).

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
2. Browse to the **Manage tab** in your Azure Data Factory, select **Linked Services**, then click **+ New**.
3. Search for the **Data source**: `Azure Blob Storage`

![0](/images/11.png)

4. Enter name: `source`
5. Select **Storage account name**: `walmartblobstorage`
6. Test the connection, and create the new linked service.

### Sink Linked Services

![0](/images/12.png)

To create a sink linked services, follow these steps:
1. Browse to the **Manage tab** in your Azure Data Factory, select **Linked Services**, then click **+ New**.
2. Search for the **Data source**: `Azure Data Lake Storage Gen2`
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
- Databricks Access Tokens. [Here](03-azure-databricks.md#Run-Databricks-Notebook-using-Azure-Data-Factory)

To create a databricks linked services, follow these steps:
1. Browse to the **Manage tab** in your Azure Data Factory, select **Linked Services**, then click **+ New**.
2. Search for the **Data source**: `Azure Databricks` 
3. Enter name: `databricks_walmart`
4. Select **Subscription**.
5. Select **Databricks workspace**: `walmart_sep_2022`
6. **Select Cluster**, click **Existing interactive cluster**.
7. On **Authentication type** click **Access token**. [Here](03-azure-databricks.md#Generate-Access-tokens)
8. Enter **Access token**.
9. Select **Choose from existing clusters**: `Walmart-Cluster`

## Create Dataset
Think of it this way the dataset represents the structure of the data. This dataset acts as a **key** (or **reference**) that lets you easily find all the data you need, even though it's stored in different locations and formats. In this case, we will create datasets for the data source in ZIP format (**Azure Blob Storage**) and the data storage in CSV format (**Azure Data Lake Storage Gen2**).

![0](/images/14.png)

### Dataset of Azure Blob Storage

![0](/images/15.png)

To create a dataset of azure blob storage, follow these steps:
1. Browse to the **Author tab** in your Azure Data Factory, and select the plus **+**, to choose **Dataset**.
2. Search for the **Data source**: `Azure Blob Storage`

![0](/images/16.png)

3. Choose **the format**: `DelimitedText`
4. Enter name: `walmart_data`
5. Select **Linked service**: `source`

![0](/images/17.png)

6. On **File path**, click **Browse** to the data source in **ZIP format**: `WMT_Grocery_202209.csv.zip`
7. On **Import schema**, click **None**.
8. Click **OK**.

![0](/images/18.png)

9. On the **Connection tab**, Select **Compression type**: `ZipDeflate(.zip)`
10. Select **Compression level**: `Optimal`
    
### Dataset of Azure Data Lake Storage Gen2

![0](/images/19.png)

To create a dataset of azure data lake storage gen2, follow these steps:
1. Browse to the **Author tab** in your Azure Data Factory, and select the plus **+**, to choose **Dataset**.
2. Search for the **Data source**: `Azure Data Lake Storage Gen2`
3. Choose **the format**: `DelimitedText`
4. Enter name: `walmart_gen2`
5. Select **Linked service**: `sink`
6. Enter **File path**: `WMT_Grocery_202209.csv`
7. On **Import schema**, click **None**.
8. Click **OK**.

![0](/images/20.png)

9. On the **Connection tab**, enter the file path **Add new container** as: `raw`<br>
You should have the file path similar to this example. <br>
**File path:** `raw/<no-directory>/WMT_Grocery_202209.csv` <br>
10. Select **Compression type**: `Comma(,)`
11. Select **Compression level**: `Optimal`
12. Click **Publishing**.

For more information about create datasets.[Here](https://learn.microsoft.com/en-us/azure/data-factory/concepts-datasets-linked-services?tabs=data-factory)

## Extract data using Azure Data Factory

![0](/images/21.png)

Extract data using the copy activity **(Azure Data Factory)**. The **Copy activity** lets you move files directly between different storage locations, like copying documents from one folder to another on your computer. It's a quick way to transfer information without needing any special tools.<br>

![0](/images/22.png)

To extract data using azure data factory, follow these steps:
1. Browse to the **Author tab** in your Azure Data Factory, and select the **pipelines**, to choose **New Pipeline**.
2. On the **Properties**, enter **Name**: `data-integration`
3. On the **General tab**, enter **Name**: `copy_walmart_data`

![0](/images/23.png)

4. On the **Source tab**, choose **Source dataset**: `walmart_data`
5. Select **File path in dataset**.
6. On the **Sink tab**, choose **Sink dataset**:`walmart_gen2`

![0](/images/24.png)

7. Click **Validate** then **Debug**.
8. To check status, click **Output tab**. 

For more information about copy data using copy activity.[Here](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-overview)
