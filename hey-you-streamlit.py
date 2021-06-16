import streamlit as st
import pandas as pd
import numpy as np
import os
import seaborn as sns

st.sidebar.title("EDA on Hey You Data")

option = st.sidebar.selectbox('Objectives', (
    '1. Describe customer behavior over time', 
    '2. Describe customer profile', 
    '3. Describe the impact of the AI system'))

st.sidebar.write(
"""
## About Hey You

## Value proposition:  
### "Make time for what matters"


### Services:
- Order ahead
- Dine in
- Delivery
- Pay through wallet

### Target Market
- App users  
  
App users are able to order ahead (and save on time),
dine in restaurants and pay through the app, 
and get food delivered to them.   

- Restaurant owners (B2B? not sure about the business model)  
  
Restaurant owners can get their processes streamlined through 
Hey You in terms of getting customers, placing orders to the kitchen, 
getting paid for the orders, setting up the logistics of the delivery, 
and marketing through promos and the website blog.
  
  
  
GitHub: maglang/hey-you-analysis
""")

if option == '1. Describe customer behavior over time':
    st.title('Customer Behavior over Time')

    """Hey You app users 
      
      

    Majority of App users use iPhones:
    """

    device_use = pd.DataFrame.from_dict(
        {"Device":["iPhone", "Android", "GCF", "X11", "Windows", "Macintosh", "Tablet"], 
        "Device Users":[1016674.0, 188930.0, 60298.0, 9858.0, 7702.0, 3664.0, 1970.0], 
        "Device Users %": ['78.8672%', '14.6560%', '4.6775%', '0.7647%', '0.7647%', '0.28425', '0.1528%']}
    ).set_index('Device')
    device_use


