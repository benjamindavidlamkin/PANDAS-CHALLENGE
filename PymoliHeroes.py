#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[10]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "../Resources/Pandas_pymoli.csv"

# Read Purchasing File and store into Pandas data frame
player_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[11]:


#Total Number of Players
total_nerds = len(player_data["SN"].value_counts())


#Dataframe with Nerd Count
nerd_count = pd.DataFrame({"Total Nerds":[total_nerds]})
nerd_count


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[12]:


#Calculations for Unique IDs, average price, #of purchases, gross revenue

number_of_unique_items = len((player_data["Item ID"]).unique())
average_price = (player_data["Price"]).mean()
number_of_purchases = (player_data["Purchase ID"]).count()
gross_revenue = (player_data["Price"]).sum()

#Data frame with new values

summary_df = pd.DataFrame({"Number of Unique Items":[number_of_unique_items],
                           "Average Price":[average_price], 
                           "Number of Purchases": [number_of_purchases], 
                           "Gross Revenue": [gross_revenue]})
#Format
summary_df.style.format({'Average Price':"${:,.2f}",
                         'Gross Revenue': '${:,.2f}'})


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[20]:


#Group by Gender
gender_demo = player_data.groupby("Gender")

#Count Screen name by gender
total_count_gender = gender_demo.nunique()["SN"]

#Gender Percentage
percentage_of_players = total_count_gender / total_nerds * 100

#Gender Data frame
gender_demographics = pd.DataFrame({"Percentage of Players": percentage_of_players, "Total Count": total_count_gender})

#Leave the Top left Corner open for alignment
gender_demographics.index.name = None

#Sort Gender by % Descending
gender_demographics.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[21]:


# Total purchases by gender 
purchase_count = gender_demo["Purchase ID"].count()

# Average purchase price by gender
avg_purchase_price = gender_demo["Price"].mean()

# Average total purchased by gender 
avg_purchase_total = gender_demo["Price"].sum()

# Average purchase total by gender divivded by purchase count by unique shoppers
avg_purchase_per_person = avg_purchase_total/total_count_gender

# Create data frame with obtained values 
gender_demographics = pd.DataFrame({"Purchase Count": purchase_count, 
                                    "Average Purchase Price": avg_purchase_price,
                                    "Average Purchase Value":avg_purchase_total,
                                    "Avg Purchase Total per Person": avg_purchase_per_person})

# Provide index in top left as "Gender"
gender_demographics.index.name = "Gender"

# Format with currency style 2 decimal places
gender_demographics.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                  "Avg Purchase Total per Person":"${:,.2f}"})


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[24]:


# Bin for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Sorted and cut age values into the bins established above
player_data["Age Group"] = pd.cut(player_data["Age"],age_bins, labels=group_names)
player_data

# Create new data frame with the added "Age Group" and group it
age_grouped = player_data.groupby("Age Group")

# Count total players by age category
total_count_age = age_grouped["SN"].nunique()

# Calculate percentages by age category 
percentage_by_age = (total_count_age/total_nerds) * 100

# Create data frame with obtained values
age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})

# Format the data frame with no index name in the corner
age_demographics.index.name = None

# Format percentage with two decimal places 
age_demographics.style.format({"Percentage of Players":"{:,.2f}"})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[25]:


# Count purchases by age group
purchase_count_age = age_grouped["Purchase ID"].count()

# Obtain average purchase price by age group 
avg_purchase_price_age = age_grouped["Price"].mean()

# Calculate total purchase value by age group 
total_purchase_value = age_grouped["Price"].sum()

# Calculate the average purchase per person in the age group 
avg_purchase_per_person_age = total_purchase_value/total_count_age

# Create data frame with obtained values
age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})

# Format the data frame with no index name in the corner
age_demographics.index.name = None

# Format with currency style
age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[27]:



# Group purchase data by screen names
nerd_stats = player_data.groupby("SN")

# Count the total purchases by name
purchase_count_spender = nerd_stats["Purchase ID"].count()

# Calculate the average purchase by name 
avg_purchase_price_spender = nerd_stats["Price"].mean()

# Calculate purchase total 
purchase_total_spender = nerd_stats["Price"].sum()

# Create a data frame with above values
top_nerds = pd.DataFrame({"Purchase Count": purchase_count_spender,
                             "Average Purchase Price": avg_purchase_price_spender,
                             "Total Purchase Value":purchase_total_spender})

# Sort in descending order to obtain top 5 nerd names 
formatted_spenders = top_nerds.sort_values(["Total Purchase Value"], ascending=False).head()

# Format with currency style
formatted_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                 "Average Purchase Price":"${:,.2f}", 
                                 "Total Purchase Value":"${:,.2f}"})


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[31]:


# Create new data frame with widgets related information 
widgets = player_data[["Item ID", "Item Name", "Price"]]

# Group the widget data by widget id and name 
widget_stats = widgets.groupby(["Item ID","Item Name"])

# Count the number of times a widget has been purchased 
purchase_count_item = widget_stats["Price"].count()

# Calcualte the purchase value per widget 
purchase_value = (widget_stats["Price"].sum()) 

# Find individual widget price
widget_price = purchase_value/purchase_count_item

# Create data frame with obtained values
most_popular_widgets = pd.DataFrame({"Widget Count": purchase_count_item, 
                                   "Widget Price": widget_price,
                                   "Total Purchase Value":purchase_value})

# Sort in descending order to obtain top nerd names and provide top 5 item names
popular_formatted = most_popular_widgets.sort_values(["Widget Count"], ascending=False).head()

# Format with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[36]:


# Sorted widgets by highest Purchase Value
popular_formatted = most_popular_widgets.sort_values(["Total Purchase Value"],
                                                   ascending=False).head()
# Format with currency style
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# In[ ]:




