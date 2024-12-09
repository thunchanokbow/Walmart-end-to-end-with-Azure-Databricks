# Import Azure Synapse Analytics (SQL DW) Data into the Power BI
Power BI is your go to smart analytics tool that will not only keep your data secure but give you insights using **data visualization**.

- [Connect to a data source in Power BI](05-power-bi.md#Connect-to-a-data-source-in-Power-BI).<br>
- [Creating Data visualizations](05-power-bi.md#Creating-Data-visualizations).<br>

### Check that this step has been completed before STAR
- Sign in Power BI Pro or Premium.
- Create workspaces on Power BI Service. [Here](https://github.com/thunchanokbow/Real-time-data-in-Power-BI/blob/main/sections/02-Create-A-Workspace.md)
- The Server for Synapse Analytics. [Here](https://www.youtube.com/watch?v=ldN6D2lhNyA)
  1. To find the **Server** go to **Synapse workspace**.
  2. On the **Overview** page, copy **SQL on-demand endpoint**.  
- Data Credential.

![0](/images/70.png)

## Connect to a data source in Power BI

To connect to a data source in Power BI, follow these steps:
1. In Power BI Desktop, click the **Get Data** button.
2. Select **Azure SQL database** from the list of data sources.
3. In the **SQL Server database** dialog box, enter the **Server** and **Database** (optional) names.
4. Select **DirectQuery** as the Data connectivity mode.
5. Click **OK**.

For more information about connect to a data source in Power BI. [Here](https://github.com/thunchanokbow/Real-time-data-in-Power-BI/blob/main/sections/04-Pulling-data-to-Power-BI.md)

## Creating Data visualizations

- Businesses Requirements
  1. The Marketing team needs a list of top categories in the month of September 2022. So that they can promote by placing them in more visible locations and on the website or application.
  2. The Product team requires a list of top-selling product names within the top categories. So that they can contact the suppliers to order more products and discuss pricing options.

![0](/images/80.png)
![0](/images/81.png)
