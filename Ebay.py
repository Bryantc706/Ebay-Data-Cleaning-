#!/usr/bin/env python
# coding: utf-8

# In[267]:


# we need to import pandas in order to make it possible to do data wrangling 
import pandas as pd 


# In[268]:


# I have to upload the CSV's so it is possible to do the data wranging. I began with the eday_df file so I can edit that before I would move on onto the ebayprice_df file where it only had just the price variables for it. 
ebay_df = pd.read_csv('EbayPcLaptopDataUnclean.csv')

ebayprice_df = pd.read_csv('EbayPcLaptopPriceData.csv')


# In[269]:


# I wanted to check out the csv on python to see how much data we are looking at while looking at how many variables that I am working with. 
ebay_df


# In[270]:


# This looks at the first couple of rows and I wanted to explore what it looked like for the first five rows. 
ebay_df.head()


# In[271]:


# I wanted to see the first 35 rows to explore what was in the ebay data and what I would to examine in this case. 
ebay_df.iloc[1:35]


# In[272]:


# With this type of code it gives what are the data types for this and it gave me an idea of what types are in each column so when  Iwork in that particular column I know what type of data it is that I am working with. 
ebay_df.info()


# In[273]:


# In this case for python, this type of code checks foor missing or null values that are in the ebay_df dataframe and it tells me how much missing data that I am working with for each column.
ebay_df.isnull().sum()


# In[274]:


# I used this in this case since it gives me a summay of the data for both its categorical and numeric columns. It also helps identify potential issues such as missing values which we do have in this case for our data. 
ebay_df.describe(include='all')


# In[275]:


# I had to use this code as this checks if there is missing data or NA which in this case it would be true, but if it is false then it would show that there is not missing data in the dataFrame. This helped me identify missing values that is across this particular dataFrame.   
ebay_df.isna()


# In[276]:


# In this case, I wanted to see the percentage of each column to see how much of the column has dropped data. In this case the higher the number the more missing data there is so for example like rating it is 95.6 which means that 95.6 of the data in this case is missing where as something like brand is 38.6 which means that 38.6 percent of the column in the dataFrame is missing. This gave me a good idea of what columns I wanted to drop in this case. 
ebay_df.isna().sum() / len(ebay_df) * 100


# In[277]:


# From what was shown above, I wanted to get rid of columns that had a high percentage of missing data, for this problem, I wanted to get rid of data that demostrated over 0.85 or more than 85 percent of the data missing so in this case it ended up being 'Rating','Ratings Count','Country Region Of Manufacture','Manufacturer Color', and 'Release Year'. These variables are shown to have data that is more than 85 percent so I wanted to get rid of them. 
ebay_df_sample = ebay_df.drop(columns=['Rating','Ratings Count','Country Region Of Manufacture','Manufacturer Color','Release Year'])
ebay_df_sample.head()


# In[278]:


# I wanted to drop all of the missing values in this case, however it only included any values that are non-null. By doing this, the amount of rows decreased from 6,676 rows to 210 and it decrease the amount of columns from 23 to 18 columns.  
ebay_df_sample = ebay_df_sample.dropna()

ebay_df_sample


# In[279]:


# I wanted to explore the different models that were apart of the dataset so in this case, this code shows what different types that appear on my dataFrame. I also sorted it so it makes it easier for me to read the different models that are on the dataFrame. 
Model_unique_values = ebay_df_sample['Model'].unique()
Model_unique_values.sort()
Model_unique_values


# In[280]:


# I looked into the models and I explored what types of models that are foreign or did not make sense, so I used AI (ChatGBT) and I ask what are models that are foreign or did not exist and I removed the models that AI considered were not real models. 
bad_items = ['14', '5410','5580', 'C731T-C0X8','E540', 'i5-4300Y', '82R', 'i5 4200M','Dell']
for item in bad_items:
    ebay_df_sample = ebay_df_sample[ebay_df_sample['Model'] != item]



# In[281]:


# This data shows the models without the foreign models. 
ebay_df_sample['Model'].unique()



# In[282]:


# In this case I used AI to look at models that were wrong and what the type of model it really is. From using AI and research on the world wide web, I was able to find which ones in the array that needed to be replaced. So in this case I replaced in and used the ebay_df_sample['Model'].unique() above to replace the data that was seen before. 
ebay_df_sample['Model'].replace (to_replace=['ELITEBOOK 745 G6'], value='HP Elitebook 745 G6', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Chromebook 11 G6 EE'], value=' HP ChromeBook 11 G6 EE', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Latitude 5430 Rugged'], value=' Dell Latitude 5430 Rugged', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Latitude 7230 Rugged Extreme Tablet'], value='Dell Latitude 7230 Rugged Extreme Tablet', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Chromebook C738T-C44Z'], value='Acer Chromebook R 11 C738T-C44Z', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Precision 7680'], value='Dell Precision 7680 Workstation', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Chromebook 11 G6 EE (3NU57UT#ABA)'], value='HP Chromebook 11A G6 EE', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Libreboot T440p'], value='Lenovo Thinkpad T440p Ultrabook High Performance', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['ThinkPad 11e Chromebook'], value='Lenovo ThinkPad 11e Chromebook', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['T490'], value='Lenovo ThinkPad T490', inplace=True)
ebay_df_sample['Model'].replace (to_replace=['Latitude E5470'], value='Dell Latitude E5470', inplace=True)


# In[283]:


# I loaded the sample to see if it worked on the dataframe and see the edits I made worked on it. 
ebay_df_sample


# In[284]:


# Next I  wanted to replace tje processor speed since there were a lot of mistakes when I uploaded the array and sorted it like I did with the model. In this case there was labels missing or the label was spelt not correctly. The only thing I left was the one that did not have a space as it was something I did not care about and it did not affect the data. In other words it was inconsequential on affecting the data. 
Model_unique_values1 = ebay_df_sample['Processor Speed'].unique()
Model_unique_values1.sort()
Model_unique_values1


# In[285]:


# Like I did before with the model, I replace the ones that did not have a label or there was an error with the label. I performed it above with the Model_unique_values1 above to see if there are any changes with the array. (Warning do not run Model_unique_values1 by itself just the code that is above!) 
ebay_df_sample['Processor Speed'].replace (to_replace=['2.3'], value='2.3Ghz', inplace=True)
ebay_df_sample['Processor Speed'].replace (to_replace=['3.10 GHz (2.50 GHz Base Frequnecy)'], value='3.1hz', inplace=True)
ebay_df_sample['Processor Speed'].replace (to_replace=['3.60 GHz (1.70 GHz Base Frequency)'], value='3.6hz', inplace=True)
ebay_df_sample['Processor Speed'].replace (to_replace=['Max Turbo Frequency @ 3.90 GHz'], value='3.9hz', inplace=True)
ebay_df_sample['Processor Speed'].replace (to_replace=['2.4'], value='2.4Ghz', inplace=True)
ebay_df_sample['Processor Speed'].replace (to_replace=['2.8GHz-3.8GHz'], value='2.8Ghz', inplace=True)
ebay_df_sample['Processor Speed'].replace (to_replace=['4.90 GHz (1.80 GHz Base Frequency)'], value='4.9Ghz', inplace=True)





# In[286]:


# There were a lot of mistakes with the OS as there was some OS that had spelling mistakes or something that may not made sense to it. 
Model_unique_values2 = ebay_df_sample['OS'].unique()
Model_unique_values2.sort()
Model_unique_values2


# In[287]:


# Like what I did before I did the same process as the model and processor speed and I ran it through Model_unique_values2 above. (Warning do not run Model_unique_values2 by itself just the code that is above!)   
ebay_df_sample['OS'].replace (to_replace=['Not Included'], value='NaN', inplace=True)
ebay_df_sample['OS'].replace (to_replace=['windows 11'], value='Windows 11', inplace=True)
ebay_df_sample['OS'].replace (to_replace=['Win 10 Pro 64'], value='Windows 10', inplace=True)
ebay_df_sample['OS'].replace (to_replace=['Windows 10 Pro'], value='Windows 10', inplace=True)
ebay_df_sample['OS'].replace (to_replace=['windows 10 Home 64'], value='Windows 10', inplace=True)


