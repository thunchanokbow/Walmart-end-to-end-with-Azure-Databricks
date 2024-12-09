# Azure Databricks
Think of Azure Databricks as a powerful toolbox for working with all your data. It lets you **easily collect, organize, analyze, and share your information** to gain valuable insights. **In our case**, we will use this to **transform data** to find a list of **top categories** for September 2022 for promotion in more visible locations on their website or application, and also identify **top-selling product names within those categories** to contact suppliers for reordering and pricing discussions.

- [Create Azure Databricks Services](03-azure-databricks.md#Create-Azure-Databricks-Services).<br>
- [Create Cluster](03-azure-databricks.md#Create-Cluster).<br>  
- [Mounting Data Lake Storage](03-azure-databricks.md#Mounting-Data-Lake-Storage).<br>  
- [Using Databricks to transform data](03-azure-databricks.md#Using-Databricks-to-transform-data).<br> 
- [Run Databricks Notebook using Azure Data Factory](03-azure-databricks.md#Run-Databricks-Notebook-using-Azure-Data-Factory).<br>
  - [Generate Access tokens](03-azure-databricks.md#Generate-Access-tokens).<br>  
  - [Run Databricks Notebook Activity](03-azure-databricks.md#Run-Databricks-Notebook-Activity).
    
### Check that this step has been completed before START
- Azure Data Lake Stoarge Gen2 Containers. [Here](01-storage-accounts.md#Create-Azure-Data-Lake-Storage-Gen2)
  1. raw.
  2. transformation. 
- Mounting storage Python script. [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/mount_storage.py)
- PySpark script. [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/Walmart_Sep_2022.ipynb)
- Databricks Linked Services. [Here](02-azure-data-factory.md#Databricks-Linked-Services)

## Create Azure Databricks Services

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

![0](/images/28.png)

To **connect** to external storage (**Azure Data Lake Storage Gen2**) in **Databricks** using a Python script, you'll need to **create a registered application in Microsoft Entra ID** with a unique identifier (**Application ID**), another identifier for your organization (**Directory ID**), and a secret key (**Service Credential**) This information is created in **Microsoft Azure**. Finally, you'll **grant access** to the storage (**Azure Data Lake Storage Gen2**) for this application **Access Control (IAM)**.

### Create App Registrations

![0](/images/29.png)

To create an app registrations, follow these steps:
1. Search for the **Microsoft Entra ID** in Microsoft Azure.
2. Browse to the **App Registrations**, then click **+ Add**.
3. Enter **Name**: `Walmart-App`
4. Click **Register**.
5. On the Walmart-App page, Copy **Application (Client) ID** and **Directory (Client) ID**.

### Add Cretificates & secrets

![0](/images/30.png)

To add cretificates and secrets, follow these steps:
1. On the App Registrations page, select **Walmart-App**.
2. Browse to the **Cretificates & secrets**.
3. Click **+ New client secret**.
4. Enter **Description**: `secret_created`
5. Select **Expires**: `180 days (6 months)`
6. Click **Add**.
7. On the **Client Secrets** tab, Copy **Value**. 

![0](/images/31.png)

For more information about register an application.[Here](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

### Grant Access to the storage ( Access Control (IAM) )

![0](/images/33.png)

To grant access to the storage, follow these steps:
1. Search for the **Storage Account** in Microsoft Azure.
2. Select **walmartazuredatabricks**.
3. Browse to the **Access Control (IAM)**, click **Add role assignment** button to continue.

![0](/images/34.png)

4. On **Job function role** tab, search for the **container**: `Storage Blob Data Contrib...`, then **Next**.
5. On the **Members** tab, click **+ Select members**.

![0](/images/35.png)

6. On the **Select Members** page, search for `Walmart-App`, click **Select**
7. Click **Review + assign** then **Create**.   

For more information about assign azure roles.[Here](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal?tabs=delegate-condition)


### Mounting storage
We need to create a folder to store the mount storage [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/mount_storage.py). Then, we can **connect Databricks to Azure Data Lake Storage Gen2** by running the `mount storage.py` script. <br>

![0](/images/43.png)

Mount the following Azure Data Lake Storage Gen2 containers. <br>
1. **raw**
2. **transformation**


Set up the configs. Make sure you have the following information: 
- **Application ID**.
- **Directory ID**.
- **Service Credential**.

```
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "<application-id>"
           "fs.azure.account.oauth2.client.secret": "<service-credential>"
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}  

```

Mount the raw container. Please update the following:
- **raw-container**.
- **storage-account-name**.

```
dbutils.fs.mount(
  source = "abfss://<raw-container>@<storage-account-name>.dfs.core.windows.net/", 
  mount_point = "/mnt/<storage-account-name>/<raw-container>", 
  extra_configs = configs)
```

Mount the transformation container. Please update the following:
- **transformation-container**.
- **storage-account-name**.

```
dbutils.fs.mount(
  source = "abfss://<transformation-container>@<storage-account-name>.dfs.core.windows.net/", 
  mount_point = "/mnt/<storage-account-name>/<transformation-container>", 
  extra_configs = configs)
```

For more information about mounting cloud object storage on azure databricks.[Here](https://learn.microsoft.com/en-us/azure/databricks/dbfs/mounts)<br>

![0](/images/36.png)
 
To create new folders in databricks, follow these steps:
1. On the **Azure Databricks Service page**, select **walmart_sep_2022**.
2. Click **Launch Workspace** button to continue.
3. Browse to **Workspace** in the Databricks, click **Add**, then select **Folder**.
4. Enter **New folder**: `set-up`
5. **Import** file `mount storage.py`

![0](/images/37.png)

6. Click **mount storage.py**.
7. Browse to **Databricks Cluster**, then select **Walmart-Cluster**.
8. Click **Run-All**. 

## Using Databricks to transform data
First, we need to create a folder to store the pyspark script [file](https://github.com/thunchanokbow/Walmart-end-to-end-with-Azure-Databricks/blob/main/Walmart_Sep_2022.ipynb). Than, we can run the Databricks notebook to **transform data** by running the `Walmart_Sep_2022.ipynb` and gain the insights.

![0](/images/38.png)

To using databricks to transform data, follow these steps:
1. Browse to **Workspace** in the Databricks, click **Add**, then select **Folder**.
2. Enter **New folder**: `transform`
3. **Import** file `Walmart_Sep_2022.ipynb`
4. Click **Walmart_Sep_2022.ipynb**.

## Run Databricks Notebook using Azure Data Factory

### Generate Access tokens
Access tokens act as **secure keys** that allow Azure Data Factory to **connect with Databricks Notebooks**. This connection makes it possible to build efficient pipelines that handle large amounts of data, all without needing to show usernames and passwords, keeping everything safe.

![0](/images/40.png)

To generate new access tokens on databricks, follow these steps:
1. Browse to **User Setting** in the Databricks.
2. On the **Settings** page, browse to **Developer**.
3. On the **Access tokens** tab, click **Generate new token**.
4. Click copy **Your Token**.

![0](/images/39.png)

### Run Databricks Notebook Activity

![0](/images/42.png)

To run databricks notebook activity, follow these steps:
1. Browse to the **Author tab** in your Azure Data Factory, and select the **pipelines**, to choose **New Pipeline**.
2. On the **Activities** tab, select **Databricks**, drag the **Notebook** activity.
3. In **Properties**, enter **Name**: `databricks_transform_walmart`

![0](/images/41.png)

4. On the **General tab**, enter **Name**: `databricks_walmart_transform`
5. In the **Azure Databricks**, set up the **Datacbricks Linked Services**. [Here](02-azure-data-factory.md#Databricks-Linked-Services)
6. On the **Authentication type**, select **Access token**, then enter **Your Token**.

![0](/images/13.png)

7. Click **Create**.
8. On the **Settings** tab, click **Browse** to **PySpark script**: `Walmart_Sep_2022.ipynb`
9. Click **Validate**, click **Trigger Now**.
10. To check status, click **Details Output**.

For more information about run databricks notebook activity.[Here](https://learn.microsoft.com/en-us/azure/data-factory/transform-data-using-databricks-notebook)
