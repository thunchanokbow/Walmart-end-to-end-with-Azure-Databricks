# Synapse Analytics
Think of Synapse Analytics is a powerful **analytics service that enables you to bring together data integration, warehousing, and big data analytics.** It combines the best features of different technologies to provide valuable insights that can drive decision-making.

- [Create Synapse Analytics workspace](04-synapse-analytics.md#Create-Synapse-Analytics-workspace).<br>
- [Create Lake database](04-synapse-analytics.md#Create-Lake-database).<br>
- [Create Table from data lake](04-synapse-analytics.md#Create-Table-from-data-lake).<br>
- [Query data on Azure Synapse Analytics](04-synapse-analytics.md#Query-data-on-Azure-Synapse-Analytics).<br>

### Check that this step has been completed before START
- Azure Data Lake Stoarge Gen2 with `transformation container`. [Here](01-storage-accounts.md#Create-Azure-Data-Lake-Storage-Gen2)  
  1. product_names_count
  2. top_category 

![0](/images/68.png)

## Create Synapse Analytics workspace

![0](/images/69.png)

To create a synapse analytics workspace, follow these steps:
1. On the **Azure Synapse Analytics page**, select **+Create**.
2. On the **Basics tab**, under **Project Details**, select **Subscription**:`Azure subscription 1`
3. Select **Resource group**:`walmart`

![0](/images/70.png)

4. Under **Workspace details**, select **Worksapce name**:`walmart-synapse-analytics`
5. Select **Region**:`Southeast Asia`
6. Click **Review + create**

For more information about create a synapse analytics workspace.[Here](https://learn.microsoft.com/en-us/azure/synapse-analytics/get-started-create-workspace)

![0](/images/71.png)

## Create Lake database

To create lake database, follow these steps:
1. On the Azure Synapse Analytics **Home page**, select the **Data** tab on the left.
2. Click the **+ button** and select **Lake database**.

![0](/images/72.png)
![0](/images/73.png)

3. The database designer has **Properties** on the right that need to be configured.
- Select **Name**:`WalmartProductDB`
- Select **Linked service**:`walmart-synapse-analytics-WorkspaceDefaultStorage(walmartazuredatabricks)`
- Select **Input folder**:`transformation/WalmartProduc...`

For more information about create lake database.[Here](https://learn.microsoft.com/en-us/azure/synapse-analytics/database-designer/create-empty-lake-database)

## Create Table from data lake

![0](/images/74.png)

To create table from data lake, follow these steps:
1. To add a table to the database, select the **+ Table button**, then select **From data lake**.
2. On the **Create external table from data lake** pane on the right that need to be configured.
- Select **External table name**:`top_category`
- Select **Linked service**:`walmart-synapse-analytics-WorkspaceDefaultStorage(walmartazuredatabricks)`
- Select **Input folder**:`transformation/top_category/part-00000-tid-81....`
- Click **Continue**.
3. On the **New external table page**, under **First row**, click **Infer column names**, then click **Create**.

For more information about create table from data lake.[Here](https://learn.microsoft.com/en-us/azure/synapse-analytics/database-designer/create-empty-lake-database)

![0](/images/75.png)
![0](/images/76.png)

## Query data on Azure Synapse Analytics

To query data on Azure Synapse Analytics, follow these steps:
1. On the **Home page**, select the **Data** tab on the left.
2. Under **Lake database**, select **top_category**, then click **[...]** button.
3. Select **New SQL script**, then click **Select TOP 100 rows**.
4. Select **Use database**:`WalmartProductsDB` from the top-right before running the query.

![0](/images/77.png)
![0](/images/78.png)
![0](/images/79.png)
