# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. transformation

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "673024e7-58e2-492b-98a1-c86c654b6513", # "<application-id>"
           "fs.azure.account.oauth2.client.secret": "KkR8Q~UxRusKGD-Q6BhMSkfEGq5YLzZJue5BEanH", # "<service-credential>"
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/d5a4b356-132f-4a26-92cf-095f4ca4afc2/oauth2/token"} # "https://login.microsoftonline.com/<directory-id>/oauth2/token"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Please update the following
# MAGIC - raw-container
# MAGIC - storage-account-name

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@walmartazuredatabricks.dfs.core.windows.net/", # "abfss://<raw-container>@<storage-account-name>.dfs.core.windows.net/"
  mount_point = "/mnt/walmartazuredatabricks/raw", # "/mnt/<storage-account-name>/<raw-container>"
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the transformation container
# MAGIC #### Please update the following
# MAGIC - transformation-container
# MAGIC - storage-account-name

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://transformation@walmartazuredatabricks.dfs.core.windows.net/", # "abfss://<transformation-container>@<storage-account-name>.dfs.core.windows.net/"
  mount_point = "/mnt/walmartazuredatabricks/transformation", # "/mnt/<storage-account-name>/<transformation-container>"
  extra_configs = configs)
