#%%
import requests
import pandas as pd
import numpy as np

#%%
def get_sold_prices_per_sql(postcode):

    endpoint = 'https://api.propertydata.co.uk/sold-prices-per-sqf?key=FZWNVHZTZY&postcode='+postcode
    
    try:   
        response = requests.get(endpoint)
        if response.status_code==200:
            return(response.json())
    except error as e:
        print(e)
        
        
    
# %%
data=[]
post_codes=['UB7 7GE','UB10 0AY','UB8 3FG'] #NW10 7YQ
for val in post_codes:
    data.append(get_sold_prices_per_sql(val))


df=pd.DataFrame(data)

# %%
#data is now a list of dictionaries.
#this can be directly be cast as a dataframe
df = pd.concat([df.drop(['data'], axis=1), df['data'].apply(pd.Series)], axis=1)

#%%
#df = pd.concat([df.drop(['raw_data'], axis=1), df['raw_data'].apply(pd.Series)], axis=1)
# %%
#df.info()
#df.columns

# %%
properties_by_pc=[]
for p,i in zip(post_codes,df['raw_data']):
    for j in i:
        properties_by_pc.append(pd.Series(j))
    


# %%
properties_by_pc=pd.DataFrame(properties_by_pc)
properties_by_pc.info()
#properties_by_pc.address[0][-7:]
#%%
properties_by_pc['postcode']=properties_by_pc.address.apply(lambda x:x[-7:])
properties_by_pc['postcode'] =properties_by_pc.postcode.apply(lambda x:"".join(x.split())) 
df['postcode'] =df['postcode'].apply(lambda x:"".join(x.split())) 

#%%
properties_by_pc.to_csv(r"D:\personal files\Real Estate\Properties.csv",index=False)


#%%
post_codes=list(properties_by_pc['postcode'])

#%%
def get_sold_prices_per_sql(postcode):

    endpoint = 'https://api.propertydata.co.uk/demand-rent?key=FZWNVHZTZY&postcode='+postcode
    
    try:   
        response = requests.get(endpoint)
        if response.status_code==200:
            return(response.json())
    except error as e:
        print(e)
        
        
    
# %%
data=[]

for val in post_codes:
    data.append(get_sold_prices_per_sql(val))



# %%
ls=[]
for i in data:
    if i!=None:
        ls.append(i)
# %%
ls
# %%
df=pd.DataFrame(ls)
df['postcode'] =df.postcode.apply(lambda x:"".join(x.split())) 
# %%
df.to_csv(r"D:\personal files\Real Estate\DemandRent_by_Pc.csv",index=False)

# %%