# In[288]:


# I wanted to do hard drive capacity as there was errors with the labels and there were words I thought were unnecessary for the data such as not included and SSD only. 
Model_unique_values3 = ebay_df_sample['Hard Drive Capacity'].unique()
Model_unique_values3.sort()
Model_unique_values3


# In[289]:


# This shows the replacement process where I ran it through Model_unique_values3 above. (Warning do not run Model_unique_values3 by itself just the code that is above!) 
ebay_df_sample['Hard Drive Capacity'].replace (to_replace=['Not Applicable'], value='NaN', inplace=True)
ebay_df_sample['Hard Drive Capacity'].replace (to_replace=['SSD only'], value='SSD Only', inplace=True)
ebay_df_sample['Hard Drive Capacity'].replace (to_replace=['64gb'], value='64 GB', inplace=True)
ebay_df_sample['Hard Drive Capacity'].replace (to_replace=['1tb'], value='1 TB', inplace=True)



# In[290]:


# I wanted to look into SSD I wanted to examine the SSD capacity as there were errors with the label and some words that were necessary to have.
Model_unique_values4 = ebay_df_sample['SSD Capacity'].unique()
Model_unique_values4.sort()
Model_unique_values4


# In[291]:


# I did the same replacement method where I used NaN to show not applicable so it makes it easier to read instead of writing different words. I ran it through Model_Unique_Values4 ((Warning do not run Model_unique_values4 by itself just the code that is above!) )
ebay_df_sample['SSD Capacity'].replace (to_replace=['Not Applicable'], value='NaN', inplace=True)
ebay_df_sample['SSD Capacity'].replace (to_replace=['na'], value='NaN', inplace=True)
ebay_df_sample['SSD Capacity'].replace (to_replace=['NONE'], value='NaN', inplace=True)
ebay_df_sample['SSD Capacity'].replace (to_replace=['1tb'], value='1 TB', inplace=True)
ebay_df_sample['SSD Capacity'].replace (to_replace=['64gb'], value='64 GB', inplace=True)
ebay_df_sample['SSD Capacity'].replace (to_replace=['256SSD'], value='256 GB', inplace=True)


# In[292]:


# I wanted to sort brands as there were models in the brand column that I had to replace in this dataFrame. 
Model_unique_values5 = ebay_df_sample['Brand'].unique()
Model_unique_values5.sort()
Model_unique_values5



# In[293]:


# This shows the brand replacement method that I did previous where I changed the models into the brand they are susposed to be. (Warning do not run Model_unique_values5 by itself just the code that is above!) 
ebay_df_sample['Brand'].replace (to_replace=['Lenovo T440'], value='Lenovo', inplace=True)
ebay_df_sample['Brand'].replace (to_replace=['Dell Inspiron'], value='Dell', inplace=True)



# In[294]:


# After doing all of the replacing for the data wrangling and felt that everything looked excellent and there was not any more replacing and problems with the dataframe, I merge the two csv together into one and created the sample called ebay_df_sample_2
ebay_df_sample_2 = pd.merge(ebay_df_sample,ebayprice_df, on= "Item Number", how= "left") 


# In[295]:


# I ran the sample to see if it worked and what it looked like on python and if there was changes neeeded and from examining it there was some errors I needed to fix for the price. 
ebay_df_sample_2


# In[296]:


# I looked into the prices and I wanted to see if there were any problems with the prices. 
Model_unique_values4 = ebay_df_sample_2['Price'].unique()
Model_unique_values4.sort()
Model_unique_values4



# In[297]:


# From examining the data I noticed there were errors with the prices for these, so what I did was that when I did the replacing method was that I did the prices that were its maximum in this case just to make it easier for me to do the data wrangling. I also did not want to have commas that showed the thousands place so I striped it entirely so it was easier to look at the data.  
ebay_df_sample_2['Price'].replace (to_replace=['$192.00 to $203.05'], value='$203.05', inplace=True)
ebay_df_sample_2['Price'].replace (to_replace=['$324.99 to $799.99'], value='$799.00', inplace=True)
ebay_df_sample_2['Price'].replace (to_replace=['$49.99 to $104.99'], value='$104.99', inplace=True)
ebay_df_sample_2['Price'] = ebay_df_sample_2['Price'].str.replace(',', '')



# In[298]:


Model_unique_values5 = ebay_df_sample_2['Screen Size'].unique()
Model_unique_values5.sort()
Model_unique_values5


# In[299]:


ebay_df_sample_2['Screen Size'].replace (to_replace=['12.5" FHD (1920x1080)'], value='12.5 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['15.6 in FHD'], value='15.6 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['14'], value='14 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['15.6 In'], value='15.6 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['15.6"'], value='15.6 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['11.6"'], value='11.6 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['14 inch'], value='14 in', inplace=True)
ebay_df_sample_2['Screen Size'].replace (to_replace=['14 In'], value='14 in', inplace=True)


# In[300]:


Model_unique_values6 = ebay_df_sample_2['Hard Drive Capacity'].unique()
Model_unique_values6.sort()
Model_unique_values6


# In[301]:


ebay_df_sample_2['Hard Drive Capacity'].replace (to_replace=['SSD Only'], value='1 TB', inplace=True)
ebay_df_sample_2['Hard Drive Capacity'].replace (to_replace=['No HDD'], value='256 TB', inplace=True)
ebay_df_sample_2['Hard Drive Capacity'].replace (to_replace=['SSD Only'], value='1 TB', inplace=True)
ebay_df_sample_2['Hard Drive Capacity'].replace (to_replace=['0'], value='NaN', inplace=True)


# In[302]:


# I saw that there was errors for the processor speed columns as there was a lot of mistakes that needed to be replaced with label corrections 
Model_unique_values6 = ebay_df_sample_2['Processor Speed'].unique()
Model_unique_values6.sort()
Model_unique_values6


# In[303]:


#This showed the replacement process for processor speed and I ran it through Model_unique_values6 ( Warning, run the code that is shown above)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['2.4ghz'], value='2.4 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['5.10 ghz'], value='5.1 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['1.10GHZ'], value='1.1 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['3.1hz'], value='3.1 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['3.9hz'], value='3.9 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['2.4ghz'], value='2.4 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['2.4hz'], value='2.4 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['3.6hz'], value='3.6 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['2.4Ghz'], value='2.4 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['2.8Ghz'], value='2.8 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['1.9 Ghz'], value='1.9 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['2.3Ghz'], value='2.3 GHz', inplace=True)
ebay_df_sample_2['Processor Speed'].replace (to_replace=['4.9Ghz'], value='4.9 GHz', inplace=True)


# In[304]:


# I saw on the csv that there were errrors on the SSD capacity so I had to do some wrangling for this columns so it was easier to read the data in this column. 
Model_unique_values7 = ebay_df_sample_2['SSD Capacity'].unique()
Model_unique_values7.sort()
Model_unique_values7


# In[305]:


# I did not want zero to represent SSD capacity in this case so I replaced it to NaN as it was easier to read in the data. 
ebay_df_sample_2['SSD Capacity'].replace (to_replace=['0'], value='NaN', inplace=True)


# In[306]:


# Save the DataFrame to a CSV file and looked to see if there needs to be more editing to the data. 
ebay_df_sample_2.to_csv('ebay_prices_cleaned.csv', index=False)


# Overall, from making the code for this scenario, some of the key things that were acomplished from working with the data was one to handle missing data. Through handling data using (dropna()) was important to remove with missing data which helps to clean the data. Another thing that was acomplished was the identifying unique values as using (unique()) it helped to identify unique values within columns, this would a business understand certain demographic or even the pricing for this with the laptops. Lastly when I was checking for missing values such as (isna()) and isnull() it helps ensure data quality while preventing flawed decision making. 
# Overall, this would be good for a business because it would help in a variety of ways. One of these ways is through improving decision making, this is because having a well structure data creates accurate insights, which would support better business decisions. Another way this would help business is through data integrity, as with removing poorly formatted data which prevents error in data analysis. Lastly through removing the commas in the pricing, it makes it easier to analyze different prices for the laptops and to examine for any price anomalies and to forecast when examining the data. 
