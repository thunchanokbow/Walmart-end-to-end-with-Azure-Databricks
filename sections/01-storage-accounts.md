# Azure Data Lake Storage
Imagine a data lake as a giant digital storage container. It can hold all sorts of information your company collects, from numbers and text to even pictures and videos, all in one place. This makes it easier to find and use the information you need, without having to worry about changing it to fit a specific format. **In our case, the data will be stored in ZIP format**.

- [Create Azure Blob Storage](01-storage-accounts.md#).<br>
- [Create Azure Data Lake Storage Gen2](01-storage-accounts.md#).<br>

### Check that this step has been completed before STAR
- Create Account Azure subscription

![0](/images/02.png)

## Create Azure Blob Storage

![0](/images/02.png)

To create an azure blob storage, follow these steps:
1. On the **Storage accounts page**, select **Create**.
2. On the Basic tab, Select **Subscription**, create new **Resource group**: `walmart`
3. Create **Storage account name**: `walmartblobstorage`
4. Select **Region**: `Southeast Asia`
5. Select **Standard** performance.
6. On the Advanced tab, Select **Allow enabling anonymous access on individual containers**.
7. Select **Enable hierarchical namespace**.
8. Click **Review + create tab** then **Create**.
9. On the **Storage accounts page**, select **walmartblobstorage**.
10. In the left menu for the storage account, select **Storage browser**.
11. Select **Blob Container**.
12. Click **Add container**.
13. Type a name for your new container: `walmart-raw-data`
14. Click **Create**.
15. Click **Upload**.
16. **Browse file** to upload into the blob container: `WMT_Grocery_202209.csv.zip`
17. Select **Upload**.

## Create Azure Data Lake Storage Gen2
Imagine if our data source is stored in a large data lake in **ZIP format**, how can we extract the data as **CSV** to make this information easier to work with and store it in Data Lake Storage Gen2. Then, we can use a tool to transform the information that's easier to analyze. First, we need to create containers.

![0](/images/02.png)

To create an azure data lake storage gen 2, follow these steps:
1. On the **Storage accounts page**, select **Create**.
2. On the Basic tab, Select **Subscription**, select **Resource group**: `walmart`
3. Create **Storage account name**: `walmartazuredatabricks`
4. Select **Region**: `Southeast Asia`
5. Select **Standard** performance.
6. On the Advanced tab, Select **Allow enabling anonymous access on individual containers**.
7. Select **Enable hierarchical namespace**.
8. Click **Review + create tab** then **Create**.
9. On the **Storage accounts page**, select **walmartazuredatabricks**.
10. In the left menu for the storage account, scroll to the **Data storage section**, then select **Containers**.
11. Select the **+ Container**.
12. Type a name for your new container: `raw`
13. Click **Create**.
14. Select the **+ Container**.
15. Type a name for your new container: `transformation` 
13. Click **Create**.
