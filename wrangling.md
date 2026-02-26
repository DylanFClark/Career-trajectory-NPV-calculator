# Data Wrangling

Here we will outline transformations applied to datasets such that their format's are accesssible to our analysis. The following datasets we're downloaded in a accessible format, thus minimal preprocessing was nessesairy. 

### Job vacancies and average offered hourly wage by occupation (unit group), quarterly, unadjusted for seasonality

We created a calculated field in tableau workbook. 

(sum of hourly wages / # job postings) => avg hourly wage 


### Labour force characteristics by industry, annual 
### Consumer Price Index by product group, monthly, percentage change, not seasonally adjusted

### tax_brackets_by_province_transposed

We took text data from the Canadian govt website. We extracted values from this data in python, using the src/taxes.py script. 

We then transposed the data into 3 columns. Province, tax_bracket, tax_rate. 

Minimal manual adjustements were required within the data after processing. These included removal of our synthetic $1M tax bracket for Newfoundland and Laborador, as this province had a bracket > 1M and didn't require it. 
