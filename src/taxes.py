federal = '''Federal income tax rates for 2026
Tax rate	Taxable income threshold
14%	on the portion of taxable income that is $58,523, plus
20.5%	on the portion of taxable income over $58,523 up to $117,045, plus
26%	on the portion of taxable income over $117,045 up to $181,440, plus
29%	on the portion of taxable income over $181,440 up to $258,482, plus
33%	on the portion of taxable income over $258,482'''

Newfoundland_and_Labrador = '''Newfoundland_and_Labrador income tax rates for 2026
Tax rate	Taxable income threshold
8.7%	on the portion of taxable income that is $44,678, plus
14.5%	on the portion of taxable income over $44,678 up to $89,354, plus
15.8%	on the portion of taxable income over $89,354 up to $159,528, plus
17.8%	on the portion of taxable income over $159,528 up to $223,340, plus
19.8%	on the portion of taxable income over $223,340 up to $285,319, plus
20.8%	on the portion of taxable income over $285,319 up to $570,638, plus
21.3%	on the portion of taxable income over $570,638 up to $1,141,275, plus
21.8%	on the portion of taxable income over $1,141,275'''

prince_edward_island = '''Prince_Edward_Island income tax rates for 2026
Tax rate	Taxable income threshold
9.5%	on the portion of taxable income that is $33,928, plus
13.47%	on the portion of taxable income over $33,928 up to $65,820, plus
16.6%	on the portion of taxable income over $65,820 up to $106,890, plus
17.62%	on the portion of taxable income over $106,890 up to $142,250, plus
19%	on the portion of taxable income over $142,250'''

nova_scoatia = '''Nova_Scotia income tax rates for 2026
Tax rate	Taxable income threshold
8.79%	on the portion of taxable income that is $30,995, plus
14.95%	on the portion of taxable income over $30,995 up to $61,991, plus
16.67%	on the portion of taxable income over $61,991 up to $97,417, plus
17.5%	on the portion of taxable income over $97,417 up to $157,124, plus
21%	on the portion of taxable income over $157,124'''

new_brunswick = '''New_Brunswick income tax rates for 2026
Tax rate	Taxable income threshold
9.4%	on the portion of taxable income that is $52,333, plus
14%	on the portion of taxable income over $52,333 up to $104,666 plus
16%	on the portion of taxable income over $104,666 up to $193,861, plus
19.5%	on the portion of taxable income over $193,861'''

ontario = '''Ontario income tax rates for 2026
Tax rate	Taxable income threshold
5.05%	on the portion of taxable income that is $53,891, plus
9.15%	on the portion of taxable income over $53,891 up to $107,785, plus
11.16%	on the portion of taxable income over $107,785 up to $150,000, plus
12.16%	on the portion of taxable income over $150,000 up to $220,000, plus
13.16%	on the portion of taxable income over $220,000'''

manitoba =  '''Manitoba income tax rates for 2026
Tax rate	Taxable income threshold
10.8%	on the portion of taxable income that is $47,000, plus
12.75%	on the portion of taxable income over $47,000 up to $100,000, plus
17.4%	on the portion of taxable income over $100,000'''

saskatchewan = '''Saskatchewan income tax rates for 2026
Tax rate	Taxable income threshold
10.5%	on the portion of taxable income that is $54,532, plus
12.5%	on the portion of taxable income over $54,532 up to $155,805, plus
14.5%	on the portion of taxable income over $155,805'''

alberta = '''Alberta income tax rates for 2026
Tax rate	Taxable income threshold
8%	on the portion of taxable income that is $61,200, plus
10%	on the portion of taxable income over $61,200 up to $154,259, plus
12%	on the portion of taxable income over $154,259 up to $185,111, plus
13%	on the portion of taxable income over $185,111 up to $246,813, plus
14%	on the portion of taxable income over $246,813 up to $370,220, plus
15%	on the portion of taxable income over $370,220
'''

british_columbia = '''British_Columbia income tax rates for 2026
Tax rate	Taxable income threshold
5.06%	on the portion of taxable income that is $50,363, plus
7.7%	on the portion of taxable income over $50,363 up to $100,728, plus
10.5%	on the portion of taxable income over $100,728 up to $115,648, plus
12.29%	on the portion of taxable income over $115,648 up to $140,430, plus
14.7%	on the portion of taxable income over $140,430 up to $190,405, plus
16.8%	on the portion of taxable income over $190,405 up to $265,545, plus
20.5%	on the portion of taxable income over $265,545'''

