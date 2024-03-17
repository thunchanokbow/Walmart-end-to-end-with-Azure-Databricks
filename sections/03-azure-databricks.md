# Azure Databricks
Think of Azure Databricks as a powerful toolbox for working with all your data. It lets you **easily collect, organize, analyze, and share your information** to gain valuable insights. **In our case**, we will use this to **transform data** to find a list of **top categories** for September 2022 for promotion in more visible locations on their website or application, and also identify **top-selling product names within those categories** to contact suppliers for reordering and pricing discussions.

- [Create Azure Databricks Services](sections/03-azure-databricks.md).<br>
- [Create Cluster](sections/03-azure-databricks.md).<br>
- [Mounting Data Lake Storage](sections/03-azure-databricks.md).<br>
- [Using Databricks to transform data](sections/03-azure-databricks.md).<br>


### Check that this step has been completed before START:
- Azure Data Lake Stoarge Gen2.
- PySpark script. [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/Walmart_Sep_2022.ipynb)
- Mounting Python script. [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/mount_storage.py)

## Create Azure Databricks Services

![0](/images/N.png)

To create an azure databricks services, follow these steps:
1. On the **Azure Databricks Service page**, select **+ Create**.
2. On the project details tab, select **Resource Group**:`walmart`
3. Enter **Workspace name**:`walmart_sep_2022`
4. Select **Region**: `Southeast Asia`
5. On **Priceing Tier** click **Standard**. 

For more information about create azure databricks workspace.[Here](https://learn.microsoft.com/en-us/azure/databricks/getting-started/)
