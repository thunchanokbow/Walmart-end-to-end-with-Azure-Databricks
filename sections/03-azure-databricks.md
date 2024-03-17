# Azure Databricks
Think of Azure Databricks as a powerful toolbox for working with all your data. It lets you **easily collect, organize, analyze, and share your information** to gain valuable insights. **In our case**, we will use this to **transform data** to find a list of **top categories** for September 2022 for promotion in more visible locations on their website or application, and also identify **top-selling product names within those categories** to contact suppliers for reordering and pricing discussions.

- [Create Azure Databricks Services](03-azure-databricks.md).<br>
- [Create Cluster](03-azure-databricks.md#Create-Cluster).<br>  
- [Mounting Data Lake Storage](04-synapse-analytics.md).<br>  
- [Using Databricks to transform data](04-synapse-analytics.md).<br>


### Check that this step has been completed before START:
- Azure Data Lake Stoarge Gen2.
- PySpark script. [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/Walmart_Sep_2022.ipynb)
- Mounting Python script. [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/mount_storage.py)

## Create Azure Databricks Service

![0](/images/25.png)

To create an azure databricks services, follow these steps:
1. On the **Azure Databricks Service page**, select **+ Create**.
2. On the project details tab, select **Resource Group**:`walmart`
3. Enter **Workspace name**:`walmart_sep_2022`
4. Select **Region**: `Southeast Asia`
5. On **Priceing Tier** choose **Standard**. 

For more information about create azure databricks workspace.[Here](https://learn.microsoft.com/en-us/azure/databricks/getting-started/)

## Create Cluster

![0](/images/26.png)

To create cluster, follow these steps:
1. On the **Azure Databricks Service page**, select **walmart_sep_2022**.
2. Click **Launch Workspace** button to continue.
3. Browse to **+ New** in the Databricks, select **Cluster**.

![0](/images/27.png)

4. Enter **Name**:`Walmart-Cluster`
5. Click **Single node**.
6. On **Databricks runtime version**, select: `2.2 LTS`
7. **Uneble** on Use Photon Acceleration.
8. On **Node Type**, select: `Standard_DS3_v2  14GB, 4 cores`
9. On **Terminate after**, enter: `20`.

For more information about create cluster.[Here](https://learn.microsoft.com/en-us/azure/databricks/compute/configure)

## Mounting Data Lake Storage

![0](/images/N.png)

To **connect** to external storage (**Azure Data Lake Storage Gen2**) in **Databricks** using a Python script, you'll need to **create a registered application in Microsoft Entra ID** with  
a unique identifier (**Application ID**), another identifier for your organization (**Directory ID**), and a secret key (**Service Credential**) This information is created in **Microsoft Azure**. Finally, you'll **grant access** to the storage (**Azure Data Lake Storage Gen2**) for this application **Access Control (IAM)**.

### Create App Registrations

To create an app registrations, follow these steps:
1. Search for the **Microsoft Entra ID** in Microsoft Azure.
2. Browse to the **App Registrations**, then click **+ Add**.
3. Enter **Name**: `Walmart-App`
4. Click **Register**.
5. On the Walmart-App page, Copy **Application (Client) ID** and **Directory (Client) ID**.

![0](/images/N.png)

### Add Cretificates & secrets

To add cretificates and secrets, follow these steps:
1. On the App Registrations page, select **Walmart-App**.
2. Browse to the **Cretificates & secrets**.
3. Click **+ New client secret**.
4. Enter **Description**: `secret_created`
5. Select **Expires**: `180 days (6 months)`
6. Click **Add**.
7. On the **Client Secrets** tab, Copy **Value**. 
      

### Grant Access to the storage ( Access Control (IAM) )
To grant access to the storage, follow these steps:
1. Search for the **Azure Data Lake Storage Gen2** in Microsoft Azure.
2. 