yukon = '''Yukon income tax rates for 2026
Tax rate	Taxable income threshold
6.4%	on the portion of taxable income that is $58,523, plus
9%	on the portion of taxable income over $58,523 up to $117,045, plus
10.9%	on the portion of taxable income over $117,045 up to $181,440, plus
12.8%	on the portion of taxable income over $181,440 up to $500,000, plus
15%	on the portion of taxable income over $500,000'''

northwest_territories = '''Northwest_Territories income tax rates for 2026
Tax rate	Taxable income threshold
5.9%	on the portion of taxable income that is $53,003, plus
8.6%	on the portion of taxable income over $53,003 up to $106,009, plus
12.2%	on the portion of taxable income over $106,009 up to $172,346, plus
14.05%	on the portion of taxable income over $172,346'''

nunavut = '''Nunavut income tax rates for 2026
Tax rate	Taxable income threshold
4%	on the portion of taxable income that is $55,801, plus
7%	on the portion of taxable income over $55,801 up to $111,602, plus
9%	on the portion of taxable income over $111,602 up to $181,439, plus
11.5%	on the portion of taxable income over $181,439'''


data = [federal, 
        Newfoundland_and_Labrador, 
        prince_edward_island,
        nova_scoatia,
        new_brunswick,
        ontario,
        manitoba, 
        alberta,
        british_columbia,
        yukon,
        northwest_territories,
        nunavut,
        saskatchewan
        ]

labels = '''federal, 
        Newfoundland_and_Labrador, 
        prince_edward_island,
        nova_scoatia,
        new_brunswick,
        ontario,
        manitoba, 
        alberta,
        british_columbia,
        yukon,
        northwest_territories,
        nunavut,
        saskatchewan'''

labels = labels.split("\n")

labels = [label[:len(label)-1] for label in labels] #remove ','


import pandas as pd

tax_data = {}
for i, item in enumerate(data):
    items = item.split("\n")
    province_data = {}
    for idx, item in enumerate(items):


        if idx == 0:
            item = item.split(" ") 
            province = item[0] 
            
        elif idx == 1:
            #empty line
            random = 2


        elif idx == len(items)-1: #last 
            item = item.split(" ")
            rate = item[0]
            rate = rate[:len(rate)-4]
            try:
                rate = float(rate) /100

            except ValueError:
                #NaN 
                random = 2    


            bracket = item[len(item)-1]

            #set upper end for bracket to 10M (Hopefully we hit errors at some point)
            province_data[1000000] = rate


        else: #not last bracket, remove 'over'
            item = item.split(" ")
            rate = item[0]
            rate = rate[:len(rate)-4]
            try:
                rate = float(rate) /100

            except ValueError:
                #NaN 
                random = 2
            
            bracket = item[len(item)-2]
            
            bracket = bracket[1:len(bracket)-1]      

            bracket = bracket.replace(',','')

            try:
                bracket = int(bracket)  
                province_data[bracket] = rate
            except ValueError:
                random = 2  
        
    tax_data[province] = province_data


#uncleaned
df = pd.DataFrame(tax_data)
bracket_data = df.index
#df["tax_bracket"] = bracket_data

#Reset columns so they can MERGE automatically
df.rename(columns={'Federal': 'Federal', 
                   'Newfoundland_and_Labrador': 'Newfoundland and Labrador', 
                   'Prince_Edward_Island':"Prince Edward Island",
                   'Nova_Scotia':'Nova Scotia', 
                   'New_Brunswick': 'New Brunswick', 
                   #'Ontario':, 
                   #'Manitoba', 
                   #'Alberta',
                   'British_Columbia':'British Columbia', 
                   #'Yukon', 
                   'Northwest_Territories':'Northwest Territories', 
                   #'Nunavut',
                   'tax_bracket':'tax_bracket'
                   }, 
                   inplace=True #modify this df
                   )

df = df.transpose()
pronvinces = df.index
df['Province'] = pronvinces
print(df)
print(df.columns)

df_melted = df.melt(id_vars=['Province'], 
                    var_name='tax_bracket',
                    value_name='tax_rate')

df_melted = df_melted.dropna(subset=['tax_rate']).reset_index(drop=True)

df_melted.to_csv("../data/tax_brackets_by_province_transposed.csv", index=True)

