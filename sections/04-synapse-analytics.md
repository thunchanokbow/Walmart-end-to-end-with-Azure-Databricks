# Synapse Analytics
Think of Synapse Analytics is a powerful **tool that helps businesses analyze large amounts of data** quickly and efficiently. It combines the best features of different technologies to provide valuable insights that can drive decision-making.

- [Create Synapse Analytics workspace](sections/04-synapse-analytics.md).<br>
- [Create Lake database](sections/04-synapse-analytics.md).<br>
- [Create Table from data lake](sections/04-synapse-analytics.md).<br>
- [Query data on Azure Synapse Analytics](sections/04-synapse-analytics.md).<br>

### Check that this step has been completed before START:

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

